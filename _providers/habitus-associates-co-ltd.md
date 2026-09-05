---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/habitus-associates-co-ltd-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/habitus-associates-co-ltd-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/habitus-associates-co-ltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artue.io
created: '2026-07-17'
description: 'Habitus Associates Co., Ltd. is the company behind Artue (artue.io), an AI-powered online marketplace for original artworks by Korean and international artists. Artue lets collectors discover, purchase, and resell paintings, photography, sculptures, and prints, with natural-language search that finds works by mood, color, style, room type, or budget. The platform is explicitly agent-native: it publishes an llms.txt and ships a hosted Model Context Protocol (MCP) server so AI assistants such as Claude and ChatGPT can search its collection directly. Backed by 500 Global and surfaced into the API Evangelist network from that portfolio.'
image: https://artue.io/favicon/favicon-96x96.png
layout: provider
mcp_servers:
- description: ''
  name: Artue MCP server (search_artworks)
  slug: artue-mcp-server-search-artworks
modified: '2026-07-19'
name: Habitus Associates Co., Ltd.
nav: Providers
network: true
overview: Habitus Associates Co., Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Art, Marketplace, E-Commerce, and Artificial Intelligence.
random_paper: 14
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/habitus-associates-co-ltd/refs/heads/main/screenshots/habitus-associates-co-ltd-2026-07-25T220515.png
security:
- kind: domain-security
  name: Habitus Associates Co Ltd Domain Security
  slug: habitus-associates-co-ltd-domain-security
  summary_line: TLSv1.3
slug: habitus-associates-co-ltd
tags:
- Company
- Art
- Marketplace
- E-Commerce
- Artificial Intelligence
- MCP
- Korea
- Discovery
website: https://artue.io
---
