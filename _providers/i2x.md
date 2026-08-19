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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/i2x-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/i2x-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/i2x-llms.txt
- group: company
  title: ''
  type: Website
  url: https://i2x.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://i2x.ai/datenschutz.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://i2x.ai/nutzungsbedingungen.html
- group: operate
  title: ''
  type: Support
  url: https://i2x.ai/#contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/i2x-ai/
coverage:
  checked: '2026-08-14'
  detail: i2x sells an end-user contact-center SaaS and publishes no developer program at all — docs.i2x.ai has served a 52-byte nginx placeholder reading "Please stand by while configuration is in progress" since August 2023 and presents a self-signed certificate over HTTPS, while the only live API host, api.eu.i2x.ai, is the login-gated backend of the app.i2x.ai customer application (POST /organizations/v1/login) and returns a hard 404 on every specification and .well-known path.
  evidence:
  - status: 200
    url: http://docs.i2x.ai/
  - status: 404
    url: https://api.eu.i2x.ai/openapi.json
  - status: 404
    url: https://api.eu.i2x.ai/.well-known/agent-card.json
  - status: 404
    url: https://i2x-api.playground.dev.i2x.ai/openapi.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'i2x is a German real-time AI platform for contact centers, built by i2x GmbH in Mönchengladbach. It provides live agent assistance that surfaces contextual recommendations during calls in under 0.4 seconds, including automatic detection of purchase signals and faster agent onboarding; full-coverage call analysis with automatic transcription plus quality, compliance, and sales-opportunity scoring across 100% of conversations; and voicebots for automated inbound/outbound telephony and virtual agent-training scenarios. The platform emphasizes DSGVO/GDPR compliance with EU-only hosting in German data centers, prepared works-council documentation, and EU AI Act alignment, positioning itself as an alternative to US-cloud-dependent conversation-intelligence tools. i2x publishes no developer program: no API reference, no OpenAPI/AsyncAPI/GraphQL specification, no SDK on any package registry, no public GitHub organization, no MCP server, no agent card, no status page and no pricing
  — the only commercial entry point is a demo-request form. A private, login-gated API host does exist at api.eu.i2x.ai serving the customer web application at app.i2x.ai, but it is undocumented and is not offered as an integration surface. This profile was surfaced as a portfolio company of hv-capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/i2x.png
layout: provider
modified: '2026-08-14'
name: i2x
nav: Providers
network: true
overview: 'i2x is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Enterprise Software, Conversation Intelligence, Contact Center, and Speech Recognition.


  i2x''s developer surface includes support and 7 more developer resources.'
plans:
- name: I2X Plans Pricing
  plan_count: 0
  slug: i2x-plans-pricing
random_paper: 126
score:
  band: minimal
  composite: 10.0
  delta: -0.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/i2x/refs/heads/main/screenshots/i2x-2026-07-25T221936.png
security:
- kind: domain-security
  name: I2X Domain Security
  slug: i2x-domain-security
  summary_line: TLSv1.3 · DMARC
slug: i2x
tags:
- Company
- Ai Enterprise Software
- Conversation Intelligence
- Contact Center
- Speech Recognition
- Real-Time AI
- Sales Enablement
- Compliance
- Germany
website: https://i2x.ai/
---
