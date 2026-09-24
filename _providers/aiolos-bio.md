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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://aiolosbio.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aiolos-bio
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/aiolos-bio_stock/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiolos-bio/refs/heads/main/security/aiolos-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiolos-bio-domain-security.yml
coverage:
  checked: '2026-09-14'
  detail: Aiolos Bio was a clinical-stage asthma-antibody developer that ceased to exist as an independent company when GSK completed its acquisition on 2024-02-14, and its domain aiolosbio.com now answers every path — including /.well-known/security.txt, /openapi.json and /llms.txt — with a blanket HTTP 301 to https://www.gsk.com/, while api., docs., developer. and portal.aiolosbio.com are all NXDOMAIN, so there is no surviving host, developer program or contract to profile.
  evidence:
  - status: 301
    url: https://aiolosbio.com/.well-known/security.txt
  - status: 301
    url: https://aiolosbio.com/openapi.json
  - status: 200
    url: https://www.gsk.com/en-gb/media/press-releases/gsk-completes-acquisition-of-aiolos-bio/
  - status: 403
    url: https://forgeglobal.com/aiolos-bio_stock/
  reason: defunct
  state: none
created: '2026-09-14'
description: 'Aiolos Bio was a clinical-stage biopharmaceutical company founded in 2023 with offices in San Francisco, California and London, United Kingdom, developing treatments for respiratory and inflammatory disease. Its sole disclosed asset was AIO-001, a half-life-extended monoclonal antibody against thymic stromal lymphopoietin (TSLP), positioned as a Phase 2-ready candidate for moderate-to-severe asthma with potential six-month dosing intervals. The company launched in October 2023 with an oversubscribed $245 million Series A co-led by Atlas Venture, Bain Capital Life Sciences, Forbion and Sofinnova Investments, with RA Capital Management. GSK plc agreed to acquire it on 9 January 2024 for $1 billion upfront plus up to $400 million in milestones, completing on 14 February 2024. Aiolos Bio is a drug developer, not a software vendor: it never ran a developer program, public API, SDK or machine-readable contract, and aiolosbio.com now serves a blanket HTTP 301 to www.gsk.com on every
  path.'
layout: provider
modified: '2026-09-14'
name: Aiolos Bio
nav: Providers
network: true
overview: Aiolos Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Biopharmaceutical, Pharmaceuticals, and Drug Development.
random_paper: 16
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 3
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
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiolos Bio Domain Security
  slug: aiolos-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiolos-bio
tags:
- Company
- Biotechnology
- Biopharmaceutical
- Pharmaceuticals
- Drug Development
- Clinical Trials
- Respiratory
- Immunology
- Monoclonal Antibodies
- Life Sciences
- Acquired
website: https://aiolosbio.com/
---
