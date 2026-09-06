---
access_model:
  confidence: high
  label: Free · No signup for the public library endpoints
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probes
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 7
apis:
- description: The REST API of Loughborough University Library's Koha integrated library system, served from the university's own koha.lboro.ac.uk host. The live description at /api/v1/ is a Swagger 2.0 document dec
  name: Loughborough University Library Catalogue API (Koha)
  slug: library-catalogue-api
- description: Loughborough's virtual learning environment, "Learn", is a Moodle instance self-hosted at learn.lboro.ac.uk in the university's own 158.125.161.0/24 address space. It runs as a 1EdTech (IMS Global) LT
  name: Loughborough Learn — LTI 1.3 Advantage Platform (Moodle)
  slug: learn-lti-platform
- description: 'Loughborough operates its own SAML 2.0 Identity Provider — SimpleSAMLphp, Loughborough-branded, at idp.lboro.ac.uk — and is registered in the UK Access Management Federation, which feeds eduGAIN. The '
  name: Loughborough University SAML 2.0 Identity Provider
  slug: identity-federation
- description: VuFind discovery layer at vufind.lboro.ac.uk, the public search interface over the Koha catalogue, on managed hosting by PTFS Europe (CNAME lboro-vufind.infrastructure.servers.ptfse.net). VuFind's Sea
  name: Loughborough University Library Discovery (VuFind)
  slug: vufind-discovery
- description: 'The Loughborough Research Repository is the university''s institutional repository for all research outputs, and it is a figshare tenancy: repository.lboro.ac.uk, lboro.figshare.com and the legacy dspa'
  name: Loughborough University Research Repository (figshare tenancy)
  slug: research-repository
- description: 'Loughborough''s reading lists run on Talis Aspire at lboro.rl.talis.com. The tenancy exposes linked data: https://lboro.rl.talis.com/index.json returns 200 application/json describing the institution i'
  name: Loughborough University Reading Lists (Talis Aspire tenancy)
  slug: reading-lists
- description: Room booking, opening hours and library event data run on Springshare LibCal at libcal.lboro.ac.uk (CNAME region-eu.libcal.com). The legacy keyless widget endpoint /api_hours_grid.php?iid=0&format=jso
  name: Loughborough University Library Hours and Bookings (Springshare LibCal tenancy)
  slug: libcal
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.lboro.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://koha.lboro.ac.uk/api/v1/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.lboro.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: http://metadata.ukfederation.org.uk/ukfederation-metadata.xml
- group: design
  title: ''
  type: Conformance
  url: conformance/loughborough-conformance.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LoughboroughUniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/school/loughborough-university/
- group: company
  title: ''
  type: Blog
  url: https://www.lboro.ac.uk/news-events/rss/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lboro.ac.uk/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lboro.ac.uk/disclaimer/
- group: operate
  title: ''
  type: Support
  url: https://www.lboro.ac.uk/services/it/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lboro.ac.uk/services/library/research-support/
- group: other
  title: ''
  type: ProductPage
  url: https://www.lboro.ac.uk/services/it/topics/student-account/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loughborough-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/loughborough-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loughborough-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loughborough-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Loughborough University is a public research university in Leicestershire, United Kingdom, a member of the Midlands Innovation group, established 1909 and best known for sport science, engineering and design. It publishes no central developer portal, no open-data portal and no first-party OpenAPI, and no such thing was generated for it here. Two surfaces are unambiguously the university''s own and are recorded as such: a self-hosted Moodle ("Learn") on Loughborough''s own address space running as a 1EdTech LTI 1.3 Advantage platform with a publicly readable JWKS, and a SimpleSAMLphp SAML 2.0 Identity Provider registered in the UK Access Management Federation. Five more carry Loughborough''s data on someone else''s platform and are recorded as tenancies: a Koha library system whose REST API serves a live Swagger 2.0 description and nineteen keyless /public endpoints — the single most usable programmable surface the institution has, and hosted by PTFS Europe; a VuFind discovery
  layer whose Search API is deployed but closed; the Loughborough Research Repository, a figshare tenancy; Talis Aspire reading lists; and Springshare LibCal. Loughborough is also a DataCite member in its own right. No contract is stored under this slug, because none of the contracts are Loughborough''s to claim.'
examples:
- key_count: 7
  name: Loughborough Koha Public Libraries Example
  slug: loughborough-koha-public-libraries-example
- key_count: 7
  name: Loughborough Moodle Lti Jwks Example
  slug: loughborough-moodle-lti-jwks-example
finops:
- name: Loughborough Finops
  service_category: Education
  slug: loughborough-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loughborough.png
layout: provider
modified: '2026-08-30'
name: Loughborough University
nav: Providers
network: true
overview: 'Loughborough University publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, United Kingdom, and Library.


  Loughborough University''s developer surface includes engineering blog, support, documentation, and 15 more developer resources.'
plans:
- name: Loughborough Plans Pricing
  plan_count: 2
  slug: loughborough-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Loughborough Rate Limits
  slug: loughborough-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 27.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loughborough/refs/heads/main/screenshots/loughborough-2026-06-20T184729.png
security:
- kind: domain-security
  name: Loughborough Domain Security
  slug: loughborough-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loughborough
tags:
- Education
- Higher Education
- University
- United Kingdom
- Library
- Library Catalog
- Identity Federation
- Learning Management
- Research Data
- Open Access
- Repository
website: https://www.lboro.ac.uk/
---
