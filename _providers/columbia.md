---
access_model:
  confidence: high
  label: Partly open, mostly affiliation-gated
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - agentic-access
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Columbia Agentic Access
  operation_count: 0
  slug: columbia-agentic-access
  summary_line: 0 operations
api_count: 1
apis:
- description: 'Columbia University Information Technology operates the university''s own identity infrastructure: a production Shibboleth Identity Provider publishing signed SAML 2.0 metadata anonymously under the In'
  name: Columbia Identity — Shibboleth IdP and CAS
  slug: identity
- description: Columbia University Libraries publishes its full catalogue — bibliographic and holdings records from the integrated library system behind CLIO — as gzipped MARCXML bulk extracts under a CC0 1.0 Public
  name: CLIO Library Catalog Open Data
  slug: clio-opendata
- description: 'The central university service publishing data feeds to software developers in programming-friendly formats such as JSON and XML — the course directory, the CLIO library catalogue and building access '
  name: Columbia Open Data Service
  slug: opendata
- description: 'The public web directory of Columbia University class offerings, browsable by subject, department, semester, instruction method, weekday and start time. Live and fully readable, and HTML only — there '
  name: CU Directory of Classes
  slug: directory-of-classes
- description: 'Columbia University''s institutional research repository, holding the scholarly output, theses and research data of the university. Unusually for this cohort it is NOT a vendor tenancy: it runs on Hyra'
  name: Columbia Academic Commons
  slug: academic-commons
- description: 'Columbia University Libraries'' digital collections platform and the resolution target for Columbia''s own DOI namespace. Columbia is a registered DataCite repository client (CUL.COLUMBIA, active since '
  name: Digital Library Collections and the 10.7916 DOI namespace
  slug: dlc
- description: The Climate Data Library run by the International Research Institute for Climate and Society and the Lamont-Doherty Earth Observatory, both Columbia University units. A long-running research-computing
  name: IRI/LDEO Climate Data Library
  slug: iri-data-library
- description: Columbia's learning management system. The REST API is live and returns a well-structured JSON 401 to unauthenticated callers, and the LTI 1.3 tool-platform JWKS is publicly readable — the best-formed
  name: CourseWorks (Instructure Canvas)
  slug: courseworks
- description: Columbia's research data platform runs on Redivis as an institution-specific tenancy, and the university has registered two distinct DataCite repository clients against it — CUL.CUIT "Columbia Univers
  name: Columbia University Data Platform (Redivis)
  slug: redivis
- baseURL: https://hours.library.columbia.edu/api/v1
  baseurl_source: declared
  description: Library locations and their posted opening hours.
  name: Columbia University Locations API
  slug: columbia-locations-api
artifact_total: 27
common:
- group: company
  title: ''
  type: Website
  url: https://www.columbia.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opendataservice.columbia.edu/
- group: other
  title: ''
  type: OpenData
  url: https://library.columbia.edu/bts/clio-data.html
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.columbia.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://doc.sis.columbia.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.columbia.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://iridl.ldeo.columbia.edu/
- group: auth
  title: ''
  type: Authentication
  url: https://www.cuit.columbia.edu/web-authentication-federation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cul
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/columbia-it
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/columbia-university/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/columbia-library-hours-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/columbia-library-hours-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
- group: design
  title: ''
  type: Rules
  url: rules/columbia-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/columbia-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/columbia-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: authentication/columbia-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/columbia-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/columbia-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/columbia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/columbia-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/columbia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/columbia-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/columbia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/columbia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/columbia-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Columbia University is a private Ivy League research university in New York City, ranked seventeenth in the QS World University Rankings. Its programmable footprint is small, real, and almost entirely invisible from the outside. Columbia operates exactly one publicly consumable, unauthenticated API of its own: the Columbia University Libraries Hours API at hours.library.columbia.edu, two read operations returning JSON with CORS enabled, built on Columbia''s own openly published Rails codebase and documented by nobody. Alongside it the university runs a production Shibboleth Identity Provider that publishes signed SAML 2.0 metadata under the InCommon entityID urn:mace:incommon:columbia.edu, mints DOIs under its own DataCite prefix 10.7916 across 1.1 million registered identifiers, deposits into Crossref as member 6984, and releases the entire CLIO library catalogue as CC0 MARCXML bulk extracts. That is the whole of it. The Open Data Service that Columbia describes as its developer-facing
  service is gated behind a UNI login, and the IRI/LDEO Climate Data Library now redirects its data paths to a login form. Columbia publishes no OpenAPI, no developer portal reachable without affiliation, no changelog, no llms.txt and no API terms, and it reserves the hostname api.library.columbia.edu while serving nothing but a placeholder there. Most consequentially for machine access, Columbia defends its estate with two different anti-bot products: a Cloudflare managed challenge across the central web estate, and an Anubis proof-of-work challenge in front of the Libraries'' entire discovery layer — the CLIO catalogue, Academic Commons and GeoData — which returns HTTP 200 with a bot-check body and made the institution''s OAI-PMH endpoint unverifiable. Learning management runs on Instructure''s Canvas and the research data platform on Redivis; both are tenant relationships, recorded as such and scored against their vendors.'
examples:
- key_count: 4
  name: Columbia Crossref Member Example
  slug: columbia-crossref-member-example
- key_count: 1
  name: Columbia Datacite Client Example
  slug: columbia-datacite-client-example
- key_count: 2
  name: Columbia Library Hours Error 400 Example
  slug: columbia-library-hours-error-400-example
- key_count: 2
  name: Columbia Library Hours Error 404 Example
  slug: columbia-library-hours-error-404-example
- key_count: 1
  name: Columbia Library Hours Location Day Example
  slug: columbia-library-hours-location-day-example
- key_count: 1
  name: Columbia Library Hours Location Range Example
  slug: columbia-library-hours-location-range-example
- key_count: 1
  name: Columbia Library Hours Open Now Example
  slug: columbia-library-hours-open-now-example
finops:
- name: Columbia Finops
  service_category: Education
  slug: columbia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/columbia.png
json_schemas:
- name: Columbia University Libraries Hours API response schemas
  property_count: 0
  slug: columbia-library-hours
jsonld:
- class_count: 8
  name: Columbia Context
  property_count: 3
  slug: columbia-context
layout: provider
modified: '2026-08-19'
name: Columbia University
nav: Providers
network: true
overview: 'Columbia University publishes 1 API on the [APIs.io](https://apis.io/) network: Locations API. Tagged areas include University, Higher Education, Education, Ivy League, and Private Research University.


  The Columbia University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Columbia University''s developer surface includes authentication, code examples, and 26 more developer resources.'
plans:
- name: Columbia Plans Pricing
  plan_count: 2
  slug: columbia-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Columbia Rate Limits
  slug: columbia-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Columbia University API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: columbia-rules
scopes:
- name: Columbia Scopes
  scope_count: 0
  slug: columbia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 3.8
    contract_quality: 69.0
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 3.8
    operational_transparency: 23.7
  previous_composite: 44.7
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/columbia/refs/heads/main/screenshots/columbia-2026-06-20T174808.png
security:
- kind: authentication
  name: Columbia Authentication
  slug: columbia-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Columbia Domain Security
  slug: columbia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: columbia
tags:
- University
- Higher Education
- Education
- Ivy League
- Private Research University
- United States
- New York
- Identity Federation
- Library
- Open Data
- Research Repository
- Research Data
- Course Catalog
- Campus Life
website: https://www.columbia.edu/
---
