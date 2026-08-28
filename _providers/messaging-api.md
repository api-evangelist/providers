---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Messaging Api Agentic Access
  operation_count: 6
  slug: messaging-api-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: Managing, sending, and receiving of messages via SMS and other channels.
  name: Messaging API Messages API
  slug: messaging-api-messages-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Messaging API Messages API
  slug: open-messaging-api-messages-api
- collection_type: open
  name: Messaging API Messages API
  slug: open-messaging-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/messaging-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/messaging-api-authentication.yml
created: '2024-12-29'
description: A template and concept entry for messaging APIs. This represents the pattern and structure for messaging API implementations used in storytelling, training, and knowledge bases.
finops:
- name: Messaging Api Finops
  service_category: API
  slug: messaging-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/messaging-api.png
layout: provider
modified: '2026-05-19'
name: Messaging API
nav: Providers
network: true
overview: 'Messaging API publishes 1 API on the [APIs.io](https://apis.io/) network: Messages API. Tagged areas include API Pattern, Messaging, and Template.


  Messaging API''s developer surface includes authentication and 1 more developer resources.'
plans:
- name: Messaging Api Plans Pricing
  plan_count: 3
  slug: messaging-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Messaging Api Rate Limits
  slug: messaging-api-rate-limits
score:
  band: thin
  composite: 26.9
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 61.5
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 26.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Messaging Api Authentication
  slug: messaging-api-authentication
  summary_line: apiKey · 1 scheme
slug: messaging-api
tags:
- API Pattern
- Messaging
- Template
---
