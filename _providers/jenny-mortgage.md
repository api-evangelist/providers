---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
api_count: 1
apis:
- description: Provides mortgage calculation tools via AI assistants as documented on the developer portal.
  name: Mortgage Tools API
  slug: mortgage-tools-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Newsroom
  url: https://jenny.mortgage/press/
- group: auth
  href: https://artifacts.apis.io/jenny-mortgage/security/jenny-mortgage-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/jenny-mortgage-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/jenny-mortgage/llms/jenny-mortgage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jenny-mortgage-llms.txt
- group: auth
  href: https://artifacts.apis.io/jenny-mortgage/well-known/jenny-mortgage-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jenny-mortgage-security.txt
- group: agent
  href: https://artifacts.apis.io/jenny-mortgage/well-known/jenny-mortgage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jenny-mortgage-well-known.yml
- group: other
  href: https://artifacts.apis.io/jenny-mortgage/hosts/jenny-mortgage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jenny-mortgage-hosts.yml
- group: other
  href: https://artifacts.apis.io/jenny-mortgage/vendors/jenny-mortgage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jenny-mortgage-vendors.yml
- group: auth
  href: https://artifacts.apis.io/jenny-mortgage/security/jenny-mortgage-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jenny-mortgage-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jenny-mortgage/security/jenny-mortgage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jenny-mortgage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jenny.mortgage/mortgage-tools/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jenny.mortgage/mortgage-tools/
- group: docs
  title: ''
  type: Documentation
  url: https://jenny.mortgage/mortgage-tools/
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.jenny.mortgage/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://jenny.mortgage/mortgage-tools/
- group: company
  title: ''
  type: Blog
  url: https://jenny.mortgage/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jenny.mortgage/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jenny.mortgage/privacy-policy.html
coverage:
  checked: '2026-10-26'
  detail: Developer portal page renders via JavaScript, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://jenny.mortgage/mortgage-tools/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Mortgage Tools by Jenny provides a set of Canadian mortgage calculation tools accessible via AI assistants like ChatGPT and Claude, as well as directly through its website. Users can compare renewal offers, model extra payments, evaluate break-or-stay scenarios, and explore debt consolidation options. The tools are free, require no account, and are intended for educational purposes only, offering illustrative calculations without financial advice or lender recommendations.
image: https://jenny.mortgage/assets/jenny-portrait.jpg
layout: provider
modified: '2026-10-26'
name: Mortgage Tools by Jenny
nav: Providers
network: true
overview: 'Mortgage Tools by Jenny is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mortgage, Calculator, Artificial Intelligence, and Canada.


  Mortgage Tools by Jenny''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 13 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 66.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jenny-mortgage/jenny-mortgage-2026-11-03T134135.png
security:
- kind: domain-security
  name: Jenny Mortgage Domain Security
  slug: jenny-mortgage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jenny Mortgage Vulnerability Disclosure
  slug: jenny-mortgage-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jenny-mortgage
tags:
- Company
- Mortgage
- Calculator
- Artificial Intelligence
- Canada
website: https://jenny.mortgage/mortgage-tools/
---
