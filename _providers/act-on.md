---
access_model:
  confidence: high
  label: Paid plan plus a free developer sandbox by request
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - sandbox
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: OAuth 2.0 REST API for Act-On marketing automation — contacts and lists, segments, email messages and campaigns, media and creative assets, landing pages and forms, subscriptions, imports, custom even
  name: Act-On REST API
  slug: act-on-rest-api
- description: Separately versioned (3.4.3) Custom Data service for defining custom object schemas and fields, creating datasets, validating and ingesting CSV/JSON data, polling ingest jobs, and querying custom data
  name: Act-On Custom Objects Service
  slug: act-on-custom-objects-service
- description: Outgoing webhook event surface — nineteen documented event types across contacts, consent, deliverability, lead scoring, subscriptions, automated programs, messaging, forms and CRM connections. Payloa
  name: Act-On Outgoing Webhooks
  slug: act-on-outgoing-webhooks
artifact_total: 15
asyncapis:
- description: ''
  name: Act On Webhooks
  slug: act-on-webhooks
collections:
- collection_type: open
  name: Custom Objects Service
  slug: open-act-on-custom-objects-service
- collection_type: open
  name: oauth
  slug: open-act-on-oauth
- collection_type: open
  name: act-on-api-raw-body
  slug: open-act-on-raw-body-api
- collection_type: open
  name: act-on-api-1
  slug: open-act-on-rest-api
common:
- group: company
  title: ''
  type: Website
  url: https://act-on.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.act-on.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.act-on.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.act-on.com/reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.act-on.com/reference/request-a-developer-account
- group: operate
  title: ''
  type: HelpCenter
  url: https://connect.act-on.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://act-on.com/product/services/support-packages/
- group: company
  title: ''
  type: Blog
  url: https://act-on.com/learn/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://act-on.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://act-on.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://act-on.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.act-on.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://connect.act-on.com/hc/en-us/categories/13386837131927-What-s-New
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/act-on-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/act-on-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/act-on-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/act-on-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/act-on-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/act-on-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/act-on-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/act-on-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/act-on-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/act-on-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/act-on-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/act-on-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/act-on-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/act-on-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/act-on-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/act-on-domain-security.yml
created: '2026-07-17'
description: 'Act-On Software is a cloud-based marketing automation platform used by B2B and B2C marketing teams for email marketing, lead generation and nurturing, landing pages and forms, website visitor tracking, lead scoring and segmentation, custom data, and campaign reporting. Act-On publishes four OpenAPI 3.1 documents through its developer portal covering 158 operations on one gateway host (https://api.actonsoftware.com, with an EU region at api-eu.actonsoftware.com): the legacy form-encoded /api/1 surface, the newer JSON Act-On Contacts layer at /ucl/v2, a transactional email endpoint at /ete/v1, and a separately versioned Custom Objects Service at /custom-objects/v1 that is in request-only beta. Authentication is OAuth 2.0 with password, refresh_token and authorization_code grants and no scopes. Act-On also ships a signed outgoing-webhook event surface with nineteen documented event types. Added to the API Evangelist network from a Norwest Venture Partners portfolio lead and enriched
  from Act-On''s public developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/act-on.png
layout: provider
mcp_servers:
- description: ''
  name: act-on-mcp.yml
  slug: act-on-mcpyml
modified: '2026-08-13'
name: Act-On
nav: Providers
network: true
overview: 'Act-On publishes 2 APIs on the [APIs.io](https://apis.io/) network: REST API and Custom Objects Service. Tagged areas include Company, Marketing, Marketing Automation, Email Marketing, and Email.


  The Act-On catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Act-On''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 23 more developer resources.'
plans:
- name: Act On Plans Pricing
  plan_count: 2
  slug: act-on-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Act On Rate Limits
  slug: act-on-rate-limits
scopes:
- name: Act On Scopes
  scope_count: 0
  slug: act-on-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.2
  delta: -7.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 16.7
    contract_quality: 65.0
    developer_ergonomics: 55.4
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 71.1
  previous_composite: 60.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/act-on/refs/heads/main/screenshots/act-on-2026-07-25T181520.png
security:
- kind: authentication
  name: Act On Authentication
  slug: act-on-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Act On Domain Security
  slug: act-on-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Act On Trust Center
  slug: act-on-trust-center
  summary_line: ISO 27001, HIPAA, TX-RAMP, TRUSTe
slug: act-on
tags:
- Company
- Marketing
- Marketing Automation
- Email Marketing
- Email
- Marketing Technology
- Lead Generation
- Campaign Management
- Customer Data
- Webhooks
- API
website: https://act-on.com
---
