---
access_model:
  confidence: high
  label: Free and anonymous — the CKAN Action API needs no key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  - documentation
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: NCKU's institutional open data portal, a CKAN 2.0 deployment on NCKU's own host publishing 108 datasets from the university and its affiliated units — student enrolment and geographic distribution sta
  name: NCKU Open Data Platform (CKAN Action API)
  slug: opendata
- description: NCKU Library's catalog and discovery layer runs on Ex Libris Primo VE backed by Alma, under the NCKU tenant view 886NCKU_INST. The search interface is a Primo Angular application (primoExploreRoot) se
  name: NCKU Library discovery (Ex Libris Primo VE tenancy)
  slug: library-discovery
- description: NCKUR is NCKU's institutional repository — theses, dissertations and university scholarly output under handle prefix 987654321, with roughly 294 handle links on the front page alone. It self-identifie
  name: NCKU Institutional Repository (NCKUR, DSpace)
  slug: institutional-repository
- description: NCKU's Research Organization Registry record — ror.org/01b8kcc49, established 1931, status active, declared domain ncku.edu.tw — and the canonical machine-readable identifier for the institution itsel
  name: ROR organization record (01b8kcc49)
  slug: ror-registration
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.ncku.edu.tw/index.php?Lang=en
- group: other
  title: ''
  type: OpenData
  url: https://data.ncku.edu.tw/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.ncku.edu.tw/zh_TW/about
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ncku.primo.exlibrisgroup.com/discovery/search?vid=886NCKU_INST:886NCKU_INST&lang=zh-tw
- group: other
  title: ''
  type: ResearchRepository
  url: https://nckur.lib.ncku.edu.tw/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://course.ncku.edu.tw/
- group: other
  title: ''
  type: AIPolicy
  url: https://hsm.ncku.edu.tw/var/file/199/1199/img/434977937.pdf
- group: build
  title: ''
  type: AITooling
  url: https://sites.google.com/gs.ncku.edu.tw/nckuaiguidance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ncku-csie
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/national-cheng-kung-university/
- group: auth
  href: https://artifacts.apis.io/ncku/security/ncku-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ncku-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/ncku/plans/ncku-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ncku-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ncku/rate-limits/ncku-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ncku-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ncku/finops/ncku-finops.yml
  title: ''
  type: FinOps
  url: finops/ncku-finops.yml
- group: other
  href: https://artifacts.apis.io/ncku/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'National Cheng Kung University (NCKU, 國立成功大學) is a public research university in Tainan, Taiwan, founded in 1931 and the second-largest comprehensive university in the country. Its programmable footprint is narrow and almost entirely accounted for by one surface: the NCKU Open Data Platform at data.ncku.edu.tw, a CKAN 2.0 deployment NCKU runs on its own host and its own domain, carrying 108 datasets and two NCKU-authored CKAN extensions (nckumetadata, nckutemplatehelper), released under Taiwan''s Open Government Data License v1. Its Action API answers anonymous callers with valid JSON and is the only endpoint in this profile that returns machine-readable institutional data without credentials. Everything else is either a vendor tenancy or barely reachable. Library discovery is Ex Libris Primo VE under an NCKU tenant view (886NCKU_INST) and is recorded as a relationship, not as NCKU''s engineering — no Ex Libris contract is saved here. The NCKU institutional repository (NCKUR)
  at nckur.lib.ncku.edu.tw is NCKU''s own DSpace, confirmed live and self-identifying as "Powered By DSPACE, MIT" Version 7.0 during one of only three responsive windows in roughly thirty probes on 2026-09-01 — the host refuses TCP the rest of the time. No OAI-PMH or REST interface survived probing: /oai/request?verb=Identify returns a genuine 404 and every other candidate path fell inside a refusal window, so the 2026-06 profile''s DSpace REST and OAI-PMH claims stay unverified. NCKU''s Shibboleth identity provider resolves in DNS at idp.ncku.edu.tw but its ports do not answer from outside Taiwan, and Taiwan has no federation in eduGAIN, so the IdP is named as an unverified lead rather than credited as a surface. NCKU registers no DOI prefix with either DataCite or Crossref. There is no central developer portal, no API key program and no institution-authored OpenAPI anywhere on the ncku.edu.tw estate.'
finops:
- has_sources: true
  method: derived
  name: Ncku Finops
  primary_unit: ''
  service_category: Education
  slug: ncku-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ncku.png
jsonld:
- class_count: 24
  name: Ncku Context
  property_count: 0
  slug: ncku-context
layout: provider
modified: '2026-09-01'
name: National Cheng Kung University
nav: Providers
network: true
overview: 'National Cheng Kung University is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Taiwan, and Asia.


  The National Cheng Kung University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Ncku Plans Pricing
  plan_count: 2
  slug: ncku-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Ncku Rate Limits
  slug: ncku-rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 14.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ncku/ncku-2026-06-20T190150.png
security:
- kind: domain-security
  name: Ncku Domain Security
  slug: ncku-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ncku
tags:
- University
- Higher Education
- Education
- Taiwan
- Asia
- Public Research University
- Open Data
- CKAN
- Research Data
- Library
- Course Catalog
- Institutional Repository
website: https://www.ncku.edu.tw/index.php?Lang=en
---
