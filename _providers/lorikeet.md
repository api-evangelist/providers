---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Lorikeet Agentic Access
  operation_count: 13
  slug: lorikeet-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 2
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
artifact_total: 17
collections:
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
- group: other
  href: https://artifacts.apis.io/lorikeet/capabilities/lorikeet-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lorikeet-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/lorikeet/agentic-access/lorikeet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lorikeet-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lorikeet/security/lorikeet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lorikeet-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lorikeet/authentication/lorikeet-authentication.yml
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
  href: https://artifacts.apis.io/lorikeet/plans/lorikeet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lorikeet-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lorikeet/rate-limits/lorikeet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lorikeet-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lorikeet/finops/lorikeet-finops.yml
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
- has_sources: true
  method: generated
  name: Lorikeet Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: lorikeet-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lorikeet.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.lorikeetcx.ai over HTTP.
  name: Lorikeet MCP Server
  slug: lorikeet
modified: '2026-07-01'
name: Lorikeet
nav: Providers
network: true
overview: 'Lorikeet publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversations API, Knowledge API, Messages API, and 1 more. Tagged areas include Artificial Intelligence, Customer Service, AI Agents, Support Automation, and Workflows.


  The Lorikeet catalog on APIs.io includes 1 Spectral governance ruleset.


  Lorikeet''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Lorikeet Plans Pricing
  plan_count: 1
  slug: lorikeet-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Lorikeet Rate Limits
  slug: lorikeet-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Lorikeet API Rules
  rule_count: 61
  severity_counts:
    error: 50
    hint: 0
    info: 5
    warn: 6
  slug: lorikeet-rules
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 30.3
    developer_ergonomics: 25.0
    discoverability: 68.3
    operational_transparency: 7.9
  previous_composite: 21.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 10.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lorikeet/lorikeet-2026-07-25T225543.png
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
- Customer Service
- AI Agents
- Support Automation
- Workflows
- Help Desk
website: https://lorikeet.ai
---
