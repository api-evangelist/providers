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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Lorikeet Agentic Access
  operation_count: 13
  slug: lorikeet-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.lorikeetcx.ai/v1
  baseurl_source: declared
  description: Create, continue, and inspect AI-agent-handled support conversations.
  name: Lorikeet Conversations API
  slug: lorikeet-conversations-api
- baseURL: https://api.lorikeetcx.ai/v1
  baseurl_source: declared
  description: Ingest and manage knowledge sources the agent reasons over.
  name: Lorikeet Knowledge API
  slug: lorikeet-knowledge-api
- baseURL: https://api.lorikeetcx.ai/v1
  baseurl_source: declared
  description: Post and list messages within a conversation.
  name: Lorikeet Messages API
  slug: lorikeet-messages-api
- baseURL: https://api.lorikeetcx.ai/v1
  baseurl_source: declared
  description: Manage webhook subscriptions and receive Lorikeet events.
  name: Lorikeet Webhooks API
  slug: lorikeet-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lorikeet Conversations API
  slug: open-lorikeet-conversations-api
- collection_type: open
  name: Lorikeet Conversations Knowledge API
  slug: open-lorikeet-knowledge-api
- collection_type: open
  name: Lorikeet Conversations Messages API
  slug: open-lorikeet-messages-api
- collection_type: open
  name: Lorikeet Conversations Webhooks API
  slug: open-lorikeet-webhooks-api
- collection_type: open
  name: Lorikeet API
  slug: open-lorikeet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lorikeet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lorikeet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lorikeet-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lorikeetcx
- group: company
  title: ''
  type: Website
  url: https://lorikeet.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lorikeetcx.ai/guides/quickstart
- group: commercial
  title: ''
  type: Plans
  url: plans/lorikeet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lorikeet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lorikeet-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lorikeetcx.ai/articles
created: '2026-07-01'
description: Lorikeet (Lorikeet CX) is an AI customer support agent built for complex and regulated businesses across chat, email, and voice. Rather than a single chatbot, it uses a workflow / "skills"-based orchestration layer that follows a company's standard operating procedures, calls into helpdesks (Zendesk, Intercom, Front) and internal systems through typed, no-code tools, and produces a per-step audit trail. Its programmatic surface centers on conversations, inbound and outbound webhooks / events, actions/tools, and knowledge ingestion, secured with scoped Bearer/API-key credentials. Full API reference is gated behind an access code, so endpoint detail below is modeled from Lorikeet's public integration and security materials and marked where unconfirmed.
finops:
- name: Lorikeet Finops
  service_category: AI and Machine Learning
  slug: lorikeet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lorikeet.png
layout: provider
modified: '2026-07-01'
name: Lorikeet
nav: Providers
network: true
overview: 'Lorikeet publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Conversations API, Knowledge API, Messages API, and 1 more. Tagged areas include Artificial Intelligence, Customer-Support, AI Agent, Support Automation, and Workflows.


  Lorikeet''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Lorikeet Plans Pricing
  plan_count: 1
  slug: lorikeet-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Lorikeet Rate Limits
  slug: lorikeet-rate-limits
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.9
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lorikeet/refs/heads/main/screenshots/lorikeet-2026-07-25T225543.png
security:
- kind: authentication
  name: Lorikeet Authentication
  slug: lorikeet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lorikeet Domain Security
  slug: lorikeet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lorikeet
tags:
- Artificial Intelligence
- Customer-Support
- AI Agent
- Support Automation
- Workflows
- Help Desk
website: https://lorikeet.ai
---
