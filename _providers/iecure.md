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
    error_semantics: derived
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the iECURE website at iecure.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: iECURE Website (WordPress REST)
  slug: iecure-com-website-wordpress-rest
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://iecure.com/
- group: company
  title: ''
  type: About
  url: https://iecure.com/about/
- group: other
  title: ''
  type: Approach
  url: https://iecure.com/approach/
- group: other
  title: ''
  type: Pipeline
  url: https://iecure.com/programs/
- group: company
  title: ''
  type: News
  url: https://iecure.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://iecure.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://iecure.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://iecure.com/contact/
- group: other
  title: ''
  type: ExpandedAccessPolicy
  url: https://iecure.com/expanded-access-policy/
- group: other
  title: ''
  type: PatientResources
  url: https://otc-hope.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iecure.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iecure.com/privacy-notice/
- group: other
  title: ''
  type: CookieNotice
  url: https://iecure.com/cookie-notice/
- group: docs
  title: ''
  type: SocialMediaGuidelines
  url: https://iecure.com/social-media-community-guidelines/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iecure
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  href: https://artifacts.apis.io/iecure/authentication/iecure-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iecure-authentication.yml
- group: design
  href: https://artifacts.apis.io/iecure/conventions/iecure-conventions.yml
  title: ''
  type: Conventions
  url: conventions/iecure-conventions.yml
- group: design
  href: https://artifacts.apis.io/iecure/conformance/iecure-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iecure-conformance.yml
- group: design
  href: https://artifacts.apis.io/iecure/errors/iecure-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/iecure-problem-types.yml
- group: design
  href: https://artifacts.apis.io/iecure/lifecycle/iecure-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iecure-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/iecure/data-model/iecure-data-model.yml
  title: ''
  type: DataModel
  url: data-model/iecure-data-model.yml
- group: auth
  href: https://artifacts.apis.io/iecure/security/iecure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iecure-domain-security.yml
- group: other
  href: https://artifacts.apis.io/iecure/overlays/iecure-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iecure-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/iecure/llms/iecure-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iecure-llms.txt
- group: operate
  href: https://artifacts.apis.io/iecure/rate-limits/iecure-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iecure-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/iecure/plans/iecure-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iecure-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/iecure/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: iECURE is a clinical-stage genetic medicines company developing variant-agnostic, in vivo targeted gene insertion therapies for rare, life-threatening inherited metabolic diseases, with an initial focus on urea cycle disorders and other neurometabolic conditions of the liver. The company takes its name from iecur, the Latin word for liver, and was founded on the translational gene therapy research of James M. Wilson, M.D., Ph.D., advancing its pipeline in partnership with the University of Pennsylvania Gene Therapy Program. Its lead candidate, ECUR-506, pairs a dual-AAV delivery approach with Precision BioSciences' ARCUS nuclease to insert a functional copy of the OTC gene into the genome of infants with neonatal-onset ornithine transcarbamylase deficiency; it is in the OTC-HOPE study and has received FDA Orphan Drug, Rare Pediatric Disease, Fast Track and RMAT designations plus EU orphan designation, with clinical trial clearances in the United States, United Kingdom, Australia
  and the EU. Discovery-stage programs target citrullinemia type 1 and phenylketonuria. iECURE has raised roughly $115 million across a $50 million Series A in 2021 and a $65 million Series A-1 in 2022 from Versant Ventures, OrbiMed, Novo Holdings, the Qatar Investment Authority, LYFE Capital and Double Point Ventures. iECURE runs no developer program and publishes no product API, developer portal or API documentation. The only machine-readable surface reachable without credentials is the WordPress REST content API behind iecure.com, catalogued here.
image: https://iecure.com/wp-content/uploads/iECURE_White_Logo.png
layout: provider
modified: '2026-08-22'
name: iECURE
nav: Providers
network: true
overview: 'iECURE is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Genetic Medicine, Gene Editing, and Gene Therapy.


  iECURE''s developer surface includes product news, support, authentication, and 25 more developer resources.'
plans:
- name: Iecure Plans Pricing
  plan_count: 0
  slug: iecure-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Iecure Rate Limits
  slug: iecure-rate-limits
score:
  band: emerging
  composite: 17.0
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
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 65.2
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    conformance: derived
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
screenshot: https://apis.io/screenshots/iecure/iecure-2026-09-02T145828.png
security:
- kind: authentication
  name: Iecure Authentication
  slug: iecure-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Iecure Domain Security
  slug: iecure-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: iecure-harvest-media-library
  slug: iecure-harvest-media-library
- name: iecure-resolve-team-and-leadership
  slug: iecure-resolve-team-and-leadership
- name: iecure-track-news-archive
  slug: iecure-track-news-archive
slug: iecure
tags:
- Company
- Biotechnology
- Genetic Medicine
- Gene Editing
- Gene Therapy
- Rare Disease
- Clinical Trials
- Life Sciences
- Pharmaceuticals
- content-api
website: https://iecure.com/
---
