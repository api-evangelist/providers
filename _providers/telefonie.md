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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Telefonie Agentic Access
  operation_count: 22
  slug: telefonie-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 6
apis:
- description: Search for phone numbers to purchase
  name: Telefonie Available Numbers API
  slug: telefonie-available-numbers-api
- description: Make and manage voice calls
  name: Telefonie Calls API
  slug: telefonie-calls-api
- description: Multi-party conferencing
  name: Telefonie Conferences API
  slug: telefonie-conferences-api
- description: Send and receive SMS/MMS messages
  name: Telefonie Messages API
  slug: telefonie-messages-api
- description: Manage phone numbers in your account
  name: Telefonie Owned Numbers API
  slug: telefonie-owned-numbers-api
- description: Manage call recordings
  name: Telefonie Recordings API
  slug: telefonie-recordings-api
artifact_total: 29
collections:
- collection_type: postman
  name: Telefonie Number Management Available Numbers API
  slug: postman-telefonie-available-numbers-api
- collection_type: postman
  name: Telefonie Number Management Available Numbers Calls API
  slug: postman-telefonie-calls-api
- collection_type: postman
  name: Telefonie Number Management Available Numbers Conferences API
  slug: postman-telefonie-conferences-api
- collection_type: postman
  name: Telefonie Number Management Available Numbers Messages API
  slug: postman-telefonie-messages-api
- collection_type: postman
  name: Telefonie Number Management Available Numbers Owned Numbers API
  slug: postman-telefonie-owned-numbers-api
- collection_type: postman
  name: Telefonie Number Management Available Numbers Recordings API
  slug: postman-telefonie-recordings-api
- collection_type: open
  name: Telefonie Number Management API
  slug: open-telefonie-numbers
- collection_type: open
  name: Telefonie Call Recording API
  slug: open-telefonie-recording
- collection_type: open
  name: Telefonie SMS API
  slug: open-telefonie-sms
- collection_type: open
  name: Telefonie Voice API
  slug: open-telefonie-voice
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/telefonie/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telefonie-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telefonie-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://developers.telefonie.com/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.telefonie.com/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.telefonie.com/rate-limits
- group: build
  title: ''
  type: SDKs
  url: https://www.telefonie.com/sdks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telefonie.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telefonie.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telefonie.com/privacy
- group: start
  title: ''
  type: Signup
  url: https://www.telefonie.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.telefonie.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.telefonie.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telefonie.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.telefonie.com/changelog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/telefonie
created: '2024-01-20'
description: Telefonie is a cloud communications platform providing programmable telephony, voice, SMS, and number management APIs for developers and businesses. The platform enables developers to build voice calling, SMS messaging, number provisioning, and call recording capabilities into their applications. Telefonie supports WebRTC, SIP trunking, and REST APIs for building modern communication workflows.
examples:
- key_count: 2
  name: Telefonie Initiate Call Example
  slug: telefonie-initiate-call-example
- key_count: 2
  name: Telefonie Send Message Example
  slug: telefonie-send-message-example
finops:
- name: Telefonie Finops
  service_category: Communications / CPaaS
  slug: telefonie-finops
image: https://www.telefonie.com/logo.png
json_schemas:
- name: Telefonie Call
  property_count: 14
  slug: telefonie-call
- name: Telefonie SMS Message
  property_count: 16
  slug: telefonie-message
json_structures:
- name: Telefonie Call Structure
  property_count: 0
  slug: telefonie-call-structure
jsonld:
- class_count: 5
  name: Telefonie Context
  property_count: 21
  slug: telefonie-context
layout: provider
modified: '2026-05-19'
name: Telefonie
nav: Providers
network: true
overview: 'Telefonie publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Available Numbers API, Calls API, Conferences API, and 3 more. Tagged areas include Call Recording, CPaaS, Messaging, Number Provisioning, and SMS.


  The Telefonie catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telefonie''s developer surface includes authentication, getting-started guide, signup flow, engineering blog, pricing, changelog, GitHub presence, and 9 more developer resources.'
plans:
- name: Telefonie Plans Pricing
  plan_count: 1
  slug: telefonie-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Telefonie Rate Limits
  slug: telefonie-rate-limits
rules:
- name: Telefonie API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: telefonie-jsonschema-spectral-rules
- name: Telefonie API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 4
  slug: telefonie-rules
score:
  band: strong
  composite: 56.3
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 69.0
    developer_ergonomics: 34.8
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 26.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telefonie/refs/heads/main/screenshots/telefonie-2026-06-20T195029.png
security:
- kind: authentication
  name: Telefonie Authentication
  slug: telefonie-authentication
  summary_line: apiKey · 1 scheme
slug: telefonie
tags:
- Call Recording
- CPaaS
- Messaging
- Number Provisioning
- SMS
- Telecommunications
- Telephony
- Voice
- VoIP
website: https://www.telefonie.com
---
