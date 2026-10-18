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
  href: https://raw.githubusercontent.com/api-evangelist/commerzbank/refs/heads/main/hosts/commerzbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commerzbank-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.commerzbank.de/konzern/newsroom/
- group: start
  title: ''
  type: Login
  url: https://www.commerzbank.de/lp/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commerzbank/refs/heads/main/security/commerzbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commerzbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commerzbank.de
coverage:
  checked: '2026-10-13'
  detail: Commerzbank provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.commerzbank.de
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Commerzbank AG is a major German universal bank offering a wide range of financial services including retail banking, corporate banking, investment banking, and asset management. The bank provides digital banking platforms for private and business customers, offering online account access, payment services, loan applications, and financial advisory. Through its developer portal, Commerzbank exposes APIs for account information, transaction processing, payment initiation, and other services to enable fintech integration and open banking solutions.
image: https://www.commerzbank.de/ms/media/generated/true_d0e3118db1950de172191d269334eeb7_1200_630_848_448_mady_morrison_tagesgeld.png
layout: provider
modified: '2026-10-13'
name: Commerzbank
nav: Providers
network: true
overview: Commerzbank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Finance, Open Banking, and Germany.
random_paper: 11
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Commerzbank Domain Security
  slug: commerzbank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: commerzbank
tags:
- Company
- Banking
- Finance
- Open Banking
- Germany
website: https://www.commerzbank.de
---
