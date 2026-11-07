---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/kewazo/hosts/kewazo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kewazo-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://www.kewazo.com/blog/news-bauma2025
- group: auth
  href: https://artifacts.apis.io/kewazo/security/kewazo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kewazo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kewazo.com
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.kewazo.com/legal_notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kewazo.com/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kewazo.com/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: KEWAZO's website provides product information but no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.kewazo.com
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Kewazo builds autonomous lifting robots (LiftBot) that combine robotics and artificial intelligence to automate material transport in industrial and construction environments. Their solutions reduce crane time, manual handling, and hazardous hours, delivering faster, safer turnarounds for capital projects, maintenance, and heavy‑industry operations. By offering battery‑powered, remote‑controlled robots, Kewazo helps customers improve productivity, lower costs, and enhance workplace safety.
image: https://framerusercontent.com/images/RBWNCksWxfUID38YObx6ybK5eQ.png?width=455&height=151
layout: provider
modified: '2026-10-29'
name: Kewazo
nav: Providers
network: true
overview: 'Kewazo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Artificial Intelligence, Industrial Automation, Material Handling, and LiftBot.


  Kewazo''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Kewazo Plans Pricing
  plan_count: 0
  slug: kewazo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Kewazo Rate Limits
  slug: kewazo-rate-limits
scopes:
- name: Kewazo Scopes
  scope_count: 0
  slug: kewazo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kewazo/kewazo-2026-11-03T134404.png
security:
- kind: authentication
  name: Kewazo Authentication
  slug: kewazo-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kewazo Domain Security
  slug: kewazo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kewazo
tags:
- Robotics
- Artificial Intelligence
- Industrial Automation
- Material Handling
- LiftBot
website: https://kewazo.com
---
