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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for controlling bHaptics devices
  name: Bhaptics API
  slug: bhaptics-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bhaptics/refs/heads/main/llms/bhaptics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bhaptics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bhaptics/refs/heads/main/hosts/bhaptics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bhaptics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bhaptics/refs/heads/main/vendors/bhaptics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bhaptics-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bhaptics/refs/heads/main/packages/bhaptics-packages.yml
  title: ''
  type: SDKs
  url: packages/bhaptics-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bhaptics/refs/heads/main/packages/bhaptics-packages.yml
  title: ''
  type: Packages
  url: packages/bhaptics-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bhaptics.com/legals/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bhaptics.com/legals/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.bhaptics.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.bhaptics.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bhaptics
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bhaptics/refs/heads/main/security/bhaptics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bhaptics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bhaptics.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bhaptics.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bhaptics.com/support/developers/?type=sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bhaptics.com/about
- group: operate
  title: ''
  type: Support
  url: https://support.bhaptics.com
coverage:
  checked: '2026-09-28'
  detail: Docs site renders via Docusaurus JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.bhaptics.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bhaptics creates advanced haptic technology, offering wearable haptic suits, vests, and accessories that enable developers to integrate tactile feedback into games, VR experiences, and other interactive applications. Their platform provides SDKs, APIs, and developer tools to control haptic patterns, synchronize with audio and visual cues, and deliver immersive sensations across a range of devices.
image: https://www.bhaptics.com/images/opengraph-image.jpg
layout: provider
modified: '2026-09-28'
name: Bhaptics
nav: Providers
network: true
overview: 'Bhaptics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Haptics, Wearables, Gaming, and VR.


  Bhaptics'' developer surface includes engineering blog, documentation, getting-started guide, support, and 12 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bhaptics Domain Security
  slug: bhaptics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bhaptics
tags:
- Company
- Haptics
- Wearables
- Gaming
- VR
- Developer Tools
website: https://www.bhaptics.com
---
