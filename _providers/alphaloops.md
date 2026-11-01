---
access_model:
  confidence: high
  label: Paid — sales-gated API key
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://runalphaloops.com/pricing
  - https://runalphaloops.com/mcp
  - https://runalphaloops.com/fmcsa-api/docs
  trial: true
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
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Hosted remote Model Context Protocol server exposing 2.7M U.S. motor carriers as tools for LLM clients (Claude Desktop/Code, Cursor, Windsurf, VS Code Copilot, Clay). Advertises 30+ tools across six c
  name: AlphaLoops MCP Server
  slug: alphaloops-mcp-server
- baseURL: https://mcp-freight.runalphaloops.com
  baseurl_source: declared
  description: The Carriers API from AlphaLoops FMCSA Carrier Data API — 19 operation(s) for carriers.
  name: AlphaLoops FMCSA Carrier Data API Carriers API
  slug: alphaloops-carriers-api
- baseURL: https://mcp-freight.runalphaloops.com
  baseurl_source: declared
  description: The Contacts API from AlphaLoops FMCSA Carrier Data API — 2 operation(s) for contacts.
  name: AlphaLoops FMCSA Carrier Data API Contacts API
  slug: alphaloops-contacts-api
- baseURL: https://mcp-freight.runalphaloops.com
  baseurl_source: declared
  description: The Inspections API from AlphaLoops FMCSA Carrier Data API — 2 operation(s) for inspections.
  name: AlphaLoops FMCSA Carrier Data API Inspections API
  slug: alphaloops-inspections-api
- baseURL: https://mcp-freight.runalphaloops.com
  baseurl_source: declared
  description: The Vins API from AlphaLoops FMCSA Carrier Data API — 1 operation(s) for vins.
  name: AlphaLoops FMCSA Carrier Data API Vins API
  slug: alphaloops-vins-api
- baseURL: https://mcp-freight.runalphaloops.com
  baseurl_source: declared
  description: The Custom Data API from AlphaLoops FMCSA Carrier Data API — 3 operation(s) for custom data.
  name: AlphaLoops FMCSA Carrier Data API Custom Data API
  slug: alphaloops-custom-data-api
- baseURL: https://mcp-freight.runalphaloops.com
  baseurl_source: declared
  description: The Mc Sale Listings API from AlphaLoops FMCSA Carrier Data API — 1 operation(s) for mc sale listings.
  name: AlphaLoops FMCSA Carrier Data API Mc Sale Listings API
  slug: alphaloops-mc-sale-listings-api
- baseURL: https://mcp-freight.runalphaloops.com
  baseurl_source: declared
  description: The Mc Sales API from AlphaLoops FMCSA Carrier Data API — 1 operation(s) for mc sales.
  name: AlphaLoops FMCSA Carrier Data API Mc Sales API
  slug: alphaloops-mc-sales-api
- baseURL: https://mcp-freight.runalphaloops.com
  baseurl_source: declared
  description: The Peer Groups API from AlphaLoops FMCSA Carrier Data API — 1 operation(s) for peer groups.
  name: AlphaLoops FMCSA Carrier Data API Peer Groups API
  slug: alphaloops-peer-groups-api
artifact_total: 21
collections:
- collection_type: open
  name: AlphaLoops FMCSA Carrier Data API
  slug: open-alphaloops-fmcsa-carrier-data-api
common:
- group: other
  href: https://artifacts.apis.io/alphaloops/capabilities/alphaloops-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/alphaloops-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/alphaloops/plans/alphaloops-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alphaloops-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/alphaloops/rate-limits/alphaloops-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/alphaloops-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://runalphaloops.com/blog/
- group: company
  title: ''
  type: Website
  url: https://www.runalphaloops.com/
- group: other
  href: https://artifacts.apis.io/alphaloops/overlays/alphaloops-fmcsa-carrier-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/alphaloops-fmcsa-carrier-data-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/alphaloops/security/alphaloops-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/alphaloops-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/alphaloops/security/alphaloops-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alphaloops-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alphaloops/security/alphaloops-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/alphaloops-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alphaloops/security/alphaloops-trust-center.yml
  title: ''
  type: Compliance
  url: security/alphaloops-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/alphaloops/security/alphaloops-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphaloops-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/alphaloops/authentication/alphaloops-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alphaloops-authentication.yml
- group: build
  href: https://artifacts.apis.io/alphaloops/packages/alphaloops-packages.yml
  title: ''
  type: Packages
  url: packages/alphaloops-packages.yml
- group: build
  href: https://artifacts.apis.io/alphaloops/packages/alphaloops-packages.yml
  title: ''
  type: SDKs
  url: packages/alphaloops-packages.yml
- group: build
  href: https://artifacts.apis.io/alphaloops/cli/alphaloops-cli.yml
  title: ''
  type: CLI
  url: cli/alphaloops-cli.yml
- group: agent
  href: https://artifacts.apis.io/alphaloops/well-known/alphaloops-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alphaloops-well-known.yml
- group: agent
  href: https://artifacts.apis.io/alphaloops/mcp/alphaloops-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alphaloops-mcp.yml
- group: build
  href: https://artifacts.apis.io/alphaloops/mcp/alphaloops-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/alphaloops-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/alphaloops/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/alphaloops/llms/alphaloops-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphaloops-llms.txt
- group: design
  href: https://artifacts.apis.io/alphaloops/conformance/alphaloops-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alphaloops-conformance.yml
- group: design
  href: https://artifacts.apis.io/alphaloops/conventions/alphaloops-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alphaloops-conventions.yml
- group: design
  href: https://artifacts.apis.io/alphaloops/lifecycle/alphaloops-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alphaloops-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/alphaloops/lifecycle/alphaloops-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/alphaloops-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.runalphaloops.com
- group: operate
  href: https://artifacts.apis.io/alphaloops/lifecycle/alphaloops-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/alphaloops-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/alphaloops/changelog/alphaloops-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alphaloops-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://runalphaloops.com/whats-new
- group: commercial
  title: ''
  type: Pricing
  url: https://runalphaloops.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://runalphaloops.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RunAlphaLoop
- group: start
  title: ''
  type: Login
  url: https://alphafreight.runalphaloops.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runalphaloops.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runalphaloops.com/privacy
created: '2026-07-07'
description: The carrier data layer for freight — FMCSA motor-carrier intelligence covering carrier profiles, authority & insurance history, VIN-level fleet data, roadside inspections, crashes, corporate connections, decision-maker contacts, and risk/watchlist monitoring. Exposes a REST API, a live OpenAPI 3.1 contract, a hosted MCP server with 30+ tools, and published Python/TypeScript SDKs plus a CLI.
finops:
- has_sources: true
  method: derived
  name: Alphaloops Finops
  primary_unit: 1,000 credits/mo
  service_category: ''
  slug: alphaloops-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alphaloops.png
layout: provider
mcp_servers:
- description: ''
  name: AlphaLoops FMCSA Carrier Data API MCP Server
  slug: mcp
modified: '2026-10-06'
name: AlphaLoops FMCSA Carrier Data API
nav: Providers
network: true
overview: 'AlphaLoops FMCSA Carrier Data API publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Carriers API, Contacts API, Inspections API, and 6 more. Tagged areas include fmcsa api, safer web api, dot lookup, carrier data, and Freight.


  AlphaLoops FMCSA Carrier Data API''s developer surface includes engineering blog, authentication, CLI, changelog, pricing, support, and 28 more developer resources.'
plans:
- name: Alphaloops Plans Pricing
  plan_count: 8
  slug: alphaloops-plans-pricing
- name: Alphaloops Price Estimates
  plan_count: 0
  slug: alphaloops-price-estimates
random_paper: 19
rate_limits:
- limit_count: 5
  name: Alphaloops Rate Limits
  slug: alphaloops-rate-limits
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 53.0
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 86.8
  previous_composite: 67.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/alphaloops/alphaloops-2026-07-25T195758.png
security:
- kind: authentication
  name: Alphaloops Authentication
  slug: alphaloops-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alphaloops Domain Security
  slug: alphaloops-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Alphaloops Vulnerability Disclosure
  slug: alphaloops-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Alphaloops Trust Center
  slug: alphaloops-trust-center
  summary_line: SOC 2 Type II, ISO 27001, NIST Cybersecurity Framework, COBIT
skill_count: 2
skills:
- name: alphaloops-carrier-prospecting
  slug: alphaloops-carrier-prospecting
- name: alphaloops-carrier-vetting
  slug: alphaloops-carrier-vetting
slug: alphaloops
tags:
- fmcsa api
- safer web api
- dot lookup
- carrier data
- Freight
- Trucking
- motor carrier
- fleet intelligence
- Sales Intelligence
- MCP Server
- Contact Enrichment
- Risk Management
- Fraud Prevention
website: https://www.runalphaloops.com/
---
