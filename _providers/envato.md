---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: quarter
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Envato Agentic Access
  operation_count: 11
  slug: envato-agentic-access
  summary_line: 11 operations
api_count: 2
apis:
- description: Affiliate-only API for Envato Elements (subscription-based stock media). Provides search and metadata for catalog discovery within affiliate properties; not a general-purpose download API.
  name: Envato Elements Affiliate API
  slug: elements-affiliate
- baseURL: https://api.envato.com
  baseurl_source: declared
  description: The Market API from Envato — 36 operation(s) for market.
  name: Envato Market API
  slug: envato-market-api
- baseURL: https://api.envato.com
  baseurl_source: declared
  description: The search API from Envato — 3 operation(s) for search.
  name: Envato Search API
  slug: envato-search-api
artifact_total: 31
collections:
- collection_type: open
  name: Envato Market Author API
  slug: open-envato-author-api
- collection_type: open
  name: Envato Market Author Catalog API
  slug: open-envato-catalog-api
- collection_type: open
  name: Envato Market Author Downloads API
  slug: open-envato-downloads-api
- collection_type: open
  name: Envato Market Author Items API
  slug: open-envato-items-api
- collection_type: open
  name: Envato Market Author Search API
  slug: open-envato-search-api
- collection_type: open
  name: Envato Market Author User API
  slug: open-envato-user-api
- collection_type: open
  name: Envato Market API
  slug: open-envato
common:
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-envato-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-envato-security.txt
- group: design
  href: https://artifacts.apis.io/envato/rules/envato-rules.yml
  title: ''
  type: Spectral
  url: rules/envato-rules.yml
- group: design
  href: https://artifacts.apis.io/envato/json-ld/envato-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/envato-context.jsonld
- group: design
  href: https://artifacts.apis.io/envato/vocabulary/envato-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/envato-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/envato/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/envato/data-model/envato-data-model.yml
  title: ''
  type: DataModel
  url: data-model/envato-data-model.yml
- group: design
  href: https://artifacts.apis.io/envato/conventions/envato-conventions.yml
  title: ''
  type: Conventions
  url: conventions/envato-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.envato.com/lp/vulnerability-disclosure/
- group: design
  href: https://artifacts.apis.io/envato/lifecycle/envato-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/envato-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/envato/conformance/envato-conformance.yml
  title: ''
  type: Conformance
  url: conformance/envato-conformance.yml
- group: other
  href: https://artifacts.apis.io/envato/overlays/envato-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/envato-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/envato/mcp/envato-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/envato-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/envato/mcp/envato-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/envato-mcp.yml
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-www-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-elements-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-elements-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-community-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-community-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-build-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-build-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-author-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-author-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-app-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-api-security.txt
- group: auth
  href: https://artifacts.apis.io/envato/well-known/envato-account-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envato-account-security.txt
- group: agent
  href: https://artifacts.apis.io/envato/well-known/envato-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/envato-well-known.yml
- group: other
  href: https://artifacts.apis.io/envato/hosts/envato-hosts.yml
  title: ''
  type: Hosts
  url: hosts/envato-hosts.yml
- group: other
  href: https://artifacts.apis.io/envato/vendors/envato-vendors.yml
  title: ''
  type: Vendors
  url: vendors/envato-vendors.yml
- group: build
  href: https://artifacts.apis.io/envato/packages/envato-packages.yml
  title: ''
  type: SDKs
  url: packages/envato-packages.yml
- group: build
  href: https://artifacts.apis.io/envato/packages/envato-packages.yml
  title: ''
  type: Packages
  url: packages/envato-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.author.envato.com/
- group: agent
  href: https://artifacts.apis.io/envato/agentic-access/envato-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/envato-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/envato/security/envato-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/envato-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/envato/security/envato-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/envato-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/envato/authentication/envato-authentication.yml
  title: ''
  type: Authentication
  url: authentication/envato-authentication.yml
- group: auth
  href: https://artifacts.apis.io/envato/scopes/envato-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/envato-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/envato
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/envato
- group: company
  title: ''
  type: Website
  url: https://envato.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://build.envato.com/
- group: commercial
  href: https://artifacts.apis.io/envato/plans/envato-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/envato-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/envato/rate-limits/envato-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/envato-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/envato/finops/envato-finops.yml
  title: ''
  type: FinOps
  url: finops/envato-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://envato.com/blog/rss.xml
- group: docs
  title: ''
  type: APIReference
  url: https://build.envato.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://build.envato.com/api/#get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://build.envato.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.envato.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.envato.com/
- group: operate
  title: ''
  type: Support
  url: https://help.market.envato.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://elements.envato.com/pricing
- group: start
  title: ''
  type: Login
  url: https://elements.envato.com/sign-in
- group: company
  title: ''
  type: Newsroom
  url: https://elements.envato.com/learn/c/news
created: '2026-05-08'
description: Envato runs Envato Market (per-asset marketplaces like ThemeForest, CodeCanyon, AudioJungle, VideoHive, GraphicRiver, 3DOcean, PhotoDune) and Envato Elements (subscription-based unlimited stock media). The Envato API exposes Market endpoints for items, search, downloads, user accounts, and earnings, documented at build.envato.com; Elements runs an affiliate program, but no public affiliate API documentation was found as of 2026-10.
finops:
- has_sources: true
  method: generated
  name: Envato Finops
  primary_unit: ''
  service_category: Stock Media / Digital Marketplace
  slug: envato-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envato.png
json_schemas:
- name: AuthorSale
  property_count: 8
  slug: envato-author-sale
- name: CollectionDetails
  property_count: 3
  slug: envato-collection-details
- name: Collection
  property_count: 7
  slug: envato-collection
- name: Item
  property_count: 24
  slug: envato-item
- name: MarketPurchaseForAuthor
  property_count: 8
  slug: envato-market-purchase-for-author
- name: MarketPurchaseForBuyer
  property_count: 7
  slug: envato-market-purchase-for-buyer
jsonld:
- class_count: 23
  name: Envato Context
  property_count: 89
  slug: envato-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.envato.com over HTTP; 15 tools listed.
  name: Envato MCP Server
  slug: envato
modified: '2026-10-21'
name: Envato
nav: Providers
network: true
overview: 'Envato publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Market API, Search API, and 1 more. Tagged areas include Stock Media, Marketplace, Themes, Audio, and Video.


  The Envato catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Envato''s developer surface includes documentation, authentication, engineering blog, API reference, getting-started guide, support, pricing, and 44 more developer resources.'
plans:
- name: Envato Plans Pricing
  plan_count: 4
  slug: envato-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Envato Rate Limits
  slug: envato-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Envato API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: envato-rules
scopes:
- name: Envato Scopes
  scope_count: 18
  slug: envato-scopes
  summary_line: 18 scopes · implicit
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 48.3
    developer_ergonomics: 51.8
    discoverability: 69.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 28.6
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/envato/envato-2026-06-20T180736.png
security:
- kind: authentication
  name: Envato Authentication
  slug: envato-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Envato Domain Security
  slug: envato-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Envato Vulnerability Disclosure
  slug: envato-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: envato-download-purchases
  slug: envato-download-purchases
- name: envato-manage-collections
  slug: envato-manage-collections
- name: envato-search-market-items
  slug: envato-search-market-items
- name: envato-verify-purchase-code
  slug: envato-verify-purchase-code
slug: envato
tags:
- Stock Media
- Marketplace
- Themes
- Audio
- Video
- Graphics
- Subscription
- Australia
website: https://envato.com/
---
