---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent Publishing, Quote & USDC Order API
  name: BidGlow API
  slug: bidglow-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/bidglow-ai/rules/bidglow-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bidglow-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bidglow-ai/json-ld/bidglow-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bidglow-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bidglow-ai/vocabulary/bidglow-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bidglow-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bidglow-ai/conformance/bidglow-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bidglow-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bidglow-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bidglow-ai/data-model/bidglow-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bidglow-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/bidglow-ai/conventions/bidglow-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bidglow-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/bidglow-ai/conventions/bidglow-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bidglow-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/bidglow-ai/errors/bidglow-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bidglow-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bidglow-ai/llms/bidglow-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidglow-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bidglow-ai/mcp/bidglow-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bidglow-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bidglow-ai/well-known/bidglow-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bidglow-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bidglow-ai/hosts/bidglow-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidglow-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidglow-ai/vendors/bidglow-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidglow-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bidglow.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidglow.ai/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://bidglow.ai/developers
- group: auth
  href: https://artifacts.apis.io/bidglow-ai/security/bidglow-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidglow-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidglow.ai/
created: '2026-11-02'
description: BidGlow is a platform that promotes websites, profiles, and businesses through AI-driven listings. Users can publish free listings with permission, optionally pay for higher placement, and view live statistics. The service enforces content review, offers transparent ranking based on verified payments, and provides developer documentation for AI integration.
image: https://bidglow.ai/og-homepage.png?v=20260827b
jsonld:
- class_count: 5
  name: Bidglow Ai Context
  property_count: 39
  slug: bidglow-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at bidglow.ai.
  name: BidGlow MCP Server
  slug: bidglow-ai-mcp-yml
modified: '2026-11-02'
name: BidGlow
nav: Providers
network: true
overview: 'BidGlow publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Promotion, Marketplace, Listings, and Developers.


  The BidGlow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BidGlow''s developer surface includes API reference and 18 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: BidGlow API Rules
  rule_count: 45
  severity_counts:
    error: 40
    hint: 0
    info: 4
    warn: 1
  slug: bidglow-ai-rules
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 5.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidglow Ai Domain Security
  slug: bidglow-ai-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: publish-agent
  slug: bidglow-ai-publish-agent
slug: bidglow-ai
tags:
- Artificial Intelligence
- Promotion
- Marketplace
- Listings
- Developers
website: https://bidglow.ai/
---
