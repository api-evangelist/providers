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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP server for AI agents to render animations, videos, and add audio/captions via JSON-RPC.
  name: Animation Machine MCP
  slug: animation-machine-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/animation-machine-com/llms/animation-machine-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/animation-machine-com-llms.txt
- group: build
  href: https://artifacts.apis.io/animation-machine-com/mcp/animation-machine-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/animation-machine-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/animation-machine-com/mcp/animation-machine-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/animation-machine-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/animation-machine-com/well-known/animation-machine-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/animation-machine-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/animation-machine-com/hosts/animation-machine-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animation-machine-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/animation-machine-com/vendors/animation-machine-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animation-machine-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/animation-machine-com/security/animation-machine-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animation-machine-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://animation-machine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://animation-machine.com/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://animation-machine.com/install.md
- group: commercial
  title: ''
  type: Pricing
  url: https://animation-machine.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://animation-machine.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://animation-machine.com/privacy
coverage:
  checked: '2026-11-01'
  detail: Public documentation exists but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://animation-machine.com/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Cash Flow Crescendo Inc. operates Animation Machine, a web‑based service that converts HTML‑based animations and video files into polished MP4 or GIF outputs. It offers AI‑generated captions in 16 languages, AI voice‑over with 14 natural voices, a library of 500 000 royalty‑free tracks, 4K rendering, batch processing, and one‑click vertical Shorts creation. The platform runs entirely in the cloud, requires no installation, and provides a $5 per month flat‑rate subscription with unlimited renders and no per‑render fees. Users can upload HTML, Lottie, GSAP, CSS, Three.js, or existing video files, add music, captions, voice‑over, and branding, then download the final video. The service also includes an MCP server for AI agents such as Claude, ChatGPT, and Cursor.
image: https://animation-machine.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at animation-machine.com.
  name: Cash Flow Crescendo Inc. MCP Server
  slug: animation-machine-com-mcp-yml
modified: '2026-11-01'
name: Cash Flow Crescendo Inc.
nav: Providers
network: true
overview: 'Cash Flow Crescendo Inc. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Animation, Video, Artificial Intelligence, Conversion, and Software-as-a-Service.


  Cash Flow Crescendo Inc.''s developer surface includes documentation, getting-started guide, pricing, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 17.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Animation Machine Com Domain Security
  slug: animation-machine-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: animation-machine-com
tags:
- Animation
- Video
- Artificial Intelligence
- Conversion
- Software-as-a-Service
- Multimedia
website: https://animation-machine.com/
---
