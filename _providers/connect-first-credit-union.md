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
  url: security/connect-first-credit-union-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/connect-first-credit-union-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/connect-first-credit-union-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/connect-first-credit-union-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/connect-first-credit-union-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connect-first-credit-union-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.connectfirstcu.com/
- group: company
  title: ''
  type: Blog
  url: https://connectfirstcu.com/en/news/news-and-announcments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/connect-first-credit-union
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://servus.ca/privacy
created: '2026-07-23'
description: 'connectFirst Credit Union is a member-owned, cooperative (Schedule-equivalent provincial credit union) financial institution headquartered in Calgary, Alberta, formed on May 3, 2021 by amalgamating four Alberta credit unions (First Calgary Financial, Chinook Financial, Mountain View Financial, and Legacy Financial). At its peak it held over CAD $6 billion in assets under administration and served more than 128,000 members across 41 branches in Central and Southern Alberta, offering retail, commercial, agricultural, and dealer-services banking. Members voted in November 2023 to merge with Servus Credit Union; the legal amalgamation closed May 1, 2024 as "Connect First and Servus Credit Union Ltd." (~CAD $29.3B assets, 600,000+ members), and the unified brand realigned to Servus Credit Union in January 2025 — the connectfirstcu.com domain now 301-redirects to servus.ca. Its open-finance posture is honest and typical of a Canadian credit union: no first-party public developer
  portal or downloadable OpenAPI, digital banking delivered via the Celero Xpress platform (powered by ebankIT) with core/banking-tech through the Central 1 / Celero cooperative ecosystem, and third-party consumer data access available only through aggregators (Plaid coverage confirmed). Canada''s federal Consumer-Driven Banking framework (Budget 2024 / FCAC-overseen) is legislated but not yet operational, so no mandated open-banking API exists.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: connectFirst Credit Union
nav: Providers
network: true
overview: 'connectFirst Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Credit Union, and Alberta.


  connectFirst Credit Union''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
random_paper: 29
scopes:
- name: Connect First Credit Union Scopes
  scope_count: 0
  slug: connect-first-credit-union-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.5
  delta: -1.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 19.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/connect-first-credit-union/refs/heads/main/screenshots/connect-first-credit-union-2026-07-25T210259.png
security:
- kind: authentication
  name: Connect First Credit Union Authentication
  slug: connect-first-credit-union-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Connect First Credit Union Domain Security
  slug: connect-first-credit-union-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: connect-first-credit-union
tags:
- Financial Services
- Banking
- Canada
- Credit Union
- Alberta
- Cooperative
- Data Aggregation
website: https://www.connectfirstcu.com/
---
