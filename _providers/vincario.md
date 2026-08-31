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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Vincario Agentic Access
  operation_count: 5
  slug: vincario-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: The Account API from Vincario — 1 operation(s) for account.
  name: Vincario Account API
  slug: vincario-account-api
- description: The Decode API from Vincario — 1 operation(s) for decode.
  name: Vincario Decode API
  slug: vincario-decode-api
- description: The Market Value API from Vincario — 1 operation(s) for market value.
  name: Vincario Market Value API
  slug: vincario-market-value-api
- description: The Stolen Check API from Vincario — 1 operation(s) for stolen check.
  name: Vincario Stolen Check API
  slug: vincario-stolen-check-api
- description: The Vehicle Info API from Vincario — 1 operation(s) for vehicle info.
  name: Vincario Vehicle Info API
  slug: vincario-vehicle-info-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vincario VIN Decoder Account API
  slug: open-vincario-account-api
- collection_type: open
  name: Vincario VIN Decoder Account Decode API
  slug: open-vincario-decode-api
- collection_type: open
  name: Vincario VIN Decoder Account Market Value API
  slug: open-vincario-market-value-api
- collection_type: open
  name: Vincario VIN Decoder Account Stolen Check API
  slug: open-vincario-stolen-check-api
- collection_type: open
  name: Vincario VIN Decoder Account Vehicle Info API
  slug: open-vincario-vehicle-info-api
- collection_type: open
  name: Vincario VIN Decoder API
  slug: open-vincario
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vincario-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vincario-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vincario-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vincario-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vincario
- group: company
  title: ''
  type: Website
  url: https://vincario.com
- group: docs
  title: ''
  type: Documentation
  url: https://vindecoder.eu/api
- group: commercial
  title: ''
  type: Plans
  url: plans/vincario-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vincario-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vincario-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://vincario.com/blog/feed/
created: '2026-06-21'
description: Vincario operates the vindecoder.eu VIN Decoder API, a global REST service that decodes a Vehicle Identification Number (VIN) into a full vehicle specification and provides vehicle market value, stolen-vehicle checks, and account balance. Requests are authenticated with an API key plus a SHA1 control sum embedded in the URL path.
finops:
- name: Vincario Finops
  service_category: Data and Analytics
  slug: vincario-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vincario.png
layout: provider
modified: '2026-06-21'
name: Vincario
nav: Providers
network: true
overview: 'Vincario publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Decode API, Market Value API, and 2 more. Tagged areas include VIN, Vehicle Data, Automotive, VIN Decoder, and Market Value.


  Vincario''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Vincario Plans Pricing
  plan_count: 5
  slug: vincario-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Vincario Rate Limits
  slug: vincario-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Vincario Authentication
  slug: vincario-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vincario Domain Security
  slug: vincario-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Vincario Vulnerability Disclosure
  slug: vincario-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vincario
tags:
- VIN
- Vehicle Data
- Automotive
- VIN Decoder
- Market Value
website: https://vincario.com
---
