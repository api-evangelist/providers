---
access_model:
  confidence: high
  label: Free · Access granted on request (email integration@cardiff.ac.uk)
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cardiff Agentic Access
  operation_count: 26
  slug: cardiff-agentic-access
  summary_line: 26 operations
api_count: 5
apis:
- description: Course records, descriptions and structure for taught programmes. 4 operation(s), from Cardiff's own CoursesApi contract on the api.data.cardiff.ac.uk gateway (base path /courses/v1).
  name: Cardiff University Courses API
  slug: cardiff-courses-api
- description: Clearing and adjustment availability against the course catalogue. 1 operation(s), from Cardiff's own CoursesApi contract on the api.data.cardiff.ac.uk gateway (base path /courses/v1).
  name: Cardiff University Clearing Adjustments API
  slug: cardiff-clearing-adjustments-api
- description: Course grouping records exposed by the Courses contract. 1 operation(s), from Cardiff's own CoursesApi contract on the api.data.cardiff.ac.uk gateway (base path /courses/v1).
  name: Cardiff University Groups API
  slug: cardiff-groups-api
- description: Module records and module catalogues for taught modules. 5 operation(s), from Cardiff's own ModulesApi contract on the api.data.cardiff.ac.uk gateway (base path /modules/v1).
  name: Cardiff University Modules API
  slug: cardiff-modules-api
- description: Assessments attached to a module, filterable by academic year. 1 operation(s), from Cardiff's own ModulesApi contract on the api.data.cardiff.ac.uk gateway (base path /modules/v1).
  name: Cardiff University Assessments API
  slug: cardiff-assessments-api
- description: Module occurrences, including the VLE (learn) occurrence records. 4 operation(s), from Cardiff's own ModulesApi contract on the api.data.cardiff.ac.uk gateway (base path /modules/v1).
  name: Cardiff University Occurrences API
  slug: cardiff-occurrences-api
- description: Year-on-year module rollover mapping. 2 operation(s), from Cardiff's own ModulesApi contract on the api.data.cardiff.ac.uk gateway (base path /modules/v1).
  name: Cardiff University Rollover API
  slug: cardiff-rollover-api
- description: Reference list of academic schools used across the University. 1 operation(s), from Cardiff's own LookupsApi contract on the api.data.cardiff.ac.uk gateway (base path /lookups/v1).
  name: Cardiff University Schools API
  slug: cardiff-schools-api
- description: Reference list of subject codes. 1 operation(s), from Cardiff's own LookupsApi contract on the api.data.cardiff.ac.uk gateway (base path /lookups/v1).
  name: Cardiff University Subjects API
  slug: cardiff-subjects-api
- description: Reference list of study levels. 1 operation(s), from Cardiff's own LookupsApi contract on the api.data.cardiff.ac.uk gateway (base path /lookups/v1).
  name: Cardiff University Levels API
  slug: cardiff-levels-api
- description: Reference list of semester codes. 1 operation(s), from Cardiff's own LookupsApi contract on the api.data.cardiff.ac.uk gateway (base path /lookups/v1).
  name: Cardiff University Semesters API
  slug: cardiff-semesters-api
- description: Reference list of qualification codes. 1 operation(s), from Cardiff's own LookupsApi contract on the api.data.cardiff.ac.uk gateway (base path /lookups/v1).
  name: Cardiff University Qualifications API
  slug: cardiff-qualifications-api
- description: Reference list of academic years. 1 operation(s), from Cardiff's own LookupsApi contract on the api.data.cardiff.ac.uk gateway (base path /lookups/v1).
  name: Cardiff University Years API
  slug: cardiff-years-api
- description: Research publication records, keyed on the ORCA EPrints identifier. 2 operation(s), from Cardiff's own PublicationsApi contract on the api.data.cardiff.ac.uk gateway (base path /publications/v1).
  name: Cardiff University Publications API
  slug: cardiff-publications-api
- description: Gateway connectivity-test catch-all path. 1 operation(s), from Cardiff's own EchoTest contract on the api.data.cardiff.ac.uk gateway (base path /echo/v1).
  name: Cardiff University Echo Default API
  slug: cardiff-default-api
- description: Gateway connectivity-test endpoint. 1 operation(s), from Cardiff's own EchoTest contract on the api.data.cardiff.ac.uk gateway (base path /echo/v1).
  name: Cardiff University Echo Test API
  slug: cardiff-test-api
- description: Online Research @ Cardiff (ORCA) is Cardiff University's own EPrints institutional repository, listed as an IT service the University runs. Its OAI-PMH interface has been registered under Cardiff Univ
  name: ORCA OAI-PMH Interface
  slug: cardiff-orca-oai-pmh
- description: 'Cardiff University publishes IT service status on an Atlassian Statuspage at status.cardiff.ac.uk, which carries the standard Statuspage v2 JSON API. Verified live: summary.json returned 200 with 40 n'
  name: Cardiff University IT Status API
  slug: cardiff-status-api
- description: Cardiff's research data repository at research-data.cardiff.ac.uk is a Figshare for Institutions instance - the host CNAMEs to proxy-eu-01.figshare.com, and Cardiff's own DataCite repository client bl
  name: Cardiff University Research Data Repository (Figshare tenancy)
  slug: cardiff-research-data-repository
- description: research.cardiff.ac.uk is Cardiff's research information system, running on Clarivate Converis - the host CNAMEs to cu.converis.clarivate.com and the University's IT status page lists "Research Portal
  name: Cardiff University Research Portal (Converis tenancy)
  slug: cardiff-research-portal
- description: librarysearch.cardiff.ac.uk is Cardiff's discovery layer, an Ex Libris Primo view (vid=44WHELF_CAR:CAR) sitting on the WHELF shared Alma library management system; the IT status page lists ALMA, Primo
  name: Cardiff LibrarySearch (Ex Libris Primo tenancy)
  slug: cardiff-librarysearch
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CoursesApi Assessments API
  slug: open-cardiff-assessments-api
- collection_type: open
  name: CoursesApi Assessments Clearing Adjustments API
  slug: open-cardiff-clearing-adjustments-api
- collection_type: open
  name: CoursesApi Assessments Courses API
  slug: open-cardiff-courses-api
- collection_type: open
  name: CoursesApi Assessments * API
  slug: open-cardiff-default-api
- collection_type: open
  name: CoursesApi Assessments Groups API
  slug: open-cardiff-groups-api
- collection_type: open
  name: CoursesApi Assessments Levels API
  slug: open-cardiff-levels-api
- collection_type: open
  name: CoursesApi Assessments Modules API
  slug: open-cardiff-modules-api
- collection_type: open
  name: CoursesApi Assessments Occurrences API
  slug: open-cardiff-occurrences-api
- collection_type: open
  name: CoursesApi Assessments Publications API
  slug: open-cardiff-publications-api
- collection_type: open
  name: CoursesApi Assessments Qualifications API
  slug: open-cardiff-qualifications-api
- collection_type: open
  name: CoursesApi Assessments Rollover API
  slug: open-cardiff-rollover-api
- collection_type: open
  name: CoursesApi Assessments Schools API
  slug: open-cardiff-schools-api
- collection_type: open
  name: CoursesApi Assessments Semesters API
  slug: open-cardiff-semesters-api
- collection_type: open
  name: CoursesApi Assessments Subjects API
  slug: open-cardiff-subjects-api
- collection_type: open
  name: CoursesApi Assessments Test API
  slug: open-cardiff-test-api
- collection_type: open
  name: CoursesApi Assessments Years API
  slug: open-cardiff-years-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.cardiff.ac.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.cardiff.ac.uk/devportal/
- group: other
  title: ''
  type: OpenData
  url: https://data.cardiff.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.cardiff.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: http://metadata.ukfederation.org.uk/ukfederation-metadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://orca.cardiff.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research-data.cardiff.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://librarysearch.cardiff.ac.uk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://data.cardiff.ac.uk/devportal/
- group: other
  title: ''
  type: ResearchComputing
  url: https://arcca.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ARCCA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cardiffnlp
- group: operate
  title: ''
  type: Status
  url: https://status.cardiff.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://sites.cardiff.ac.uk/ilrb/using-gen-ai-to-support-your-literature-searching/
- group: commercial
  title: ''
  type: TermsOfService
  url: http://www.cardiff.ac.uk/terms/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/cardiff-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/cardiff-education-standards.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cardiff-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cardiff-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardiff-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cardiff-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cardiff-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cardiff-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cardiff-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cardiff-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Cardiff University is a public research university in Cardiff, Wales, and a member of the Russell Group. Unusually for a UK institution it operates its own API gateway rather than only buying one: api.data.cardiff.ac.uk runs WSO2 API Manager under the University''s own registrable domain and serves five institution-authored REST contracts - Courses, Modules, Lookups, Publications and an Echo connectivity test - published through a developer portal at data.cardiff.ac.uk/devportal. Access is OAuth2 client-credentials and is not open self-serve: external developers must email integration@cardiff.ac.uk with a use case before an application can be created. As of a probe on 2026-08-30 both data.cardiff.ac.uk and api.data.cardiff.ac.uk 302-redirect every path to the University''s service-unavailable page at outage.cf.ac.uk, so nothing on the gateway is callable from outside at this moment; the contracts in this repository were harvested while it was up. Beyond the gateway, Cardiff''s
  genuinely institution-operated machine-readable surfaces are its Shibboleth identity federation membership (a registered UK Access Management Federation IdP), the OAI-PMH interface of its own EPrints repository ORCA, its DataCite repository client and DOI prefix 10.17035, and the ARCCA research-computing GitHub organisation. Its research data repository, research portal and library discovery layer are vendor platforms running under Cardiff subdomains - Figshare, Clarivate Converis and Ex Libris respectively - and are recorded here as tenant relationships, not as Cardiff''s engineering.'
examples:
- key_count: 2
  name: Cardiff Courses List Example
  slug: cardiff-courses-list-example
- key_count: 2
  name: Cardiff Lookups Schools Example
  slug: cardiff-lookups-schools-example
- key_count: 2
  name: Cardiff Modules List Example
  slug: cardiff-modules-list-example
- key_count: 2
  name: Cardiff Publications List Example
  slug: cardiff-publications-list-example
finops:
- name: Cardiff Finops
  service_category: Education
  slug: cardiff-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardiff.png
json_schemas:
- name: Course
  property_count: 19
  slug: cardiff-course
- name: Meta
  property_count: 5
  slug: cardiff-meta
- name: Module
  property_count: 10
  slug: cardiff-module
- name: Publication
  property_count: 31
  slug: cardiff-publication
json_structures:
- name: Cardiff Course Structure
  property_count: 13
  slug: cardiff-course-structure
- name: Cardiff Module Structure
  property_count: 10
  slug: cardiff-module-structure
- name: Cardiff Publication Structure
  property_count: 16
  slug: cardiff-publication-structure
jsonld:
- class_count: 5
  name: Cardiff Context
  property_count: 4
  slug: cardiff-context
layout: provider
modified: '2026-08-30'
name: Cardiff University
nav: Providers
network: true
overview: 'Cardiff University publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Courses API, Clearing Adjustments API, Groups API, and 13 more. Tagged areas include Education, Higher Education, University, Public Research University, and United Kingdom.


  The Cardiff University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cardiff University''s developer surface includes status page, authentication, and 24 more developer resources.'
plans:
- name: Cardiff Plans Pricing
  plan_count: 2
  slug: cardiff-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Cardiff Rate Limits
  slug: cardiff-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cardiff University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cardiff-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Cardiff University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: cardiff-rules
scopes:
- name: Cardiff Scopes
  scope_count: 2
  slug: cardiff-scopes
  summary_line: 2 scopes · implicit
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 9.8
    contract_quality: 50.5
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardiff/refs/heads/main/screenshots/cardiff-2026-06-20T173956.png
security:
- kind: authentication
  name: Cardiff Authentication
  slug: cardiff-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cardiff Domain Security
  slug: cardiff-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardiff
tags:
- Education
- Higher Education
- University
- Public Research University
- United Kingdom
- Wales
- Russell Group
- Open Data
- Course Catalog
- Research Repository
- Identity Federation
- Research Computing
- Publications
website: https://www.cardiff.ac.uk/
---
