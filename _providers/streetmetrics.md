---
access_model:
  confidence: medium
  label: Public API, platform credentials required
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  - docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The Ad Groups API from StreetMetrics — 7 operation(s) for ad groups.
  name: StreetMetrics Ad Groups API
  slug: streetmetrics-ad-groups-api
- description: The Assets API from StreetMetrics — 5 operation(s) for assets.
  name: StreetMetrics Assets API
  slug: streetmetrics-assets-api
- description: The Attribution Studies API from StreetMetrics — 6 operation(s) for attribution studies.
  name: StreetMetrics Attribution Studies API
  slug: streetmetrics-attribution-studies-api
- description: The Authentication API from StreetMetrics — 1 operation(s) for authentication.
  name: StreetMetrics Authentication API
  slug: streetmetrics-authentication-api
- description: The Campaigns API from StreetMetrics — 2 operation(s) for campaigns.
  name: StreetMetrics Campaigns API
  slug: streetmetrics-campaigns-api
- description: The Creatives API from StreetMetrics — 2 operation(s) for creatives.
  name: StreetMetrics Creatives API
  slug: streetmetrics-creatives-api
- description: The Frames API from StreetMetrics — 2 operation(s) for frames.
  name: StreetMetrics Frames API
  slug: streetmetrics-frames-api
- description: The Markets API from StreetMetrics — 1 operation(s) for markets.
  name: StreetMetrics Markets API
  slug: streetmetrics-markets-api
- description: The Media API from StreetMetrics — 2 operation(s) for media.
  name: StreetMetrics Media API
  slug: streetmetrics-media-api
- description: The Pixels API from StreetMetrics — 4 operation(s) for pixels.
  name: StreetMetrics Pixels API
  slug: streetmetrics-pixels-api
- description: The Reporting API from StreetMetrics — 8 operation(s) for reporting.
  name: StreetMetrics Reporting API
  slug: streetmetrics-reporting-api
artifact_total: 18
collections:
- collection_type: open
  name: StreetMetrics Public API
  slug: open-streetmetrics-public-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/streetmetrics-public-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/streetmetrics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://streetmetrics.com/
- group: company
  title: ''
  type: Blog
  url: https://streetmetrics.com/resource-hub
- group: commercial
  title: ''
  type: TermsOfService
  url: https://streetmetrics.com/privacy-terms/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://streetmetrics.com/privacy-terms/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streetmetrics-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.streetmetrics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.streetmetrics.com/reference/ad-groups
- group: docs
  title: ''
  type: APIReference
  url: https://docs.streetmetrics.com/reference/ad-groups
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.streetmetrics.com/recipes/how-to-authenticate-requests-and-create-tokens
- group: start
  title: ''
  type: Login
  url: https://platform.streetmetrics.com/login
- group: operate
  title: ''
  type: Support
  url: https://streetmetrics.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/streetmetrics
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/streetmetrics-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.streetmetrics.com/changelog
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/streetmetrics-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/streetmetrics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/streetmetrics-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/streetmetrics-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/streetmetrics-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/streetmetrics-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/streetmetrics-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/streetmetrics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/streetmetrics-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.streetmetrics.com/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/streetmetrics-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/streetmetrics-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.streetmetrics.com/mcp
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/streetmetrics-tool-crosswalk.yml
created: '2026-07-17'
description: StreetMetrics is an out-of-home (OOH) advertising measurement, planning, and attribution platform that gives operators, agencies, and brands data-driven tools to plan campaigns, track delivery in near real-time across 1.6M+ OOH units, and measure business outcomes from outdoor advertising. Its SmartSearch planning intelligence surfaces unit-level performance and audience insights, daily-refreshed impression measurement tracks delivery, and attribution connects OOH exposure to website visits, app opens, and in-store lift. StreetMetrics publishes a public REST API — the StreetMetrics Public API, documented at docs.streetmetrics.com and served from dashboard.streetmetrics.io/v3/public/ — covering campaigns, ad groups, assets, frames, creatives, markets, media, attribution studies, conversion pixels, and impression/demographic/uniques-and-frequency reporting. Authentication is a JWT bearer token minted from the same email and password used to sign in to the StreetMetrics platform,
  so API access follows a platform subscription rather than self-serve developer signup.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/streetmetrics.png
layout: provider
mcp_servers:
- description: ''
  name: StreetMetrics Documentation MCP Server
  slug: streetmetrics-documentation-mcp-server
- description: ''
  name: StreetMetrics MCP Server
  slug: streetmetrics-mcp-server
modified: '2026-08-12'
name: StreetMetrics
nav: Providers
network: true
overview: 'StreetMetrics publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Ad Groups API, Assets API, Attribution Studies API, and 8 more. Tagged areas include Company, Advertising, Out-of-Home, Measurements, and Attribution.


  StreetMetrics'' developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, changelog, and 24 more developer resources.'
plans:
- name: Streetmetrics Plans Pricing
  plan_count: 0
  slug: streetmetrics-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Streetmetrics Rate Limits
  slug: streetmetrics-rate-limits
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 47.0
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 35.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/streetmetrics/refs/heads/main/screenshots/streetmetrics-2026-08-17T082138.png
security:
- kind: authentication
  name: Streetmetrics Authentication
  slug: streetmetrics-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Streetmetrics Domain Security
  slug: streetmetrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: streetmetrics
tags:
- Company
- Advertising
- Out-of-Home
- Measurements
- Attribution
- Analytics
- Marketing
- Location Data
- Media Planning
- Transit Advertising
- Campaign Reporting
- Audience Data
website: https://streetmetrics.com/
---
