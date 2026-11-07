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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bibleglide-com/plans/bibleglide-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bibleglide-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bibleglide-com/llms/bibleglide-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bibleglide-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bibleglide-com/well-known/bibleglide-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bibleglide-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bibleglide-com/hosts/bibleglide-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bibleglide-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bibleglide-com/vendors/bibleglide-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bibleglide-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bibleglide.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.bibleglide.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bibleglide.com/privacy
- group: auth
  href: https://artifacts.apis.io/bibleglide-com/security/bibleglide-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bibleglide-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bibleglide.com/
coverage:
  checked: '2026-11-02'
  detail: Main website is a JavaScript‑rendered single‑page app with no publicly accessible API documentation.
  evidence:
  - status: 200
    url: https://www.bibleglide.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Bible Glide is a reading and study app that lets users read the Bible online for free, keep passages in context, and ask Scripture questions using AI chat. It offers daily reading, group study features, and a simple interface without requiring an account. Founded by Nicholas, the service aims to provide honest, context‑rich Scripture engagement for individuals, small groups, and churches.
image: https://www.bibleglide.com/og-bible.png
layout: provider
modified: '2026-11-02'
name: Bible Glide
nav: Providers
network: true
overview: 'Bible Glide is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bible, Reading, Artificial Intelligence, Study, and Scripture.


  Bible Glide''s developer surface includes support and 9 more developer resources.'
plans:
- name: Bibleglide Com Plans Pricing
  plan_count: 4
  slug: bibleglide-com-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bibleglide Com Domain Security
  slug: bibleglide-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bibleglide-com
tags:
- Bible
- Reading
- Artificial Intelligence
- Study
- Scripture
website: https://bibleglide.com/
---
