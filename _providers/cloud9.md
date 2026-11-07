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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
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
  score: 20.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'The public WordPress REST API (wp-json) of the Cloud9 website at cloud9.gg: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Cloud9 Website (WordPress REST)
  slug: cloud9-gg-website-wordpress-rest
- description: A remote Model Context Protocol server published on cloud9.gg and advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. It is the WordPress MCP adap
  name: Cloud9 MCP Server
  slug: mcp-server
- description: The official Cloud9 merchandise store at store.cloud9.gg is a Shopify storefront, and Shopify serves its standard anonymous product and collection JSON endpoints on it — /products.json returns the liv
  name: Cloud9 Store JSON Endpoints
  slug: store-json
artifact_total: 10
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://cloud9.gg/feed/
- group: auth
  href: https://artifacts.apis.io/cloud9/security/cloud9-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloud9-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloud9.gg/
- group: company
  title: ''
  type: Blog
  url: https://cloud9.gg/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloud9esports
- group: operate
  title: ''
  type: Support
  url: https://cloud9.gg/contact/
- group: operate
  title: ''
  type: Community
  url: https://discordapp.com/invite/cloud9
- group: start
  title: ''
  type: SignUp
  url: https://club9.cloud9.gg/explore?callbackUrl=/explore&login=open
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud9.gg/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud9.gg/privacy-policy/
- group: company
  title: ''
  type: About
  url: https://cloud9.gg/about/
- group: company
  title: ''
  type: Careers
  url: https://cloud9.gg/careers/
- group: other
  title: ''
  type: BrandAssets
  url: https://cloud9.gg/brand-assets/
- group: other
  title: ''
  type: Shop
  url: https://store.cloud9.gg/
- group: agent
  href: https://artifacts.apis.io/cloud9/well-known/cloud9-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloud9-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cloud9/authentication/cloud9-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloud9-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cloud9/scopes/cloud9-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloud9-scopes.yml
- group: agent
  href: https://artifacts.apis.io/cloud9/mcp/cloud9-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloud9-mcp.yml
- group: build
  href: https://artifacts.apis.io/cloud9/mcp/cloud9-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cloud9-tool-crosswalk.yml
- group: docs
  href: https://artifacts.apis.io/cloud9/json-schema/cloud9-wp-rest-schemas.json
  title: ''
  type: JSONSchema
  url: json-schema/cloud9-wp-rest-schemas.json
- group: design
  href: https://artifacts.apis.io/cloud9/data-model/cloud9-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloud9-data-model.yml
- group: design
  href: https://artifacts.apis.io/cloud9/conventions/cloud9-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloud9-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloud9/conformance/cloud9-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloud9-conformance.yml
- group: design
  href: https://artifacts.apis.io/cloud9/errors/cloud9-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloud9-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloud9/lifecycle/cloud9-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloud9-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/cloud9/llms/cloud9-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloud9-llms.txt
- group: agent
  href: https://artifacts.apis.io/cloud9/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cloud9_stock/
- group: agent
  href: https://artifacts.apis.io/cloud9/skills/cloud9-read-roster-and-news.md
  title: ''
  type: AgentSkill
  url: skills/cloud9-read-roster-and-news.md
created: '2026-08-09'
description: 'Cloud9 Esports, Inc. is a North American professional esports organization founded in 2013 by Jack and Paullie Etienne and headquartered in Santa Monica, California. It fields competitive rosters across League of Legends, VALORANT, VALORANT Game Changers, Call of Duty and Rainbow Six, and its trophy case includes the inaugural Overwatch World Championship, the 2018 Rocket League World Championship, multiple LCS titles and a Counter-Strike Major. Beyond competition it runs Club9 (a membership and fan community at club9.cloud9.gg), an official Shopify merchandise store at store.cloud9.gg, and a content and creator division. Cloud9 publishes no developer program and no OpenAPI, but its public web estate is machine-readable: cloud9.gg runs on WordPress and serves an anonymous, unauthenticated WordPress REST API at /wp-json/ covering news posts, pages, media and the Cloud9-specific players, teams, achievement and case-study content types, alongside a remote Model Context Protocol
  server advertised through RFC 8414 and RFC 9728 discovery metadata.'
image: https://cloud9.gg/wp-content/uploads/Team_C9_blu_80x80.svg
json_schemas:
- name: Cloud9 Wp Rest Index
  property_count: 0
  slug: cloud9-wp-rest-index
- name: Cloud9 Wp Rest Schemas
  property_count: 0
  slug: cloud9-wp-rest-schemas
layout: provider
mcp_servers:
- description: Cloud9 publishes a remote Model Context Protocol server on its primary marketing host, cloud9.gg. It is not listed in any MCP registry, is not mentioned anywhere on the Cloud9 site, and Cloud9 operate
  name: Cloud9 MCP Server
  slug: cloud9
modified: '2026-10-06'
name: Cloud9
nav: Providers
network: true
overview: 'Cloud9 is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Esports, Gaming, Entertainment, and Media.


  Cloud9''s developer surface includes engineering blog, support, signup flow, authentication, and 25 more developer resources.'
random_paper: 16
scopes:
- name: Cloud9 Scopes
  scope_count: 1
  slug: cloud9-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 65.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 24.8
  provenance:
    conformance: first-party
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cloud9/cloud9-2026-09-02T145113.png
security:
- kind: authentication
  name: Cloud9 Authentication
  slug: cloud9-authentication
  summary_line: none/http/oauth2 · 4 schemes
- kind: domain-security
  name: Cloud9 Domain Security
  slug: cloud9-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Read the Cloud9 roster, teams, record and news
  slug: cloud9-read-roster-and-news
slug: cloud9
tags:
- Company
- Esports
- Gaming
- Entertainment
- Media
- Sports
- Content
- WordPress
- Community
- Merchandise
website: https://cloud9.gg/
---
