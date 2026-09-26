---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/seismic/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/percolate/refs/heads/main/security/percolate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/percolate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://percolate.com
- group: start
  title: ''
  type: Login
  url: https://percolate.com/app/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seismic.com/percolate-privacy-policy/
created: '2026-07-17'
description: Percolate was a New York-based content marketing and marketing-orchestration platform, backed by Lightspeed Venture Partners and Slow Ventures, that helped enterprise marketing teams plan, create, and distribute campaign content. The company was acquired by Seismic in 2019 and the product has been folded into the Seismic marketing-enablement platform. As of this enrichment pass percolate.com serves only a "Percolate is now a part of the Seismic platform" landing page with a product login; all former developer, documentation, and API endpoints (developer/docs/api subdomains) no longer resolve, so there is no independent, active API surface to catalog for this provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/percolate.png
layout: provider
modified: '2026-09-15'
name: Percolate
nav: Providers
network: true
overview: Percolate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Content Marketing, Marketing Technology, and Marketing Enablement.
random_paper: 13
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/percolate/refs/heads/main/screenshots/percolate-2026-09-02T151036.png
security:
- kind: domain-security
  name: Percolate Domain Security
  slug: percolate-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: percolate
tags:
- Company
- Marketing
- Content Marketing
- Marketing Technology
- Marketing Enablement
- Acquired
- Defunct
website: https://percolate.com
---
