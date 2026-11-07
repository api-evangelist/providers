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
  band: agent-aware
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Pocket ID API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Pocket ID API
  slug: pocket-id-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/pocket-id/rules/pocket-id-rules.yml
  title: ''
  type: Spectral
  url: rules/pocket-id-rules.yml
- group: design
  href: https://artifacts.apis.io/pocket-id/vocabulary/pocket-id-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pocket-id-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/pocket-id/pocket-id/security/policy
- group: auth
  href: https://artifacts.apis.io/pocket-id/authentication/pocket-id-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pocket-id-authentication.yml
- group: design
  href: https://artifacts.apis.io/pocket-id/conformance/pocket-id-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pocket-id-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pocket-id/llms/pocket-id-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pocket-id-llms.txt
- group: auth
  href: https://artifacts.apis.io/pocket-id/well-known/pocket-id-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pocket-id-security.txt
- group: agent
  href: https://artifacts.apis.io/pocket-id/well-known/pocket-id-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pocket-id-well-known.yml
- group: other
  href: https://artifacts.apis.io/pocket-id/hosts/pocket-id-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pocket-id-hosts.yml
- group: other
  href: https://artifacts.apis.io/pocket-id/vendors/pocket-id-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pocket-id-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://pocket-id.org/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://pocket-id.org/docs/setup/installation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pocket-id.org/
- group: docs
  title: ''
  type: APIReference
  url: https://pocket-id.org/llms.txt
- group: auth
  href: https://artifacts.apis.io/pocket-id/security/pocket-id-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pocket-id-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pocket-id/security/pocket-id-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pocket-id-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pocket-id.org/
coverage:
  checked: '2026-10-26'
  detail: Main website returns a JavaScript shell preventing machine-readable access
  evidence:
  - status: 200
    url: https://pocketid.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Pocket ID is an easy-to-use, self-hosted OpenID Connect Certified™ and OAuth 2.0 provider. It enables applications to authenticate users with passkeys instead of passwords, offering a secure and passwordless login experience. The solution is open source, runs on Linux, macOS, and Windows, and can be deployed on-premises for full control over identity data.
image: https://pocket-id.org/og/index.jpg
layout: provider
modified: '2026-10-26'
name: Pocket ID
nav: Providers
network: true
overview: 'Pocket ID is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, OpenID Connect, OAuth, and Self-Hosted.


  The Pocket ID catalog on APIs.io includes 1 Spectral governance ruleset.


  Pocket ID''s developer surface includes authentication, changelog, getting-started guide, documentation, API reference, and 12 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Pocket ID API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: pocket-id-rules
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pocket-id/pocket-id-2026-11-03T141329.png
security:
- kind: authentication
  name: Pocket Id Authentication
  slug: pocket-id-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pocket Id Domain Security
  slug: pocket-id-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pocket Id Vulnerability Disclosure
  slug: pocket-id-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pocket-id
tags:
- Company
- Identity
- OpenID Connect
- OAuth
- Self-Hosted
website: https://pocket-id.org/
---
