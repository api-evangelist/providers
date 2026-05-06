---
aid: zephyr
name: Zephyr Project
description: The Zephyr Project is a Linux Foundation project that delivers a small, scalable, secure, and open-source real-time operating system (RTOS) for resource-constrained embedded devices. Zephyr supports 1000+ boards across ARM Cortex, RISC-V, ARC, x86, Xtensa, and other architectures, ships with a C kernel, device drivers, networking stacks (BLE, Wi-Fi, Thread, Matter), security subsystems, and is supported by a meta-tool (west), an SDK (sdk-ng), and a broad ecosystem of training partners and commercial silicon and module vendors.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Embedded
  - IoT
  - Linux Foundation
  - RTOS
  - Open Source
  - Edge
created: '2026-03-16'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/zephyr/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: zephyr:zephyr-kernel-api
    name: Zephyr RTOS Kernel API
    description: The Zephyr kernel C API exposes scheduling, threading, synchronization, memory management, and timer services for real-time embedded applications. It is the foundation that device drivers and application code build on.
    humanURL: https://docs.zephyrproject.org/latest/kernel/index.html
    tags:
      - RTOS
      - Embedded
      - Kernel
    properties:
      - type: Documentation
        url: https://docs.zephyrproject.org/latest/kernel/index.html
      - type: APIReference
        url: https://docs.zephyrproject.org/apidoc/latest/index.html
      - type: GettingStarted
        url: https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - type: GitHubRepository
        url: https://github.com/zephyrproject-rtos/zephyr
  - aid: zephyr:zephyr-device-driver-api
    name: Zephyr Device Driver API
    description: The Zephyr device driver subsystem exposes a uniform device model across GPIO, I2C, SPI, UART, ADC, sensors, displays, networking, USB, Bluetooth, and many other peripheral classes, configured through Devicetree and Kconfig.
    humanURL: https://docs.zephyrproject.org/latest/build/dts/index.html
    tags:
      - Drivers
      - Devicetree
      - Embedded
    properties:
      - type: Documentation
        url: https://docs.zephyrproject.org/latest/hardware/index.html
      - type: APIReference
        url: https://docs.zephyrproject.org/apidoc/latest/group__io__interfaces.html
  - aid: zephyr:zephyr-networking-api
    name: Zephyr Networking API
    description: The Zephyr networking stack exposes BSD-like sockets, TLS/DTLS, MQTT, CoAP, LWM2M, HTTP, WebSocket, gRPC, and connectivity layers including IPv4/IPv6, Wi-Fi, Thread, OpenThread, Matter, and BLE.
    humanURL: https://docs.zephyrproject.org/latest/connectivity/networking/index.html
    tags:
      - Networking
      - IoT
      - Connectivity
    properties:
      - type: Documentation
        url: https://docs.zephyrproject.org/latest/connectivity/networking/index.html
common:
  - type: Portal
    name: Zephyr Project
    url: https://www.zephyrproject.org/
  - type: Documentation
    name: Zephyr Project Documentation
    url: https://docs.zephyrproject.org/latest/
  - type: APIReference
    name: Zephyr API Reference
    url: https://docs.zephyrproject.org/apidoc/latest/index.html
  - type: GettingStarted
    name: Zephyr Getting Started Guide
    url: https://docs.zephyrproject.org/latest/develop/getting_started/index.html
  - type: GitHubOrganization
    name: Zephyr Project on GitHub
    url: https://github.com/zephyrproject-rtos
  - type: GitHubRepository
    name: Zephyr Primary Git Repository
    url: https://github.com/zephyrproject-rtos/zephyr
  - type: SDK
    name: Zephyr SDK (sdk-ng)
    url: https://github.com/zephyrproject-rtos/sdk-ng
  - type: CLI
    name: West - Zephyr's Meta-Tool
    url: https://github.com/zephyrproject-rtos/west
  - type: Blog
    name: Zephyr Project Blog
    url: https://www.zephyrproject.org/blog/
  - type: ReleaseNotes
    name: Zephyr Release Notes
    url: https://docs.zephyrproject.org/latest/releases/index.html
  - type: Training
    name: Zephyr Training Partner Program
    url: https://www.zephyrproject.org/training-partner-program/
  - type: Events
    name: Zephyr Events
    url: https://www.zephyrproject.org/events/
  - type: Compliance
    name: Zephyr Security
    url: https://docs.zephyrproject.org/latest/security/index.html
  - type: TermsOfService
    name: Linux Foundation Terms of Use
    url: https://www.linuxfoundation.org/terms
  - type: PrivacyPolicy
    name: Linux Foundation Privacy Policy
    url: https://www.linuxfoundation.org/privacy-policy/
  - type: JSONLD
    name: Zephyr JSON-LD Context
    url: json-ld/zephyr-context.jsonld
  - type: Resources
    name: Zephyr Vocabulary
    url: vocabulary/zephyr-vocabulary.yml
  - type: Resources
    name: Zephyr Build Capability
    url: capabilities/zephyr-build.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
