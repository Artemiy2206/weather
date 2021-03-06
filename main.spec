# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('design/main.ui', 'design'),
            ('design/main_detail.ui', 'design'),
            ('design/auth.ui', 'design'),
            ('design/cabinet.ui', 'design'),
            ('design/register.ui', 'design'),
            ('files/pyweather.db', 'files'),
            ('files/russian-cities.json', 'files'),
            ('files/setting.py', 'files'),
            ('image/logo.png', 'image'),
            ('image/01d.png', 'image'),
            ('image/02d.png', 'image'),
            ('image/03d.png', 'image'),
            ('image/04d.png', 'image'),
            ('image/09d.png', 'image'),
            ('image/10d.png', 'image'),
            ('image/11d.png', 'image'),
            ('image/13d.png', 'image'),
            ('image/50d.png', 'image'),
            ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PyWeather',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False, icon='image/logo.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
