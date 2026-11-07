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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides a developer‑friendly API for the self‑hosted Soulseek daemon, enabling file‑sharing operations, search, and token‑based authentication.
  name: slskd API
  slug: slskd-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Blog
  url: https://slskd.com/category/blog/
- group: agent
  href: https://artifacts.apis.io/slskd/well-known/slskd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/slskd-well-known.yml
- group: other
  href: https://artifacts.apis.io/slskd/hosts/slskd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/slskd-hosts.yml
- group: other
  href: https://artifacts.apis.io/slskd/vendors/slskd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/slskd-vendors.yml
- group: auth
  href: https://artifacts.apis.io/slskd/security/slskd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slskd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slskd.org
- group: start
  title: ''
  type: GettingStarted
  url: https://slskd.com/guide/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://slskd.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://slskd.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slskd.com/privacy-policy/
coverage:
  checked: '2026-10-28'
  detail: The slskd website renders documentation via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 301
    url: https://slskd.com/guide/getting-started/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: slskd provides a modern, self‑hosted Soulseek client that runs as a daemon and offers a remote web interface and a developer‑friendly API. It enables secure, continuous file‑sharing across Windows, Linux, macOS and Docker, with features like automated workflows, privacy controls, and easy installation via Docker or native binaries.
image: https://slskd.com/wp-content/uploads/2026/03/slskd-2.webp
layout: provider
modified: '2026-10-28'
name: slskd
nav: Providers
network: true
overview: 'slskd is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, File Sharing, Self-Hosted, and Open Source.


  slskd''s developer surface includes engineering blog, getting-started guide, support, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/slskd/slskd-2026-11-03T143337.png
security:
- kind: domain-security
  name: Slskd Domain Security
  slug: slskd-domain-security
  summary_line: TLSv1.3
slug: slskd
tags:
- Company
- File Sharing
- Self-Hosted
- Open Source
website: https://slskd.org
---
