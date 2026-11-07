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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://www.avocadoai.co/api/v1
  baseurl_source: declared
  description: 'HTTP endpoints behind the Avocado MCP server and CLI: MCP, OAuth discovery, API keys and generation. Not a public developer API.'
  name: Avocado AI API
  slug: avocado-ai-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/avocadoai-co/rate-limits/avocadoai-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avocadoai-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/avocadoai-co/plans/avocadoai-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avocadoai-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/avocadoai-co/vocabulary/avocadoai-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avocadoai-co-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/avocadoai-co/cli/avocadoai-co-cli.yml
  title: ''
  type: CLI
  url: cli/avocadoai-co-cli.yml
- group: auth
  href: https://artifacts.apis.io/avocadoai-co/authentication/avocadoai-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avocadoai-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/avocadoai-co/conformance/avocadoai-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avocadoai-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avocadoai-co/llms/avocadoai-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avocadoai-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/avocadoai-co/mcp/avocadoai-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avocadoai-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/avocadoai-co/well-known/avocadoai-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avocadoai-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/avocadoai-co/hosts/avocadoai-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avocadoai-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/avocadoai-co/vendors/avocadoai-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avocadoai-co-vendors.yml
- group: build
  href: https://artifacts.apis.io/avocadoai-co/packages/avocadoai-co-packages.yml
  title: ''
  type: SDKs
  url: packages/avocadoai-co-packages.yml
- group: build
  href: https://artifacts.apis.io/avocadoai-co/packages/avocadoai-co-packages.yml
  title: ''
  type: Packages
  url: packages/avocadoai-co-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.avocadoai.co/press
- group: start
  title: ''
  type: Login
  url: https://www.avocadoai.co/login
- group: auth
  href: https://artifacts.apis.io/avocadoai-co/security/avocadoai-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avocadoai-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avocadoai.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.avocadoai.co/knowledge-base
- group: commercial
  title: ''
  type: Pricing
  url: https://www.avocadoai.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avocadoai.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avocadoai.co/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.avocadoai.co/contact
- group: company
  title: ''
  type: Blog
  url: https://www.avocadoai.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.avocadoai.co/knowledge-base/getting-started-with-super-agent
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://avocadoai.co/openapi.json
  - status: null
    url: https://www.avocadoai.co/openapi.json
  - status: 401
    url: https://www.avocadoai.co/mcp
  - status: 200
    url: https://avocadoai.co/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Avocado AI is a creative AI workspace for ecommerce brands, especially wellness, skincare, protein, supplements, and other DTC categories, that helps teams ship on‑brand product ads without a creative bottleneck. Studio is where you make images, videos, UGC and audio yourself. Flows and Director mode chain prompt, image, video, music, and voice nodes into repeatable campaigns and full commercials on an infinite canvas. Super Agent turns a product photo or one‑line brief into statics, videos, and UGC ads, then drafts captions and can schedule and publish approved posts. Models include GPT Image 2.5, Nano Banana 2, Seedance 2.5, Kling 3.0, Veo 3.1, and Fish Audio S2 Pro for voiceovers. Generations include full commercial rights, and you can connect your own agent, such as Claude, Codex or Cursor, through the Avocado MCP server or CLI.
image: https://www.avocadoai.co/_next/image?url=%2Fbrand%2Favocado%2Flogo%2Favocado-logo-light.png&w=1200&q=75
layout: provider
mcp_servers:
- description: Remote MCP server at www.avocadoai.co.
  name: Avocado AI MCP Server
  slug: avocadoai-co-mcp-yml
modified: '2026-11-02'
name: Avocado AI
nav: Providers
network: true
overview: 'Avocado AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Creative, E-Commerce, Image Generation, and Video Generation.


  Avocado AI''s developer surface includes CLI, authentication, documentation, pricing, support, engineering blog, getting-started guide, and 17 more developer resources.'
plans:
- name: Avocadoai Co Plans Pricing
  plan_count: 5
  slug: avocadoai-co-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Avocadoai Co Rate Limits
  slug: avocadoai-co-rate-limits
scopes:
- name: Avocadoai Co Scopes
  scope_count: 0
  slug: avocadoai-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 58.3
    catalog_earned_first_party: 20.0
    catalog_gap: 56.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 40.5
    discoverability: 65.8
    operational_transparency: 21.1
  previous_composite: 48.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avocadoai Co Authentication
  slug: avocadoai-co-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Avocadoai Co Domain Security
  slug: avocadoai-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avocadoai-co
tags:
- Artificial Intelligence
- Creative
- E-Commerce
- Image Generation
- Video Generation
website: https://www.avocadoai.co/
---
