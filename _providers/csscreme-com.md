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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for CSS Crème platform offering theme extraction and design assistance.
  name: CSS Crème API
  slug: css-cr-me-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/csscreme-com/mcp/csscreme-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/csscreme-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/csscreme-com/well-known/csscreme-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/csscreme-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/csscreme-com/hosts/csscreme-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/csscreme-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/csscreme-com/vendors/csscreme-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/csscreme-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/csscreme-com/security/csscreme-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/csscreme-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://csscreme.com/
- group: docs
  title: ''
  type: APIReference
  url: https://csscreme.com/ai
- group: start
  title: ''
  type: GettingStarted
  url: https://csscreme.com/ai
- group: operate
  title: ''
  type: Support
  url: https://csscreme.com/ai
- group: company
  title: ''
  type: Blog
  url: https://csscreme.com/blog
- group: agent
  title: ''
  type: llms.txt
  url: https://csscreme.com/llms.txt
coverage:
  checked: '2026-11-04'
  detail: API documentation page https://csscreme.com/api returns a JavaScript challenge page, preventing machine‑readable spec retrieval.
  evidence:
  - status: 429
    url: https://csscreme.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: CSS Crème is a platform that discovers, decodes, and helps build exceptional web design. It offers tools to extract themes from live sites, generate design systems, and provides AI‑assisted design assistance. Users can decode pages, extract CSS tokens, spacing, radii, and create installable design files. The service includes a free AI MCP server, design guidelines, UI pattern libraries, and open‑source icon and emoji packs, aiming to make modern, safe, and consistent web design accessible to developers and designers alike.
image: https://csscreme.com/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at csscreme.com.
  name: CSS Crème MCP Server
  slug: csscreme-com-mcp-yml
modified: '2026-11-04'
name: CSS Crème
nav: Providers
network: true
overview: 'CSS Crème is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Design, Artificial Intelligence, CSS, and Tools.


  CSS Crème''s developer surface includes API reference, getting-started guide, support, engineering blog, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 56.7
    operational_transparency: 0.0
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
  name: Csscreme Com Domain Security
  slug: csscreme-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: csscreme-com
tags:
- Company
- Design
- Artificial Intelligence
- CSS
- Tools
- Open Source
website: https://csscreme.com/
---
