---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upswing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upswing.one/
- group: company
  title: ''
  type: Blog
  url: https://upswing.one/news
- group: company
  title: ''
  type: Careers
  url: https://upswing.one/career
- group: company
  title: ''
  type: Partners
  url: https://upswing.one/our-partners
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upswing-one
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upswing-financial-technologies/
- group: operate
  title: ''
  type: Contact
  url: mailto:contact@upswing.one
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upswing-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/upswing-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upswing-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integration-docs.upswing.one
- group: operate
  title: ''
  type: Support
  url: https://zh.support.upswing.one/portal/en/home
created: '2026-07-17'
description: Upswing Financial Technologies is an Indian open finance-as-a-service platform headquartered in Bengaluru and Mumbai. Its full-stack API platform lets consumer companies embed financial products such as deposits and lending from regulated partner banks (AU Small Finance Bank, DCB Bank, Utkarsh, Shivalik, Unity, South Indian Bank, Suryoday), while Upswing manages the bank integrations and compliance. Backed by QED Investors and Quona Capital. Upswing publishes no public developer portal or API documentation; its APIs are offered to partners under commercial agreements.
image: https://cdn.prod.website-files.com/640f1cf7637b80779a61f818/65d309ac6e4a0177aef94e99_webclip.svg
layout: provider
modified: '2026-07-21'
name: Upswing
nav: Providers
network: true
overview: 'Upswing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Open Finance, Embedded Finance, and Banking.


  Upswing''s developer surface includes engineering blog, authentication, support, and 10 more developer resources.'
random_paper: 70
score:
  band: emerging
  composite: 13.1
  delta: -1.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Upswing Authentication
  slug: upswing-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Upswing Domain Security
  slug: upswing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upswing
tags:
- Company
- Fintech
- Open Finance
- Embedded Finance
- Banking
- India
- Deposits
- Lending
website: https://upswing.one/
---
