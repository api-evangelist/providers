---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Digital Maker AI API speaks JSON-RPC (Model Context Protocol) at a single endpoint, https://digitalmaker.ai/mcp. Clients authenticate with an API key created in Account Settings (API tab), sent in
  name: Digital Maker AI MCP API
  slug: digital-maker-ai-mcp-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/digitalmaker-ai/rate-limits/digitalmaker-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digitalmaker-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/digitalmaker-ai/plans/digitalmaker-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digitalmaker-ai-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/digitalmaker-ai/cli/digitalmaker-ai-cli.yml
  title: ''
  type: CLI
  url: cli/digitalmaker-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/digitalmaker-ai/conventions/digitalmaker-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digitalmaker-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/digitalmaker-ai/authentication/digitalmaker-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digitalmaker-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/digitalmaker-ai/lifecycle/digitalmaker-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/digitalmaker-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/digitalmaker-ai/errors/digitalmaker-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/digitalmaker-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/digitalmaker-ai/llms/digitalmaker-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digitalmaker-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/digitalmaker-ai/mcp/digitalmaker-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/digitalmaker-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/digitalmaker-ai/well-known/digitalmaker-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digitalmaker-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/digitalmaker-ai/hosts/digitalmaker-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitalmaker-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/digitalmaker-ai/integrations/digitalmaker-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/digitalmaker-ai-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/digitalmaker-ai/vendors/digitalmaker-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digitalmaker-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/digitalmaker-ai/packages/digitalmaker-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/digitalmaker-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/digitalmaker-ai/packages/digitalmaker-ai-packages.yml
  title: ''
  type: Packages
  url: packages/digitalmaker-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/digitalmaker-ai/security/digitalmaker-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitalmaker-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://digitalmaker.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://digitalmaker.ai/agents
- group: company
  title: ''
  type: Blog
  url: https://digitalmaker.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://digitalmaker.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://digitalmaker.ai/contact
- group: operate
  title: ''
  type: FAQ
  url: https://digitalmaker.ai/faq
- group: company
  title: ''
  type: About
  url: https://digitalmaker.ai/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://digitalmaker.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://digitalmaker.ai/privacy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@DigitalMaker-AI
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/digitalmakerai/
created: '2026-11-05'
description: 'Digital Maker AI (digitalmaker.ai) is an AI platform for creating faceless videos and digital products: it turns a single topic into YouTube videos and Shorts, AI avatars, animated podcasts and whiteboard videos with AI scripts, scenes and voiceovers, and generates ebooks, planners, images and websites. It also offers Faceless Finder and Trend Finder research tools, and exposes its tools to AI agents through a remote MCP server (https://digitalmaker.ai/mcp, Bearer key), a local npm stdio package, and Claude, ChatGPT and Gemini connectors. Digital Maker AI is a trading name of Digital Income FZE, registered in the Sharjah Publishing City Free Zone, United Arab Emirates.'
image: https://auth.digitalmaker.ai/storage/v1/object/public/digital-maker-outputs/favicon-256.png
layout: provider
mcp_servers:
- description: Remote MCP server at digitalmaker.ai requiring an API key; 48 tools listed.
  name: Digital Maker AI
  slug: digital-maker-ai
modified: '2026-11-05'
name: Digital Maker AI
nav: Providers
network: true
overview: 'Digital Maker AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video Generation, Faceless Video, and YouTube.


  Digital Maker AI''s developer surface includes CLI, authentication, documentation, engineering blog, pricing, support, FAQ, and 20 more developer resources.'
plans:
- name: Digitalmaker Ai Plans Pricing
  plan_count: 4
  slug: digitalmaker-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Digitalmaker Ai Rate Limits
  slug: digitalmaker-ai-rate-limits
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digitalmaker Ai Authentication
  slug: digitalmaker-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Digitalmaker Ai Domain Security
  slug: digitalmaker-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digitalmaker-ai
tags:
- Company
- Artificial Intelligence
- Video Generation
- Faceless Video
- YouTube
- Content Creation
- Digital Products
- MCP
website: https://digitalmaker.ai/
---
