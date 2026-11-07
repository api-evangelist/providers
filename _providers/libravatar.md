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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/libravatar/conformance/libravatar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/libravatar-conformance.yml
- group: other
  href: https://artifacts.apis.io/libravatar/hosts/libravatar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/libravatar-hosts.yml
- group: build
  href: https://artifacts.apis.io/libravatar/packages/libravatar-packages.yml
  title: ''
  type: Packages
  url: packages/libravatar-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://libravatar.org/security/
- group: build
  title: ''
  type: SDKs
  url: https://wiki.libravatar.org/libraries/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.libravatar.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/libravatar
- group: auth
  href: https://artifacts.apis.io/libravatar/security/libravatar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/libravatar-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/libravatar/security/libravatar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/libravatar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://libravatar.org/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.libravatar.org/
- group: docs
  title: ''
  type: APIReference
  url: https://wiki.libravatar.org/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://libravatar.org/accounts/new/
- group: operate
  title: ''
  type: Support
  url: https://libravatar.org/contact/
- group: company
  title: ''
  type: Blog
  url: https://blog.libravatar.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://libravatar.org/privacy/
created: '2026-10-28'
description: Libravatar provides a free, federated avatar service that lets users host their profile pictures and serve them to other websites via a simple API. The open‑source platform allows anyone to run their own instance, integrates with many applications, and offers libraries for various languages. Developers can easily add avatar support to forums, blogs, and comment systems using the documented API endpoints.
layout: provider
modified: '2026-10-28'
name: Libravatar
nav: Providers
network: true
overview: 'Libravatar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Avatars, Open Source, and Federated.


  Libravatar''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 35.7
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/libravatar/libravatar-2026-11-03T134844.png
security:
- kind: domain-security
  name: Libravatar Domain Security
  slug: libravatar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Libravatar Vulnerability Disclosure
  slug: libravatar-vulnerability-disclosure
  summary_line: no policy recorded
slug: libravatar
tags:
- Company
- Avatars
- Open Source
- Federated
website: https://libravatar.org/
---
