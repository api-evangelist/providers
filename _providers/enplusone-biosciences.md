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
- group: other
  href: https://artifacts.apis.io/enplusone-biosciences/hosts/enplusone-biosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enplusone-biosciences-hosts.yml
- group: other
  href: https://artifacts.apis.io/enplusone-biosciences/vendors/enplusone-biosciences-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enplusone-biosciences-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enplusone.bio/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enplusone.bio/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://enplusone.bio/news/
- group: other
  title: ''
  type: Leadership
  url: https://enplusone.bio/team/
- group: auth
  href: https://artifacts.apis.io/enplusone-biosciences/security/enplusone-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enplusone-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enplusonebio.com/
coverage:
  checked: '2026-10-25'
  detail: The website returns HTML pages and no machine‑readable OpenAPI spec was found at common endpoints.
  evidence:
  - status: 200
    url: https://enplusone.bio/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: EnPlusOne Biosciences is a biotechnology company focused on developing flexible enzymatic platforms for scalable RNA therapeutics. They aim to overcome current manufacturing limitations by unlocking over 200 RNA modifications, enabling faster and more diverse therapeutic development. Their mission is to make better RNA, solving today’s limitations and unlocking tomorrow’s innovations in the RNA therapeutics space.
layout: provider
modified: '2026-10-25'
name: EnPlusOne Biosciences
nav: Providers
network: true
overview: EnPlusOne Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, RNA Therapeutics, Enzymatic Platform, and Synthetic Biology.
random_paper: 5
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/enplusone-biosciences/enplusone-biosciences-2026-11-03T131531.png
security:
- kind: domain-security
  name: Enplusone Biosciences Domain Security
  slug: enplusone-biosciences-domain-security
  summary_line: TLSv1.3
slug: enplusone-biosciences
tags:
- Company
- Biotechnology
- RNA Therapeutics
- Enzymatic Platform
- Synthetic Biology
website: https://www.enplusonebio.com/
---
