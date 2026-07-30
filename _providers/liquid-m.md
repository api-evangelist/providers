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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-07-28'
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
artifact_total: 10
common:
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
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liquid-m-well-known.yml
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
created: '2026-07-17'
description: 'LiquidM Technology GmbH is a Berlin-based demand-side platform for programmatic advertising, backed by Earlybird. Its platform at platform.liquidm.com exposes two developer surfaces: a Reporting API that returns the same data as the platform''s Visual Reports UI, split across more than thirty dimensions (campaign, ad, site, domain, device, geo, audience) and thirty-plus metrics (impressions, bids, bid requests, clicks, CTR, win rate, eCPM, conversion funnels, video quartiles); and a campaign Management API covering campaigns, budgets and ads. LiquidM publishes a first-party MIT-licensed JavaScript client for the Management API and an example Ruby client for the Reporting API from a 100-repo public GitHub organization. The liquidm.com marketing domain now redirects to Equativ, though the platform host and its APIs remain reachable.'
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
  name: liquid-m-mcp.yml
  slug: liquid-m-mcpyml
modified: '2026-07-19'
name: Liquid M
nav: Providers
network: true
overview: 'Liquid M publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Authentication API, Budgets API, and 2 more. Tagged areas include Company, Advertising, AdTech, Demand-Side Platform, and Programmatic Advertising.


  Liquid M''s developer surface includes developer portal, signup flow, authentication, code examples, and 16 more developer resources.'
random_paper: 64
score:
  band: thin
  composite: 35.6
  delta: -2.1
  facets:
    commercial_clarity: 13.2
    contract_quality: 57.8
    developer_ergonomics: 29.9
    discoverability: 92.6
    governance: 21.9
    operational_transparency: 5.3
  previous_composite: 37.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
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
  summary_line: TLSv1.2 · HSTS
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
