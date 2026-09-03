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
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Nectar Hr Agentic Access
  operation_count: 9
  slug: nectar-hr-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.nectarhr.com
  baseurl_source: declared
  description: The Analytics API from Nectar — 1 operation(s) for analytics.
  name: Nectar Analytics API
  slug: nectar-hr-analytics-api
- baseURL: https://api.nectarhr.com
  baseurl_source: declared
  description: The Custom Awards API from Nectar — 2 operation(s) for custom awards.
  name: Nectar Custom Awards API
  slug: nectar-hr-custom-awards-api
- baseURL: https://api.nectarhr.com
  baseurl_source: declared
  description: The Flows API from Nectar — 1 operation(s) for flows.
  name: Nectar Flows API
  slug: nectar-hr-flows-api
- baseURL: https://api.nectarhr.com
  baseurl_source: declared
  description: The Health API from Nectar — 1 operation(s) for health.
  name: Nectar Health API
  slug: nectar-hr-health-api
- baseURL: https://api.nectarhr.com
  baseurl_source: declared
  description: The Recognition API from Nectar — 1 operation(s) for recognition.
  name: Nectar Recognition API
  slug: nectar-hr-recognition-api
- baseURL: https://api.nectarhr.com
  baseurl_source: declared
  description: The Users API from Nectar — 2 operation(s) for users.
  name: Nectar Users API
  slug: nectar-hr-users-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nectar Public Analytics API
  slug: open-nectar-hr-analytics-api
- collection_type: open
  name: Nectar Public Analytics Custom Awards API
  slug: open-nectar-hr-custom-awards-api
- collection_type: open
  name: Nectar Public Analytics Flows API
  slug: open-nectar-hr-flows-api
- collection_type: open
  name: Nectar Public Analytics Health API
  slug: open-nectar-hr-health-api
- collection_type: open
  name: Nectar Public Analytics Recognition API
  slug: open-nectar-hr-recognition-api
- collection_type: open
  name: Nectar Public Analytics Users API
  slug: open-nectar-hr-users-api
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
random_paper: 18
rate_limits:
- limit_count: 6
  name: Nectar Hr Rate Limits
  slug: nectar-hr-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 52.3
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
