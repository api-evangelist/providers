---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Georgia Institute Of Technology Agentic Access
  operation_count: 14
  slug: georgia-institute-of-technology-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 3
apis:
- description: 'Public OAI-PMH 2.0 metadata harvesting interface for the Georgia Tech Digital Repository, the institutional repository for theses, dissertations, publications, and other scholarly output. Re-verified '
  name: GT Digital Repository OAI-PMH
  slug: repository-oai
- description: 'DSpace 7.6 REST API for the Georgia Tech Digital Repository, providing programmatic read access to communities, collections, items and bitstreams. Re-verified 2026-09-01: /server/api returns 200 appli'
  name: GT Digital Repository REST API
  slug: repository-rest
- description: Georgia Tech's enterprise integration API (BuzzAPI v3), operated by the Office of Information Technology at api.gatech.edu with a test environment at test.api.gatech.edu. Access requires an institutio
  name: BuzzAPI
  slug: buzzapi
- description: Georgia Tech's own SAML 2.0 / Shibboleth identity provider, entityID https://idp.gatech.edu/idp/shibboleth, registered in the InCommon federation and reachable through its per-entity metadata service.
  name: Georgia Tech Shibboleth Identity Provider (InCommon)
  slug: shibboleth-idp
- description: 'Course and curriculum data for the Georgia Tech catalog, served as XML from the institution''s own host through the CourseLeaf "ribbit" data endpoint. Verified 2026-09-01: https://catalog.gatech.edu/ri'
  name: Georgia Tech Course Catalog Data (CourseLeaf)
  slug: course-catalog
- description: 'Georgia Tech is a DataCite direct member. Verified 2026-09-01: https://api.datacite.org/providers/gt returns symbol GT, name "Georgia Institute of Technology", memberType direct_member, rorId https://'
  name: DataCite membership (provider GT, prefix 10.35090)
  slug: datacite
- description: Georgia Institute of Technology is registered in the Research Organization Registry as https://ror.org/01zkghx44, with declared domain gatech.edu, established 1885, and external ids including GRID gri
  name: ROR registration (01zkghx44)
  slug: ror
- description: Georgia Tech's learning management system is Canvas, running as an Instructure-hosted tenant at gatech.instructure.com (200 on 2026-09-01, titled "GT | GT Login") with an institutional alias at canvas
  name: Canvas LMS (Instructure tenant)
  slug: canvas
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The buildings API from Georgia Institute of Technology — 1 operation(s) for buildings.
  name: Georgia Institute of Technology Buildings API
  slug: georgia-institute-of-technology-buildings-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The buildings_id API from Georgia Institute of Technology — 1 operation(s) for buildings_id.
  name: Georgia Institute of Technology Buildings ID API
  slug: georgia-institute-of-technology-buildings-id-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The categories API from Georgia Institute of Technology — 1 operation(s) for categories.
  name: Georgia Institute of Technology Categories API
  slug: georgia-institute-of-technology-categories-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The tags API from Georgia Institute of Technology — 2 operation(s) for tags.
  name: Georgia Institute of Technology Tags API
  slug: georgia-institute-of-technology-tags-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The Add User By Username API from Georgia Institute of Technology — 1 operation(s) for add user by username.
  name: Georgia Institute of Technology Add User By Username API
  slug: georgia-institute-of-technology-add-user-by-username-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The ContactForms API from Georgia Institute of Technology — 1 operation(s) for contactforms.
  name: Georgia Institute of Technology Contact Forms API
  slug: georgia-institute-of-technology-contactforms-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The EquipmentGroup Info API from Georgia Institute of Technology — 1 operation(s) for equipmentgroup info.
  name: Georgia Institute of Technology EquipmentGroup Info API
  slug: georgia-institute-of-technology-equipmentgroup-info-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The EquipmentGroup QueueGroups API from Georgia Institute of Technology — 1 operation(s) for equipmentgroup queuegroups.
  name: Georgia Institute of Technology EquipmentGroup QueueGroups API
  slug: georgia-institute-of-technology-equipmentgroup-queuegroups-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The EquipmentGroup QueueUsers API from Georgia Institute of Technology — 1 operation(s) for equipmentgroup queueusers.
  name: Georgia Institute of Technology EquipmentGroup QueueUsers API
  slug: georgia-institute-of-technology-equipmentgroup-queueusers-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The EquipmentGroup Tools API from Georgia Institute of Technology — 1 operation(s) for equipmentgroup tools.
  name: Georgia Institute of Technology EquipmentGroup Tools API
  slug: georgia-institute-of-technology-equipmentgroup-tools-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The GetToolStatus API from Georgia Institute of Technology — 1 operation(s) for gettoolstatus.
  name: Georgia Institute of Technology Get Tool Status API
  slug: georgia-institute-of-technology-gettoolstatus-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The GetTrainingReport API from Georgia Institute of Technology — 1 operation(s) for gettrainingreport.
  name: Georgia Institute of Technology Get Training Report API
  slug: georgia-institute-of-technology-gettrainingreport-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The GetUserNameAndEmailByBuzzCardNumber API from Georgia Institute of Technology — 1 operation(s) for getusernameandemailbybuzzcardnumber.
  name: Georgia Institute of Technology Get User Name And Email By Buzz Card Number API
  slug: georgia-institute-of-technology-getusernameandemailbybuzzcardnumber-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The ToolCheckLoggedIn API from Georgia Institute of Technology — 1 operation(s) for toolcheckloggedin.
  name: Georgia Institute of Technology Tool Check Logged In API
  slug: georgia-institute-of-technology-toolcheckloggedin-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The TrainingInfo API from Georgia Institute of Technology — 1 operation(s) for traininginfo.
  name: Georgia Institute of Technology Training Info API
  slug: georgia-institute-of-technology-traininginfo-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The UpdateUserTemplate API from Georgia Institute of Technology — 1 operation(s) for updateusertemplate.
  name: Georgia Institute of Technology Update User Template API
  slug: georgia-institute-of-technology-updateusertemplate-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The User Info API from Georgia Institute of Technology — 1 operation(s) for user info.
  name: Georgia Institute of Technology User Info API
  slug: georgia-institute-of-technology-user-info-api
- baseURL: https://repository.gatech.edu/server/oai/request
  baseurl_source: declared
  description: The WhoLoggedIn API from Georgia Institute of Technology — 1 operation(s) for whologgedin.
  name: Georgia Institute of Technology Who Logged In API
  slug: georgia-institute-of-technology-whologgedin-api
artifact_total: 43
collections:
- collection_type: open
  name: Georgia Tech SUMS REST API API
  slug: open-georgia-institute-of-technology-api-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://news.research.gatech.edu/rss.xml
- group: other
  href: https://artifacts.apis.io/georgia-institute-of-technology/capabilities/georgia-institute-of-technology-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/georgia-institute-of-technology-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.gatech.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gatech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gt-ospo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/georgia-institute-of-technology/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rnoc.gatech.edu/api
- group: build
  title: ''
  type: SourceCode
  url: https://ospo.cc.gatech.edu/github-resources/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.gatech.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.gatech.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/https%3A%2F%2Fidp.gatech.edu%2Fidp%2Fshibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.gatech.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.gatech.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://oit.gatech.edu/ai/guidance
- group: other
  title: ''
  type: AIGovernance
  url: https://oit.gatech.edu/governance/ai
- group: build
  title: ''
  type: AITooling
  url: https://oit.gatech.edu/ai/tools
- group: operate
  title: ''
  type: Status
  url: https://status.gatech.edu/
- group: operate
  title: ''
  type: Support
  url: https://gatech.service-now.com/technology
- group: company
  title: ''
  type: Blog
  url: https://news.gatech.edu/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gatech.edu/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gatech.edu/privacy
- group: agent
  href: https://artifacts.apis.io/georgia-institute-of-technology/agentic-access/georgia-institute-of-technology-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/georgia-institute-of-technology-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/georgia-institute-of-technology/security/georgia-institute-of-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/georgia-institute-of-technology-domain-security.yml
- group: design
  href: https://artifacts.apis.io/georgia-institute-of-technology/conformance/georgia-institute-of-technology-conformance.yml
  title: ''
  type: Conformance
  url: conformance/georgia-institute-of-technology-conformance.yml
- group: auth
  href: https://artifacts.apis.io/georgia-institute-of-technology/authentication/georgia-institute-of-technology-authentication.yml
  title: ''
  type: x-authentication
  url: authentication/georgia-institute-of-technology-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/georgia-institute-of-technology/plans/georgia-institute-of-technology-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/georgia-institute-of-technology-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/georgia-institute-of-technology/rate-limits/georgia-institute-of-technology-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/georgia-institute-of-technology-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/georgia-institute-of-technology/finops/georgia-institute-of-technology-finops.yml
  title: ''
  type: FinOps
  url: finops/georgia-institute-of-technology-finops.yml
- group: other
  href: https://artifacts.apis.io/georgia-institute-of-technology/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Georgia Institute of Technology (Georgia Tech) is a public technological research university in Atlanta, Georgia, United States. Its programmable footprint is real but small, decentralized, and operated by individual units rather than by any central API program: there is no developer portal, no self-service key issuance, and no published OpenAPI anywhere on a gatech.edu host that Georgia Tech itself indexes. What does exist, and what was verified live on 2026-09-01, is four institution-operated machine surfaces — an OAI-PMH 2.0 provider and a DSpace 7.6 REST API on repository.gatech.edu (the Georgia Tech Digital Repository), a Shibboleth SAML 2.0 identity provider registered in InCommon and scoped gatech.edu, and a CourseLeaf course-data endpoint on catalog.gatech.edu — plus two contracts Georgia Tech units publish as documents: the SUMS (Shared User Management System) Swagger on sums.gatech.edu and the RNOC GT Places API Swagger on rnoc.gatech.edu. Georgia Tech is a DataCite
  direct member (symbol GT, prefix 10.35090) and is registered in ROR as 01zkghx44. Two things the profile has to say plainly: GT Places is documented as "open to all" but its declared host now answers with a Microsoft Entra ID sign-in redirect, and the enterprise integration API BuzzAPI (api.gatech.edu) lost its public documentation when webmasters.gatech.edu was rebuilt in 2026, so it is a credentialed surface with nothing public left to read.'
examples:
- key_count: 2
  name: Georgia Institute Of Technology Getusernameandemailbybuzzcardnumber Example
  slug: georgia-institute-of-technology-GetUserNameAndEmailByBuzzCardNumber-example
- key_count: 2
  name: Georgia Institute Of Technology Whologgedin Example
  slug: georgia-institute-of-technology-WhoLoggedIn-example
finops:
- has_sources: true
  method: generated
  name: Georgia Institute Of Technology Finops
  primary_unit: ''
  service_category: Education
  slug: georgia-institute-of-technology-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/georgia-institute-of-technology.png
json_schemas:
- name: SUMS Tool Record
  property_count: 19
  slug: georgia-institute-of-technology-tool
- name: SUMS TrainingInfo Record
  property_count: 7
  slug: georgia-institute-of-technology-traininginfo
- name: SUMS WhoLoggedIn Record
  property_count: 5
  slug: georgia-institute-of-technology-whologgedin
json_structures:
- name: Georgia Institute Of Technology Tool Structure
  property_count: 18
  slug: georgia-institute-of-technology-tool-structure
- name: Georgia Institute Of Technology Whologgedin Structure
  property_count: 5
  slug: georgia-institute-of-technology-whologgedin-structure
jsonld:
- class_count: 25
  name: Georgia Institute Of Technology Context
  property_count: 2
  slug: georgia-institute-of-technology-context
layout: provider
modified: '2026-10-06'
name: Georgia Institute of Technology
nav: Providers
network: true
overview: 'Georgia Institute of Technology publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buildings API, Buildings ID API, Categories API, and 23 more. Tagged areas include University, Higher Education, Education, United States, and Institute of Technology.


  The Georgia Institute of Technology catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Georgia Institute of Technology''s developer surface includes GitHub presence, authentication, status page, support, engineering blog, and 24 more developer resources.'
plans:
- name: Georgia Institute Of Technology Plans Pricing
  plan_count: 2
  slug: georgia-institute-of-technology-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Georgia Institute Of Technology Rate Limits
  slug: georgia-institute-of-technology-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Georgia Institute of Technology — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: georgia-institute-of-technology-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 7
  extends: []
  name: Georgia Institute of Technology API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 4
  slug: georgia-institute-of-technology-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 50.3
    catalog_earned_first_party: 0.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 26.3
    contract_governance: 28.0
    contract_quality: 51.7
    developer_ergonomics: 38.1
    discoverability: 62.5
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 18
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/georgia-institute-of-technology/georgia-institute-of-technology-2026-06-20T181758.png
security:
- kind: authentication
  name: Georgia Institute Of Technology Authentication
  slug: georgia-institute-of-technology-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Georgia Institute Of Technology Domain Security
  slug: georgia-institute-of-technology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: georgia-institute-of-technology
tags:
- University
- Higher Education
- Education
- United States
- Institute of Technology
- Public Research University
- Research Repository
- Identity Federation
- Course Catalog
- Library
- Open Data
- Research
website: https://www.gatech.edu/
---
