[app]

# (str) Title of your application
title = Chess Game

# (str) Package name
package.name = chessgame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
#android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (int) Android build tools version to use
android.build_tools_version = 34.0.0

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML arguments:
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Full name including package path of the Java class that implements Python Service
# use that parameter to set custom Java class which extends PythonService
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# Either form may be used, and assets need not be in 'source.include_exts'.
# 1) android.add_assets = source_asset_relative_path
# 2) android.add_assets = source_asset_path:destination_asset_relative_path
#android.add_assets =

# (list) Put these files or directories in the apk res directory.
# The option may be used in three ways, the value may contain one or zero ':'
# Some examples:
# 1) A file to add to resources, legal resource names contain ['a-z','0-9','_']
# android.add_resources = my_icons/all-inclusive.png:drawable/all_inclusive.png
# 2) A directory, here  'legal_icons' must contain resources of one kind
# android.add_resources = legal_icons:drawable
# 3) A directory, here 'legal_resources' must contain one or more directories,
# each of a resource kind:  drawable, xml, etc...
# android.add_resources = legal_resources

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
#android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes
# e.g. android.gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"
#android.add_gradle_repositories =

# (list) packaging options to add
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes
# e.g. android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"
#android.add_packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set it to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the project.properties automatically.)
#android.library_references =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, comma separated
# On android, you can only build for the archs the NDK supports
#android.archs = arm64-v8a, armeabi-v7a, x86_64

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (string)
# android.manifest_placeholders = [activityLabel1:"defaultValue1", activityLabel2:"defaultValue2"]

# (bool) Enable/disable Android compilation with the clang compiler (default for api 23+)
# android.use_clang = True

# (str) Path to a Python file, will be called if the build fails.
# The script should be in the root of your project directory and should implement
# def handle_build_failure():
# android.build_failure_hook = build_failure_handler.py

# (str) name of the directory to look for build recipes (see python-for-android)
# p4a.local_recipes =

# (str) Filename to the hook for p4a
# p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
# p4a.port =

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# "in the future" --use-setup-py is going to be the default behaviour in p4a, right now it is not
# Setting it to "true" will pass --use-setup-py, false will pass --ignore-setup-py
# p4a.setup_py = False

# (str) Command line options to pass to p4a
# p4a.extra_args =


# -----------------------------------------------------------------------------
# iOS specific
# -----------------------------------------------------------------------------

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
#ios.kivy_ios_url = https://github.com/kivy/kivy-ios
#ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
#ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
#ios.ios_deploy_branch = 1.7.0

# (bool) Whether or not to sign the code
#ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the debug version
#ios.codesign.development_team.debug = <hexstring>

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = "iPhone Distribution: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the release version
#ios.codesign.development_team.release = <hexstring>

# (str) URL pointing to .ipa file to be installed
# This option should be used for private repositories
#ios.ipa_url =

# (str) Additional arguments to pass to xcodebuild (if you use xcode)
#ios.extra_args =

# (str) file to include as an intent filter inside the <activity> tag
# use that parameter to provide a filename from where to load your custom XML arguments:
#android.extra_manifest_activity_arguments = ./src/android/extra_manifest_activity_arguments.xml

# (str) Title for the notification channel to use when sending notifications
#android.notification_channel_title = Chess Game Notifications

# (str) Description for the notification channel to use when sending notifications
#android.notification_channel_description = Notifications for the Chess Game app

# (bool) Whether to use the new android packaging system with .aab files instead of .apk
#android.use_aab = False

# (list) list of key=value to set in the buildozer.spec file
# buildozer.global_settings = key1=value1,key2=value2

# (str) Default encoding to be used by the Python interpreter when `str.decode` is invoked without an explicit encoding
#python.default_encoding = utf-8

# (list) Pattern to exclude from the source distribution
#e.g. exclude=*.txt,*.csv
#source.exclude_patterns =

# (str) Path to a requirements file, that will be used if pip doesn't find
# the module locally.
#requirements_file = requirements.txt

# (str) Filename to the build output, as a format string for p4a
#p4a.output_filename =

# -----------------------------------------------------------------------------
# Packaging
# -----------------------------------------------------------------------------

# (str) Packaging format: either 'apk' or 'aab'
android.packaging_format = apk

# (list) Which architectures to include in the package
# e.g. android.archs = armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a, arm64-v8a

# -----------------------------------------------------------------------------
# Release options
# -----------------------------------------------------------------------------

# (bool) Indicate whether the application should be built in release mode
#android.release = 0

# (str) Username to use for signing the release (should match the keystore)
#android.release.keystore.username =

# (str) Password to use for signing the release (should match the keystore)
#android.release.keystore.password =

# (str) Alias to use for signing the release
#android.release.keystore.alias =

# (str) Filename of the keystore to use for signing the release
#android.release.keystore.filename =

# (str) Password for the keystore
#android.release.keystore.storepass =

# (str) Path to the json keystore file for android releases
#android.release.keystore.json =

# -----------------------------------------------------------------------------
# Debug options
# -----------------------------------------------------------------------------

# (bool) Indicate whether the application should be built in debug mode
#android.debug = 1

# (str) Username to use for signing the debug (should match the keystore)
#android.debug.keystore.username =

# (str) Password to use for signing the debug (should match the keystore)
#android.debug.keystore.password =

# (str) Alias to use for signing the debug
#android.debug.keystore.alias =

# (str) Filename of the keystore to use for signing the debug
#android.debug.keystore.filename =

# (str) Password for the keystore
#android.debug.keystore.storepass =

# (str) Path to the json keystore file for android debug builds
#android.debug.keystore.json =