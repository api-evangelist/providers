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
    agent_card: flavored
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
  score: 1.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Vivioo platform, providing test code generation and agent execution endpoints.
  name: Vivioo API
  slug: vivioo-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://vivioo.io/security
- group: agent
  href: https://artifacts.apis.io/vivioo-io/llms/vivioo-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vivioo-io-llms.txt
- group: other
  href: https://artifacts.apis.io/vivioo-io/a2a/vivioo-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/vivioo-io-a2a.yml
- group: auth
  href: https://artifacts.apis.io/vivioo-io/well-known/vivioo-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vivioo-io-security.txt
- group: agent
  href: https://artifacts.apis.io/vivioo-io/well-known/vivioo-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vivioo-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/vivioo-io/hosts/vivioo-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vivioo-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/vivioo-io/vendors/vivioo-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vivioo-io-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/viviooio
- group: auth
  href: https://artifacts.apis.io/vivioo-io/security/vivioo-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vivioo-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vivioo-io/security/vivioo-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vivioo-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vivioo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://vivioo.io/guides
- group: company
  title: ''
  type: Blog
  url: https://vivioo.io/journal
- group: company
  title: ''
  type: About
  url: https://vivioo.io/about-vivienne
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vivioo.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vivioo.io/privacy
created: '2026-10-30'
description: Vivioo.io provides a platform for testing AI agents on harmless tasks, ensuring they ask for permission before acting. The service offers a simple web interface where users can generate test codes, run agents like Claude, ChatGPT, and others through predefined errands, and receive detailed proof of behavior. It emphasizes privacy, transparency, and ethical AI interactions, with no sign‑up required and no collection of personal data.
image: https://vivioo.io/opengraph-image?64f98004b3831177
layout: provider
modified: '2026-10-30'
name: vivioo-io
nav: Providers
network: true
overview: 'vivioo-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Ethics, Testing, and Privacy.


  vivioo-io''s developer surface includes documentation, engineering blog, and 14 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 64.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vivioo-io/vivioo-io-2026-11-03T145908.png
security:
- kind: domain-security
  name: Vivioo Io Domain Security
  slug: vivioo-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vivioo Io Vulnerability Disclosure
  slug: vivioo-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vivioo-io
tags:
- Company
- Artificial Intelligence
- Ethics
- Testing
- Privacy
website: https://vivioo.io/
---
