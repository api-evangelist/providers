---
aid: qlik-sense-enterprise
name: Qlik Sense Enterprise
description: Collection of APIs for Qlik Sense Enterprise, a modern analytics platform for business intelligence and data visualization.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Business Intelligence
  - Data Visualization
  - Enterprise
  - REST API
url: https://raw.githubusercontent.com/api-evangelist/qlik-sense-enterprise/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: qlik-sense-enterprise:qlik-sense-repository-service
    name: Qlik Sense Repository Service
    description: Core REST API for managing Qlik Sense Enterprise resources including apps, streams, users, security rules, and all configuration available through the Qlik Management Console.
    humanURL: https://help.qlik.com/en-US/sense-developer/November2025/Subsystems/RepositoryServiceAPI/Content/Sense_RepositoryServiceAPI/RepositoryServiceAPI-Introduction.htm
    tags:
      - Management
      - Repository
      - Security
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/November2025/Subsystems/RepositoryServiceAPI/Content/Sense_RepositoryServiceAPI/RepositoryServiceAPI-Introduction.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qlik-sense-enterprise/refs/heads/main/openapi/qlik-sense-enterprise-repository-service-openapi.yml
      - type: Authentication
        url: https://help.qlik.com/en-US/sense-developer/November2025/Subsystems/RepositoryServiceAPI/Content/Sense_RepositoryServiceAPI/RepositoryServiceAPI-Connect-API-Authenticate.htm
  - aid: qlik-sense-enterprise:qlik-sense-engine-json-api
    name: Qlik Sense Engine JSON API
    description: WebSocket protocol API using JSON-RPC for interacting with the Qlik Associative Engine.
    humanURL: https://help.qlik.com/en-US/sense-developer/November2025/Subsystems/EngineJSONAPI/Content/introduction.htm
    tags:
      - Engine
      - JSON-RPC
      - WebSocket
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/November2025/Subsystems/EngineJSONAPI/Content/introduction.htm
  - aid: qlik-sense-enterprise:qlik-sense-proxy-service
    name: Qlik Sense Proxy Service
    description: REST API for managing sessions, virtual proxies, and authentication in Qlik Sense Enterprise deployments.
    humanURL: https://help.qlik.com/en-US/sense-developer/Subsystems/ProxyServiceAPI/Content/Sense_ProxyServiceAPI/ProxyServiceAPI-Introduction.htm
    tags:
      - Proxy
      - Authentication
      - Sessions
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/Subsystems/ProxyServiceAPI/Content/Sense_ProxyServiceAPI/ProxyServiceAPI-Introduction.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qlik-sense-enterprise/refs/heads/main/openapi/qlik-sense-enterprise-proxy-service-openapi.yml
  - aid: qlik-sense-enterprise:qlik-sense-about-service
    name: Qlik Sense About Service
    description: Service that exposes metadata about the running Qlik Sense Enterprise deployment including versions and supported APIs.
    humanURL: https://help.qlik.com/en-US/sense-developer/Subsystems/RepositoryServiceAPI/Content/Sense_RepositoryServiceAPI/About-API/About-API-Introduction.htm
    tags:
      - Metadata
      - Service
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/Subsystems/RepositoryServiceAPI/Content/Sense_RepositoryServiceAPI/About-API/About-API-Introduction.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qlik-sense-enterprise/refs/heads/main/openapi/qlik-sense-enterprise-about-service-openapi.yml
  - aid: qlik-sense-enterprise:qlik-sense-data-connection
    name: Qlik Sense Data Connection
    description: API for managing data connections and data sources.
    humanURL: https://help.qlik.com/en-US/sense-developer/APIs/RepositoryServiceAPI/index.html
    tags:
      - Data Connections
      - Integration
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/APIs/RepositoryServiceAPI/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qlik-sense-enterprise/refs/heads/main/openapi/qlik-sense-enterprise-data-connection-openapi.yml
  - aid: qlik-sense-enterprise:qlik-sense-licenses
    name: Qlik Sense Licenses
    description: API for managing licenses, license allocations, and user access in Qlik Sense Enterprise.
    humanURL: https://help.qlik.com/en-US/sense-admin/Content/Sense_AdministerQSE/Licensing/Licensing.htm
    tags:
      - Licensing
      - Allocation
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-admin/Content/Sense_AdministerQSE/Licensing/Licensing.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qlik-sense-enterprise/refs/heads/main/openapi/qlik-sense-enterprise-licenses-openapi.yml
  - aid: qlik-sense-enterprise:qlik-sense-odag
    name: Qlik Sense ODAG
    description: On-Demand App Generation service API for orchestrating dynamic app generation against large data sources.
    humanURL: https://help.qlik.com/en-US/sense/Content/Sense_Helpsites/On-demand-apps.htm
    tags:
      - ODAG
      - On-Demand
      - Apps
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense/Content/Sense_Helpsites/On-demand-apps.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qlik-sense-enterprise/refs/heads/main/openapi/qlik-sense-enterprise-odag-service-openapi.yml
  - aid: qlik-sense-enterprise:qlik-sense-capabilities
    name: Qlik Sense Capabilities
    description: High-level JavaScript API for embedding and extending Qlik Sense visualizations and mashups.
    humanURL: https://help.qlik.com/en-US/sense-developer/APIs/CapabilityAPIs/index.html
    tags:
      - Visualization
      - Mashup
      - Embedding
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/APIs/CapabilityAPIs/index.html
common:
  - type: Portal
    url: https://qlik.dev/
  - type: Documentation
    url: https://help.qlik.com/en-US/sense-developer/November2025/Content/Sense_Helpsites/APIs-and-SDKs.htm
  - type: Authentication
    url: https://qlik.dev/toolkits/qlik-api/authentication/
  - type: Blog
    url: https://www.qlik.com/blog
  - type: Status
    url: https://status.qlikcloud.com/
  - type: Support
    url: https://community.qlik.com/t5/Support/ct-p/qlikSupport
  - type: TermsOfService
    url: https://www.qlik.com/us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.qlik.com/us/legal/privacy
  - type: GitHubOrganization
    url: https://github.com/qlik-oss
  - type: Community
    url: https://community.qlik.com/
  - type: Website
    url: https://www.qlik.com/
  - type: Login
    url: https://qlikid.qlik.com/
  - type: SignUp
    url: https://register.myqlik.qlik.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
