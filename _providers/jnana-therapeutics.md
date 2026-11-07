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
- description: 'The public WordPress REST API (wp-json) of the Jnana Therapeutics website at www.jnanatx.com: the route index of the site''s content management system, catalogued as one site surface rather than as sep'
  name: Jnana Therapeutics Website (WordPress REST)
  slug: jnanatx-com-website-wordpress-rest
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/jnana-therapeutics/security/jnana-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jnana-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jnanatx.com/
- group: other
  title: ''
  type: Platform
  url: https://www.jnanatx.com/rapid-platform/
- group: other
  title: ''
  type: Programs
  url: https://www.jnanatx.com/programs/
- group: other
  title: ''
  type: Team
  url: https://www.jnanatx.com/team/
- group: company
  title: ''
  type: News
  url: https://www.jnanatx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.jnanatx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.jnanatx.com/join-us/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.jnanatx.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jnanatx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jnanatx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jnana-therapeutics/
- group: other
  title: ''
  type: X
  url: https://x.com/jnanatx
- group: other
  title: ''
  type: ParentCompany
  url: https://www.otsuka.co.jp/en/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/jnana-therapeutics_stock/
- group: auth
  href: https://artifacts.apis.io/jnana-therapeutics/authentication/jnana-therapeutics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jnana-therapeutics-authentication.yml
- group: design
  href: https://artifacts.apis.io/jnana-therapeutics/conventions/jnana-therapeutics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jnana-therapeutics-conventions.yml
- group: design
  href: https://artifacts.apis.io/jnana-therapeutics/conformance/jnana-therapeutics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jnana-therapeutics-conformance.yml
- group: design
  href: https://artifacts.apis.io/jnana-therapeutics/errors/jnana-therapeutics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jnana-therapeutics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jnana-therapeutics/lifecycle/jnana-therapeutics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jnana-therapeutics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jnana-therapeutics/data-model/jnana-therapeutics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jnana-therapeutics-data-model.yml
- group: build
  href: https://artifacts.apis.io/jnana-therapeutics/packages/jnana-therapeutics-packages.yml
  title: ''
  type: Packages
  url: packages/jnana-therapeutics-packages.yml
- group: operate
  href: https://artifacts.apis.io/jnana-therapeutics/rate-limits/jnana-therapeutics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jnana-therapeutics-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jnana-therapeutics/plans/jnana-therapeutics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jnana-therapeutics-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/jnana-therapeutics/llms/jnana-therapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jnana-therapeutics-llms.txt
- group: agent
  href: https://artifacts.apis.io/jnana-therapeutics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: 'Jnana Therapeutics Inc. is a biotechnology company headquartered at One Design Center Place, Suite 19-400, Boston, Massachusetts, that built RAPID — Reactive Affinity Probe Interaction Discovery — a next-generation chemoproteomics platform for discovering small-molecule medicines against target classes that conventional screening has struggled to drug, including SLC transporters, transcription factors, signaling scaffold proteins, phosphatases, GPCRs and helicases. RAPID runs in living cells: a proprietary Reactive Affinity Probe library covalently labels druggable pockets on a validated target, and a proprietary detection technology then screens large drug-like compound libraries for binders that displace the probe, yielding allosteric inhibitors, localization modulators and molecular glues without iterative structural biology. Its internal pipeline focuses on phenylketonuria (PKU) — where JNT-517, an oral inhibitor acting at a cryptic allosteric site on the SLC6A19 transporter,
  reached Phase 1b/2 — and on immune-mediated diseases including targets such as interferon regulatory factor 3 (IRF3), alongside biopharma collaborations that include Roche. Otsuka Pharmaceutical Co., Ltd. completed its acquisition of Jnana on 23 September 2024 for $800 million plus up to $325 million in development and regulatory milestones, making Jnana a direct subsidiary of Otsuka America, Inc.; Otsuka initiated a global Phase 3 trial of repinatrabit in PKU in December 2025. Jnana Therapeutics runs no developer program and publishes no product API, developer portal, API reference or SDK. The only machine-readable surface reachable without credentials is the WordPress REST content API behind www.jnanatx.com, catalogued here.'
image: https://www.jnanatx.com/wp-content/uploads/2022/09/cropped-android-chrome-512x512-1.png
layout: provider
modified: '2026-08-23'
name: Jnana Therapeutics
nav: Providers
network: true
overview: 'Jnana Therapeutics publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and chemoproteomics.


  Jnana Therapeutics'' developer surface includes product news, authentication, and 24 more developer resources.'
plans:
- name: Jnana Therapeutics Plans Pricing
  plan_count: 0
  slug: jnana-therapeutics-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Jnana Therapeutics Rate Limits
  slug: jnana-therapeutics-rate-limits
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 18.5
    discoverability: 65.2
    operational_transparency: 0.0
  previous_composite: 17.0
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
screenshot: https://apis.io/screenshots/jnana-therapeutics/jnana-therapeutics-2026-09-02T145947.png
security:
- kind: authentication
  name: Jnana Therapeutics Authentication
  slug: jnana-therapeutics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Jnana Therapeutics Domain Security
  slug: jnana-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: jnana-therapeutics-company-profile
  slug: jnana-therapeutics-company-profile
- name: jnana-therapeutics-news-monitoring
  slug: jnana-therapeutics-news-monitoring
slug: jnana-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- chemoproteomics
- Rare Disease
- Immunology
- Life Sciences
- Clinical Trials
- content-api
website: https://www.jnanatx.com/
---
