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
  type: DomainSecurity
  url: security/sense-street-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sensestreet.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sensestreet.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensestreet.com
- group: operate
  title: ''
  type: Support
  url: https://sensestreet.com/contact
- group: company
  title: ''
  type: Blog
  url: https://sensestreet.com/resources
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sensestreet.com/security-compliance/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://sensestreet.com/security-compliance/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/sense-street-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sense-street-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sense-street-llms.txt
created: '2026-07-17'
description: Sense Street provides production-grade AI workflow automation for capital markets, structuring unstructured OTC trading conversations in real time. Its platform connects to trading communication channels such as Bloomberg, Symphony and ICE and extracts RFQs, orders and market sentiment from broker chat, delivering them to the desk through an AI-Enhanced Blotter and a Quotebook that feeds structured market data to algo models and alerts. The product supports multiple asset classes (Fixed Income, Commodities) and languages with claimed 95%+ accuracy. API access — a batch processing API and WebSocket streaming endpoints secured with SSO and role-based access control — is offered to enterprise customers but is gated behind a sales/onboarding contact, so no public OpenAPI specification is published. Sense Street is a portfolio company of Seedcamp and Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sense-street.png
layout: provider
modified: '2026-07-21'
name: Sense Street
nav: Providers
network: true
overview: 'Sense Street is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Capital Markets, Trading, Artificial Intelligence, and Fintech.


  Sense Street''s developer surface includes documentation, support, engineering blog, and 8 more developer resources.'
random_paper: 50
score:
  band: emerging
  composite: 19.7
  delta: -1.1
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 20.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Sense Street Domain Security
  slug: sense-street-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Sense Street Trust Center
  slug: sense-street-trust-center
  summary_line: SOC 2 Type II, ISO 27001, Data Protection Registration Certificate
slug: sense-street
tags:
- Company
- Capital Markets
- Trading
- Artificial Intelligence
- Fintech
- Conversation Intelligence
- OTC
website: https://sensestreet.com
---
