---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-09-12'
api_count: 2
apis:
- description: The agent-facing commerce surface for Cosmos Store, Agnikul's branded merchandise shop, implementing the Universal Commerce Protocol (dev.ucp.shopping) over MCP. Thirteen tools cover catalog search an
  name: Agnikul Cosmos Store Commerce MCP API
  slug: agnikul-cosmos-store-commerce-mcp-api
- description: The read-only storefront JSON endpoints Cosmos Store documents for agents in its own /agents.md and /llms.txt — product JSON at /products/{handle}.json, collection product listings at /collections/{ha
  name: Agnikul Cosmos Store Storefront JSON API
  slug: agnikul-cosmos-store-storefront-json-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://agnikul.in/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.agnikul.in/agents.md
- group: company
  title: ''
  type: Blog
  url: https://agnikul.in/media/
- group: operate
  title: ''
  type: Support
  url: https://agnikul.in/contact-us/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agnikul-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/agnikul-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agnikul-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agnikul-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agnikul-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agnikul-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agnikul-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/agnikul-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agnikul-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agnikul-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agnikul-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agnikul-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agnikul-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agnikul-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/agnikul-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agnikul-domain-security.yml
created: '2026-09-12'
description: 'Agnikul Cosmos Private Limited is an Indian aerospace manufacturer and commercial launch service provider founded in 2017 and incubated at the National Centre for Combustion Research and Development at IIT Madras, Chennai. It builds Agnibaan, a configurable small-lift orbital launch vehicle powered by Agnilet — a single-piece, fully 3D-printed semi-cryogenic rocket engine — and flies it from Dhanush (ALP-01), India''s first privately built launchpad, at Satish Dhawan Space Centre. On 30 May 2024 its Agnibaan SOrTeD suborbital demonstrator became the first vehicle to fly from a privately built launchpad in India. Agnikul publishes NO API for its launch business: launch is sold per kilogram through an HTML enquiry form, with no developer portal, no OpenAPI and no mission or manifest API anywhere. What it does publish is a genuine, hand-authored corporate /llms.txt and /llms-full.txt about the launch programme, and — on its Cosmos Store merchandise storefront at shop.agnikul.in
  — a live, anonymous agent-commerce surface: a /.well-known/ucp merchant profile implementing the Universal Commerce Protocol 2026-08-25 and two Model Context Protocol endpoints offering fourteen catalog, cart, checkout, order and policy tools.'
image: https://agnikul.in/wp-content/uploads/2024/06/Agnikul-Logo.png
layout: provider
mcp_servers:
- description: ''
  name: Agnikul Cosmos Store Model Context Protocol servers
  slug: agnikul-cosmos-store-model-context-protocol-servers
modified: '2026-09-12'
name: Agnikul Cosmos
nav: Providers
network: true
overview: 'Agnikul Cosmos publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Space, Launch Services, and Satellites.


  Agnikul Cosmos'' developer surface includes documentation, engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Agnikul Plans Pricing
  plan_count: 0
  slug: agnikul-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Agnikul Rate Limits
  slug: agnikul-rate-limits
scopes:
- name: Agnikul Scopes
  scope_count: 0
  slug: agnikul-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agnikul Authentication
  slug: agnikul-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Agnikul Domain Security
  slug: agnikul-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agnikul
tags:
- Company
- Aerospace
- Space
- Launch Services
- Satellites
- Manufacturing
- Additive Manufacturing
- India
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Shopify
website: https://agnikul.in/
---
