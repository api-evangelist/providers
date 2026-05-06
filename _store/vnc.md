---
aid: vnc
name: VNC
description: RealVNC provides the VNC Connect remote desktop platform and VNC Developer SDK, enabling organizations to embed secure remote access into products and automate device management. The VNC Cloud REST API manages cloud address allocation and connectivity brokering, while the VNC Developer SDK (C, Java, Python, .NET, JavaScript) enables embedding Viewer and Server capabilities into applications.
type: Index
url: https://www.realvnc.com/en/developer/
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Remote Desktop
  - Remote Access
  - VNC
  - Networking
  - Screen Sharing
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vnc:vnc-cloud-api
    name: VNC Cloud API
    description: The VNC Cloud REST API manages cloud addresses that allow devices to join VNC Cloud and establish remote connections through RealVNC's managed broker service. Supports creating, listing, updating, resetting, and deleting cloud addresses with access control via groups and allowlisted peer cloud addresses.
    humanURL: https://www.realvnc.com/en/developer/docs/latest/api/cloud/
    baseURL: https://api.vnc.com/cloud/1.1
    tags:
      - Cloud
      - Remote Access
      - VNC
    properties:
      - type: Documentation
        url: https://www.realvnc.com/en/developer/docs/latest/api/cloud/
      - type: OpenAPI
        url: openapi/vnc-cloud-openapi.yml
      - type: JSONSchema
        url: json-schema/vnc-cloud-address-schema.json
  - aid: vnc:vnc-connect-api
    name: VNC Connect Management API
    description: The VNC Connect API Access feature enables programmatic management of devices registered to a team account, supporting device inventory, renaming, deduplication, and integration with ITSM tools. Authenticated with team-scoped API access keys with granular permission control.
    humanURL: https://www.realvnc.com/en/connect/api-access/
    tags:
      - Device Management
      - Automation
      - VNC Connect
    properties:
      - type: Documentation
        url: https://www.realvnc.com/en/connect/api-access/
  - aid: vnc:vnc-sdk
    name: VNC Developer SDK
    description: Cross-platform SDK for embedding VNC Viewer and Server functionality into applications. Available for C, Java, Python, .NET, and JavaScript. Supports direct TCP/UDP connections, VNC Cloud brokering, end-to-end AES-128 encryption, custom messaging, multi-display, clipboard sharing, and screen annotations.
    humanURL: https://www.realvnc.com/en/developer/docs/latest/overview.html
    tags:
      - SDK
      - Embedded
      - Remote Desktop
      - Developer Tools
    properties:
      - type: Documentation
        url: https://www.realvnc.com/en/developer/docs/latest/overview.html
      - type: Reference
        url: https://www.realvnc.com/en/developer/docs/latest/api/
common:
  - type: Website
    url: https://www.realvnc.com/en/developer/
  - type: Documentation
    url: https://www.realvnc.com/en/developer/docs/latest/
  - type: OpenAPI
    url: openapi/vnc-cloud-openapi.yml
  - type: JSONSchema
    url: json-schema/vnc-cloud-address-schema.json
  - type: JSONStructure
    url: json-structure/vnc-cloud-address-structure.json
  - type: JSON-LD
    url: json-ld/vnc-context.jsonld
  - type: Vocabulary
    url: vocabulary/vnc-vocabulary.yml
  - type: SpectralRules
    url: rules/vnc-rules.yml
  - type: NaftikoCapability
    url: capabilities/remote-access-management.yaml
  - type: GettingStarted
    url: https://www.realvnc.com/en/developer/docs/latest/overview.html
  - type: GitHubOrganization
    url: https://github.com/realvnc
  - type: GitHubOrganization
    url: https://github.com/realvnc-labs
  - type: Pricing
    url: https://www.realvnc.com/en/connect/pricing/
  - type: Support
    url: https://help.realvnc.com/
  - type: TermsOfService
    url: https://www.realvnc.com/en/legal/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
