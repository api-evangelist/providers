---
access_model:
  confidence: high
  label: Free · Registration required for Project Tycho, none for the rest
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - openapi
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Project Tycho is an open-access repository for global health surveillance data, built and run at the University of Pittsburgh and served from www.tycho.pitt.edu. It holds case counts for 78 notifiable
  name: Project Tycho API
  slug: project-tycho
- description: WPRDC is a regional open data portal led by the University Center for Social and Urban Research (UCSUR) at the University of Pittsburgh, in partnership with Allegheny County and the City of Pittsburgh
  name: Western Pennsylvania Regional Data Center (WPRDC) CKAN API
  slug: wprdc-ckan
- description: The University Library System publishes dozens of open-access journals on PKP Open Journal Systems that ULS self-hosts, each with a conformant OAI-PMH 2.0 provider on a pitt.edu host. anthro-age.pitt.
  name: ULS E-Journal Publishing — OAI-PMH 2.0 providers
  slug: uls-ejournal-oai
- description: The University of Pittsburgh's campus-wide single sign-on identity provider. Its SAML 2.0 metadata is publicly readable at the canonical Shibboleth /idp/shibboleth location, declares the shibmd namesp
  name: Pitt Passport (Shibboleth SAML 2.0 Identity Provider)
  slug: pitt-passport-idp
- description: D-Scholarship@Pitt is the University Library System's institutional repository of research and scholarly output. The content, the collections and the DataCite DOIs are Pitt's; the platform and the OAI
  name: D-Scholarship@Pitt Institutional Repository (Hyku Commons) — tenant
  slug: d-scholarship-oai
- description: PittAPI is an unofficial, community-maintained Python library published by the Pitt Computer Science Club that scrapes University of Pittsburgh web sources for courses, dining, library, news, laundry,
  name: PittAPI (Pitt Computer Science Club) — student-built
  slug: pittapi
artifact_total: 18
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/pittcsc/PittAPI/blob/dev/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.pitt.edu
- group: docs
  title: ''
  type: Documentation
  url: https://www.tycho.pitt.edu/dataset/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.tycho.pitt.edu/dataset/api/
- group: other
  title: ''
  type: OpenData
  url: https://data.wprdc.org
- group: other
  title: ''
  type: OpenData
  url: https://data.wprdc.org/data.json
- group: other
  title: ''
  type: OpenData
  url: https://www.ucsur.pitt.edu/western-pennsylvania-regional-data-center-wprdc
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.library.pitt.edu/d-scholarship
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.cadb.pitt.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.library.pitt.edu/publishing-open-access
- group: build
  title: ''
  type: LibraryCatalog
  url: https://pittcat.pitt.edu
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.library.pitt.edu
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.upp.pitt.edu
- group: other
  title: ''
  type: IdentityFederation
  url: https://passport.pitt.edu/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/https%3A%2F%2Fpassport.pitt.edu%2Fidp%2Fshibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://crc.pitt.edu
- group: other
  title: ''
  type: AIPolicy
  url: https://www.technology.pitt.edu/ai
- group: build
  title: ''
  type: AITooling
  url: https://www.technology.pitt.edu/services/pitt-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ulsdevteam
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/University-of-Pittsburgh
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pittcsc/PittAPI
- group: operate
  title: ''
  type: Status
  url: https://status.pitt.edu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pitt.edu/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.technology.pitt.edu/help
- group: company
  title: ''
  type: Blog
  url: https://www.pitt.edu/pittwire
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-pittsburgh/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-pittsburgh-project-tycho-api-openapi.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-pittsburgh-education-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-pittsburgh-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-pittsburgh-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-pittsburgh-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-pittsburgh-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-pittsburgh-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-pittsburgh-project-tycho-data-row.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-pittsburgh-wprdc-ckan-action-envelope.json
- group: build
  title: ''
  type: Examples
  url: examples/university-of-pittsburgh-examples-manifest.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-pittsburgh-rules.yml
- group: design
  title: ''
  type: DataModel
  url: json-ld/university-of-pittsburgh-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-pittsburgh-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-pittsburgh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-pittsburgh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-pittsburgh-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Pittsburgh is a public research university in Pittsburgh, Pennsylvania, ranked #271 in the QS World University Rankings 2025. It operates no central developer portal, no API gateway and no institution-wide developer program — developer.pitt.edu and apis.pitt.edu do not resolve, and www.pitt.edu serves neither apis.json nor llms.txt. What it does operate is four unrelated machine-readable surfaces built by four different units that share no identifier, no envelope, no error model and no case convention: Project Tycho, a global epidemiological surveillance API at www.tycho.pitt.edu built in the Public Health Dynamics Laboratory; the Western Pennsylvania Regional Data Center, a CKAN 2.11.6 open data portal led by Pitt''s UCSUR in partnership with Allegheny County and the City of Pittsburgh; the University Library System''s E-Journal Publishing platform, a self-hosted PKP Open Journal Systems estate on ULS''s own machines serving conformant OAI-PMH 2.0 across
  dozens of journals and 14,470 Crossref-registered DOIs; and Pitt Passport, the campus Shibboleth SAML 2.0 identity provider registered in InCommon and eduGAIN. None of the four publishes an OpenAPI, a changelog, a deprecation policy or a status page, and Project Tycho serves a rejected credential with HTTP 200 and an HTML sentence. Two further surfaces carrying Pitt''s name are tenancies rather than Pitt''s engineering: D-Scholarship@Pitt is now a Hyku Commons tenant (d-scholarship.pitt.edu CNAMEs to pittir.hykucommons.org), and PittAPI is an unofficial library written by a student club. This profile was rebuilt on 2026-08-30 under the university pipeline, which settles who operates a surface before saving anything about it.'
examples:
- key_count: 11
  name: University Of Pittsburgh Project Tycho Requests
  slug: university-of-pittsburgh-project-tycho-requests
- key_count: 3
  name: University Of Pittsburgh Wprdc Ckan Status Show
  slug: university-of-pittsburgh-wprdc-ckan-status-show
finops:
- name: University Of Pittsburgh Finops
  service_category: Education
  slug: university-of-pittsburgh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-pittsburgh.png
json_schemas:
- name: Project Tycho Pre-compiled Data Format v1.0 — surveillance row
  property_count: 19
  slug: university-of-pittsburgh-project-tycho-data-row
- name: WPRDC CKAN Action API response envelope
  property_count: 4
  slug: university-of-pittsburgh-wprdc-ckan-action-envelope
jsonld:
- class_count: 13
  name: University Of Pittsburgh Context
  property_count: 9
  slug: university-of-pittsburgh-context
layout: provider
modified: '2026-08-30'
name: University of Pittsburgh
nav: Providers
network: true
overview: 'University of Pittsburgh publishes 1 API on the [APIs.io](https://apis.io/) network: Project Tycho API. Tagged areas include University, Higher Education, Education, United States, and Public Research University.


  The University of Pittsburgh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Pittsburgh''s developer surface includes documentation, API reference, status page, support, engineering blog, authentication, code examples, and 36 more developer resources.'
plans:
- name: University Of Pittsburgh Plans Pricing
  plan_count: 2
  slug: university-of-pittsburgh-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: University Of Pittsburgh Rate Limits
  slug: university-of-pittsburgh-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: University of Pittsburgh API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: university-of-pittsburgh-rules
scopes:
- name: University Of Pittsburgh Scopes
  scope_count: 0
  slug: university-of-pittsburgh-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 30.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 60.6
    contract_quality: 63.9
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 60.6
    operational_transparency: 23.7
  previous_composite: 54.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-pittsburgh/refs/heads/main/screenshots/university-of-pittsburgh-2026-06-20T200224.png
security:
- kind: authentication
  name: University Of Pittsburgh Authentication
  slug: university-of-pittsburgh-authentication
  summary_line: api_key/none/saml · 6 schemes
- kind: domain-security
  name: University Of Pittsburgh Domain Security
  slug: university-of-pittsburgh-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: university-of-pittsburgh
tags:
- University
- Higher Education
- Education
- United States
- Public Research University
- Research Data
- Open Data
- Epidemiology
- Public Health
- Civic Data
- Scholarly Publishing
- Institutional Repository
- Library
- Identity Federation
- OAI-PMH
- Open Access
website: https://www.pitt.edu
---
