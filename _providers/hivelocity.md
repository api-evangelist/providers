---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provisioning, managing and monitoring infrastructure via Hivelocity's developer portal.
  name: Hivelocity API
  slug: hivelocity-api
artifact_total: 5
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/rate-limits/hivelocity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hivelocity-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/plans/hivelocity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hivelocity-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/changelog/hivelocity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hivelocity-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/authentication/hivelocity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hivelocity-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/llms/hivelocity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hivelocity-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/well-known/hivelocity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hivelocity-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/hosts/hivelocity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hivelocity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/vendors/hivelocity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hivelocity-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hivelocity.net/
- group: auth
  title: ''
  type: Security
  url: https://www.hivelocity.net/kb/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.hivelocity.net/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hivelocity/refs/heads/main/security/hivelocity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hivelocity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hivelocity.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hivelocity.net
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hivelocity.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hivelocity.net/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hivelocity.net/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.hivelocity.net/about/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.hivelocity.net/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hivelocity
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hivelocity.net/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.hivelocity.net/sign-up
coverage:
  checked: '2026-10-14'
  detail: Developer portal pages render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developers.hivelocity.net/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Hivelocity provides bare metal dedicated servers, virtual private servers, and colocation services with human support. Their platform offers a developer portal with a comprehensive API for provisioning, managing, and monitoring infrastructure across global data centers. The API enables automated creation of clients, retrieval of device data, bandwidth monitoring, backup management, and more, facilitating seamless integration into enterprise workflows.
image: https://www.hivelocity.net/logo.png
layout: provider
modified: '2026-10-14'
name: Hivelocity
nav: Providers
network: true
overview: 'Hivelocity is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Hosting, BareMetal, VPS, and Colocation.


  Hivelocity''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
plans:
- name: Hivelocity Plans Pricing
  plan_count: 17
  slug: hivelocity-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Hivelocity Rate Limits
  slug: hivelocity-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 64.3
    operational_transparency: 68.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hivelocity Authentication
  slug: hivelocity-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hivelocity Domain Security
  slug: hivelocity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hivelocity
tags:
- Cloud
- Hosting
- BareMetal
- VPS
- Colocation
- Infrastructure
website: https://www.hivelocity.net
---
