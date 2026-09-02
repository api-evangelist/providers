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
  band_gated_from: agent-native
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-09-01'
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
- description: The Canned Reports API from Yieldmo — 19 operation(s) for canned reports.
  name: Yieldmo Canned Reports API
  slug: yieldmo-canned-reports-api
- description: The Dcs API from Yieldmo — 1 operation(s) for dcs.
  name: Yieldmo Dcs API
  slug: yieldmo-dcs-api
- description: The Manage API from Yieldmo — 1 operation(s) for manage.
  name: Yieldmo Manage API
  slug: yieldmo-manage-api
- description: The Mcp API from Yieldmo — 1 operation(s) for mcp.
  name: Yieldmo MCP API
  slug: yieldmo-mcp-api
- description: The Ping API from Yieldmo — 1 operation(s) for ping.
  name: Yieldmo Ping API
  slug: yieldmo-ping-api
- description: The Register API from Yieldmo — 1 operation(s) for register.
  name: Yieldmo Register API
  slug: yieldmo-register-api
- description: The .well Known API from Yieldmo — 3 operation(s) for .well known.
  name: Yieldmo .well Known API
  slug: yieldmo-well-known-api
artifact_total: 20
collections:
- collection_type: open
  name: FastAPI
  slug: open-yieldmo-dcs-mcp
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/yieldmo/yieldmo-js-sdk/issues
- group: other
  title: ''
  type: Overlay
  url: overlays/yieldmo-dcs-mcp-overlay.yaml
- group: auth
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
  title: ''
  type: Plans
  url: plans/yieldmo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yieldmo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yieldmo-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yieldmo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/yieldmo-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yieldmo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yieldmo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/yieldmo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yieldmo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yieldmo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yieldmo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yieldmo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yieldmo-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/yieldmo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/yieldmo-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/yieldmo-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/yieldmo-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yieldmo-llms.txt
created: '2026-06-13'
description: Yieldmo is a programmatic native advertising marketplace and smart exchange that differentiates and enhances the value of ad inventory for buyers and sellers. The platform provides REST APIs and JavaScript SDKs for managing ad placements, proprietary ad formats, contextual targeting, publisher inventory monetization, and campaign performance analytics powered by attention data and machine learning.
finops:
- name: Yieldmo Finops
  service_category: ''
  slug: yieldmo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yieldmo.png
jsonld:
- class_count: 0
  name: Yieldmo Context
  property_count: 0
  slug: yieldmo
layout: provider
mcp_servers:
- description: ''
  name: Yieldmo MCP Server
  slug: yieldmo-mcp-server
modified: '2026-08-12'
name: Yieldmo
nav: Providers
network: true
overview: 'Yieldmo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Canned Reports API, Dcs API, Manage API, and 4 more. Tagged areas include Advertising, Programmatic, Native Advertising, Ad Exchange, and Publisher Monetization.


  The Yieldmo catalog on APIs.io includes 1 JSON-LD context.


  Yieldmo''s developer surface includes documentation, engineering blog, pricing, authentication, sandbox, and 26 more developer resources.'
plans:
- name: Yieldmo Plans Pricing
  plan_count: 3
  slug: yieldmo-plans-pricing
random_paper: 20
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
  composite: 27.6
  coverage:
    artifact_dirs: 25
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 4.5
    contract_quality: 43.8
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  open_source:
    applies: true
    score: 0.0
  previous_composite: 27.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yieldmo/refs/heads/main/screenshots/yieldmo-2026-06-20T201742.png
security:
- kind: authentication
  name: Yieldmo Authentication
  slug: yieldmo-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Yieldmo Domain Security
  slug: yieldmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- SSP
- Campaign Reporting
- Attention Analytics
- MCP
- Prebid
- AdTech
website: https://yieldmo.com
---
