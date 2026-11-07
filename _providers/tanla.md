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
  href: https://artifacts.apis.io/tanla/hosts/tanla-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tanla-hosts.yml
- group: other
  href: https://artifacts.apis.io/tanla/vendors/tanla-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tanla-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tanla.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tanla.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.tanla.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.tanla.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.tanla.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://tanla.com/newsroom/tanla-solutions-announces-onboarding-of-three-new-independent-directors
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tanla
- group: auth
  href: https://artifacts.apis.io/tanla/security/tanla-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tanla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tanla.com
coverage:
  checked: '2026-10-03'
  detail: The Tanla website provides API information only via JavaScript‑rendered pages with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.tanla.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Tanla Platforms Limited provides a unified communications platform that integrates messaging, voice, email, and digital engagement services through a single API. Leveraging blockchain-based smart routing and end‑to‑end encryption, Tanla enables enterprises to deliver secure, scalable, and intelligent interactions across channels such as SMS, WhatsApp, RCS, email, and voice. The platform offers products like User.ai, Anti‑Spam, Anti‑Scam, Data Privacy, Enterprise‑AI, and Wise Albert, targeting industries from banking to e‑commerce, aiming to simplify digital communication workflows and enhance user experiences.
image: https://cdn.prod.website-files.com/65a4d6e71551dd4dd97a2ac6/65cc5b8916cba6d19f22b779_Rectangle%2067.png
layout: provider
modified: '2026-10-03'
name: Tanla
nav: Providers
network: true
overview: 'Tanla is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Messaging, and Platform.


  Tanla''s developer surface includes engineering blog, getting-started guide, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 41.1
    operational_transparency: 2.6
  previous_composite: 11.8
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/tanla/tanla-2026-10-11T130644.png
security:
- kind: domain-security
  name: Tanla Domain Security
  slug: tanla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tanla
tags:
- Company
- Communications
- Messaging
- Platform
website: https://www.tanla.com
---
