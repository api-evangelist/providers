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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 9.6
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Feedvisor's External API for exporting configuration reports and importing pricing/repricing feeds. OAuth2 client-credentials auth; asynchronous report/feed jobs are submitted then polled by request_i
  name: Feedvisor External API
  slug: feedvisor-external-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://feedvisor.com
- group: company
  title: ''
  type: Blog
  url: https://feedvisor.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://feedvisor.com/contact-feedvisor/
- group: start
  title: ''
  type: Login
  url: https://dashboard.feedvisor.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://feedvisor.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://feedvisor.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/feedvisor
- group: auth
  title: ''
  type: Authentication
  url: authentication/feedvisor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/feedvisor-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/feedvisor-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/feedvisor-domain-security.yml
created: '2026-07-17'
description: Feedvisor is an AI-powered agentic commerce platform for brands and large sellers on Amazon, unifying advertising optimization, dynamic pricing, and competitive market intelligence in a single system. Its Agentis platform and ProductSphere pricing technology apply machine learning to manage Buy Box share, sponsored-ads spend (TACoS), and margin across an $8B+ GMV base. Feedvisor also exposes an External API secured with OAuth2 client-credentials for exporting configuration reports and importing pricing and repricing feeds programmatically, letting brands automate listing and repricing operations.
image: https://feedvisor.com/wp-content/uploads/2026/02/Feedvisor_Wordmark_G_RGB-square-200x200-1.png
layout: provider
modified: '2026-07-19'
name: Feedvisor
nav: Providers
network: true
overview: 'Feedvisor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Amazon, E-Commerce, Retail, and Advertising.


  Feedvisor''s developer surface includes engineering blog, support, authentication, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/feedvisor/refs/heads/main/screenshots/feedvisor-2026-07-25T214318.png
security:
- kind: authentication
  name: Feedvisor Authentication
  slug: feedvisor-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Feedvisor Domain Security
  slug: feedvisor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: feedvisor
tags:
- Company
- Amazon
- E-Commerce
- Retail
- Advertising
- Pricing
- Repricing
- Marketplace
- Machine Learning
- Optimization
website: https://feedvisor.com
---
