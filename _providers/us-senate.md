---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Us Senate Agentic Access
  operation_count: 14
  slug: us-senate-agentic-access
  summary_line: 14 operations
api_count: 6
apis:
- description: Clients on whose behalf lobbying is conducted
  name: US Senate Clients API
  slug: us-senate-clients-api
- description: Reference data — filing types, issue codes, government entities, etc.
  name: US Senate Constants API
  slug: us-senate-constants-api
- description: Semi-annual campaign contribution reports (LD-203)
  name: US Senate Contributions API
  slug: us-senate-contributions-api
- description: Lobbying disclosure filings (LD-1, LD-2, LD-203)
  name: US Senate Filings API
  slug: us-senate-filings-api
- description: Individual lobbyist records
  name: US Senate Lobbyists API
  slug: us-senate-lobbyists-api
- description: Lobbying firm and self-employed lobbyist registrations
  name: US Senate Registrants API
  slug: us-senate-registrants-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: US Senate Lobbying Disclosure Act (LDA) Clients API
  slug: open-us-senate-clients-api
- collection_type: open
  name: US Senate Lobbying Disclosure Act (LDA) Clients Constants API
  slug: open-us-senate-constants-api
- collection_type: open
  name: US Senate Lobbying Disclosure Act (LDA) Clients Contributions API
  slug: open-us-senate-contributions-api
- collection_type: open
  name: US Senate Lobbying Disclosure Act (LDA) Clients Filings API
  slug: open-us-senate-filings-api
- collection_type: open
  name: US Senate Lobbying Disclosure Act (LDA) API
  slug: open-us-senate-lda
- collection_type: open
  name: US Senate Lobbying Disclosure Act (LDA) Clients Lobbyists API
  slug: open-us-senate-lobbyists-api
- collection_type: open
  name: US Senate Lobbying Disclosure Act (LDA) Clients Registrants API
  slug: open-us-senate-registrants-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-senate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-senate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-senate-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ussenate
created: '2024-12-03'
description: The United States Senate is one of the two chambers of Congress, responsible for representing the interests of the individual states and ensuring that federal legislation is passed in a fair and representative manner. The Senate plays a crucial role in the legislative process, with its members debating and voting on bills and resolutions that affect the country as a whole. The Senate also administers the Lobbying Disclosure Act (LDA) reporting system, which requires lobbyists and lobbying firms to register and report their activities, clients, and campaign contributions for public transparency.
examples:
- key_count: 2
  name: Lda Get Registrant Example
  slug: lda-get-registrant-example
- key_count: 2
  name: Lda List Filings Example
  slug: lda-list-filings-example
finops:
- name: Us Senate Finops
  service_category: API
  slug: us-senate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-senate.png
json_schemas:
- name: Senate LDA Lobbying Filing
  property_count: 11
  slug: us-senate-lda-filing
json_structures:
- name: Us Senate Lda Filing Structure
  property_count: 0
  slug: us-senate-lda-filing-structure
jsonld:
- class_count: 4
  name: Us Senate Context
  property_count: 19
  slug: us-senate-context
layout: provider
modified: '2026-05-19'
name: US Senate
nav: Providers
network: true
overview: 'US Senate publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Constants API, Contributions API, and 3 more. Tagged areas include Federal-Government, Lobbying, Government Transparency, Campaign Finance, and Open Data.


  The US Senate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Senate''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Us Senate Plans Pricing
  plan_count: 3
  slug: us-senate-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Us Senate Rate Limits
  slug: us-senate-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Senate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-senate-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: US Senate API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: us-senate-rules
score:
  band: thin
  composite: 31.7
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 62.4
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-senate/refs/heads/main/screenshots/us-senate-2026-06-20T200626.png
security:
- kind: authentication
  name: Us Senate Authentication
  slug: us-senate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Us Senate Domain Security
  slug: us-senate-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: us-senate
tags:
- Federal-Government
- Lobbying
- Government Transparency
- Campaign Finance
- Open Data
---
