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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acelyrin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acelyrin.com/
coverage:
  checked: '2026-09-06'
  detail: ACELYRIN was absorbed into Alumis, Inc. on 2025-05-21 as a wholly owned subsidiary and its corporate domain acelyrin.com now 301-redirects to www.alumis.com, so the only surviving surface belongs to the acquirer; the company was a clinical-stage drug developer that never published a developer portal, API, or GitHub organization.
  evidence:
  - status: 301
    url: https://acelyrin.com/
  - status: 200
    url: https://www.alumis.com/
  - status: 404
    url: https://acelyrin.com/.well-known/api-catalog
  - status: 404
    url: https://acelyrin.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/acelyrin
  reason: defunct
  state: none
created: '2026-09-06'
description: 'ACELYRIN, Inc. (Nasdaq: SLRN) was a late-stage clinical biopharmaceutical company headquartered in Agoura Hills, California, focused on accelerating the development and commercialization of medicines in immunology. Its lead candidates were izokibep, an anti-IL-17A small protein therapeutic, and lonigutamab, a humanized IgG1 monoclonal antibody against IGF-1R. It completed a $540M IPO in May 2023, and on May 21, 2025 it merged with a subsidiary of Alumis, Inc. and survives as a wholly owned Alumis subsidiary. Its corporate domain acelyrin.com now 301-redirects to alumis.com. The company is a drug developer, not a software vendor: it published no developer program, public API, SDK, webhook surface, or machine-readable specification, and no GitHub organization exists under the ACELYRIN name.'
layout: provider
modified: '2026-09-06'
name: ACELYRIN, Inc.
nav: Providers
network: true
overview: ACELYRIN, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharmaceutical, Biotechnology, Pharmaceuticals, and Immunology.
random_paper: 15
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
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
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
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acelyrin Domain Security
  slug: acelyrin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acelyrin
tags:
- Company
- Biopharmaceutical
- Biotechnology
- Pharmaceuticals
- Immunology
- Clinical Trials
- Healthcare
- Acquired
website: https://acelyrin.com/
---
