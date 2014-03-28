# This makefile will be used to generate the virtual environment for the blog. The reason for using this is because many of us are
# either running Unix (e.g. Linux or Mac) systems, or if we are on Windows may have MinGW or Cygwin

# The location of the virtualenv
VIRTENV_DIR=ENV

all: clean init activateEnv loadModules

clean:
	# Clean previous environment if one exists
	@rm -rf $(VIRTENV_DIR)
	@echo cleaned previous environments if they existed

init:
	@virtualenv $(VIRTENV_DIR)
	@echo Created the base virtual environment

activateEnv:
	# runs the activate script inside of the environment
	# THe command should run for both windows and unix
	@$(VIRTENV_DIR)/Scritpts/activate

loadModules: loadDjango
	@echo
	@echo Finished loading modules
	@echo Enjoy!
	
loadDjango:
	# This might differ on your system - I am running the github version of django for now, and it installed from the github repo
	# using a different command , for the newer features, which means that it is
	# django 1.7. Let me know if this has to absolutely be changed.
	@pip install django
	@echo Finished loading Django