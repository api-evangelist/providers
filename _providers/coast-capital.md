---
access_model:
  confidence: high
  label: No public API · Aggregator-mediated data access only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
  - research
  trial: false
  try_now: false
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
  url: security/coast-capital-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coast-capital-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coast-capital-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coast-capital-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coast-capital-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coast-capital-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.coastcapitalsavings.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coastcapitalsavings.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coast-capital-savings
created: '2026-07-23'
description: 'Coast Capital Savings is a member-owned financial co-operative headquartered in Surrey, British Columbia, serving over 600,000 members across roughly 45 branches. On November 1, 2018 it became Canada''s first British Columbia-based federal credit union (regulated federally rather than provincially), and in May 2026 it completed a merger with Prospera Credit Union. With approximately $21.9 billion CAD in total assets it is one of Canada''s largest credit unions. As a cooperative credit union rather than a Schedule I/II bank, Coast Capital operates within Canada''s voluntary and still-fragmented open-finance landscape: the federal Consumer-Driven Banking (open banking) framework legislated under Budget 2024 and the Fall Economic Statement 2024, with the Financial Consumer Agency of Canada (FCAC) as overseer, is not yet operational. Coast Capital publishes NO public first-party developer portal or documented API; consumer financial-data access today is aggregator-mediated (e.g.
  Plaid) via screen-scraping/credential-based connections rather than a first-party API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Coast Capital Savings
nav: Providers
network: true
overview: 'Coast Capital Savings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Credit Union, and Cooperative.


  Coast Capital Savings'' developer surface includes authentication and 8 more developer resources.'
random_paper: 53
scopes:
- name: Coast Capital Scopes
  scope_count: 2
  slug: coast-capital-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 18.0
  delta: -1.5
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 19.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coast-capital/refs/heads/main/screenshots/coast-capital-2026-07-25T205833.png
security:
- kind: authentication
  name: Coast Capital Authentication
  slug: coast-capital-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Coast Capital Domain Security
  slug: coast-capital-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coast-capital
tags:
- Financial Services
- Banking
- Canada
- Credit Union
- Cooperative
- Consumer-Driven Banking
- Data Aggregation
website: https://www.coastcapitalsavings.com/
---
