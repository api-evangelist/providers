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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/qpex-biopharma/hosts/qpex-biopharma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qpex-biopharma-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.qpexbio.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.qpexbio.com/company/leadership/
- group: auth
  href: https://artifacts.apis.io/qpex-biopharma/security/qpex-biopharma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qpex-biopharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qpexbio.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qpexbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qpexbio.com/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.qpexbio.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Qpex Biopharma is a biopharmaceutical company focused on developing novel antimicrobial therapies to combat the global threat of antimicrobial resistance (AMR). The company builds a pipeline of innovative antibiotics and anti‑infective agents, aiming to address urgent and serious bacterial and fungal pathogens worldwide. Through advanced research and collaborations, Qpex Biopharma seeks to replenish the dwindling antibiotic pipeline and provide effective treatments for patients in need.
image: https://qpexprod.wpenginepowered.com/wp-content/uploads/gram-negative-bacteria-scaled.webp
layout: provider
modified: '2026-10-22'
name: Qpex Biopharma
nav: Providers
network: true
overview: Qpex Biopharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Antimicrobial, Antibiotics, and Healthcare.
random_paper: 22
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qpex Biopharma Domain Security
  slug: qpex-biopharma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qpex-biopharma
tags:
- Company
- Biopharma
- Antimicrobial
- Antibiotics
- Healthcare
website: https://www.qpexbio.com
---
