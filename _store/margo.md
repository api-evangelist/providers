---
aid: margo
name: Margo
description: Margo is a Linux Foundation open standard initiative for interoperability at the edge of industrial automation ecosystems. Founded by ABB, Capgemini, Microsoft, Rockwell Automation, Schneider Electric, and Siemens, it defines mechanisms for interoperability between edge applications, devices, and orchestration software.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Edge
  - Industrial
  - Interoperability
  - Linux Foundation
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/margo/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: margo:margo-specification
    name: Margo Specification
    description: Margo defines an open standard specification for interoperability of edge applications, devices, and orchestration software in industrial automation. The specification is in pre-draft stage and includes an application registry covering app/device interfaces. No public REST APIs are published; reference implementation is provided via the Margo sandbox.
    humanURL: https://docs.margo.org/
    tags:
      - Edge
      - Industrial
      - Interoperability
      - Linux Foundation
      - Specification
    properties:
      - type: Documentation
        url: https://docs.margo.org/
      - type: Specification
        url: https://docs.margo.org/specification/applications/application-registry
      - type: SourceCode
        url: https://github.com/margo/sandbox
common:
  - type: Documentation
    name: Margo Documentation
    description: Official documentation for Margo.
    url: https://margo.org/specifications/
  - type: GitHubOrg
    name: Margo GitHub
    description: Source code and repositories for Margo.
    url: https://github.com/margo
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
