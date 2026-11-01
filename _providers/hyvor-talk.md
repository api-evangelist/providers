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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Commenting platform API documented at Hyvor Talk developer docs.
  name: Hyvor Talk API
  slug: hyvor-talk-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://hyvor.com/security
- group: agent
  href: https://artifacts.apis.io/hyvor-talk/llms/hyvor-talk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hyvor-talk-llms.txt
- group: other
  href: https://artifacts.apis.io/hyvor-talk/hosts/hyvor-talk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hyvor-talk-hosts.yml
- group: other
  href: https://artifacts.apis.io/hyvor-talk/vendors/hyvor-talk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hyvor-talk-vendors.yml
- group: build
  href: https://artifacts.apis.io/hyvor-talk/packages/hyvor-talk-packages.yml
  title: ''
  type: SDKs
  url: packages/hyvor-talk-packages.yml
- group: build
  href: https://artifacts.apis.io/hyvor-talk/packages/hyvor-talk-packages.yml
  title: ''
  type: Packages
  url: packages/hyvor-talk-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hyvor.com/talk/terms
- group: operate
  title: ''
  type: Support
  url: https://hyvor.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hyvor.com
- group: auth
  title: ''
  type: Security
  url: https://hyvor.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://talk.hyvor.com/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hyvor.com/talk/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://hyvor.com/talk/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyvor
- group: docs
  title: ''
  type: Documentation
  url: https://hyvor.com/talk/docs
- group: company
  title: ''
  type: Blog
  url: https://hyvor.com/blog
- group: auth
  href: https://artifacts.apis.io/hyvor-talk/security/hyvor-talk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hyvor-talk-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hyvor-talk/security/hyvor-talk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hyvor-talk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hyvor-talk/security/hyvor-talk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hyvor-talk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hyvor.com/talk
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are JavaScript‑rendered and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 301
    url: https://hyvor.com/talk/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Hyvor Talk provides a privacy‑focused, fully‑featured commenting platform that enables websites, blogs, newsrooms, and enterprises to add interactive discussions, reactions, and ratings. The service supports easy integration with WordPress, Ghost, Wix, Squarespace, and other platforms, offering built‑in spam detection, no ads, and customizable moderation tools. Over 10,000 businesses and individual creators use Hyvor Talk to build community, increase engagement, and gather audience feedback across multiple languages.
image: https://hyvor.com/img/logo.png
layout: provider
modified: '2026-10-26'
name: Hyvor Talk
nav: Providers
network: true
overview: 'Hyvor Talk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include comments, platform, SaaS, engagement, and privacy.


  Hyvor Talk''s developer surface includes support, sandbox, pricing, documentation, engineering blog, and 15 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hyvor Talk Domain Security
  slug: hyvor-talk-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hyvor Talk Vulnerability Disclosure
  slug: hyvor-talk-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Hyvor Talk Trust Center
  slug: hyvor-talk-trust-center
  summary_line: ISO 27001, GDPR
slug: hyvor-talk
tags:
- comments
- platform
- SaaS
- engagement
- privacy
website: https://hyvor.com/talk
---
