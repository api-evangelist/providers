---
aid: gvisor
url: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/apis.yml
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
name: gVisor
tags:
- Containers
- Kernel
- Linux
- Open Source
- Sandboxing
- Security
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: gVisor is an application kernel written in Go that implements a substantial portion of the Linux system surface. It provides an additional layer of isolation between running applications and the host operating system, intercepting and handling application system calls in user space to reduce the attack surface of the host kernel.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

