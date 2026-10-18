---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Perenual Agentic Access
  operation_count: 5
  slug: perenual-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://perenual.com/api/v2
  baseurl_source: declared
  description: Plant care guides
  name: Perenual Care API
  slug: perenual-care-api
- baseURL: https://perenual.com/api/v2
  baseurl_source: declared
  description: Hardiness map data
  name: Perenual Maps API
  slug: perenual-maps-api
- baseURL: https://perenual.com/api/v2
  baseurl_source: declared
  description: Pest and disease data
  name: Perenual Pests API
  slug: perenual-pests-api
- baseURL: https://perenual.com/api/v2
  baseurl_source: declared
  description: Plant species data
  name: Perenual Species API
  slug: perenual-species-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Perenual Care API
  slug: open-perenual-care-api
- collection_type: open
  name: Perenual Care Maps API
  slug: open-perenual-maps-api
- collection_type: open
  name: Perenual API
  slug: open-perenual-perenual
- collection_type: open
  name: Perenual Care Pests API
  slug: open-perenual-pests-api
- collection_type: open
  name: Perenual Care Species API
  slug: open-perenual-species-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/plans/perenual-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/perenual-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/rate-limits/perenual-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/perenual-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/finops/perenual-finops.yml
  title: ''
  type: FinOps
  url: finops/perenual-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://perenual.com/blog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/agentic-access/perenual-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/perenual-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/security/perenual-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/perenual-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/security/perenual-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perenual-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/authentication/perenual-authentication.yml
  title: ''
  type: Authentication
  url: authentication/perenual-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://perenual.com
- group: docs
  title: ''
  type: Documentation
  url: https://perenual.com/docs/api
- group: agent
  title: ''
  type: LlmsText
  url: https://perenual.com/llms.txt
created: '2025-02-24'
description: Perenual provides a comprehensive plant database API offering access to over 10,000+ plant species, including details on care, watering, sunlight, edibility, toxicity, pests, diseases, and care guides.
finops:
- has_sources: false
  method: generated
  name: Perenual Finops
  primary_unit: ''
  service_category: API
  slug: perenual-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perenual.png
layout: provider
modified: '2026-10-06'
name: Perenual
nav: Providers
network: true
overview: 'Perenual publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Care API, Maps API, Pests API, and 1 more. Tagged areas include Plants, Botany, Gardening, and Horticulture.


  Perenual''s developer surface includes engineering blog, authentication, documentation, and 8 more developer resources.'
plans:
- name: Perenual Plans Pricing
  plan_count: 3
  slug: perenual-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Perenual Rate Limits
  slug: perenual-rate-limits
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 49.6
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/screenshots/perenual-2026-06-20T191559.png
security:
- kind: authentication
  name: Perenual Authentication
  slug: perenual-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Perenual Domain Security
  slug: perenual-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Perenual Vulnerability Disclosure
  slug: perenual-vulnerability-disclosure
  summary_line: no policy recorded
slug: perenual
tags:
- Plants
- Botany
- Gardening
- Horticulture
website: https://perenual.com
---
