---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kick.com/changelog
- group: auth
  href: https://artifacts.apis.io/kick-com/security/kick-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/kick-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/kick-com/llms/kick-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kick-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/kick-com/well-known/kick-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kick-com-security.txt
- group: agent
  href: https://artifacts.apis.io/kick-com/well-known/kick-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kick-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/kick-com/hosts/kick-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kick-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/kick-com/vendors/kick-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kick-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/kick-com/packages/kick-com-packages.yml
  title: ''
  type: SDKs
  url: packages/kick-com-packages.yml
- group: build
  href: https://artifacts.apis.io/kick-com/packages/kick-com-packages.yml
  title: ''
  type: Packages
  url: packages/kick-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/kick-com/security/kick-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kick-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kick-com/security/kick-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kick-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kick.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kick.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.kick.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kick.com/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kick.com/getting-started/kick-apps-setup
- group: operate
  title: ''
  type: Support
  url: https://help.kick.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kick.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kick.com/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: Documentation at https://docs.kick.com is a JavaScript-rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.kick.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Kick (kick.com) is a live streaming platform that enables creators to broadcast video content to audiences worldwide. It offers features such as real-time chat, channel subscriptions, and monetization tools. Kick positions itself as a community-focused alternative to larger streaming services, emphasizing creator control and audience interaction. The platform supports a variety of content categories, including gaming, music, and talk shows, and provides resources for developers through its API and documentation.
image: https://kick.com/img/kick-social-logo-1600x840.png
layout: provider
modified: '2026-10-26'
name: Kick (kick.com)
nav: Providers
network: true
overview: 'Kick (kick.com) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Streaming, Live, Video, and Community.


  Kick (kick.com)''s developer surface includes changelog, documentation, API reference, getting-started guide, support, and 14 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kick Com Domain Security
  slug: kick-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kick Com Vulnerability Disclosure
  slug: kick-com-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: kick-com
tags:
- Company
- Streaming
- Live
- Video
- Community
- Platform
website: https://kick.com/
---
