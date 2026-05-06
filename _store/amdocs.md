---
aid: amdocs
name: Amdocs
description: Amdocs is a global technology company providing software and services to communications and media companies worldwide. Its connectX platform is a cloud-native SaaS BSS solution for telecom operators covering customer management, billing, provisioning, and subscription lifecycle. Amdocs also provides MarketONE for digital BSS, NetCracker for OSS network management, and an expanding suite of AI-powered telco solutions built on TM Forum Open APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Telecom
  - BSS
  - OSS
  - Billing
  - Customer Management
  - MVNO
  - 5G
  - SaaS
url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amdocs:amdocs-connectx-api
    name: Amdocs connectX BSS API
    description: The Amdocs connectX BSS API provides cloud-native SaaS BSS capabilities for telecom operators, covering billing, provisioning, customer management, and subscription lifecycle. Built on TM Forum Open APIs, it enables integration with CRM, network management, and revenue assurance systems for digital telco and MVNO operations. Powered by AWS with AI-native capabilities and eSIM support.
    humanURL: https://devportal.amdocs-dbs.com/
    baseURL: https://api.amdocs-dbs.com
    tags:
      - Billing
      - BSS
      - Provisioning
      - Telecom
      - MVNO
      - SaaS
    properties:
      - type: Documentation
        url: https://devportal.amdocs-dbs.com/
      - type: GettingStarted
        url: https://developer.amdocs-dbs.com/reference/getting-started-with-your-api
      - type: APIReference
        url: https://developer.amdocs-dbs.com/reference/getting-started-with-your-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/openapi/amdocs-connectx-openapi.yml
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/asyncapi/amdocs-events-asyncapi.yml
  - aid: amdocs:amdocs-marketone-api
    name: Amdocs MarketONE API
    description: The Amdocs MarketONE API provides digital BSS capabilities for telecoms, supporting catalog management, order management, customer management, and digital service delivery. REST APIs enable integration with the Amdocs MarketONE platform for telco digital transformation and omnichannel service delivery including mobile apps and web self-services.
    humanURL: https://developer.m1amdocs.com/
    baseURL: https://api.m1amdocs.com
    tags:
      - BSS
      - Digital Services
      - Order Management
      - Telecom
    properties:
      - type: Documentation
        url: https://developer.m1amdocs.com/
      - type: APIReference
        url: https://developer.m1amdocs.com/api/
      - type: Authentication
        url: https://developer.m1amdocs.com/documentation/Content/E-API%20Guides/ULMProcessGuide/ProcessCatalogue/AuthenticateUserProcess.htm
  - aid: amdocs:amdocs-netcracker-oss-api
    name: Amdocs NetCracker OSS API
    description: The Amdocs NetCracker OSS API provides network inventory management, network provisioning, and service assurance capabilities for telecom operators. REST and SOAP APIs support integration with network management systems, trouble ticketing, and service fulfillment platforms across multi-vendor network environments.
    humanURL: https://www.amdocs.com/products-services
    baseURL: https://api.amdocs.com
    tags:
      - Network Inventory
      - Network Management
      - OSS
      - Telecom
    properties:
      - type: Documentation
        url: https://www.amdocs.com/products-services
common:
  - type: Website
    url: https://www.amdocs.com/
  - type: Portal
    url: https://devportal.amdocs-dbs.com/
  - type: Documentation
    url: https://knowledge.amdocs-dbs.com/
  - type: GettingStarted
    url: https://developer.amdocs-dbs.com/reference/getting-started-with-your-api
  - type: GitHubOrganization
    url: https://github.com/open-amdocs
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/json-schema/amdocs-customer-schema.json
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/json-ld/amdocs-context.jsonld
  - type: Features
    data:
      - name: TM Forum Open API Compliance
        description: All connectX APIs comply with TM Forum Open API standards, enabling fast integration with third-party systems and reducing customization requirements.
      - name: AI-Native Capabilities
        description: GenAI-powered platform capabilities including AI-driven customer journeys, predictive analytics, and automated decision making for telco operations.
      - name: Cloud-Native SaaS Architecture
        description: Serverless microservices architecture deployed on AWS providing elastic scalability, local data residency compliance, and rapid deployment for MVNOs and telcos.
      - name: eSIM Management
        description: Built-in eSIM lifecycle management enabling telcos and MVNOs to support digital SIM provisioning without physical SIM cards.
      - name: Omnichannel Customer Experience
        description: Pre-built customer journeys spanning mobile apps, web self-service, and multi-channel support for consumer and business segments.
      - name: MVNO and MVNE Support
        description: End-to-end MVNO and MVNE capabilities including wireless prepaid, postpaid, and B2C solutions with rapid market launch support.
      - name: Catalog and Order Management
        description: Flexible product catalog management for bundling connectivity with digital services, plus end-to-end order management across consumer, business, and enterprise segments.
      - name: Revenue Management
        description: Converged billing, revenue assurance, and monetization capabilities supporting current and emerging revenue models including subscription and usage-based billing.
  - type: UseCases
    data:
      - name: MVNO Launch
        description: Rapidly launch new MVNO brands with pre-integrated telco-in-a-box capabilities including customer management, billing, and digital channels.
      - name: BSS Digital Transformation
        description: Migrate from legacy BSS to cloud-native SaaS BSS with TM Forum Open API compliance and pre-built integrations for telco digital transformation.
      - name: 5G Monetization
        description: Launch and monetize 5G services with flexible catalog management, usage-based billing, and analytics for network slicing and IoT.
      - name: Customer Self-Service
        description: Deploy omnichannel self-service portals and mobile apps with pre-built customer journeys for account management, plan changes, and billing.
      - name: Gen Z Mobile Services
        description: Launch fully customizable mobile plans enabling subscribers to configure data, calls, texts, and plan length via AI-powered apps.
      - name: IoT Service Management
        description: Manage IoT connectivity, device onboarding, and usage-based billing for enterprise IoT deployments across telecom networks.
  - type: Integrations
    data:
      - name: AWS
        description: connectX is powered by Amazon Web Services providing cloud infrastructure, elastic scalability, and global reach.
      - name: TM Forum Open APIs
        description: Full compliance with TM Forum Open API standards enabling plug-and-play integration with ecosystem partners and third-party systems.
      - name: Microsoft
        description: Customer Engagement Platform partnership with Microsoft for AI-driven customer interactions and analytics.
      - name: Network Management Systems
        description: Integration with multi-vendor network management systems and OSS platforms via NetCracker APIs.
  - type: Solutions
    data:
      - name: connectX
        description: All-in-one SaaS BSS platform for telcos and MVNOs with AI-powered customer management, billing, and monetization capabilities.
      - name: MarketONE
        description: Digital BSS platform for managing and monetizing subscriptions with integrated digital partners and omnichannel delivery.
      - name: Amdocs Networks
        description: Telco cloud transformation solutions for 5G, fiber, and IoT network deployment and optimization.
      - name: Digital Financial Services Platform
        description: Mobile wallet and financial services enablement for telco operators entering digital banking and fintech markets.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
