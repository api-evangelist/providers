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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aulos/refs/heads/main/hosts/aulos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aulos-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://aulosbio.com/about-us/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aulos/refs/heads/main/security/aulos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aulos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aulosbio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aulosbio.com/about-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aulosbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aulosbio.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://aulosbio.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://aulosbio.com/careers/
- group: company
  title: ''
  type: Newsroom
  url: https://aulosbio.com/newsroom/
coverage:
  checked: 2026-09-26
  detail: The provider's website offers only HTML documentation with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://aulosbio.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Aulos Bioscience develops an immune‑activating antibody therapeutic, imneskibart (AU‑007), that binds the interleukin‑2 region interacting with the CD25 receptor to shift IL‑2 activity toward immune activation and away from suppression. The company is advancing this investigational product in Phase 1/2 trials for patients with unresectable locally advanced or metastatic solid‑tumor cancers, including melanoma and renal cell carcinoma. Its focus is on delivering a novel IL‑2‑based therapy to cancer patients and the clinical research community.
image: https://aulos.b-cdn.net/wp-content/uploads/2021/12/Aulos-Bio-logo-for-social-share-300-x-300.jpg
layout: provider
modified: '2026-09-26'
name: Aulos
nav: Providers
network: true
overview: 'Aulos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Oncology, Biopharma, Antibody Therapeutics, IL-2 Therapeutics, and Clinical Trials.


  Aulos'' developer surface includes documentation and 9 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aulos Domain Security
  slug: aulos-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aulos
tags:
- Oncology
- Biopharma
- Antibody Therapeutics
- IL-2 Therapeutics
- Clinical Trials
website: https://aulosbio.com/
---
