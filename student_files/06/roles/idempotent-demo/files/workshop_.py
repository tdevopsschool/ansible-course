import signal
import os
import sys
from argparse import ArgumentParser
from time import sleep


# TODO: create socket create/delete func

class SignalHandler:
    signal_received = False

    def __init__(self):
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        signal.signal(signal.SIGINT, self.exit_gracefully)

    def exit_gracefully(self, *_):
        self.signal_received = True


class SocketFile:
    """Dummy socket file context manager class."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        """Create a dummy socket file."""
        try:
            with open(self.path, 'w+'):
                pass
        except IOError:
            sys.stderr.write('Something went horribly wrong')
            sys.exit(1)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Delete dummy socket file if it exits."""
        if os.path.exists(self.path):
            try:
                os.remove(self.path)
            except OSError:
                sys.stderr.write('Something went horribly wrong')
                sys.exit(1)


class WorkshopApplication:
    def __init__(self, delay=10, valid=True):
        self._socket_file_path = '/tmp/workshop.sock'
        self._config_file_path = '/tmp/workshop.conf'
        self._startup_delay = delay
        self._config_validity = valid

        command_choices = ['generate', 'validate', 'run']
        parser = ArgumentParser(description='Example application for Ansible workshop')
        parser.add_argument('command', choices=command_choices, default='run', nargs='?', help='Command to execute')
        self.command = parser.parse_args().command

    def _create_config(self):
        """Create configuration file, exit if it exists"""
        if os.path.exists(self._config_file_path):
            exit('Config file already exists')
        try:
            with open(self._config_file_path, 'w+') as config:
                config.write(str(int(self._config_validity)))
        except IOError:
            exit('Something went horribly wrong')

    def _validate_config(self):
        """Exit with error if boolean value inside the config file is false"""
        if os.path.exists(self._config_file_path):
            try:
                with open(self._config_file_path, 'r') as config:
                    if not bool(int(config.read())):
                        exit('Config file is invalid')
                    print('Config file is valid')
            except IOError:
                exit('Something went horribly wrong')
        else:
            exit('Config file not found')

    def run(self):
        """Run application according to command given."""
        if self.command == 'generate':
            self._create_config()

        if self.command == 'validate':
            self._validate_config()

        if self.command == 'run':
            self._validate_config()
            signal_handler = SignalHandler()
            print('Starting up')

            # Check for interrupt signal during startup delay
            for _ in range(self._startup_delay):
                if signal_handler.signal_received:
                    exit(0)
                sleep(1)

            # Sleep indefinitely and listen for the interrupt signal
            with SocketFile(self._socket_file_path):
                while True:
                    if signal_handler.signal_received:
                        exit(0)
                    sleep(1)
