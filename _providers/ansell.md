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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/ansell/well-known/ansell-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ansell-security.txt
- group: agent
  href: https://artifacts.apis.io/ansell/well-known/ansell-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ansell-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ansell.com/us/en/legal/vulnerability-disclosure-policy
- group: other
  href: https://artifacts.apis.io/ansell/hosts/ansell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ansell-hosts.yml
- group: other
  href: https://artifacts.apis.io/ansell/vendors/ansell-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ansell-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ansell/security/ansell-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ansell-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ansell/security/ansell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ansell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ansell.com/
- group: company
  title: ''
  type: Investors
  url: https://investor.ansell.com/investor-centre/
- group: operate
  title: ''
  type: Contact
  url: https://investor.ansell.com/contact/?page=investor-relations
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ansell.com/int/en/legal/privacy-policy
created: '2026-10-21'
description: 'Ansell Limited (ASX: ANN) is an Australian-headquartered global manufacturer of personal protective equipment, describing itself as "a global leader in personal protection and safety solutions, enabling safer workforces through quality, expertise, and sustainable innovation." It operates Healthcare (surgical and examination gloves) and Industrial (hand and chemical protection) segments. The company traces its origins to 1893 (Dunlop Perdriau, later Pacific Dunlop) and took the Ansell name in 2002. It publishes no public developer API. Ansell was surfaced through the API Evangelist harvest backlog (australia-apidays-2026).'
image: https://investor.ansell.com/FormBuilder/_Resource/_module/WEtAsUy_jk6Kmk_vOw9f5g/image/ansell_logo_2025.png
layout: provider
modified: '2026-10-21'
name: Ansell
nav: Providers
network: true
overview: Ansell is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Personal Protective Equipment, Gloves, Healthcare, and Manufacturing.
random_paper: 15
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
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
  previous_composite: 8.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ansell/ansell-2026-11-03T120847.png
security:
- kind: domain-security
  name: Ansell Domain Security
  slug: ansell-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ansell Vulnerability Disclosure
  slug: ansell-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ansell
tags:
- Company
- Personal Protective Equipment
- Gloves
- Healthcare
- Manufacturing
- Industrial Safety
- Australia
website: https://www.ansell.com/
---
