---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-09-19'
api_count: 5
apis:
- description: Machine-payable US recall lookups over x402. Given a product, brand, ingredient or vehicle (make/model/year), returns active recalls across FDA food/drug/device enforcement, NHTSA vehicle safety campa
  name: RecallScout
  slug: recallscout
- description: 'Machine-payable air-quality queries over x402 with global coverage: current US AQI and pollutant breakdown for a lat/lon, an EPA (AirNow) based verdict on whether it is safe to exercise outdoors, and '
  name: AirScout
  slug: airscout
- description: 'Machine-payable US border-crossing queries over x402. Ranks all 85 US ports of entry by all-in time - the drive there plus the live CBP wait once there - per lane type (standard, SENTRI/NEXUS, Ready, '
  name: BorderScout
  slug: borderscout
- description: 'Machine-payable cheapest-fuel queries over x402. Station-level prices for Spain, France and Italy and official regional averages for the US, by location and grade, with an optional smart ranking that '
  name: FuelScout
  slug: fuelscout
- description: 'Machine-payable, impersonal research feeds over x402: ranked 0-30 DTE options candidates (/picks), dividend and tax-free municipal income (/dividends), crypto scalp candidates (/crypto) and risk-adjus'
  name: ScalpStream Research
  slug: scalpstream-research
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://scalpstream.com/
- group: docs
  title: ''
  type: Documentation
  url: https://recallscout.scalpstream.com/.well-known/x402
- group: start
  title: ''
  type: GettingStarted
  url: https://www.scalpstream.com/#Products
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scalpstream.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DV1-321
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/DV1-321/scalpstream-mcp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/a2a/scalpstream-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/scalpstream-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/mcp/scalpstream-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scalpstream-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/packages/scalpstream-com-packages.yml
  title: ''
  type: Packages
  url: packages/scalpstream-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/well-known/scalpstream-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scalpstream-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/x402/scalpstream-com-x402.yml
  title: ''
  type: X-X402
  url: x402/scalpstream-com-x402.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/llms/scalpstream-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scalpstream-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://recallscout.scalpstream.com/llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/conformance/scalpstream-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scalpstream-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/conventions/scalpstream-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scalpstream-com-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/authentication/scalpstream-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scalpstream-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/errors/scalpstream-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scalpstream-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/lifecycle/scalpstream-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scalpstream-com-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/plans/scalpstream-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scalpstream-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/rate-limits/scalpstream-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scalpstream-com-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/changelog/scalpstream-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/scalpstream-com-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/data-model/scalpstream-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scalpstream-com-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/sandbox/scalpstream-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/scalpstream-com-sandbox.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scalpstream-com/refs/heads/main/regulatory/scalpstream-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/scalpstream-com-regulatory-posture.yml
created: '2026-09-19'
description: 'ScalpStream operates a family of machine-payable data APIs built for autonomous agents: RecallScout (active US FDA, NHTSA and CPSC recalls with severity normalised across the three regulators), AirScout (global air quality with an EPA-based outdoor-exertion verdict and the cleanest window ahead), BorderScout (all 85 US ports of entry ranked by drive-plus-wait time per lane), FuelScout (cheapest fuel - station-level for Spain, France and Italy, official regional averages for the US) and ScalpStream Research (impersonal ranked options, dividend, crypto and yield feeds). Every service is a plain HTTPS GET priced at a flat $0.01 per request and settled per request over x402 (HTTP 402) in USDC on Base, Arbitrum or Polygon or XRP/RLUSD on the XRP Ledger - no accounts, no API keys, no subscriptions - with a free preview on every host, an A2A agent card and JSON-RPC endpoint per service, and a first-party local MCP server (scalpmcp) that buys from all of them with the user''s own wallet.'
image: https://recallscout.scalpstream.com/icon.png
json_schemas:
- name: Scalpstream Com Research
  property_count: 0
  slug: scalpstream-com-research
layout: provider
mcp_servers:
- description: ''
  name: ScalpStream MCP Server
  slug: scalpstream-mcp-server
modified: '2026-09-19'
name: ScalpStream
nav: Providers
network: true
overview: 'ScalpStream publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agents, A2A, x402, and Micropayments.


  ScalpStream''s developer surface includes documentation, getting-started guide, pricing, authentication, changelog, sandbox, and 18 more developer resources.'
plans:
- name: Scalpstream Com Plans Pricing
  plan_count: 0
  slug: scalpstream-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Scalpstream Com Rate Limits
  slug: scalpstream-com-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 13.3
    developer_ergonomics: 34.5
    discoverability: 81.5
    operational_transparency: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Scalpstream Com Authentication
  slug: scalpstream-com-authentication
  summary_line: 0 schemes
slug: scalpstream-com
tags:
- Company
- Agents
- A2A
- x402
- Micropayments
- MCP
- Open Data
- Product Recalls
- Air Quality
- Border Crossings
- Fuel Prices
- Market Research
- Public Safety
- Cryptocurrency
- USDC
- XRP Ledger
- llms-txt
- JSON Schema
website: https://scalpstream.com/
---
