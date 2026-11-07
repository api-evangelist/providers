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
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the KSQ Therapeutics website at ksqtx.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate AP'
  name: KSQ Therapeutics Website (WordPress REST)
  slug: ksqtx-com-website-wordpress-rest
artifact_total: 8
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/ksqtx/TRACE/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://ksqtx.com/
- group: company
  title: ''
  type: About
  url: https://ksqtx.com/about/
- group: other
  title: ''
  type: Platform
  url: https://ksqtx.com/platform/
- group: other
  title: ''
  type: Pipeline
  url: https://ksqtx.com/pipeline/
- group: company
  title: ''
  type: Partners
  url: https://ksqtx.com/partners/
- group: company
  title: ''
  type: Blog
  url: https://ksqtx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://ksqtx.com/feed/
- group: company
  title: ''
  type: News
  url: https://ksqtx.com/press-releases/
- group: company
  title: ''
  type: Careers
  url: https://ksqtx.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://ksqtx.com/contact-us/
- group: other
  title: ''
  type: PatientResources
  url: https://ksqtx.com/eap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ksqtx
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ksqtx/TRACE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/10414448/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/KSQ_TX
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/ksq-therapeutics_stock/
- group: auth
  href: https://artifacts.apis.io/ksq-therapeutics/authentication/ksq-therapeutics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ksq-therapeutics-authentication.yml
- group: design
  href: https://artifacts.apis.io/ksq-therapeutics/conventions/ksq-therapeutics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ksq-therapeutics-conventions.yml
- group: design
  href: https://artifacts.apis.io/ksq-therapeutics/conformance/ksq-therapeutics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ksq-therapeutics-conformance.yml
- group: design
  href: https://artifacts.apis.io/ksq-therapeutics/errors/ksq-therapeutics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ksq-therapeutics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ksq-therapeutics/lifecycle/ksq-therapeutics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ksq-therapeutics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ksq-therapeutics/data-model/ksq-therapeutics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ksq-therapeutics-data-model.yml
- group: other
  href: https://artifacts.apis.io/ksq-therapeutics/overlays/ksq-therapeutics-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ksq-therapeutics-content-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/ksq-therapeutics/security/ksq-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ksq-therapeutics-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/ksq-therapeutics/llms/ksq-therapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ksq-therapeutics-llms.txt
- group: build
  href: https://artifacts.apis.io/ksq-therapeutics/packages/ksq-therapeutics-packages.yml
  title: ''
  type: Packages
  url: packages/ksq-therapeutics-packages.yml
- group: build
  href: https://artifacts.apis.io/ksq-therapeutics/cli/ksq-therapeutics-cli.yml
  title: ''
  type: CLI
  url: cli/ksq-therapeutics-cli.yml
- group: commercial
  href: https://artifacts.apis.io/ksq-therapeutics/plans/ksq-therapeutics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ksq-therapeutics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ksq-therapeutics/rate-limits/ksq-therapeutics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ksq-therapeutics-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/ksq-therapeutics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: 'KSQ Therapeutics is a clinical-stage biotechnology company headquartered at 4 Maguire Road in Lexington, Massachusetts, founded in 2015 by pioneers of CRISPR screening and functional genomics. Its proprietary CRISPRomics platform runs genome-scale CRISPR/Cas9 functional genomic screens across cancer models and immune cell types to identify therapeutic targets that directly correlate genomic function to disease. The company applies those targets in two directions: CRISPR/Cas9-engineered tumor-infiltrating lymphocyte (eTIL) cell therapies, where a single gene is inactivated to increase the tumor-killing capacity of a patient''s own T cells — KSQ-001EX (SOCS1 inactivated) and KSQ-004EX (SOCS1 and Regnase-1 inactivated) — and small molecules such as KSQ-4279, a first-in-class USP1 inhibitor for advanced solid tumors. KSQ has run broad discovery collaborations with Takeda, licensed cell-therapy technology with CRISPR Therapeutics, partnered manufacturing with CTMC, and sold multiple
  research-stage oncology programs to Ono Pharmaceutical. Investors include Flagship Pioneering, ARCH Venture Partners, Polaris Partners, Alexandria, Alpha Wave Global, Baillie Gifford, Invus, LG and Lilly Asia Ventures. KSQ Therapeutics runs no developer program and publishes no product API, developer portal, OpenAPI or API reference. The only machine-readable surfaces reachable without credentials are the WordPress REST content API behind ksqtx.com, an All in One SEO generated /llms.txt, and the open-source bioinformatics code in its public GitHub organization — all catalogued here.'
image: https://ksqtx.com/wp-content/uploads/2024/02/KSQ-logo-color-RegTM.png
layout: provider
modified: '2026-08-23'
name: KSQ Therapeutics
nav: Providers
network: true
overview: 'KSQ Therapeutics publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Therapeutics, and Oncology.


  KSQ Therapeutics'' developer surface includes engineering blog, product news, support, authentication, CLI, and 26 more developer resources.'
plans:
- name: Ksq Therapeutics Plans Pricing
  plan_count: 0
  slug: ksq-therapeutics-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Ksq Therapeutics Rate Limits
  slug: ksq-therapeutics-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 32.7
    discoverability: 65.2
    operational_transparency: 2.6
  previous_composite: 15.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ksq-therapeutics/ksq-therapeutics-2026-09-02T150151.png
security:
- kind: authentication
  name: Ksq Therapeutics Authentication
  slug: ksq-therapeutics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ksq Therapeutics Domain Security
  slug: ksq-therapeutics-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 3
skills:
- name: ksq-therapeutics-harvest-media-library
  slug: ksq-therapeutics-harvest-media-library
- name: ksq-therapeutics-search-and-resolve
  slug: ksq-therapeutics-search-and-resolve
- name: ksq-therapeutics-track-press-release-archive
  slug: ksq-therapeutics-track-press-release-archive
slug: ksq-therapeutics
tags:
- Company
- Biotechnology
- Life Sciences
- Therapeutics
- Oncology
- Genomics
- CRISPR
- Gene Editing
- Cell Therapy
- Clinical Stage
- Functional Genomics
- content-api
website: https://ksqtx.com/
---
