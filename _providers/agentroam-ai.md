---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/agentroam-ai/plans/agentroam-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentroam-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agentroam-ai/llms/agentroam-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentroam-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agentroam-ai/hosts/agentroam-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentroam-ai-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://agentroam.ai/trust
- group: auth
  href: https://artifacts.apis.io/agentroam-ai/security/agentroam-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentroam-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentroam.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentroam.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://agentroam.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://agentroam.ai/.well-known/mcp.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agentroam.ai/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://agentroam.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentroam.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentroam.ai/privacy
coverage:
  checked: '2026-11-01'
  detail: Developer portal provides HTML docs but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract.
  evidence:
  - status: 200
    url: https://agentroam.ai/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AgentRoam.ai provides travel eSIMs that can be purchased with stablecoins and cryptocurrencies. The platform offers a range of data plans for over 130 countries, allowing users to buy, activate, and manage eSIMs instantly via email QR codes. It targets travelers seeking flexible, cashless connectivity, featuring AI‑ready checkout, crypto payments, and a developer-friendly MCP skill for integration.
image: https://agentroam.ai/brand/og-image.jpg
layout: provider
modified: '2026-11-01'
name: AgentRoam.ai
nav: Providers
network: true
overview: 'AgentRoam.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include eSIM, Travel Data, AI Agents, and Mobile Connectivity.


  AgentRoam.ai''s developer surface includes documentation, API reference, getting-started guide, support, and 9 more developer resources.'
plans:
- name: Agentroam Ai Plans Pricing
  plan_count: 69
  slug: agentroam-ai-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 46.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 39.3
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentroam Ai Domain Security
  slug: agentroam-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentroam-ai
tags:
- eSIM
- Travel Data
- AI Agents
- Mobile Connectivity
website: https://agentroam.ai/
---
