---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bridgeapp-ai/plans/bridgeapp-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bridgeapp-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bridgeapp-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bridgeapp-ai/well-known/bridgeapp-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bridgeapp-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bridgeapp-ai/hosts/bridgeapp-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridgeapp-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bridgeapp.ai/legal/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://bridgeapp.ai/resources/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bridgeapp.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://bridgeapp.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://bridgeapp.ai/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://coder.bridgeapp.ai/getting-started/overview/
- group: auth
  href: https://artifacts.apis.io/bridgeapp-ai/security/bridgeapp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridgeapp-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridgeapp.ai/
coverage:
  checked: '2026-11-03'
  detail: Provider docs are rendered via JavaScript and no machine‑readable OpenAPI or other contract could be found.
  evidence:
  - status: 200
    url: https://bridgeapp.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: BridgeApp provides an on‑premise AI‑powered workspace for teams, enabling creation, management and sharing of knowledge through documents, copilots, tasks and chat. It offers a unified platform for AI agents, collaborative task handling, and a searchable knowledge base, targeting enterprises seeking integrated AI assistance in their workflows.
image: https://bridgeapp.ai/_next/image?url=%2Fassets%2Flogo.png&w=256&q=75
layout: provider
modified: '2026-11-03'
name: BridgeApp
nav: Providers
network: true
overview: 'BridgeApp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Workspace, Team, Collaboration, and Knowledge Base.


  BridgeApp''s developer surface includes support, pricing, engineering blog, getting-started guide, and 8 more developer resources.'
plans:
- name: Bridgeapp Ai Plans Pricing
  plan_count: 3
  slug: bridgeapp-ai-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bridgeapp Ai Domain Security
  slug: bridgeapp-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bridgeapp-ai
tags:
- Artificial Intelligence
- Workspace
- Team
- Collaboration
- Knowledge Base
website: https://bridgeapp.ai/
---
