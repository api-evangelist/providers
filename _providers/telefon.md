---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Telefon Agentic Access
  operation_count: 20
  slug: telefon-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 7
apis:
- description: Search for available numbers to purchase
  name: Telefon Available Numbers API
  slug: telefon-available-numbers-api
- description: Make and manage phone calls
  name: Telefon Calls API
  slug: telefon-calls-api
- description: Multi-party conferencing
  name: Telefon Conferences API
  slug: telefon-conferences-api
- description: Send and receive SMS and MMS messages
  name: Telefon Messages API
  slug: telefon-messages-api
- description: Manage numbers in your account
  name: Telefon Owned Numbers API
  slug: telefon-owned-numbers-api
- description: Call recording management
  name: Telefon Recordings API
  slug: telefon-recordings-api
- description: Recording transcription management
  name: Telefon Transcriptions API
  slug: telefon-transcriptions-api
artifact_total: 31
collections:
- collection_type: postman
  name: Telefon Number Management Available Numbers API
  slug: postman-telefon-available-numbers-api
- collection_type: postman
  name: Telefon Number Management Available Numbers Calls API
  slug: postman-telefon-calls-api
- collection_type: postman
  name: Telefon Number Management Available Numbers Conferences API
  slug: postman-telefon-conferences-api
- collection_type: postman
  name: Telefon Number Management Available Numbers Messages API
  slug: postman-telefon-messages-api
- collection_type: postman
  name: Telefon Number Management Available Numbers Owned Numbers API
  slug: postman-telefon-owned-numbers-api
- collection_type: postman
  name: Telefon Number Management Available Numbers Recordings API
  slug: postman-telefon-recordings-api
- collection_type: postman
  name: Telefon Number Management Available Numbers Transcriptions API
  slug: postman-telefon-transcriptions-api
- collection_type: open
  name: Telefon Number Management API
  slug: open-telefon-numbers
- collection_type: open
  name: Telefon Call Recording API
  slug: open-telefon-recording
- collection_type: open
  name: Telefon SMS API
  slug: open-telefon-sms
- collection_type: open
  name: Telefon Voice API
  slug: open-telefon-voice
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/telefon/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telefon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telefon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telefon-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.telefon.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.telefon.com/authentication
- group: build
  title: ''
  type: SDKs
  url: https://www.telefon.com/sdks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telefon.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telefon.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telefon.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.telefon.com/support
- group: company
  title: ''
  type: Blog
  url: https://blog.telefon.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.telefon.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telefon.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/telefon-api
- group: agent
  title: ''
  type: LlmsText
  url: https://telefon.com/llms.txt
created: '2024-01-15'
description: Telefon is a cloud-based programmable communications platform providing voice calling, SMS messaging, number management, and call recording APIs for developers and enterprises. The platform enables applications to make and receive phone calls, send SMS and MMS messages, manage phone number inventories, and record calls for compliance and quality assurance purposes. Telefon supports global coverage across 180+ countries with competitive per-minute and per-message pricing.
examples:
- key_count: 2
  name: Telefon Create Call Example
  slug: telefon-create-call-example
- key_count: 2
  name: Telefon Send Sms Example
  slug: telefon-send-sms-example
finops:
- name: Telefon Finops
  service_category: Communications / CPaaS
  slug: telefon-finops
image: https://www.telefon.com/logo.png
json_schemas:
- name: Telefon Call
  property_count: 11
  slug: telefon-call
json_structures:
- name: Telefon Call Structure
  property_count: 0
  slug: telefon-call-structure
jsonld:
- class_count: 6
  name: Telefon Context
  property_count: 20
  slug: telefon-context
layout: provider
modified: '2026-05-19'
name: Telefon
nav: Providers
network: true
overview: 'Telefon publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Available Numbers API, Calls API, Conferences API, and 4 more. Tagged areas include Call Recording, Communications, CPaaS, Global Coverage, and Messaging.


  The Telefon catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telefon''s developer surface includes authentication, getting-started guide, support, engineering blog, changelog, pricing, GitHub presence, and 9 more developer resources.'
plans:
- name: Telefon Plans Pricing
  plan_count: 1
  slug: telefon-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 1
  name: Telefon Rate Limits
  slug: telefon-rate-limits
rules:
- name: Telefon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: telefon-jsonschema-spectral-rules
- name: Telefon API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 4
  slug: telefon-rules
score:
  band: developing
  composite: 55.5
  delta: -6.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.1
    developer_ergonomics: 39.1
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/telefon/refs/heads/main/screenshots/telefon-2026-06-20T195028.png
security:
- kind: authentication
  name: Telefon Authentication
  slug: telefon-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Telefon Domain Security
  slug: telefon-domain-security
  summary_line: DMARC
slug: telefon
tags:
- Call Recording
- Communications
- CPaaS
- Global Coverage
- Messaging
- Number Provisioning
- SMS
- Telephony
- Voice
- VoIP
website: https://www.telefon.com
---
