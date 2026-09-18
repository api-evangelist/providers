---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apa Agentic Access
  operation_count: 28
  slug: apa-agentic-access
  summary_line: 28 operations
api_count: 2
apis:
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: 'APA Corporation''s own corporate web surface at apacorp.com, exposed as a public, unauthenticated WordPress REST API at https://apacorp.com/wp-json. This entry covers the self-describing root: the name'
  name: APA Corporation
  slug: apa-corporation
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: 'The one route on apacorp.com that APA Corporation registered itself rather than inheriting from WordPress or a plugin: apa-ticker/v1, a public, unauthenticated, CORS-open JSON endpoint returning the d'
  name: APA Corporation Ticker API
  slug: apa-ticker-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the APA Corporation newsroom archive — press releases, community stories and operational updates published at apacorp.com. Verified live at 51 published posts on
  name: APA Corporation Newsroom API
  slug: apa-newsroom-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the APA Corporation leadership roster — the leaderships custom post type carrying executive team and board-of-director profiles rendered on the corporate governa
  name: APA Corporation Leadership API
  slug: apa-leadership-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static corporate pages of apacorp.com — operations by region (United States, Egypt, United Kingdom, Suriname), sustainability, governance, careers and policy
  name: APA Corporation Pages API
  slug: apa-pages-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the syndicated feed items APA Corporation aggregates onto apacorp.com — the wprss_feed_item custom post type produced by the site's RSS aggregator. Verified live
  name: APA Corporation Feed Items API
  slug: apa-feed-items-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the classification terms applied to APA Corporation newsroom content — the category and post_tag taxonomies. Verified live at 1 category and 0 tags on 2026-09-14
  name: APA Corporation Taxonomy API
  slug: apa-taxonomy-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the authors credited on APA Corporation newsroom posts. Verified live at 5 public authors on 2026-09-14. WordPress exposes only the public author view anonymousl
  name: APA Corporation Authors API
  slug: apa-authors-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated cross-resource search over apacorp.com content, returning lightweight id/title/url/type records. Measured behaviour on 2026-09-14: a search for ''energy'' returned X-WP-Total: 0,'
  name: APA Corporation Search API
  slug: apa-search-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: APA Corporation video content and media library assets.
  name: APA Corporation Media API
  slug: apa-media-api
- baseURL: https://apacorp.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 discovery and embed payloads for apacorp.com URLs.
  name: APA Corporation o Embed API
  slug: apa-o-embed-api
artifact_total: 28
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/overlays/apa-oembed-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apa-oembed-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/overlays/apa-media-hub-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apa-media-hub-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/security/apa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apa-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apa-corporation
- group: company
  title: ''
  type: Website
  url: https://apacorp.com
- group: operate
  title: ''
  type: Support
  url: https://apacorp.com/newsroom/contact-media-relations/
- group: company
  title: ''
  type: Blog
  url: https://apacorp.com/feed/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/authentication/apa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apa-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/conventions/apa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apa-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/errors/apa-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apa-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/conformance/apa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apa-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/lifecycle/apa-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apa-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/data-model/apa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apa-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/rate-limits/apa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apa-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/plans/apa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apa-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/llms/apa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apa-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/mcp/apa-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apa-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/agentic-access/apa-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apa-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/examples/apa-examples.yml
  title: ''
  type: Examples
  url: examples/apa-examples.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/packages/apa-packages.yml
  title: ''
  type: Packages
  url: packages/apa-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apacorp.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apacorp.com/terms-of-use/
- group: other
  title: ''
  type: Sustainability
  url: https://apacorp.com/sustainability/
- group: company
  title: ''
  type: Careers
  url: https://apacorp.com/careers/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.apacorp.com/
created: '2026-03-21'
description: APA Corporation is an independent energy company that explores for, develops, and produces natural gas, crude oil, and natural gas liquids, with operations in the United States, Egypt, the United Kingdom, and Suriname. Organized in Delaware and headquartered in Houston, Texas, APA is listed on Nasdaq (APA) and listed on Nasdaq Texas since March 2026.
examples:
- key_count: 22
  name: Apa Discovery Types
  slug: apa-discovery-types
- key_count: 6
  name: Apa Ticker Quote
  slug: apa-ticker-quote
features:
- description: Exploration and production activities in the Permian Basin and other US basins through the Apache Corporation subsidiary.
  name: United States Operations
- description: Long-standing operations in Egypt's Western Desert through Apache Corporation, one of the largest private natural gas producers in Egypt.
  name: Egypt Operations
- description: North Sea oil and gas operations through Apache Corporation's UK subsidiary.
  name: United Kingdom Operations
- description: Offshore exploration in Suriname Block 58 through the APA Suriname subsidiary, with significant oil discoveries including the GranMorgu project.
  name: Suriname Exploration
- description: Exploration activities on Alaska's North Slope including the Sockeye-2 well oil discovery in partnership with Lagniappe Alaska and Santos.
  name: Alaska Exploration
finops:
- name: Apa Finops
  service_category: API
  slug: apa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apa.png
integrations:
- description: 'APA Corporation is listed on Nasdaq (ticker: APA) and Nasdaq Texas, enabling trading and investor relations integrations.'
  name: Nasdaq
layout: provider
mcp_servers:
- description: APA Corporation ships no MCP server. This is a CANDIDATE manifest derived from the eleven OpenAPI documents in this repository, showing what an MCP server over the public apacorp.com REST surface woul
  name: APA Corporation MCP Server
  slug: apa-corporation-mcp-server
modified: '2026-09-14'
name: APA Corporation
nav: Providers
network: true
overview: 'APA Corporation publishes 11 APIs on the [APIs.io](https://apis.io/) network, including APA Corporation, Ticker API, Newsroom API, and 8 more. Tagged areas include Oil and Gas, Energy, Exploration, Production, and WordPress.


  APA Corporation''s developer surface includes support, engineering blog, authentication, code examples, and 22 more developer resources.'
plans:
- name: Apa Plans Pricing
  plan_count: 0
  slug: apa-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Apa Rate Limits
  slug: apa-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 17.2
    developer_ergonomics: 20.8
    discoverability: 75.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/screenshots/apa-2026-06-20T172039.png
security:
- kind: authentication
  name: Apa Authentication
  slug: apa-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Apa Domain Security
  slug: apa-domain-security
  summary_line: TLSv1.3
slug: apa
tags:
- Oil and Gas
- Energy
- Exploration
- Production
- WordPress
- REST
- Content
- Newsroom
- Investor Relations
- Energy Production
use_cases:
- description: Access financial results, stock information, SEC filings, and corporate governance information for APA Corporation shareholders.
  name: Investor Relations
- description: Track oil, natural gas, and natural gas liquids production data across APA's operational regions.
  name: Energy Production Data
website: https://apacorp.com
---
