'''
Description: 
Version: 1.0
Autor: laijiatao
Date: 2023-07-16 11:19:17
LastEditors: laijiatao
LastEditTime: 2023-07-25 23:20:44
'''
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:762683@127.0.0.1:3308/flask_news?charset=utf8'
app.config['SECRET_KEY'] = 'this is a random key string'
db = SQLAlchemy(app)


log_txt = '''
--------- beginning of system
06-26 15:18:59.546  1513  1513 I vold    : Vold 3.0 (the awakening) firing up
06-26 15:18:59.546  1513  1513 V vold    : Detected support for: ext4 vfat
06-26 15:18:59.551  1513  1513 W vold    : Failed to LOOP_GET_STATUS64 /dev/block/loop5: No such device or address
06-26 15:18:59.581  1513  1513 W vold    : Failed to LOOP_GET_STATUS64 /dev/block/loop1: No such device or address
06-26 15:18:59.621  1513  1513 W vold    : Failed to LOOP_GET_STATUS64 /dev/block/loop6: No such device or address
06-26 15:18:59.662  1513  1513 W vold    : Failed to LOOP_GET_STATUS64 /dev/block/loop2: No such device or address
06-26 15:18:59.700  1513  1513 W vold    : Failed to LOOP_GET_STATUS64 /dev/block/loop4: No such device or address
06-26 15:18:59.810  1513  1513 W vold    : Failed to LOOP_GET_STATUS64 /dev/block/loop0: No such device or address
06-26 15:18:59.841  1513  1513 W vold    : Failed to LOOP_GET_STATUS64 /dev/block/loop7: No such device or address
06-26 15:18:59.880  1513  1513 W vold    : Failed to LOOP_GET_STATUS64 /dev/block/loop3: No such device or address
06-26 15:18:59.915  1513  1513 D vold    : VoldNativeService::start() completed OK
06-26 15:18:59.932  1513  1517 D vold    : e4crypt_init_user0
06-26 15:18:59.933  1513  1517 D vold    : e4crypt_prepare_user_storage for volume null, user 0, serial 0, flags 1
06-26 15:18:59.933  1513  1517 D vold    : Preparing: /data/system/users/0
06-26 15:18:59.933  1513  1516 I vold    : Found disk at /devices/pci0000:00/0000:00:08.0/virtio5/block/vdf but delaying scan due to secure keyguard
06-26 15:18:59.933  1513  1517 D vold    : Preparing: /data/misc/profiles/cur/0
06-26 15:18:59.933  1513  1517 D vold    : Preparing: /data/system_de/0
06-26 15:18:59.933  1513  1517 D vold    : Preparing: /data/misc_de/0
06-26 15:18:59.933  1513  1517 D vold    : Preparing: /data/vendor_de/0
06-26 15:18:59.933  1513  1517 D vold    : Preparing: /data/user_de/0
06-26 15:18:59.934  1513  1517 V vold    : /system/bin/vold_prepare_subdirs
06-26 15:18:59.935  1513  1517 V vold    :     prepare
06-26 15:18:59.935  1513  1517 V vold    :     0
06-26 15:18:59.935  1513  1517 V vold    :     1
06-26 15:18:59.949  1513  1517 D vold    : e4crypt_unlock_user_key 0 serial=0 token_present=0
06-26 15:18:59.949  1513  1517 E vold    : Failed to chmod /data/system_ce/0: No such file or directory
06-26 15:18:59.949  1513  1517 E vold    : Failed to chmod /data/misc_ce/0: No such file or directory
06-26 15:18:59.949  1513  1517 E vold    : Failed to chmod /data/media/0: No such file or directory
06-26 15:19:00.225  1513  1590 I Cryptfs : cryptfs_check_passwd
06-26 15:19:00.227  1513  1590 D Cryptfs : crypt_ftr->fs_size = 1638400
06-26 15:19:00.227  1513  1590 I Cryptfs : Using scrypt for cryptfs KDF
06-26 15:19:00.393  1572  1572 I android.hardware.wifi@1.0-service: Wifi Hal is booting up...
06-26 15:19:00.813  1513  1590 I Cryptfs : Extra parameters for dm_crypt: 1 allow_discards
06-26 15:19:00.822  1513  1516 D vold    : Disk at 252:0 changed
06-26 15:19:00.978  1513  1590 I Cryptfs : Password matches
06-26 15:19:00.980  1513  1590 D Cryptfs : test_mount_encrypted_fs(): Master key saved
06-26 15:19:00.990  1513  1590 I vold    : List of Keymaster HALs found:
06-26 15:19:00.990  1513  1590 I vold    : Keymaster HAL #1: SoftwareKeymasterDevice from Google SecurityLevel: SOFTWARE HAL : android.hardware.keymaster@3.0::IKeymasterDevice instance default
06-26 15:19:00.990  1513  1590 I vold    : Using SoftwareKeymasterDevice from Google for encryption.  Security level: SOFTWARE, HAL: android.hardware.keymaster@3.0::IKeymasterDevice/default
06-26 15:19:00.990  1513  1590 D Cryptfs : Password is default - restarting filesystem
06-26 15:19:01.032  1513  1590 D Cryptfs : unmounting /data succeeded
06-26 15:19:01.036  1513  1590 I vold    : [libfs_mgr]superblock s_max_mnt_count:65535,/dev/block/dm-0
06-26 15:19:01.037  1513  1590 I vold    : [libfs_mgr]Filesystem on /dev/block/dm-0 was not cleanly shutdown; state flags: 0x1, incompat feature flags: 0x46
06-26 15:19:01.315  1513  1590 I vold    : [libfs_mgr]check_fs(): mount(/dev/block/dm-0,/data,ext4)=0: Success
06-26 15:19:01.354  1513  1590 I vold    : [libfs_mgr]check_fs(): unmount(/data) succeeded
06-26 15:19:01.355  1513  1590 I vold    : [libfs_mgr]Running /system/bin/e2fsck on /dev/block/dm-0
06-26 15:19:01.601  1513  1590 I vold    : [libfs_mgr]e2fsck returned status 0x100
06-26 15:19:01.612  1513  1590 I vold    : [libfs_mgr]__mount(source=/dev/block/dm-0,target=/data,type=ext4)=0: Success
06-26 15:19:01.612  1513  1590 D Cryptfs : Just triggered post_fs_data
06-26 15:19:01.649  1513  1515 D vold    : e4crypt_init_user0
06-26 15:19:01.649  1513  1515 D vold    : e4crypt_prepare_user_storage for volume null, user 0, serial 0, flags 1
06-26 15:19:01.649  1513  1515 D vold    : Preparing: /data/system/users/0
06-26 15:19:01.649  1513  1515 D vold    : Preparing: /data/misc/profiles/cur/0
06-26 15:19:01.650  1513  1515 D vold    : Preparing: /data/system_de/0
06-26 15:19:01.651  1513  1515 D vold    : Preparing: /data/misc_de/0
06-26 15:19:01.652  1513  1515 D vold    : Preparing: /data/vendor_de/0
06-26 15:19:01.652  1513  1515 D vold    : Preparing: /data/user_de/0
06-26 15:19:01.653  1513  1515 V vold    : /system/bin/vold_prepare_subdirs
06-26 15:19:01.653  1513  1515 V vold    :     prepare
06-26 15:19:01.653  1513  1515 V vold    :     
06-26 15:19:01.653  1513  1515 V vold    :     0
06-26 15:19:01.653  1513  1515 V vold    :     1
06-26 15:19:01.667  1513  1515 D vold    : e4crypt_unlock_user_key 0 serial=0 token_present=0
06-26 15:19:01.691  1513  1590 D Cryptfs : post_fs_data done
06-26 15:19:01.692  1513  1590 D Cryptfs : Just triggered restart_framework
06-26 15:19:01.987  1694  1694 I wificond: wificond is starting up...
06-26 15:19:02.140  1685  1685 I installd: installd firing up
06-26 15:19:03.232  1681  1681 D Zygote32Timing: BeginIcuCachePinning took to complete: 46ms
06-26 15:19:03.721  1681  1681 D Zygote32Timing: PreloadClasses took to complete: 489ms
06-26 15:19:03.829  1681  1681 D Zygote32Timing: PreloadResources took to complete: 107ms
06-26 15:19:03.864  1681  1681 D Zygote32Timing: ZygotePreload took to complete: 679ms
06-26 15:19:03.873  1681  1681 D Zygote32Timing: PostZygoteInitGC took to complete: 9ms
06-26 15:19:03.873  1681  1681 D Zygote32Timing: ZygoteInit took to complete: 694ms
06-26 15:19:04.001  1819  1819 I SystemServer: InitBeforeStartServices
06-26 15:19:04.002  1819  1819 I SystemServer: Entered the Android system server!
06-26 15:19:04.162  1819  1819 D SystemServerTiming: InitBeforeStartServices took to complete: 161ms
06-26 15:19:04.162  1819  1819 I SystemServer: StartServices
06-26 15:19:04.162  1819  1819 I SystemServer: Reading configuration...
06-26 15:19:04.162  1819  1819 I SystemServer: ReadingSystemConfig
06-26 15:19:04.164  1819  1819 D SystemServerTiming: ReadingSystemConfig took to complete: 2ms
06-26 15:19:04.164  1819  1819 I SystemServer: StartInstaller
06-26 15:19:04.164  1819  1819 I SystemServiceManager: Starting com.android.server.pm.Installer
06-26 15:19:04.165  1819  1832 D SystemServerInitThreadPool: Started executing ReadingSystemConfig
06-26 15:19:04.169  1819  1819 D SystemServerTiming: StartInstaller took to complete: 5ms
06-26 15:19:04.169  1819  1819 I SystemServer: DeviceIdentifiersPolicyService
06-26 15:19:04.169  1819  1819 I SystemServiceManager: Starting com.android.server.os.DeviceIdentifiersPolicyService
06-26 15:19:04.171  1819  1819 D SystemServerTiming: DeviceIdentifiersPolicyService took to complete: 2ms
06-26 15:19:04.171  1819  1819 I SystemServer: StartActivityManager
06-26 15:19:04.171  1819  1819 I SystemServiceManager: Starting com.android.server.am.ActivityManagerService$Lifecycle
06-26 15:19:04.197  1819  1819 I ActivityManager: Memory class: 384
06-26 15:19:04.207  1819  1832 D SystemServerInitThreadPool: Finished executing ReadingSystemConfig
06-26 15:19:04.216  1819  1819 D BatteryStatsImpl: Reading daily items from /data/system/batterystats-daily.xml
06-26 15:19:04.230  1819  1840 E BatteryExternalStatsWorker: no controller energy info supplied for telephony
06-26 15:19:04.233  1819  1840 I KernelUidCpuFreqTimeReader: mPerClusterTimesAvailable=false
06-26 15:19:04.235  1819  1840 W KernelCpuProcReader: File not exist: /proc/uid_cpupower/time_in_state
06-26 15:19:04.235  1819  1840 W KernelCpuProcReader: File not exist: /proc/uid_cpupower/concurrent_active_time
06-26 15:19:04.236  1819  1840 W KernelCpuProcReader: File not exist: /proc/uid_cpupower/concurrent_policy_time
06-26 15:19:04.236  1819  1840 E KernelCpuSpeedReader: Failed to read cpu-freq: /sys/devices/system/cpu/cpu0/cpufreq/stats/time_in_state (No such file or directory)
06-26 15:19:04.236  1819  1840 W KernelMemoryBandwidthStats: No kernel memory bandwidth stats available
06-26 15:19:04.252  1819  1819 W AppOps  : Unknown attribute in 'op'  : n
06-26 15:19:04.256  1819  1819 I chatty  : uid=1000 system_server identical 163 lines
06-26 15:19:04.256  1819  1819 W AppOps  : Unknown attribute in 'op' tag: n
06-26 15:19:04.266  1819  1819 I IntentFirewall: Read new rules (A:0 B:0 S:0)
06-26 15:19:04.277  1819  1819 D AppOps  : AppOpsService published
06-26 15:19:04.277  1819  1819 D SystemServerTiming: StartActivityManager took to complete: 106ms
06-26 15:19:04.277  1819  1819 I SystemServer: StartPowerManager
06-26 15:19:04.277  1819  1819 I SystemServiceManager: Starting com.android.server.power.PowerManagerService
06-26 15:19:04.288  1819  1819 D SystemServerTiming: StartPowerManager took to complete: 11ms
06-26 15:19:04.288  1819  1819 I SystemServer: InitPowerManagement
06-26 15:19:04.290  1819  1819 D SystemServerTiming: InitPowerManagement took to complete: 2ms
06-26 15:19:04.290  1819  1819 I SystemServer: StartRecoverySystemService
06-26 15:19:04.290  1819  1819 I SystemServiceManager: Starting com.android.server.RecoverySystemService
06-26 15:19:04.291  1819  1819 D SystemServerTiming: StartRecoverySystemService took to complete: 1ms
06-26 15:19:04.293  1819  1819 W RescueParty: Failed to determine if device was on USB
06-26 15:19:04.293  1819  1819 W RescueParty: java.io.FileNotFoundException: /sys/class/android_usb/android0/state (No such file or directory)
06-26 15:19:04.293  1819  1819 W error:   at java.io.FileInputStream.open0(Native Method)
06-26 15:19:04.293  1819  1819 W Error:   at java.io.FileInputStream.open(FileInputStream.java:231)
06-26 15:19:04.293  1819  1819 W ERROR:   at java.io.FileInputStream.<init>(FileInputStream.java:165)
06-26 15:19:04.293  1819  1819 W RescueParty:   at android.os.FileUtils.readTextFile(FileUtils.java:514)
06-26 15:19:04.293  1819  1819 W RescueParty:   at com.android.server.RescueParty.isUsbActive(RescueParty.java:348)
06-26 15:19:04.293  1819  1819 W RescueParty:   at com.android.server.RescueParty.isDisabled(RescueParty.java:88)
06-26 15:19:04.293  1819  1819 W RescueParty:   at com.android.server.RescueParty.noteBoot(RescueParty.java:107)
06-26 15:19:04.293  1819  1819 W RescueParty:   at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:587)
06-26 15:19:04.293  1819  1819 W RescueParty:   at com.android.server.SystemServer.run(SystemServer.java:429)
06-26 15:19:04.293  1819  1819 W RescueParty:   at com.android.server.SystemServer.main(SystemServer.java:294)
06-26 15:19:04.293  1819  1819 W RescueParty:   at java.lang.reflect.Method.invoke(Native Method)
06-26 15:19:04.293  1819  1819 W RescueParty:   at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:493)
06-26 15:19:04.293  1819  1819 W RescueParty:   at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:838)
06-26 15:19:04.296  1819  1819 W RescueParty: Noticed 1 events for UID 0 in last 7 sec
06-26 15:19:04.296  1819  1819 I SystemServer: StartLightsService
06-26 15:19:04.296  1819  1819 I SystemServiceManager: Starting com.android.server.lights.LightsService
06-26 15:19:04.297  1819  1819 D SystemServerTiming: StartLightsService took to complete: 1ms
06-26 15:19:04.297  1819  1819 I SystemServer: StartSidekickService
06-26 15:19:04.297  1819  1819 D SystemServerTiming: StartSidekickService took to complete: 0ms
06-26 15:19:04.297  1819  1819 I SystemServer: StartDisplayManager
06-26 15:19:04.297  1819  1819 I SystemServiceManager: Starting com.android.server.display.DisplayManagerService
06-26 15:19:04.301  1819  1819 D SystemServerTiming: StartDisplayManager took to complete: 4ms
06-26 15:19:04.301  1819  1819 I SystemServer: WaitForDisplay
06-26 15:19:04.301  1819  1819 I SystemServiceManager: Starting phase 100
echo "Hello, world!"
while true
do
    sleep 2
done
'''

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/logFiles')
def log_files():
    menu = [
        {'name': 'masterlogfile', 'url': '/logFiles/masterlogfile'},
        {'name': 'slavelogfile', 'url': '/logFiles/slavelogfile'},
        {'name': 'xxx', 'url': '/menu3'}
    ]
    return render_template('log_files.html', menu=menu, log_txt=log_txt)


@app.route('/logFiles/masterlogfile')
def master_log_files():
    menu = [
        {'name': 'masterlogfile', 'url': '/logFiles/masterlogfile'},
        {'name': 'slavelogfile', 'url': '/logFiles/slavelogfile'},
        {'name': 'xxx', 'url': '/menu3'}
    ]
    #<a href="/index">Home</a>
    headers = ['Product', 'Price']
    items = [
        ['Apple', 1.00],
        ['Banana', 0.50]
    ]
    
    return render_template('log_files.html', menu=menu, headers=headers, items=items)


@app.route('/errorParse')
def error_parse():
    menu = [
        {'name': '容器复位', 'url': '/menu1'}
    ]
    return render_template('error_parse.html', menu=menu)
