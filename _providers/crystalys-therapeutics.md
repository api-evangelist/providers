---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://crystalystx.com/
- group: company
  title: ''
  type: Newsroom
  url: https://crystalystx.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crystalystx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crystalystx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crystalys-therapeutics/
- group: other
  title: ''
  type: X
  url: https://x.com/Crystalys_Tx
- group: other
  href: https://artifacts.apis.io/crystalys-therapeutics/hosts/crystalys-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crystalys-therapeutics-hosts.yml
- group: other
  href: https://artifacts.apis.io/crystalys-therapeutics/vendors/crystalys-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crystalys-therapeutics-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crystalys-therapeutics/security/crystalys-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crystalys-therapeutics-domain-security.yml
coverage:
  checked: '2026-11-04'
  detail: Crystalys Therapeutics is a clinical-stage biopharmaceutical company; its own site is a WordPress corporate marketing site (home, about-us, science, news, investors, contact, legal) with no developer, API, docs or SDK pages, and preflight contract discovery against crystalystx.com and api.crystalystx.com returned absent for OpenAPI, AsyncAPI, GraphQL and MCP.
  evidence:
  - status: 404
    url: https://crystalystx.com/api
  - status: 404
    url: https://crystalystx.com/developers
  - status: 404
    url: https://crystalystx.com/docs
  - status: 404
    url: https://crystalystx.com/developer
  - status: 200
    url: https://crystalystx.com/sitemap_index.xml
  reason: not-a-software-company
  state: none
created: '2026-10-11'
description: Crystalys Therapeutics is a clinical-stage biopharmaceutical company headquartered in San Diego, California, focused on addressing the significant unmet medical needs of people living with gout. Its lead investigational therapy, dotinurad, is a next-generation, highly selective urate transporter 1 (URAT1) inhibitor designed to lower serum uric acid by targeting the renal transport pathways responsible for urate reabsorption. The company was co-founded by its executive team together with Catalys Pacific and Novo Holdings, and is running Phase 2 and Phase 3 clinical trials (AMETHYST, RUBY and TOPAZ) in the U.S. and Europe to evaluate dotinurad as a second-line therapy for hyperuricemia associated with gout.
image: https://crystalystx.com/wp-content/uploads/2024/12/crystalys_wordmark_rgb.svg
layout: provider
modified: '2026-11-04'
name: Crystalys Therapeutics
nav: Providers
network: true
overview: Crystalys Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharmaceutical, Clinical Stage, Pharmaceuticals, and Drug Development.
random_paper: 20
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 1.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crystalys Therapeutics Domain Security
  slug: crystalys-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crystalys-therapeutics
tags:
- Company
- Biopharmaceutical
- Clinical Stage
- Pharmaceuticals
- Drug Development
- Therapeutics
- Gout
- Hyperuricemia
- Dotinurad
- URAT1 Inhibitor
website: https://crystalystx.com/
---
