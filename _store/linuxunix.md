---
aid: linuxunix
name: Linux/Unix System
description: A topic catalog of system-level APIs and interfaces available across Linux/Unix-like operating systems. Includes kernel system calls, POSIX standards, inter-process communication mechanisms (D-Bus, Netlink), virtual filesystems (procfs, sysfs), event-notification facilities (epoll, inotify), device management (udev, systemd), and userspace security interfaces.
type: Topic
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Kernel
  - Linux
  - Operating System
  - System
  - Unix
  - POSIX
url: https://raw.githubusercontent.com/api-evangelist/linuxunix/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: linuxunix:system-calls-api
    name: System Calls API
    description: Low-level interface between user-space applications and the Linux kernel providing access to process management, file I/O, memory, networking, signals, and IPC primitives.
    humanURL: https://man7.org/linux/man-pages/man2/syscalls.2.html
    tags:
      - Kernel
      - Low-Level
      - Syscalls
    properties:
      - type: Documentation
        url: https://man7.org/linux/man-pages/dir_section_2.html
      - type: Reference
        url: https://www.kernel.org/doc/html/latest/userspace-api/index.html
  - aid: linuxunix:posix-api
    name: POSIX API
    description: Portable Operating System Interface standards for Unix-like systems, defining a consistent application programming interface across platforms.
    humanURL: https://pubs.opengroup.org/onlinepubs/9699919799/
    tags:
      - POSIX
      - Standards
      - Portability
    properties:
      - type: Documentation
        url: https://pubs.opengroup.org/onlinepubs/9699919799/
      - type: Specification
        url: https://standards.ieee.org/ieee/1003.1/7101/
  - aid: linuxunix:dbus-api
    name: D-Bus API
    description: Inter-process communication and remote procedure call mechanism widely used on Linux desktop and system services.
    humanURL: https://www.freedesktop.org/wiki/Software/dbus/
    tags:
      - IPC
      - Messaging
      - Desktop
    properties:
      - type: Documentation
        url: https://dbus.freedesktop.org/doc/dbus-specification.html
      - type: SourceCode
        url: https://gitlab.freedesktop.org/dbus/dbus
  - aid: linuxunix:netlink-api
    name: Netlink API
    description: Socket-based interface for communication between the kernel and user space, particularly for networking and device subsystems.
    humanURL: https://man7.org/linux/man-pages/man7/netlink.7.html
    tags:
      - Networking
      - Kernel
      - Sockets
    properties:
      - type: Documentation
        url: https://man7.org/linux/man-pages/man7/netlink.7.html
      - type: Reference
        url: https://www.kernel.org/doc/html/latest/userspace-api/netlink/intro.html
  - aid: linuxunix:procfs-api
    name: procfs API
    description: Virtual filesystem providing process and system information through a hierarchical file-based interface.
    humanURL: https://man7.org/linux/man-pages/man5/proc.5.html
    tags:
      - Filesystem
      - Process
      - Monitoring
    properties:
      - type: Documentation
        url: https://man7.org/linux/man-pages/man5/proc.5.html
      - type: Reference
        url: https://www.kernel.org/doc/html/latest/filesystems/proc.html
  - aid: linuxunix:sysfs-api
    name: sysfs API
    description: Virtual filesystem for kernel objects and device information presented under /sys.
    humanURL: https://man7.org/linux/man-pages/man5/sysfs.5.html
    tags:
      - Filesystem
      - Kernel
      - Devices
    properties:
      - type: Documentation
        url: https://man7.org/linux/man-pages/man5/sysfs.5.html
      - type: Reference
        url: https://www.kernel.org/doc/html/latest/filesystems/sysfs.html
  - aid: linuxunix:inotify-api
    name: inotify API
    description: Linux kernel subsystem for monitoring filesystem events such as file creation, deletion, and modification.
    humanURL: https://man7.org/linux/man-pages/man7/inotify.7.html
    tags:
      - Filesystem
      - Monitoring
      - Events
    properties:
      - type: Documentation
        url: https://man7.org/linux/man-pages/man7/inotify.7.html
  - aid: linuxunix:epoll-api
    name: epoll API
    description: I/O event notification facility for scalable monitoring of large numbers of file descriptors.
    humanURL: https://man7.org/linux/man-pages/man7/epoll.7.html
    tags:
      - I/O
      - Events
      - Performance
    properties:
      - type: Documentation
        url: https://man7.org/linux/man-pages/man7/epoll.7.html
  - aid: linuxunix:udev-api
    name: udev API
    description: Device manager for the Linux kernel handling device nodes and hotplug events in /dev.
    humanURL: https://www.freedesktop.org/software/systemd/man/udev.html
    tags:
      - Devices
      - Hardware
      - Hotplug
    properties:
      - type: Documentation
        url: https://www.freedesktop.org/software/systemd/man/udev.html
      - type: SourceCode
        url: https://github.com/systemd/systemd/tree/main/src/udev
  - aid: linuxunix:systemd-api
    name: systemd API
    description: System and service manager exposing a D-Bus interface for managing services, sockets, devices, mounts, and timers.
    humanURL: https://www.freedesktop.org/wiki/Software/systemd/
    tags:
      - Init
      - Service Management
      - System
    properties:
      - type: Documentation
        url: https://www.freedesktop.org/software/systemd/man/
      - type: Reference
        url: https://www.freedesktop.org/wiki/Software/systemd/dbus/
      - type: SourceCode
        url: https://github.com/systemd/systemd
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
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
