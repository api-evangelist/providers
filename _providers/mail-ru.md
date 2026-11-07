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
  href: https://artifacts.apis.io/mail-ru/hosts/mail-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mail-ru-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.mail.ru/marusia/skill/vk/android_assistant/trouble_android_assistant/no_setup/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.mail.ru/
- group: auth
  href: https://artifacts.apis.io/mail-ru/security/mail-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mail-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mail.ru/
coverage:
  checked: '2026-10-28'
  detail: The provider's main site returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://mail.ru/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Mail.ru Cloud is a Russian cloud services provider offering email, file storage, collaboration tools, and a suite of online applications. It operates under the Mail.ru brand, serving both consumer and business customers with cloud-based solutions such as Mail.ru Cloud storage, document editing, and integrated messaging. The platform emphasizes data security and integrates with other Mail.ru services, providing a comprehensive ecosystem for personal and enterprise use.
layout: provider
modified: '2026-10-27'
name: Mail.ru Cloud
nav: Providers
network: true
overview: 'Mail.ru Cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Storage, Collaboration, Russian, and Email.


  Mail.ru Cloud''s developer surface includes getting-started guide, documentation, and 3 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mail-ru/mail-ru-2026-11-03T135300.png
security:
- kind: domain-security
  name: Mail Ru Domain Security
  slug: mail-ru-domain-security
  summary_line: TLSv1.2 · DMARC
slug: mail-ru
tags:
- Cloud
- Storage
- Collaboration
- Russian
- Email
website: https://mail.ru/
---
