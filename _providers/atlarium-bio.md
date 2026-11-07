---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
  score: 14.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public read‑only MCP server providing structured aquarium and terrarium data and tools.
  name: Atlarium Habitat Database MCP
  slug: atlarium-habitat-database-mcp
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/atlarium-bio/llms/atlarium-bio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlarium-bio-llms.txt
- group: agent
  href: https://artifacts.apis.io/atlarium-bio/mcp/atlarium-bio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlarium-bio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atlarium-bio/well-known/atlarium-bio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlarium-bio-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlarium-bio/hosts/atlarium-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlarium-bio-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlarium-bio/vendors/atlarium-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlarium-bio-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://atlarium.bio/en/press
- group: auth
  href: https://artifacts.apis.io/atlarium-bio/security/atlarium-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlarium-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlarium.bio/
- group: docs
  title: ''
  type: Documentation
  url: https://atlarium.bio/en/guide
- group: start
  title: ''
  type: GettingStarted
  url: https://atlarium.bio/en/guide
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlarium.bio/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlarium.bio/en/privacy
- group: start
  title: ''
  type: Login
  url: https://atlarium.bio/en/login
created: '2026-11-01'
description: Atlarium is an online atlas for aquariums and terrariums, offering species profiles for fish, plants, amphibians, reptiles, and invertebrates, along with practical guides, tools, and a community for hobbyists. The platform provides a searchable catalog, detailed care parameters, equipment recommendations, and community‑driven content to help enthusiasts create and maintain healthy aquatic and terrarium habitats.
image: https://atlarium.bio/api/img/img-wm-v11/thumbnail-w128-q70.webp?src=%2Fimages%2Fbrand%2Fatlarium-logo-horizontal-v3.png&v=img-wm-v11&w=128&q=70&f=webp&p=thumbnail
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.atlarium.bio.
  name: Atlarium MCP Server
  slug: atlarium-bio-mcp-yml
modified: '2026-11-02'
name: Atlarium
nav: Providers
network: true
overview: 'Atlarium is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Aquariums, Terrariums, Species, Guides, and Community.


  Atlarium''s developer surface includes documentation, getting-started guide, and 11 more developer resources.'
random_paper: 22
scopes:
- name: Atlarium Bio Scopes
  scope_count: 0
  slug: atlarium-bio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 65.8
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlarium Bio Authentication
  slug: atlarium-bio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atlarium Bio Domain Security
  slug: atlarium-bio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: atlarium-bio
tags:
- Aquariums
- Terrariums
- Species
- Guides
- Community
website: https://atlarium.bio/
---
