---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/choco-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/choco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://choco.com/us/
- group: start
  title: ''
  type: Login
  url: https://web.choco.com
- group: operate
  title: ''
  type: Support
  url: https://help.choco.com/en/
- group: company
  title: ''
  type: Blog
  url: https://choco.com/us/stories
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chocoapp
- group: other
  title: Open Source Contact
  type: email
  url: open.source@choco.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/choco-app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://choco.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://choco.com/privacy-policy
created: '2026-06-02'
description: Choco is an AI-powered digital ordering platform that simplifies how restaurants order from their food suppliers and distributors. Serving tens of thousands of distributors and over one hundred thousand buyers across the US, UK, Europe, and the GCC, Choco lets restaurateurs place orders and chat with all their suppliers in one app while converting orders into a supplier's preferred format (email, WhatsApp, text, fax, or direct ERP integration). Choco connects to supplier ERP systems such as Entree, NetSuite, QuickBooks, Microsoft Dynamics, Target Data System, NCR, Sage, and Odoo, and uses AI — including OrderAgent for multimodal order capture and VoiceAgent built on OpenAI's Realtime API — to turn emails, texts, images, and documents into structured, ERP-ready orders. Choco does not publish a public developer API; integration is delivered through managed ERP connections, and its public GitHub organization (chocoapp) hosts only internal data-engineering and infrastructure tooling
  rather than client SDKs or API specifications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/choco.png
layout: provider
modified: '2026-06-02'
name: Choco
nav: Providers
network: true
overview: 'Choco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Ordering, Food Distribution, Suppliers, and ERP Integration.


  Choco''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 62
score:
  band: emerging
  composite: 15.4
  delta: -1.8
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/choco/refs/heads/main/screenshots/choco-2026-06-20T174321.png
security:
- kind: domain-security
  name: Choco Domain Security
  slug: choco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Choco Trust Center
  slug: choco-trust-center
  summary_line: SOC 2
slug: choco
tags:
- Restaurant
- Ordering
- Food Distribution
- Suppliers
- ERP Integration
- Artificial Intelligence
- Supply Chain
- Food Service
website: https://choco.com/us/
---
