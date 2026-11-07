---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Ferc Agentic Access
  operation_count: 18
  slug: ferc-agentic-access
  summary_line: 18 operations · 2 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.data.ferc.gov/v1
  baseurl_source: declared
  description: The Data API from FERC — 1 operation(s) for data.
  name: FERC Data API
  slug: ferc-data-api
- baseURL: https://api.data.ferc.gov/v1
  baseurl_source: declared
  description: The Data-Assets API from FERC — 1 operation(s) for data-assets.
  name: FERC Data Assets API
  slug: ferc-data-assets-api
- baseURL: https://api.data.ferc.gov/v1
  baseurl_source: declared
  description: The Details API from FERC — 1 operation(s) for details.
  name: FERC Details API
  slug: ferc-details-api
- baseURL: https://api.data.ferc.gov/v1
  baseurl_source: declared
  description: The Dictionary API from FERC — 1 operation(s) for dictionary.
  name: FERC Dictionary API
  slug: ferc-dictionary-api
- baseURL: https://api.data.ferc.gov/v1
  baseurl_source: declared
  description: Credentialed machine-to-machine submission of XBRL filings.
  name: FERC Filing API
  slug: ferc-filing-api
- baseURL: https://api.data.ferc.gov/v1
  baseurl_source: declared
  description: Anonymous read access to the public FERC eForms submission record.
  name: FERC Public Filings API
  slug: ferc-public-filings-api
- baseURL: https://api.data.ferc.gov/v1
  baseurl_source: declared
  description: Form lists and submission constraints.
  name: FERC Reference API
  slug: ferc-reference-api
- baseURL: https://api.data.ferc.gov/v1
  baseurl_source: declared
  description: XBRL taxonomy versions, packages and sample forms for the FERC eForms.
  name: FERC Taxonomy API
  slug: ferc-taxonomy-api
arazzos:
- description: 'The full happy path against the FERC Open Data API: list the catalog, resolve a dataset ID from the nested data-sets array, read its metadata and record count, fetch the column dictionary so the rows '
  name: FERC open data — discover a dataset and retrieve it
  slug: ferc-dataset-discovery-and-retrieval
artifact_total: 25
collections:
- collection_type: open
  name: API Endpoints
  slug: open-ferc-data-api
- collection_type: open
  name: FERC eForms (eCollection) API
  slug: open-ferc-eforms-api-openapi-derived
common:
- group: design
  href: https://artifacts.apis.io/ferc/rules/ferc-rules.yml
  title: ''
  type: Spectral
  url: rules/ferc-rules.yml
- group: design
  href: https://artifacts.apis.io/ferc/json-ld/ferc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ferc-context.jsonld
- group: design
  href: https://artifacts.apis.io/ferc/vocabulary/ferc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ferc-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/ferc/lifecycle/ferc-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ferc-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/ferc/hosts/ferc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ferc-hosts.yml
- group: other
  href: https://artifacts.apis.io/ferc/vendors/ferc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ferc-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.ferc.gov/news-events/news/decisions-notices?new=
- group: docs
  href: https://artifacts.apis.io/ferc/openapi/_original/ferc-data-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/ferc-data-api-openapi.json
- group: docs
  href: https://artifacts.apis.io/ferc/openapi/_ae-authored/ferc-eforms-api-openapi-derived.yml
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/ferc-eforms-api-openapi-derived.yml
- group: other
  href: https://artifacts.apis.io/ferc/overlays/ferc-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ferc-data-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ferc/agentic-access/ferc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ferc-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ferc/security/ferc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ferc-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ferc/authentication/ferc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ferc-authentication.yml
- group: design
  href: https://artifacts.apis.io/ferc/conventions/ferc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ferc-conventions.yml
- group: design
  href: https://artifacts.apis.io/ferc/errors/ferc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ferc-problem-types.yml
- group: build
  href: https://artifacts.apis.io/ferc/examples/ferc-data-api-examples.yml
  title: ''
  type: Examples
  url: examples/ferc-data-api-examples.yml
- group: build
  href: https://artifacts.apis.io/ferc/examples/ferc-eforms-api-examples.yml
  title: ''
  type: Examples
  url: examples/ferc-eforms-api-examples.yml
- group: operate
  href: https://artifacts.apis.io/ferc/rate-limits/ferc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ferc-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ferc/lifecycle/ferc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ferc-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ferc/changelog/ferc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ferc-changelog.yml
- group: design
  href: https://artifacts.apis.io/ferc/data-model/ferc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ferc-data-model.yml
- group: design
  href: https://artifacts.apis.io/ferc/conformance/ferc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ferc-conformance.yml
- group: start
  href: https://artifacts.apis.io/ferc/sandbox/ferc-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ferc-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://data.ferc.gov/developer/apiendpoints/
- group: agent
  href: https://artifacts.apis.io/ferc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ferc/arazzo/ferc-dataset-discovery-and-retrieval.yml
  title: ''
  type: Arazzo
  url: arazzo/ferc-dataset-discovery-and-retrieval.yml
- group: build
  href: https://artifacts.apis.io/ferc/collections/ferc-xbrl-submission-api.postman_collection.json
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
  href: https://artifacts.apis.io/ferc/security/ferc-vulnerability-disclosure.yml
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
json_schemas:
- name: FormList
  property_count: 3
  slug: ferc-form-list
- name: PublicSubmission
  property_count: 11
  slug: ferc-public-submission
- name: SubmissionDetail
  property_count: 7
  slug: ferc-submission-detail
- name: TaxonomyVersion
  property_count: 11
  slug: ferc-taxonomy-version
- name: TestStatus
  property_count: 6
  slug: ferc-test-status
jsonld:
- class_count: 6
  name: Ferc Context
  property_count: 38
  slug: ferc-context
layout: provider
modified: '2026-09-16'
name: FERC
nav: Providers
network: true
overview: 'FERC publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data API, Data Assets API, Details API, and 5 more. Tagged areas include Energy, United States, Energy Markets, Electricity, and Natural Gas.


  The FERC catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FERC''s developer surface includes authentication, code examples, changelog, sandbox, developer console, developer portal, documentation, and 40 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 1
  name: Ferc Rate Limits
  slug: ferc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: FERC API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ferc-rules
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 47.3
    developer_ergonomics: 64.9
    discoverability: 67.0
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 55.6
      derived: 5
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 36.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ferc/ferc-2026-08-07T165243.png
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
skill_count: 2
skills:
- name: ferc-retrieve-open-data-dataset
  slug: ferc-retrieve-open-data-dataset
- name: ferc-track-eforms-taxonomy
  slug: ferc-track-eforms-taxonomy
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
