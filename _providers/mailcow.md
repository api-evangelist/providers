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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/mailcow/well-known/mailcow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailcow-well-known.yml
- group: other
  href: https://artifacts.apis.io/mailcow/hosts/mailcow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailcow-hosts.yml
- group: other
  href: https://artifacts.apis.io/mailcow/vendors/mailcow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mailcow-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://mailcow.email/tags/security/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mailcow.email/post_installation/setup-mta-sts/
- group: auth
  href: https://artifacts.apis.io/mailcow/security/mailcow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailcow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailcow.email/
- group: docs
  title: ''
  type: Documentation
  url: https://mailcow.github.io/mailcow-dockerized-docs/
- group: operate
  title: ''
  type: Support
  url: https://www.servercow.de/mailcow?lang=en#support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailcow
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/mailcow/workspace/mailcow-api/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 301
    url: https://mailcow.github.io/mailcow-dockerized-docs/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Mailcow provides a dockerized mail server suite, offering a full-featured, self‑hosted email solution with webmail, spam filtering, antivirus, and advanced management tools. It is maintained by The Infrastructure Company GmbH and supports modern protocols, multiple domains, and extensive configuration options, targeting both small businesses and larger enterprises seeking control over their email infrastructure.
image: https://mailcow.email/images/cow_mailcow.svg
layout: provider
modified: '2026-10-27'
name: mailcow
nav: Providers
network: true
overview: 'mailcow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Docker, Open Source, and Self-Hosted.


  mailcow''s developer surface includes getting-started guide, documentation, support, and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 48.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mailcow/mailcow-2026-11-03T135242.png
security:
- kind: domain-security
  name: Mailcow Domain Security
  slug: mailcow-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: mailcow
tags:
- Company
- Email
- Docker
- Open Source
- Self-Hosted
website: https://mailcow.email/
---
