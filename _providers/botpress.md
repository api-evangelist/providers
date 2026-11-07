---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Botpress Agentic Access
  operation_count: 31
  slug: botpress-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 1
apis:
- description: Webhook-based REST API for sending and receiving chat messages with deployed Botpress bots. Endpoint pattern is https://chat.botpress.cloud/{webhookUrl}/messages.
  name: Botpress Chat API
  slug: chat
- baseURL: https://api.botpress.cloud
  baseurl_source: declared
  description: The Admin API from Botpress — 3 operation(s) for admin.
  name: Botpress Admin API
  slug: botpress-admin-api
- baseURL: https://api.botpress.cloud
  baseurl_source: declared
  description: The Conversations API from Botpress — 3 operation(s) for conversations.
  name: Botpress Conversations API
  slug: botpress-conversations-api
- baseURL: https://api.botpress.cloud
  baseurl_source: declared
  description: The Files API from Botpress — 3 operation(s) for files.
  name: Botpress Files API
  slug: botpress-files-api
- baseURL: https://api.botpress.cloud
  baseurl_source: declared
  description: The Messages API from Botpress — 2 operation(s) for messages.
  name: Botpress Messages API
  slug: botpress-messages-api
- baseURL: https://api.botpress.cloud
  baseurl_source: declared
  description: The Tables API from Botpress — 3 operation(s) for tables.
  name: Botpress Tables API
  slug: botpress-tables-api
- baseURL: https://api.botpress.cloud
  baseurl_source: declared
  description: The Users API from Botpress — 2 operation(s) for users.
  name: Botpress Users API
  slug: botpress-users-api
- description: REST API for managing bots, integrations, conversations, users, and analytics on Botpress Cloud. Authentication via personal access tokens or workspace API keys.
  name: Botpress Cloud Management API
  slug: cloud-management
artifact_total: 23
collections:
- collection_type: open
  name: Botpress Cloud Admin API
  slug: open-botpress-admin-api
- collection_type: open
  name: Botpress Cloud Admin Conversations API
  slug: open-botpress-conversations-api
- collection_type: open
  name: Botpress Cloud Admin Files API
  slug: open-botpress-files-api
- collection_type: open
  name: Botpress Cloud Admin Messages API
  slug: open-botpress-messages-api
- collection_type: open
  name: Botpress Cloud Admin Tables API
  slug: open-botpress-tables-api
- collection_type: open
  name: Botpress Cloud Admin Users API
  slug: open-botpress-users-api
- collection_type: open
  name: Botpress Cloud API
  slug: open-botpress
common:
- group: other
  href: https://artifacts.apis.io/botpress/capabilities/botpress-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/botpress-capability-edges.yml
- group: company
  title: ''
  type: Blog
  url: https://botpress.com/blog
- group: agent
  href: https://artifacts.apis.io/botpress/agentic-access/botpress-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/botpress-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/botpress/security/botpress-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/botpress-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/botpress/security/botpress-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botpress-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/botpress/authentication/botpress-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botpress-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/botpress
- group: company
  title: ''
  type: Website
  url: https://botpress.com/
- group: docs
  title: ''
  type: Documentation
  url: https://botpress.com/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/botpress/botpress
- group: commercial
  href: https://artifacts.apis.io/botpress/plans/botpress-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botpress-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/botpress/rate-limits/botpress-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/botpress-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/botpress/finops/botpress-finops.yml
  title: ''
  type: FinOps
  url: finops/botpress-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://botpress.com/llms.txt
created: '2026-05-08'
description: Botpress is an open-source conversational AI platform for building, deploying, and managing chatbots with a visual flow editor and cloud hosting. Botpress Cloud exposes a REST API plus a Chat API for sending messages to deployed bots. Self-hosted Botpress remains open-source.
finops:
- has_sources: true
  method: generated
  name: Botpress Finops
  primary_unit: ''
  service_category: AI
  slug: botpress-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/botpress.png
layout: provider
modified: '2026-10-06'
name: Botpress
nav: Providers
network: true
overview: 'Botpress publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Conversations API, Files API, and 5 more. Tagged areas include Artificial Intelligence, Conversational AI, Chat, Open Source, and Bot Builder.


  The Botpress catalog on APIs.io includes 1 Spectral governance ruleset.


  Botpress'' developer surface includes engineering blog, authentication, documentation, GitHub presence, and 10 more developer resources.'
plans:
- name: Botpress Plans Pricing
  plan_count: 6
  slug: botpress-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 7
  name: Botpress Rate Limits
  slug: botpress-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Botpress API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: botpress-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 45.6
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 13.2
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/botpress/botpress-2026-06-20T173622.png
security:
- kind: authentication
  name: Botpress Authentication
  slug: botpress-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Botpress Domain Security
  slug: botpress-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Botpress Trust Center
  slug: botpress-trust-center
  summary_line: SOC 2, ISO 27001
slug: botpress
tags:
- Artificial Intelligence
- Conversational AI
- Chat
- Open Source
- Bot Builder
- LLM
website: https://botpress.com/
---
