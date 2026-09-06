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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Proompty Agentic Access
  operation_count: 14
  slug: proompty-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- baseURL: https://app.proompty.com/api/
  baseurl_source: declared
  description: The Chat API from Proompty — 1 operation(s) for chat.
  name: Proompty Chat API
  slug: proompty-chat-api
- baseURL: https://app.proompty.com/api/
  baseurl_source: declared
  description: The Documents API from Proompty — 2 operation(s) for documents.
  name: Proompty Documents API
  slug: proompty-documents-api
- baseURL: https://app.proompty.com/api/
  baseurl_source: declared
  description: The Me API from Proompty — 1 operation(s) for me.
  name: Proompty Me API
  slug: proompty-me-api
- baseURL: https://app.proompty.com/api/
  baseurl_source: declared
  description: The Prompt API from Proompty — 2 operation(s) for prompt.
  name: Proompty Prompt API
  slug: proompty-prompt-api
- baseURL: https://app.proompty.com/api/
  baseurl_source: declared
  description: The Prompts API from Proompty — 3 operation(s) for prompts.
  name: Proompty Prompts API
  slug: proompty-prompts-api
- baseURL: https://app.proompty.com/api/
  baseurl_source: declared
  description: The Topic API from Proompty — 6 operation(s) for topic.
  name: Proompty Topic API
  slug: proompty-topic-api
- baseURL: https://app.proompty.com/api/
  baseurl_source: declared
  description: The Topics API from Proompty — 7 operation(s) for topics.
  name: Proompty Topics API
  slug: proompty-topics-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Proompty Chat API
  slug: open-proompty-chat-api
- collection_type: open
  name: Proompty Chat Documents API
  slug: open-proompty-documents-api
- collection_type: open
  name: Proompty Chat Me API
  slug: open-proompty-me-api
- collection_type: open
  name: Proompty Chat Prompt API
  slug: open-proompty-prompt-api
- collection_type: open
  name: Proompty Chat Prompts API
  slug: open-proompty-prompts-api
- collection_type: open
  name: Proompty Chat Topic API
  slug: open-proompty-topic-api
- collection_type: open
  name: Proompty Chat Topics API
  slug: open-proompty-topics-api
- collection_type: open
  name: Proompty Chat Uploads API
  slug: open-proompty-uploads-api
- collection_type: open
  name: Proompty Chat User API
  slug: open-proompty-user-api
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
overview: 'Proompty publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Documents API, Me API, and 4 more. Tagged areas include Artificial Intelligence and Prompts.


  Proompty''s developer surface includes getting-started guide and 2 more developer resources.'
plans:
- name: Proompty Plans Pricing
  plan_count: 3
  slug: proompty-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Proompty Rate Limits
  slug: proompty-rate-limits
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.9
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
