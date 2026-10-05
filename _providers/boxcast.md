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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: BoxCast provides streaming video APIs for custom viewer experiences.
  name: BoxCast API
  slug: boxcast-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/plans/boxcast-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boxcast-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/authentication/boxcast-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boxcast-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/llms/boxcast-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boxcast-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/well-known/boxcast-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boxcast-support-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/well-known/boxcast-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boxcast-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/hosts/boxcast-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boxcast-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/vendors/boxcast-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boxcast-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/packages/boxcast-packages.yml
  title: ''
  type: SDKs
  url: packages/boxcast-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/packages/boxcast-packages.yml
  title: ''
  type: Packages
  url: packages/boxcast-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boxcast.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boxcast.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://login.boxcast.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://support.boxcast.com/en/articles/6376916-how-to-use-producer-by-boxcast-quick-start-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boxcast
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boxcast/refs/heads/main/security/boxcast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boxcast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boxcast.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.boxcast.com/platform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.boxcast.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.boxcast.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.boxcast.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.boxcast.com/en/
coverage:
  checked: '2026-10-03'
  detail: API documentation is served as HTML pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://dashboard.boxcast.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: BoxCast provides professional live video streaming and production solutions for businesses, houses of worship, athletics, and more. Their platform includes streaming, video management, remote mixing, and OTT apps, enabling users to broadcast high‑quality live video easily. Founded to simplify live video workflows, BoxCast offers a cloud‑based service with robust analytics, integrations, and support for various devices and encoders.
image: https://www.boxcast.com/hubfs/BoxCast.com%20-%20Visual%20Assets/Landing%20Pages/Easter%202026/Easter-2026_Feature-Image.jpg
layout: provider
modified: '2026-10-03'
name: BoxCast
nav: Providers
network: true
overview: 'BoxCast publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Streaming, Live, and Platform.


  BoxCast''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, support, and 15 more developer resources.'
plans:
- name: Boxcast Plans Pricing
  plan_count: 2
  slug: boxcast-plans-pricing
random_paper: 8
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Boxcast Authentication
  slug: boxcast-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Boxcast Domain Security
  slug: boxcast-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: boxcast
tags:
- Company
- Video
- Streaming
- Live
- Platform
website: https://www.boxcast.com/
---
