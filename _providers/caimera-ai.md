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
    agent_skills: false
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Caimera AI visual production platform
  name: Caimera API
  slug: caimera-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/caimera-ai/plans/caimera-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/caimera-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/caimera-ai/llms/caimera-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caimera-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/caimera-ai/mcp/caimera-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caimera-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/caimera-ai/well-known/caimera-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caimera-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/caimera-ai/hosts/caimera-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caimera-ai-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.caimera.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://app.caimera.ai/changelog
- group: auth
  href: https://artifacts.apis.io/caimera-ai/security/caimera-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caimera-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caimera.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.caimera.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caimera.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caimera.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.caimera.ai/en/
- group: docs
  title: ''
  type: Documentation
  url: https://help.caimera.ai/en/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://help.caimera.ai/mcp/v1
  - status: 401
    url: https://app.caimera.ai/api/mcp
  - status: 200
    url: https://caimera.ai/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: On-brand fashion visuals from sketch to sale. Caimera provides an AI visual production platform for fashion teams, offering AI fashion models, flat‑lay to on‑model catalog, editorials, video and tech packs in one solution. Try free.
image: https://framerusercontent.com/images/XdXXVRqvEk3ykrFjNO2zskNkyM.png
layout: provider
mcp_servers:
- description: Remote MCP server at help.caimera.ai.
  name: Caimera MCP Server
  slug: caimera-ai-mcp-yml
modified: '2026-11-03'
name: Caimera
nav: Providers
network: true
overview: 'Caimera is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Fashion, Visual-Production, Platform, and Image Generation.


  Caimera''s developer surface includes changelog, pricing, support, documentation, and 10 more developer resources.'
plans:
- name: Caimera Ai Plans Pricing
  plan_count: 5
  slug: caimera-ai-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 56.7
    operational_transparency: 7.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caimera Ai Domain Security
  slug: caimera-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: caimera-ai
tags:
- Artificial Intelligence
- Fashion
- Visual-Production
- Platform
- Image Generation
website: https://www.caimera.ai/
---
