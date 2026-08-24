---
access_model:
  confidence: high
  label: Free · No registration for the institution-operated public APIs
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cornell Agentic Access
  operation_count: 11
  slug: cornell-agentic-access
  summary_line: 11 operations
api_count: 6
apis:
- description: 'Public, read-only API (version 2.0) for Cornell Class Roster data: scheduled classes with Course of Study detail, plus configuration lookups for rosters, academic careers, academic groups, class level'
  name: Cornell Class Roster API
  slug: class-roster
- description: JSON search over Cornell University Library's catalog. The catalog is the library's own Blacklight deployment; appending .json to any catalog route returns a Solr-backed JSON envelope, and an OpenSear
  name: Cornell University Library Catalog Search API
  slug: library-catalog
- description: JSON:API search and record retrieval for CUGIR, Cornell University Library's geospatial data and historical map repository, running GeoBlacklight on the library's own infrastructure. Records carry Ope
  name: CUGIR — Cornell University Geospatial Information Repository API
  slug: cugir
- description: 'Global bird-observation API run by the Cornell Lab of Ornithology, a unit of Cornell University. Free but token-gated: requests without a valid X-eBirdApiToken return 403. Reference documentation is p'
  name: eBird API 2.0
  slug: ebird
- description: 'eCommons is Cornell University Library''s institutional repository: Cornell''s content, Cornell''s DOIs, Cornell''s host. The interface is not Cornell''s engineering. It runs DSpace 8.2 on a 4Science-manag'
  name: eCommons Institutional Repository (DSpace REST + OAI-PMH) — tenant
  slug: ecommons
- description: 'The Cornell events calendar at events.cornell.edu answers a live JSON API at /api/2/events, and the data is Cornell''s. The platform is Localist (Concept3D): the response headers carry x-slzr-platform:'
  name: Cornell Events Calendar API (Localist) — tenant
  slug: events-calendar
artifact_total: 22
common:
- group: company
  title: ''
  type: Website
  url: https://www.cornell.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://classes.cornell.edu/content/FA26/api-details
- group: docs
  title: ''
  type: APIReference
  url: https://classes.cornell.edu/content/FA26/api-details
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cul
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cornell-data
- group: learn
  title: ''
  type: CourseCatalog
  url: https://classes.cornell.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalog.library.cornell.edu/catalog.json?q=cornell&search_field=all_fields
- group: other
  title: ''
  type: ResearchRepository
  url: https://ecommons.cornell.edu/
- group: other
  title: ''
  type: OpenData
  url: https://cugir.library.cornell.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibidp.cit.cornell.edu/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/https:%2F%2Fshibidp.cit.cornell.edu%2Fidp%2Fshibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.cac.cornell.edu/services/
- group: other
  title: ''
  type: AIPolicy
  url: https://it.cornell.edu/ai/ai-guidelines
- group: build
  title: ''
  type: AITooling
  url: https://it.cornell.edu/tags/ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.cornell.edu/university-privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.cornell.edu/
- group: operate
  title: ''
  type: Support
  url: https://it.cornell.edu/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/cornell-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/cornell-education-standards-conformance.yml
- group: design
  title: ''
  type: Errors
  url: errors/cornell-errors.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cornell-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cornell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cornell-authentication.yml
- group: design
  title: ''
  type: Rules
  url: rules/cornell-rules.yml
- group: design
  title: ''
  type: Rules
  url: rules/cornell-jsonschema-spectral-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cornell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cornell-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cornell-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Cornell University is a private Ivy League and statutory land-grant research university in Ithaca, New York. It operates no central developer portal, no API gateway and no published API program, and this profile records that plainly. What it does operate, directly and on its own hosts, is a small set of real machine-readable surfaces: the Class Roster API on classes.cornell.edu (public, read-only, version 2.0, maintained behind the scenes by the Office of the University Registrar), the Cornell University Library''s self-hosted Blacklight catalog and CUGIR geospatial repository, both of which answer JSON on every route, its own Shibboleth identity provider published as SAML 2.0 metadata and registered with InCommon/eduGAIN, and — through the Cornell Lab of Ornithology — the token-gated eBird API 2.0. Everything else that looks like a Cornell API belongs to somebody else: the events calendar at events.cornell.edu is a Localist tenancy, eCommons is a 4Science-managed DSpace instance,
  and arXiv, hosted at Cornell for twenty-five years, spun out as an independent nonprofit on 2026-07-01 and is no longer a Cornell surface at all. The Cornell Open Data Initiative specs that once padded this profile described a dining API, a campus-map API and a Cornell Days API that are all dead as of 2026-08-19.'
examples:
- key_count: 3
  name: Cornell Class Roster Rosters Example
  slug: cornell-class-roster-rosters-example
- key_count: 3
  name: Cornell Ecommons Dspace Root Example
  slug: cornell-ecommons-dspace-root-example
- key_count: 3
  name: Cornell Library Catalog Search Example
  slug: cornell-library-catalog-search-example
- key_count: 3
  name: Cornell Search Classes Example
  slug: cornell-search-classes-example
- key_count: 3
  name: Cugir Record Example
  slug: cugir-record-example
finops:
- name: Cornell Finops
  service_category: Education
  slug: cornell-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cornell.png
json_schemas:
- name: Cornell Class
  property_count: 23
  slug: cornell-class
json_structures:
- name: Cornell Class Structure
  property_count: 14
  slug: cornell-class-structure
jsonld:
- class_count: 18
  name: Cornell Context
  property_count: 0
  slug: cornell-context
layout: provider
modified: '2026-08-19'
name: Cornell University
nav: Providers
network: true
overview: 'Cornell University publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cornell Class Roster API, Library Catalog Search API, and CUGIR — Cornell University Geospatial Information Repository API. Tagged areas include University, Higher Education, Education, Ivy League, and United States.


  The Cornell University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cornell University''s developer surface includes documentation, API reference, support, authentication, and 25 more developer resources.'
plans:
- name: Cornell Plans Pricing
  plan_count: 2
  slug: cornell-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Cornell Rate Limits
  slug: cornell-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cornell University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cornell-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Cornell University API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: cornell-rules
score:
  band: thin
  composite: 34.9
  delta: -2.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 22.7
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 23.7
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/screenshots/cornell-2026-06-20T175031.png
security:
- kind: authentication
  name: Cornell Authentication
  slug: cornell-authentication
  summary_line: none/apiKey/saml · 6 schemes
- kind: domain-security
  name: Cornell Domain Security
  slug: cornell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cornell
tags:
- University
- Higher Education
- Education
- Ivy League
- United States
- Course Catalog
- Library
- Research Data
- Geospatial
- Identity Federation
website: https://www.cornell.edu/
---
