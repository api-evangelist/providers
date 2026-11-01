---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Ad Groups API from StreetMetrics — 7 operation(s) for ad groups.
  name: StreetMetrics Ad Groups API
  slug: streetmetrics-ad-groups-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Assets API from StreetMetrics — 5 operation(s) for assets.
  name: StreetMetrics Assets API
  slug: streetmetrics-assets-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Attribution Studies API from StreetMetrics — 6 operation(s) for attribution studies.
  name: StreetMetrics Attribution Studies API
  slug: streetmetrics-attribution-studies-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Authentication API from StreetMetrics — 1 operation(s) for authentication.
  name: StreetMetrics Authentication API
  slug: streetmetrics-authentication-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Campaigns API from StreetMetrics — 2 operation(s) for campaigns.
  name: StreetMetrics Campaigns API
  slug: streetmetrics-campaigns-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Creatives API from StreetMetrics — 2 operation(s) for creatives.
  name: StreetMetrics Creatives API
  slug: streetmetrics-creatives-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Frames API from StreetMetrics — 2 operation(s) for frames.
  name: StreetMetrics Frames API
  slug: streetmetrics-frames-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Markets API from StreetMetrics — 1 operation(s) for markets.
  name: StreetMetrics Markets API
  slug: streetmetrics-markets-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Media API from StreetMetrics — 2 operation(s) for media.
  name: StreetMetrics Media API
  slug: streetmetrics-media-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Pixels API from StreetMetrics — 4 operation(s) for pixels.
  name: StreetMetrics Pixels API
  slug: streetmetrics-pixels-api
- baseURL: https://dashboard.streetmetrics.io/v3/public/
  baseurl_source: declared
  description: The Reporting API from StreetMetrics — 8 operation(s) for reporting.
  name: StreetMetrics Reporting API
  slug: streetmetrics-reporting-api
artifact_total: 22
collections:
- collection_type: open
  name: StreetMetrics Public API
  slug: open-streetmetrics-public-api
common:
- group: other
  href: https://artifacts.apis.io/streetmetrics/capabilities/streetmetrics-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/streetmetrics-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/streetmetrics/overlays/streetmetrics-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/streetmetrics-public-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/streetmetrics/authentication/streetmetrics-authentication.yml
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
  href: https://artifacts.apis.io/streetmetrics/security/streetmetrics-domain-security.yml
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
  href: https://artifacts.apis.io/streetmetrics/changelog/streetmetrics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/streetmetrics-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.streetmetrics.com/changelog
- group: design
  href: https://artifacts.apis.io/streetmetrics/lifecycle/streetmetrics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/streetmetrics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/streetmetrics/conventions/streetmetrics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/streetmetrics-conventions.yml
- group: design
  href: https://artifacts.apis.io/streetmetrics/errors/streetmetrics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/streetmetrics-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/streetmetrics/rate-limits/streetmetrics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/streetmetrics-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/streetmetrics/data-model/streetmetrics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/streetmetrics-data-model.yml
- group: design
  href: https://artifacts.apis.io/streetmetrics/conformance/streetmetrics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/streetmetrics-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/streetmetrics/plans/streetmetrics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/streetmetrics-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/streetmetrics/packages/streetmetrics-packages.yml
  title: ''
  type: Packages
  url: packages/streetmetrics-packages.yml
- group: agent
  href: https://artifacts.apis.io/streetmetrics/llms/streetmetrics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/streetmetrics-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.streetmetrics.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/streetmetrics/well-known/streetmetrics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/streetmetrics-well-known.yml
- group: agent
  href: https://artifacts.apis.io/streetmetrics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/streetmetrics/mcp/streetmetrics-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/streetmetrics-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.streetmetrics.com/mcp
- group: build
  href: https://artifacts.apis.io/streetmetrics/mcp/streetmetrics-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/streetmetrics-tool-crosswalk.yml
created: '2026-07-17'
description: StreetMetrics is an out-of-home (OOH) advertising measurement, planning, and attribution platform that gives operators, agencies, and brands data-driven tools to plan campaigns, track delivery in near real-time across 1.6M+ OOH units, and measure business outcomes from outdoor advertising. Its SmartSearch planning intelligence surfaces unit-level performance and audience insights, daily-refreshed impression measurement tracks delivery, and attribution connects OOH exposure to website visits, app opens, and in-store lift. StreetMetrics publishes a public REST API — the StreetMetrics Public API, documented at docs.streetmetrics.com and served from dashboard.streetmetrics.io/v3/public/ — covering campaigns, ad groups, assets, frames, creatives, markets, media, attribution studies, conversion pixels, and impression/demographic/uniques-and-frequency reporting. Authentication is a JWT bearer token minted from the same email and password used to sign in to the StreetMetrics platform,
  so API access follows a platform subscription rather than self-serve developer signup.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/streetmetrics.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.streetmetrics.com over streamable HTTP.
  name: StreetMetrics Documentation MCP Server
  slug: streetmetrics-documentation-mcp-server
modified: '2026-08-12'
name: StreetMetrics
nav: Providers
network: true
overview: 'StreetMetrics publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad Groups API, Assets API, Attribution Studies API, and 8 more. Tagged areas include Company, Advertising, Out-of-Home, Measurements, and Attribution.


  StreetMetrics'' developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, changelog, and 25 more developer resources.'
plans:
- name: Streetmetrics Plans Pricing
  plan_count: 0
  slug: streetmetrics-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Streetmetrics Rate Limits
  slug: streetmetrics-rate-limits
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 43.5
    developer_ergonomics: 58.9
    discoverability: 71.7
    operational_transparency: 21.1
  previous_composite: 41.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/streetmetrics/streetmetrics-2026-08-17T082138.png
security:
- kind: authentication
  name: Streetmetrics Authentication
  slug: streetmetrics-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Streetmetrics Domain Security
  slug: streetmetrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: streetmetrics-authenticate
  slug: streetmetrics-authenticate
- name: streetmetrics-build-a-campaign
  slug: streetmetrics-build-a-campaign
- name: streetmetrics-pull-campaign-reporting
  slug: streetmetrics-pull-campaign-reporting
- name: read-the-docs
  slug: streetmetrics-read-the-docs
- name: streetmetrics-run-an-attribution-study
  slug: streetmetrics-run-an-attribution-study
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
