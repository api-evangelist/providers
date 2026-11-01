---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: HDFC Bank’s APIs enable open banking integration for partners, providing account information, transaction history, and fund transfers.
  name: HDFC Bank API
  slug: hdfc-bank-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/hdfc-bank/authentication/hdfc-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hdfc-bank-authentication.yml
- group: agent
  href: https://artifacts.apis.io/hdfc-bank/llms/hdfc-bank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hdfc-bank-llms.txt
- group: other
  href: https://artifacts.apis.io/hdfc-bank/hosts/hdfc-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hdfc-bank-hosts.yml
- group: other
  href: https://artifacts.apis.io/hdfc-bank/vendors/hdfc-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hdfc-bank-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hdfc.bank.in/terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://merchantmandate.hdfc.bank.in/login
- group: auth
  href: https://artifacts.apis.io/hdfc-bank/security/hdfc-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hdfc-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hdfc.bank.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hdfc.bank.in/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hdfc.bank.in/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hdfc.bank.in/api-catalog
- group: operate
  title: ''
  type: Support
  url: https://developer.hdfc.bank.in/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HDFC-Bank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hdfc.bank.in/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: The developer portal provides human‑readable API documentation but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable specification.
  evidence:
  - status: 200
    url: https://developer.hdfc.bank.in/api-catalog
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: HDFC Bank Ltd. is one of India’s leading private sector banks, offering a wide range of financial services including retail banking, corporate banking, loans, credit cards, and digital payments. The bank provides an open banking developer portal that publishes APIs for account information, transaction history, fund transfers, and other services to enable fintech integration. The portal is hosted at https://developer.hdfc.bank.in/ and requires registration for full access.
image: https://www.hdfc.bank.in/content/dam/hdfcbankpws/home-page/hdfc-bank-logo.svg
layout: provider
modified: '2026-10-28'
name: HDFC Bank
nav: Providers
network: true
overview: 'HDFC Bank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Finance, India, Payments, and OpenBanking.


  HDFC Bank''s developer surface includes authentication, documentation, API reference, support, and 10 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hdfc Bank Authentication
  slug: hdfc-bank-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hdfc Bank Domain Security
  slug: hdfc-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hdfc-bank
tags:
- Banking
- Finance
- India
- Payments
- OpenBanking
website: https://hdfc.bank.in/
---
