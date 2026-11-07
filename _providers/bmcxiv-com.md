---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://breach402.bmcxiv.com
  baseurl_source: declared
  description: Machine-readable agent discovery.
  name: BMC XIV Discovery API
  slug: bmcxiv-com-discovery-api
- baseURL: https://breach402.bmcxiv.com
  baseurl_source: declared
  description: Prove control of the owner's mailbox before a paid lookup.
  name: BMC XIV Owner Verification API
  slug: bmcxiv-com-owner-verification-api
- baseURL: https://breach402.bmcxiv.com
  baseurl_source: declared
  description: $1.00 USDC on Solana via x402.
  name: BMC XIV Paid Check API
  slug: bmcxiv-com-paid-check-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/bmcxiv-com/capabilities/bmcxiv-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bmcxiv-com-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/bmcxiv-com/plans/bmcxiv-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bmcxiv-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bmcxiv-com/rate-limits/bmcxiv-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bmcxiv-com-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://breach402.bmcxiv.com/llms.txt
- group: other
  href: https://artifacts.apis.io/bmcxiv-com/overlays/bmcxiv-com-breach402-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bmcxiv-com-breach402-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://bmcxiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://breach402.bmcxiv.com/
- group: docs
  title: ''
  type: APIReference
  url: https://breach402.bmcxiv.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://breach402.bmcxiv.com/skill.md
- group: agent
  href: https://artifacts.apis.io/bmcxiv-com/llms/bmcxiv-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bmcxiv-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://breach402.bmcxiv.com/llms.txt
- group: other
  href: https://artifacts.apis.io/bmcxiv-com/a2a/bmcxiv-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bmcxiv-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/bmcxiv-com/mcp/bmcxiv-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bmcxiv-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bmcxiv-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bmcxiv-com/well-known/bmcxiv-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bmcxiv-com-well-known.yml
- group: build
  href: https://artifacts.apis.io/bmcxiv-com/packages/bmcxiv-com-packages.yml
  title: ''
  type: Packages
  url: packages/bmcxiv-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/bmcxiv-com/security/bmcxiv-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bmcxiv-com-domain-security.yml
created: '2026-09-19'
description: 'BMC XIV operates Breach402, an agent-native breach-intelligence service at breach402.bmcxiv.com. An AI agent verifies that its owner controls an exact email address (free, by confirmation link or one-time code), then pays $1.00 USDC on Solana through x402 for one lookup across a corpus the provider describes as more than 13.3 billion indexed breach records, receiving the complete private records plus deterministic cyber-expert and social-engineering mitigation guidance. The surface is published for machines first: an OpenAPI 3.1 contract, a remote MCP server with eight tools and five resources, an A2A 0.3 agent card, an llms.txt, and five portable Agent Skill / trust documents. It is explicitly not a third-party lookup, surveillance or screening tool.'
finops:
- has_sources: true
  method: derived
  name: Bmcxiv Com Finops
  primary_unit: check
  service_category: ''
  slug: bmcxiv-com-finops
  template: false
layout: provider
mcp_servers:
- description: Remote MCP server at breach402.bmcxiv.com over HTTP; 8 tools listed.
  name: BMC XIV MCP Server
  slug: breach402
modified: '2026-09-19'
name: BMC XIV
nav: Providers
network: true
overview: 'BMC XIV publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API, Owner Verification API, and Paid Check API. Tagged areas include Company, Security, Cybersecurity, Breach Intelligence, and Identity Protection.


  The BMC XIV catalog on APIs.io includes 1 Spectral governance ruleset.


  BMC XIV''s developer surface includes pricing, documentation, API reference, getting-started guide, and 13 more developer resources.'
plans:
- name: Bmcxiv Com Plans Pricing
  plan_count: 1
  slug: bmcxiv-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Bmcxiv Com Rate Limits
  slug: bmcxiv-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: BMC XIV API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: bmcxiv-com-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 50.5
    catalog_earned_first_party: 8.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 52.2
    developer_ergonomics: 54.8
    discoverability: 71.7
    operational_transparency: 0.0
  previous_composite: 42.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/bmcxiv-com/bmcxiv-com-2026-10-11T183856.png
security:
- kind: authentication
  name: Bmcxiv Com Authentication
  slug: bmcxiv-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bmcxiv Com Domain Security
  slug: bmcxiv-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: breach402-cyber-expert
  slug: bmcxiv-com-cyber-expert
- name: owner-breach-protection
  slug: bmcxiv-com-owner-breach-protection
- name: breach402-social-engineering-protector
  slug: bmcxiv-com-social-engineering-protector
slug: bmcxiv-com
tags:
- Company
- Security
- Cybersecurity
- Breach Intelligence
- Identity Protection
- Data Breaches
- Agents
- MCP
- A2A
- x402
website: https://bmcxiv.com/
---
