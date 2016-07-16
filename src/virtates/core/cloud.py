# I'm just a little black rain cloud
# Hovering under the honey tree
# I'm just a little black rain cloud
# Pay no attention to little me

from abc import ABCMeta, abstractmethod


class Cloud(metaclass=ABCMeta):
    @abstractmethod
    def connect():
        pass

    @abstractmethod
    def disconnect():
        pass

    @abstractmethod
    def is_connected():
        pass

    @abstractmethod
    def getVMs(query):
        """ Returns all VM's, with optional freetext filter query """
        pass

    @abstractmethod
    def getVM(query):
        """ Returns one VM (or none...) """
        pass

    @abstractmethod
    def PauseVM(vm):
        pass

    @abstractmethod
    def ResumeVM(vm):
        pass

    @abstractmethod
    def StopVM(force, vm):
        pass

    @abstractmethod
    def StartVM(vm):
        pass

    @abstractmethod
    def RestartVM(force, vm):
        pass

    @abstractmethod
    def PollVM(vm):
        """ This returns some sort of datapoint """
        pass


class LibvirtCloud(Cloud):
    """ Local and remote implementations will exist """
    @abstractmethod
    def _libvirt_api(libvirt_cmd):
        pass


class LocalLibvirtCloud(LibvirtCloud):
    pass


class RemoteSSHLibvirtCloud(LibvirtCloud):
    pass
