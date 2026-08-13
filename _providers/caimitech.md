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
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caimitech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caimitech.com
- group: company
  title: ''
  type: Website
  url: https://www.wacai.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wacai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/wacai/wacai-open-sdk
- group: build
  title: ''
  type: Packages
  url: packages/caimitech-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/caimitech-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/caimitech-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caimitech-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/caimitech-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caimitech-llms.txt
created: '2026-07-17'
description: caimitech.com is the domain of Wacai (挖财, Hangzhou Wacai Network Technology Co.), a Chinese personal-finance and wealth-management company founded in 2009 that offers accounting/bookkeeping apps, personal financial management (PFM) tools, wealth-management services, and credit solutions. Its developer surface is the Wacai Open Platform (挖财开放平台) — an HMAC-signed API gateway addressed by (api_name, api_version) pairs rather than REST paths, with first-party client SDKs in Java (published to Maven Central under com.wacai), Node.js, PHP, Go, and C#, plus a separate topic-based message gateway (pull/ack). Access uses an app_key/app_secret credential with MAC or RSA request signing and an optional token service. No OpenAPI document is published; this profile was enriched from the provider's public GitHub SDKs and package registries.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caimitech.png
layout: provider
modified: '2026-07-18'
name: caimitech
nav: Providers
network: true
overview: 'caimitech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Personal Finance, Wealth Management, and Accounting.


  caimitech''s developer surface includes documentation, authentication, sandbox, and 8 more developer resources.'
random_paper: 95
score:
  band: minimal
  composite: 12.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caimitech/refs/heads/main/screenshots/caimitech-2026-07-25T204219.png
security:
- kind: authentication
  name: Caimitech Authentication
  slug: caimitech-authentication
  summary_line: app-credential/request-signature/bearer-token · 3 schemes
- kind: domain-security
  name: Caimitech Domain Security
  slug: caimitech-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: caimitech
tags:
- Company
- FinTech
- Personal Finance
- Wealth Management
- Accounting
- Credit
- Open Platform
- API Gateway
- China
website: https://caimitech.com
---
