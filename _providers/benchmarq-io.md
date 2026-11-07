---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/benchmarq-io/plans/benchmarq-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/benchmarq-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/benchmarq-io/changelog/benchmarq-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/benchmarq-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/benchmarq-io/security/benchmarq-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/benchmarq-io-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/benchmarq-io/llms/benchmarq-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/benchmarq-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/benchmarq-io/well-known/benchmarq-io-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/benchmarq-io-www-security.txt
- group: auth
  href: https://artifacts.apis.io/benchmarq-io/well-known/benchmarq-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/benchmarq-io-security.txt
- group: agent
  href: https://artifacts.apis.io/benchmarq-io/well-known/benchmarq-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/benchmarq-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/benchmarq-io/hosts/benchmarq-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benchmarq-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/benchmarq-io/vendors/benchmarq-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benchmarq-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.benchmarq.io/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://benchmarq.io/en/resources/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://benchmarq.io/en/resources/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://benchmarq.io/resources/getting-started
- group: auth
  href: https://artifacts.apis.io/benchmarq-io/security/benchmarq-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/benchmarq-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/benchmarq-io/security/benchmarq-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benchmarq-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://benchmarq.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://benchmarq.io/en/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://benchmarq.io/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://benchmarq.io/en/support
- group: operate
  title: ''
  type: Contact
  url: https://benchmarq.io/en/contact
coverage:
  checked: '2026-11-02'
  detail: Benchmarq's documentation pages are rendered via JavaScript, preventing machine-readable API specifications from being retrieved.
  evidence:
  - status: 200
    url: https://benchmarq.io/en/resources/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Benchmarq provides an AI readiness audit for websites, running over 200 standardized tests to evaluate how well a site can be discovered, read, and trusted by AI search agents. It scores each site from 0 to 100, highlights critical issues, and offers a prioritized fix list. The service includes free plans for developers and supports enterprise features via Enso DX.
image: https://benchmarq.io/og-image.png
layout: provider
modified: '2026-11-02'
name: Benchmarq
nav: Providers
network: true
overview: 'Benchmarq is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, SEO, Website Audit, Analytics, and Search.


  Benchmarq''s developer surface includes changelog, documentation, getting-started guide, pricing, support, and 15 more developer resources.'
plans:
- name: Benchmarq Io Plans Pricing
  plan_count: 3
  slug: benchmarq-io-plans-pricing
random_paper: 6
scopes:
- name: Benchmarq Io Scopes
  scope_count: 0
  slug: benchmarq-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 18.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Benchmarq Io Authentication
  slug: benchmarq-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Benchmarq Io Domain Security
  slug: benchmarq-io-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Benchmarq Io Vulnerability Disclosure
  slug: benchmarq-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: benchmarq-io
tags:
- Artificial Intelligence
- SEO
- Website Audit
- Analytics
- Search
website: https://benchmarq.io/
---
