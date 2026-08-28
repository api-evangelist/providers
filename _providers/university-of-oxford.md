---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - probed
  trial: false
  try_now: false
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
    error_semantics: false
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
  score: 23.0
  scored_at: '2026-08-26'
api_count: 10
apis:
- description: The only API surface Oxford actually documents. An OAI-PMH 2.0 data provider over the institutional open-access repository, serving ten metadata formats including DataCite kernel 4.6, OpenAIRE 4.0, th
  name: ORA — Oxford University Research Archive OAI-PMH
  slug: ora-oai-pmh
- description: 'An undocumented but live JSON search and record API over ORA. GET /objects.json returns a paged, faceted, JSON:API-shaped result set; GET /objects/{uuid}.json returns a single record. The endpoint is '
  name: ORA — Research Archive Search & Record API
  slug: ora-search
- description: 'The strongest institution-operated API surface Oxford runs, and the one entirely absent from this profile before 2026-08-19. Three conformant IIIF specifications on Oxford''s own infrastructure: Image '
  name: Digital Bodleian IIIF API
  slug: bodleian-iiif
- description: A second, independent OAI-PMH data provider, separate from ORA — the Bodleian Libraries' language-resources repository, running on a self-hosted DSpace installation with an OLAC archive description. S
  name: Oxford Text Archive OAI-PMH
  slug: oxford-text-archive-oai-pmh
- description: A SAML 2.0 identity provider serving live machine-readable metadata, with Redirect/SSO, POST/SSO, POST-SimpleSign/SSO, POST/SLO and SOAP/Redirect/SLO bindings and a signing certificate rotated 2026-05
  name: University of Oxford Shibboleth Identity Provider
  slug: shibboleth-idp
- description: 'The public WordPress REST API of Oxford''s Department for Continuing Education, live and anonymous on the read paths. Recorded honestly for what it is: a content-management platform default, not a desi'
  name: Oxford Continuing Education WordPress REST API
  slug: conted-wp-rest
- description: Oxford's research data portal runs on Figshare under an Oxford-owned hostname. The data, the DOI prefix and the collection are Oxford's; the contract, the API and the engineering are Figshare's. No Fi
  name: Sustainable Digital Scholarship research data portal (Figshare tenancy)
  slug: sds-figshare-tenancy
- description: 'The Bodleian Libraries'' discovery layer is Ex Libris Primo VE. Any Primo or Alma REST API reachable under this tenancy is Ex Libris''s contract governing Oxford''s holdings, not an Oxford API. Recorded '
  name: SOLO library discovery (Ex Libris Primo VE tenancy)
  slug: solo-primo-tenancy
- description: Oxford's virtual learning environment, replacing the retired WebLearn Sakai service. The Canvas LMS REST API and Canvas's LTI and Caliper conformance belong to Instructure. The Canvas REST API is live
  name: Oxford Canvas VLE (Instructure tenancy)
  slug: canvas-tenancy
- description: Vacancies were once part of Oxford's own open-data programme; they are now a CoreHR application reached through an Oxford vanity hostname. The redirect target leaves the ox.ac.uk domain entirely, whic
  name: Oxford recruitment (CoreHR tenancy)
  slug: recruit-corehr-tenancy
artifact_total: 28
common:
- group: company
  title: ''
  type: Website
  url: https://www.ox.ac.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://ora.ox.ac.uk/api
- group: docs
  title: ''
  type: APIReference
  url: https://iiif.bodleian.ox.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ora.ox.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://solo.bodleian.ox.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.shibboleth.ox.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://arc-user-guide.readthedocs.io/en/latest/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://lifelong-learning.ox.ac.uk/
- group: other
  title: ''
  type: OpenData
  url: https://data.mrc.ox.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://libguides.bodleian.ox.ac.uk/using-ai-to-support-academic-work/university-policies
- group: build
  title: ''
  type: AITooling
  url: https://libguides.bodleian.ox.ac.uk/using-ai-to-support-academic-work
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ox-it
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OxfordRSE
- group: operate
  title: ''
  type: Status
  url: https://status.it.ox.ac.uk/
- group: operate
  title: ''
  type: Support
  url: https://ora.ox.ac.uk/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ora.ox.ac.uk/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glam.web.ox.ac.uk/privacy-policy-ora
- group: other
  title: ''
  type: Policies
  url: https://ora.ox.ac.uk/policies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-oxford/
- group: company
  title: ''
  type: Blog
  url: https://blog.oxrse.uk/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-oxford-ora-search-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-oxford-ora-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-oxford-bodleian-iiif-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-oxford-oxford-text-archive-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-oxford-ora-search-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-oxford-ora-object-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-oxford-bodleian-iiif-image-info-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-oxford-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-oxford-vocabulary.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-oxford-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-oxford-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-oxford-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-oxford-domain-standards.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-oxford-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-oxford-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-oxford-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-oxford-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-oxford-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-oxford-context.jsonld
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blogs
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The University of Oxford is a collegiate public research university in Oxford, United Kingdom, and a Russell Group member. It operates no central developer programme, no API portal, no developer account and no authenticated API of any kind — and the one it used to run, the Open Data Service at data.ox.ac.uk with OxPoints linked data, places, courses and vacancies over REST and SPARQL, was decommissioned without a successor; that domain and the Mobile Oxford API host no longer resolve. What Oxford does operate, entirely inside its library and research-infrastructure estate, is more substantial than that absence suggests: the Bodleian Libraries run a conformant IIIF stack at iiif.bodleian.ox.ac.uk (Image API 2.1 level 2, Presentation API 2.1 and a Change Discovery 1.0 activity stream over 21,843 items), two independent OAI-PMH data providers (ORA and the Oxford Text Archive), an undocumented but live JSON search API over the institutional repository, and a Shibboleth identity
  provider registered in the UK Access Management Federation and eduGAIN alongside 35 federated service providers across central IT, departments and colleges. Four of the twelve education-regime domain standards are evidenced directly in what those endpoints return: OAI-PMH, DataCite, ORCID and SAML/Shibboleth. Set against that, four significant surfaces carrying Oxford''s name are vendor contracts running under a tenancy and are recorded here as such rather than credited to the University: the Sustainable Digital Scholarship research data portal at portal.sds.ox.ac.uk is Figshare, SOLO is Ex Libris Primo VE, the VLE is Instructure Canvas, and recruitment is CoreHR. Nothing Oxford operates is documented with a machine-readable contract; every OpenAPI and schema in this repository was derived by API Evangelist from live responses and is marked as such.'
examples:
- key_count: 6
  name: University Of Oxford Bodleian Iiif Activity Stream
  slug: university-of-oxford-bodleian-iiif-activity-stream
- key_count: 6
  name: University Of Oxford Bodleian Iiif Collection Top
  slug: university-of-oxford-bodleian-iiif-collection-top
- key_count: 9
  name: University Of Oxford Bodleian Iiif Image Info
  slug: university-of-oxford-bodleian-iiif-image-info
- key_count: 16
  name: University Of Oxford Bodleian Iiif Manifest
  slug: university-of-oxford-bodleian-iiif-manifest
- key_count: 3
  name: University Of Oxford Bodleian Iiif Service Description
  slug: university-of-oxford-bodleian-iiif-service-description
- key_count: 2
  name: University Of Oxford Ora Object Response
  slug: university-of-oxford-ora-object-response
- key_count: 4
  name: University Of Oxford Ora Search Response
  slug: university-of-oxford-ora-search-response
finops:
- name: University Of Oxford Finops
  service_category: Education
  slug: university-of-oxford-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-oxford.png
json_schemas:
- name: Digital Bodleian IIIF Image Information
  property_count: 9
  slug: university-of-oxford-bodleian-iiif-image-info
- name: ORA Object Response
  property_count: 2
  slug: university-of-oxford-ora-object
- name: ORA Search Response
  property_count: 4
  slug: university-of-oxford-ora-search-response
jsonld:
- class_count: 14
  name: University Of Oxford Context
  property_count: 5
  slug: university-of-oxford-context
layout: provider
modified: '2026-08-19'
name: University of Oxford
nav: Providers
network: true
overview: 'University of Oxford publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ORA — Oxford University Research Archive OAI-PMH, ORA — Research Archive Search & Record API, Digital Bodleian IIIF API, and 1 more. Tagged areas include University, Higher Education, Education, Research, and United Kingdom.


  The University of Oxford catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Oxford''s developer surface includes documentation, API reference, GitHub presence, status page, support, engineering blog, code examples, and 35 more developer resources.'
plans:
- name: University Of Oxford Plans Pricing
  plan_count: 2
  slug: university-of-oxford-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: University Of Oxford Rate Limits
  slug: university-of-oxford-rate-limits
rules:
- effective_rule_count: 19
  extends: []
  name: University of Oxford API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 0
    warn: 2
  slug: university-of-oxford-rules
scopes:
- name: University Of Oxford Scopes
  scope_count: 0
  slug: university-of-oxford-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.1
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 22.7
    contract_quality: 27.8
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 22.7
    operational_transparency: 34.2
  previous_composite: 41.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-oxford/refs/heads/main/screenshots/university-of-oxford-2026-06-20T200220.png
security:
- kind: authentication
  name: University Of Oxford Authentication
  slug: university-of-oxford-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Oxford Domain Security
  slug: university-of-oxford-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-oxford
tags:
- University
- Higher Education
- Education
- Research
- United Kingdom
- Russell Group
- Research Repository
- Library
- Digital Collections
- IIIF
- OAI-PMH
- Identity Federation
- Open Access
- Research Computing
website: https://www.ox.ac.uk/
---
