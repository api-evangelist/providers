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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-14'
  detail: AiBiotech's own domain aibiotech.com no longer belongs to the company — it is a HugeDomains for-sale parking lander that returns HTTP 200 with the identical sale page for every path probed, including /openapi.json and /.well-known/agent-card.json, and HTTPS on the domain does not answer at all.
  evidence:
  - status: 200
    url: http://aibiotech.com/
  - status: 200
    url: https://www.hugedomains.com/domain_profile.cfm?d=aibiotech.com
  - status: 200
    url: http://aibiotech.com/openapi.json
  - status: 404
    url: https://www.grangergenetics.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/aibiotech
  reason: defunct
  state: none
created: '2026-09-14'
description: AiBiotech (AIBioTech, American International Biotechnology) was a Richmond, Virginia contract research organization and CLIA/CAP clinical laboratory offering molecular biology, immunochemistry, protein expression, peptide chemistry, bioanalytical mass spectrometry, microbiology, BSL3 virology, genetic identity and forensic DNA analysis to pharmaceutical, biotech, academic and government clients. It was a wet-lab services business, not a software company, and never published an API, SDK, webhook surface or developer portal. Its domain aibiotech.com is now a HugeDomains for-sale parking lander answering HTTP 200 with the same sale page on every path; the last archived snapshot of a real company site dates to 2017. Laboratory directories list the operation under Granger Genetics, which makes no first-party claim to the brand, so no successor host is wired here.
layout: provider
modified: '2026-09-14'
name: AiBiotech
nav: Providers
network: true
overview: AiBiotech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Contract Research, and Clinical Laboratory.
random_paper: 12
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: aibiotech
tags:
- Company
- Biotechnology
- Life Sciences
- Contract Research
- Clinical Laboratory
- Diagnostics
- Genomics
- Defunct
---
