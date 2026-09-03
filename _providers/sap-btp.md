---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 7
apis:
- description: REST APIs for managing SAP BTP global accounts, subaccounts, directories, and entitlements. Provides programmatic control over the platform hierarchy and service provisioning.
  name: SAP BTP Core Services API
  slug: sap-btp-core-services-api
- description: OAuth 2.0-based authorization and trust management service for SAP BTP. Handles user authentication, client credentials grants, and JWT token issuance for service-to-service communication.
  name: SAP Authorization and Trust Management Service API (XSUAA)
  slug: sap-authorization-and-trust-management-service-api-xsuaa
- description: REST API for retrieving and managing connectivity destinations in SAP BTP. Used by applications to look up connection parameters for remote services and on-premise systems.
  name: SAP Destination Service API
  slug: sap-destination-service-api
- description: APIs for SAP Integration Suite, providing cloud integration, API management, event mesh, and integration advisor capabilities for connecting SAP and third-party systems.
  name: SAP Integration Suite API
  slug: sap-integration-suite-api
- description: REST API for SAP AI Core, enabling training, deployment, and inference of AI and machine learning models within the SAP BTP ecosystem.
  name: SAP AI Core API
  slug: sap-ai-core-api
- description: REST API for managing service instances and service bindings across SAP BTP environments, enabling multi-environment service lifecycle management.
  name: SAP Service Manager API
  slug: sap-service-manager-api
- description: REST API for configuring and receiving alerts about events in SAP BTP services. Enables proactive monitoring, incident response, and budget threshold notifications.
  name: SAP Alert Notification Service API
  slug: sap-alert-notification-service-api
artifact_total: 13
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sap/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-btp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-btp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/technology-platform.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/btp/sap-business-technology-platform/sap-business-technology-platform
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SAP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/sap-developers
- group: company
  title: ''
  type: Blog
  url: https://community.sap.com/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sap.com/products/technology-platform/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: other
  title: ''
  type: X
  url: https://twitter.com/sapCommBlogs
- group: commercial
  title: ''
  type: Plans
  url: plans/sap-btp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sap-btp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sap-btp-finops.yml
created: '2026-06-13'
description: Cloud platform with REST APIs for application development, integration, data management, AI services, and analytics across the SAP ecosystem. SAP BTP unifies AI agents, applications, and data across SAP and third-party landscapes with secure, API-ready integrations.
finops:
- name: Sap Btp Finops
  service_category: ''
  slug: sap-btp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sap-btp.png
jsonld:
- class_count: 0
  name: Sap Btp Context
  property_count: 0
  slug: sap-btp
layout: provider
modified: '2026-08-21'
name: SAP Business Technology Platform
nav: Providers
network: true
overview: 'SAP Business Technology Platform publishes 1 API on the [APIs.io](https://apis.io/) network: SAP BTP Core Services API. Tagged areas include SAP, Cloud Platform, Integration, Artificial Intelligence, and Data Management.


  The SAP Business Technology Platform catalog on APIs.io includes 1 JSON-LD context.


  SAP Business Technology Platform''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Sap Btp Plans Pricing
  plan_count: 5
  slug: sap-btp-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Sap Btp Rate Limits
  slug: sap-btp-rate-limits
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-btp/refs/heads/main/screenshots/sap-btp-2026-06-20T193421.png
security:
- kind: domain-security
  name: Sap Btp Domain Security
  slug: sap-btp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Btp Vulnerability Disclosure
  slug: sap-btp-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-btp
tags:
- SAP
- Cloud Platform
- Integration
- Artificial Intelligence
- Data Management
- Analytics
- Application Development
- Enterprise
website: https://www.sap.com/products/technology-platform.html
---
