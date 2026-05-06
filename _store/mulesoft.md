---
aid: mulesoft
name: MuleSoft
description: MuleSoft Anypoint Platform is an enterprise integration and API management platform offering an API gateway, design center, exchange marketplace, and monitoring for hybrid deployments connecting applications and data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - API Management
  - Enterprise
  - Integration
url: https://raw.githubusercontent.com/api-evangelist/mulesoft/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: mulesoft:mulesoft
    name: MuleSoft Anypoint Platform
    description: MuleSoft Anypoint Platform unifies API management with integration, providing a complete solution to connect any application, data source, or device with reusable APIs and integrations.
    humanURL: https://www.mulesoft.com/platform/api
    tags:
      - API Gateway
      - API Management
      - Enterprise
    properties:
      - type: Documentation
        url: https://docs.mulesoft.com/
      - type: GettingStarted
        url: https://docs.mulesoft.com/general/
  - aid: mulesoft:mulesoft-anypoint-platform-api
    name: MuleSoft Anypoint Platform Management API
    description: The Anypoint Platform Management API provides programmatic access to manage organizations, business groups, environments, and users within the MuleSoft Anypoint Platform. It enables automation of platform administration tasks including configuring access management, managing connected applications, and controlling role-based access control across the platform.
    humanURL: https://docs.mulesoft.com/access-management/
    baseURL: https://anypoint.mulesoft.com
    tags:
      - Administration
      - API Management
      - Enterprise
      - REST
    properties:
      - type: Documentation
        url: https://docs.mulesoft.com/access-management/
      - type: APIReference
        url: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/
      - type: Authentication
        url: https://docs.mulesoft.com/access-management/connected-apps-overview
      - type: OpenAPI
        url: openapi/mulesoft-anypoint-platform-openapi.yml
      - type: JSONSchema
        url: json-schema/mulesoft-application-schema.json
      - type: JSONLD
        url: json-ld/mulesoft-context.jsonld
  - aid: mulesoft:mulesoft-anypoint-exchange-api
    name: MuleSoft Anypoint Exchange API
    description: The Anypoint Exchange API provides programmatic access to MuleSoft's asset marketplace, enabling discovery, publishing, and management of reusable integration assets including APIs, connectors, templates, examples, and custom pages. It allows organizations to automate asset lifecycle management and promote API reuse across teams.
    humanURL: https://docs.mulesoft.com/exchange/
    baseURL: https://anypoint.mulesoft.com/exchange/api/v2
    tags:
      - API Catalog
      - Asset Management
      - Enterprise
      - Marketplace
    properties:
      - type: Documentation
        url: https://docs.mulesoft.com/exchange/
      - type: APIReference
        url: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/exchange-experience-api/
      - type: GettingStarted
        url: https://docs.mulesoft.com/exchange/to-publish-assets-maven
  - aid: mulesoft:mulesoft-anypoint-runtime-manager-api
    name: MuleSoft Anypoint Runtime Manager API
    description: The Anypoint Runtime Manager API provides programmatic control over Mule application deployments across CloudHub, Runtime Fabric, and hybrid deployment targets. It enables CI/CD automation for deploying, updating, starting, stopping, and monitoring Mule applications and their runtime environments.
    humanURL: https://docs.mulesoft.com/runtime-manager/
    baseURL: https://anypoint.mulesoft.com/cloudhub/api
    tags:
      - CI/CD
      - CloudHub
      - Deployment
      - Runtime Manager
    properties:
      - type: Documentation
        url: https://docs.mulesoft.com/runtime-manager/
      - type: APIReference
        url: https://docs.mulesoft.com/runtime-manager/cloudhub-api
      - type: GettingStarted
        url: https://docs.mulesoft.com/runtime-manager/deploying-to-cloudhub
  - aid: mulesoft:mulesoft-anypoint-mq-api
    name: MuleSoft Anypoint MQ API
    description: The Anypoint MQ API provides a cloud messaging service built on the Anypoint Platform for asynchronous messaging between Mule applications and other systems. It supports queues, exchanges, and dead-letter queues for reliable message delivery and decoupled integration patterns.
    humanURL: https://docs.mulesoft.com/mq/
    baseURL: https://anypoint.mulesoft.com/mq/stats/api/v1
    tags:
      - Async
      - Cloud
      - Messaging
      - Queue
    properties:
      - type: Documentation
        url: https://docs.mulesoft.com/mq/
      - type: APIReference
        url: https://docs.mulesoft.com/mq/mq-apis
      - type: GettingStarted
        url: https://docs.mulesoft.com/mq/mq-tutorial
  - aid: mulesoft:mulesoft-anypoint-design-center-api
    name: MuleSoft Anypoint Design Center API
    description: The Anypoint Design Center API provides access to the MuleSoft web-based API design environment for creating and editing API specifications in RAML and OAS formats. It supports project management, file operations, and publishing designed APIs to Anypoint Exchange for reuse across the organization.
    humanURL: https://docs.mulesoft.com/design-center/
    baseURL: https://anypoint.mulesoft.com/designcenter/api-designer
    tags:
      - API Design
      - Design Center
      - OpenAPI
      - RAML
    properties:
      - type: Documentation
        url: https://docs.mulesoft.com/design-center/
      - type: GettingStarted
        url: https://docs.mulesoft.com/design-center/design-create-publish-api-specs
common:
  - type: Portal
    url: https://www.mulesoft.com/
  - type: DeveloperPortal
    url: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/
  - type: Documentation
    url: https://docs.mulesoft.com/
  - type: GettingStarted
    url: https://docs.mulesoft.com/general/
  - type: Authentication
    url: https://docs.mulesoft.com/access-management/connected-apps-overview
  - type: Console
    url: https://anypoint.mulesoft.com/
  - type: Blog
    url: https://blogs.mulesoft.com/
  - type: ChangeLog
    url: https://docs.mulesoft.com/release-notes/
  - type: StatusPage
    url: https://trust.mulesoft.com/
  - type: Support
    url: https://help.mulesoft.com/s/support
  - type: Pricing
    url: https://www.mulesoft.com/platform/mule-esb-open-source-esb/pricing
  - type: TermsOfService
    url: https://www.mulesoft.com/legal/terms/EULA
  - type: PrivacyPolicy
    url: https://www.mulesoft.com/legal/privacy
  - type: GitHubOrganization
    url: https://github.com/mulesoft
  - type: GitHubRepository
    url: https://github.com/mulesoft/anypoint-examples
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/mule
  - type: YouTube
    url: https://www.youtube.com/user/mulesofttv
  - type: SDK
    url: https://docs.mulesoft.com/mule-sdk/latest/
  - type: Glossary
    url: https://docs.mulesoft.com/general/glossary
  - type: SignUp
    url: https://anypoint.mulesoft.com/login/signup?apintent=generic
  - type: Login
    url: https://anypoint.mulesoft.com/login/signin?apintent=generic
  - type: Partners
    url: https://www.mulesoft.com/integration-partner/partnermax-retirement
  - type: SpectralRules
    url: rules/mulesoft-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/mulesoft-vocabulary.yaml
  - type: Features
    url: https://www.mulesoft.com/platform
    data:
      - name: API Gateway
        description: Enterprise-grade API gateway for securing, governing, and managing API traffic across cloud and on-premises environments.
      - name: Anypoint Exchange
        description: Centralized marketplace for discovering, sharing, and reusing APIs, connectors, templates, and integration assets across the organization.
      - name: Design Center
        description: Web-based API design environment for creating and editing API specifications in RAML and OAS formats with real-time collaboration.
      - name: Runtime Manager
        description: Unified management console for deploying, monitoring, and managing Mule applications across CloudHub, Runtime Fabric, and hybrid targets.
      - name: Anypoint MQ
        description: Cloud-native messaging service supporting queues, exchanges, and dead-letter queues for reliable asynchronous integration patterns.
      - name: DataWeave
        description: Powerful data transformation language for mapping and converting data between formats within Mule integration flows.
      - name: Anypoint Studio
        description: Eclipse-based IDE for building Mule applications with visual flow design and integrated debugging capabilities.
      - name: Flow Designer
        description: Browser-based low-code tool for building simple integrations and automations without needing Anypoint Studio.
      - name: API Governance
        description: Policy enforcement and governance framework for ensuring API consistency, security, and compliance across the platform.
      - name: Anypoint Monitoring
        description: Real-time visibility into API and integration performance with dashboards, alerts, and log management.
  - type: UseCases
    url: https://www.mulesoft.com/integration-solutions
    data:
      - name: Application Integration
        description: Connect SaaS and on-premises applications to create unified business processes and eliminate data silos.
      - name: API-Led Connectivity
        description: Build reusable APIs organized in system, process, and experience layers to accelerate digital transformation.
      - name: B2B Integration
        description: Automate partner onboarding and EDI/AS2 data exchange with trading partners using pre-built connectors.
      - name: Cloud Migration
        description: Migrate on-premises integrations to the cloud while maintaining connectivity with legacy systems.
      - name: Customer 360
        description: Unify customer data across CRM, ERP, and marketing systems to create a single view of the customer.
      - name: AI Agent Integration
        description: Connect AI agents to enterprise systems, models, and vector stores to orchestrate complex agentic workflows.
  - type: Integrations
    url: https://www.mulesoft.com/exchange/
    data:
      - name: Salesforce
        description: Native integration with Salesforce CRM, Service Cloud, and Marketing Cloud for bidirectional data sync and event-driven workflows.
      - name: SAP
        description: Pre-built connector for SAP ERP, S/4HANA, and BTP enabling real-time data exchange with SAP systems.
      - name: Workday
        description: Connector for syncing HR, finance, and planning data between Workday and other enterprise applications.
      - name: ServiceNow
        description: Integration with ServiceNow ITSM and ITOM for automated ticket creation, incident management, and CMDB sync.
      - name: AWS
        description: Connectors for Amazon S3, SQS, SNS, Lambda, and other AWS services for hybrid cloud integration.
      - name: Microsoft Azure
        description: Integration with Azure Service Bus, Blob Storage, SQL Database, and Active Directory services.
      - name: Slack
        description: Connector for sending notifications, creating channels, and automating workflows within Slack workspaces.
      - name: NetSuite
        description: Pre-built connector for Oracle NetSuite ERP enabling financial, inventory, and order management integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
