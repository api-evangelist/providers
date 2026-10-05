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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beepsaude/refs/heads/main/llms/beepsaude-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beepsaude-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beepsaude/refs/heads/main/hosts/beepsaude-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beepsaude-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beepsaude/refs/heads/main/vendors/beepsaude-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beepsaude-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beepsaude.com.br/tosse-alergica/
- group: start
  title: ''
  type: Login
  url: https://checkout.beepsaude.com.br/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beepsaude/refs/heads/main/security/beepsaude-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beepsaude-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beepsaude.com.br
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://equityzen.com/company/beepsaúde
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Beepsaúde (Beep Saúde) is a Brazilian digital health platform offering at‑home medical services such as laboratory exams, vaccinations, and immunobiologics. Operating in Rio de Janeiro, São Paulo and the Federal District, the company provides a web portal and mobile app for scheduling, payment, and results delivery. It serves both private customers and health‑plan members, partnering with over 40 insurers. The service emphasizes convenience, rapid home visits, and transparent pricing, with a focus on preventive care and chronic‑disease monitoring.
image: https://beepsaude.com.br/wp-content/uploads/2020/08/destacada-bg.jpg
layout: provider
modified: '2026-09-27'
name: Beepsaúde
nav: Providers
network: true
overview: Beepsaúde is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Digital Health, Brazil, Home Care, and Telehealth.
random_paper: 18
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beepsaude Domain Security
  slug: beepsaude-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beepsaude
tags:
- Health
- Digital Health
- Brazil
- Home Care
- Telehealth
- Company
website: https://beepsaude.com.br
---
