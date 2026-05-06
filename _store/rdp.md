---
aid: rdp
name: RDP
description: The Remote Desktop Protocol (RDP) is a proprietary network protocol developed by Microsoft that provides a graphical interface to connect to another computer over a network. RDP transmits keyboard, mouse, display, and audio data between client and host, enabling remote administration, virtual desktops, and remote work scenarios. The protocol typically operates on TCP and UDP port 3389 and is defined in the MS-RDPBCGR open specification. It is implemented by Microsoft's Remote Desktop Services as well as third-party clients across Windows, macOS, Linux, iOS, and Android. The RDP acronym is also shared with the Refinitiv Data Platform (LSEG), a cloud REST API platform for financial market data, historical pricing, ESG, and analytics.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/apis.yml
tags:
  - Financial Data
  - LSEG
  - Microsoft
  - Networking
  - RDP
  - Remote Access
  - Remote Desktop
  - Refinitiv
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis: []
common:
  - type: JSONSchema
    name: RDP Connection Schema
    description: JSON Schema describing an RDP connection profile.
    url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/json-schema/rdp-connection.json
  - type: JSONSchema
    name: RDP Session Schema
    description: JSON Schema describing an active or historical RDP session on an RDS host.
    url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/json-schema/rdp-session-schema.json
  - type: JSONStructure
    name: RDP Connection Structure
    description: Field-level structure documentation for the RDP connection profile object.
    url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/json-structure/rdp-connection-structure.json
  - type: JSONLDContext
    name: RDP JSON-LD Context
    description: JSON-LD context mapping RDP concepts to linked data identifiers.
    url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/json-ld/rdp-context.jsonld
  - type: Example
    name: RDP Connection Example
    description: Example RDP connection profile for a corporate development server.
    url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/examples/rdp-connection-example.json
  - type: Example
    name: RDP Session Example
    description: Example active RDP session record from a Remote Desktop Services host.
    url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/examples/rdp-session-example.json
  - type: Vocabulary
    name: RDP Vocabulary
    description: Domain vocabulary for RDP protocol concepts and Refinitiv Data Platform terms.
    url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/vocabulary/rdp-vocabulary.yml
  - type: Specification
    name: MS-RDPBCGR Remote Desktop Protocol Basic Connectivity and Graphics Remoting
    description: Microsoft Open Specification defining the core RDP protocol.
    url: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/
  - type: Specification
    name: MS-RDSOD Remote Desktop Services Protocols Overview
    description: Microsoft overview of all Remote Desktop Services protocol components.
    url: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdsod/
  - type: Documentation
    name: Microsoft Remote Desktop Services Documentation
    description: Official documentation for Microsoft Remote Desktop Services.
    url: https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds
  - type: Documentation
    name: LSEG Refinitiv Data Platform APIs
    description: LSEG developer portal for Refinitiv Data Platform (RDP) REST APIs.
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
