---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Edf Energy Agentic Access
  operation_count: 43
  slug: edf-energy-agentic-access
  summary_line: 43 operations · 18 acting
api_count: 2
apis:
- description: EDF Energy's primary developer API, and the surface EDF markets as its "open tariff APIs". It is the Kraken GraphQL API, licensed from Octopus Energy Group and hosted for EDF GB. Introspection is enab
  name: EDF Kraken GraphQL API
  slug: edf-kraken-graphql-api
- description: APIs for importing accounts.
  name: EDF Energy Account Import API
  slug: edf-energy-account-import-api
- description: The data-import API from EDF Energy — 1 operation(s) for data-import.
  name: EDF Energy Data Import API
  slug: edf-energy-data-import-api
- description: The external-client-healthcheck API from EDF Energy — 1 operation(s) for external-client-healthcheck.
  name: EDF Energy External Client Healthcheck API
  slug: edf-energy-external-client-healthcheck-api
- description: The external-events API from EDF Energy — 1 operation(s) for external-events.
  name: EDF Energy External Events API
  slug: edf-energy-external-events-api
- description: APIs for importing additional data after an account has been imported.
  name: EDF Energy Post Account Import API
  slug: edf-energy-post-account-import-api
- description: APIs for querying import status and retrieving data
  name: EDF Energy Query API
  slug: edf-energy-query-api
- description: The v1 API from EDF Energy — 23 operation(s) for v1.
  name: EDF Energy V1 API
  slug: edf-energy-v1-api
- description: The v2 API from EDF Energy — 1 operation(s) for v2.
  name: EDF Energy V2 API
  slug: edf-energy-v2-api
artifact_total: 18
collections:
- collection_type: open
  name: Kraken
  slug: open-edf-energy-kraken-data-import
- collection_type: open
  name: Kraken
  slug: open-edf-energy-kraken
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/edf-energy-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/edf-energy-compare-tariffs.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/edf-energy-read-consumption.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/edf-energy-quote-and-enrol.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/edf-energy-migrate-customer-book.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/edf-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edf-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edf-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/edf-energy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/edf-energy-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/edf-energy-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edf-energy-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edf-energy-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edf-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edf-energy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.edfgb-kraken.energy/announcements/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/edf-energy-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.edfgb-kraken.energy/graphql/changelog/
- group: design
  title: ''
  type: Conformance
  url: conformance/edf-energy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/edf-energy-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/edf-energy-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://api.edfgb-kraken.energy/v1/graphql/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/edf-energy-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/edf-energy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/edf-energy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/edf-energy-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edf-energy-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edf-energy-api-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/edf-energy-kraken-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/edf-energy-kraken-data-import-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.edfenergy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.edfgb-kraken.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.edfgb-kraken.energy/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.edfgb-kraken.energy/rest/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.edfgb-kraken.energy/rest/guides/api-basics/
- group: operate
  title: ''
  type: Changelog
  url: https://developer.edfgb-kraken.energy/announcements/
- group: auth
  title: ''
  type: Authentication
  url: authentication/edf-energy-kraken-openid-configuration.json
- group: docs
  title: ''
  type: Documentation
  url: https://www.edfenergy.com/energywise/edfs-open-tariff-apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.edfenergy.com/energy/remit-summary
- group: company
  title: ''
  type: About
  url: https://www.edfenergy.com/about
- group: company
  title: ''
  type: News
  url: https://www.edfenergy.com/media-centre
- group: company
  title: ''
  type: Blog
  url: https://www.edfenergy.com/energywise
- group: operate
  title: ''
  type: Support
  url: https://www.edfenergy.com/help-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.edfenergy.com/for-home/help-centre
- group: commercial
  title: ''
  type: Pricing
  url: https://www.edfenergy.com/deemed-tariff-prices
- group: start
  title: ''
  type: SignUp
  url: https://www.edfenergy.com/gas-and-electricity/switch-energy-supplier
- group: start
  title: ''
  type: Login
  url: https://www.edfenergy.com/customer-information/activate-myaccount
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edfenergy.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edfenergy.com/terms-conditions/privacy-cookie-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edfenergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edf-energy
created: '2026-07-27'
description: 'EDF Energy Ltd is the British integrated energy business wholly owned by Electricite de France (EDF), the French state-owned utility. Formed in 2002 from London Electricity, SWEB and SEEBOARD and enlarged by the 2009 acquisition of British Energy, it is one of the largest suppliers of electricity and gas in Great Britain with roughly five million customer accounts, and it is also Britain''s largest generator of zero-carbon electricity — it operates the country''s fleet of operating nuclear power stations (the advanced gas-cooled reactors at Hartlepool, Heysham 1, Heysham 2 and Torness, and the Sizewell B pressurised water reactor), is building Hinkley Point C, and owns wind, solar, battery (Pivot Power) and EV charging (Pod Point) businesses. It therefore sits at both ends of the GB value chain: a licensed generator and wholesale market participant, and the retailer of record holding the customer relationship, the billing account and the meter data. Its API posture is the opposite
  of the mandated-utility pattern. The United Kingdom has no consumer energy data-portability right — no Consumer Data Right, no Green Button obligation. Britain mandated infrastructure instead: the licensed Smart DCC monopoly carries smart-meter traffic under the Smart Energy Code, and EDF is bound by that as a licensed supplier, but it confers no third-party consumer data API. And yet EDF publishes one of the more substantial public API programmes of any European utility, because it does not run its own retail platform: in 2023 EDF licensed Kraken from Octopus Energy Group and completed the migration of 5.8 million customer accounts in fifteen months, so EDF''s API is Kraken''s API, branded for EDF GB at developer.edfgb-kraken.energy. That portal is fully public and was confirmed live at HTTP 200 on 2026-07-27. It publishes a first-party OpenAPI 3.0.3 document for a 27-path REST API, a second OpenAPI 3.0.3 document for a 16-path customer-migration API, and a GraphQL API whose schema —
  2,492 types, 246 queries, 417 mutations — was harvested by anonymous introspection with no key and no account. EDF''s retail tariff and product data is genuinely open: GET https://api.edfgb-kraken.energy/v1/products/ returned 21 live products at HTTP 200 anonymously, and the GraphQL energyProducts query returns real EDF tariffs with brand "EDF". Consumer usage and billing data is documented in the same contracts but requires an Authorization token issued to the account holder, or an OAuth application authorised against the OpenID Connect server at auth.edfgb-kraken.energy, whose anonymously served discovery document advertises 111 scopes including request:consumption-data and view:smartflex-data. Open market data is the gap: EDF discloses its REMIT generation unavailability on its own website as an HTML table, but the XML and CSV export links it publishes on that very page both return HTTP 404, and the machine-readable channel for those disclosures is Elexon''s BMRS platform, which EDF
  does not operate — 27 EDF REMIT messages under registration code 48X000000000022A were confirmed there in a single week. Open on tariffs, gated on consumer data, broken on its own market-data exports, and none of it compelled.'
graphqls:
- description: EDF Energy's primary API is a GraphQL API, because EDF Energy runs on Kraken — the energy
  name: EDF Energy (EDF GB) Kraken GraphQL API
  slug: edf-energy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: No official EDF Energy or Kraken MCP server exists. Searched the EDF GB developer portal (developer.edfgb-kraken.energy), the EDF GitHub organisation, npm (edf-energy, edfgb-kraken, kraken-energy, oct
  name: EDF Energy MCP Server
  slug: edf-energy-mcp-server
modified: '2026-07-27'
name: EDF Energy
nav: Providers
network: true
overview: 'EDF Energy publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account Import API, Data Import API, External Client Healthcheck API, and 5 more. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  EDF Energy''s developer surface includes authentication, changelog, sandbox, developer console, documentation, API reference, getting-started guide, and 45 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 5
  name: Edf Energy Rate Limits
  slug: edf-energy-rate-limits
scopes:
- name: Edf Energy Scopes
  scope_count: 111
  slug: edf-energy-scopes
  summary_line: 111 scopes · authorizationCode/clientCredentials/deviceCode/tokenExchange
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 24
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 55.7
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: GB
      standard: smart-energy-code
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 78.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edf-energy/refs/heads/main/screenshots/edf-energy-2026-08-07T164723.png
security:
- kind: authentication
  name: Edf Energy Authentication
  slug: edf-energy-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 8 schemes
- kind: domain-security
  name: Edf Energy Domain Security
  slug: edf-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edf-energy
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Energy Retailer
- Energy Supplier
- Smart Metering
- Nuclear
- Renewables
- EV Charging
- Demand Response
- Tariffs
- Energy Markets
website: https://www.edfenergy.com/
---
