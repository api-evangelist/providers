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
api_count: 1
apis:
- description: A long-term path of deep meditation training, guided by Zen Master Henry Shukman
  name: The Way API
  slug: the-way-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/the-way/llms/the-way-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-way-llms.txt
- group: other
  href: https://artifacts.apis.io/the-way/hosts/the-way-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-way-hosts.yml
- group: other
  href: https://artifacts.apis.io/the-way/vendors/the-way-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-way-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thewayapp.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thewayapp.com/privacy
- group: auth
  href: https://artifacts.apis.io/the-way/security/the-way-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-way-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thewayapp.com
coverage:
  checked: '2026-10-29'
  detail: API documentation is behind a customer login portal at https://app.thewayapp.com/.
  evidence:
  - status: 200
    url: https://app.thewayapp.com/
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: The Way App is a meditation platform founded by Zen Master Henry Shukman and his nephew Jack, offering a long‑term path of deep meditation training guided by authentic Zen teachings. The app combines Henry’s decades of experience teaching at the Mountain Cloud Zen Center with Jack’s corporate background to create a step‑by‑step journey that helps users calm the nervous system, heal trauma, and explore the nature of the self. By providing accessible, single‑path guidance, The Way App aims to bring unconditional wellbeing to anyone seeking clarity, peace, and spiritual growth.
image: https://images.ctfassets.net/db647e76yckr/5XSZvjckVZT3wiDwZljz56/53e475dd100757e54a78ec5a53b3ba73/The-Way-App_cover-img_2000x.webp
layout: provider
modified: '2026-10-29'
name: The Way
nav: Providers
network: true
overview: The Way is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Meditation, Wellness, Zen, and Spirituality.
random_paper: 7
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/the-way/the-way-2026-11-03T144633.png
security:
- kind: domain-security
  name: The Way Domain Security
  slug: the-way-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-way
tags:
- Company
- Meditation
- Wellness
- Zen
- Spirituality
- Mental Health
website: https://thewayapp.com
---
