MCU_SERIES = MIMXRT1011
MCU_VARIANT = MIMXRT1011DAE5A

JLINK_PATH = /media/RT1010-EVK/

deploy: $(BUILD)/firmware.bin
	cp $< $(JLINK_PATH)
