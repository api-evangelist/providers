---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Memo Therapeutics website at memo-therapeutics.com: the route index of the site''s content management system, catalogued as one site surface rather than a'
  name: Memo Therapeutics Website (WordPress REST)
  slug: memo-therapeutics-com-website-wordpress-rest
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/memo-therapeutics/security/memo-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memo-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memo-therapeutics.com/
- group: company
  title: ''
  type: About
  url: https://memo-therapeutics.com/about-us/
- group: company
  title: ''
  type: News
  url: https://memo-therapeutics.com/latest-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://memo-therapeutics.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://memo-therapeutics.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memo-therapeutics.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memo-therapeutics.com/terms-and-conditions/
- group: other
  title: ''
  type: CookiePolicy
  url: https://memo-therapeutics.com/cookie-policy/
- group: other
  title: ''
  type: PatientResources
  url: https://memo-therapeutics.com/expanded-access-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://memo-therapeutics.com/further-information/
- group: other
  title: ''
  type: Science
  url: https://memo-therapeutics.com/bkv/
- group: company
  title: ''
  type: Careers
  url: https://www.ipsen.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/memo-therapeutics-ag/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.ipsen.com/
- group: other
  title: ''
  type: Sitemap
  url: https://memo-therapeutics.com/sitemap.xml
- group: auth
  href: https://artifacts.apis.io/memo-therapeutics/authentication/memo-therapeutics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/memo-therapeutics-authentication.yml
- group: design
  href: https://artifacts.apis.io/memo-therapeutics/conventions/memo-therapeutics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/memo-therapeutics-conventions.yml
- group: design
  href: https://artifacts.apis.io/memo-therapeutics/conformance/memo-therapeutics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/memo-therapeutics-conformance.yml
- group: design
  href: https://artifacts.apis.io/memo-therapeutics/errors/memo-therapeutics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/memo-therapeutics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/memo-therapeutics/lifecycle/memo-therapeutics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/memo-therapeutics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/memo-therapeutics/data-model/memo-therapeutics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/memo-therapeutics-data-model.yml
- group: operate
  href: https://artifacts.apis.io/memo-therapeutics/rate-limits/memo-therapeutics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/memo-therapeutics-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/memo-therapeutics/plans/memo-therapeutics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/memo-therapeutics-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/memo-therapeutics/overlays/memo-therapeutics-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/memo-therapeutics-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/memo-therapeutics/llms/memo-therapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/memo-therapeutics-llms.txt
- group: agent
  href: https://artifacts.apis.io/memo-therapeutics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: Memo Therapeutics AG ("MTx"), an Ipsen company, is a late-stage biotechnology company headquartered at Wagistrasse 27 in Schlieren / Zurich, Switzerland, with a US office as Memo Therapeutics US, Inc. in Wilson, North Carolina. It develops best-in-class therapeutic antibodies to transform the lives of patients with viral infections and cancer, built on DROPZYLLA, a microfluidic single-cell platform that makes a recombinant in vitro copy of an individual donor's B-cell antibody repertoire, banks it as a library, and screens it functionally at high throughput. Its lead program, potravitug, is a first-in-class monoclonal antibody against BK polyomavirus (BKPyV) reactivation in kidney transplant recipients; the Phase II SAFE KIDNEY II trial reported biopsy-proven resolution of BKPyV-associated nephropathy with sustained viral-load reduction to week 38, and the asset holds EU orphan designation. In February 2026 the company entered a collaboration and option agreement with CSL for
  its recombinant polyclonal IgG technology carrying milestones of up to CHF 265 million, and it has run an oncology antibody-discovery collaboration with Ono Pharmaceutical since 2022 alongside nephrology collaborations with the University Hospital of Zurich and the University Hospital of Bern. Ipsen completed its acquisition of Memo Therapeutics AG on 22 July 2026, adding potravitug to Ipsen's rare-disease pipeline. Memo Therapeutics runs no developer program and publishes no product API, developer portal, SDK or API documentation. The only machine-readable surface reachable without credentials is the WordPress REST content API behind memo-therapeutics.com, catalogued here, together with an llms.txt the site's SEO plugin publishes.
image: https://memo-therapeutics.com/wp-content/uploads/2024/07/memo-therapeutics-ipsen-logo.webp
layout: provider
modified: '2026-08-25'
name: Memo Therapeutics
nav: Providers
network: true
overview: 'Memo Therapeutics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Antibody Therapeutics, and Rare Disease.


  Memo Therapeutics'' developer surface includes product news, authentication, and 25 more developer resources.'
plans:
- name: Memo Therapeutics Plans Pricing
  plan_count: 0
  slug: memo-therapeutics-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Memo Therapeutics Rate Limits
  slug: memo-therapeutics-rate-limits
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 18.5
    discoverability: 65.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 18.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/memo-therapeutics/memo-therapeutics-2026-10-11T111010.png
security:
- kind: authentication
  name: Memo Therapeutics Authentication
  slug: memo-therapeutics-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Memo Therapeutics Domain Security
  slug: memo-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: memo-therapeutics-content-discovery
  slug: memo-therapeutics-content-discovery
- name: memo-therapeutics-corporate-documents
  slug: memo-therapeutics-corporate-documents
- name: memo-therapeutics-track-news
  slug: memo-therapeutics-track-news
slug: memo-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Antibody Therapeutics
- Rare Disease
- Nephrology
- transplantation
- virology
- Oncology
- Clinical Trials
- Life Sciences
- Switzerland
- content-api
website: https://memo-therapeutics.com/
---
