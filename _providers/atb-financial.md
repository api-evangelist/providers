---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atb-financial-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atb-financial-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.atb.com
- group: company
  title: ''
  type: About
  url: https://www.atb.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.atb.com/personal/good-advice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atb.com/company/privacy-and-security/
- group: operate
  title: ''
  type: Support
  url: https://www.atb.com/resources/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ATBFinancial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atb-financial
created: '2026-07-23'
description: ATB Financial (formerly Alberta Treasury Branches) is a financial institution and Crown corporation wholly owned by the Government of Alberta, established in 1938 and operating under the provincial ATB Financial Act rather than the federal Bank Act. Headquartered in Edmonton, it is Alberta's largest home-grown financial institution and the largest public bank in North America, with roughly C$64 billion in assets, more than 800,000 customers, about 5,000 team members, and 300+ branches and agencies across the province; deposits are guaranteed by the Province of Alberta rather than covered by CDIC. On the open-finance front, ATB does NOT operate a public first-party developer portal or documented public API surface (developer.atb.com returns HTTP 404), and Canada's federal Consumer-Driven Banking framework (legislated in Budget 2024 and the Fall Economic Statement 2024, with the FCAC as overseer) is not yet operational. Consumer financial-data access to ATB today is therefore
  voluntary and aggregator-mediated — reached through third-party aggregators such as Finicity (by Mastercard) and Flinks rather than a direct bank API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: ATB Financial
nav: Providers
network: true
overview: 'ATB Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Alberta, and Crown Corporation.


  ATB Financial''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 46
score:
  band: minimal
  composite: 10.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atb-financial/refs/heads/main/screenshots/atb-financial-2026-07-25T201528.png
security:
- kind: domain-security
  name: Atb Financial Domain Security
  slug: atb-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atb-financial
tags:
- Financial Services
- Banking
- Canada
- Alberta
- Crown Corporation
- Public Bank
- Data Aggregation
- Open Banking
- Consumer-Driven Banking
website: https://www.atb.com
---
