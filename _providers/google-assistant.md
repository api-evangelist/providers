---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
  score: 20.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Assistant Agentic Access
  operation_count: 6
  slug: google-assistant-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- description: Interact with Google Assistant
  name: Google Assistant Assistant API
  slug: google-assistant-assistant-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Assistant API
  slug: open-google-assistant-assistant-api
- collection_type: open
  name: Google Assistant API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-assistant-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-assistant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-assistant-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googlesamples
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/assistant/sdk/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/assistant
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-assistant/refs/heads/main/json-ld/google-assistant.jsonld
created: '2026-03-13'
description: The Google Assistant API enables developers to embed the Google Assistant into devices and applications. It provides conversational interfaces through gRPC and REST endpoints for sending text or audio queries and receiving responses. The API supports device model and instance registration, custom Actions with intents and scenes, and the Actions SDK for building conversational experiences that extend the Assistant's capabilities.
finops:
- name: Google Assistant Finops
  service_category: API
  slug: google-assistant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-assistant.png
json_schemas:
- name: Google Assistant API Schema
  property_count: 0
  slug: google-assistant
jsonld:
- class_count: 0
  name: Google Assistant Context
  property_count: 9
  slug: google-assistant
layout: provider
modified: '2026-05-19'
name: Google Assistant
nav: Providers
network: true
overview: 'Google Assistant publishes 1 API on the [APIs.io](https://apis.io/) network: Assistant API. Tagged areas include Actions on Google, Conversational AI, Google Assistant, Natural-Language, and Smart Home.


  The Google Assistant catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Assistant''s developer surface includes getting-started guide, pricing, and 5 more developer resources.'
plans:
- name: Google Assistant Plans Pricing
  plan_count: 3
  slug: google-assistant-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Google Assistant Rate Limits
  slug: google-assistant-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Assistant API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-assistant-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.7
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 58.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-assistant/refs/heads/main/screenshots/google-assistant-2026-06-20T182023.png
security:
- kind: domain-security
  name: Google Assistant Domain Security
  slug: google-assistant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Assistant Vulnerability Disclosure
  slug: google-assistant-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-assistant
tags:
- Actions on Google
- Conversational AI
- Google Assistant
- Natural-Language
- Smart Home
- Voice Assistant
---
