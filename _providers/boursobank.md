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
  href: https://raw.githubusercontent.com/api-evangelist/boursobank/refs/heads/main/hosts/boursobank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boursobank-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boursobank/refs/heads/main/security/boursobank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boursobank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boursobank.com
coverage:
  checked: '2026-10-03'
  detail: API endpoints return HTML shells instead of machine‑readable OpenAPI specifications.
  evidence:
  - status: 200
    url: https://api.boursobank.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Boursobank, operating under the brand BoursoBank, is a French online bank offering a full suite of financial services including free banking accounts, credit cards, loans, insurance, investment products, and savings plans. It positions itself as the cheapest digital bank in France, targeting individuals, professionals, youth, and private banking clients. The platform provides a modern web and mobile experience, emphasizing low fees, transparent pricing, and a wide range of banking and investment options.
layout: provider
modified: '2026-10-03'
name: Boursobank
nav: Providers
network: true
overview: Boursobank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, Online Banking, and France.
random_paper: 0
score:
  band: minimal
  composite: 2.1
  coverage:
    artifact_dirs: 4
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
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boursobank Domain Security
  slug: boursobank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boursobank
tags:
- Company
- Banking
- Fintech
- Online Banking
- France
website: https://www.boursobank.com
---
