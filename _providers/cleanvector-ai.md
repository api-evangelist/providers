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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/cleanvector-ai/plans/cleanvector-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cleanvector-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cleanvector-ai/llms/cleanvector-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleanvector-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/cleanvector-ai/mcp/cleanvector-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cleanvector-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/cleanvector-ai/hosts/cleanvector-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleanvector-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cleanvector-ai/vendors/cleanvector-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleanvector-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleanvector.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleanvector.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cleanvector.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://cleanvector.ai/login
- group: company
  title: ''
  type: Blog
  url: https://cleanvector.ai/blog
- group: auth
  href: https://artifacts.apis.io/cleanvector-ai/security/cleanvector-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleanvector-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleanvector.ai/
coverage:
  checked: '2026-11-04'
  detail: Pricing page is HTML with tool listings but no machine-readable API spec.
  evidence:
  - status: 200
    url: https://cleanvector.ai/pricing
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: 'cleanvector-ai is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://cleanvector.ai/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at cleanvector.ai requiring an API key.
  name: CleanVector MCP Server
  slug: cleanvector-ai-mcp-yml
modified: '2026-11-03'
name: CleanVector
nav: Providers
network: true
overview: 'CleanVector is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI vector generator, SVG editor, logo generator, mascot generator, and Image Conversion.


  CleanVector''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Cleanvector Ai Plans Pricing
  plan_count: 4
  slug: cleanvector-ai-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 40.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleanvector Ai Domain Security
  slug: cleanvector-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cleanvector-ai
tags:
- AI vector generator
- SVG editor
- logo generator
- mascot generator
- Image Conversion
- Design Tools
website: https://cleanvector.ai/
---
