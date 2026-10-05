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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Bertis services (no public spec found)
  name: Bertis API
  slug: bertis-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bertis/refs/heads/main/hosts/bertis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bertis-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.bertis.com/bbs/register.php
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bertis/refs/heads/main/security/bertis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bertis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bertis.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Bertis is a South Korean biotechnology company specializing in AI-driven proteomics solutions for precision medicine. It offers integrated platforms for protein analysis, early cancer detection biomarkers, and collaborative research services, aiming to accelerate drug development and personalized healthcare.
image: https://www.bertis.com/img/og_images.jpg
layout: provider
modified: '2026-09-27'
name: Bertis
nav: Providers
network: true
overview: 'Bertis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Proteomics, Precision Medicine, Artificial Intelligence, and South Korea.


  Bertis'' developer surface includes signup flow and 3 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bertis Domain Security
  slug: bertis-domain-security
  summary_line: TLSv1.2
slug: bertis
tags:
- Biotechnology
- Proteomics
- Precision Medicine
- Artificial Intelligence
- South Korea
website: https://www.bertis.com/
---
