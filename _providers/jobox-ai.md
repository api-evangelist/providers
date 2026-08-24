---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Jobox "Kili" platform API — the production HTTP API behind the Jobox pro app and the Jobox managed-marketplace product. Covers jobs (create, dispatch, status, logs, notes, descriptions and descrip
  name: Jobox Kili API
  slug: kili
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.jobox.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.jobox.ai/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.jobox.ai/en/articles/2790099-getting-started-with-the-talus-pay-app
- group: operate
  title: ''
  type: Support
  url: https://help.jobox.ai/en/articles/9702013-how-and-when-to-contact-support
- group: company
  title: ''
  type: Blog
  url: https://blog.jobox.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jobox.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jobox.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jobox-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/jobox-ai-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jobox-ai-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: JOBOX.ai (Jobox) is a home-services fintech and marketplace-infrastructure platform for skilled trades professionals — locksmiths, plumbers, HVAC and appliance technicians. Founded in California in 2016 and operating since 2018, Jobox runs a mobile business app for independent pros (job intake from SMS/WhatsApp, dispatching, invoicing, tap-to-pay card acceptance, receipts, settlement reports, the Jobox Wallet and a Jobox credit card) plus a B2B "managed marketplace" product that lets retailers, distributors, discovery platforms and franchises embed home services into their own customer journeys through programmable APIs, an automated dispatch algorithm, a demand-partner dashboard, Jobox-handled KYC and weekly settlement reconciliation. Jobox.ai was acquired by Talus Pay in January 2024; the pro-facing mobile app and help center have since been rebranded to Talus Pay while the jobox.ai marketing site and the api.jobox.ai "Kili" production API remain live.
image: https://cdn.prod.website-files.com/621a3e492346748467acfaa9/62399d2f126332471592241d_256.png
layout: provider
mcp_servers:
- description: ''
  name: JOBOX.ai MCP Server
  slug: joboxai-mcp-server
modified: '2026-08-23'
name: JOBOX.ai
nav: Providers
network: true
overview: 'JOBOX.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Jobox Kili API. Tagged areas include Company, Home Services, Field Service Management, Marketplace, and Payments.


  JOBOX.ai''s developer surface includes documentation, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Jobox Ai Plans Pricing
  plan_count: 0
  slug: jobox-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Jobox Ai Rate Limits
  slug: jobox-ai-rate-limits
score:
  band: thin
  composite: 29.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 28.2
    developer_ergonomics: 35.7
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Jobox Ai Authentication
  slug: jobox-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Jobox Ai Domain Security
  slug: jobox-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jobox-ai
tags:
- Company
- Home Services
- Field Service Management
- Marketplace
- Payments
- Fintech
- Dispatching
- Skilled Trades
- KYC
- Wallet
website: https://www.jobox.ai/
---
