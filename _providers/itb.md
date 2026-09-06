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
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: ITB's campus-wide single sign-on, built on the Apereo CAS (Central Authentication Service) protocol and running on ITB's own host login.itb.ac.id. The CAS 2.0 and CAS 3.0 ticket-validation endpoints a
  name: ITB Single Sign-On (CAS)
  slug: sso-cas
- description: ITB's scholarly journal platform at journals.itb.ac.id, hosted on ITB's own domain and administered by ITB (OAI Identify returns repositoryName "ITB Journals" and adminEmail journal@itb.ac.id). It exp
  name: ITB Journals OAI-PMH
  slug: journals-oai
- description: ITB is a registered Crossref member through its Institute for Research and Community Services (LPPM), which registers the DOIs for the ITB journal titles published on journals.itb.ac.id. Member ID 361
  name: Crossref Membership (LPPM ITB)
  slug: crossref-membership
- description: ITB is registered in the Research Organization Registry as https://ror.org/00apj8t60 ("Bandung Institute of Technology", acronym ITB, Indonesian label "Institut Teknologi Bandung"). Verified live 2026
  name: ROR Registration
  slug: ror-registration
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://itb.ac.id/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/institut-teknologi-bandung/
- group: auth
  title: ''
  type: Authentication
  url: https://login.itb.ac.id/
- group: other
  title: ''
  type: ResearchRepository
  url: https://digilib.itb.ac.id/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/STEI-ITB
- group: company
  title: ''
  type: Blog
  url: https://itb.ac.id/berita
- group: design
  title: ''
  type: Conformance
  url: conformance/itb-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/itb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/itb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/itb-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Institut Teknologi Bandung (ITB) is a public technical university in Bandung, Indonesia, and one of the country''s oldest and most selective engineering and science institutions. ITB publishes no developer portal, no API gateway, no API terms of service and no specification of any kind — api.itb.ac.id and data.itb.ac.id do not resolve, and no open-data portal was found. What it does operate, on its own domain and its own address space, are two protocol endpoints with no contract behind them: a campus-wide Apereo CAS single sign-on whose ticket-validation endpoints return machine-readable CAS XML, and an Open Journal Systems installation at journals.itb.ac.id that exposes a live, fully open OAI-PMH 2.0 data provider across twenty journal sets. Both are institution-operated; neither is institution-specified — the OJS software and its REST API are the Public Knowledge Project''s, and that REST API is credential-gated (403). ITB is additionally a registered Crossref member through
  its research institute LPPM (member 3613, DOI prefix 10.5614, 6,568 DOIs) and carries a ROR identifier. The Ganesha Digital Library repository is publicly browseable but its historical OAI-PMH and RSS endpoints stayed dead after a platform migration, and the library site lib.itb.ac.id now returns a database error. This profile records institution-operated surfaces with no institution-published contract, which is the honest result rather than a gap to be padded.'
finops:
- name: Itb Finops
  service_category: Education
  slug: itb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/itb.png
jsonld:
- class_count: 15
  name: Itb Context
  property_count: 2
  slug: itb-context
layout: provider
modified: '2026-09-01'
name: Bandung Institute of Technology
nav: Providers
network: true
overview: 'Bandung Institute of Technology publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Institute of Technology, and Research.


  The Bandung Institute of Technology catalog on APIs.io includes 1 JSON-LD context.


  Bandung Institute of Technology''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Itb Plans Pricing
  plan_count: 2
  slug: itb-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Itb Rate Limits
  slug: itb-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 17.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 30.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/itb/refs/heads/main/screenshots/itb-2026-06-20T183631.png
security:
- kind: domain-security
  name: Itb Domain Security
  slug: itb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: itb
tags:
- Education
- Higher Education
- University
- Institute of Technology
- Research
- Indonesia
- Southeast Asia
- Authentication
- Single Sign-On
- Scholarly Publishing
- OAI-PMH
- Digital Library
- Research Repository
website: https://itb.ac.id/
---
