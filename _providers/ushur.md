---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
- description: 'REST API for the Ushur customer experience automation platform. Documented operations (per the official UshurNodeSDK) include logging in to a tenant instance, initiating campaign engagements with end '
  name: Ushur Platform API
  slug: ushur-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ushur-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ushur.ai
- group: company
  title: ''
  type: Blog
  url: https://ushur.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ushur.com
- group: operate
  title: ''
  type: Support
  url: https://ushur.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UshurInc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ushur.ai/legal
- group: auth
  title: ''
  type: TrustCenter
  url: security/ushur-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ushur.ai/security-and-compliance
- group: company
  title: ''
  type: Partners
  url: https://ushur.ai/partners
- group: build
  title: ''
  type: Packages
  url: packages/ushur-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ushur-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ushur-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ushur-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ushur-authentication.yml
created: '2026-07-17'
description: Ushur is an agentic AI platform for customer experience automation (CXA) in regulated industries, including healthcare, insurance, and financial services. Enterprises use Ushur Studio, AI Agents, the Invisible App, intelligent document automation, and the platform's REST APIs and prebuilt integrations to automate end-to-end member, patient, and policyholder journeys across SMS, email, voice, and web channels, with HIPAA, HITRUST, SOC 2, and PCI DSS compliance built in.
image: https://cdn.prod.website-files.com/66b170e39e75a071ecd6a1e1/69319b90541bfce5aeeadec3_Home%20OG.png
layout: provider
modified: '2026-07-21'
name: Ushur
nav: Providers
network: true
overview: 'Ushur publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Customer Experience, Automation, and Healthcare.


  Ushur''s developer surface includes engineering blog, documentation, support, authentication, and 11 more developer resources.'
random_paper: 28
score:
  band: emerging
  composite: 25.2
  delta: -1.7
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 26.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 39.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ushur Authentication
  slug: ushur-authentication
  summary_line: session-login/otp · 2 schemes
- kind: domain-security
  name: Ushur Domain Security
  slug: ushur-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ushur Trust Center
  slug: ushur-trust-center
  summary_line: HITRUST r2, SOC 2, HIPAA, PCI DSS, ISO 27001, GDPR, CCPA, PIPEDA
slug: ushur
tags:
- Company
- Artificial Intelligence
- Customer Experience
- Automation
- Healthcare
- Insurance
- Financial Services
- Agents
website: https://ushur.ai
---
