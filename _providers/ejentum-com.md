---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Deterministic Reasoning-Augmented Retrieval (RAR) Hybrid Semantic Retrieval & Graph-Composed Cognitive Engine
  name: Ejentum Logic API
  slug: ejentum-logic-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/ejentum-com/plans/ejentum-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ejentum-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/ejentum-com/authentication/ejentum-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ejentum-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ejentum-com/conformance/ejentum-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ejentum-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ejentum-com/llms/ejentum-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ejentum-com-llms.txt
- group: build
  href: https://artifacts.apis.io/ejentum-com/mcp/ejentum-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ejentum-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ejentum-com/mcp/ejentum-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ejentum-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/ejentum-com/hosts/ejentum-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ejentum-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ejentum-com/vendors/ejentum-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ejentum-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://ejentum.com/playground
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.ejentum.com</code
- group: auth
  href: https://artifacts.apis.io/ejentum-com/security/ejentum-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ejentum-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ejentum.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ejentum.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://ejentum.com/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://ejentum.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ejentum.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ejentum.com/privacy
created: '2026-10-30'
description: Ejentum provides a reasoning harness for agentic AI, offering sub‑2ms verification checklists to keep autonomous AI workflows grounded in truth. It prevents drift and costly errors by delivering focused verification before actions, cutting token costs by 60‑85% and ensuring zero data retention. Free tier includes 1,000 calls and a 30‑day evaluation, with SDKs and REST access.
image: https://ejentum.com/og-preview.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.ejentum.com.
  name: ejentum-com MCP Server
  slug: ejentum-com-mcp-yml
modified: '2026-10-30'
name: ejentum-com
nav: Providers
network: true
overview: 'ejentum-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Reasoning, AI Agents, and Verification.


  ejentum-com''s developer surface includes authentication, sandbox, documentation, getting-started guide, pricing, and 12 more developer resources.'
plans:
- name: Ejentum Com Plans Pricing
  plan_count: 3
  slug: ejentum-com-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.8
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ejentum-com/ejentum-com-2026-11-03T131339.png
security:
- kind: authentication
  name: Ejentum Com Authentication
  slug: ejentum-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ejentum Com Domain Security
  slug: ejentum-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: ejentum-com
tags:
- Company
- Artificial Intelligence
- Reasoning
- AI Agents
- Verification
- Platform
website: https://ejentum.com/
---
