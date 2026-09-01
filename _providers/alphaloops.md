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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: Hosted remote Model Context Protocol server exposing 2.7M U.S. motor carriers as tools for LLM clients (Claude Desktop/Code, Cursor, Windsurf, VS Code Copilot, Clay). Advertises 30+ tools across six c
  name: AlphaLoops MCP Server
  slug: alphaloops-mcp-server
- description: The Carriers API from AlphaLoops FMCSA Carrier Data API — 19 operation(s) for carriers.
  name: AlphaLoops FMCSA Carrier Data API Carriers API
  slug: alphaloops-carriers-api
- description: The Contacts API from AlphaLoops FMCSA Carrier Data API — 2 operation(s) for contacts.
  name: AlphaLoops FMCSA Carrier Data API Contacts API
  slug: alphaloops-contacts-api
- description: The Inspections API from AlphaLoops FMCSA Carrier Data API — 2 operation(s) for inspections.
  name: AlphaLoops FMCSA Carrier Data API Inspections API
  slug: alphaloops-inspections-api
- description: The Vins API from AlphaLoops FMCSA Carrier Data API — 1 operation(s) for vins.
  name: AlphaLoops FMCSA Carrier Data API Vins API
  slug: alphaloops-vins-api
artifact_total: 14
collections:
- collection_type: open
  name: AlphaLoops FMCSA Carrier Data API
  slug: open-alphaloops-fmcsa-carrier-data-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/alphaloops-fmcsa-carrier-data-api-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/alphaloops-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alphaloops-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/alphaloops-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: security/alphaloops-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alphaloops-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alphaloops-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/alphaloops-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alphaloops-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/alphaloops-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alphaloops-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alphaloops-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/alphaloops-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alphaloops-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/alphaloops-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alphaloops-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alphaloops-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/alphaloops-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.runalphaloops.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/alphaloops-lifecycle.yml
- group: operate
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alphaloops.png
layout: provider
mcp_servers:
- description: ''
  name: AlphaLoops FMCSA Carrier Data API MCP Server
  slug: alphaloops-fmcsa-carrier-data-api-mcp-server
- description: AlphaLoops operates a hosted, remote MCP server exposing its FMCSA carrier-data platform as tools. The provider publishes a dedicated MCP reference page marked "Live" carrying the endpoint, the transp
  name: AlphaLoops MCP Server
  slug: alphaloops-mcp-server
modified: '2026-08-11'
name: AlphaLoops FMCSA Carrier Data API
nav: Providers
network: true
overview: 'AlphaLoops FMCSA Carrier Data API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Carriers API, Contacts API, Inspections API, and 1 more. Tagged areas include fmcsa api, safer web api, dot lookup, carrier data, and Freight.


  AlphaLoops FMCSA Carrier Data API''s developer surface includes authentication, CLI, changelog, pricing, support, and 24 more developer resources.'
plans:
- name: Alphaloops Plans Pricing
  plan_count: 6
  slug: alphaloops-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Alphaloops Rate Limits
  slug: alphaloops-rate-limits
score:
  band: exemplar
  composite: 67.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 62.4
    developer_ergonomics: 70.8
    discoverability: 85.2
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 67.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alphaloops/refs/heads/main/screenshots/alphaloops-2026-07-25T195758.png
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
- Risk
- Fraud
---
