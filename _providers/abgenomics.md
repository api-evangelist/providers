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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abgenomics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.altrubio.com/altrubio/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altrubio.com/altrubio/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.altrubio.com/altrubio/en/contact
coverage:
  checked: '2026-09-06'
  detail: AbGenomics is a clinical-stage biopharmaceutical developer of antibody therapeutics (now trading as AltruBio) whose product is a drug pipeline, not software — its own abgenomics.com domain has been released to an abovedomains.com "this domain may be for sale" parking page, and the successor site altrubio.com publishes only pipeline, news and careers pages with no developer program, no API, no SDK and no /llms.txt.
  evidence:
  - status: 200
    url: https://abgenomics.com/
  - status: 404
    url: https://abgenomics.com/.well-known/apis.json
  - status: 200
    url: https://www.altrubio.com/altrubio/en
  - status: 200
    url: https://www.altrubio.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/abgenomics
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'AbGenomics (AbGenomics International, Inc.) is a clinical-stage biopharmaceutical company founded in 2000 with offices in the San Francisco Bay Area, California and an R&D center in Taipei, Taiwan. It develops targeted antibody therapeutics for immune-mediated inflammatory disease and cancer, built on a PSGL-1 T-cell checkpoint regulator platform, with clinical candidates including neihulizumab (AbGn-168H / ALTB-168) and the antibody-drug conjugate AbGn-107. The company rebranded as AltruBio, Inc. in 2020 and now operates at altrubio.com; the original abgenomics.com domain is a parked for-sale listing. It is a therapeutics developer, not a software vendor: it publishes no developer program, no public API, no SDKs and no machine-readable API description of any kind.'
image: https://www.altrubio.com/assets/img/logo.png
layout: provider
modified: '2026-09-06'
name: Abgenomics
nav: Providers
network: true
overview: 'Abgenomics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Therapeutics.


  Abgenomics'' developer surface includes support and 3 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 7.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abgenomics Domain Security
  slug: abgenomics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: abgenomics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Therapeutics
- Clinical Research
- Immunology
- Oncology
website: https://www.altrubio.com/altrubio/en
---
