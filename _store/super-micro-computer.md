---
aid: super-micro-computer
name: Super Micro Computer
description: Super Micro Computer (Supermicro) is a global leader in high-performance, high-efficiency server technology and innovation, providing complete server, storage, and networking solutions for data center, cloud, AI, and edge applications. Supermicro exposes its server management capabilities through the DMTF Redfish RESTful API standard, enabling programmatic management of servers, storage, and networking hardware via BMC.
url: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Servers
  - Data Center
  - Hardware
  - Server Management
  - Redfish
  - BMC
  - IPMI
  - Fortune 500
  - Infrastructure
  - Cloud
apis:
  - aid: super-micro-computer:redfish-api
    name: Supermicro Redfish API
    description: Supermicro's implementation of the DMTF Redfish RESTful API standard for out-of-band server management via BMC. Provides programmatic access to server health monitoring, power management, BIOS/BMC firmware updates, storage configuration, network configuration, user account management, and event logging across Supermicro server platforms.
    humanURL: https://www.supermicro.com/en/solutions/management-software/redfish
    baseURL: https://{bmc-ip}/redfish/v1
    tags:
      - Redfish
      - Server Management
      - BMC
      - IPMI
      - Hardware
      - Data Center
    properties:
      - type: Documentation
        url: https://www.supermicro.com/manuals/other/redfish-ref-guide-html/Content/general-content/introduction.htm
      - type: Documentation
        url: https://www.supermicro.com/manuals/other/RedfishUserGuide.pdf
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/openapi/supermicro-redfish-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/json-schema/supermicro-computer-system-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/json-structure/supermicro-computer-system-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/json-ld/super-micro-computer-context.jsonld
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/rules/supermicro-redfish-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/capabilities/server-management.yaml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/vocabulary/super-micro-computer-vocabulary.yml
      - type: GitHub Repository
        url: https://github.com/supermicro/redfish
    contact:
      - FN: Supermicro Support
        url: https://www.supermicro.com/en/support
        email: support@supermicro.com
common:
  - type: Website
    url: https://www.supermicro.com
  - type: Developer Portal
    url: https://www.supermicro.com/en/solutions/management-software
  - type: Documentation
    url: https://www.supermicro.com/manuals/other/redfish-ref-guide-html/Content/general-content/introduction.htm
  - type: GitHub Organization
    url: https://github.com/supermicro
  - type: Blog
    url: https://www.supermicro.com/en/newsroom
  - type: Support
    url: https://www.supermicro.com/en/support
  - type: Pricing
    url: https://www.supermicro.com/en/products/servers
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
