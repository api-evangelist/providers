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
- group: auth
  href: https://artifacts.apis.io/federation-university-australia/well-known/federation-university-australia-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/federation-university-australia-security.txt
- group: auth
  href: https://artifacts.apis.io/federation-university-australia/well-known/federation-university-australia-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/federation-university-australia-www-security.txt
- group: agent
  href: https://artifacts.apis.io/federation-university-australia/well-known/federation-university-australia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/federation-university-australia-well-known.yml
- group: other
  href: https://artifacts.apis.io/federation-university-australia/hosts/federation-university-australia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/federation-university-australia-hosts.yml
- group: other
  href: https://artifacts.apis.io/federation-university-australia/vendors/federation-university-australia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/federation-university-australia-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.federation.edu.au/privacy/
- group: other
  title: ''
  type: Leadership
  url: https://www.federation.edu.au/about/structure/leadership/
- group: auth
  href: https://artifacts.apis.io/federation-university-australia/security/federation-university-australia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/federation-university-australia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://federation.edu.au
coverage:
  checked: '2026-10-23'
  detail: The university website provides only standard HTML pages with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.federation.edu.au/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Federation University Australia is a public university offering a wide range of undergraduate and postgraduate courses across multiple campuses in Australia. It emphasizes cooperative education, industry placements, and research collaborations, providing students with practical experience and pathways to employment. The university’s mission is to deliver accessible, high‑quality education and foster innovation through strong community and industry partnerships.
image: https://www.federation.edu.au/contentassets/5de6b8829b7343528c6d662a0474eb9b/federation-uni_logo_blue-2024_rgb.png
layout: provider
modified: '2026-10-23'
name: Federation University Australia
nav: Providers
network: true
overview: Federation University Australia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, University, Australia, Higher Education, and CooperativeEducation.
random_paper: 19
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/federation-university-australia/federation-university-australia-2026-11-03T131925.png
security:
- kind: domain-security
  name: Federation University Australia Domain Security
  slug: federation-university-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: federation-university-australia
tags:
- Education
- University
- Australia
- Higher Education
- CooperativeEducation
- Company
website: http://federation.edu.au
---
