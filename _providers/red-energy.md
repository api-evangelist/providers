---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Red Energy Agentic Access
  operation_count: 27
  slug: red-energy-agentic-access
  summary_line: 27 operations
api_count: 3
apis:
- description: 'The unauthenticated Consumer Data Right Product Reference Data surface for the Red Energy brand - Get Generic Plans and Get Generic Plan Detail from the Consumer Data Standards CDR Energy API. Unlike '
  name: Red Energy CDR Energy Product Reference Data API
  slug: red-energy-cdr-energy-product-reference-data-api
- description: Red Energy's own registered Consumer Data Right public base URI, serving the two unauthenticated Data Holder Operations endpoints of the Consumer Data Standards CDR Common API - Get Status and Get Out
  name: Red Energy CDR Discovery API
  slug: red-energy-cdr-discovery-api
- description: The consumer-authorised half of the Consumer Data Right energy obligation that Red Energy is designated to meet as a data holder - electricity service points, usage, distributed energy resources, ener
  name: Red Energy CDR Energy Consumer Data API
  slug: red-energy-cdr-energy-consumer-data-api
arazzos:
- description: Check that Red Energy's CDR implementation is available, then list its published electricity plans and pull the full tariff detail for one of them. Every step is unauthenticated — no API key, no signu
  name: Compare Red Energy tariff plans
  slug: red-energy-compare-plans-workflow
artifact_total: 19
collections:
- collection_type: open
  name: CDR Common API
  slug: open-red-energy-cds-common
- collection_type: open
  name: CDR Energy API
  slug: open-red-energy-cds-energy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/red-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/red-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/red-energy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/red-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/red-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/red-energy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr.redenergy.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#endpoint-version-schedule
- group: operate
  title: ''
  type: Roadmap
  url: https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/red-energy-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/red-energy-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/red-energy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.redenergy.com.au/docs/Red-Energy-Consumer-Data-Right-Policy.pdf
- group: design
  title: ''
  type: DataModel
  url: data-model/red-energy-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/red-energy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/red-energy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/red-energy-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/red-energy-llms.txt
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-energy-compare-plans-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.redenergy.com.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/red-energy
- group: operate
  title: ''
  type: Status
  url: https://public.cdr.redenergy.com.au/cds-au/v1/discovery/status
- group: start
  title: ''
  type: Registry
  url: https://api.cdr.gov.au/cdr-register/v1/energy/data-holders/brands/summary
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: operate
  title: ''
  type: Support
  url: https://www.redenergy.com.au/contactus/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.redenergy.com.au/help-centre/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redenergy.com.au/products/
- group: start
  title: ''
  type: SignUp
  url: https://myaccount.redenergy.com.au/registration
- group: start
  title: ''
  type: Login
  url: https://myaccount.redenergy.com.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redenergy.com.au/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redenergy.com.au/privacy-policy/index.html
- group: other
  title: ''
  type: Owner
  url: https://www.snowyhydro.com.au/retail/
created: '2026-07-27'
description: 'Red Energy Pty Ltd (ABN 60 107 479 372) is an Australian electricity and gas retailer, wholly owned by Snowy Hydro Ltd, that supplies more than a million residential and business customers across New South Wales, Victoria, Queensland, South Australia and the ACT from a Richmond, Victoria base. It sits on the retail end of the National Electricity Market value chain: Snowy Hydro generates, the distribution network businesses own the poles and wires, AEMO operates the market and holds metering data, and Red Energy owns the customer, the tariff and the bill. Its API posture is entirely a product of statute rather than product strategy. Red Energy publishes no developer portal, no self-serve API programme and no proprietary specification - developer., api., docs. and data. subdomains do not resolve, and redenergy.com.au itself sits behind a Cloudflare bot challenge that returns HTTP 403 to any non-browser client. What it does have is a real, verified Consumer Data Right implementation:
  it is a designated CDR energy data holder listed on the CDR Register with the public base URI https://public.cdr.redenergy.com.au, which serves the Consumer Data Standards discovery endpoints live with correct x-v version negotiation, while 1,705 Red Energy branded plans are published anonymously through the Australian Energy Regulator''s Energy Made Easy CDR host. The split is the story - open, standardised, anonymous product reference data on one side, and consumer usage, billing and account data available only to accredited CDR data recipients with the customer''s consent on the other, with nothing at all in between.'
examples:
- key_count: 7
  name: Red Energy Error Missing X V Example
  slug: red-energy-error-missing-x-v-example
- key_count: 7
  name: Red Energy Error Plan Not Found Example
  slug: red-energy-error-plan-not-found-example
- key_count: 7
  name: Red Energy Error Unsupported Version Example
  slug: red-energy-error-unsupported-version-example
- key_count: 7
  name: Red Energy Get Energy Plan Detail Example
  slug: red-energy-get-energy-plan-detail-example
- key_count: 7
  name: Red Energy Get Outages Example
  slug: red-energy-get-outages-example
- key_count: 7
  name: Red Energy Get Status Example
  slug: red-energy-get-status-example
- key_count: 7
  name: Red Energy List Energy Plans Example
  slug: red-energy-list-energy-plans-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/red-energy.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool set derived from the CDR specs
  slug: candidate-mcp-tool-set-derived-from-the-cdr-specs
modified: '2026-07-27'
name: Red Energy
nav: Providers
network: true
overview: 'Red Energy publishes 3 APIs on the [APIs.io](https://apis.io/) network: CDR Energy Product Reference Data API, CDR Discovery API, and CDR Energy Consumer Data API. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  Red Energy''s developer surface includes authentication, changelog, code examples, status page, documentation, API reference, support, and 29 more developer resources.'
random_paper: 116
rate_limits:
- limit_count: 15
  name: Red Energy Rate Limits
  slug: red-energy-rate-limits
scopes:
- name: Red Energy Scopes
  scope_count: 11
  slug: red-energy-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 56.8
  delta: 4.7
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 30.3
    contract_quality: 51.7
    developer_ergonomics: 35.1
    discoverability: 72.2
    governance: 30.3
    operational_transparency: 68.4
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Red Energy Authentication
  slug: red-energy-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Red Energy Domain Security
  slug: red-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: red-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retail
- Consumer Data Right
- CDR
- Product Reference Data
- Smart Metering
- Open Data
website: https://www.redenergy.com.au/
---
