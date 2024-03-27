# juic3b0x 2024 - Makefile for installing directory tree into prefix /data/data/io.neoterm/files/usr

# Define the destination prefix
prefix = /data/data/io.neoterm/files/usr

# Define the directories to be installed
dirs = bin control-files-dir etc lib sbin share doc man python3

# Define the installation directory for each directory
bin_PROGRAMS = $(prefix)/bin/command-not-found
sbin_PROGRAMS = $(prefix)/sbin/update-command-not-found
man8_MANS = $(prefix)/share/man/man8/update-command-not-found.8.gz
doc_DATA = $(prefix)/share/doc/command-not-found/README.md
python3_DATA = $(prefix)/share/python3/runtime.d/command-not-found.rtupdate

# Define the installation rules for each file
install-data-local:
    mkdir -p $(DESTDIR)$(prefix)/share/command-not-found
    cp -r share/command-not-found/* $(DESTDIR)$(prefix)/share/command-not-found/
    mkdir -p $(DESTDIR)$(prefix)/lib/command-not-found
    cp -r lib/command-not-found/* $(DESTDIR)$(prefix)/lib/command-not-found/
    mkdir -p $(DESTDIR)$(prefix)/etc/apt/apt.conf.d
    cp -r etc/apt/apt.conf.d/* $(DESTDIR)$(prefix)/etc/apt/apt.conf.d/
    mkdir -p $(DESTDIR)$(prefix)/etc/zsh_command_not_found
    cp -r etc/zsh_command_not_found/* $(DESTDIR)$(prefix)/etc/zsh_command_not_found/
    mkdir -p $(DESTDIR)$(prefix)/share/doc/command-not-found
    cp -r doc/command-not-found/* $(DESTDIR)$(prefix)/share/doc/command-not-found/
    mkdir -p $(DESTDIR)$(prefix)/share/man/man8
    cp -r man/man8/* $(DESTDIR)$(prefix)/share/man/man8/
    chmod 755 $(DESTDIR)$(prefix)/bin/command-not-found
    chmod 755 $(DESTDIR)$(prefix)/sbin/update-command-not-found

# Define the uninstallation rules for each file
uninstall-local:
    rm -rf $(DESTDIR)$(prefix)/bin/command-not-found
    rm -rf $(DESTDIR)$(prefix)/sbin/update-command-not-found
    rm -rf $(DESTDIR)$(prefix)/share/man/man8/update-command-not-found.8.gz
    rm -rf $(DESTDIR)$(prefix)/share/doc/command-not-found/README.md
    rm -rf $(DESTDIR)$(prefix)/share/python3/runtime.d/command-not-found.rtupdate

# Define the installation targets
install-data-hook: install-data-local

# Define the uninstallation targets
uninstall-hook: uninstall-local

# Define the targets for installation and uninstallation
install-data-am: install-data-hook
uninstall-am: uninstall-hook

# Define the phony targets
.PHONY: install-data-hook uninstall-hook install-data-am uninstall-am
