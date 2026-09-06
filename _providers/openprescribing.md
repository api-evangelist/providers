---
access_model:
  confidence: high
  label: Free · Open public API · No registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - documentation
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openprescribing Agentic Access
  operation_count: 19
  slug: openprescribing-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://openprescribing.net/api/1.0
  baseurl_source: declared
  description: Retrieve total prescribing spending, quantity and items across the last five years of the English Prescribing Dataset — by BNF code (section, chemical or presentation) and by NHS organisation (practic
  name: OpenPrescribing Spending API
  slug: openprescribing-spending-api
- baseURL: https://openprescribing.net/api/1.0
  baseurl_source: declared
  description: Standardised NHS prescribing-quality and safety measures (numerators, denominators and calculated values) at national, Regional Team, ICB, Sub-ICB Location, PCN and practice level. These endpoints pow
  name: OpenPrescribing Measures API
  slug: openprescribing-measures-api
- description: Reference-data lookups for the prescribing dataset — search BNF sections, chemicals and presentations by name or code; look up NHS organisations (Sub-ICB Location or practice) by code or name; retriev
  name: OpenPrescribing Information API
  slug: openprescribing-information-api
- baseURL: https://openprescribing.net/api/1.0
  baseurl_source: declared
  description: Standardised NHS prescribing-quality and safety measures.
  name: OpenPrescribing Measures API
  slug: openprescribing-measures-api
- baseURL: https://openprescribing.net/api/1.0
  baseurl_source: declared
  description: BNF code, organisation code and organisation-location reference lookups.
  name: OpenPrescribing Reference API
  slug: openprescribing-reference-api
- baseURL: https://openprescribing.net/api/1.0
  baseurl_source: declared
  description: Prescribing spending, quantity and item counts by BNF code and organisation.
  name: OpenPrescribing Spending API
  slug: openprescribing-spending-api
- baseURL: https://openprescribing.net/api/1.0
  baseurl_source: declared
  description: Drug-tariff prices and price-per-unit / ghost-generic savings data.
  name: OpenPrescribing Tariff API
  slug: openprescribing-tariff-api
artifact_total: 11
collections:
- collection_type: open
  name: OpenPrescribing API
  slug: open-openprescribing
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bennettoxford/openprescribing/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bennettoxford/openprescribing/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/bennettoxford/openprescribing/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openprescribing-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openprescribing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openprescribing.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openprescribing.net/api/
- group: docs
  title: ''
  type: Documentation
  url: https://openprescribing.net/api/
- group: docs
  title: ''
  type: APIReference
  url: https://openprescribing.net/api/
- group: company
  title: ''
  type: About
  url: https://openprescribing.net/about/
- group: operate
  title: ''
  type: Support
  url: https://openprescribing.net/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bennettoxford
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bennettoxford/openprescribing
- group: company
  title: ''
  type: Blog
  url: https://www.bennett.ox.ac.uk/openprescribing/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://openprescribing.net/api/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/openprescribing-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openprescribing-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openprescribing-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openprescribing-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openprescribing-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openprescribing-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openprescribing-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openprescribing-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/openprescribing-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openprescribing-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/openprescribing-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: OpenPrescribing.net is an open-data service built and operated by the Bennett Institute for Applied Data Science at the University of Oxford. It turns the English Prescribing Dataset published monthly by the NHS Business Services Authority into public dashboards, prescribing-safety measures, and a free RESTful API covering primary-care GP prescribing across England. The API exposes spending, quantity and item counts by BNF code and by NHS organisation (practice, PCN, Sub-ICB Location, ICB, Regional Team), standardised prescribing measures, drug-tariff and price-per-unit data, and organisation reference/boundary lookups, all returned as JSON, CSV or GeoJSON. Home market is the United Kingdom (England prescribing data). It is an independent academic analytics platform layered on NHS open data, not an NHS FHIR clinical system; there is no OAuth, no SMART-on-FHIR, and currently no registration or API key is required.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: OpenPrescribing
nav: Providers
network: true
overview: 'OpenPrescribing publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Spending API, Measures API, and 4 more. Tagged areas include Healthcare, United Kingdom, NHS, Prescribing, and Pharmacy.


  OpenPrescribing''s developer surface includes documentation, API reference, support, engineering blog, getting-started guide, authentication, and 21 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 50.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  open_source:
    applies: true
    score: 25.0
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openprescribing/refs/heads/main/screenshots/openprescribing-2026-08-07T190634.png
security:
- kind: authentication
  name: Openprescribing Authentication
  slug: openprescribing-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Openprescribing Domain Security
  slug: openprescribing-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openprescribing
tags:
- Healthcare
- United Kingdom
- NHS
- Prescribing
- Pharmacy
- Open Data
- Primary Care
- Public Health
- Analytics
website: https://openprescribing.net/
---
