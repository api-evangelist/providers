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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banco-central-do-brasil/refs/heads/main/security/banco-central-do-brasil-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/banco-central-do-brasil-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banco-central-do-brasil/refs/heads/main/hosts/banco-central-do-brasil-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banco-central-do-brasil-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banco-central-do-brasil/refs/heads/main/security/banco-central-do-brasil-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/banco-central-do-brasil-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banco-central-do-brasil/refs/heads/main/security/banco-central-do-brasil-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banco-central-do-brasil-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bcb.gov.br
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.bcb.gov.br
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Banco Central do Brasil (BCB) is the central bank of Brazil, responsible for ensuring price stability, overseeing the financial system, and promoting economic growth. It regulates monetary policy, supervises financial institutions, and provides a framework for payments and settlements. The BCB offers various public data APIs covering exchange rates, financial statistics, and regulatory information, supporting developers and researchers in accessing authoritative financial data.
image: https://www.bcb.gov.br/assets/img/bc_marca_bg.png
layout: provider
modified: '2026-10-14'
name: Banco Central do Brasil
nav: Providers
network: true
overview: Banco Central do Brasil is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Banking, CentralBank, and Brazil.
random_paper: 21
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Banco Central Do Brasil Domain Security
  slug: banco-central-do-brasil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Banco Central Do Brasil Vulnerability Disclosure
  slug: banco-central-do-brasil-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: banco-central-do-brasil
tags:
- Company
- Finance
- Banking
- CentralBank
- Brazil
website: https://www.bcb.gov.br
---
