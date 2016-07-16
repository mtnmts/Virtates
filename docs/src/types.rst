Types
======

Legend
--------
- Name: Type - {Members/Functions/Methods/Etc} # Notes
- member @method !abstract_method $class &type


Cloud
------
- VMState - Enum {On, Off, Paused, Running, Unknown, Error}
- Status: {state: &VMState, stats: &stats} 
- Stats - Class {status: &Status, stuff_that_holds_polling_data} # This is the statistics from polling, VMState may sit in here and not in status
- Cloud: Abstract Class - {!get_vm, !start_vm, !stop_vm, !poll_vm, !migrate_vm, !pause_vm, !resume_vm} # Generic abstract cloud
- VM: Class - {cloud : &Cloud, cs_data : &dict, friendly_name, uuid, status: &Stats, wlock: Lock} # cs_data - cloud specific data that Cloud may need, access needs to be transactional(?)
- [Libvirt|ESX|AWS]Cloud - Subclass $Cloud - {} # Implement all of Cloud functionalities
 

Notes
------
