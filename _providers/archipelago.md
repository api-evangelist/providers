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
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Archipelago's customer-facing API is a GraphQL API that lets customers access and use their property and SOV data in custom applications. Access is credential-based; Archipelago provisions credentials
  name: Archipelago GraphQL API
  slug: archipelago-graphql-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.onarchipelago.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.onarchipelago.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onarchipelago.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.onarchipelago.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.onarchipelago.com/get-started-with-archipelago
- group: company
  title: ''
  type: Blog
  url: https://www.onarchipelago.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.onarchipelago.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://platform.onarchipelago.com
- group: start
  title: ''
  type: Login
  url: https://platform.onarchipelago.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onarchipelago.com/user-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onarchipelago.com/customers/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onarchipelago
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onarchipelago
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/OnArchipelago
- group: auth
  title: ''
  type: Security
  url: https://www.onarchipelago.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.onarchipelago.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/archipelago-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/archipelago-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/archipelago-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archipelago-domain-security.yml
created: '2026-07-17'
description: Archipelago is a San Francisco-based insurtech company, founded in 2018, that operates an AI-powered platform and agent for property and casualty (P&C) insurance risk data. Its software helps commercial property owners, brokers, and insurance underwriters ingest, remediate, enrich, and centralize Statement of Values (SOV) data and property documents, making risk information model-ready for submission to insurance markets. Archipelago exposes a customer-facing GraphQL API so customers can use their property data in custom applications, and the platform holds a SOC 2 Type 2 attestation. The company is backed by Canaan Partners, Scale Venture Partners, Ignition Partners, Prologis Ventures, Stone Point Capital, and Zigg Capital.
image: https://platform.onarchipelago.com/android-chrome-256x256.png
layout: provider
modified: '2026-07-18'
name: Archipelago
nav: Providers
network: true
overview: 'Archipelago publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Property Risk, and Underwriting.


  Archipelago''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 32.3
  delta: -3.1
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 35.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archipelago/refs/heads/main/screenshots/archipelago-2026-07-25T201034.png
security:
- kind: authentication
  name: Archipelago Authentication
  slug: archipelago-authentication
  summary_line: credential · 1 scheme
- kind: domain-security
  name: Archipelago Domain Security
  slug: archipelago-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: archipelago
tags:
- Company
- Insurance
- Insurtech
- Property Risk
- Underwriting
- Risk Management
- Commercial Property
- GraphQL
- Data
- AI Agent
website: https://www.onarchipelago.com
---
