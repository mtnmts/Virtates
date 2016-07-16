Design
=======


Provide a simple, easy, turn-key solution for managing "Cloud" providers.


Guidelines
------------
- Simple Web UI
- Support libvirt
- Simple setup (docker?)
  

Overview
---------

- Generalized cloud providers, mist.io has the right idea but i don't like their implementation

    + Clouds should be more tightly bound to the cloud representation for execution of operations

    + Start/Stop/Clone etc does methods are owned by the VM, but should be agnostic to implementation

    + Supported/Unsupported is good enough (?)

- Easy specialization

    + It shouldn't be too hard to create different pages and management interfaces for various clouds beyond the global features that all providers support

    + How should we go about this?
      
- Desired Features

	+ Monitoring
		
		+ Polling VM and Hypervisor(If hypervisor makes sense in the providers context) should be a first class feature

		+ Network, IO, CPU

      
- Security

    + Security should be built-in well enough that someone can spin up a docker instance, get credentials and open one port for web and not expect to get hacked

    + User/Password definitely, perhaps also oAuth?

- Persistance

    + Let users export and import all the settings in one convinient manner

    + Format should make sense, lets not pickle objects, cross-versioning at least from some point

    + DB? SQL? Just nothing bloated... (sqlite perhaps), not sure it's necessary persistently, maybe just for monitoring.