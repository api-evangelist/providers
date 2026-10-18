---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chain-bridge-bank/refs/heads/main/well-known/chain-bridge-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chain-bridge-bank-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chain-bridge-bank/refs/heads/main/hosts/chain-bridge-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chain-bridge-bank-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chain-bridge-bank/refs/heads/main/vendors/chain-bridge-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chain-bridge-bank-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chainbridgebank.com/disclosures/privacy-statement
- group: company
  title: ''
  type: Newsroom
  url: https://www.chainbridgebank.com/connect-with-us/about-us/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chain-bridge-bank/refs/heads/main/security/chain-bridge-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chain-bridge-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chainbridgebank.com/
coverage:
  checked: '2026-10-08'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on any discovered host.
  evidence:
  - status: 0
    url: https://api.chainbridgebank.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Chain Bridge Bank, N.A., is a nationally chartered bank headquartered in McLean, Virginia, offering commercial, personal, and trust banking services. Founded in 2007, it serves political campaigns, lobbying firms, and other clients, providing deposit accounts, loans, treasury management, and wealth management nationwide.
image: https://www.chainbridgebank.com/assets/files/EJtOvDB4/washington-dc-skyline-dawn-hero.jpg
layout: provider
modified: '2026-10-07'
name: Chain Bridge Bank
nav: Providers
network: true
overview: Chain Bridge Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial Services, Commercial Banking, and Trust Services.
random_paper: 10
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
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
    score: 12.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chain Bridge Bank Domain Security
  slug: chain-bridge-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chain-bridge-bank
tags:
- Company
- Banking
- Financial Services
- Commercial Banking
- Trust Services
website: https://www.chainbridgebank.com/
---
