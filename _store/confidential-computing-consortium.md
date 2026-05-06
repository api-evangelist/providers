---
aid: confidential-computing-consortium
name: Confidential Computing Consortium
description: The Confidential Computing Consortium (CCC) is a Linux Foundation project that brings together hardware vendors, cloud providers, and software developers to accelerate the adoption of confidential computing. CCC defines, advances, and standardizes hardware-based Trusted Execution Environments (TEEs) that protect data and code while in use, complementing existing protections for data at rest and in transit. The consortium governs open source projects and specifications spanning attestation, trustworthy workload identity, and TEE runtimes.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/confidential-computing-consortium/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: opensource
tags:
  - Attestation
  - Confidential Computing
  - Hardware
  - Linux Foundation
  - Open Source
  - Privacy
  - Security
  - TEE
  - Trusted Execution Environment
apis:
  - aid: confidential-computing-consortium:ccc-projects
    name: Confidential Computing Consortium Projects
    description: A portfolio of open source projects governed by the Confidential Computing Consortium covering Trusted Execution Environment runtimes, remote attestation services, trustworthy workload identity, and shared tooling for confidential computing across CPU, GPU, and accelerator vendors. Projects include hosted SDKs, attestation services, and reference implementations rather than a single REST API.
    humanURL: https://confidentialcomputing.io/projects/
    baseURL: https://confidentialcomputing.io/projects/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Attestation
      - Confidential Computing
      - Open Source
      - TEE
    properties:
      - type: Documentation
        url: https://confidentialcomputing.io/projects/
      - type: GitHub
        url: https://github.com/confidential-computing
    x-features:
      - TEE Runtimes
      - Remote Attestation
      - Workload Identity
      - Hardware Security
      - Open Source Governance
    x-use-cases:
      - Protect AI/ML training and inference data in use
      - Run regulated workloads in untrusted clouds
      - Establish verifiable identity for cloud workloads
      - Build privacy-preserving multi-party computation
      - Standardize cross-vendor TEE attestation flows
  - aid: confidential-computing-consortium:trustworthy-workload-identity
    name: Trustworthy Workload Identity (TWI) Specifications
    description: A working group and set of Internet Draft specifications under the Confidential Computing Consortium that define how confidential workloads establish, prove, and consume identity using remote attestation evidence. TWI work intersects with the IETF RATS (Remote Attestation Procedures) and WIMSE (Workload Identity in a Multi-System Environment) groups, providing the foundation for attested, portable workload identity.
    humanURL: https://github.com/confidential-computing/twi
    baseURL: https://github.com/confidential-computing/twi
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Attestation
      - IETF
      - Specifications
      - Workload Identity
    properties:
      - type: Documentation
        url: https://github.com/confidential-computing/twi
      - type: GitHub
        url: https://github.com/confidential-computing/twi
      - type: Related
        url: https://github.com/confidential-computing/twi-rats
      - type: Related
        url: https://github.com/confidential-computing/twi-wimse
    x-features:
      - Workload Identity Standards
      - Remote Attestation Mappings
      - IETF Drafts
    x-use-cases:
      - Define identity for confidential workloads
      - Bind workload identity to hardware attestation
      - Interoperate across cloud providers and hardware vendors
common:
  - type: Website
    url: https://confidentialcomputing.io/
  - type: Documentation
    url: https://confidentialcomputing.io/resources/
  - type: Projects
    url: https://confidentialcomputing.io/projects/
  - type: GitHub
    url: https://github.com/confidential-computing
  - type: Glossary
    url: https://github.com/confidential-computing/glossary
  - type: Governance
    url: https://github.com/confidential-computing/governance
  - type: Mailing Lists
    url: https://lists.confidentialcomputing.io/
  - type: Blog
    url: https://confidentialcomputing.io/news/
  - type: Events
    url: https://confidentialcomputing.io/events/
  - type: Membership
    url: https://confidentialcomputing.io/membership/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
