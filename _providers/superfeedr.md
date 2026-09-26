---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/superfeedr/refs/heads/main/hosts/superfeedr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/superfeedr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/superfeedr/refs/heads/main/vendors/superfeedr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/superfeedr-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/superfeedr/refs/heads/main/packages/superfeedr-packages.yml
  title: ''
  type: SDKs
  url: packages/superfeedr-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/superfeedr/refs/heads/main/packages/superfeedr-packages.yml
  title: ''
  type: Packages
  url: packages/superfeedr-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superfeedr.com/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://superfeedr.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superfeedr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.superfeedr.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.superfeedr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.superfeedr.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/superfeedr/refs/heads/main/security/superfeedr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/superfeedr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://superfeedr.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superfeedr.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://superfeedr.com/users/new
- group: operate
  title: ''
  type: Support
  url: https://superfeedr.com/contact
- group: docs
  title: ''
  type: APIReference
  url: http://documentation.superfeedr.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://superfeedr.com/about
coverage:
  checked: 2026-09-22
  detail: The provider's documentation pages are HTML only and no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://portal.superfeedr.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-22'
description: Superfeedr provides a real-time feed API that pushes RSS and Atom updates instantly via PubSubHubbub. It enables publishers and subscribers to deliver content as soon as it changes, offering a simple Push API for developers, content publishers, and application teams.
layout: provider
modified: '2026-09-22'
name: Superfeedr
nav: Providers
network: true
overview: 'Superfeedr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Time, Feed, and PubSubHubbub.


  Superfeedr''s developer surface includes pricing, engineering blog, documentation, signup flow, support, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 35.7
    operational_transparency: 5.3
  previous_composite: 23.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Superfeedr Domain Security
  slug: superfeedr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: superfeedr
tags:
- Company
- Real-Time
- Feed
- PubSubHubbub
website: https://superfeedr.com/
---
