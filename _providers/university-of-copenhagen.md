---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://curis.ku.dk/ws/oai
  baseurl_source: declared
  description: A complete, unauthenticated OAI-PMH 2.0 repository operated by the university on its own host. verb=Identify names the repository "University of Copenhagen", gives adminEmail curis@adm.ku.dk and attri
  name: University of Copenhagen CURIS OAI-PMH Repository Interface
  slug: curis-oai-pmh
- description: The university publishes a signed SAML 2.0 EntityDescriptor at https://id.ku.dk/nidp/saml2/metadata (200, 24,737 bytes, text/xml), entityID https://id.ku.dk/nidp/saml2/metadata. Three ku.dk SAML entit
  name: University of Copenhagen SAML 2.0 Identity Provider
  slug: identity-federation
- description: The Natural History Museum of Denmark, a University of Copenhagen faculty museum, publishes thirteen Darwin Core Archive exports from the Faculty of Science's own host specify-snm.science.ku.dk — ento
  name: Natural History Museum of Denmark Darwin Core Archive Feeds
  slug: nhmd-darwin-core
- description: ERDA (erda.ku.dk, erda.dk, sid.erda.dk) is the university's research data archive, operated by the SCIENCE HPC Center at the Faculty of Science and skinned erda-ucph-science. UCPH users authenticate t
  name: Electronic Research Data Archive (ERDA) and SCIENCE HPC Center
  slug: erda
- description: kurser.ku.dk is the university's course catalogue, on a Copenhagen hostname running on Arcanic infrastructure (courses.loadbalancer.arcanic.dk). It serves human-readable course pages keyed by course c
  name: University of Copenhagen Course Catalogue
  slug: course-catalog
- description: 'researchprofiles.ku.dk is the university''s public research portal and the front end of CURIS. It is an Elsevier Pure tenancy, not Copenhagen''s engineering: the hostname CNAMEs researchprofiles.ku.dk -'
  name: University of Copenhagen Research Portal (Elsevier Pure tenancy)
  slug: research-portal-pure
- description: 'The university is an active DataCite member — provider symbol XIZZ, memberType consortium_organization, isActive true — with two registered repositories: xizz.curis ("CURIS", pointed at researchprofil'
  name: University of Copenhagen DataCite Membership (XIZZ)
  slug: datacite-xizz
- description: 'github.com/ku-kom is the university''s GitHub account — a User account rather than an Organization, named "University of Copenhagen" and linked to www.ku.dk — publishing 52 public repositories: the KU '
  name: University of Copenhagen Web Platform Source (ku-kom)
  slug: ku-kom-github
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-copenhagen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ku.dk/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ku-kom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ku-kom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-copenhagen/
- group: company
  title: ''
  type: Blog
  url: https://news.ku.dk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchprofiles.ku.dk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://id.ku.dk/nidp/saml2/metadata
- group: other
  title: ''
  type: OpenData
  url: https://specify-snm.science.ku.dk/static/depository/export_feed/DwCA-QZ.zip
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.ku.dk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://kurser.ku.dk/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-copenhagen-curis-oai-pmh-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-copenhagen-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-copenhagen-oai-pmh-errors.yml
- group: build
  title: ''
  type: Examples
  url: examples/university-of-copenhagen-curis-oai-pmh-examples.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-copenhagen-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-copenhagen-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-copenhagen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-copenhagen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-copenhagen-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Copenhagen (Københavns Universitet, UCPH), founded in 1479, is Denmark''s oldest and largest university and one of the leading research institutions in the Nordic region. It operates no central developer portal, no REST API program and no open-data portal — api.ku.dk and developer.ku.dk do not resolve, and data.ku.dk redirects to the homepage. What it does operate, and what makes it unusually well-covered for this cohort, is a set of standards-based machine-readable surfaces on its own infrastructure: a complete OAI-PMH 2.0 repository at curis.ku.dk serving 440,535 research records across 7,430 sets in six metadata formats; a signed SAML 2.0 identity provider at id.ku.dk registered in the Danish WAYF federation; and thirteen Darwin Core Archive feeds published by the Natural History Museum of Denmark from specify-snm.science.ku.dk and harvested by GBIF. Its public research portal researchprofiles.ku.dk is by contrast an Elsevier Pure tenancy — it CNAMEs to
  ku.elsevierpure.com and its REST contract is Elsevier''s, api-key gated — and is recorded here as a tenant relationship rather than as the university''s own API. The only source code the institution publishes is the ku-kom GitHub account: 52 repositories of TYPO3 content elements and a Bootstrap styleguide that build the ku.dk web platform.'
finops:
- name: University Of Copenhagen Finops
  service_category: Education
  slug: university-of-copenhagen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-copenhagen.png
jsonld:
- class_count: 9
  name: University Of Copenhagen Context
  property_count: 6
  slug: university-of-copenhagen-context
layout: provider
modified: '2026-08-30'
name: University of Copenhagen
nav: Providers
network: true
overview: 'University of Copenhagen publishes 1 API on the [APIs.io](https://apis.io/) network: CURIS OAI-PMH Repository Interface. Tagged areas include Education, Higher Education, University, Research, and Denmark.


  The University of Copenhagen catalog on APIs.io includes 1 JSON-LD context.


  University of Copenhagen''s developer surface includes GitHub presence, engineering blog, authentication, code examples, and 17 more developer resources.'
plans:
- name: University Of Copenhagen Plans Pricing
  plan_count: 2
  slug: university-of-copenhagen-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: University Of Copenhagen Rate Limits
  slug: university-of-copenhagen-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 60.3
    catalog_earned_first_party: 0.0
    catalog_gap: 54.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 8.3
    contract_quality: 22.3
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 8.3
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 29.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-copenhagen/refs/heads/main/screenshots/university-of-copenhagen-2026-06-20T200145.png
security:
- kind: authentication
  name: University Of Copenhagen Authentication
  slug: university-of-copenhagen-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Copenhagen Domain Security
  slug: university-of-copenhagen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-copenhagen
tags:
- Education
- Higher Education
- University
- Research
- Denmark
- Nordic
- Open-Source
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
- Open Data
- Research Computing
- Course Catalog
- Biodiversity
website: https://www.ku.dk/en
---
