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
- description: API for Merlin's digital music licensing platform, documented on the Technology page.
  name: Merlin API
  slug: merlin-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Blog
  url: https://merlinnetwork.org/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://merlinnetwork.org/news/feed/
- group: other
  href: https://artifacts.apis.io/merlin/hosts/merlin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/merlin-hosts.yml
- group: other
  href: https://artifacts.apis.io/merlin/vendors/merlin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/merlin-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://merlinnetwork.org/news
- group: auth
  href: https://artifacts.apis.io/merlin/security/merlin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/merlin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merlinnetwork.org/
- group: docs
  title: ''
  type: Documentation
  url: https://merlinnetwork.org/technology/
- group: start
  title: ''
  type: GettingStarted
  url: https://merlinnetwork.org/becoming-a-member/
- group: operate
  title: ''
  type: Support
  url: https://merlinnetwork.org/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://merlinnetwork.org/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://merlinnetwork.org/privacy-policy/
coverage:
  checked: 2026-09-23
  detail: Technology page loads content via JavaScript, preventing retrieval of a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://merlinnetwork.org/technology/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: Merlin is a global digital music licensing organization that represents independent music companies, providing them access to licensing deals, tools, and data insights. It operates a membership platform called Wizard, offers technology solutions, and publishes reports and industry insights to support its members in navigating the digital music ecosystem.
image: https://merlinnetwork.org/wp-content/uploads/2023/09/merlin-site-image.png
layout: provider
modified: '2026-10-06'
name: Merlin
nav: Providers
network: true
overview: 'Merlin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Licensing, Technology, and Membership.


  Merlin''s developer surface includes engineering blog, documentation, getting-started guide, support, and 8 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 15.6
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/merlin/merlin-2026-10-11T111023.png
security:
- kind: domain-security
  name: Merlin Domain Security
  slug: merlin-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: merlin
tags:
- Company
- Music
- Licensing
- Technology
- Membership
website: https://merlinnetwork.org/
---
