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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Botpress Agentic Access
  operation_count: 31
  slug: botpress-agentic-access
  summary_line: 31 operations · 19 acting
api_count: 8
apis:
- description: Webhook-based REST API for sending and receiving chat messages with deployed Botpress bots. Endpoint pattern is https://chat.botpress.cloud/{webhookUrl}/messages.
  name: Botpress Chat API
  slug: chat
- description: The Admin API from Botpress — 3 operation(s) for admin.
  name: Botpress Admin API
  slug: botpress-admin-api
- description: The Conversations API from Botpress — 3 operation(s) for conversations.
  name: Botpress Conversations API
  slug: botpress-conversations-api
- description: The Files API from Botpress — 3 operation(s) for files.
  name: Botpress Files API
  slug: botpress-files-api
- description: The Messages API from Botpress — 2 operation(s) for messages.
  name: Botpress Messages API
  slug: botpress-messages-api
- description: The Tables API from Botpress — 3 operation(s) for tables.
  name: Botpress Tables API
  slug: botpress-tables-api
- description: The Users API from Botpress — 2 operation(s) for users.
  name: Botpress Users API
  slug: botpress-users-api
- description: REST API for managing bots, integrations, conversations, users, and analytics on Botpress Cloud. Authentication via personal access tokens or workspace API keys.
  name: Botpress Cloud Management API
  slug: cloud-management
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/botpress-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/botpress-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/botpress-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/botpress-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/botpress-rate-limits.yml
- group: commercial
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
- name: Botpress Finops
  service_category: AI
  slug: botpress-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/botpress.png
layout: provider
modified: '2026-07-25'
name: Botpress
nav: Providers
network: true
overview: 'Botpress publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Conversations API, Files API, and 3 more. Tagged areas include Artificial Intelligence, Conversational, Chat, Open-Source, and Bot Builder.


  Botpress'' developer surface includes authentication, documentation, GitHub presence, and 9 more developer resources.'
plans:
- name: Botpress Plans Pricing
  plan_count: 6
  slug: botpress-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 7
  name: Botpress Rate Limits
  slug: botpress-rate-limits
score:
  band: thin
  composite: 36.2
  delta: 3.9
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/botpress/refs/heads/main/screenshots/botpress-2026-06-20T173622.png
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
- Conversational
- Chat
- Open-Source
- Bot Builder
- LLM
website: https://botpress.com/
---
