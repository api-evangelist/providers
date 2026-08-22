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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: Core REST API for Service Cloud operations including cases, knowledge articles, and customer interactions.
  name: Service Cloud REST API
  slug: service-cloud-rest-api
- description: Specialized API for managing support cases, case routing, and escalations.
  name: Service Cloud Case Management API
  slug: service-cloud-case-management-api
- description: API for managing knowledge articles, categories, and knowledge base operations.
  name: Service Cloud Knowledge API
  slug: service-cloud-knowledge-api
- description: API for managing omni-channel routing, presence, and work assignments.
  name: Service Cloud Omni-Channel API
  slug: service-cloud-omni-channel-api
- description: API for real-time chat and messaging with customers.
  name: Service Cloud Live Agent API
  slug: service-cloud-live-agent-api
- description: API for building and managing AI-powered chatbots for customer service.
  name: Service Cloud Einstein Bots API
  slug: service-cloud-einstein-bots-api
- description: API for receiving near real-time notifications of changes to Service Cloud data.
  name: Service Cloud Streaming API
  slug: service-cloud-streaming-api
- description: Computer Telephony Integration API for connecting phone systems with Service Cloud.
  name: Service Cloud CTI API
  slug: service-cloud-cti-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/service-cloud-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forcedotcom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/salesforce-for-service
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
- group: auth
  title: ''
  type: Authentication
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_authentication.htm
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
- group: build
  title: ''
  type: SDKs
  url: https://developer.salesforce.com/tools/sdks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
created: '2024-01-15'
description: A collection of APIs for Salesforce Service Cloud, enabling customer service and support operations.
finops:
- name: Service Cloud Finops
  service_category: API
  slug: service-cloud-finops
image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
layout: provider
modified: '2024-01-15'
name: Salesforce Service Cloud APIs
nav: Providers
network: true
overview: 'Salesforce Service Cloud APIs publishes 1 API on the [APIs.io](https://apis.io/) network: Service Cloud REST API. Tagged areas include Cloud, CRM, Customer-Service, Enterprise, and Salesforce.


  Salesforce Service Cloud APIs'' developer surface includes developer portal, getting-started guide, authentication, support, and 8 more developer resources.'
plans:
- name: Service Cloud Plans Pricing
  plan_count: 3
  slug: service-cloud-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Service Cloud Rate Limits
  slug: service-cloud-rate-limits
score:
  band: thin
  composite: 30.2
  delta: -2.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 45.2
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 32.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/service-cloud/refs/heads/main/screenshots/service-cloud-2026-06-20T193724.png
security:
- kind: domain-security
  name: Service Cloud Domain Security
  slug: service-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: service-cloud
tags:
- Cloud
- CRM
- Customer-Service
- Enterprise
- Salesforce
- Support
website: https://developer.salesforce.com/
---
