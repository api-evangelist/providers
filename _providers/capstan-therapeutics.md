---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://capstantx.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.abbvie.com/capstan-therapeutics.html — a different registrable domain (capstantx.com -> abbvie.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://capstantx.com/
coverage:
  checked: '2026-08-09'
  detail: 'Capstan''s own site is gone: capstantx.com 301s to www.abbvie.com/capstan-therapeutics.html and its nameservers are now ns1-4.abbviedns.com, following AbbVie''s completed acquisition on 19 August 2025 — the company was a clinical-stage biotech that never operated a developer program, GitHub org, or public API.'
  evidence:
  - status: 301
    url: https://capstantx.com/
  - status: 301
    url: https://www.capstantx.com/
  - status: 403
    url: https://capstantx.com/.well-known/agent-card.json
  - status: 403
    url: https://capstantx.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/capstantx
  reason: defunct
  state: none
created: '2026-08-09'
description: Capstan Therapeutics was a clinical-stage biotechnology company based in San Diego, California, developing in vivo cell engineering medicines built on a proprietary targeted lipid nanoparticle (tLNP) platform that delivers mRNA and other RNA payloads to specific cell types inside the body. Its lead candidate CPTX2309 is an anti-CD19 in vivo CAR-T therapy in Phase 1 for B cell-mediated autoimmune disease, intended to achieve deep B cell depletion without lymphodepleting chemotherapy. AbbVie completed its acquisition of Capstan on 19 August 2025 for up to $2.1 billion. The company's own domain now redirects to AbbVie and its DNS is served by AbbVie nameservers; it operates no developer program, public API, SDK, or machine-readable specification.
layout: provider
modified: '2026-08-09'
name: Capstan Therapeutics
nav: Providers
network: true
overview: Capstan Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Cell Therapy, and Immunology.
random_paper: 9
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 1
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capstan-therapeutics/refs/heads/main/screenshots/capstan-therapeutics-2026-09-02T145011.png
slug: capstan-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Cell Therapy
- Immunology
- Life Sciences
- Acquired
website: https://capstantx.com/
---
