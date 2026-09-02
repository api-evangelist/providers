---
access_model:
  confidence: high
  label: Free · No registration · No developer programme
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - authentication
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
  score: 20.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: McGill's SAML 2.0 identity provider and the only machine-readable surface in this profile that McGill itself operates. The federation metadata document at /idp/shibboleth is served unauthenticated (HT
  name: McGill University Authentication Service — Shibboleth SAML 2.0 Identity Provider
  slug: shibboleth-idp
- description: McGill's institutional research repository, running as a tenant on Scholaris. It exposes a DSpace REST (HAL) root at /server/api and a conformant OAI-PMH 2.0 endpoint at /server/oai/request advertisin
  name: eScholarship@McGill on Scholaris (tenant)
  slug: escholarship-scholaris
- description: McGill's research-data collection on Borealis, the Canadian consortial Dataverse repository. The collection, its datasets and its DOIs are McGill's. The Dataverse Native and Search REST APIs that serv
  name: McGill University Dataverse on Borealis (tenant)
  slug: dataverse-borealis
- description: McGill's official course catalogue, published on CourseLeaf. It carries an undocumented but live machine-readable course-detail endpoint — GET /ribbit/index.cgi?page=getcourse.rjs with a space-separat
  name: McGill Course Catalogue on CourseLeaf (tenant)
  slug: coursecatalogue-courseleaf
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.mcgill.ca/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.mcgill.ca/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://mcgill.scholaris.ca/
- group: other
  title: ''
  type: OpenData
  url: https://borealisdata.ca/dataverse/mcgill
- group: learn
  title: ''
  type: CourseCatalog
  url: https://coursecatalogue.mcgill.ca/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.mcgill.ca/libraries/
- group: build
  title: ''
  type: AITooling
  url: https://www.mcgill.ca/it/ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/mcgill-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcgill-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mcgill.ca/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mcgill.ca/secretariat/repository-university-policies-and-regulations
- group: operate
  title: ''
  type: Support
  url: https://www.mcgill.ca/it/support
- group: company
  title: ''
  type: Blog
  url: https://www.mcgill.ca/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mcgill.ca/newsroom/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/mcgill-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/mcgillu
- group: commercial
  title: ''
  type: Plans
  url: plans/mcgill-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mcgill-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mcgill-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'McGill University is a public research university in Montreal, Quebec, Canada, and one of Canada''s two U15 institutions in the global top 100. Its programmable footprint is small and must be described honestly: McGill operates no developer portal, publishes no API key programme, and runs no OAuth authorization server. Exactly one machine-readable surface is operated by the institution itself — the Shibboleth SAML 2.0 identity provider at shibboleth.mcgill.ca, whose federation metadata is served unauthenticated at /idp/shibboleth and carries entityID and shibmd:Scope of mcgill.ca. Everything else that looks like a McGill API is a platform McGill is a tenant on: eScholarship@McGill runs on Scholaris (Scholars Portal / OCUL DSpace 7) at mcgill.scholaris.ca, which serves a DSpace REST root and a valid OAI-PMH 2.0 endpoint; the McGill University Dataverse is a collection on Borealis (borealisdata.ca), a consortial host shared with five other institutions in this catalog; the course
  catalogue at coursecatalogue.mcgill.ca is a CourseLeaf instance CNAMEd to mcgill-ca-public.courseleaf.com. Those relationships are real institutional facts and are recorded as tenant surfaces — the data is McGill''s, the contracts are not. Registration, library discovery and HR run on Banner/Minerva, WorldCat and Workday behind authentication with no public interface.'
finops:
- name: Mcgill Finops
  service_category: Education
  slug: mcgill-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mcgill.png
layout: provider
modified: '2026-08-30'
name: McGill University
nav: Providers
network: true
overview: 'McGill University publishes 1 API on the [APIs.io](https://apis.io/) network: Authentication Service — Shibboleth SAML 2.0 Identity Provider. Tagged areas include University, Higher Education, Education, Canada, and Quebec.


  The McGill University catalog on APIs.io includes 1 Spectral governance ruleset.


  McGill University''s developer surface includes authentication, support, engineering blog, and 17 more developer resources.'
plans:
- name: Mcgill Plans Pricing
  plan_count: 2
  slug: mcgill-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Mcgill Rate Limits
  slug: mcgill-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: McGill University API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: mcgill-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 44.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 45.5
    contract_quality: 48.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 45.5
    operational_transparency: 21.1
  previous_composite: 41.6
  provenance:
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
    score: 37.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mcgill/refs/heads/main/screenshots/mcgill-2026-06-20T185057.png
security:
- kind: authentication
  name: Mcgill Authentication
  slug: mcgill-authentication
  summary_line: saml/none · 2 schemes
- kind: domain-security
  name: Mcgill Domain Security
  slug: mcgill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mcgill
tags:
- University
- Higher Education
- Education
- Canada
- Quebec
- U15
- Public Research University
- Identity Federation
- Research Repository
- Research Data
- Course Catalog
website: https://www.mcgill.ca/
---
