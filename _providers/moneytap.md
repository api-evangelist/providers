---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/moneytap/plans/moneytap-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moneytap-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/moneytap/hosts/moneytap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moneytap-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://freo.money/terms-and-conditions/
- group: auth
  title: ''
  type: Security
  url: https://freo.money/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://freo.money/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://freo.money/guides/
- group: auth
  href: https://artifacts.apis.io/moneytap/security/moneytap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moneytap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.moneytap.com
coverage:
  checked: '2026-10-26'
  detail: The main site redirects to a Framer‑hosted page that serves only JavaScript‑rendered content, preventing machine‑readable discovery.
  evidence:
  - status: 200
    url: https://moneytap.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: 'MoneyTap is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by nea) and added to the network as a stub for full-pipeline profiling.'
image: https://framerusercontent.com/images/yoO3dItggCc88Mzyn1xInatGrig.png
layout: provider
modified: '2026-10-26'
name: MoneyTap
nav: Providers
network: true
overview: 'MoneyTap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Loans, Credit Line, Instant Loans, Fintech, and RBI Regulated.


  MoneyTap''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Moneytap Plans Pricing
  plan_count: 16
  slug: moneytap-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 39.3
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.5
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/moneytap/moneytap-2026-11-03T135832.png
security:
- kind: domain-security
  name: Moneytap Domain Security
  slug: moneytap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moneytap
tags:
- Personal Loans
- Credit Line
- Instant Loans
- Fintech
- RBI Regulated
- Consumer Credit
website: https://www.moneytap.com
---
