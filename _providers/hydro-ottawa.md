---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Hydro Ottawa's mandated Green Button Connect My Data surface — the OAuth-authorized, machine-to-machine channel through which a customer can grant a third-party application ongoing access to their sma
  name: Hydro Ottawa Green Button Connect My Data (CMD) API
  slug: hydro-ottawa-green-button-connect-my-data-api
artifact_total: 5
collections:
- collection_type: open
  name: Green Button API Documentation
  slug: open-hydro-ottawa-green-button-espi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hydro-ottawa-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hydro-ottawa-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hydro-ottawa-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/hydro-ottawa-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hydro-ottawa-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hydro-ottawa-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/hydro-ottawa-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hydro-ottawa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hydro-ottawa-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hydro-ottawa-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hydro-ottawa-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://hydroottawa.com/
- group: company
  title: ''
  type: Website
  url: https://hydroottawagroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ottawaonboarding.savagedata.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://hydroottawa.com/en/accounts-services/services/green-button/green-button-and-third-party-registration
- group: start
  title: ''
  type: SignUp
  url: https://ottawaonboarding.savagedata.com/
- group: company
  title: ''
  type: Blog
  url: https://hydroottawa.com/en/about-us/blogs-articles
- group: company
  title: ''
  type: BlogRSS
  url: https://hydroottawa.com/en/rss.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hydroottawa.com/en/about-us/policies-and-terms/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hydroottawa.com/en/about-us/policies-and-terms/privacy-notice
- group: docs
  title: ''
  type: Documentation
  url: https://hydroottawa.com/en/residential/rates-billing/track-your-usage/green-button
- group: other
  title: ''
  type: Registration
  url: https://ottawaonboarding.savagedata.com/
- group: operate
  title: ''
  type: Support
  url: https://hydroottawa.com/en/faq
- group: operate
  title: ''
  type: StatusPage
  url: https://outages.hydroottawa.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hydroottawa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hydro-ottawa
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/hydroottawa.bsky.social
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/hydroottawalimited/
created: '2026-07-27'
description: 'Hydro Ottawa Holding Inc. is a private corporation 100 percent owned by the City of Ottawa, and the parent of Hydro Ottawa Limited — the regulated local distribution company (LDC) that delivers electricity to roughly 372,000 customers in Ottawa and Casselman, Ontario — alongside Portage Power (Ontario''s largest municipally-owned renewable generator, with run-of-river hydroelectric plants at Chaudière Falls and elsewhere in Ontario, Quebec and New York plus solar installations across Ottawa), Envari (energy solutions) and Hiboo Networks (fibre). It sits at the wires-and-meter end of the Canadian value chain: it does not run the market — that is IESO — and it is not a competitive retailer, it is the monopoly distributor that owns the smart meter, the interval data and the billing relationship. Its API posture exists because Ontario legislated it. Ontario Regulation 633/21 (Energy Data) under the Electricity Act, 1998 compels roughly sixty electricity and natural gas utilities
  in the province to implement Green Button Download My Data and Green Button Connect My Data to the NAESB REQ.21 ESPI v3.3 standard and to have those implementations certified by the Green Button Alliance — a province-level, standard-specific consumer data mandate with no Canadian national equivalent. Hydro Ottawa states on its own site that it offers both services free of charge and that third parties must complete its onboarding process and certify with the GBA. Two live surfaces back that up: a customer Green Button authorization portal at https://hydroottawa.savagedata.com/Connect/Authorize (HTTP 200) and an anonymously reachable third-party developer registration application at https://ottawaonboarding.savagedata.com/ (HTTP 200), both operated by the North Bay vendor Savage Data Systems. What could NOT be verified is the thing the mandate actually requires: no ESPI base URI is published anywhere, the vendor host is a catch-all Blazor SPA that returns HTTP 200 with identical HTML for
  every path including invented ones, no OpenID Connect discovery document is served anonymously, and no public Green Button Alliance certificate register listing Hydro Ottawa by name could be found. The mandate is recorded here as claimed-and-plausibly- operating, not as verified. Everything else is closed: hydroottawa.com returns 404 for /developers, /api, /docs, /data, /openapi.json and /swagger.json; developers.hydroottawa.com does not resolve and developersdev.hydroottawa.com answers HTTP 530 through Cloudflare; api.hydroottawa.com exists but returns 403 at root and 404 on every path; the github.com/hydroottawa organization has existed since 2015 with zero public repositories; and the City of Ottawa open data portal carries 682 datasets, none of them Hydro Ottawa''s. The one genuinely open, anonymous, machine-readable feed carrying Hydro Ottawa data — live outage counts under the KUBRA StormCenter instance behind outages.hydroottawa.com — is undocumented vendor infrastructure that Hydro
  Ottawa does not publish as a product, and it is deliberately not listed as an API here. Hydro Ottawa is therefore a utility with a mandated consumer data API it does not document, and no open market data at all.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Hydro Ottawa
nav: Providers
network: true
overview: 'Hydro Ottawa publishes 1 API on the [APIs.io](https://apis.io/) network: Green Button Connect My Data (CMD) API. Tagged areas include Energy, Canada, Ontario, Utilities, and Electricity.


  Hydro Ottawa''s developer surface includes authentication, getting-started guide, signup flow, engineering blog, documentation, support, YouTube channel, and 22 more developer resources.'
random_paper: 59
scopes:
- name: Hydro Ottawa Scopes
  scope_count: 0
  slug: hydro-ottawa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.9
  delta: -6.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 11.5
    developer_ergonomics: 30.4
    discoverability: 77.8
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 35.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/hydro-ottawa/refs/heads/main/screenshots/hydro-ottawa-2026-08-07T170509.png
security:
- kind: authentication
  name: Hydro Ottawa Authentication
  slug: hydro-ottawa-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hydro Ottawa Domain Security
  slug: hydro-ottawa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hydro-ottawa
tags:
- Energy
- Canada
- Ontario
- Utilities
- Electricity
- Electricity Distribution
- Smart Metering
- Green Button
- ESPI
- Municipal Utility
- Renewables
- Hydroelectric
- Solar
- Demand Response
- Grid
website: https://hydroottawa.com/
---
