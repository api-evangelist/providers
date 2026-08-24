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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Telefoon Agentic Access
  operation_count: 15
  slug: telefoon-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 5
apis:
- description: Search available numbers
  name: Telefoon Available Numbers API
  slug: telefoon-available-numbers-api
- description: Make and manage voice calls
  name: Telefoon Calls API
  slug: telefoon-calls-api
- description: Multi-party conferencing
  name: Telefoon Conferences API
  slug: telefoon-conferences-api
- description: Send and receive SMS messages
  name: Telefoon Messages API
  slug: telefoon-messages-api
- description: Manage owned numbers
  name: Telefoon Owned Numbers API
  slug: telefoon-owned-numbers-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Telefoon Number Management Available Numbers API
  slug: open-telefoon-available-numbers-api
- collection_type: open
  name: Telefoon Number Management Available Numbers Calls API
  slug: open-telefoon-calls-api
- collection_type: open
  name: Telefoon Number Management Available Numbers Conferences API
  slug: open-telefoon-conferences-api
- collection_type: open
  name: Telefoon Number Management Available Numbers Messages API
  slug: open-telefoon-messages-api
- collection_type: open
  name: Telefoon Number Management API
  slug: open-telefoon-numbers
- collection_type: open
  name: Telefoon Number Management Available Numbers Owned Numbers API
  slug: open-telefoon-owned-numbers-api
- collection_type: open
  name: Telefoon SMS API
  slug: open-telefoon-sms
- collection_type: open
  name: Telefoon Voice API
  slug: open-telefoon-voice
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telefoon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telefoon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telefoon-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://developers.telefoon.com/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.telefoon.com/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.telefoon.com/rate-limits
- group: auth
  title: ''
  type: GDPR
  url: https://www.telefoon.com/gdpr
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telefoon.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telefoon.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telefoon.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telefoon.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.telefoon.com/support
- group: company
  title: ''
  type: Blog
  url: https://blog.telefoon.com
created: '2024-01-01'
description: Telefoon is a cloud telephony and communications platform offering programmable voice, SMS, and number management APIs tailored for European markets. Built for GDPR compliance and EU regulatory requirements, Telefoon provides developers with REST APIs to build voice calling, SMS notification, number provisioning, and interactive voice response (IVR) solutions. The platform supports Dutch, Belgian, German, and broader European telecommunications infrastructure with local number availability and EU data residency.
examples:
- key_count: 2
  name: Telefoon Initiate Call Example
  slug: telefoon-initiate-call-example
- key_count: 2
  name: Telefoon Send Sms Example
  slug: telefoon-send-sms-example
finops:
- name: Telefoon Finops
  service_category: Communications / CPaaS
  slug: telefoon-finops
image: https://www.telefoon.com/logo.png
json_schemas:
- name: Telefoon Call
  property_count: 10
  slug: telefoon-call
json_structures:
- name: Telefoon Call Structure
  property_count: 0
  slug: telefoon-call-structure
jsonld:
- class_count: 4
  name: Telefoon Context
  property_count: 18
  slug: telefoon-context
layout: provider
modified: '2026-05-19'
name: Telefoon
nav: Providers
network: true
overview: 'Telefoon publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Available Numbers API, Calls API, Conferences API, and 2 more. Tagged areas include Belgium, CPaaS, EU Data Residency, Europe, and GDPR Compliant.


  The Telefoon catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telefoon''s developer surface includes authentication, getting-started guide, pricing, support, engineering blog, and 8 more developer resources.'
plans:
- name: Telefoon Plans Pricing
  plan_count: 1
  slug: telefoon-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Telefoon Rate Limits
  slug: telefoon-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Telefoon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: telefoon-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Telefoon API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: telefoon-rules
score:
  band: thin
  composite: 35.4
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 60.1
    developer_ergonomics: 15.5
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 29.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Telefoon Authentication
  slug: telefoon-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Telefoon Domain Security
  slug: telefoon-domain-security
  summary_line: DNSSEC
slug: telefoon
tags:
- Belgium
- CPaaS
- EU Data Residency
- Europe
- GDPR Compliant
- Messaging
- Netherlands
- Number Provisioning
- SMS
- Telephony
- Voice
website: https://www.telefoon.com
---
