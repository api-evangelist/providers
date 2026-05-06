---
aid: analog-devices
url: https://raw.githubusercontent.com/api-evangelist/analog-devices/refs/heads/main/apis.yml
modified: '2026-04-19'
name: Analog Devices
description: Analog Devices (ADI) is a global semiconductor company designing high-performance analog, mixed-signal, and digital signal processing integrated circuits for industrial, communications, automotive, and consumer markets. ADI provides developer tools through its CodeFusion Studio embedded development environment and the ADI Developer Portal. ADI's APIs are primarily embedded software APIs for microcontrollers and DSPs via the libiio library for Linux Industrial I/O devices, pyadi-iio Python interfaces, and security APIs within the ADI Assure Trusted Edge Security Architecture. The company also maintains the no-OS driver library for bare-metal embedded systems.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Embedded Systems
  - Hardware
  - IoT
  - Semiconductor
  - Signal Processing
apis:
  - aid: analog-devices:libiio-api
    name: Analog Devices libiio API
    description: The libiio library provides a cross-platform C API for interfacing with Linux Industrial I/O (IIO) devices including ADCs, DACs, and RF transceivers. It supports local and remote device access via a network daemon, enabling developers to control ADI hardware from Linux and other host platforms.
    tags:
      - Embedded Systems
      - Hardware Interface
      - IIO
      - Linux
      - Signal Processing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://github.com/analogdevicesinc/libiio
    humanURL: https://analogdevicesinc.github.io/libiio/
    properties:
      - url: https://analogdevicesinc.github.io/libiio/
        type: Documentation
      - url: https://github.com/analogdevicesinc/libiio
        type: GitHubRepository
  - aid: analog-devices:pyadi-iio-api
    name: Analog Devices PyADI-IIO Python API
    description: PyADI-IIO provides Python interfaces for ADI hardware with IIO drivers, enabling Python developers to interact with ADI evaluation boards and production hardware. It abstracts libiio with device-specific high-level interfaces for transceivers, converters, and sensors.
    tags:
      - ADC
      - Embedded Systems
      - Hardware
      - Python
      - RF
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://github.com/analogdevicesinc/pyadi-iio
    humanURL: https://analogdevicesinc.github.io/pyadi-iio/
    properties:
      - url: https://analogdevicesinc.github.io/pyadi-iio/
        type: Documentation
      - url: https://github.com/analogdevicesinc/pyadi-iio
        type: GitHubRepository
      - url: https://pypi.org/project/pyadi-iio/
        type: SDK
  - aid: analog-devices:codefusion-studio
    name: Analog Devices CodeFusion Studio
    description: CodeFusion Studio is ADI's embedded software development environment built on Visual Studio Code for ADI microcontrollers and DSPs. It provides graphical system configuration, code generation, debugging, and security APIs for the ADI Assure Trusted Edge Security Architecture. Initially supports MAX32690 and ADSP-SC5xx processor families.
    tags:
      - Embedded Development
      - IDE
      - Microcontrollers
      - Security
      - VSCode
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://developer.analog.com
    humanURL: https://developer.analog.com/solutions/codefusionstudio
    properties:
      - url: https://developer.analog.com/solutions/codefusionstudio
        type: Documentation
      - url: https://developer.analog.com/docs/codefusion-studio/1.0.2/
        type: APIReference
      - url: https://github.com/analogdevicesinc/codefusion-studio
        type: GitHubRepository
      - url: https://marketplace.visualstudio.com/items?itemName=AnalogDevices.cfs-ide
        type: SDK
common:
  - type: Portal
    url: https://www.analog.com
  - type: DeveloperPortal
    url: https://developer.analog.com
  - type: Documentation
    url: https://www.analog.com/en/software.html
  - type: GitHubOrganization
    url: https://github.com/analogdevicesinc
  - type: Blog
    url: https://www.analog.com/en/resources/media-center/analog-dialogue.html
  - type: Support
    url: https://ez.analog.com/
  - type: Features
    data:
      - name: Linux IIO Interface
        description: libiio library for accessing Linux Industrial I/O devices over USB, network, and local interfaces.
      - name: Python Hardware Interfaces
        description: PyADI-IIO provides Pythonic device-specific APIs for ADI transceivers, converters, and sensors.
      - name: Embedded Security APIs
        description: ADI Assure security APIs for hardware root of trust, secure boot, and cryptographic operations.
      - name: No-OS Drivers
        description: Bare-metal C drivers for ADI ICs without requiring an operating system.
      - name: CodeFusion Studio
        description: VS Code-based IDE for ADI MCUs and DSPs with graphical configuration and code generation.
      - name: Open Source Ecosystem
        description: Active contributor to Linux kernel IIO subsystem, Zephyr RTOS, and other open source projects.
  - type: UseCases
    data:
      - name: Precision Measurement
        description: High-accuracy data acquisition from ADI ADCs and sensors using libiio or PyADI-IIO.
      - name: RF and Communications
        description: Control of RF transceivers like ADRV9002 and AD9361 for SDR and communications applications.
      - name: Industrial Automation
        description: Integration of ADI industrial ICs into factory automation and process control systems.
      - name: Secure IoT Devices
        description: Building secure edge devices with hardware root of trust using ADI Assure security APIs.
      - name: Motor Control
        description: Developing motor drive applications using ADI ADSP processors and evaluation kits.
  - type: Integrations
    data:
      - name: Linux Kernel IIO Subsystem
        description: ADI actively contributes drivers to the Linux kernel IIO framework.
      - name: Zephyr RTOS
        description: ADI maintains hardware support for ADI MCUs in the Zephyr real-time operating system.
      - name: GNU Radio
        description: Integration with GNU Radio for software-defined radio applications using ADI transceivers.
      - name: MATLAB/Simulink
        description: MathWorks toolbox support for ADI hardware for signal processing prototyping.
      - name: Microsoft Visual Studio Code
        description: CodeFusion Studio is built as a VS Code extension for embedded development.
  - type: JSONSchema
    url: json-schema/analog-devices-iio-device-schema.json
  - type: JSONSchema
    url: json-schema/analog-devices-iio-context-schema.json
  - type: JSONLD
    url: json-ld/analog-devices-context.jsonld
  - type: Vocabulary
    url: vocabulary/analog-devices-vocabulary.yaml
  - type: SpectralRules
    url: rules/analog-devices-spectral-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
