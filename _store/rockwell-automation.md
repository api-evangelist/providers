---
aid: rockwell-automation
name: Rockwell Automation
description: Rockwell Automation is a global provider of industrial automation and digital transformation solutions, helping manufacturers boost productivity, sustainability, and agility. The company offers a portfolio of hardware, software, and services including programmable logic controllers (PLCs), industrial networking, motor control, safety systems, and the FactoryTalk software suite for MES, SCADA, historian, remote access, and industrial data management.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/rockwell-automation/refs/heads/main/apis.yml
tags:
  - Industrial Automation
  - Manufacturing
  - PLC
  - SCADA
  - IIoT
created: '2026-03-21'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rockwell-automation:plex-erp-api
    name: Rockwell Automation Plex ERP API
    description: Plex by Rockwell Automation provides a Smart Manufacturing Platform ERP API with REST/JSON endpoints for customer orders, shipping, production, quality, and just-in-sequence parts delivery. Enables integration with third-party systems and cloud services through role-based security.
    tags:
      - ERP
      - Manufacturing
      - Smart Manufacturing
      - REST
      - Industrial Automation
    humanURL: https://plex.rockwellautomation.com/en-us/resources/enterprise-resource-planning-erp-apis.html
    baseURL: https://api.plex.com
    properties:
      - url: https://plex.rockwellautomation.com/en-us/resources/enterprise-resource-planning-erp-apis.html
        type: Documentation
      - url: https://developers.plex.com/docs
        type: Portal
      - url: https://docs.plex.com/welcome
        type: Documentation
  - aid: rockwell-automation:factorytalk-datamosaix-api
    name: Rockwell Automation FactoryTalk DataMosaix API
    description: FactoryTalk DataMosaix is an Industrial DataOps solution that provides REST API access for industrial data management, contextualization, and analytics. Supports machine-to-machine (M2M) communication, data ingestion, visualization, and integration with enterprise analytics tools via OpenAPI-specified endpoints accessible through Swagger UI.
    tags:
      - Industrial Data
      - DataOps
      - Manufacturing
      - REST
      - Industrial Automation
    humanURL: https://www.rockwellautomation.com/en-us/products/software/factorytalk/datamosaix.html
    baseURL: https://datamosaix-portal.cloud.rockwellautomation.com
    properties:
      - url: https://www.rockwellautomation.com/en-us/docs/factorytalk-datamosaix/current/online-help-ditamap/api-reference.html
        type: Documentation
      - url: https://www.rockwellautomation.com/en-us/products/software/factorytalk/datamosaix.html
        type: Website
  - aid: rockwell-automation:factorytalk-remote-access-api
    name: Rockwell Automation FactoryTalk Remote Access Web API
    description: FactoryTalk Remote Access (FTRA) Web API provides RESTful HTTP interface for remote access management, enabling developers to integrate industrial device remote access capabilities into third-party applications and proprietary systems. Supports GET, POST, PUT, PATCH, and DELETE operations for device and session management.
    tags:
      - Remote Access
      - Industrial Automation
      - REST
      - Manufacturing
    humanURL: https://www.rockwellautomation.com/en-us/products/software/factorytalk/remote-access.html
    baseURL: https://api.rockwellautomation.com
    properties:
      - url: https://www.rockwellautomation.com/en-pr/docs/factorytalk-remote-access/ubiquity-ftra-help/ftra-ditamap/web-api.html
        type: Documentation
  - aid: rockwell-automation:logix-designer-api
    name: Rockwell Automation Logix Designer SDK
    description: The Studio 5000 Logix Designer Software Development Kit (LDSDK) provides programmatic access to Logix controller programming for CI/CD pipeline automation, version control integration, and export of L5X controller files for PLC program management.
    tags:
      - PLC
      - Programming
      - SDK
      - Industrial Automation
      - Manufacturing
    humanURL: https://github.com/RockwellAutomation/ra-logix-designer-vcs-custom-tools
    baseURL: https://github.com/RockwellAutomation
    properties:
      - url: https://github.com/RockwellAutomation/ra-logix-cicd
        type: GitHubRepository
      - url: https://github.com/RockwellAutomation/ra-logix-designer-vcs-custom-tools
        type: GitHubRepository
  - aid: rockwell-automation:emulate3d-api
    name: Rockwell Automation Emulate3D API
    description: Emulate3D Core API provides programmatic access to 3D simulation and digital twin capabilities for factory automation. Enables integration with Nvidia Omniverse and custom automation workflows via scripting interfaces.
    tags:
      - Digital Twin
      - Simulation
      - Industrial Automation
      - Manufacturing
    humanURL: https://github.com/RockwellAutomation/ra-emulate3d-core-samples
    baseURL: https://github.com/RockwellAutomation
    properties:
      - url: https://github.com/RockwellAutomation/ra-emulate3d-core-samples
        type: GitHubRepository
      - url: https://github.com/RockwellAutomation/ra-emulate3d-kit-app-template
        type: GitHubRepository
common:
  - url: https://www.rockwellautomation.com
    type: Website
  - url: https://www.rockwellautomation.com/en-us/support/documentation.html
    type: Documentation
  - url: https://developers.plex.com/docs
    type: Portal
  - url: https://github.com/RockwellAutomation
    type: GitHubOrganization
  - url: https://www.rockwellautomation.com/en-us/support/
    type: Support
  - url: https://www.rockwellautomation.com/en-us/company/about-us/legal-notices/privacy-and-cookies-policy.html
    type: PrivacyPolicy
  - url: https://www.rockwellautomation.com/en-us/company/news/blogs/
    type: Blog
  - url: json-schema/rockwell-automation-plex-order-schema.json
    type: JSONSchema
  - url: json-structure/rockwell-automation-plex-structure.json
    type: JSONStructure
  - url: json-ld/rockwell-automation-context.jsonld
    type: JSONLDContext
  - url: vocabulary/rockwell-automation-vocabulary.yml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
