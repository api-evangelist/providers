---
access_model:
  confidence: medium
  label: Free · affiliation or request gated
  onboarding: unknown
  pricing: free
  public: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.8
  scored_at: '2026-09-03'
api_count: 7
apis:
- description: DTU operates its own security token service at sts.ait.dtu.dk (Microsoft AD FS) and publishes signed SAML 2.0 metadata and an OpenID Connect discovery document, both openly and without authentication.
  name: DTU Identity Federation (SAML 2.0 / WS-Federation / OpenID Connect)
  slug: identity-federation
- description: 'An OGC Web Processing Service 1.0.0 serving Global Wind Atlas results. The GetCapabilities document names DTU Wind Energy as the ows:ServiceProvider, with a Risø Campus, Roskilde address and a dtu.dk '
  name: Global Wind Atlas Web Processing Service
  slug: global-wind-atlas-wps
- description: 'DTU Library''s discovery interface, running on DTU''s own host on the open-source Blacklight stack rather than on a vendor SaaS domain. It publishes an OpenSearch 1.1 description document that resolves '
  name: DTU Findit — library discovery
  slug: findit
- description: DTU Data is DTU's institutional research data repository — DTU's records, DTU's DOIs, Figshare's platform and Figshare's contract. DTU records are scoped by Figshare institution id 379. The API that s
  name: DTU Data research data repository (Figshare tenant)
  slug: dtu-data
- description: DTU Orbit is DTU's research information database — publications, projects, activities, researcher and department profiles — deployed on Elsevier Pure. The public portal is on DTU's own host but is ser
  name: DTU Orbit research database (Elsevier Pure tenant)
  slug: orbit
- description: 'DTU''s learning management system, a D2L Brightspace deployment on a dtu.dk subdomain. Brightspace holds IMS Global LTI certification as a product, but that certification is D2L''s and DTU publishes no '
  name: DTU Learn (D2L Brightspace tenant)
  slug: learn
- description: 'DTU''s own course catalogue and timetable system, on DTU''s own host. It is not open: every path returns a small shell that forces a sign-in redirect, so no course data is machine-readable without insti'
  name: DTU course base (kurser.dtu.dk)
  slug: course-catalog
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.dtu.dk/english
- group: other
  title: ''
  type: IdentityFederation
  url: https://sts.ait.dtu.dk/FederationMetadata/2007-06/FederationMetadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://data.dtu.dk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://findit.dtu.dk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://kurser.dtu.dk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.hpc.dtu.dk/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.ai.dtu.dk/rules/
- group: build
  title: ''
  type: AITooling
  url: https://www.ai.dtu.dk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dtudk
- group: build
  title: ''
  type: GitHub
  url: https://github.com/DTUWindEnergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/technical-university-of-denmark/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dtu.dk/english/about/strategy-policy/policies/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/dtu-authentication.yml
- group: design
  title: ''
  type: x-conformance
  url: conformance/dtu-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dtu-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dtu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dtu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dtu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.dtu.dk/english/news/all-news
created: '2026-06-03'
description: 'The Technical University of Denmark (DTU) is a technical university in Kongens Lyngby, Denmark. DTU operates no central developer portal and publishes no OpenAPI-described public REST API of its own. Its two clearly institution-operated machine-readable surfaces are its identity federation — a DTU-run SAML 2.0 / WS-Federation / OpenID Connect token service at sts.ait.dtu.dk, registered in the Danish national federation WAYF and in eduGAIN — and the Global Wind Atlas OGC Web Processing Service, whose GetCapabilities document names DTU Wind Energy as the service provider with a dtu.dk contact. Everything that previously read as a DTU API was not: DTU Data (data.dtu.dk) is a Figshare tenant and DTU Orbit (orbit.dtu.dk) is an Elsevier Pure deployment, and both are recorded here as tenant relationships rather than DTU contracts. DTU Learn is a D2L Brightspace tenant. The course catalogue at kurser.dtu.dk is DTU-operated but sign-in gated. DTU maintains public GitHub organizations
  (dtudk, DTUWindEnergy) hosting affiliated open-source software.'
finops:
- name: Dtu Finops
  service_category: Education
  slug: dtu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dtu.png
layout: provider
modified: '2026-08-30'
name: Technical University of Denmark
nav: Providers
network: true
overview: 'Technical University of Denmark publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Technical University, and Denmark.


  Technical University of Denmark''s developer surface includes GitHub presence, authentication, engineering blog, and 17 more developer resources.'
plans:
- name: Dtu Plans Pricing
  plan_count: 2
  slug: dtu-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Dtu Rate Limits
  slug: dtu-rate-limits
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 20.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 29.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dtu/refs/heads/main/screenshots/dtu-2026-06-20T180302.png
security:
- kind: authentication
  name: Dtu Authentication
  slug: dtu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dtu Domain Security
  slug: dtu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dtu
tags:
- Education
- Higher Education
- University
- Technical University
- Denmark
- Europe
- Identity Federation
- Research Data
- Library
- Course Catalog
- Wind Energy
website: https://www.dtu.dk/english
---
