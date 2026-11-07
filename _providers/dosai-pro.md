---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Manage DOS AI projects, leads, conversations and analytics programmatically.
  name: DOS AI Public API
  slug: dos-ai-public-api
artifact_total: 6
asyncapis:
- description: ''
  name: Dosai Pro Webhooks
  slug: dosai-pro-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/dosai-pro/plans/dosai-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dosai-pro-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dosai-pro/vocabulary/dosai-pro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dosai-pro-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dosai-pro/asyncapi/dosai-pro-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dosai-pro-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dosai-pro/conventions/dosai-pro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dosai-pro-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dosai-pro/authentication/dosai-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dosai-pro-authentication.yml
- group: design
  href: https://artifacts.apis.io/dosai-pro/conformance/dosai-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dosai-pro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dosai-pro/llms/dosai-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dosai-pro-llms.txt
- group: agent
  href: https://artifacts.apis.io/dosai-pro/mcp/dosai-pro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dosai-pro-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dosai-pro/well-known/dosai-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dosai-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/dosai-pro/hosts/dosai-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dosai-pro-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dosai.pro/terms
- group: auth
  title: ''
  type: Security
  url: https://dosai.pro/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dosai.pro/privacy
- group: start
  title: ''
  type: Login
  url: https://dosai.pro/login
- group: other
  title: ''
  type: Leadership
  url: https://dosai.pro/learn/team
- group: start
  title: ''
  type: GettingStarted
  url: https://dosai.pro/docs/guide/00-start/02-quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://dosai.pro/llms.txt
- group: auth
  href: https://artifacts.apis.io/dosai-pro/security/dosai-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dosai-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dosai.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://dosai.pro/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://dosai.pro/#brut-pricing
- group: company
  title: ''
  type: Blog
  url: https://dosai.pro/blog
created: '2026-11-05'
description: DOS AI provides an AI-powered assistant platform for WhatsApp, Instagram, and Telegram, enabling businesses to automate sales, support, and lead qualification. The service integrates with CRM systems, offers 24/7 client interaction, and can be deployed in 10‑15 minutes without developers. It targets worldwide markets and supports multiple languages, positioning itself as a no‑code solution for conversational AI in messaging channels.
image: https://dosai.pro/og?v=20261024
layout: provider
mcp_servers:
- description: Remote MCP server at dosai.pro.
  name: DOS AI MCP Server
  slug: dosai-pro-mcp-yml
modified: '2026-11-05'
name: DOS AI
nav: Providers
network: true
overview: 'DOS AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Messaging, Chatbots, No-Code, and CRM.


  The DOS AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DOS AI''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Dosai Pro Plans Pricing
  plan_count: 1
  slug: dosai-pro-plans-pricing
random_paper: 22
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 39.0
    developer_ergonomics: 42.9
    discoverability: 66.7
    operational_transparency: 18.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dosai Pro Authentication
  slug: dosai-pro-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dosai Pro Domain Security
  slug: dosai-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dosai-pro
tags:
- Artificial Intelligence
- Messaging
- Chatbots
- No-Code
- CRM
- Company
website: https://dosai.pro/
---
