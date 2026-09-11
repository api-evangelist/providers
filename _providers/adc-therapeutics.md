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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adc-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adctherapeutics.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adctherapeutics.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adctherapeutics.com/legal-notice/
- group: operate
  title: ''
  type: Contact
  url: https://www.adctherapeutics.com/about-adc-therapeutics/contact/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.adctherapeutics.com/overview
- group: company
  title: ''
  type: Careers
  url: https://www.adctherapeutics.com/culture-careers/culture/
- group: company
  title: ''
  type: About
  url: https://www.adctherapeutics.com/about-adc-therapeutics/leadership/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adc-therapeutics-llms.txt
coverage:
  checked: '2026-09-07'
  detail: 'ADC Therapeutics is an oncology drug developer whose product is ZYNLONTA, not software: its WordPress corporate site serves no /developers, /api or /llms.txt path, its Q4-hosted investor site answers every unknown path with a 200 HTML soft-404, no npm/PyPI package carries its name, and no /.well-known/ discovery document exists on any of its five hosts.'
  evidence:
  - status: 404
    url: https://www.adctherapeutics.com/developers
  - status: 404
    url: https://www.adctherapeutics.com/openapi.json
  - status: 404
    url: https://www.adctherapeutics.com/llms.txt
  - status: 404
    url: https://www.adctherapeutics.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/adctherapeutics
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'ADC Therapeutics SA (NYSE: ADCT) is a commercial-stage biotechnology company headquartered at the Biopôle in Lausanne, Switzerland, with US operations in New Jersey, that discovers and develops antibody drug conjugates (ADCs) for hematologic malignancies and solid tumors. Its approved product ZYNLONTA (loncastuximab tesirine-lpyl) is a CD19-directed ADC for relapsed or refractory diffuse large B-cell lymphoma, and the company is expanding it into earlier lines through the LOTIS-5 Phase 3 and LOTIS-7 Phase 1b trials alongside a preclinical and clinical ADC pipeline. It is a therapeutics developer, not a software vendor: a 2026-09-07 probe of every host it operates found no developer portal, no public API, no SDK and no machine-readable contract.'
image: https://www.adctherapeutics.com/wp-content/uploads/2026/03/adc-logo.png
layout: provider
modified: '2026-09-07'
name: ADC Therapeutics
nav: Providers
network: true
overview: ADC Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Life Sciences.
random_paper: 0
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adc Therapeutics Domain Security
  slug: adc-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adc-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Life Sciences
- Healthcare
- Clinical Trials
- Antibody Drug Conjugates
website: https://www.adctherapeutics.com/
---
