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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Proompty Agentic Access
  operation_count: 14
  slug: proompty-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 9
apis:
- description: The Chat API from Proompty — 1 operation(s) for chat.
  name: Proompty Chat API
  slug: proompty-chat-api
- description: The Documents API from Proompty — 2 operation(s) for documents.
  name: Proompty Documents API
  slug: proompty-documents-api
- description: The Me API from Proompty — 1 operation(s) for me.
  name: Proompty Me API
  slug: proompty-me-api
- description: The Prompt API from Proompty — 2 operation(s) for prompt.
  name: Proompty Prompt API
  slug: proompty-prompt-api
- description: The Prompts API from Proompty — 3 operation(s) for prompts.
  name: Proompty Prompts API
  slug: proompty-prompts-api
- description: The Topic API from Proompty — 6 operation(s) for topic.
  name: Proompty Topic API
  slug: proompty-topic-api
- description: The Topics API from Proompty — 7 operation(s) for topics.
  name: Proompty Topics API
  slug: proompty-topics-api
- description: The Uploads API from Proompty — 1 operation(s) for uploads.
  name: Proompty Uploads API
  slug: proompty-uploads-api
- description: User related endpoints
  name: Proompty User API
  slug: proompty-user-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/proompty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proompty-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://app.proompty.com/docs/api
created: '2024-06-06'
description: Proompty is a web-based platform that offers customizable prompts and exercises to inspire creativity and productivity. Users can access a wide range of prompts, from writing exercises to drawing challenges, designed to spark new ideas and break through mental blocks.
finops:
- name: Proompty Finops
  service_category: API
  slug: proompty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/proompty.png
layout: provider
modified: '2026-05-19'
name: Proompty
nav: Providers
network: true
overview: 'Proompty publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Documents API, Me API, and 6 more. Tagged areas include Artificial Intelligence and Prompts.


  Proompty''s developer surface includes getting-started guide and 2 more developer resources.'
plans:
- name: Proompty Plans Pricing
  plan_count: 3
  slug: proompty-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Proompty Rate Limits
  slug: proompty-rate-limits
score:
  band: emerging
  composite: 26.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 55.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/proompty/refs/heads/main/screenshots/proompty-2026-06-20T192204.png
security:
- kind: domain-security
  name: Proompty Domain Security
  slug: proompty-domain-security
  summary_line: TLSv1.3 · HSTS
slug: proompty
tags:
- Artificial Intelligence
- Prompts
---
