---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: June Agentic Access
  operation_count: 4
  slug: june-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 6
apis:
- description: Pro Plan add-on API that allows embedding June analytics dashboards directly into customer-facing products, enabling teams to surface product metrics for individual accounts within their own applicati
  name: June Embed API
  slug: embed-api
- description: API for managing data within the June platform, including the ability to delete users and workspaces to support GDPR and privacy compliance requirements.
  name: June Data Deletions API
  slug: data-deletions-api
- description: The Companies API from June — 1 operation(s) for companies.
  name: June Companies API
  slug: june-companies-api
- description: The Events API from June — 1 operation(s) for events.
  name: June Events API
  slug: june-events-api
- description: The Page Views API from June — 1 operation(s) for page views.
  name: June Page Views API
  slug: june-page-views-api
- description: The Users API from June — 1 operation(s) for users.
  name: June Users API
  slug: june-users-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/june-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/june-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/june-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/june-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/june-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.june.so/
- group: docs
  title: ''
  type: Documentation
  url: https://www.june.so/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/juneHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/juneso
- group: other
  title: ''
  type: X
  url: https://x.com/juneDotSo
- group: company
  title: ''
  type: Blog
  url: https://www.june.so/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.june.so
- group: commercial
  title: ''
  type: Pricing
  url: https://www.june.so/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/june/refs/heads/main/plans/june-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/june/refs/heads/main/rate-limits/june-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/june/refs/heads/main/finops/june-finops.yml
created: '2026-06-12'
description: June is a product analytics platform purpose-built for B2B SaaS companies, providing company-level and user-level analytics focused on key SaaS metrics such as activation, retention, and feature adoption. The platform offers a REST-based Tracking API compatible with the Segment protocol, enabling teams to identify users, track events, group users into companies, and record page views. June also provides server-side SDKs for Node.js, Python, and Ruby, as well as client-side JavaScript and React/Next.js libraries. An Embed API (available as a Pro Plan add-on) allows embedding June dashboards directly into customer-facing products, and a Data Deletions API supports GDPR compliance by enabling deletion of user and workspace data.
examples:
- key_count: 4
  name: June Group Company Example
  slug: june-group-company-example
- key_count: 3
  name: June Identify User Example
  slug: june-identify-user-example
- key_count: 4
  name: June Page View Example
  slug: june-page-view-example
- key_count: 5
  name: June Track Event Example
  slug: june-track-event-example
finops:
- name: June Finops
  service_category: ''
  slug: june-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/june.png
json_schemas:
- name: June Group Request
  property_count: 6
  slug: june-group-request
- name: June Identify Request
  property_count: 5
  slug: june-identify-request
- name: June Page Request
  property_count: 5
  slug: june-page-request
- name: June Track Request
  property_count: 6
  slug: june-track-request
jsonld:
- class_count: 7
  name: June Context
  property_count: 22
  slug: june-context
layout: provider
modified: '2026-06-12'
name: June
nav: Providers
network: true
overview: 'June publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Events API, Page Views API, and 1 more. Tagged areas include Analytics, Product Analytics, B2B SaaS, Event Tracking, and Segment Compatible.


  The June catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  June''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 11 more developer resources.'
plans:
- name: June Plans Pricing
  plan_count: 2
  slug: june-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 3
  name: June Rate Limits
  slug: june-rate-limits
rules:
- name: June API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: june-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 75.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/june/refs/heads/main/screenshots/june-2026-06-20T183828.png
security:
- kind: authentication
  name: June Authentication
  slug: june-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: June Domain Security
  slug: june-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: June Vulnerability Disclosure
  slug: june-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: June Trust Center
  slug: june-trust-center
  summary_line: SOC 2, GDPR
slug: june
tags:
- Analytics
- Product Analytics
- B2B SaaS
- Event Tracking
- Segment Compatible
- Retention
- Feature Adoption
- Activation
website: https://www.june.so/
---
