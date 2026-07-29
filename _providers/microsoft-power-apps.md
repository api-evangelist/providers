---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Microsoft Power Apps Agentic Access
  operation_count: 12
  slug: microsoft-power-apps-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 12
apis:
- description: API for administrative tasks including environment management, app sharing, and user permissions.
  name: Power Apps Management API
  slug: power-apps-management-api
- description: API for working with custom and standard connectors to integrate external services and data sources.
  name: Power Apps Connectors API
  slug: power-apps-connectors-api
- description: API specific to Canvas Apps for creating pixel-perfect user interfaces with drag-and-drop functionality.
  name: Power Apps Canvas Apps API
  slug: power-apps-canvas-apps-api
- description: API for Model-driven Apps that automatically generate UI based on data model and business logic.
  name: Power Apps Model-driven Apps API
  slug: power-apps-model-driven-apps-api
- description: Framework API for professional developers to create reusable code components for model-driven and canvas apps using TypeScript and web technologies.
  name: Power Apps Component Framework (PCF) API
  slug: power-apps-component-framework-pcf-api
- description: Unified RESTful API for Power Platform administration including environment management, governance, licensing, app management, and capacity reporting.
  name: Power Platform REST API
  slug: power-platform-rest-api
- description: Web API for Power Pages (formerly Power Apps Portals) enabling CRUD operations on Dataverse tables from external-facing portal web pages.
  name: Power Pages Web API
  slug: power-pages-web-api
- description: .NET SDK providing strongly-typed access to Microsoft Dataverse through the IOrganizationService interface for server-side development and plugins.
  name: Dataverse Organization Service SDK
  slug: dataverse-organization-service-sdk
- description: API and SDK for building code-first Power Apps using popular frameworks like React and Vue, developed in any code-first IDE and deployed to Power Apps.
  name: Power Apps Code Apps API
  slug: power-apps-code-apps-api
- description: Operations on the account entity set. An account represents a business that is a customer or potential customer, typically the company billed in business transactions.
  name: Microsoft Power Apps Accounts API
  slug: microsoft-power-apps-accounts-api
- description: Operations on the contact entity set. A contact represents a person with whom a business unit has a relationship, such as a customer, supplier, or colleague.
  name: Microsoft Power Apps Contacts API
  slug: microsoft-power-apps-contacts-api
- description: Operations on the entity definition entity set. Provides metadata about Dataverse tables (entities) including their logical names, collection names, and structural information. Read-only access via Re
  name: Microsoft Power Apps Entities API
  slug: microsoft-power-apps-entities-api
artifact_total: 69
collections:
- collection_type: postman
  name: Microsoft Power Apps Microsoft Dataverse Web Accounts API
  slug: postman-microsoft-power-apps-accounts-api
- collection_type: postman
  name: Microsoft Power Apps Microsoft Dataverse Web Accounts Contacts API
  slug: postman-microsoft-power-apps-contacts-api
- collection_type: postman
  name: Microsoft Power Apps Microsoft Dataverse Web Accounts Entities API
  slug: postman-microsoft-power-apps-entities-api
- collection_type: open
  name: Microsoft Power Apps Microsoft Dataverse Web API
  slug: open-microsoft-power-apps-dataverse-web-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-power-apps/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-power-apps-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-power-apps-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-power-apps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-power-apps-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-power-apps-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.microsoft.com/en-us/power-apps/developer/
- group: operate
  title: ''
  type: Community
  url: https://powerusers.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://powerapps.microsoft.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://powerapps.microsoft.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.powerplatform.microsoft.com/
- group: operate
  title: ''
  type: Support
  url: https://powerapps.microsoft.com/support/
- group: learn
  title: ''
  type: Training
  url: https://docs.microsoft.com/en-us/learn/powerplatform/power-apps
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/PowerApps-Samples
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/productoffering/MicrosoftPowerApps
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: docs
  title: ALM Documentation
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-platform/alm/
- group: docs
  title: Pipelines
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-platform/alm/pipelines
- group: docs
  title: Power Platform Developer Documentation
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-platform/developer/
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/pipeline
- group: auth
  title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/power-platform/admin/wp-security
- group: docs
  title: Power Fx Overview
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-platform/power-fx/overview
- group: docs
  title: Power Fx Formula Reference
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-overview
- group: learn
  title: Deployment Training
  type: Training
  url: https://learn.microsoft.com/en-us/training/paths/simplify-power-platform-deployments/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave1/power-apps/planned-features
created: '2024'
description: Collection of APIs for Microsoft Power Apps platform enabling low-code application development, automation, and data connectivity.
examples:
- key_count: 4
  name: Microsoft Power Apps Dataverse Web Account Collection Example
  slug: microsoft-power-apps-dataverse-web-account-collection-example
- key_count: 69
  name: Microsoft Power Apps Dataverse Web Account Example
  slug: microsoft-power-apps-dataverse-web-account-example
- key_count: 4
  name: Microsoft Power Apps Dataverse Web Contact Collection Example
  slug: microsoft-power-apps-dataverse-web-contact-collection-example
- key_count: 68
  name: Microsoft Power Apps Dataverse Web Contact Example
  slug: microsoft-power-apps-dataverse-web-contact-example
- key_count: 4
  name: Microsoft Power Apps Dataverse Web Entity Collection Example
  slug: microsoft-power-apps-dataverse-web-entity-collection-example
- key_count: 22
  name: Microsoft Power Apps Dataverse Web Entity Example
  slug: microsoft-power-apps-dataverse-web-entity-example
- key_count: 1
  name: Microsoft Power Apps Dataverse Web O Data Error Example
  slug: microsoft-power-apps-dataverse-web-o-data-error-example
features:
- description: Visual drag-and-drop app building with Power Fx formulas and pre-built templates.
  name: Low-Code Development
- description: Built-in data platform with security, business logic, and integration capabilities.
  name: Microsoft Dataverse
- description: Connect to any external API through standard and custom connector definitions.
  name: Custom Connectors
- description: Automatically generated UIs based on data model and business logic configuration.
  name: Model-Driven Apps
- description: Professional code components using TypeScript for custom controls in canvas and model-driven apps.
  name: Component Framework
finops:
- name: Microsoft Power Apps Finops
  service_category: Business Applications / Low-Code
  slug: microsoft-power-apps-finops
image: https://powerplatform.microsoft.com/images/power-apps-logo.png
integrations:
- description: Native integration with Teams, SharePoint, Outlook, and Excel for productivity workflows.
  name: Microsoft 365
- description: Shared Dataverse platform with Dynamics 365 CRM and ERP modules for unified data.
  name: Dynamics 365
- description: Trigger automated flows from Power Apps for cross-system process automation.
  name: Power Automate
json_schemas:
- name: Account
  property_count: 69
  slug: microsoft-power-apps-account
- name: AccountCollection
  property_count: 4
  slug: microsoft-power-apps-accountcollection
- name: Contact
  property_count: 68
  slug: microsoft-power-apps-contact
- name: ContactCollection
  property_count: 4
  slug: microsoft-power-apps-contactcollection
- name: AccountCollection
  property_count: 4
  slug: microsoft-power-apps-dataverse-web-account-collection
- name: Account
  property_count: 69
  slug: microsoft-power-apps-dataverse-web-account
- name: ContactCollection
  property_count: 4
  slug: microsoft-power-apps-dataverse-web-contact-collection
- name: Contact
  property_count: 68
  slug: microsoft-power-apps-dataverse-web-contact
- name: EntityCollection
  property_count: 4
  slug: microsoft-power-apps-dataverse-web-entity-collection
- name: Entity
  property_count: 22
  slug: microsoft-power-apps-dataverse-web-entity
- name: ODataError
  property_count: 1
  slug: microsoft-power-apps-dataverse-web-o-data-error
- name: Microsoft Power Apps Dataverse Entity Schema
  property_count: 0
  slug: microsoft-power-apps-entity
- name: EntityCollection
  property_count: 4
  slug: microsoft-power-apps-entitycollection
- name: ODataError
  property_count: 1
  slug: microsoft-power-apps-odataerror
json_structures:
- name: Microsoft Power Apps Dataverse Web Account Collection Structure
  property_count: 4
  slug: microsoft-power-apps-dataverse-web-account-collection-structure
- name: Microsoft Power Apps Dataverse Web Account Structure
  property_count: 69
  slug: microsoft-power-apps-dataverse-web-account-structure
- name: Microsoft Power Apps Dataverse Web Contact Collection Structure
  property_count: 4
  slug: microsoft-power-apps-dataverse-web-contact-collection-structure
- name: Microsoft Power Apps Dataverse Web Contact Structure
  property_count: 68
  slug: microsoft-power-apps-dataverse-web-contact-structure
- name: Microsoft Power Apps Dataverse Web Entity Collection Structure
  property_count: 4
  slug: microsoft-power-apps-dataverse-web-entity-collection-structure
- name: Microsoft Power Apps Dataverse Web Entity Structure
  property_count: 22
  slug: microsoft-power-apps-dataverse-web-entity-structure
- name: Microsoft Power Apps Dataverse Web O Data Error Structure
  property_count: 1
  slug: microsoft-power-apps-dataverse-web-o-data-error-structure
- name: Microsoft Power Apps Structure
  property_count: 0
  slug: microsoft-power-apps-structure
jsonld:
- class_count: 0
  name: Microsoft Power Apps Context
  property_count: 5
  slug: microsoft-power-apps-context
- class_count: 0
  name: Microsoft Power Apps Dataverse Web Context
  property_count: 0
  slug: microsoft-power-apps-dataverse-web-context
layout: provider
modified: '2026-05-19'
name: Microsoft Power Apps
nav: Providers
network: true
overview: 'Microsoft Power Apps publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Contacts API, and Entities API. Tagged areas include Business Applications, Cloud, Enterprise, Low-Code, and Microsoft.


  The Microsoft Power Apps catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Microsoft Power Apps'' developer surface includes authentication, engineering blog, pricing, support, training material, documentation, CLI, and 18 more developer resources.'
plans:
- name: Microsoft Power Apps Plans Pricing
  plan_count: 6
  slug: microsoft-power-apps-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 9
  name: Microsoft Power Apps Rate Limits
  slug: microsoft-power-apps-rate-limits
rules:
- name: Microsoft Power Apps API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: microsoft-power-apps-jsonschema-spectral-rules
- name: Microsoft Power Apps API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: microsoft-power-apps-spectral-rules
scopes:
- name: Microsoft Power Apps Scopes
  scope_count: 2
  slug: microsoft-power-apps-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 64.5
  delta: -3.5
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.2
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 73.7
  previous_composite: 68.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-power-apps/refs/heads/main/screenshots/microsoft-power-apps-2026-06-20T185522.png
security:
- kind: authentication
  name: Microsoft Power Apps Authentication
  slug: microsoft-power-apps-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Power Apps Domain Security
  slug: microsoft-power-apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Power Apps Vulnerability Disclosure
  slug: microsoft-power-apps-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-power-apps
tags:
- Business Applications
- Cloud
- Enterprise
- Low-Code
- Microsoft
- No-Code
- Power Platform
- SaaS
use_cases:
- description: Digitize paper-based processes and manual workflows with custom business applications.
  name: Business Process Automation
- description: Build external-facing portals using Power Pages with Dataverse Web API integration.
  name: Customer Portal
- description: Create mobile applications for field workers with offline capabilities and data sync.
  name: Field Service Apps
- description: Build CRUD applications on Dataverse for managing business data with role-based security.
  name: Data Management
website: https://docs.microsoft.com/en-us/power-apps/developer/
---
