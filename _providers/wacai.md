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
api_count: 1
apis:
- description: Partner-facing API gateway for the Wacai open platform. Callers POST JSON to a single gateway entry, addressing operations by (apiName, apiVersion) and authenticating with appKey/appSecret HMAC reques
  name: Wacai Open API Gateway
  slug: wacai-open-api-gateway
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wacai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wacai.com
- group: company
  title: ''
  type: About
  url: https://www.wacai.com/intro/aboutus.jsp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wacai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/wacai/wacai-open-sdk/tree/master/doc
- group: build
  title: ''
  type: Packages
  url: packages/wacai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wacai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wacai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wacai-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wacai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wacai-llms.txt
created: '2026-07-17'
description: Wacai (挖财, Hangzhou Wacai Network Technology Co., Ltd.) is a Chinese fintech and personal-finance company founded in 2009, best known for its "挖财记账" personal accounting and bookkeeping app and its internet wealth-management platform. Beyond its consumer apps, Wacai operates a partner-facing open API gateway (挖财开放平台) at open.wacai.com that exposes services through a single JSON-over-HTTPS entry point using appKey/appSecret signed requests, with official client SDKs published for Java (Maven Central), Node.js, PHP, Go, and C#. It was surfaced as a portfolio company of Qiming Venture Partners.
image: https://www.wacai.com/website/favicon.ico
layout: provider
modified: '2026-07-21'
name: wacai
nav: Providers
network: true
overview: 'wacai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Personal Finance, Accounting, and Wealth Management.


  wacai''s developer surface includes documentation, authentication, and 9 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 14.6
  delta: -0.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wacai Authentication
  slug: wacai-authentication
  summary_line: apiKey/hmac-signature · 2 schemes
- kind: domain-security
  name: Wacai Domain Security
  slug: wacai-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: wacai
tags:
- Company
- Fintech
- Personal Finance
- Accounting
- Wealth Management
- Open Platform
- API Gateway
- China
website: https://www.wacai.com
---
