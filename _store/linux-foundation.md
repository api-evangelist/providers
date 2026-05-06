---
aid: linux-foundation
name: Linux Foundation
description: The Linux Foundation is a nonprofit technology consortium that supports open source projects and ecosystems. It provides a neutral home for collaboration on open source software, hardware, standards, and data, and hosts hundreds of projects including the Linux kernel, Kubernetes, Node.js, PyTorch, OpenSSF, CNCF, RISC-V, and FINOS. The LFX platform offers tooling and insights for open source contributors and member organizations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Linux Foundation
  - Nonprofit
  - Open Source
  - Technology
  - LFX
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/linux-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: linux-foundation:linux-foundation-projects
    name: Linux Foundation Projects
    description: Programmatic access to Linux Foundation project resources, member data, and open source ecosystem information across hosted foundations such as CNCF, OpenSSF, OpenJS, LF Networking, LF Decentralized Trust, and others.
    humanURL: https://www.linuxfoundation.org/projects
    tags:
      - Linux Foundation
      - Projects
      - Open Source
    properties:
      - type: Documentation
        url: https://www.linuxfoundation.org/projects
  - aid: linux-foundation:lfx-platform
    name: LFX Platform
    description: LFX is the Linux Foundation's developer and community platform offering insights, tooling, and project lifecycle management for open source contributors and member organizations.
    humanURL: https://lfx.linuxfoundation.org/
    tags:
      - LFX
      - Platform
      - Insights
    properties:
      - type: Documentation
        url: https://lfx.linuxfoundation.org/
      - type: Insights
        url: https://insights.lfx.dev/
      - type: Profile
        url: https://myprofile.lfx.linuxfoundation.org/
common:
  - type: Documentation
    name: Linux Foundation Documentation
    description: Official documentation for the Linux Foundation.
    url: https://www.linuxfoundation.org/projects
  - type: GitHubOrg
    name: LF Engineering GitHub
    description: Source code and repositories for Linux Foundation engineering.
    url: https://github.com/LF-Engineering
  - type: Website
    name: Linux Foundation Website
    description: The main Linux Foundation website.
    url: https://www.linuxfoundation.org/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
