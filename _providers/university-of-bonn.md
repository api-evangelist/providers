---
access_model:
  confidence: high
  label: Free · no key, no onboarding · public read endpoints
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Bonn Agentic Access
  operation_count: 7
  slug: university-of-bonn-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: 'OAI-PMH 2.0 metadata-harvesting endpoint for bonndata, the University of Bonn institutional research data repository. Re-verified live 2026-09-01: verb=Identify returns repositoryName "bonndata Datave'
  name: bonndata OAI-PMH Metadata Endpoint
  slug: bonndata-oai-pmh
- baseURL: https://bonndata.uni-bonn.de/api/datasets/:persistentId/?persistentId=doi:10.60507/FK2/BBP6GG
  baseurl_source: declared
  description: 'Retrieve published datasets, their versions, and export metadata from bonndata. Re-verified live 2026-09-01: /datasets/:persistentId?persistentId=doi:10.60507/FK2/BBP6GG returned 200 with 12,647 bytes'
  name: University of Bonn Datasets API
  slug: university-of-bonn-datasets-api
- baseURL: https://bonndata.uni-bonn.de/api/info/version
  baseurl_source: declared
  description: 'Repository version and software information for bonndata. Re-verified live 2026-09-01: GET /info/version returned {"status":"OK","data":{"version":"6.7.1","build":"1955-8e18f64"}}. The OpenAPI server '
  name: University of Bonn Info API
  slug: university-of-bonn-info-api
- baseURL: https://bonndata.uni-bonn.de/api/info/metrics/datasets
  baseurl_source: declared
  description: 'Aggregate repository metrics for bonndata. Re-verified live 2026-09-01: GET /info/metrics/datasets returned {"status":"OK","data":{"count":376}}. Note the path is /info/metrics/datasets — a bare /metr'
  name: University of Bonn Metrics API
  slug: university-of-bonn-metrics-api
- baseURL: https://bonndata.uni-bonn.de/api/search?q=*&type=dataset
  baseurl_source: declared
  description: 'Search the published catalog of datasets, dataverses and files in bonndata. Re-verified live 2026-09-01: /search?q=*&type=dataset returned total_count 376 (362 at first profiling on 2026-06-03), and /'
  name: University of Bonn Search API
  slug: university-of-bonn-search-api
- description: 'OAI-PMH 2.0 endpoint for bonndoc, "Der Publikationsserver der Universitaet Bonn" — the university''s DSpace-based publication and dissertation server, operated by the ULB. Verified live 2026-09-01: ver'
  name: bonndoc Publication Server OAI-PMH Endpoint
  slug: bonndoc-oai-pmh
- description: 'bonndoc runs DSpace 7-class software, which exposes a HAL/JSON REST API at /server/api. It is recorded with an honest limit rather than as a working surface: on 2026-09-01 https://bonndoc.ulb.uni-bonn'
  name: bonndoc DSpace REST API (bot-challenged)
  slug: bonndoc-dspace-rest
- description: 'The University of Bonn self-hosts GitLab at gitlab.uni-bonn.de and its REST API v4 answers anonymous callers over the public project set. Verified live 2026-09-01: GET /api/v4/projects?per_page=1&simp'
  name: University of Bonn GitLab REST API v4
  slug: gitlab-api
- description: The University of Bonn operates its own SAML 2.0 / Shibboleth Identity Provider and publishes signed metadata from its own host — https://shibboleth.uni-bonn.de/idp/shibboleth returned 200 application
  name: DFN-AAI Identity Federation — University of Bonn Shibboleth IdP
  slug: dfn-aai-idp
- description: 'The University of Bonn is a DataCite member organization and mints DOIs for its research data. Verified 2026-09-01 at https://api.datacite.org/providers/bxbq (200): symbol BXBQ, name "University of Bo'
  name: DataCite Membership — University of Bonn (BXBQ)
  slug: datacite-member
- description: 'The University of Bonn''s Research Organization Registry identifier, https://ror.org/041nas322, verified live 2026-09-01. Domain uni-bonn.de, established 1818, located in Bonn, North Rhine-Westphalia, '
  name: ROR Registry Record — University of Bonn
  slug: ror-record
- description: bonndata is registered in re3data, the Registry of Research Data Repositories, as r3d100014222 with its own DOI https://doi.org/10.17616/R31NJNGU. Verified 2026-09-01 via https://www.re3data.org/api/b
  name: re3data Registry Record — bonndata
  slug: re3data-record
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: bonndata Dataverse Native REST API (Public Read Subset) Datasets API
  slug: open-university-of-bonn-datasets-api
- collection_type: open
  name: bonndata Dataverse Native REST API (Public Read Subset) Datasets Info API
  slug: open-university-of-bonn-info-api
- collection_type: open
  name: bonndata Dataverse Native REST API (Public Read Subset) Datasets Metrics API
  slug: open-university-of-bonn-metrics-api
- collection_type: open
  name: bonndata Dataverse Native REST API (Public Read Subset) Datasets Search API
  slug: open-university-of-bonn-search-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.uni-bonn.de/en
- group: docs
  title: ''
  type: Documentation
  url: https://guides.dataverse.org/en/latest/api/native-api.html
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.hrz.uni-bonn.de/en/all-services/data-storage-fileservices/bonndata
- group: build
  title: ''
  type: LibraryCatalog
  url: https://bonnus.ulb.uni-bonn.de/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://basis.uni-bonn.de/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.uni-bonn.de/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.hpc.uni-bonn.de/en
- group: other
  title: ''
  type: AIPolicy
  url: https://www.ktf.uni-bonn.de/faecher/fundamentaltheologie/medien-1/ki-richtlinien-uni-bonn.pdf
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.uni-bonn.de/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unibonn
- group: operate
  title: ''
  type: Support
  url: https://www.hrz.uni-bonn.de/en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uni-bonn.de/en/imprint
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uni-bonn.de/en/data-protection
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.uni-bonn.de/.well-known/security.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-bonn/
- group: company
  title: ''
  type: Blog
  url: https://www.uni-bonn.de/news/rss.xml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-bonn-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-bonn-authentication.yml
- group: design
  title: ''
  type: x-errors
  url: errors/university-of-bonn-errors.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-bonn-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-bonn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bonn-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bonn-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bonn-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bonn-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Bonn (Rheinische Friedrich-Wilhelms-Universitaet Bonn), founded in 1818, is a public research university in North Rhine-Westphalia, Germany, and a member of the German Universities Excellence Initiative. Like every institution it is a federation of buyers rather than an API producer, but it is an unusually self-hosted one: the surfaces in this profile run on the university''s own hosts, inside its own computing centre, rather than on a vendor''s multi-tenant platform. bonndata, the institutional cross-disciplinary research data repository, runs Dataverse 6.7.1 at bonndata.uni-bonn.de (CNAME bonndata-produktiv.rhrz.uni-bonn.de, 131.220.213.19) and exposes a genuinely public, anonymous, read-only REST API — /search, /datasets, /datasets/export, /info/version, /info/metrics — plus a full OAI-PMH 2.0 endpoint; every documented path was re-verified live on 2026-09-01 and /search returned 376 indexed datasets. bonndoc, the university publication server at bonndoc.ulb.uni-bonn.de,
  answers OAI-PMH in ten metadata formats. The university runs its own Shibboleth Identity Provider at shibboleth.uni-bonn.de and is the only uni-bonn.de entity in the 11,457-entity DFN-AAI federation aggregate. It self-hosts GitLab at gitlab.uni-bonn.de, whose REST API v4 answers anonymously across 195 public projects, and keeps a GitHub organization at github.com/unibonn. It is a DataCite member (BXBQ) minting DOIs under prefix 10.60507 through the bonndata repository client, is registered in ROR as 041nas322 and in re3data as r3d100014222. What it does NOT have is equally clear and is stated here rather than padded: no central developer portal, no institution-authored OpenAPI or AsyncAPI, no llms.txt, sitemap.xml, apis.json or agent card on any host it controls, no public course, timetable or student-information API (BASIS runs HISinOne behind sign-in, eCampus runs ILIAS), and no institutional open-data portal — opendata.bonn.de belongs to the City of Bonn, not the university. Library
  discovery (bonnus) is Ex Libris Primo, self-hosted on a university IP, with no public API. The four OpenAPI documents in this repo are API-Evangelist-authored descriptions of the public read subset of the Dataverse Native API as deployed by Bonn; the Dataverse contract itself belongs to the Dataverse project, and no vendor specification is saved under this institution.'
examples:
- key_count: 2
  name: University Of Bonn Info Version Example
  slug: university-of-bonn-info-version-example
- key_count: 2
  name: University Of Bonn Metrics Datasets Example
  slug: university-of-bonn-metrics-datasets-example
- key_count: 2
  name: University Of Bonn Search Example
  slug: university-of-bonn-search-example
finops:
- name: University Of Bonn Finops
  service_category: Education
  slug: university-of-bonn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bonn.png
json_schemas:
- name: bonnDataSearchItem
  property_count: 24
  slug: university-of-bonn-search-item
- name: bonnDataSearchResponse
  property_count: 2
  slug: university-of-bonn-search-response
json_structures:
- name: University Of Bonn Dataset Structure
  property_count: 22
  slug: university-of-bonn-dataset-structure
jsonld:
- class_count: 14
  name: University Of Bonn Context
  property_count: 8
  slug: university-of-bonn-context
layout: provider
modified: '2026-09-01'
name: University of Bonn
nav: Providers
network: true
overview: 'University of Bonn publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Info API, Metrics API, and 1 more. Tagged areas include University, Higher Education, Education, Germany, and Public Research University.


  The University of Bonn catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Bonn''s developer surface includes documentation, support, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: University Of Bonn Plans Pricing
  plan_count: 2
  slug: university-of-bonn-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: University Of Bonn Rate Limits
  slug: university-of-bonn-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Bonn API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-bonn-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: University of Bonn API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: university-of-bonn-rules
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 41.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 28.0
    contract_quality: 23.7
    developer_ergonomics: 28.6
    discoverability: 79.6
    governance: 28.0
    operational_transparency: 26.3
  previous_composite: 45.7
  provenance:
    agentic_access: derived
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
    score: 72.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bonn/refs/heads/main/screenshots/university-of-bonn-2026-06-20T200139.png
security:
- kind: authentication
  name: University Of Bonn Authentication
  slug: university-of-bonn-authentication
  summary_line: none/saml2/api_key · 4 schemes
- kind: domain-security
  name: University Of Bonn Domain Security
  slug: university-of-bonn-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Bonn Vulnerability Disclosure
  slug: university-of-bonn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-bonn
tags:
- University
- Higher Education
- Education
- Germany
- Public Research University
- Research Data
- Open Data
- Open Science
- Institutional Repository
- Dataverse
- OAI-PMH
- Identity Federation
- Shibboleth
- DFN-AAI
- Research Computing
- Scholarly Publishing
website: https://www.uni-bonn.de/en
---
