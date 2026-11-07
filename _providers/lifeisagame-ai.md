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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/lifeisagame-ai/llms/lifeisagame-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lifeisagame-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/lifeisagame-ai/mcp/lifeisagame-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lifeisagame-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lifeisagame-ai/well-known/lifeisagame-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lifeisagame-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/lifeisagame-ai/hosts/lifeisagame-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lifeisagame-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/lifeisagame-ai/vendors/lifeisagame-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lifeisagame-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lifeisagame-ai/security/lifeisagame-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lifeisagame-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lifeisagame.ai/
- group: company
  title: ''
  type: Blog
  url: https://lifeisagame.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lifeisagame.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lifeisagame.ai/privacy-policy
coverage:
  checked: '2026-10-30'
  detail: Life is a Game provides mental health tools and does not offer a developer API.
  evidence:
  - status: 200
    url: https://lifeisagame.ai/
  reason: not-a-software-company
  state: none
created: '2026-10-30'
description: 'Life is a Game: Mental Health Tools, One Per Struggle. A studio building small, focused mental health apps for fear, focus, habits and obsessive thoughts. Each one breaks the problem into steps you can actually take.'
image: https://lifeisagame.ai/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.lifeisagame.ai requiring OAuth.
  name: lifeisagame-ai MCP Server
  slug: lifeisagame-ai-mcp-yml
modified: '2026-10-30'
name: lifeisagame-ai
nav: Providers
network: true
overview: 'lifeisagame-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Artificial Intelligence, Wellness, and Technology.


  lifeisagame-ai''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 58.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lifeisagame-ai/lifeisagame-ai-2026-11-03T134938.png
security:
- kind: domain-security
  name: Lifeisagame Ai Domain Security
  slug: lifeisagame-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lifeisagame-ai
tags:
- Company
- Mental Health
- Artificial Intelligence
- Wellness
- Technology
website: https://lifeisagame.ai/
---
