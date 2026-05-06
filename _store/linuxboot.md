---
aid: linuxboot
name: LinuxBoot
description: LinuxBoot is a Linux Foundation firmware project that uses a Linux kernel and initramfs as a bootloader, replacing specific firmware functionality such as UEFI DXE. It provides faster, more reliable, and more secure boot processes by leveraging the well-tested Linux kernel for hardware initialization. Core components include u-root (the ramfs builder), the LinuxBoot build system, and the NERF (Non-Extensible Reduced Firmware) heritage from Google.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Boot
  - Firmware
  - Hardware
  - Linux Foundation
  - u-root
  - UEFI
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/linuxboot/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: linuxboot:linuxboot-build-system
    name: LinuxBoot Build System
    description: The LinuxBoot project's build system and tooling for replacing UEFI DXE with a Linux kernel-based boot environment. Includes integrations with coreboot/LinuxBoot and UEFI PEI/LinuxBoot configurations.
    humanURL: https://www.linuxboot.org/
    tags:
      - Boot
      - Firmware
      - Build
    properties:
      - type: Documentation
        url: https://book.linuxboot.org
      - type: SourceCode
        url: https://github.com/linuxboot/linuxboot
  - aid: linuxboot:u-root
    name: u-root
    description: u-root is a Go-based universal root filesystem and ramfs builder used by LinuxBoot to assemble a minimal initramfs containing the userspace tools needed for booting.
    humanURL: https://u-root.org/
    tags:
      - Initramfs
      - Go
      - Userspace
    properties:
      - type: Documentation
        url: https://u-root.org/
      - type: SourceCode
        url: https://github.com/u-root/u-root
common:
  - type: Documentation
    name: LinuxBoot Book
    description: Official LinuxBoot project documentation and guide.
    url: https://book.linuxboot.org
  - type: GitHubOrg
    name: LinuxBoot GitHub
    description: Source code and repositories for LinuxBoot.
    url: https://github.com/linuxboot
  - type: Website
    name: LinuxBoot Website
    description: The main LinuxBoot project website.
    url: https://www.linuxboot.org/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
