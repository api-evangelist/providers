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
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/designare-at/well-known/designare-at-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/designare-at-well-known.yml
- group: agent
  href: https://artifacts.apis.io/designare-at/llms/designare-at-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/designare-at-llms.txt
- group: agent
  href: https://artifacts.apis.io/designare-at/mcp/designare-at-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/designare-at-mcp.yml
- group: other
  href: https://artifacts.apis.io/designare-at/hosts/designare-at-hosts.yml
  title: ''
  type: Hosts
  url: hosts/designare-at-hosts.yml
- group: other
  href: https://artifacts.apis.io/designare-at/vendors/designare-at-vendors.yml
  title: ''
  type: Vendors
  url: vendors/designare-at-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/michael-kanda
- group: company
  title: ''
  type: Blog
  url: https://designare.at/blog
- group: auth
  href: https://artifacts.apis.io/designare-at/security/designare-at-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/designare-at-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://designare.at/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite probing known API endpoints.
  evidence:
  - status: 404
    url: https://designare.at/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Designare.at appears to be a personal portfolio site for Michael Kanda, focusing on web and AI projects. The site includes a brief introduction, links to projects, and contact information. While the domain suggests a company, the content does not provide clear corporate information, services, or an API offering. Further investigation is needed to determine if a formal company exists behind this domain.
image: https://designare.at/images/michael-kanda.webp
layout: provider
mcp_servers:
- description: Remote MCP server at designare.at.
  name: designare-at MCP Server
  slug: designare-at-mcp-yml
modified: '2026-11-05'
name: designare-at
nav: Providers
network: true
overview: 'designare-at is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Web, and Artificial Intelligence.


  designare-at''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.0
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Designare At Domain Security
  slug: designare-at-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: designare-at
tags:
- Company
- Technology
- Web
- Artificial Intelligence
website: https://designare.at/
---
