---
access_model:
  confidence: high
  label: Free · Open OAI-PMH harvesting, no signup; Pure REST is credentialed
  onboarding: unknown
  pricing: free
  public: true
  source:
  - conformance/aarhus-conformance.yml
  trial: false
  try_now: true
agent_readiness:
  band: human-only
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
  score: 5.0
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: 'Open Archives Initiative Protocol for Metadata Harvesting 2.0 service for Aarhus University''s research record. Verified live on 2026-08-30: the Identify verb returns repositoryName "Aarhus University"'
  name: Aarhus University OAI-PMH Metadata Service
  slug: pure-oai
- description: Aarhus University's deployment of the Elsevier Pure research information system REST API. The data is Aarhus's — its researchers, projects, research outputs and organisational units — and the deployme
  name: Elsevier Pure REST API — Aarhus University deployment
  slug: pure-rest
- description: kursuskatalog.au.dk is Aarhus University's public course catalogue, built and operated by the university on its own domain and served through AU's own CDN and font hosts. It is a web application only.
  name: Aarhus University Course Catalogue
  slug: course-catalogue
- description: timetable.au.dk is Aarhus University's timetabling service. The host is the university's own, but the product is MyTimetable by Semestry — the served page identifies itself as "Powered by MyTimetable,
  name: Aarhus University Timetable (MyTimetable)
  slug: timetable
- description: erda.au.dk is Aarhus University's Electronic Research Data Archive, running on the university's own infrastructure with AU and external user sign-in paths and companion hosts at int.erda.au.dk, cert.e
  name: Aarhus University ERDA Research Data Archive
  slug: erda
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.au.dk/en/
- group: company
  title: ''
  type: About
  url: https://www.au.dk/en/about/profile/
- group: other
  title: ''
  type: ResearchRepository
  url: https://pure.au.dk/portal/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://kursuskatalog.au.dk/en
- group: other
  title: ''
  type: IdentityFederation
  url: https://wayf.au.dk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://genome.au.dk/
- group: docs
  title: ''
  type: Documentation
  url: https://genome.au.dk/docs/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.au.dk/en
- group: other
  title: ''
  type: AIPolicy
  url: https://studerende.au.dk/en/gai
- group: build
  title: ''
  type: AITooling
  url: https://medarbejdere.au.dk/en/administration/it/guides/using-gai-responsibly
- group: other
  title: ''
  type: AIPolicy
  url: https://educate.au.dk/en/teaching-with-technology/chatbots
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://international.au.dk/about/profile/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://international.au.dk/about/profile/cookies-policy/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://au.dk/.well-known/security.txt
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cs-au-dk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/aarhus-university/
- group: design
  title: ''
  type: x-conformance
  url: conformance/aarhus-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aarhus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aarhus-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aarhus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aarhus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aarhus-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Aarhus University (Aarhus Universitet) is a public research university in Aarhus, Denmark, founded in 1928, with roughly 38,000 students across five faculties. It operates no central developer portal, no public API program, and no general-purpose institutional API — api.au.dk, data.au.dk, developer.au.dk and opendata.au.dk do not resolve. Its one genuinely institution-operated, publicly readable machine-readable surface is the OAI-PMH metadata harvesting service at pure.au.dk/ws/oai, which is live and fully functional: it identifies itself as the Aarhus University repository, is administered from pure@au.dk, offers five metadata profiles including the Danish national research-database formats, and emits ORCID iDs for Aarhus researchers. Everything else in the university''s programmable footprint is a vendor''s product running under the institution''s name — the Elsevier Pure research information REST API at pure.au.dk/ws/api (gated, HTTP 401 without a key, and an Elsevier contract
  regardless of the host it is served from), the Semestry MyTimetable service at timetable.au.dk, and the ERDA/MiG research data archive at erda.au.dk. The kursuskatalog.au.dk course catalogue and the mitstudie.au.dk student self-service environment are web applications with no documented API. Aarhus is a member of WAYF, Denmark''s national identity federation, and operates a SAML identity provider scoped to au.dk behind it. Code activity lives in departmental GitHub organisations such as cs-au-dk rather than in any central engineering programme.'
finops:
- name: Aarhus Finops
  service_category: Education
  slug: aarhus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aarhus.png
layout: provider
modified: '2026-08-30'
name: Aarhus University
nav: Providers
network: true
overview: 'Aarhus University publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and Research Repository.


  Aarhus University''s developer surface includes documentation, GitHub presence, and 21 more developer resources.'
plans:
- name: Aarhus Plans Pricing
  plan_count: 2
  slug: aarhus-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Aarhus Rate Limits
  slug: aarhus-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 54.0
    catalog_earned_first_party: 0.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 48.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aarhus/refs/heads/main/screenshots/aarhus-2026-06-20T163007.png
security:
- kind: domain-security
  name: Aarhus Domain Security
  slug: aarhus-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aarhus Vulnerability Disclosure
  slug: aarhus-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aarhus
tags:
- University
- Higher Education
- Education
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Research Computing
- Course Catalog
- Denmark
- Nordic
- Europe
website: https://www.au.dk/en/
---
