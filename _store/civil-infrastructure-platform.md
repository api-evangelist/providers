---
aid: civil-infrastructure-platform
name: Civil Infrastructure Platform
url: https://raw.githubusercontent.com/api-evangelist/civil-infrastructure-platform/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Embedded
  - Industrial
  - Infrastructure
  - Linux
  - Linux Foundation
  - Long-Term Support
  - Open Source
description: The Civil Infrastructure Platform (CIP) is a Linux Foundation collaborative project that builds an industrial-grade open source base layer for civil infrastructure systems such as transportation, power generation and distribution, building and city management, industrial control, and healthcare equipment. CIP curates a Super Long-Term Support (SLTS) kernel and core user-space packages that can be maintained for more than ten years, plus working groups for security (IEC 62443 alignment), software update, real-time, and testing. CIP does not publish a public REST API surface; its programmable interface is the source code, kernel, and tooling published through GitLab and Debian-derived package archives.
apis:
  - aid: civil-infrastructure-platform:cip-kernel
    name: CIP SLTS Kernel
    tags:
      - Embedded
      - Kernel
      - Linux
      - SLTS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://wiki.linuxfoundation.org/civilinfrastructureplatform/cipkernelmaintenance
    properties:
      - url: https://wiki.linuxfoundation.org/civilinfrastructureplatform/cipkernelmaintenance
        type: Documentation
      - url: https://gitlab.com/cip-project/cip-kernel
        type: Source Code
    description: The CIP Kernel is a Super Long-Term Support (SLTS) Linux kernel branch maintained for ten or more years, providing a stable base for industrial systems that must remain in service across multi-decade lifecycles.
  - aid: civil-infrastructure-platform:cip-core
    name: CIP Core Packages
    tags:
      - Debian
      - Packages
      - Userspace
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://wiki.linuxfoundation.org/civilinfrastructureplatform/cipcore
    properties:
      - url: https://wiki.linuxfoundation.org/civilinfrastructureplatform/cipcore
        type: Documentation
      - url: https://gitlab.com/cip-project/cip-core
        type: Source Code
    description: CIP Core provides a curated set of Debian-derived user-space packages aligned with the SLTS kernel to deliver a complete reference platform for civil infrastructure devices.
  - aid: civil-infrastructure-platform:cip-software-update
    name: CIP Software Update
    tags:
      - OTA
      - Software Update
      - SWUpdate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://wiki.linuxfoundation.org/civilinfrastructureplatform/softwareupdate
    properties:
      - url: https://wiki.linuxfoundation.org/civilinfrastructureplatform/softwareupdate
        type: Documentation
    description: The CIP Software Update working group maintains tooling such as SWUpdate and hawkBit-based servers used to deliver secure over-the-air updates across long-lived industrial deployments.
  - aid: civil-infrastructure-platform:cip-security
    name: CIP Security
    tags:
      - IEC 62443
      - Industrial Security
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://wiki.linuxfoundation.org/civilinfrastructureplatform/cipsecurity
    properties:
      - url: https://wiki.linuxfoundation.org/civilinfrastructureplatform/cipsecurity
        type: Documentation
    description: The CIP Security working group aligns the CIP base layer with IEC 62443-4-1 and 62443-4-2 industrial cybersecurity requirements and tracks CVE handling across the SLTS kernel and user-space.
  - aid: civil-infrastructure-platform:cip-testing
    name: CIP Testing
    tags:
      - CI
      - LAVA
      - Testing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://wiki.linuxfoundation.org/civilinfrastructureplatform/ciptesting
    properties:
      - url: https://wiki.linuxfoundation.org/civilinfrastructureplatform/ciptesting
        type: Documentation
    description: The CIP Testing working group runs continuous-integration and hardware-in-the-loop testing on member-supplied boards to validate kernel and core packages against the SLTS branch.
common:
  - type: Website
    url: https://www.cip-project.org/
  - type: Wiki
    url: https://wiki.linuxfoundation.org/civilinfrastructureplatform
  - type: GitLab
    url: https://gitlab.com/cip-project
  - type: GitHub
    url: https://github.com/cip-project
  - type: Mailing List
    url: https://lists.cip-project.org/g/cip-dev
  - type: Foundation
    url: https://www.linuxfoundation.org/projects/civil-infrastructure-platform/
  - type: JSON-LD
    url: json-ld/civil-infrastructure-platform-context.jsonld
  - type: Spectral
    url: rules/civil-infrastructure-platform-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/civil-infrastructure-platform-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
