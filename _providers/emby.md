---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/emby/vendors/emby-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emby-vendors.yml
- group: auth
  href: https://artifacts.apis.io/emby/authentication/emby-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emby-authentication.yml
- group: other
  href: https://artifacts.apis.io/emby/hosts/emby-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emby-hosts.yml
- group: build
  title: ''
  type: SDKs
  url: https://emby.media/community/index.php?/tags/forums/libraries/
- group: start
  title: ''
  type: Login
  url: https://emby.media/community/index.php?/tags/forums/login/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.emby.media/
- group: company
  title: ''
  type: Blog
  url: https://emby.media/community/index.php?/blog/1/entry-317-7illusionss-emby-app-updated-for-windows-10-uwp/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.emby.media/reference/index.html
- group: auth
  href: https://artifacts.apis.io/emby/security/emby-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emby-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emby.media/
- group: docs
  title: ''
  type: Documentation
  url: https://emby.media/support/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emby.media/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emby.media/privacy.html
coverage:
  checked: '2026-10-28'
  detail: Emby provides no public API documentation or OpenAPI spec.
  evidence:
  - status: 404
    url: https://emby.media/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Emby provides a media server platform that allows users to organize, stream, and share personal video, music, and photo collections across a wide range of devices. It offers a customizable interface, supports live TV and DVR functionality, and integrates with various third‑party services. Emby is available for Windows, macOS, Linux, and NAS devices, with client apps for mobile, smart TVs, and streaming devices.
layout: provider
modified: '2026-10-28'
name: Emby
nav: Providers
network: true
overview: 'Emby is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media Server, Personal Media, Streaming, Video Library, and Music Library.


  Emby''s developer surface includes authentication, engineering blog, API reference, documentation, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 21.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/emby/emby-2026-11-03T131449.png
security:
- kind: authentication
  name: Emby Authentication
  slug: emby-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Emby Domain Security
  slug: emby-domain-security
  summary_line: TLSv1.3 · DMARC
slug: emby
tags:
- Media Server
- Personal Media
- Streaming
- Video Library
- Music Library
- Live TV
website: https://emby.media/
---
