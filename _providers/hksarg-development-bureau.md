---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/hksarg-development-bureau/hosts/hksarg-development-bureau-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hksarg-development-bureau-hosts.yml
- group: auth
  href: https://artifacts.apis.io/hksarg-development-bureau/security/hksarg-development-bureau-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hksarg-development-bureau-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.devb.gov.hk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.devb.gov.hk/en/home/index.html
coverage:
  checked: '2026-10-26'
  detail: The developer site returns a JavaScript shell with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.devb.gov.hk/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: The Hong Kong Special Administrative Region Government Development Bureau (HKSARG Development Bureau) is responsible for planning, land use, and urban development policies in Hong Kong. It provides public information, regulatory guidance, and data services related to construction, land allocation, and development projects. The bureau’s website offers resources for developers, stakeholders, and the public, including project updates, policy documents, and contact information.
layout: provider
modified: '2026-10-26'
name: HKSARG, Development Bureau
nav: Providers
network: true
overview: 'HKSARG, Development Bureau is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Urban Planning, Development, and Hong Kong.


  HKSARG, Development Bureau''s developer surface includes documentation and 3 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hksarg-development-bureau/hksarg-development-bureau-2026-11-03T133434.png
security:
- kind: domain-security
  name: Hksarg Development Bureau Domain Security
  slug: hksarg-development-bureau-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hksarg-development-bureau
tags:
- Company
- Government
- Urban Planning
- Development
- Hong Kong
website: https://www.devb.gov.hk/
---
