---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
- acting_count: 4
  human_in_the_loop: 0
  name: Google Business Messages Agentic Access
  operation_count: 4
  slug: google-business-messages-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: The Conversations API from Google Business Messages — 4 operation(s) for conversations.
  name: Google Business Messages Conversations API
  slug: google-business-messages-conversations-api
artifact_total: 13
collections:
- collection_type: open
  name: Google Business Messages API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-business-messages-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-business-messages-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-business-messages-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-business-messages-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-business-messages-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google-business-communications
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/business-communications/business-messages/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/business-communications/business-messages
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google Business Messages API enables agents to send messages, create events, and manage customer satisfaction surveys within conversations. It allows businesses to communicate with customers directly through Google entry points such as Search and Maps.
finops:
- name: Google Business Messages Finops
  service_category: API
  slug: google-business-messages-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-business-messages.png
json_schemas:
- name: Google Business Message
  property_count: 9
  slug: Message
jsonld:
- class_count: 11
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Business Messages
nav: Providers
network: true
overview: 'Google Business Messages publishes 1 API on the [APIs.io](https://apis.io/) network: Conversations API. Tagged areas include Business Communications, Conversations, Customer Support, Google, and Messaging.


  The Google Business Messages catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Business Messages'' developer surface includes authentication, getting-started guide, pricing, and 6 more developer resources.'
plans:
- name: Google Business Messages Plans Pricing
  plan_count: 3
  slug: google-business-messages-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Google Business Messages Rate Limits
  slug: google-business-messages-rate-limits
rules:
- name: Google Business Messages API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-business-messages-jsonschema-spectral-rules
scopes:
- name: Google Business Messages Scopes
  scope_count: 1
  slug: google-business-messages-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 51.3
  delta: -3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.3
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.5
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
    score: 55.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-business-messages/refs/heads/main/screenshots/google-business-messages-2026-06-20T182030.png
security:
- kind: authentication
  name: Google Business Messages Authentication
  slug: google-business-messages-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Business Messages Domain Security
  slug: google-business-messages-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Business Messages Vulnerability Disclosure
  slug: google-business-messages-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-business-messages
tags:
- Business Communications
- Conversations
- Customer Support
- Google
- Messaging
---
