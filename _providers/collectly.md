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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: JWT-authenticated, practice-scoped REST API for integrating patient billing and payment workflows — practices, patients, appointments, providers, locations, insurance companies and policies, statement
  name: Collectly Partners API
  slug: collectly-partners-api
artifact_total: 6
asyncapis:
- description: ''
  name: Collectly Webhooks
  slug: collectly-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.collectly.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.collectly.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.collectly.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.collectly.co/docs/implementation-guide
- group: company
  title: ''
  type: Blog
  url: https://www.collectly.co/blog
- group: start
  title: ''
  type: Login
  url: https://app.collectly.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.collectly.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.collectly.co/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.collectly.co/security-compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/collectly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/collectly-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/collectly-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.collectly.co/
created: '2026-07-17'
description: Collectly is a healthtech company providing AI-powered revenue cycle automation for healthcare providers, spanning the full patient financial journey from insurance eligibility and cost estimation through point-of-service and post-visit payment collection. Its platform includes pre-visit intake automation, AI eligibility and benefits checks, AI cost estimation, point-of-service payments, post-visit billing automation, a payments platform, and an AI voice agent (Billie) for patient billing support. Collectly exposes a Partners API (JWT-authenticated, practice-scoped REST) covering practices, patients, appointments, providers, locations, insurance companies and policies, statements, payments, refunds, and subscriptions, plus embeddable patient portal / iframe components and outbound webhooks. Backed by Sapphire Ventures.
image: https://cdn.prod.website-files.com/69ba35b83a30189f9f939f89/69c40b30d5c3530eda3fe299_OpenGraph_Homepage_OG_1200x627px_2_BW20260325.png
layout: provider
mcp_servers:
- description: ''
  name: collectly-mcp.yml
  slug: collectly-mcpyml
modified: '2026-07-18'
name: Collectly
nav: Providers
network: true
overview: 'Collectly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthtech, Revenue Cycle Management, Patient Payments, and Medical Billing.


  The Collectly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Collectly''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 36.0
  delta: -1.1
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 27.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 37.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/collectly/refs/heads/main/screenshots/collectly-2026-07-25T210051.png
security:
- kind: authentication
  name: Collectly Authentication
  slug: collectly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Collectly Domain Security
  slug: collectly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Collectly Trust Center
  slug: collectly-trust-center
  summary_line: HITRUST i1 Validated, SOC 2 Type 2, PCI DSS Level 1, HIPAA (Business Associate)
slug: collectly
tags:
- Company
- Healthtech
- Revenue Cycle Management
- Patient Payments
- Medical Billing
- Payments
- Healthcare
- Insurance Eligibility
website: https://www.collectly.co/
---
