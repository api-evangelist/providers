---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Liquid M Agentic Access
  operation_count: 7
  slug: liquid-m-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 5
apis:
- description: The Ads API from Liquid M — 1 operation(s) for ads.
  name: Liquid M Ads API
  slug: liquid-m-ads-api
- description: Auth token issuance for the Reporting API.
  name: Liquid M Authentication API
  slug: liquid-m-authentication-api
- description: The Budgets API from Liquid M — 1 operation(s) for budgets.
  name: Liquid M Budgets API
  slug: liquid-m-budgets-api
- description: The Campaigns API from Liquid M — 1 operation(s) for campaigns.
  name: Liquid M Campaigns API
  slug: liquid-m-campaigns-api
- description: Visual report queries across dimensions and metrics.
  name: Liquid M Reporting API
  slug: liquid-m-reporting-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LiquidM Management Ads API
  slug: open-liquid-m-ads-api
- collection_type: open
  name: LiquidM Management Ads Authentication API
  slug: open-liquid-m-authentication-api
- collection_type: open
  name: LiquidM Management Ads Budgets API
  slug: open-liquid-m-budgets-api
- collection_type: open
  name: LiquidM Management Ads Campaigns API
  slug: open-liquid-m-campaigns-api
- collection_type: open
  name: LiquidM Management Ads Reporting API
  slug: open-liquid-m-reporting-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liquid-m-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/liquid-m-management-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/liquidm/liquidm-reporting-api-client/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liquidm
- group: company
  title: ''
  type: Website
  url: https://liquidm.com
- group: start
  title: ''
  type: Portal
  url: https://platform.liquidm.com
- group: start
  title: ''
  type: SignUp
  url: https://platform.liquidm.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/liquid-m-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liquid-m-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/liquid-m-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liquid-m-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liquid-m-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/liquid-m-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/liquid-m-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/liquid-m-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/liquid-m-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/liquid-m-visual-report-response.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/liquid-m-visual-report.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquid-m-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/liquid-m-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liquid-m-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/liquid-m-reporting-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/liquid-m-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/liquid-m-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/liquidm/liquidm-reporting-api-client/blob/master/README.md
created: '2026-07-17'
description: 'LiquidM Technology GmbH is a Berlin-based demand-side platform for programmatic advertising, founded in 2013 and backed early by Earlybird, later Bertelsmann-owned, and acquired by Smart AdServer — now Equativ — in December 2019. Its platform at platform.liquidm.com exposes two developer surfaces: a Reporting API that returns the same data as the platform''s Visual Reports UI, split across more than thirty dimensions (campaign, ad, site, domain, device, geo, audience) and thirty-plus metrics (impressions, bids, bid requests, clicks, CTR, win rate, eCPM, conversion funnels, video quartiles); and a campaign Management API covering campaigns, budgets and ads. LiquidM publishes a first-party MIT-licensed JavaScript client for the Management API and an example Ruby client for the Reporting API from a 100-repo public GitHub organization, neither released to a package registry. Both APIs remain live and authenticate, but the published surface has fallen well behind the deployed one:
  probing confirms fifteen live v1 collections against the three the client documents, and an entirely undocumented v2 generation that answers in JSON:API. The liquidm.com marketing domain no longer serves HTTPS — its certificate expired in July 2026 — and over plain HTTP redirects to Equativ.'
examples:
- key_count: 3
  name: Liquid M Visual Report Response
  slug: liquid-m-visual-report-response
image: https://avatars.githubusercontent.com/u/5937978?v=4
json_schemas:
- name: LiquidM Visual Report
  property_count: 3
  slug: liquid-m-visual-report
layout: provider
mcp_servers:
- description: ''
  name: Liquid M MCP Server
  slug: liquid-m-mcp-server
modified: '2026-08-13'
name: Liquid M
nav: Providers
network: true
overview: 'Liquid M publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Authentication API, Budgets API, and 2 more. Tagged areas include Company, Advertising, AdTech, Demand-Side Platform, and Programmatic Advertising.


  Liquid M''s developer surface includes developer portal, signup flow, authentication, code examples, API reference, and 21 more developer resources.'
plans:
- name: Liquid M Plans Pricing
  plan_count: 0
  slug: liquid-m-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Liquid M Rate Limits
  slug: liquid-m-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 53.4
    developer_ergonomics: 37.5
    discoverability: 92.6
    governance: 31.8
    operational_transparency: 2.6
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liquid-m/refs/heads/main/screenshots/liquid-m-2026-07-25T225318.png
security:
- kind: authentication
  name: Liquid M Authentication
  slug: liquid-m-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Liquid M Domain Security
  slug: liquid-m-domain-security
  summary_line: TLSv1.2
slug: liquid-m
tags:
- Company
- Advertising
- AdTech
- Demand-Side Platform
- Programmatic Advertising
- Mobile Advertising
- Reporting
- Analytics
- Campaign Management
- OpenRTB
website: https://liquidm.com
---
