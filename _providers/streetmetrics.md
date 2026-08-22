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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Public REST API for the StreetMetrics out-of-home advertising platform. 54 operations across campaigns, transit and stationary ad groups, assets and asset owners, frames, creatives, markets, media and
  name: StreetMetrics Public API
  slug: streetmetrics-public-api
artifact_total: 8
collections:
- collection_type: open
  name: StreetMetrics Public API
  slug: open-streetmetrics-public-api
common:
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
  name: streetmetrics-mcp.yml
  slug: streetmetrics-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-12'
name: StreetMetrics
nav: Providers
network: true
overview: 'StreetMetrics publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Advertising, Out-of-Home, Measurement, and Attribution.


  StreetMetrics'' developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, changelog, and 23 more developer resources.'
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
  composite: 37.6
  delta: -7.7
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 52.6
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 45.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
- Measurement
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
