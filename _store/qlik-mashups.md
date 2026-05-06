---
aid: qlik-mashups
name: Qlik Mashups
description: APIs and resources for building custom visualizations and analytics applications using Qlik Sense mashups.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Business Intelligence
  - Embedded Analytics
  - Mashup
  - Visualization
url: https://raw.githubusercontent.com/api-evangelist/qlik-mashups/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: qlik-mashups:qlik-sense-capability-apis
    name: Qlik Sense Capability APIs
    description: JavaScript APIs for building mashups and custom visualizations in Qlik Sense.
    humanURL: https://help.qlik.com/en-US/sense-developer/Subsystems/APIs/Content/Sense_ClientAPIs/capability-apis-reference.htm
    tags:
      - JavaScript
      - Visualization
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/Subsystems/APIs/Content/Sense_ClientAPIs/capability-apis-reference.htm
      - type: Tutorial
        url: https://help.qlik.com/en-US/sense-developer/Subsystems/Mashups/Content/Sense_Mashups/mashups-getting-started.htm
  - aid: qlik-mashups:qlik-engine-api
    name: Qlik Engine API
    description: JSON-RPC API for interacting with the Qlik Associative Engine.
    humanURL: https://qlik.dev/apis/json-rpc/qix
    tags:
      - Engine
      - WebSocket
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/json-rpc/qix
  - aid: qlik-mashups:qlik-repository-api
    name: Qlik Repository API
    description: REST API for managing Qlik Sense repository content and configuration.
    humanURL: https://help.qlik.com/en-US/sense-developer/Subsystems/RepositoryServiceAPI/Content/Sense_RepositoryServiceAPI/RepositoryServiceAPI-Introduction.htm
    tags:
      - Repository
      - Administration
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/Subsystems/RepositoryServiceAPI/Content/Sense_RepositoryServiceAPI/RepositoryServiceAPI-Introduction.htm
  - aid: qlik-mashups:qlik-single-configurator
    name: Qlik Single Configurator
    description: API for configuring single integrations and mashup authentication.
    humanURL: https://help.qlik.com/en-US/sense-developer/Subsystems/Mashups/Content/Sense_Mashups/mashups-single-configurator.htm
    tags:
      - Configuration
      - Mashup
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/Subsystems/Mashups/Content/Sense_Mashups/mashups-single-configurator.htm
  - aid: qlik-mashups:qlik-nebula-js
    name: Qlik Nebula.js
    description: Modern framework for building visualization mashups with Qlik's next-generation APIs.
    humanURL: https://qlik.dev/libraries-and-tools/nebulajs
    tags:
      - Visualization
      - JavaScript
    properties:
      - type: Documentation
        url: https://qlik.dev/libraries-and-tools/nebulajs
      - type: GitHub
        url: https://github.com/qlik-oss/nebula.js
common:
  - type: GettingStarted
    url: https://help.qlik.com/en-US/sense-developer/Subsystems/Mashups/Content/Sense_Mashups/mashups-getting-started.htm
  - type: Community
    url: https://community.qlik.com/t5/Developers/ct-p/qlik-developer
  - type: Support
    url: https://support.qlik.com
  - type: Website
    url: https://www.qlik.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
