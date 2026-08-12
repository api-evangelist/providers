---
agent_readiness:
  band: agent-ready
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Anonymous, unaccredited Consumer Data Right energy Product Reference Data endpoint operated by the AER. Returns a paged summary of all current, generally available retail energy plans for one retailer
  name: AER Energy Product Reference Data - Get Generic Plans
  slug: aer-energy-product-reference-data-get-generic-plans
- description: Anonymous, unaccredited Consumer Data Right energy Product Reference Data endpoint operated by the AER. Returns the full detail of a single current, generally available retail energy plan by plan iden
  name: AER Energy Product Reference Data - Get Generic Plan Detail
  slug: aer-energy-product-reference-data-get-generic-plan-detail
- description: 'Anonymous Consumer Data Standards Common API discovery endpoints served by the AER on its CDR host. GET /discovery/status returns the current operational status of the data holder''s CDR endpoints and '
  name: AER CDR Discovery - Get Status and Get Outages
  slug: aer-cdr-discovery-status-and-outages
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aer.gov.au/
- group: company
  title: ''
  type: About
  url: https://www.aer.gov.au/about
- group: operate
  title: ''
  type: Contact
  url: https://www.aer.gov.au/about/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.aer.gov.au/energy-product-reference-data
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: start
  title: ''
  type: Registers
  url: https://www.aer.gov.au/industry/registers
- group: start
  title: ''
  type: Registers
  url: https://www.aer.gov.au/industry/registers/authorisations
- group: start
  title: ''
  type: DataPortal
  url: https://www.aer.gov.au/industry/registers/charts
- group: other
  title: ''
  type: Reports
  url: https://www.aer.gov.au/industry/wholesale/performance
- group: company
  title: ''
  type: Website
  url: https://www.energymadeeasy.gov.au/
- group: company
  title: ''
  type: Blog
  url: https://www.aer.gov.au/news
- group: other
  title: ''
  type: RSS
  url: https://www.aer.gov.au/rss.xml
- group: other
  title: ''
  type: Regulation
  url: https://www.cdr.gov.au/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aer.gov.au/documents/fact-sheet-accessing-energy-product-reference-data
- group: operate
  title: ''
  type: Support
  url: https://www.aer.gov.au/about/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aer.gov.au/about/policies/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aer.gov.au/about/policies/disclaimer-copyright
- group: other
  title: ''
  type: Accessibility
  url: https://www.aer.gov.au/about/policies/accessibility
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aergovau/
- group: operate
  title: ''
  type: StatusPage
  url: https://cdr.energymadeeasy.gov.au/agl/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/includes/endpoint-version-schedule/index.html
- group: auth
  title: ''
  type: Security
  url: https://www.aer.gov.au/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/aer-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aer-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aer-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aer-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aer-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aer-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/aer-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aer-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aer-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aer-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aer-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aer-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aer-cdr-energy-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aer-cds-common-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cds-common-api-openapi.json
created: '2026-07-27'
description: 'The Australian Energy Regulator (AER) is the independent national economic regulator of Australia''s energy markets, established under the Competition and Consumer Act 2010 and operating alongside the ACCC. It sets network revenues and prices, enforces the National Electricity, Gas and Energy Retail Rules, monitors wholesale and retail market conduct, sets the Default Market Offer, keeps the public registers of authorised retailers and exemptions, and operates Energy Made Easy, the government price-comparison service. Its API posture is the strongest found among Australian energy regulators and it is genuinely implemented rather than merely mandated. The AER is a designated data holder under the Competition and Consumer (Consumer Data Right) Rules 2020 and it serves the Consumer Data Standards energy Product Reference Data endpoints — Get Generic Plans and Get Generic Plan Detail — anonymously, with no accreditation, no API key and no signup, returning live retail plan, tariff,
  fee, discount and eligibility data for the six jurisdictions that adopted the National Energy Customer Framework. Verified on 2026-07-27, 79 of the 84 energy data-holder brands in the ACCC CDR Register point their productBaseUri at the AER''s own host, cdr.energymadeeasy.gov.au, which makes the regulator the actual operator of the product-data API layer for nearly the whole Australian retail energy industry. The split matters: the AER''s open surface is product and tariff data only. It holds and exposes no individual consumer usage or billing data — the CDR consumer endpoints 404 on its host — because those flow from retailers as primary data holders and AEMO as the secondary data holder gateway, behind ACCC accreditation, OAuth2/OIDC and mTLS. The AER''s own market statistics, wholesale performance reporting and public registers are published as web pages, charts and document downloads, not as an API, and no developer., developers., api., docs. or data. subdomain resolves.'
image: https://www.aer.gov.au/sites/default/files/2023-08/logo-2x.png
layout: provider
mcp_servers:
- description: ''
  name: aer-mcp.yml
  slug: aer-mcpyml
modified: '2026-07-27'
name: Australian Energy Regulator
nav: Providers
network: true
overview: 'Australian Energy Regulator publishes 3 APIs on the [APIs.io](https://apis.io/) network: AER Energy Product Reference Data - Get Generic Plans, AER Energy Product Reference Data - Get Generic Plan Detail, and AER CDR Discovery - Get Status and Get Outages. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  Australian Energy Regulator''s developer surface includes documentation, API reference, engineering blog, getting-started guide, support, authentication, changelog, and 35 more developer resources.'
random_paper: 80
rate_limits:
- limit_count: 3
  name: Aer Rate Limits
  slug: aer-rate-limits
score:
  band: developing
  composite: 50.3
  delta: -0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.2
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 81.6
  previous_composite: 50.8
  provenance:
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
    score: 48.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Aer Authentication
  slug: aer-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aer Domain Security
  slug: aer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aer Vulnerability Disclosure
  slug: aer-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aer
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Markets
- Consumer Data Right
- Retail Energy
- Regulation
- Government
- Open Data
- Smart Metering
website: https://www.aer.gov.au/
---
