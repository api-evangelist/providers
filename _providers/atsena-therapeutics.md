---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Atsena Therapeutics website at atsenatx.com: the route index of the site''s content management system, catalogued as one site surface rather than as separ'
  name: Atsena Therapeutics Website (WordPress REST)
  slug: atsenatx-com-website-wordpress-rest
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Collection
  slug: open-atsena-therapeutics-wp-rest-discovery-original
common:
- group: company
  title: ''
  type: Website
  url: https://atsenatx.com/
- group: company
  title: ''
  type: About
  url: https://atsenatx.com/about/overview/
- group: company
  title: ''
  type: Blog
  url: https://atsenatx.com/news/
- group: company
  title: ''
  type: News
  url: https://atsenatx.com/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://atsenatx.com/news/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://atsenatx.com/feed/
- group: other
  title: ''
  type: Publications
  url: https://atsenatx.com/news/presentations-and-publications/
- group: other
  title: ''
  type: Pipeline
  url: https://atsenatx.com/programs/pipeline/
- group: other
  title: ''
  type: Technology
  url: https://atsenatx.com/our-approach/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://atsenatx.com/clinical-trials/
- group: other
  title: ''
  type: Patients
  url: https://atsenatx.com/for-patients/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atsenatx.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://atsenatx.com/contact/
- group: operate
  title: ''
  type: Contact
  url: https://atsenatx.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://atsenatx.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atsenatx
- group: company
  title: ''
  type: Investors
  url: https://atsenatx.com/about/investors/
- group: company
  title: ''
  type: Partners
  url: https://atsenatx.com/about/partners/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/atsena-therapeutics_stock/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/overlays/atsena-therapeutics-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/atsena-therapeutics-wp-rest-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/authentication/atsena-therapeutics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atsena-therapeutics-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/conventions/atsena-therapeutics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/atsena-therapeutics-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/errors/atsena-therapeutics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/atsena-therapeutics-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/data-model/atsena-therapeutics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atsena-therapeutics-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/lifecycle/atsena-therapeutics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/atsena-therapeutics-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/conformance/atsena-therapeutics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atsena-therapeutics-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/well-known/atsena-therapeutics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atsena-therapeutics-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/security/atsena-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atsena-therapeutics-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/llms/atsena-therapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atsena-therapeutics-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'Atsena Therapeutics is a clinical-stage gene therapy company based in Durham, North Carolina, in the Research Triangle, developing first- and best-in-class genetic medicines for inherited retinal diseases with the goal of reversing or preventing blindness. Founded by ocular gene therapy pioneers Shannon Boye and Sanford Boye, the company builds on two proprietary AAV delivery platforms: a laterally spreading AAV.SPR capsid engineered to reach retinal cells without the surgical trauma of a subretinal bleb, and a dual-vector technology that splits genes too large for a single AAV across two vectors. Its clinical pipeline includes ATSN-201 for X-linked retinoschisis (XLRS) in a pivotal Phase 3 trial, ATSN-101 for LCA1 (Leber congenital amaurosis 1) advancing to a pivotal trial with partner Nippon Shinyaku, and IND-enabling programs ATSN-301 for Usher syndrome 1B and ATSN-401 for Stargardt disease. Atsena runs no developer program and publishes no product API, no developer documentation
  and no specification of its own. The only machine-readable surface it exposes is the anonymously readable WordPress REST content API behind atsenatx.com, which serves the company''s press releases, program and platform pages, and media library as JSON; the OpenAPI in this repo is derived by API Evangelist from that surface''s own live route index.'
image: https://atsenatx.com/wp-content/themes/atsenatx/img/touch-icon-ipad-retina.png
layout: provider
modified: '2026-08-02'
name: Atsena Therapeutics
nav: Providers
network: true
overview: 'Atsena Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network: Website (WordPress REST). Tagged areas include Company, Biotechnology, Gene Therapy, Life Sciences, and Pharmaceuticals.


  Atsena Therapeutics'' developer surface includes engineering blog, product news, support, authentication, and 26 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 8.3
    developer_ergonomics: 30.4
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/atsena-therapeutics/refs/heads/main/screenshots/atsena-therapeutics-2026-08-07T161907.png
security:
- kind: authentication
  name: Atsena Therapeutics Authentication
  slug: atsena-therapeutics-authentication
  summary_line: none/http/apiKey · 3 schemes
- kind: domain-security
  name: Atsena Therapeutics Domain Security
  slug: atsena-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atsena-therapeutics
tags:
- Company
- Biotechnology
- Gene Therapy
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Ophthalmology
- Rare Disease
- Healthcare
- Research and Development
- content-api
- WordPress
website: https://atsenatx.com/
---
