---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canadian-tire-bank-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canadian-tire-bank-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canadian-tire-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/canadian-tire-bank-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canadian-tire-bank-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canadian-tire-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ctfs.com
- group: company
  title: ''
  type: About
  url: https://www.ctfs.com/content/ctfs/en/about-us.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ctfs.com/content/ctfs3/en/legal.html
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/canadian-tire-bank
created: '2026-07-23'
description: Canadian Tire Bank (operating as Canadian Tire Financial Services) is a federally regulated Schedule I bank, wholly owned by Canadian Tire Corporation, Limited and federally chartered in 2003. Headquartered in Oakville, Ontario with operations in St. Catharines and Welland, the bank is the financial-services arm of one of Canada's best-known retailers. It issues the Triangle Mastercard, Triangle World Mastercard, Triangle World Elite Mastercard, Gas Advantage and Cash Advantage Mastercards, and offers high-interest savings accounts and GICs, all tied to the Triangle Rewards loyalty program. On open finance, the bank exposes no first-party public developer API or banking API portal. Canada's Consumer-Driven Banking framework (Budget 2024 / Fall Economic Statement 2024, overseen by the FCAC) is legislated but not yet operational, so consumer data access today is voluntary and aggregator-based — Canadian Tire Bank card and account data is reached through aggregators such as Finicity
  (by Mastercard), Flinks and Plaid rather than a first-party API. The cantire.com developer portal is run by the retail parent Canadian Tire Corporation, not the bank, is gated behind sign-in, and its TLS certificate expired in February 2026.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Canadian Tire Bank
nav: Providers
network: true
overview: 'Canadian Tire Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Schedule I Bank, and Credit Cards.


  Canadian Tire Bank''s developer surface includes authentication and 9 more developer resources.'
random_paper: 52
scopes:
- name: Canadian Tire Bank Scopes
  scope_count: 4
  slug: canadian-tire-bank-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.1
  delta: -1.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 19.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 55.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canadian-tire-bank/refs/heads/main/screenshots/canadian-tire-bank-2026-07-25T204326.png
security:
- kind: authentication
  name: Canadian Tire Bank Authentication
  slug: canadian-tire-bank-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Canadian Tire Bank Domain Security
  slug: canadian-tire-bank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: canadian-tire-bank
tags:
- Financial Services
- Banking
- Canada
- Schedule I Bank
- Credit Cards
- Mastercard
- Consumer-Driven Banking
- Data Aggregation
website: https://www.ctfs.com
---
