all:

install:
	mkdir -p $(DESTDIR)/opt/45drives/serial45d
	mkdir -p $(DESTDIR)/usr/bin
	cp -a src/fakeroot/opt/45drives/serial45d/* $(DESTDIR)/opt/45drives/serial45d
ifdef SERIAL_VERSION
	echo $(SERIAL_VERSION) > $(DESTDIR)/opt/45drives/serial45d/configs/version
endif
	ln -sf /opt/45drives/serial45d/serial45d $(DESTDIR)/usr/bin/serial45d

uninstall:
	rm -rf $(DESTDIR)/opt/45drives/serial45d
	rmdir /opt/45drives --ignore-fail-on-non-empty