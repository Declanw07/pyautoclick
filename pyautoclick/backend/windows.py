import wmi
import psutil


class Process:
    """
    Class to encapsulate a currently running Win32 Process.
    """
    # __slots__ = ['_name', '_pid']

    def __init__(self, name, pid):
        self._name = name
        self._pid = pid
        # self._exe_path = exe_path

    def __repr__(self):
        return 'Process("{_name}", PID={_pid})'.format(**self.__dict__)

    @property
    def name(self):
        return self._name

    @property
    def pid(self):
        return self._pid

    # @property
    # def exe_path(self):
    #     return self._exe_path

    @property
    def is_alive(self):
        return psutil.pid_exists(self._pid)


def get_processes():
    """
    Returns a list Process objects which currently running.

    kwargs:
        name (str):         Name of a process

    Returns:
        processes (dict):   A dict mapping of process name to PID
                                E.g: {u'svchost.exe': 10145}
    """
    processes = wmi.WMI().InstancesOf('Win32_Process')
    process_objects = [
        Process(
            name=process.Properties_('Name').Value,
            pid=process.Properties_('ProcessId').Value
        ) for process in processes
    ]
    return process_objects
