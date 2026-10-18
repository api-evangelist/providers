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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brii-biosciences/refs/heads/main/hosts/brii-biosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brii-biosciences-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.briibio.com/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.briibio.com/en/privacy-statement/
- group: other
  title: ''
  type: Leadership
  url: https://www.briibio.com/en/company/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brii-biosciences/refs/heads/main/security/brii-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brii-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.briibio.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.briibio.com
  - status: 403
    url: https://forgeglobal.com/brii-biosciences_stock/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: 'Brii BioSciences Limited (stock code: 2137.HK) is a biotechnology company founded in 2018, developing therapies for high unmet medical needs, notably hepatitis B virus infection. Operating in China and the United States, the firm focuses on innovative therapeutic candidates and has a pipeline of unique programs. It employs a visionary leadership team and aims to improve patient health through advanced biotech research.'
layout: provider
modified: '2026-10-06'
name: Brii BioSciences
nav: Providers
network: true
overview: Brii BioSciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Monoclonal Antibodies, Infectious Diseases, Hepatitis B, and COVID-19.
random_paper: 20
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brii Biosciences Domain Security
  slug: brii-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brii-biosciences
tags:
- Biotechnology
- Monoclonal Antibodies
- Infectious Diseases
- Hepatitis B
- COVID-19
- Neuroscience
- China
website: https://www.briibio.com
---
