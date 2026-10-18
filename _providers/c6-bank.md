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
  href: https://raw.githubusercontent.com/api-evangelist/c6-bank/refs/heads/main/well-known/c6-bank-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/c6-bank-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/c6-bank/refs/heads/main/well-known/c6-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/c6-bank-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/c6-bank/refs/heads/main/hosts/c6-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/c6-bank-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/c6-bank/refs/heads/main/vendors/c6-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/c6-bank-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/c6-bank/refs/heads/main/security/c6-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/c6-bank-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/c6-bank/refs/heads/main/security/c6-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/c6-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.c6bank.com.br:443/
coverage:
  checked: '2026-10-06'
  detail: No API documentation or OpenAPI spec found at known API hosts (api.com.br) and no developer portal is listed.
  evidence:
  - status: 404
    url: https://api.com.br/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: C6 Bank is a Brazilian digital bank offering a full suite of financial products including checking accounts, credit cards, loans, investments, and international banking, all accessible via a mobile app. It emphasizes innovative features such as C6 Carbon, C6 Graphene, and AI-powered assistance, targeting both individuals and businesses with competitive rewards and low fees.
layout: provider
modified: '2026-10-06'
name: C6 Bank
nav: Providers
network: true
overview: C6 Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, Digital Bank, and Brazil.
random_paper: 16
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 6
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
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: C6 Bank Domain Security
  slug: c6-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: C6 Bank Vulnerability Disclosure
  slug: c6-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: c6-bank
tags:
- Company
- Banking
- Fintech
- Digital Bank
- Brazil
website: https://www.c6bank.com.br:443/
---
