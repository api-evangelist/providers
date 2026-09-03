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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 8
apis:
- description: USC's production single sign-on identity provider, operated by USC Information Technology Services on USC's own host, publishing its SAML 2.0 metadata unauthenticated. GET https://shibboleth.usc.edu/i
  name: USC Shibboleth Identity Provider (SAML 2.0 Metadata)
  slug: shibboleth-idp
- description: Keyless, read-only JSON REST API of the FaceBase craniofacial data hub, an NIDCR-funded resource led from USC and engineered by USC's Information Sciences Institute. GET https://www.facebase.org/ermre
  name: FaceBase ERMrest Data API
  slug: facebase-ermrest
- description: USC holds a DataCite direct membership in its own name and mints DOIs for eleven USC repositories under it. GET https://api.datacite.org/providers/usc returns 200 with name "University of Southern Cal
  name: USC DataCite DOI Registration (Provider Account)
  slug: datacite-membership
- description: A live, token-gated REST API on USC's own host running Orange Logic's Cortex digital asset platform. GET https://digitallibrary.usc.edu/API/search/v3.0/search?query=test&format=json returns 401 applic
  name: USC Digital Library API (Orange Logic Cortex)
  slug: digital-library-cortex
- description: 'USC Libraries offers Figshare to USC researchers as its data-output repository for datasets, posters and presentations, at the institution-specific tenant usc.figshare.com. Probed 2026-08-30 the host '
  name: USC Figshare Research Repository (Tenant)
  slug: figshare-repository
- description: USC Libraries' catalog and discovery layer runs on Ex Libris Primo VE as institution view 01USC_INST:01USC at uosc.primo.exlibrisgroup.com. The public Primo configuration REST endpoint /primaws/rest/p
  name: USC Libraries Discovery (Ex Libris Primo VE, Tenant)
  slug: primo-discovery
- description: USC's learning management system is an Instructure Canvas tenant at usc.instructure.com, verified live 2026-08-30 (200, redirecting to /login/canvas). Canvas exposes a substantial REST API and is an L
  name: USC Canvas Learning Management System (Instructure, Tenant)
  slug: canvas-lms
- description: USC's Schedule of Classes Web Services API, which exposed terms, departments, courses and sections and once powered the online schedule, is retired. Its host, web-app.usc.edu, no longer resolves at al
  name: USC Schedule of Classes (SOC) — Web Services API, retired
  slug: schedule-of-classes
artifact_total: 13
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/informatics-isi-edu/ermrest/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.usc.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.usc.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.usc.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://usc.figshare.com/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://uosc.primo.exlibrisgroup.com/discovery/search?vid=01USC_INST:01USC
- group: learn
  title: ''
  type: CourseCatalog
  url: https://classes.usc.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://catalogue.usc.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.carc.usc.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://www.carc.usc.edu/user-guides
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.usc.edu/policy-and-governance/
- group: build
  title: ''
  type: AITooling
  url: https://ai.usc.edu/tools/
- group: docs
  title: ''
  type: APIReference
  url: https://www.facebase.org/ermrest/catalog/1/schema
- group: operate
  title: ''
  type: Support
  url: https://itservices.usc.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/informatics-isi-edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/USCDataScience
- group: build
  title: ''
  type: GitHub
  url: https://github.com/isi-usc-edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/usc-its
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usc.edu/privacy-notice/
- group: other
  title: ''
  type: Accessibility
  url: https://accessibility.usc.edu/accessibility-at-usc/digital-accessibility/
- group: other
  title: ''
  type: Policies
  url: https://policy.usc.edu/
- group: company
  title: ''
  type: Blog
  url: https://news.usc.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-southern-california/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/USC
- group: design
  title: ''
  type: Conformance
  url: conformance/usc-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usc-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/usc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usc-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/usc-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The University of Southern California is a private research university in Los Angeles, ranked #59 in the QS World University Rankings 2025. USC operates no central developer portal, publishes no OpenAPI, AsyncAPI or apis.json anywhere on its public surface, and issues no self-service API keys — www.usc.edu serves neither llms.txt nor .well-known/security.txt, and api.usc.edu is a default IIS Windows Server placeholder page last modified in 2019, not an API. What USC does operate, verified live on 2026-08-30, is three genuinely institutional machine surfaces: a Shibboleth SAML 2.0 identity provider whose metadata is published unauthenticated at shibboleth.usc.edu and registered with InCommon as urn:mace:incommon:usc.edu; a DataCite direct membership under its own name that carries eleven repositories and 1.5 million minted DOIs; and the FaceBase craniofacial data hub, whose keyless ERMrest REST API is built and run by USC''s own Information Sciences Institute on ISI''s Apache-2.0
  DERIVA stack. Everything else that looks like a USC API is a vendor''s contract running under USC''s name and is recorded here as a tenant relationship, never as USC''s engineering: Figshare, Ex Libris Primo/Alma, Orange Logic Cortex and Instructure Canvas. The Schedule of Classes Web Services API that this profile previously led with is gone — web-app.usc.edu no longer resolves at all.'
finops:
- name: Usc Finops
  service_category: Education
  slug: usc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usc.png
jsonld:
- class_count: 9
  name: Usc Context
  property_count: 4
  slug: usc-context
layout: provider
modified: '2026-08-30'
name: University of Southern California
nav: Providers
network: true
overview: 'University of Southern California publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and Private Research University.


  The University of Southern California catalog on APIs.io includes 1 JSON-LD context.


  University of Southern California''s developer surface includes documentation, API reference, support, GitHub presence, engineering blog, and 27 more developer resources.'
plans:
- name: Usc Plans Pricing
  plan_count: 2
  slug: usc-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Usc Rate Limits
  slug: usc-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 25.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usc/refs/heads/main/screenshots/usc-2026-06-20T200656.png
security:
- kind: domain-security
  name: Usc Domain Security
  slug: usc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: usc
tags:
- University
- Higher Education
- Education
- Research
- Private Research University
- Association of American Universities
- United States
- California
- Los Angeles
- Identity Federation
- Research Data
- Research Repository
- Library
- Course Catalog
- Research Computing
website: https://www.usc.edu/
---
