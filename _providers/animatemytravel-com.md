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
    agent_skills: unknown
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP server for AnimateMyTravel Studio enabling animated map video creation via streamable HTTP, no authentication.
  name: AnimateMyTravel Studio MCP
  slug: animatemytravel-studio-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/animatemytravel-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/animatemytravel-com/llms/animatemytravel-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/animatemytravel-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/animatemytravel-com/mcp/animatemytravel-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/animatemytravel-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/animatemytravel-com/hosts/animatemytravel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animatemytravel-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/animatemytravel-com/vendors/animatemytravel-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animatemytravel-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/animatemytravel-com/security/animatemytravel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animatemytravel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://animatemytravel.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.animatemytravel.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.animatemytravel.com/en/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.animatemytravel.com/en/create
- group: operate
  title: ''
  type: Support
  url: https://www.animatemytravel.com/en#faq
- group: docs
  title: ''
  type: Documentation
  url: https://www.animatemytravel.com/en
created: '2026-11-01'
description: AnimateMyTravel is a free web‑based tool that lets users create animated travel route videos and map visualizations directly in the browser. Leveraging AI assistants such as ChatGPT, Claude or Gemini, users can describe a trip, a historical campaign, a wildfire or any dataset and the service builds a customizable map animation that can be edited, exported to MP4 or WebM up to 4K, and shared without requiring an account or watermark. The platform offers quick‑route creation, AI‑driven suggestions, and a library of example guides covering history, nature, travel and data‑driven stories. It is operated by the AnimateMyTravel team and is hosted at animatemytravel.com.
image: https://www.animatemytravel.com/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at www.animatemytravel.com.
  name: AnimateMyTravel MCP Server
  slug: animatemytravel-com-mcp-yml
modified: '2026-11-01'
name: AnimateMyTravel
nav: Providers
network: true
overview: 'AnimateMyTravel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Animation, Artificial Intelligence, Video, and Mapping.


  AnimateMyTravel''s developer surface includes getting-started guide, support, documentation, and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.5
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 16.9
  provenance:
    mcp: first-party
    skills: unknown
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
  name: Animatemytravel Com Domain Security
  slug: animatemytravel-com-domain-security
  summary_line: TLSv1.3
slug: animatemytravel-com
tags:
- Travel
- Animation
- Artificial Intelligence
- Video
- Mapping
website: https://animatemytravel.com/
---
