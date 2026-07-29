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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Trivia Db Agentic Access
  operation_count: 5
  slug: open-trivia-db-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: Retrieve available trivia categories.
  name: Open Trivia DB Categories API
  slug: open-trivia-db-categories-api
- description: Retrieve trivia questions.
  name: Open Trivia DB Questions API
  slug: open-trivia-db-questions-api
- description: Manage session tokens to track served questions.
  name: Open Trivia DB Tokens API
  slug: open-trivia-db-tokens-api
artifact_total: 9
collections:
- collection_type: open
  name: Open Trivia DB API
  slug: open-open-trivia-db
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-trivia-db-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-trivia-db-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opentdb.com
- group: docs
  title: ''
  type: Documentation
  url: https://opentdb.com/api_config.php
created: '2025-02-12'
description: The Open Trivia Database provides a completely free JSON API for use in programming projects. Use of this API does not require an API key, just generate the URL and use it in your own application to retrieve trivia questions across multiple categories, difficulties, and types.
finops:
- name: Open Trivia Db Finops
  service_category: API
  slug: open-trivia-db-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-trivia-db.png
layout: provider
modified: '2026-05-19'
name: Open Trivia DB
nav: Providers
network: true
overview: 'Open Trivia DB publishes 3 APIs on the [APIs.io](https://apis.io/) network: Categories API, Questions API, and Tokens API. Tagged areas include Free, Games, Questions, and Trivia.


  Open Trivia DB''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Open Trivia Db Plans Pricing
  plan_count: 3
  slug: open-trivia-db-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Open Trivia Db Rate Limits
  slug: open-trivia-db-rate-limits
score:
  band: thin
  composite: 33.4
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.5
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-trivia-db/refs/heads/main/screenshots/open-trivia-db-2026-06-20T190856.png
security:
- kind: domain-security
  name: Open Trivia Db Domain Security
  slug: open-trivia-db-domain-security
  summary_line: TLSv1.3 · HSTS
slug: open-trivia-db
tags:
- Free
- Games
- Questions
- Trivia
website: https://opentdb.com
---
