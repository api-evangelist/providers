---
aid: linux
name: Linux
description: Linux is an open-source Unix-like operating system kernel originally created by Linus Torvalds. This index catalogs the userspace and kernel programming interfaces exposed by Linux, including system calls, eBPF, ioctl, netlink, procfs, sysfs, GPIO, and security interfaces such as Seccomp, Landlock, and Linux Security Modules. It also covers ecosystem APIs for systemd and PAM.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Kernel
  - Linux
  - Open Source
  - Operating System
  - Unix
  - Userspace API
url: https://raw.githubusercontent.com/api-evangelist/linux/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: linux:linux-kernel-userspace-api
    name: Linux Kernel Userspace API
    description: The set of stable userspace-facing interfaces exposed by the Linux kernel, including system calls, ioctls, eBPF, futex2, and the netlink protocol.
    humanURL: https://www.kernel.org/doc/html/latest/userspace-api/index.html
    tags:
      - Kernel
      - Userspace
      - System Calls
    properties:
      - type: Documentation
        url: https://www.kernel.org/doc/html/latest/userspace-api/index.html
      - type: Reference
        url: https://man7.org/linux/man-pages/man2/syscalls.2.html
  - aid: linux:ebpf-userspace-api
    name: eBPF Userspace API
    description: Extended Berkeley Packet Filter (eBPF) userspace API for loading and interacting with sandboxed programs running in the kernel.
    humanURL: https://www.kernel.org/doc/html/latest/userspace-api/ebpf/index.html
    tags:
      - eBPF
      - Kernel
      - Observability
    properties:
      - type: Documentation
        url: https://www.kernel.org/doc/html/latest/userspace-api/ebpf/index.html
  - aid: linux:netlink-api
    name: Netlink API
    description: Socket-based interface for communication between the kernel and userspace, used widely for networking, routing, and device configuration.
    humanURL: https://man7.org/linux/man-pages/man7/netlink.7.html
    tags:
      - Networking
      - IPC
      - Kernel
    properties:
      - type: Documentation
        url: https://www.kernel.org/doc/html/latest/userspace-api/netlink/index.html
  - aid: linux:seccomp-bpf
    name: Seccomp BPF
    description: SECure COMPuting mode with BPF filters, used to restrict which system calls a process can make for sandboxing and hardening.
    humanURL: https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html
    tags:
      - Security
      - Sandboxing
      - Syscalls
    properties:
      - type: Documentation
        url: https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html
  - aid: linux:landlock
    name: Landlock
    description: Unprivileged access-control framework allowing processes to restrict themselves and their descendants from filesystem and network operations.
    humanURL: https://www.kernel.org/doc/html/latest/userspace-api/landlock.html
    tags:
      - Security
      - Access Control
    properties:
      - type: Documentation
        url: https://www.kernel.org/doc/html/latest/userspace-api/landlock.html
  - aid: linux:procfs
    name: procfs
    description: Virtual filesystem mounted at /proc that exposes process and kernel information through a file-based interface.
    humanURL: https://man7.org/linux/man-pages/man5/proc.5.html
    tags:
      - Filesystem
      - Process
      - Monitoring
    properties:
      - type: Documentation
        url: https://www.kernel.org/doc/html/latest/filesystems/proc.html
  - aid: linux:sysfs
    name: sysfs
    description: Virtual filesystem mounted at /sys that exports kernel object and device information to userspace.
    humanURL: https://man7.org/linux/man-pages/man5/sysfs.5.html
    tags:
      - Filesystem
      - Devices
      - Kernel
    properties:
      - type: Documentation
        url: https://www.kernel.org/doc/html/latest/filesystems/sysfs.html
  - aid: linux:systemd-dbus
    name: systemd D-Bus API
    description: The system and service manager API exposed by systemd over D-Bus for managing units, services, and the boot process.
    humanURL: https://www.freedesktop.org/wiki/Software/systemd/dbus/
    tags:
      - systemd
      - D-Bus
      - Service Management
    properties:
      - type: Documentation
        url: https://www.freedesktop.org/software/systemd/man/
      - type: Reference
        url: https://www.freedesktop.org/wiki/Software/systemd/dbus/
  - aid: linux:linux-pam
    name: Linux PAM
    description: Pluggable Authentication Modules providing flexible, configurable authentication mechanisms for Linux applications.
    humanURL: http://www.linux-pam.org/
    tags:
      - Authentication
      - Security
    properties:
      - type: Documentation
        url: http://www.linux-pam.org/Linux-PAM-html/
  - aid: linux:udev
    name: udev
    description: Device manager for the Linux kernel handling device nodes and hotplug events under /dev.
    humanURL: https://www.freedesktop.org/software/systemd/man/udev.html
    tags:
      - Devices
      - Hardware
      - Hotplug
    properties:
      - type: Documentation
        url: https://www.freedesktop.org/software/systemd/man/udev.html
common:
  - type: Website
    name: Kernel.org
    description: Home of the Linux kernel project.
    url: https://www.kernel.org/
  - type: Documentation
    name: Linux Kernel Documentation
    description: Official kernel documentation tree.
    url: https://www.kernel.org/doc/html/latest/
  - type: Reference
    name: Linux man-pages
    description: The Linux man-pages project.
    url: https://man7.org/linux/man-pages/
  - type: Website
    name: Linux Foundation
    description: The Linux Foundation hosts the Linux kernel project.
    url: https://www.linuxfoundation.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
