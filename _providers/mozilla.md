---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/mozilla/llms/mozilla-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mozilla-llms.txt
- group: auth
  href: https://artifacts.apis.io/mozilla/well-known/mozilla-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mozilla-security.txt
- group: auth
  href: https://artifacts.apis.io/mozilla/well-known/mozilla-mozilla-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mozilla-mozilla-security.txt
- group: agent
  href: https://artifacts.apis.io/mozilla/well-known/mozilla-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mozilla-well-known.yml
- group: other
  href: https://artifacts.apis.io/mozilla/hosts/mozilla-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mozilla-hosts.yml
- group: other
  href: https://artifacts.apis.io/mozilla/vendors/mozilla-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mozilla-vendors.yml
- group: build
  href: https://artifacts.apis.io/mozilla/packages/mozilla-packages.yml
  title: ''
  type: SDKs
  url: packages/mozilla-packages.yml
- group: build
  href: https://artifacts.apis.io/mozilla/packages/mozilla-packages.yml
  title: ''
  type: Packages
  url: packages/mozilla-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mozilla.org/en-US/security/
- group: other
  title: ''
  type: Leadership
  url: https://www.mozilla.org/en-US/about/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mozilla.org/en-US/
- group: auth
  href: https://artifacts.apis.io/mozilla/security/mozilla-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mozilla-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mozilla/security/mozilla-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mozilla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mozilla.org/
- group: docs
  title: ''
  type: Documentation
  url: https://mozilla.github.io/glean/
- group: start
  title: ''
  type: GettingStarted
  url: https://mozilla.github.io/glean/book/user/adding-glean-to-your-project/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.mozilla.org/
- group: company
  title: ''
  type: Blog
  url: https://blog.mozilla.org/data/tag/glean/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mozilla/glean
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mozilla.org/en-US/about/legal/terms/mozilla/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mozilla.org/en-US/privacy/
coverage:
  checked: '2026-10-28'
  detail: Glean documentation provides SDK guides but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://mozilla.github.io/glean/book/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Mozilla Glean is an open-source telemetry library developed by Mozilla that provides cross-platform SDKs for collecting, aggregating, and exporting product usage data. It powers data collection in Firefox and other Mozilla applications, offering a privacy-preserving design, configurable metrics, and a data-control plane for developers to manage data pipelines. The project is hosted on GitHub and documented with comprehensive guides, API references, and examples for Android, iOS, JavaScript, Rust, and other platforms.
image: https://www.mozilla.org/media/img/m24/og.3a69dffad83e.png
layout: provider
modified: '2026-10-28'
name: Mozilla Glean
nav: Providers
network: true
overview: 'Mozilla Glean is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telemetry, SDK, Open Source, Data Engineering, and Mozilla.


  Mozilla Glean''s developer surface includes documentation, getting-started guide, support, engineering blog, and 17 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 0
  name: Mozilla Rate Limits
  slug: mozilla-rate-limits
scopes:
- name: Mozilla Scopes
  scope_count: 0
  slug: mozilla-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 56.3
    operational_transparency: 7.9
  previous_composite: 24.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mozilla/mozilla-2026-11-03T135859.png
security:
- kind: authentication
  name: Mozilla Authentication
  slug: mozilla-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mozilla Domain Security
  slug: mozilla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mozilla Vulnerability Disclosure
  slug: mozilla-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mozilla
tags:
- Telemetry
- SDK
- Open Source
- Data Engineering
- Mozilla
website: https://mozilla.org/
---
