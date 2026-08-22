---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Ferc Agentic Access
  operation_count: 18
  slug: ferc-agentic-access
  summary_line: 18 operations · 2 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: FERC's public open data API, serving the same data assets and datasets published in the data.ferc.gov Data Catalog. A Data-Assets endpoint returns the catalog and the dataset IDs; Details, Data, and D
  name: FERC Open Data API
  slug: ferc-open-data-api
- description: The machine-to-machine API behind FERC's mandated eForms. Credentialed filers exchange their FERC eRegistration and Company Registration username and password for a bearer token at POST /api/token (OA
  name: FERC eForms XBRL Submission API
  slug: ferc-eforms-xbrl-submission-api
arazzos:
- description: 'The full happy path against the FERC Open Data API: list the catalog, resolve a dataset ID from the nested data-sets array, read its metadata and record count, fetch the column dictionary so the rows '
  name: FERC open data — discover a dataset and retrieve it
  slug: ferc-dataset-discovery-and-retrieval
artifact_total: 10
collections:
- collection_type: open
  name: API Endpoints
  slug: open-ferc-data-api
- collection_type: open
  name: FERC eForms (eCollection) API
  slug: open-ferc-eforms-api-openapi-derived
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ferc-data-api-openapi.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ferc-eforms-api-openapi-derived.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ferc-data-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ferc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ferc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ferc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ferc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ferc-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/ferc-data-api-examples.yml
- group: build
  title: ''
  type: Examples
  url: examples/ferc-eforms-api-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ferc-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ferc-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ferc-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ferc-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ferc-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ferc-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://data.ferc.gov/developer/apiendpoints/
- group: build
  title: ''
  type: Packages
  url: packages/ferc-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ferc-dataset-discovery-and-retrieval.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ferc-llms.txt
- group: build
  title: ''
  type: Postman
  url: collections/ferc-xbrl-submission-api.postman_collection.json
- group: company
  title: ''
  type: Website
  url: https://www.ferc.gov
- group: start
  title: ''
  type: Portal
  url: https://data.ferc.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://data.ferc.gov/developer/gettingstarted/
- group: docs
  title: ''
  type: APIReference
  url: https://data.ferc.gov/developer/apiendpoints/
- group: start
  title: ''
  type: GettingStarted
  url: https://data.ferc.gov/developer/gettingstarted/understanding-our-apis/
- group: other
  title: ''
  type: DataCatalog
  url: https://data.ferc.gov/datacatalog/
- group: start
  title: ''
  type: SignUp
  url: https://data.ferc.gov/developer/gettingstarted/sign-up-form/
- group: auth
  title: ''
  type: Authentication
  url: https://data.ferc.gov/developer/gettingstarted/api-key-usage/
- group: operate
  title: ''
  type: RateLimits
  url: https://data.ferc.gov/developer/gettingstarted/api-key-usage/
- group: operate
  title: ''
  type: Support
  url: https://data.ferc.gov/developer/helpandsupport/
- group: operate
  title: ''
  type: FAQ
  url: https://data.ferc.gov/developer/helpandsupport/api-faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.ferc.gov/disclaimer/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ferc.gov/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.ferc.gov/media/ferc-vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ferc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.ferc.gov/vulnerability-disclosure-policy
- group: other
  title: ''
  type: Strategy
  url: https://www.ferc.gov/about/what-ferc/digital-strategy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-energy-regulatory-commission
- group: docs
  title: ''
  type: Documentation
  url: https://www.ferc.gov/ferc-online/elibrary
- group: docs
  title: ''
  type: Documentation
  url: https://www.ferc.gov/power-sales-and-markets/electric-quarterly-reports-eqr
created: '2026-07-27'
description: The Federal Energy Regulatory Commission (FERC) is the independent United States federal agency that regulates the interstate transmission of electricity, natural gas, and oil, licenses hydropower projects, and oversees the wholesale power markets run by the seven ISOs and RTOs. FERC sits on the wholesale side of the US energy value chain — it does not regulate retail utility service, retail rates, or the customer relationship, which remain with the fifty state public utility commissions. That jurisdictional line defines FERC's API posture exactly. FERC operates a real, self-serve open data API at api.data.ferc.gov, documented at data.ferc.gov with a published OpenAPI 3.0 description, a free 40-character API key issued from a sign-up form, a 1,000-request-per-hour rate limit, and X-Api-Key header or api_key query authentication on the api.data.gov API Umbrella stack — genuinely open market and regulatory data covering the Market-Based Rate Database, FERC Form No. 552 natural
  gas transactions, FERC Form 556 qualifying facility certifications, Company Registration, Annual Charges, Information Collections Management, and the NEPA infrastructure schedule. FERC also runs a credentialed OAuth2 XBRL submission API at ecollection.ferc.gov for the mandated eForms filings (Form Nos. 1, 2, 3-Q, 6, 60, 552, 714). What FERC does NOT do is any part of consumer energy data — there is no Green Button, no ESPI, no consumer data right, and no individual customer usage or billing API anywhere in FERC's surface, because retail customer data is outside its statutory reach. FERC is therefore an open-market-data, zero-consumer-data regulator, and it publishes a better documented API than most of the utilities it indirectly touches.
image: https://ecollection.ferc.gov/assets/images/ferc-logo/ferc%20logo.png
layout: provider
modified: '2026-07-27'
name: FERC
nav: Providers
network: true
overview: 'FERC publishes 2 APIs on the [APIs.io](https://apis.io/) network: Open Data API and eForms XBRL Submission API. Tagged areas include Energy, United States, Energy Markets, Electricity, and Natural Gas.


  FERC''s developer surface includes authentication, code examples, changelog, sandbox, developer console, developer portal, documentation, and 35 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Ferc Rate Limits
  slug: ferc-rate-limits
score:
  band: developing
  composite: 51.5
  delta: 7.8
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 32.4
    developer_ergonomics: 68.5
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 47.4
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 1
      marker_coverage: 50.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 59.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ferc/refs/heads/main/screenshots/ferc-2026-08-07T165243.png
security:
- kind: authentication
  name: Ferc Authentication
  slug: ferc-authentication
  summary_line: apiKey/oauth2/http · 4 schemes
- kind: domain-security
  name: Ferc Domain Security
  slug: ferc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ferc Vulnerability Disclosure
  slug: ferc-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: ferc
tags:
- Energy
- United States
- Energy Markets
- Electricity
- Natural Gas
- Grid
- Regulator
- Government
- Open Data
- Wholesale Power Markets
- Hydropower
- Oil Pipelines
website: https://www.ferc.gov
---
