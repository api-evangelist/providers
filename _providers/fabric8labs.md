---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fabric8Labs Agentic Access
  operation_count: 19
  slug: fabric8labs-agentic-access
  summary_line: 19 operations
api_count: 2
apis:
- description: A Model Context Protocol server endpoint registered on www.fabric8labs.com under the WordPress REST "mcp" namespace and served at /wp-json/mcp/mcp-oauth-server (with a sibling /wp-json/mcp/mcp-adapter
  name: Fabric8Labs MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: 'The public WordPress REST API (wp-json) of the Fabric8Labs website at www.fabric8labs.com: the route index of the site''s content management system, catalogued as one site surface rather than as separa'
  name: Fabric8Labs Website (WordPress REST)
  slug: fabric8labs-com-website-wordpress-rest
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/fabric8labs/agentic-access/fabric8labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fabric8labs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fabric8labs/security/fabric8labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fabric8labs-domain-security.yml
- group: docs
  href: https://artifacts.apis.io/fabric8labs/openapi/
  title: ''
  type: OpenAPI
  url: openapi/
- group: agent
  href: https://artifacts.apis.io/fabric8labs/llms/fabric8labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fabric8labs-llms.txt
- group: agent
  href: https://artifacts.apis.io/fabric8labs/well-known/fabric8labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fabric8labs-well-known.yml
- group: auth
  href: https://artifacts.apis.io/fabric8labs/authentication/fabric8labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fabric8labs-authentication.yml
- group: auth
  href: https://artifacts.apis.io/fabric8labs/scopes/fabric8labs-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fabric8labs-scopes.yml
- group: design
  href: https://artifacts.apis.io/fabric8labs/conventions/fabric8labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fabric8labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/fabric8labs/conformance/fabric8labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fabric8labs-conformance.yml
- group: design
  href: https://artifacts.apis.io/fabric8labs/lifecycle/fabric8labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fabric8labs-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fabric8labs/data-model/fabric8labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fabric8labs-data-model.yml
- group: design
  href: https://artifacts.apis.io/fabric8labs/errors/fabric8labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fabric8labs-problem-types.yml
- group: build
  href: https://artifacts.apis.io/fabric8labs/examples/fabric8labs-examples.yml
  title: ''
  type: Examples
  url: examples/fabric8labs-examples.yml
- group: build
  href: https://artifacts.apis.io/fabric8labs/packages/fabric8labs-packages.yml
  title: ''
  type: Packages
  url: packages/fabric8labs-packages.yml
- group: commercial
  href: https://artifacts.apis.io/fabric8labs/plans/fabric8labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fabric8labs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fabric8labs/rate-limits/fabric8labs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fabric8labs-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/fabric8labs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.fabric8labs.com/
- group: company
  title: ''
  type: About
  url: https://www.fabric8labs.com/about/
- group: other
  title: ''
  type: Technology
  url: https://www.fabric8labs.com/technology/
- group: other
  title: ''
  type: Manufacturing
  url: https://www.fabric8labs.com/manufacturing/
- group: other
  title: ''
  type: Markets
  url: https://www.fabric8labs.com/markets/
- group: other
  title: ''
  type: Industries
  url: https://www.fabric8labs.com/industries/
- group: company
  title: ''
  type: Blog
  url: https://www.fabric8labs.com/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fabric8labs.com/feed/
- group: company
  title: ''
  type: Press
  url: https://www.fabric8labs.com/press/
- group: other
  title: ''
  type: Events
  url: https://www.fabric8labs.com/events/
- group: operate
  title: ''
  type: Support
  url: https://www.fabric8labs.com/contact-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.fabric8labs.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fabric8labs.com/privacy-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://www.fabric8labs.com/web-accessibility/
- group: other
  title: ''
  type: SiteMap
  url: https://www.fabric8labs.com/site-map/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fabric8Labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fabric8labs
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/fabric8labs_stock/
created: '2026-08-12'
description: Fabric8Labs is a San Diego, California based advanced-manufacturing company founded in 2015 that invented and commercialized Electrochemical Additive Manufacturing (ECAM), a room-temperature metal 3D printing process that uses a patented microelectrode array printhead to electroplate copper ions out of a water-based metal-salt solution pixel by pixel. Unlike powder-bed and laser metal additive methods, ECAM needs no high-temperature step, no expensive metal powder feedstock and effectively no post-processing, prints at micron-scale resolution directly onto temperature-sensitive substrates, and the company reports more than a 90% reduction in greenhouse gas emissions against alternative additive and traditional manufacturing routes. Fabric8Labs operates as both a technology developer and a production foundry, manufacturing high-precision components for data-center liquid cooling and AI/HPC thermal management (cold plates, single-phase, two-phase and immersion cooling), RF and
  wireless communications, satellite and aerospace systems, power electronics, photonics cooling, semiconductors, medical devices and luxury goods. It has raised funding from Intel Capital, TDK Ventures and others, including a $50M round announced in November 2025 to expand United States manufacturing capacity toward tens of millions of components annually, and on 10 June 2026 announced it will be acquired by TDK Corporation — the company continues under existing leadership, with ECAM folded into TDK's global manufacturing network. Fabric8Labs publishes no product, customer or developer API and runs no developer program; the only machine-readable surface on fabric8labs.com is the public WordPress REST API (namespace wp/v2) that serves the company newsroom, site pages, leadership team directory, taxonomy and media library as JSON, alongside a WordPress MCP Adapter endpoint and RFC 8414/RFC 9728 OAuth discovery documents that are served but authentication-gated.
image: https://www.fabric8labs.com/wp-content/uploads/2024/06/logo-background.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.fabric8labs.com over HTTP.
  name: Fabric8Labs MCP Server
  slug: fabric8labs
modified: '2026-08-12'
name: Fabric8Labs
nav: Providers
network: true
overview: 'Fabric8Labs is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advanced Manufacturing, 3D Printing, Metal 3D Printing, and Electrochemical Additive Manufacturing.


  Fabric8Labs'' developer surface includes authentication, code examples, engineering blog, support, and 31 more developer resources.'
plans:
- name: Fabric8Labs Plans Pricing
  plan_count: 0
  slug: fabric8labs-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Fabric8Labs Rate Limits
  slug: fabric8labs-rate-limits
scopes:
- name: Fabric8Labs Scopes
  scope_count: 1
  slug: fabric8labs-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 61.7
    operational_transparency: 2.6
  previous_composite: 19.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 31.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fabric8labs/fabric8labs-2026-09-02T145452.png
security:
- kind: authentication
  name: Fabric8Labs Authentication
  slug: fabric8labs-authentication
  summary_line: none/oauth2 · 3 schemes
- kind: domain-security
  name: Fabric8Labs Domain Security
  slug: fabric8labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Read the Fabric8Labs newsroom
  slug: fabric8labs-read-newsroom
- name: Search and inventory all Fabric8Labs public content
  slug: fabric8labs-search-and-inventory-content
slug: fabric8labs
tags:
- Company
- Advanced Manufacturing
- 3D Printing
- Metal 3D Printing
- Electrochemical Additive Manufacturing
- Thermal Management
- Liquid Cooling
- Data Center
- Semiconductors
- Electronics
- Aerospace
- Photonics
- Power Electronics
- Hardware
- Content
website: https://www.fabric8labs.com/
---
