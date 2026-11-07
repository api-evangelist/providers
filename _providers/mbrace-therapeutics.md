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
api_count: 9
apis:
- description: 'The public WordPress REST API (wp-json) of the MBrace Therapeutics website at mbracetrx.com: the route index of the site''s content management system, catalogued as one site surface rather than as sepa'
  name: MBrace Therapeutics Website (WordPress REST)
  slug: mbracetrx-com-website-wordpress-rest
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://mbracetrx.com/
- group: company
  title: ''
  type: About
  url: https://mbracetrx.com/about-us/
- group: other
  title: ''
  type: Pipeline
  url: https://mbracetrx.com/pipeline/
- group: other
  title: ''
  type: DiscoveryPlatform
  url: https://mbracetrx.com/discovery-platform/
- group: build
  title: ''
  type: ClinicalProgram
  url: https://mbracetrx.com/clinical-program-mbrc-101/
- group: build
  title: ''
  type: ClinicalProgram
  url: https://mbracetrx.com/clinical-program-mbrc-201/
- group: other
  title: ''
  type: ExpandedAccess
  url: https://mbracetrx.com/expanded-access-statement/
- group: company
  title: ''
  type: News
  url: https://mbracetrx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://mbracetrx.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://mbracetrx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mbracetrx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mbracetrx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mbrace-therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/mbrace-therapeutics_stock/
- group: auth
  href: https://artifacts.apis.io/mbrace-therapeutics/authentication/mbrace-therapeutics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mbrace-therapeutics-authentication.yml
- group: design
  href: https://artifacts.apis.io/mbrace-therapeutics/conventions/mbrace-therapeutics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mbrace-therapeutics-conventions.yml
- group: design
  href: https://artifacts.apis.io/mbrace-therapeutics/conformance/mbrace-therapeutics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mbrace-therapeutics-conformance.yml
- group: design
  href: https://artifacts.apis.io/mbrace-therapeutics/errors/mbrace-therapeutics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mbrace-therapeutics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mbrace-therapeutics/lifecycle/mbrace-therapeutics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mbrace-therapeutics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mbrace-therapeutics/data-model/mbrace-therapeutics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mbrace-therapeutics-data-model.yml
- group: auth
  href: https://artifacts.apis.io/mbrace-therapeutics/security/mbrace-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mbrace-therapeutics-domain-security.yml
- group: build
  href: https://artifacts.apis.io/mbrace-therapeutics/packages/mbrace-therapeutics-packages.yml
  title: ''
  type: Packages
  url: packages/mbrace-therapeutics-packages.yml
- group: commercial
  href: https://artifacts.apis.io/mbrace-therapeutics/plans/mbrace-therapeutics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mbrace-therapeutics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mbrace-therapeutics/rate-limits/mbrace-therapeutics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mbrace-therapeutics-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/mbrace-therapeutics/llms/mbrace-therapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mbrace-therapeutics-llms.txt
- group: agent
  href: https://artifacts.apis.io/mbrace-therapeutics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: MBrace Therapeutics is a privately held, clinical-stage biopharmaceutical company developing antibody-drug conjugates (ADCs) against novel oncology targets. Co-founded by Renata Pasqualini, Ph.D. and Isan Chen, MD, the company builds its pipeline on SPARTA, an in vivo antibody selection and target discovery process it uses to find ADC targets that conventional in vitro discovery misses. Its lead candidate MBRC-101 is an anti-EphA5 monomethyl auristatin E (MMAE) antibody-drug conjugate in a multi-centre, open-label Phase 1/1b dose-finding, safety and pharmacokinetic study in advanced refractory solid tumours; MBRC-201 is in Phase 2, MBRC-301 is in IND-enabling studies against solid tumours, and MBRC-401 is in discovery. MBrace emerged from stealth in November 2023 with an $85 million Series B led by TPG through TPG Life Sciences Innovations, alongside Avidity Partners, Blue Owl Capital, Venrock and Alta Partners, bringing total capital raised to $110 million. MBRC-101 was named
  Most Promising Clinical Candidate at the 11th Annual World ADC Awards. MBrace Therapeutics runs no developer program and publishes no product API, developer portal, API reference or SDK. The only machine-readable surface reachable without credentials is the WordPress REST content API behind mbracetrx.com, catalogued here — notable because the company registered five of its own custom post types, so its board, executive committee, founders, named investors and scientific advisory board are all published as structured JSON rather than only as rendered HTML.
image: https://mbracetrx.com/wp-content/uploads/2021/12/logo-mbrace.svg
layout: provider
modified: '2026-08-25'
name: MBrace Therapeutics
nav: Providers
network: true
overview: 'MBrace Therapeutics publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Antibody-Drug Conjugates.


  MBrace Therapeutics'' developer surface includes product news, authentication, and 24 more developer resources.'
plans:
- name: Mbrace Therapeutics Plans Pricing
  plan_count: 0
  slug: mbrace-therapeutics-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Mbrace Therapeutics Rate Limits
  slug: mbrace-therapeutics-rate-limits
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 18.5
    discoverability: 63.4
    operational_transparency: 0.0
  previous_composite: 16.9
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mbrace-therapeutics/mbrace-therapeutics-2026-09-02T150447.png
security:
- kind: authentication
  name: Mbrace Therapeutics Authentication
  slug: mbrace-therapeutics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mbrace Therapeutics Domain Security
  slug: mbrace-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: mbrace-therapeutics-harvest-company-graph
  slug: mbrace-therapeutics-harvest-company-graph
- name: mbrace-therapeutics-search-and-resolve
  slug: mbrace-therapeutics-search-and-resolve
- name: mbrace-therapeutics-track-news-archive
  slug: mbrace-therapeutics-track-news-archive
slug: mbrace-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Antibody-Drug Conjugates
- Drug Discovery
- Clinical Trials
- Life Sciences
- Precision Medicine
- content-api
website: https://mbracetrx.com/
---
