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
  url: security/alterna-savings-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alterna-savings-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alterna-savings-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/alterna-savings-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alterna-savings-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.alterna.ca/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alterna.ca/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alterna.ca/en/privacy-and-security
- group: operate
  title: ''
  type: Support
  url: https://www.alterna.ca/en/about-us/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.alterna.ca/en/personal/resource-centre/advice-for-life-blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alternasavings
created: '2026-07-23'
description: Alterna Savings and Credit Union Limited is a member-owned financial cooperative (credit union) founded in 1908 as the Civil Service Savings and Loan Society, headquartered in Ottawa, Ontario and regulated provincially by the Financial Services Regulatory Authority of Ontario (FSRAO). It is one of Ontario's largest credit unions, serving roughly 217,000 members with about C$10.8 billion in assets across branches in Ontario, and operates the federally regulated direct-banking subsidiary Alterna Bank, one of Canada's earliest digital-first banks. Alterna offers personal and business banking, mortgages, lending, investments and insurance. Consistent with Canada's voluntary, not-yet-operational Consumer-Driven Banking framework (legislated in Budget 2024 / Fall Economic Statement 2024 with the FCAC as overseer), Alterna Savings exposes NO public first-party developer portal or documented API. Digital access is delivered through its online and mobile banking apps and the Interac
  e-Transfer consumer rail; any third-party data access today is aggregator/screen-scraping based rather than a first-party API. This is an identity-only record with an honest no-public-API posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23T18:00:00Z'
name: Alterna Savings
nav: Providers
network: true
overview: 'Alterna Savings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Credit Union, and Cooperative.


  Alterna Savings'' developer surface includes authentication, support, engineering blog, and 8 more developer resources.'
random_paper: 31
scopes:
- name: Alterna Savings Scopes
  scope_count: 0
  slug: alterna-savings-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.8
  delta: -3.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 46.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alterna-savings/refs/heads/main/screenshots/alterna-savings-2026-07-25T195822.png
security:
- kind: authentication
  name: Alterna Savings Authentication
  slug: alterna-savings-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alterna Savings Domain Security
  slug: alterna-savings-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: alterna-savings
tags:
- Financial Services
- Banking
- Canada
- Credit Union
- Cooperative
- Consumer-Driven Banking
- Interac
- Data Aggregation
website: https://www.alterna.ca/
---
