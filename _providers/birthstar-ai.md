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
  score: 9.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/birthstar-ai/llms/birthstar-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/birthstar-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/birthstar-ai/mcp/birthstar-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/birthstar-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/birthstar-ai/well-known/birthstar-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/birthstar-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/birthstar-ai/hosts/birthstar-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/birthstar-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/birthstar-ai/vendors/birthstar-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/birthstar-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.birthstar.ai/privacy
- group: auth
  href: https://artifacts.apis.io/birthstar-ai/security/birthstar-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/birthstar-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://birthstar.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.birthstar.ai/
- group: operate
  title: ''
  type: Support
  url: https://wa.me/918546948448
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/birthstar.ai/
coverage:
  checked: '2026-11-02'
  detail: Provider documentation at https://mcp.birthstar.ai/ contains no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://mcp.birthstar.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Birthstar provides Vedic astrology services via WhatsApp, allowing users to obtain their birth chart and receive personalized readings on career, marriage, finance, and timing. The platform emphasizes computed, not guessed, analyses and offers readings starting at ₹499. It aims to make traditional astrology accessible through modern messaging.
image: https://birthstar.ai/assets/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.birthstar.ai.
  name: Birthstar MCP Server
  slug: birthstar-ai-mcp-yml
modified: '2026-11-02'
name: Birthstar
nav: Providers
network: true
overview: 'Birthstar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Astrology, Vedic, WhatsApp, BirthChart, and Personal Readings.


  Birthstar''s developer surface includes support and 10 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Birthstar Ai Domain Security
  slug: birthstar-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: birthstar-ai
tags:
- Astrology
- Vedic
- WhatsApp
- BirthChart
- Personal Readings
- Company
website: https://birthstar.ai/
---
