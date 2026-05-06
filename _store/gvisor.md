---
aid: gvisor
name: gVisor
description: gVisor is an application kernel written in Go that implements a substantial portion of the Linux system surface. It provides an additional layer of isolation between running applications and the host operating system, intercepting and handling application system calls in user space to reduce the attack surface of the host kernel.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - Kernel
  - Linux
  - Open Source
  - Sandboxing
  - Security
url: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: gvisor:gvisor
    name: gVisor
    description: gVisor is an open-source application kernel written in Go that provides an additional layer of isolation between containerized applications and the host operating system. It implements a substantial portion of the Linux system call interface in user space, making it compatible with most Linux applications while providing stronger security guarantees than traditional container runtimes.
    humanURL: https://gvisor.dev/
    tags:
      - Containers
      - Kernel
      - Linux
      - Open Source
      - Sandboxing
      - Security
    properties:
      - type: Documentation
        url: https://gvisor.dev/docs/
      - type: Getting Started
        url: https://gvisor.dev/docs/user_guide/quick_start/docker/
common:
  - type: Website
    url: https://gvisor.dev/
  - type: GitHub Organization
    url: https://github.com/google
  - type: GitHub Repository
    url: https://github.com/google/gvisor
  - type: Documentation
    url: https://gvisor.dev/docs/
  - type: Blog
    url: https://gvisor.dev/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
