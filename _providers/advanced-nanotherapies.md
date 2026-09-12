---
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://advancednanotherapies.com/
- group: company
  title: ''
  type: Blog
  url: https://advancednanotherapies.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://advancednanotherapies.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advancednanotherapies.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/advanced-nanotherapies
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advanced-nanotherapies-domain-security.yml
coverage:
  checked: '2026-09-07'
  detail: Advanced NanoTherapies is a clinical-stage interventional-device maker whose product is a physical dual-drug coated balloon (SirPlux Duo), not software - its WordPress marketing site exposes only company, product, news, privacy and terms pages, api/docs/developer/portal subdomains all NXDOMAIN, and there is no GitHub organization, SDK or machine-readable contract anywhere on its public surface.
  evidence:
  - status: 202
    url: https://advancednanotherapies.com/
  - status: 202
    url: https://advancednanotherapies.com/openapi.json
  - status: 202
    url: https://advancednanotherapies.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/search/users?q=advancednanotherapies
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: Advanced NanoTherapies, Inc. (ANT) is a clinical-stage medical device company founded in 2018 and based in Santa Clara / Los Gatos, California, applying nanoparticle engineering to vascular drug delivery. Its lead program, SirPlux Duo, is a dual-drug drug-coated balloon (DCB) that delivers sirolimus and paclitaxel simultaneously from a proprietary nanoparticle coating to inhibit restenosis in coronary and peripheral arteries, and it has received FDA Breakthrough Device designations for small-vessel coronary artery disease, coronary in-stent restenosis and below-the-knee peripheral lesions. The company builds physical interventional devices rather than software; it operates no developer program and publishes no public API, SDK, webhook surface or machine-readable API contract.
layout: provider
modified: '2026-09-07'
name: Advanced NanoTherapies
nav: Providers
network: true
overview: 'Advanced NanoTherapies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Technology, Health Care, and Life Sciences.


  Advanced NanoTherapies'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advanced Nanotherapies Domain Security
  slug: advanced-nanotherapies-domain-security
  summary_line: TLSv1.3
slug: advanced-nanotherapies
tags:
- Company
- Medical Devices
- Medical Technology
- Health Care
- Life Sciences
- Nanotechnology
- Cardiovascular
- Drug Delivery
website: https://advancednanotherapies.com/
---
