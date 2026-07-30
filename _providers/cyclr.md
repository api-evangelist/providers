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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Cyclr Agentic Access
  operation_count: 28
  slug: cyclr-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 9
apis:
- description: Manage Cyclr accounts
  name: Cyclr Accounts API
  slug: cyclr-accounts-api
- description: Obtain access tokens for API authentication
  name: Cyclr Authentication API
  slug: cyclr-authentication-api
- description: Manage and install connectors
  name: Cyclr Connectors API
  slug: cyclr-connectors-api
- description: Manage integration cycles
  name: Cyclr Cycles API
  slug: cyclr-cycles-api
- description: API-driven data requests (proxy)
  name: Cyclr Data on Demand API
  slug: cyclr-data-on-demand-api
- description: Deploy LAUNCH integration UI for end users
  name: Cyclr LAUNCH API
  slug: cyclr-launch-api
- description: Deploy Marketplace integration UI for end users
  name: Cyclr Marketplace API
  slug: cyclr-marketplace-api
- description: Manage cycle steps, parameters, and field mappings
  name: Cyclr Steps API
  slug: cyclr-steps-api
- description: Manage and install integration templates
  name: Cyclr Templates API
  slug: cyclr-templates-api
artifact_total: 27
asyncapis:
- description: AsyncAPI specification for Cyclr webhook events. Cyclr is an embedded iPaaS/integration platform that emits webhook notifications when key events occur within accounts, cycles, connectors, and templat
  name: Cyclr Webhook Events
  slug: cyclr-cyclr-asyncapi
collections:
- collection_type: open
  name: Cyclr API
  slug: open-cyclr-cyclr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cyclr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyclr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyclr-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cyclr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cyclr-systems-ltd
- group: company
  title: ''
  type: Website
  url: https://cyclr.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://cyclr.com/product/pricing
- group: other
  title: ''
  type: CaseStudies
  url: https://cyclr.com/case-studies
- group: learn
  title: ''
  type: Webinars
  url: https://cyclr.com/resources/webinars
- group: company
  title: ''
  type: Blog
  url: https://cyclr.com/blog
- group: other
  title: ''
  type: Branding
  url: https://cyclr.com/brand
- group: company
  title: ''
  type: Partners
  url: https://cyclr.com/become-a-partner
- group: auth
  title: ''
  type: Security
  url: https://cyclr.com/security-and-compliance
- group: auth
  title: ''
  type: GDPR
  url: https://cyclr.com/legal/gdpr-compliance
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://cyclr.com/sla
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.cyclr.com/user-documentation/release-notes/introduction-to-release-notes
- group: start
  title: ''
  type: Login
  url: https://my.cyclr.com/account/login
- group: other
  title: ''
  type: GetStarted
  url: https://cyclr.com/get-started
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cyclr-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/cyclr-api-capabilities.yml
- group: design
  title: ''
  type: Rules
  url: rules/cyclr-api-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://cyclr.com/llms.txt
created: '2025-06-06'
description: Cyclr is an embedded iPaaS (integration platform as a service) used by SaaS vendors to deliver native integrations to their customers without each vendor building and maintaining one-off connectors. The platform provides a connector library covering hundreds of business applications (CRM, marketing, finance, support, ERP, e-commerce), drag-and-drop integration templates, embedded LAUNCH and Marketplace UIs, custom connector creation, fully managed authentication, and workflow orchestration. Cyclr exposes a public REST API at api.cyclr.com (with regional EU / AU / UK / US2 siblings) protected by OAuth 2.0 client credentials. Account-scoped calls require an X-Cyclr-Account header to identify the target Cyclr account.
finops:
- name: Cyclr Finops
  service_category: API
  slug: cyclr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cyclr.png
json_schemas:
- name: Cyclr Account
  property_count: 7
  slug: cyclr-account
- name: Cyclr Connector
  property_count: 7
  slug: cyclr-connector
- name: Cyclr Cycle
  property_count: 8
  slug: cyclr-cycle
- name: Cyclr Installed Connector
  property_count: 6
  slug: cyclr-installed-connector
- name: Cyclr Step
  property_count: 5
  slug: cyclr-step
- name: Cyclr Template
  property_count: 5
  slug: cyclr-template
jsonld:
- class_count: 0
  name: Cyclr Context
  property_count: 6
  slug: cyclr-context
layout: provider
modified: '2026-05-19'
name: Cyclr
nav: Providers
network: true
overview: 'Cyclr publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Connectors API, and 6 more. Tagged areas include Connectors, Custom Connectors, Data Synchronization, Embedded iPaaS, and Embedded SaaS Integration.


  The Cyclr catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Cyclr''s developer surface includes authentication, pricing, engineering blog, changelog, and 18 more developer resources.'
plans:
- name: Cyclr Plans Pricing
  plan_count: 3
  slug: cyclr-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Cyclr Rate Limits
  slug: cyclr-rate-limits
rules:
- name: Cyclr API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: cyclr-api-rules
- name: Cyclr API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: cyclr-asyncapi-spectral-rules
- name: Cyclr API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cyclr-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.8
  delta: -3.4
  facets:
    commercial_clarity: 63.2
    contract_quality: 84.7
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 31.3
    operational_transparency: 63.2
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyclr/refs/heads/main/screenshots/cyclr-2026-06-20T175412.png
security:
- kind: authentication
  name: Cyclr Authentication
  slug: cyclr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cyclr Domain Security
  slug: cyclr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cyclr
tags:
- Connectors
- Custom Connectors
- Data Synchronization
- Embedded iPaaS
- Embedded SaaS Integration
- Embedded UI
- Integration Platform
- Integrations
- Marketplace
- OAuth 2.0
- REST API
- SaaS
- Templates
- Webhooks
- White Label
- Workflows
website: https://cyclr.com/
---
