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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Agl Energy Agentic Access
  operation_count: 27
  slug: agl-energy-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 3
apis:
- description: 'AGL''s mandated Consumer Data Right energy data-sharing surface, implementing the DSB Consumer Data Standards CDR Energy API v1.36.0 — service points, electricity usage, DER register detail, accounts, '
  name: AGL CDR Energy API
  slug: agl-cdr-energy-api
- description: The unauthenticated half of AGL's Consumer Data Right implementation, served from its CDR public base URI and conforming to the DSB Consumer Data Standards CDR Common API v1.36.0. GET /cds-au/v1/disco
  name: AGL CDR Discovery (Common) API
  slug: agl-cdr-discovery-api
- description: 'AGL''s retail energy plans published as anonymous, machine-readable Consumer Data Right Product Reference Data. Verified live on 2026-07-27: GET /energy/plans?page-size=10 returned HTTP 200 with x-v:1,'
  name: AGL Energy Product Reference Data (PRD) API
  slug: agl-energy-product-reference-data-api
artifact_total: 11
collections:
- collection_type: open
  name: CDR Common API
  slug: open-agl-energy-cds-common
- collection_type: open
  name: CDR Energy API
  slug: open-agl-energy-cds-energy
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agl-energy-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agl-energy-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agl-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agl-energy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agl-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agl-energy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agl-energy-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agl-energy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr.agl.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#endpoint-version-schedule
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agl-energy-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agl-energy-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agl-energy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agl-energy-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agl-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.agl.com.au/terms-conditions/responsible-disclosure-policy
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: company
  title: ''
  type: Website
  url: https://www.agl.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agl.com.au/consumer-data-right-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agl.com.au/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agl.com.au/terms-conditions/online-services
- group: operate
  title: ''
  type: Support
  url: https://www.agl.com.au/help-support/account-setup-management/manage-consumer-data-right
- group: operate
  title: ''
  type: Forum
  url: https://neighbourhood.agl.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AGLEnergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agl-energy
- group: other
  title: ''
  type: Registration
  url: https://api.cdr.gov.au/cdr-register/v1/all/data-holders/brands/summary
created: '2026-07-27'
description: 'AGL Energy Limited (ASX:AGL) is Australia''s oldest listed company — founded in Sydney in 1837 as the Australian Gas Light Company — and one of the country''s largest integrated energy businesses, retailing electricity, gas, broadband and mobile to roughly four million customer accounts while owning the nation''s largest electricity generation portfolio (Bayswater and Loy Yang A coal, gas peakers, hydro, wind, utility-scale solar and grid-scale batteries). It sits at both ends of the Australian value chain: generator and wholesale market participant in the NEM, and the retailer of record that holds the customer relationship, the billing account and the metering data. Its API posture is entirely a product of regulation, not of product strategy. AGL publishes no public developer portal and no self-serve API programme — apideveloper.agl.com.au resolves through Akamai but returns HTTP 403 to every anonymous client, and agl.com.au itself is bot-blocked at 403. What AGL does expose
  is the Consumer Data Right: it is a designated CDR energy data holder, listed on the CDR Register under brand "AGL" with public base URI https://public.cdr.agl.com.au, and that surface is real and verified — GET /cds-au/v1/discovery/status and /cds-au/v1/discovery/outages both return HTTP 200 with conformant Consumer Data Standards envelopes, and AGL''s own outage notices describe scheduled downtime of the "AGL CDR Consent flow". Its energy plan Product Reference Data is genuinely open and anonymous — 1,343 plans at https://cdr.energymadeeasy.gov.au/agl/cds-au/v1/energy/plans — but that endpoint is operated centrally by the Australian Energy Regulator, not by AGL, which is the structural difference from CDR banking where every bank serves its own PRD. Consumer usage, billing, service point, DER and account data is available only to Accredited Data Recipients, over mTLS, under a consumer authorisation, with the base URI distributed through the CDR Register rather than published. AGL is
  therefore open on product data, closed to everyone but accredited recipients on consumer data, and silent everywhere else — it publishes no open grid or market data of its own. It is also migrating around four million customer services onto the Kaluza platform under a A$150m, 20 percent stake taken in 2024, so the retail data layer behind these mandated endpoints is being rebuilt on a third-party energy operating system.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: agl-energy-mcp.yml
  slug: agl-energy-mcpyml
modified: '2026-07-27'
name: AGL Energy
nav: Providers
network: true
overview: 'AGL Energy publishes 3 APIs on the [APIs.io](https://apis.io/) network: AGL CDR Energy API, AGL CDR Discovery (Common) API, and Product Reference Data (PRD) API. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  AGL Energy''s developer surface includes authentication, changelog, API reference, documentation, support, and 22 more developer resources.'
random_paper: 109
scopes:
- name: Agl Energy Scopes
  scope_count: 11
  slug: agl-energy-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 13.1
    developer_ergonomics: 34.2
    discoverability: 72.2
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Agl Energy Authentication
  slug: agl-energy-authentication
  summary_line: oauth2/openIdConnect/mutualTLS/none · 3 schemes
- kind: domain-security
  name: Agl Energy Domain Security
  slug: agl-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agl Energy Vulnerability Disclosure
  slug: agl-energy-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: agl-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retailer
- Consumer Data Right
- CDR
- Smart Metering
- Solar
- DER
- Renewables
- Energy Markets
website: https://www.agl.com.au/
---
