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
  href: https://artifacts.apis.io/asrm-ai/plans/asrm-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asrm-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/asrm-ai/llms/asrm-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asrm-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/asrm-ai/mcp/asrm-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asrm-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/asrm-ai/hosts/asrm-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asrm-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/asrm-ai/vendors/asrm-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asrm-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/asrm-ai/security/asrm-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asrm-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asrm.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://asrm.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://asrm.ai/signup
- group: start
  title: ''
  type: Login
  url: https://asrm.ai/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asrm.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asrm.ai/terms
coverage:
  checked: '2026-11-02'
  detail: MCP tools/list endpoint requires authentication, returning HTTP 406.
  evidence:
  - status: 406
    url: https://asrm.ai/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: ASRM (AI Search Rank Monitor) provides AI visibility monitoring, allowing brands to track how often AI engines mention, cite, and recommend them. The service offers free scoring, tiered subscription plans (Solo $39/mo, Agency $149/mo, Agency Pro $349/mo), and a dashboard to improve AI search presence.
image: https://asrm.ai/opengraph-image.png?opengraph-image.2dn3-6vdwc3r_.png
layout: provider
mcp_servers:
- description: Remote MCP server at asrm.ai.
  name: ASRM MCP Server
  slug: asrm-ai-mcp-yml
modified: '2026-11-02'
name: ASRM
nav: Providers
network: true
overview: 'ASRM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, SEO, Monitoring, Visibility, and Search.


  ASRM''s developer surface includes pricing, signup flow, and 10 more developer resources.'
plans:
- name: Asrm Ai Plans Pricing
  plan_count: 1
  slug: asrm-ai-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 17.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asrm Ai Domain Security
  slug: asrm-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: asrm-ai
tags:
- Artificial Intelligence
- SEO
- Monitoring
- Visibility
- Search
website: https://asrm.ai/
---
