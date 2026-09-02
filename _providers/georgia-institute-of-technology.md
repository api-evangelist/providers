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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Georgia Institute Of Technology Agentic Access
  operation_count: 14
  slug: georgia-institute-of-technology-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 2
apis:
- description: 'Public OAI-PMH 2.0 metadata harvesting interface for the Georgia Tech Digital Repository, the institutional repository for theses, dissertations, publications, and other scholarly output. Re-verified '
  name: GT Digital Repository OAI-PMH
  slug: repository-oai
- description: 'DSpace 7.6 REST API for the Georgia Tech Digital Repository, providing programmatic read access to communities, collections, items and bitstreams. Re-verified 2026-09-01: /server/api returns 200 appli'
  name: GT Digital Repository REST API
  slug: repository-rest
- description: Campus place data — buildings, offices, categories and community tags with names, addresses, phone numbers, images and GPS coordinates — documented and published by the Georgia Tech Research Network O
  name: GT Places API
  slug: gt-places
- description: The Shared User Management System (SUMS) REST API, operated by Georgia Tech at sums.gatech.edu to manage researcher access to shared lab instruments, training records, equipment-group queues and BuzzC
  name: Georgia Tech SUMS REST API
  slug: sums
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Georgia Tech SUMS REST API API
  slug: open-georgia-institute-of-technology-api-api
common:
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
  title: ''
  type: AgenticAccess
  url: agentic-access/georgia-institute-of-technology-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/georgia-institute-of-technology-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/georgia-institute-of-technology-conformance.yml
- group: auth
  title: ''
  type: x-authentication
  url: authentication/georgia-institute-of-technology-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/georgia-institute-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/georgia-institute-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/georgia-institute-of-technology-finops.yml
- group: other
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
- name: Georgia Institute Of Technology Finops
  service_category: Education
  slug: georgia-institute-of-technology-finops
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
modified: '2026-09-01'
name: Georgia Institute of Technology
nav: Providers
network: true
overview: 'Georgia Institute of Technology publishes 2 APIs on the [APIs.io](https://apis.io/) network: GT Places API and Georgia Tech SUMS REST API. Tagged areas include University, Higher Education, Education, United States, and Institute of Technology.


  The Georgia Institute of Technology catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Georgia Institute of Technology''s developer surface includes GitHub presence, authentication, status page, support, engineering blog, and 22 more developer resources.'
plans:
- name: Georgia Institute Of Technology Plans Pricing
  plan_count: 2
  slug: georgia-institute-of-technology-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Georgia Institute Of Technology Rate Limits
  slug: georgia-institute-of-technology-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Georgia Institute of Technology API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: georgia-institute-of-technology-jsonschema-spectral-rules
- effective_rule_count: 7
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
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 13.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.0
    contract_quality: 49.8
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 28.0
    operational_transparency: 26.3
  previous_composite: 34.4
  provenance:
    agentic_access: derived
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
    score: 61.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/georgia-institute-of-technology/refs/heads/main/screenshots/georgia-institute-of-technology-2026-06-20T181758.png
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
