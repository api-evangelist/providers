---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 33.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: Figshare Agentic Access
  operation_count: 157
  slug: figshare-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The altmetric API from Figshare — 1 operation(s) for altmetric.
  name: Figshare altmetric API
  slug: figshare-altmetric-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The articles API from Figshare — 34 operation(s) for articles.
  name: Figshare articles API
  slug: figshare-articles-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The authors API from Figshare — 2 operation(s) for authors.
  name: Figshare authors API
  slug: figshare-authors-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The collections API from Figshare — 21 operation(s) for collections.
  name: Figshare collections API
  slug: figshare-collections-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The institutions API from Figshare — 20 operation(s) for institutions.
  name: Figshare institutions API
  slug: figshare-institutions-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The oauth API from Figshare — 1 operation(s) for oauth.
  name: Figshare oauth API
  slug: figshare-oauth-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The other API from Figshare — 7 operation(s) for other.
  name: Figshare other API
  slug: figshare-other-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The profiles API from Figshare — 2 operation(s) for profiles.
  name: Figshare profiles API
  slug: figshare-profiles-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The projects API from Figshare — 17 operation(s) for projects.
  name: Figshare projects API
  slug: figshare-projects-api
- baseURL: https://api.figshare.com/v2
  baseurl_source: declared
  description: The symplectic API from Figshare — 5 operation(s) for symplectic.
  name: Figshare symplectic API
  slug: figshare-symplectic-api
artifact_total: 57
collections:
- collection_type: postman
  name: Figshare altmetric API
  slug: postman-figshare-altmetric-api
- collection_type: postman
  name: Figshare altmetric articles API
  slug: postman-figshare-articles-api
- collection_type: postman
  name: Figshare altmetric authors API
  slug: postman-figshare-authors-api
- collection_type: postman
  name: Figshare altmetric collections API
  slug: postman-figshare-collections-api
- collection_type: postman
  name: Figshare altmetric institutions API
  slug: postman-figshare-institutions-api
- collection_type: postman
  name: Figshare altmetric oauth API
  slug: postman-figshare-oauth-api
- collection_type: postman
  name: Figshare altmetric other API
  slug: postman-figshare-other-api
- collection_type: postman
  name: Figshare altmetric profiles API
  slug: postman-figshare-profiles-api
- collection_type: postman
  name: Figshare altmetric projects API
  slug: postman-figshare-projects-api
- collection_type: postman
  name: Figshare altmetric symplectic API
  slug: postman-figshare-symplectic-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Figshare altmetric API
  slug: open-figshare-altmetric-api
- collection_type: open
  name: Figshare altmetric articles API
  slug: open-figshare-articles-api
- collection_type: open
  name: Figshare altmetric authors API
  slug: open-figshare-authors-api
- collection_type: open
  name: Figshare altmetric collections API
  slug: open-figshare-collections-api
- collection_type: open
  name: Figshare altmetric institutions API
  slug: open-figshare-institutions-api
- collection_type: open
  name: Figshare altmetric oauth API
  slug: open-figshare-oauth-api
- collection_type: open
  name: Figshare altmetric other API
  slug: open-figshare-other-api
- collection_type: open
  name: Figshare altmetric profiles API
  slug: open-figshare-profiles-api
- collection_type: open
  name: Figshare altmetric projects API
  slug: open-figshare-projects-api
- collection_type: open
  name: Figshare altmetric symplectic API
  slug: open-figshare-symplectic-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/figshare-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/figshare/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/figshare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/figshare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/figshare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/figshare-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://figshare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.figshare.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/figshare
- group: company
  title: ''
  type: Blog
  url: https://info.figshare.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://info.figshare.com/figshare-plus/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.figshare.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/figshare/
- group: other
  title: ''
  type: X
  url: https://x.com/figshare
- group: operate
  title: ''
  type: Support
  url: https://support.figshare.com/
- group: docs
  title: ''
  type: UserDocumentation
  url: https://info.figshare.com/user-guide/how-to-use-the-figshare-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/figshare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/figshare-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/figshare-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/figshare-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/figshare-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://info.figshare.com/blog/feed/
created: '2026-06-12'
description: Figshare is a research data repository platform that enables researchers, institutions, and organizations to upload, manage, and publicly share scientific outputs including datasets, figures, media, papers, posters, and software. The platform provides persistent DOI assignment for all published research outputs, enabling proper citation and long-term discoverability. Figshare's REST API v2 allows programmatic access to articles, collections, projects, file uploads, statistics, and administrative functions. The platform is built on AWS infrastructure and supports both individual researchers with a free 20GB tier and institutional deployments with custom storage configurations up to multiple terabytes.
examples:
- key_count: 17
  name: Figshare Article Example
  slug: figshare-article-example
- key_count: 10
  name: Figshare Collection Example
  slug: figshare-collection-example
- key_count: 11
  name: Figshare File_Upload Example
  slug: figshare-file_upload-example
- key_count: 9
  name: Figshare Project Example
  slug: figshare-project-example
finops:
- name: Figshare Finops
  service_category: ''
  slug: figshare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/figshare.png
json_schemas:
- name: Account
  property_count: 19
  slug: figshare-account
- name: Article
  property_count: 16
  slug: figshare-article
- name: ArticleComplete
  property_count: 7
  slug: figshare-articlecomplete
- name: Author
  property_count: 7
  slug: figshare-author
- name: Category
  property_count: 6
  slug: figshare-category
- name: Collection
  property_count: 6
  slug: figshare-collection
- name: CollectionComplete
  property_count: 23
  slug: figshare-collectioncomplete
- name: FundingInformation
  property_count: 6
  slug: figshare-fundinginformation
- name: License
  property_count: 3
  slug: figshare-license
- name: PrivateFile
  property_count: 5
  slug: figshare-privatefile
- name: Project
  property_count: 5
  slug: figshare-project
- name: ProjectComplete
  property_count: 7
  slug: figshare-projectcomplete
- name: PublicFile
  property_count: 8
  slug: figshare-publicfile
jsonld:
- class_count: 38
  name: Figshare Context
  property_count: 5
  slug: figshare-context
layout: provider
modified: '2026-06-12'
name: Figshare
nav: Providers
network: true
overview: 'Figshare publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Research Data, Data Repository, Open Science, DOI, and Datasets.


  The Figshare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Figshare''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Figshare Plans Pricing
  plan_count: 8
  slug: figshare-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Figshare Rate Limits
  slug: figshare-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Figshare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: figshare-jsonschema-spectral-rules
scopes:
- name: Figshare Scopes
  scope_count: 1
  slug: figshare-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 90.3
    catalog_earned_first_party: 0.0
    catalog_gap: 24.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 74.0
    developer_ergonomics: 17.9
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/figshare/refs/heads/main/screenshots/figshare-2026-06-20T181159.png
security:
- kind: authentication
  name: Figshare Authentication
  slug: figshare-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Figshare Domain Security
  slug: figshare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: figshare
tags:
- Research Data
- Data Repository
- Open Science
- DOI
- Datasets
- Academic
- File Storage
- Open Access
website: https://figshare.com/
---
