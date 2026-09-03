---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Versioned REST Content API with 67 documented operations across content, collections, comments, reminders, tasks, visibility, ideas, initiatives, custom fields, content types, destinations, membership
  name: Kapost Content API
  slug: kapost-content-api
artifact_total: 7
asyncapis:
- description: ''
  name: Kapost Webhooks
  slug: kapost-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://kapost.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kapost.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kapost.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kapost.com/content-api-responses
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kapost.com/api-getting-started
- group: start
  title: ''
  type: Login
  url: https://app.kapost.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: https://support.uplandsoftware.com/portal/ss/login
- group: company
  title: ''
  type: Blog
  url: https://uplandsoftware.com/kapost/resources/blog/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kapost-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kapost-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kapost-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/kapost-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kapost-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kapost-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uplandsoftware.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kapost
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kapost-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/kapost-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kapost-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kapost-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.uplandsoftware.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/kapost-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kapost-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kapost-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kapost-rate-limits.yml
created: '2026-07-17'
description: Kapost is a content operations platform — now part of Upland Software — that lets B2B marketing teams plan, produce, distribute, and analyze content across the customer journey through its Canvas, Studio, Gallery, and Insights modules. Kapost exposes a versioned REST Content API (/api/v1) secured with HTTP Basic authentication using a per-user API token and returning JSON, plus outbound content webhooks (create/update/publish/delete), an XML-RPC interface, and a first-party WordPress plugin for publishing content from Kapost to WordPress sites. This profile was enriched from Kapost's live developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kapost.png
layout: provider
modified: '2026-08-13'
name: Kapost
nav: Providers
network: true
overview: 'Kapost publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Content Operations, Content Marketing, Content Management, Marketing, and Sales Enablement.


  The Kapost catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kapost''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 18 more developer resources.'
plans:
- name: Kapost Plans Pricing
  plan_count: 0
  slug: kapost-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Kapost Rate Limits
  slug: kapost-rate-limits
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 41.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kapost/refs/heads/main/screenshots/kapost-2026-07-25T223456.png
security:
- kind: authentication
  name: Kapost Authentication
  slug: kapost-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kapost Domain Security
  slug: kapost-domain-security
  summary_line: TLSv1.2 · HSTS
- kind: trust-center
  name: Kapost Trust Center
  slug: kapost-trust-center
  summary_line: SOC 2 Type 2, SOC 1 Type 2, ISO/IEC 27001:2022, PCI DSS, CSA STAR Level 1, GDPR, CCPA, PIPEDA, GLBA, EU-US Data Privacy Framework, Swiss-US Data Privacy Framework, UK Extension to the EU-US Data Privacy Framework
slug: kapost
tags:
- Content Operations
- Content Marketing
- Content Management
- Marketing
- Sales Enablement
- Webhook
- REST API
- B2B
- Upland Software
website: https://kapost.com/
---
