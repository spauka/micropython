include("../manifest.py")
freeze("modules", "quokka.py", opt=3)
freeze("modules", (
    "drivers/__init__.py",
    "drivers/imu.py",
    "drivers/mpu9250.py",
    "drivers/quokka_radio.py",
    "drivers/series.py",
    "drivers/ssd1306.py",
    "drivers/vector3d.py"),
    opt=3
)