---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: JavaScript SDK providing publisher-side API methods for managing ad placements and requesting page views in single-page applications and infinite scroll implementations. Enables dynamic ad loading wit
  name: Yieldmo JavaScript SDK API
  slug: yieldmo-javascript-sdk-api
- description: Header bidding integration adapter for Prebid.js enabling publishers to receive bids from Yieldmo's exchange for display and video inventory. Supports placement-based targeting with optional bid floor
  name: Yieldmo Prebid.js Bid Adapter
  slug: yieldmo-prebidjs-bid-adapter
- description: Prebid.js module enabling publishers to integrate Yieldmo Synthetic Outstream ads by automatically creating placements and injecting the Yieldmo SDK. Requires a Yieldmo placement ID and Google Ad Mana
  name: Yieldmo Synthetic Inventory Module
  slug: yieldmo-synthetic-inventory-module
- description: Proprietary programmatic exchange and creative intelligence platform offering curated inventory access, contextual targeting, attention analytics, and deal management for advertisers and demand-side p
  name: Yieldmo YMax Platform API
  slug: yieldmo-ymax-platform-api
- baseURL: https://ads.yieldmo.com
  baseurl_source: declared
  description: The Canned Reports API from Yieldmo — 19 operation(s) for canned reports.
  name: Yieldmo Canned Reports API
  slug: yieldmo-canned-reports-api
- baseURL: https://ads.yieldmo.com
  baseurl_source: declared
  description: The Dcs API from Yieldmo — 1 operation(s) for dcs.
  name: Yieldmo Dcs API
  slug: yieldmo-dcs-api
- baseURL: https://ads.yieldmo.com
  baseurl_source: declared
  description: The Manage API from Yieldmo — 1 operation(s) for manage.
  name: Yieldmo Manage API
  slug: yieldmo-manage-api
- baseURL: https://ads.yieldmo.com
  baseurl_source: declared
  description: The Mcp API from Yieldmo — 1 operation(s) for mcp.
  name: Yieldmo MCP API
  slug: yieldmo-mcp-api
- baseURL: https://ads.yieldmo.com
  baseurl_source: declared
  description: The Ping API from Yieldmo — 1 operation(s) for ping.
  name: Yieldmo Ping API
  slug: yieldmo-ping-api
- baseURL: https://ads.yieldmo.com
  baseurl_source: declared
  description: The Register API from Yieldmo — 1 operation(s) for register.
  name: Yieldmo Register API
  slug: yieldmo-register-api
- baseURL: https://ads.yieldmo.com
  baseurl_source: declared
  description: The .well Known API from Yieldmo — 3 operation(s) for .well known.
  name: Yieldmo .well Known API
  slug: yieldmo-well-known-api
artifact_total: 22
collections:
- collection_type: open
  name: FastAPI
  slug: open-yieldmo-dcs-mcp
common:
- group: other
  href: https://artifacts.apis.io/yieldmo/capabilities/yieldmo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/yieldmo-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/yieldmo/yieldmo-js-sdk/issues
- group: other
  href: https://artifacts.apis.io/yieldmo/overlays/yieldmo-dcs-mcp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/yieldmo-dcs-mcp-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/yieldmo/security/yieldmo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yieldmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yieldmo.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/yieldmo/yieldmo-js-sdk/wiki
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yieldmo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yieldmo
- group: company
  title: ''
  type: Blog
  url: https://yieldmo.com/category/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://yieldmo.com/solutions/
- group: other
  title: ''
  type: X
  url: https://x.com/yieldmo
- group: start
  title: ''
  type: Login
  url: https://apps.yieldmo.com/auth
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yieldmo.com/privacy-policy/
- group: commercial
  href: https://artifacts.apis.io/yieldmo/plans/yieldmo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yieldmo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/yieldmo/rate-limits/yieldmo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/yieldmo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/yieldmo/finops/yieldmo-finops.yml
  title: ''
  type: FinOps
  url: finops/yieldmo-finops.yml
- group: agent
  href: https://artifacts.apis.io/yieldmo/mcp/yieldmo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/yieldmo-mcp.yml
- group: build
  href: https://artifacts.apis.io/yieldmo/mcp/yieldmo-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/yieldmo-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/yieldmo/well-known/yieldmo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yieldmo-well-known.yml
- group: auth
  href: https://artifacts.apis.io/yieldmo/authentication/yieldmo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yieldmo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/yieldmo/scopes/yieldmo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/yieldmo-scopes.yml
- group: design
  href: https://artifacts.apis.io/yieldmo/conventions/yieldmo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/yieldmo-conventions.yml
- group: design
  href: https://artifacts.apis.io/yieldmo/errors/yieldmo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/yieldmo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/yieldmo/data-model/yieldmo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yieldmo-data-model.yml
- group: design
  href: https://artifacts.apis.io/yieldmo/conformance/yieldmo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yieldmo-conformance.yml
- group: design
  href: https://artifacts.apis.io/yieldmo/lifecycle/yieldmo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/yieldmo-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/yieldmo/packages/yieldmo-packages.yml
  title: ''
  type: Packages
  url: packages/yieldmo-packages.yml
- group: build
  href: https://artifacts.apis.io/yieldmo/packages/yieldmo-packages.yml
  title: ''
  type: SDKs
  url: packages/yieldmo-packages.yml
- group: start
  href: https://artifacts.apis.io/yieldmo/sandbox/yieldmo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/yieldmo-sandbox.yml
- group: design
  href: https://artifacts.apis.io/yieldmo/components/yieldmo-components.yml
  title: ''
  type: Components
  url: components/yieldmo-components.yml
- group: agent
  href: https://artifacts.apis.io/yieldmo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/yieldmo/llms/yieldmo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yieldmo-llms.txt
created: '2026-06-13'
description: Yieldmo is a programmatic native advertising marketplace and smart exchange that differentiates and enhances the value of ad inventory for buyers and sellers. The platform provides REST APIs and JavaScript SDKs for managing ad placements, proprietary ad formats, contextual targeting, publisher inventory monetization, and campaign performance analytics powered by attention data and machine learning.
finops:
- has_sources: false
  method: generated
  name: Yieldmo Finops
  primary_unit: ''
  service_category: ''
  slug: yieldmo-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yieldmo.png
jsonld:
- class_count: 0
  name: Yieldmo Context
  property_count: 0
  slug: yieldmo
layout: provider
modified: '2026-08-12'
name: Yieldmo
nav: Providers
network: true
overview: 'Yieldmo publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Canned Reports API, Dcs API, Manage API, and 8 more. Tagged areas include Advertising, Programmatic, Native Advertising, Ad Exchange, and Publisher Monetization.


  The Yieldmo catalog on APIs.io includes 1 JSON-LD context.


  Yieldmo''s developer surface includes documentation, engineering blog, pricing, authentication, sandbox, and 27 more developer resources.'
plans:
- name: Yieldmo Plans Pricing
  plan_count: 3
  slug: yieldmo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Yieldmo Rate Limits
  slug: yieldmo-rate-limits
scopes:
- name: Yieldmo Scopes
  scope_count: 3
  slug: yieldmo-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 39.8
    developer_ergonomics: 39.9
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 36.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/yieldmo/yieldmo-2026-06-20T201742.png
security:
- kind: authentication
  name: Yieldmo Authentication
  slug: yieldmo-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Yieldmo Domain Security
  slug: yieldmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Profile a Yieldmo audience and pull attribution
  slug: yieldmo-audience-and-attribution
- name: Review Yieldmo campaign performance
  slug: yieldmo-campaign-performance-review
- name: Audit Yieldmo inventory quality by URL
  slug: yieldmo-inventory-quality-audit
slug: yieldmo
tags:
- Advertising
- Programmatic
- Native Advertising
- Ad Exchange
- Publisher Monetization
- Header Bidding
- Contextual Targeting
- Ad Formats
- Supply Side Platform
- Campaign Reporting
- Attention Analytics
- MCP
- Prebid
- AdTech
website: https://yieldmo.com
---
