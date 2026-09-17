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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cornell Agentic Access
  operation_count: 11
  slug: cornell-agentic-access
  summary_line: 11 operations
api_count: 2
apis:
- baseURL: https://catalog.library.cornell.edu
  baseurl_source: declared
  description: JSON search over Cornell University Library's catalog. The catalog is the library's own Blacklight deployment; appending .json to any catalog route returns a Solr-backed JSON envelope, and an OpenSear
  name: Cornell University Library Catalog Search API
  slug: library-catalog
- description: 'Global bird-observation API run by the Cornell Lab of Ornithology, a unit of Cornell University. Free but token-gated: requests without a valid X-eBirdApiToken return 403. Reference documentation is p'
  name: eBird API 2.0
  slug: ebird
- description: 'eCommons is Cornell University Library''s institutional repository: Cornell''s content, Cornell''s DOIs, Cornell''s host. The interface is not Cornell''s engineering. It runs DSpace 8.2 on a 4Science-manag'
  name: eCommons Institutional Repository (DSpace REST + OAI-PMH) — tenant
  slug: ecommons
- description: 'The Cornell events calendar at events.cornell.edu answers a live JSON API at /api/2/events, and the data is Cornell''s. The platform is Localist (Concept3D): the response headers carry x-slzr-platform:'
  name: Cornell Events Calendar API (Localist) — tenant
  slug: events-calendar
- baseURL: https://classes.cornell.edu/api/2.0
  baseurl_source: declared
  description: Search and retrieve Cornell geospatial datasets and historical maps.
  name: Cornell University Cugir API
  slug: cornell-cugir-api
- baseURL: https://classes.cornell.edu/api/2.0
  baseurl_source: declared
  description: The config API from Cornell University — 5 operation(s) for config.
  name: Cornell University Config API
  slug: cornell-config-api
- baseURL: https://classes.cornell.edu/api/2.0
  baseurl_source: declared
  description: The search API from Cornell University — 1 operation(s) for search.
  name: Cornell University Search API
  slug: cornell-search-api
artifact_total: 23
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
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/conformance/cornell-education-standards-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cornell-education-standards-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/errors/cornell-errors.yml
  title: ''
  type: Errors
  url: errors/cornell-errors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/agentic-access/cornell-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cornell-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/security/cornell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cornell-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/authentication/cornell-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cornell-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/rules/cornell-rules.yml
  title: ''
  type: Rules
  url: rules/cornell-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/rules/cornell-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/cornell-jsonschema-spectral-rules.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/plans/cornell-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cornell-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/rate-limits/cornell-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cornell-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/finops/cornell-finops.yml
  title: ''
  type: FinOps
  url: finops/cornell-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/review.yml
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
overview: 'Cornell University publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Library Catalog Search API, Cugir API, Config API, and 1 more. Tagged areas include University, Higher Education, Education, Ivy League, and United States.


  The Cornell University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cornell University''s developer surface includes documentation, API reference, support, authentication, and 25 more developer resources.'
plans:
- name: Cornell Plans Pricing
  plan_count: 2
  slug: cornell-plans-pricing
random_paper: 3
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
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 75.8
    catalog_earned_first_party: 8.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.6
  facets:
    access_clarity: 50.0
    contract_governance: 17.4
    contract_quality: 44.6
    developer_ergonomics: 21.4
    discoverability: 68.5
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 50.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
