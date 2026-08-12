---
access_model:
  confidence: high
  label: Free - Open, no registration
  onboarding: open
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The public CKAN 2.8.7 API behind the NESO Data Portal, serving 128 open datasets covering GB electricity demand, generation, balancing, ancillary services, constraints, interconnectors, connection reg
  name: NESO Data Portal API
  slug: neso-data-portal-api
- description: The official Carbon Intensity API for Great Britain, developed by NESO, giving national and regional carbon intensity of GB electricity - actual, forecast up to 96+ hours ahead, half-hourly generation
  name: Carbon Intensity API
  slug: neso-carbon-intensity-api
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/carbon-intensity/api-definitions/issues
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/neso-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.neso.energy/responsible-disclosure
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/neso-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neso-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/neso-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neso-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neso-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neso-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/neso-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neso-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neso-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/neso-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/neso-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/neso-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neso-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.neso.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://www.neso.energy/data-portal/api-guidance
- group: start
  title: ''
  type: Portal
  url: https://www.neso.energy/data-portal
- group: docs
  title: ''
  type: APIReference
  url: https://carbon-intensity.github.io/api-definitions/
- group: other
  title: ''
  type: Licensing
  url: https://www.neso.energy/data-portal/neso-open-licence
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neso.energy/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neso.energy/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.neso.energy/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carbon-intensity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neso-energy
- group: company
  title: ''
  type: BlogRSS
  url: https://www.neso.energy/rss.xml
- group: company
  title: ''
  type: News
  url: https://www.neso.energy/news
created: '2026-07-27'
description: The National Energy System Operator (NESO) is Great Britain's publicly owned, operationally independent electricity system operator and whole-energy system planner, created on 1 October 2024 when the UK government purchased National Grid Electricity System Operator Limited and folded in gas system planning from National Gas Transmission. NESO balances the GB electricity system in real time, runs the connections queue, publishes Future Energy Scenarios, and sits at the centre of the value chain between generators, interconnectors, transmission and distribution networks, and suppliers. Its API posture is the sector's classic split, and NESO lands firmly on the open side of that split. Market and system data is genuinely open and anonymous - the NESO Data Portal exposes 128 datasets over a public CKAN API at api.neso.energy with no key, no account and no application, all under the permissive NESO Open Data Licence, and the Carbon Intensity API for Great Britain that NESO develops
  is one of the most openly consumed public energy APIs in the world. There is no consumer data surface at all, and none is expected, because NESO holds no retail customer relationships, Britain has no consumer energy data-portability mandate comparable to the Australian Consumer Data Right, and smart-meter consumption data travels through the licensed Smart DCC monopoly rather than through the system operator. NESO's open-data obligation comes from Ofgem's Data Best Practice Guidance embedded in its RIIO-2 licence, and unlike most of the sector that obligation is visibly implemented rather than merely claimed.
image: https://www.neso.energy/themes/custom/neso_theme/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: neso-mcp.yml
  slug: neso-mcpyml
modified: '2026-07-27'
name: National Energy System Operator (NESO)
nav: Providers
network: true
overview: 'National Energy System Operator (NESO) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United Kingdom, Electricity, Energy Markets, and Grid.


  National Energy System Operator (NESO)''s developer surface includes authentication, documentation, developer portal, API reference, support, product news, and 23 more developer resources.'
random_paper: 89
rate_limits:
- limit_count: 3
  name: Neso Rate Limits
  slug: neso-rate-limits
score:
  band: thin
  composite: 30.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 47.4
  previous_composite: 30.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neso/refs/heads/main/screenshots/neso-2026-08-07T184913.png
security:
- kind: authentication
  name: Neso Authentication
  slug: neso-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Neso Domain Security
  slug: neso-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Neso Vulnerability Disclosure
  slug: neso-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: neso
tags:
- Energy
- United Kingdom
- Electricity
- Energy Markets
- Grid
- Open Data
- Carbon
- Renewables
- Gas
- Demand Response
website: https://www.neso.energy/
---
