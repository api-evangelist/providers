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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Clicksend Sms Agentic Access
  operation_count: 7
  slug: clicksend-sms-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- description: The Sms API from ClickSend SMS — 6 operation(s) for sms.
  name: ClickSend SMS Sms API
  slug: clicksend-sms-sms-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClickSend REST API v3 Sms API
  slug: open-clicksend-sms-sms-api
- collection_type: open
  name: ClickSend SMS REST API v3
  slug: open-clicksend-sms
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clicksend-sms-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clicksend-sms-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clicksend-sms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clicksend-sms-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clicksend
- group: company
  title: ''
  type: Website
  url: https://www.clicksend.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.clicksend.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clicksend.com/en/pricing/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.clicksend.com/signup
- group: other
  title: ''
  type: Knowledge Base
  url: https://help.clicksend.com
- group: company
  title: ''
  type: Blog
  url: https://blog.clicksend.com
created: '2026-05-11'
description: ClickSend is a global business communications platform for sending and receiving SMS, MMS, voice, email, fax, and physical post via API or web dashboard, with direct carrier routing and a 99.95% uptime SLA. The ClickSend REST API v3 provides endpoints for SMS, MMS, voice, email, fax, post letters, contacts, accounts, and webhooks, secured with HTTP Basic Authentication using a username and API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clicksend-sms.png
layout: provider
modified: '2026-05-11'
name: ClickSend SMS
nav: Providers
network: true
overview: 'ClickSend SMS publishes 1 API on the [APIs.io](https://apis.io/) network: Sms API. Tagged areas include SMS, MMS, Messaging, Voice, and Email.


  ClickSend SMS''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 28.6
  delta: -0.3
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 46.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clicksend-sms/refs/heads/main/screenshots/clicksend-sms-2026-06-20T174517.png
security:
- kind: authentication
  name: Clicksend Sms Authentication
  slug: clicksend-sms-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clicksend Sms Domain Security
  slug: clicksend-sms-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Clicksend Sms Trust Center
  slug: clicksend-sms-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: clicksend-sms
tags:
- SMS
- MMS
- Messaging
- Voice
- Email
- Fax
- Direct Mail
- Communications
website: https://www.clicksend.com
---
