from __future__ import absolute_import 

import os
import commands
from cloudagent.celery import celery

target="/var/tenriolacloud"

@celery.task
def init_cloud(mac, password, memory, hdd, name, template_path):
	destination = "%s/images/%s.img" %(target, name)
	commands.getoutput("sudo cp %s %s" %(template_path, destination)) #copy template
	
	
@celery.task
def start_cloud(nama):
	commands.getoutput("sudo virsh start %s" % nama)
	return "%s turned ON" % nama

@celery.task
def stop_cloud(nama):
	commands.getoutput("sudo virsh shutdown %s" % nama)
	return "%s shutted down" % nama

@celery.task 
def reboot_cloud(nama):
	commands.getoutput("sudo virsh reboot %s" % nama)
	return "%s rebooted" % nama

@celery.task
def remove_cloud(nama):
	commands.getoutput("sudo virsh destroy %s" % nama)
	commands.getoutput("sudo virsh undefine %s" % nama)
	return "%s removed" % nama

@celery.task
def get_cloud_status(nama)
	
