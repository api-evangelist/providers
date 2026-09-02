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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 25.0
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: 'Tapis is the API platform TACC builds and operates for programmatic access to research computing: registering storage and compute systems, moving files, defining applications, submitting and tracking '
  name: Tapis v3 Research Computing Platform (TACC production tenant)
  slug: tapis
- description: UT Austin's Shibboleth identity provider, and the most under-catalogued class of institutional API surface. It publishes SAML 2.0 metadata at /idp/shibboleth (entityID https://enterprise.login.utexas.
  name: UT Austin Enterprise Identity Provider (SAML 2.0 + OpenID Connect)
  slug: enterprise-idp
- description: Public DSpace REST API for Texas ScholarWorks, the UT Libraries institutional repository of theses, dissertations, faculty research and open-access scholarship. The root document reports dspaceName "D
  name: Texas ScholarWorks DSpace REST API
  slug: scholarworks-rest
- description: OAI-PMH 2.0 metadata-harvesting endpoint for Texas ScholarWorks. An Identify request returns repositoryName "DSpace at UT Austin", baseURL https://repositories.lib.utexas.edu/server/oai/request, granu
  name: Texas ScholarWorks OAI-PMH Endpoint
  slug: scholarworks-oai
- description: 'UT Austin publishes and archives research datasets in the Texas Data Repository, a Dataverse instance operated by the Texas Digital Library and shared across Texas institutions. The instance reported '
  name: Texas Data Repository (Dataverse) — UT Austin collection
  slug: texas-data-repository
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.utexas.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://tacc.utexas.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://identity.utexas.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositories.lib.utexas.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.lib.utexas.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.utexas.edu/
- group: other
  title: ''
  type: OpenData
  url: https://dataverse.tdl.org/dataverse/utexas
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.utexas.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tacc.utexas.edu/
- group: docs
  title: ''
  type: APIReference
  url: https://tapis.readthedocs.io/en/latest/technical/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TACC
- group: other
  title: ''
  type: OpenSourceProgramOffice
  url: https://opensource.utexas.edu/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.utexas.edu/site-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://security.utexas.edu/policies
- group: operate
  title: ''
  type: Support
  url: https://tacc.utexas.edu/about/help/
- group: company
  title: ''
  type: Blog
  url: https://news.utexas.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-texas-at-austin/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-texas-at-austin-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-texas-at-austin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-texas-at-austin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-texas-at-austin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Texas at Austin is a flagship public research university in Austin, Texas, United States, and the largest institution in the University of Texas System. It operates no central developer portal, publishes no institution-wide API catalog, and its enterprise integration APIs (Identity and Access Management, student and financial systems) are gated behind UT EID authentication and an internal ServiceNow request process, so they are not publicly readable. What UT Austin does genuinely operate and expose publicly is narrower and more specific than a portal: the Tapis v3 research-computing platform, designed, built and run by the Texas Advanced Computing Center — an organized research unit of UT Austin — which serves five OpenAPI-described services (Systems, Files, Apps, Jobs, Notifications) on its production TACC tenant; an InCommon-registered Shibboleth identity provider publishing both SAML 2.0 metadata and an OpenID Connect discovery document; and Texas ScholarWorks,
  the UT Libraries DSpace repository, with a public REST API and an OAI-PMH 2.0 harvesting endpoint on the university''s own host. Its research-data archive is a tenancy rather than an operation: UT Austin publishes into a Dataverse collection on the Texas Digital Library''s shared instance, and the library discovery layer is Ex Libris Primo. Both are recorded here as relationships, not as UT Austin engineering.'
examples:
- key_count: 26
  name: University Of Texas At Austin Idp Openid Configuration
  slug: university-of-texas-at-austin-idp-openid-configuration
- key_count: 6
  name: University Of Texas At Austin Scholarworks Dspace Root
  slug: university-of-texas-at-austin-scholarworks-dspace-root
- key_count: 7
  name: University Of Texas At Austin Tapis Systems Healthcheck
  slug: university-of-texas-at-austin-tapis-systems-healthcheck
- key_count: 2
  name: University Of Texas At Austin Tdr Dataverse Collection
  slug: university-of-texas-at-austin-tdr-dataverse-collection
finops:
- name: University Of Texas At Austin Finops
  service_category: Education
  slug: university-of-texas-at-austin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-texas-at-austin.png
jsonld:
- class_count: 11
  name: University Of Texas At Austin Context
  property_count: 3
  slug: university-of-texas-at-austin-context
layout: provider
modified: '2026-08-30'
name: University of Texas at Austin
nav: Providers
network: true
overview: 'University of Texas at Austin publishes 1 API on the [APIs.io](https://apis.io/) network: Tapis v3 Research Computing Platform (TACC production tenant). Tagged areas include University, Higher Education, Education, Public Research University, and United States.


  The University of Texas at Austin catalog on APIs.io includes 1 JSON-LD context.


  University of Texas at Austin''s developer surface includes documentation, API reference, support, engineering blog, and 18 more developer resources.'
plans:
- name: University Of Texas At Austin Plans Pricing
  plan_count: 2
  slug: university-of-texas-at-austin-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: University Of Texas At Austin Rate Limits
  slug: university-of-texas-at-austin-rate-limits
scopes:
- name: University Of Texas At Austin Scopes
  scope_count: 0
  slug: university-of-texas-at-austin-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.8
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 62.5
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 50.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: University Of Texas At Austin Authentication
  slug: university-of-texas-at-austin-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Texas At Austin Domain Security
  slug: university-of-texas-at-austin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-texas-at-austin
tags:
- University
- Higher Education
- Education
- Public Research University
- United States
- Texas
- Research Computing
- Identity Federation
- Institutional Repository
- Research Data
- Library
- Open Data
website: https://www.utexas.edu/
---
