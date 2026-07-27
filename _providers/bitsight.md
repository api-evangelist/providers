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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'RESTful API for Bitsight security ratings, portfolio and company data, findings, alerts, and cyber threat intelligence. Authenticated with an API token via HTTP Basic over HTTPS; versioned in the URL '
  name: Bitsight API
  slug: bitsight-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: http://www.bitsight.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.bitsighttech.com/hc/en-us/categories/360005934253-Bitsight-API
- group: docs
  title: ''
  type: Documentation
  url: https://help.bitsighttech.com/hc/en-us/articles/231872628-API-Documentation-Overview
- group: docs
  title: ''
  type: APIReference
  url: https://bitsight.stoplight.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.bitsighttech.com/hc/en-us/sections/4411972074263-Bitsight-API-Guides
- group: operate
  title: ''
  type: Support
  url: https://help.bitsighttech.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.bitsight.com/blog
- group: start
  title: ''
  type: Login
  url: https://service.bitsighttech.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitsight.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitsight.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/bitsight-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bitsight.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitsight-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitsight-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitsight-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitsight-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bitsight-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bitsight-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitsight-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitsight-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitsight-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bitsight-vulnerability-disclosure.yml
created: '2026-07-17'
description: Bitsight is a global cyber risk intelligence platform that combines security ratings, external attack surface management (EASM), third-party risk management (TPRM), and cyber threat intelligence (CTI) in a single data model. Its outside-in, agentless monitoring produces continuously updated security ratings validated against real-world breach likelihood, powering vendor risk workflows, insurance underwriting, and capital-markets portfolio oversight for more than 3,500 organizations across 60+ countries. Bitsight exposes a RESTful HTTP API at api.bitsighttech.com (companies, portfolios, ratings, findings, alerts, and CTI) authenticated with an API token over HTTP Basic, documented in the Bitsight Knowledge Base and an interactive Stoplight reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitsight.png
layout: provider
modified: '2026-07-18'
name: BitSight
nav: Providers
network: true
overview: 'BitSight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cyber Risk, Security Ratings, and Third-Party Risk Management.


  BitSight''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 46
score:
  band: thin
  composite: 31.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitsight/refs/heads/main/screenshots/bitsight-2026-07-25T203206.png
security:
- kind: authentication
  name: Bitsight Authentication
  slug: bitsight-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bitsight Domain Security
  slug: bitsight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bitsight Vulnerability Disclosure
  slug: bitsight-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Bitsight Trust Center
  slug: bitsight-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, HIPAA
slug: bitsight
tags:
- Company
- Security
- Cyber Risk
- Security Ratings
- Third-Party Risk Management
- Attack Surface Management
- Threat Intelligence
- Vendor Risk
website: http://www.bitsight.com/
---
