---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Uk Power Networks Agentic Access
  operation_count: 32
  slug: uk-power-networks-agentic-access
  summary_line: 32 operations
api_count: 2
apis:
- description: The current read-only REST API behind the UK Power Networks Open Data Portal, served from the company's own opendatasoft.com subdomain under an Opendatasoft Explore API v2.1 contract. Sixteen GET endp
  name: UK Power Networks Open Data Explore API v2.1
  slug: uk-power-networks-explore-api-v2-1
- description: The previous version of the UK Power Networks Open Data Portal REST API, still live and still serving its own OpenAPI 3.0.3 contract at the company domain. Same sixteen endpoints and same catalogue as
  name: UK Power Networks Open Data Explore API v2.0
  slug: uk-power-networks-explore-api-v2-0
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uk-power-networks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uk-power-networks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uk-power-networks-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ukpowernetworks.co.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UKPN-DSO
- group: start
  title: ''
  type: Portal
  url: https://ukpowernetworks.opendatasoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ukpowernetworks.co.uk/our-company/open-data-portal
- group: start
  title: ''
  type: Console
  url: https://ukpowernetworks.opendatasoft.com/api-console/explore/v2.1/
- group: start
  title: ''
  type: Signup
  url: https://ukpowernetworks.opendatasoft.com/signup/
- group: start
  title: ''
  type: Login
  url: https://ukpowernetworks.opendatasoft.com/login/
- group: other
  title: ''
  type: Glossary
  url: https://ukpowernetworks.opendatasoft.com/pages/glossary/
- group: auth
  title: ''
  type: Compliance
  url: https://ukpowernetworks.opendatasoft.com/pages/data-best-practice/
- group: other
  title: ''
  type: Regulation
  url: https://www.ofgem.gov.uk/decision/decision-updates-data-best-practice-guidance-and-digitalisation-strategy-and-action-plan-guidance
- group: other
  title: ''
  type: Data
  url: https://ukpowernetworks.opendatasoft.com/explore/
- group: other
  title: ''
  type: DSO
  url: https://dso.ukpowernetworks.co.uk/
- group: build
  title: ''
  type: SDK
  url: https://pypi.org/project/ukpyn/
- group: other
  title: ''
  type: Showcase
  url: https://ukpowernetworks.opendatasoft.com/pages/reuses/
- group: build
  title: ''
  type: Packages
  url: packages/uk-power-networks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/uk-power-networks-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uk-power-networks-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/uk-power-networks-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uk-power-networks-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uk-power-networks-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/uk-power-networks-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uk-power-networks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uk-power-networks-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/uk-power-networks-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uk-power-networks-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/uk-power-networks-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uk-power-networks-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/uk-power-networks-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uk-power-networks-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uk-power-networks-rate-limits.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uk-power-networks-business-glossary.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uk-power-networks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/UKPN-DSO/ukpyn/blob/main/SECURITY.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ukpowernetworks.opendatasoft.com/
- group: docs
  title: ''
  type: APIReference
  url: https://ukpowernetworks.opendatasoft.com/api-console/explore/v2.1/
- group: start
  title: ''
  type: GettingStarted
  url: https://ukpn-dso.github.io/ukpyn/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://github.com/UKPN-DSO/ukpyn/issues
- group: start
  title: ''
  type: SignUp
  url: https://ukpowernetworks.opendatasoft.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.huwise.com/en/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.huwise.com/en/privacy-policy.html
- group: start
  title: ''
  type: Sandbox
  url: https://ukpowernetworks.opendatasoft.com/api-console/explore/v2.1/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/UKPN-DSO/ukpyn
- group: learn
  title: ''
  type: Tutorials
  url: https://ukpn-dso.github.io/ukpyn/tutorials/
created: '2026-07-27'
description: 'UK Power Networks is the distribution network operator for London, the South East and the East of England, running three electricity distribution licence areas — London Power Networks (LPN), South Eastern Power Networks (SPN) and Eastern Power Networks (EPN) — and the Distribution System Operator function that sits on top of them. It is a poles-and-wires business: it owns the substations, cables and overhead lines, holds the network capacity and connection queue, and handles more than 70,000 connection enquiries a year, but it does not sell electricity and has no retail customer relationship to expose. Its API posture is the exact inverse of the usual utility story. Britain never legislated a consumer energy data right — there is no CDR equivalent, no Green Button obligation, and the one thing the UK did mandate was infrastructure (the Smart DCC carrying smart-meter traffic under the Smart Energy Code), which produces no public API. What did produce an API was Ofgem''s Data
  Best Practice and digitalisation obligation on network licensees, and UK Power Networks has actually implemented it: a live Opendatasoft-hosted Open Data Portal serving 136 datasets over a documented, versioned REST API with a real OpenAPI 3.0.3 contract published at its own domain, a DCAT-AP catalogue export, and an official open-source Python client (ukpyn) on PyPI. So the split is unusually sharp and unusually positive on one side: market and network data is genuinely open and genuinely queryable — live faults, carbon intensity, embedded capacity register, substation and feeder-level smart meter aggregates, LTDS tables, flexibility dispatches, curtailment events — while consumer data is not merely closed but absent, because as a DNO it holds no billable customer account to hand over. The gate is free and self-serve rather than open: the catalogue and 36 of 136 datasets answer anonymously, but the other 99 return HTTP 403 until you register a free account and mint an API key.'
examples:
- key_count: 10
  name: Uk Power Networks Getdataset Live Faults Response
  slug: uk-power-networks-getDataset-live-faults-response
- key_count: 2
  name: Uk Power Networks Getdatasets Response
  slug: uk-power-networks-getDatasets-response
- key_count: 2
  name: Uk Power Networks Getdatasetsfacets Response
  slug: uk-power-networks-getDatasetsFacets-response
- key_count: 2
  name: Uk Power Networks Getrecords Carbon Intensity Response
  slug: uk-power-networks-getRecords-carbon-intensity-response
- key_count: 2
  name: Uk Power Networks Getrecords Live Faults Response
  slug: uk-power-networks-getRecords-live-faults-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: uk-power-networks-mcp.yml
  slug: uk-power-networks-mcpyml
modified: '2026-07-27'
name: UK Power Networks
nav: Providers
network: true
overview: 'UK Power Networks publishes 2 APIs on the [APIs.io](https://apis.io/) network: Open Data Explore API v2.1 and Open Data Explore API v2.0. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Grid.


  UK Power Networks'' developer surface includes authentication, developer portal, documentation, developer console, signup flow, SDKs, changelog, and 41 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Uk Power Networks Rate Limits
  slug: uk-power-networks-rate-limits
score:
  band: developing
  composite: 48.7
  delta: -6.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 32.3
    developer_ergonomics: 73.4
    discoverability: 87.0
    governance: 31.3
    operational_transparency: 39.5
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 48.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Uk Power Networks Authentication
  slug: uk-power-networks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uk Power Networks Domain Security
  slug: uk-power-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uk Power Networks Vulnerability Disclosure
  slug: uk-power-networks-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: uk-power-networks
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Grid
- Distribution Network
- Open Data
- Smart Metering
- DER
- EV Charging
- Carbon
- Energy Markets
website: https://www.ukpowernetworks.co.uk/
---
