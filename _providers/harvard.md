---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-26'
api_count: 14
apis:
- description: Native REST API of Harvard Dataverse, the institution's research data repository, running Dataverse 6.10.1 (build iqss-4) on Harvard's own AWS infrastructure with no vendor CNAME. Public read operatio
  name: Harvard Dataverse API
  slug: dataverse
- description: OAI-PMH 2.0 metadata harvesting endpoint for Harvard Dataverse. Identify returns repositoryName "Harvard Dataverse Dataverse OAI Archive" with adminEmail support@dataverse.harvard.edu, earliest datest
  name: Harvard Dataverse OAI-PMH
  slug: dataverse-oai
- description: 'Open metadata hub aggregating Harvard bibliographic metadata (12.7M+ bib records, image records, ArchivesSpace finding aids) and returning normalized MODS or Dublin Core. The public Item API needs no '
  name: Harvard Library LibraryCloud API (Open Metadata)
  slug: librarycloud
- description: REST/JSON API to the Harvard Art Museums' collections across 25 documented resources (object, person, exhibition, publication, gallery, classification, culture, medium, period, place, image, iiif, spe
  name: Harvard Art Museums API
  slug: art-museums
- description: Harvard's SAML 2.0 identity provider, entityID https://fed.huit.harvard.edu/idp/shibboleth, registered in the InCommon federation and reachable as signed machine-readable metadata through the InCommon
  name: Harvard University Shibboleth Identity Provider (InCommon)
  slug: identity-federation
- description: 'A 2026 agent-native surface from the Harvard Law School Library Innovation Lab: a static JSON API for progressively discovering and loading pedagogical AI skills for legal education, organized by pers'
  name: Legal Ed Skills Hub (Harvard Law School Library Innovation Lab)
  slug: lil-lawskills
- description: Harvard Law School Library Innovation Lab's digitization of US case law, served as static bulk data organized by reporter. The live REST API at api.case.law was retired in 2024 and now 301-redirects t
  name: Caselaw Access Project bulk data (Harvard Library Innovation Lab)
  slug: caselaw-access-project
- description: Perma.cc is the Harvard Law School Library Innovation Lab's link-rot service, creating permanent citable archives of web pages, and it exposes a public REST API at api.perma.cc. Ownership is confirmed
  name: Perma.cc API (Harvard Library Innovation Lab)
  slug: perma
- description: 'Harvard University Information Technology''s central catalog of administrative APIs - Courses, Person Data Service, Library Catalog, Dining, HR Departments, Zoom, Emailer and Generative AI. The portal '
  name: Harvard API Portal (HUIT)
  slug: api-portal
- description: DASH (Digital Access to Scholarship at Harvard) is Harvard's open-access institutional repository of 58,000+ scholarly works, exposing an open OAI-PMH 2.0 endpoint and a DSpace 7 HAL REST API. TENANT,
  name: Harvard DASH institutional repository (4Science-managed DSpace)
  slug: dash
- description: HOLLIS is Harvard Library's discovery layer. hollis.harvard.edu CNAMEs to hvd.primo.exlibrisgroup.com and redirects to /discovery/search?vid=01HVD_INST:HVD2, a standard Ex Libris Primo VE tenant insta
  name: HOLLIS library discovery (Ex Libris Primo VE tenancy)
  slug: hollis
- description: 'harvard.figshare.com is a Figshare institutional tenancy - the host CNAMEs directly to figshare.com. This is precisely the surface that produced the misattribution this pipeline exists to prevent: in '
  name: Harvard Figshare tenancy
  slug: figshare
- description: canvas.harvard.edu CNAMEs to harvard-vanity.instructure.com. The Canvas REST API is live on that hostname and returns a well-formed JSON 401 to an anonymous caller, which makes it the best-behaved err
  name: Canvas LMS tenancy (Instructure)
  slug: canvas
- description: harvard.zoom.us is a Zoom institutional tenancy branded "Zoom for Harvard", and a Zoom API appears in the HUIT API Portal catalog. The account is Harvard's; the API is Zoom's. Recorded so the HUIT cat
  name: Zoom tenancy
  slug: zoom
artifact_total: 30
common:
- group: company
  title: ''
  type: Website
  url: https://www.harvard.edu/
- group: company
  title: ''
  type: About
  url: https://www.harvard.edu/about/
- group: docs
  title: ''
  type: Documentation
  url: https://library.harvard.edu/services-tools/harvard-library-apis-datasets
- group: docs
  title: ''
  type: APIReference
  url: https://portal.apis.huit.harvard.edu/apis
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.apis.huit.harvard.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harvard
- group: build
  title: ''
  type: GitHub
  url: https://github.com/huit
- group: build
  title: ''
  type: GitHub
  url: https://github.com/harvard-lil
- group: build
  title: ''
  type: GitHub
  url: https://github.com/harvard-lts
- group: build
  title: ''
  type: GitHub
  url: https://github.com/harvard-library
- group: build
  title: ''
  type: GitHub
  url: https://github.com/harvardartmuseums
- group: build
  title: ''
  type: GitHub
  url: https://github.com/IQSS
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.harvard.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://library.harvard.edu/services-tools/dash
- group: build
  title: ''
  type: LibraryCatalog
  url: https://hollis.harvard.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.my.harvard.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/https%3A%2F%2Ffed.huit.harvard.edu%2Fidp%2Fshibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://rc.fas.harvard.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.harvard.edu/ai/
- group: build
  title: ''
  type: AITooling
  url: https://www.harvard.edu/ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harvard.edu/privacy-statement/
- group: operate
  title: ''
  type: Support
  url: https://www.harvard.edu/contact-harvard
- group: operate
  title: ''
  type: Status
  url: https://status.huit.harvard.edu/
- group: company
  title: ''
  type: Blog
  url: https://news.harvard.edu/gazette/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Harvard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/harvard-university/
- group: auth
  title: ''
  type: SecurityDisclosure
  url: https://www.harvard.edu/security-issue/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/harvard-dataverse-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/harvard-lil-legal-ed-skills-hub-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/harvard-librarycloud-item.schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/harvard-lil-lawskills-persona-index.schema.json
- group: build
  title: ''
  type: Examples
  url: examples/README.yml
- group: design
  title: ''
  type: Rules
  url: rules/harvard-governance-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/harvard-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/harvard-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: authentication/harvard-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/harvard-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/harvard-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harvard-education-domain-standards.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harvard-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/harvard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harvard-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/harvard-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/harvard-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/harvard-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Harvard University (Cambridge, Massachusetts; founded 1636; private, Ivy League) is one of the few institutions in this cohort with a genuinely institution-operated programmable footprint rather than a borrowed one. Five surfaces are Harvard''s own: the Harvard Dataverse research data repository, which runs on Harvard''s own infrastructure and whose Dataverse software is written by Harvard''s Institute for Quantitative Social Science and serves a live 450-path OpenAPI; the Harvard Library LibraryCloud open metadata API, unauthenticated over 12M+ bibliographic records; the Harvard Art Museums collections API; a Shibboleth identity provider registered in the InCommon federation with REFEDS SIRTFI assurance; and two Harvard Law School Library Innovation Lab surfaces, the Caselaw Access Project static bulk data and a 2026 OpenAPI 3.1 agent-skills hub. Alongside them sit five vendor tenancies that are just as real and are recorded as such rather than credited to Harvard: DASH runs
  on 4Science''s managed DSpace behind a harvard.edu hostname, the HOLLIS catalog is an Ex Libris Primo VE instance, harvard.figshare.com is a Figshare tenancy, canvas.harvard.edu is an Instructure tenancy, and harvard.zoom.us is a Zoom tenancy. There is no unified developer program: the central HUIT API Portal exists but its catalog, its base URLs and its credentials all sit behind HarvardKey, and the whole harvard.edu Drupal estate answers automated clients with an Akamai 403.'
examples:
- key_count: 6
  name: Harvard Dash Dspace Rest Root
  slug: harvard-dash-dspace-rest-root
- key_count: 1
  name: Harvard Datacite Prefix 10.7910
  slug: harvard-datacite-prefix-10.7910
- key_count: 2
  name: Harvard Dataverse Search Response
  slug: harvard-dataverse-search-response
- key_count: 2
  name: Harvard Librarycloud Item Response
  slug: harvard-librarycloud-item-response
- key_count: 2
  name: Harvard Lil Lawskills Personas
  slug: harvard-lil-lawskills-personas
finops:
- name: Harvard Finops
  service_category: Education
  slug: harvard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harvard.png
json_schemas:
- name: Harvard Library LibraryCloud Item response
  property_count: 2
  slug: harvard-librarycloud-item.schema
- name: Harvard LIL Legal Ed Skills Hub persona index
  property_count: 2
  slug: harvard-lil-lawskills-persona-index.schema
jsonld:
- class_count: 33
  name: Harvard Context
  property_count: 3
  slug: harvard-context
layout: provider
modified: '2026-08-19'
name: Harvard University
nav: Providers
network: true
overview: 'Harvard University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Harvard Dataverse API and Legal Ed Skills Hub (Harvard Law School Library Innovation Lab). Tagged areas include University, Higher Education, Education, United States, and Ivy League.


  The Harvard University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Harvard University''s developer surface includes documentation, API reference, GitHub presence, support, status page, engineering blog, code examples, and 39 more developer resources.'
plans:
- name: Harvard Plans Pricing
  plan_count: 2
  slug: harvard-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Harvard Rate Limits
  slug: harvard-rate-limits
rules:
- effective_rule_count: 10
  extends: []
  name: Harvard University API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 4
  slug: harvard-governance-rules
scopes:
- name: Harvard Scopes
  scope_count: 0
  slug: harvard-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.0
  delta: 2.6
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 11.4
    contract_quality: 54.8
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 11.4
    operational_transparency: 23.7
  previous_composite: 44.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 68.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harvard/refs/heads/main/screenshots/harvard-2026-06-20T182525.png
security:
- kind: authentication
  name: Harvard Authentication
  slug: harvard-authentication
  summary_line: 8 schemes
- kind: domain-security
  name: Harvard Domain Security
  slug: harvard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Harvard Vulnerability Disclosure
  slug: harvard-vulnerability-disclosure
  summary_line: disclosure policy published
slug: harvard
tags:
- University
- Higher Education
- Education
- United States
- Ivy League
- Private Research University
- Research Data
- Research Repository
- Open Metadata
- OAI-PMH
- Identity Federation
- Libraries
- Museums
- Course Catalog
- Research Computing
website: https://www.harvard.edu/
---
