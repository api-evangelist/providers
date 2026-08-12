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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Nectar Hr Agentic Access
  operation_count: 9
  slug: nectar-hr-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 6
apis:
- description: The Analytics API from Nectar — 1 operation(s) for analytics.
  name: Nectar Analytics API
  slug: nectar-hr-analytics-api
- description: The Custom Awards API from Nectar — 2 operation(s) for custom awards.
  name: Nectar Custom Awards API
  slug: nectar-hr-custom-awards-api
- description: The Flows API from Nectar — 1 operation(s) for flows.
  name: Nectar Flows API
  slug: nectar-hr-flows-api
- description: The Health API from Nectar — 1 operation(s) for health.
  name: Nectar Health API
  slug: nectar-hr-health-api
- description: The Recognition API from Nectar — 1 operation(s) for recognition.
  name: Nectar Recognition API
  slug: nectar-hr-recognition-api
- description: The Users API from Nectar — 2 operation(s) for users.
  name: Nectar Users API
  slug: nectar-hr-users-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nectar-hr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nectar-hr-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nectar-hr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nectar-hr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nectar-hr-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nectarhr
- group: company
  title: ''
  type: Website
  url: https://nectarhr.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.nectarhr.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/nectar-hr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nectar-hr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nectar-hr-finops.yml
created: '2026-07-10'
description: Nectar is an employee recognition and rewards platform that helps organizations build culture through peer-to-peer and manager recognition, a points-based global rewards catalog (gift cards, Amazon, swag, custom company rewards), automated milestone celebrations, and internal comms. Nectar exposes a documented Open API (base https://api.nectarhr.com, Swagger at /docs) covering users, the company recognition feed, custom awards, financial redemption analytics, and Flow triggers. The API is an account add-on - access is enabled by Nectar support/your account manager and then a scoped API key is generated in Settings > Integrations; all endpoints use Bearer (JWT) authentication.
finops:
- name: Nectar Hr Finops
  service_category: HR and Employee Recognition
  slug: nectar-hr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nectar-hr.png
layout: provider
modified: '2026-07-10'
name: Nectar
nav: Providers
network: true
overview: 'Nectar publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Custom Awards API, Flows API, and 3 more. Tagged areas include Employee Recognition, Rewards, Points, HR, and Employee Engagement.


  Nectar''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Nectar Hr Plans Pricing
  plan_count: 4
  slug: nectar-hr-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 6
  name: Nectar Hr Rate Limits
  slug: nectar-hr-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -0.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nectar-hr/refs/heads/main/screenshots/nectar-hr-2026-08-07T184814.png
security:
- kind: authentication
  name: Nectar Hr Authentication
  slug: nectar-hr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nectar Hr Domain Security
  slug: nectar-hr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nectar Hr Vulnerability Disclosure
  slug: nectar-hr-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nectar Hr Trust Center
  slug: nectar-hr-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: nectar-hr
tags:
- Employee Recognition
- Rewards
- Points
- HR
- Employee Engagement
- Culture
- People Operations
website: https://nectarhr.com
---
