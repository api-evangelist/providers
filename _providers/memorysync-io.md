---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Production-grade memory retention API service with vector search and summarization
  name: MemorySync API
  slug: memorysync-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/memorysync-io/rate-limits/memorysync-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/memorysync-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/memorysync-io/plans/memorysync-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/memorysync-io-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/memorysync-io/cli/memorysync-io-cli.yml
  title: ''
  type: CLI
  url: cli/memorysync-io-cli.yml
- group: operate
  href: https://artifacts.apis.io/memorysync-io/changelog/memorysync-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/memorysync-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/memorysync-io/conventions/memorysync-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/memorysync-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/memorysync-io/authentication/memorysync-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/memorysync-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/memorysync-io/conformance/memorysync-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/memorysync-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/memorysync-io/llms/memorysync-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/memorysync-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/memorysync-io/well-known/memorysync-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/memorysync-io-security.txt
- group: auth
  href: https://artifacts.apis.io/memorysync-io/well-known/memorysync-io-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/memorysync-io-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/memorysync-io/well-known/memorysync-io-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/memorysync-io-app-security.txt
- group: agent
  href: https://artifacts.apis.io/memorysync-io/well-known/memorysync-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/memorysync-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/memorysync-io/hosts/memorysync-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/memorysync-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/memorysync-io/vendors/memorysync-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/memorysync-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memorysync.io/legal/terms
- group: start
  title: ''
  type: SignUp
  url: https://app.memorysync.io/register
- group: auth
  title: ''
  type: Security
  url: https://memorysync.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memorysync.io/legal/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://memorysync.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.memorysync.io/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.memorysync.io</span
- group: auth
  href: https://artifacts.apis.io/memorysync-io/security/memorysync-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/memorysync-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/memorysync-io/security/memorysync-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memorysync-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memorysync.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.memorysync.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://memorysync.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://memorysync.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.memorysync.io
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.memorysync.io/openapi.json
  - status: null
    url: https://docs.memorysync.io/mcp
  - status: 401
    url: https://api.memorysync.io/mcp
  - status: 200
    url: https://memorysync.io/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: MemorySync provides an AI‑focused memory infrastructure platform that enables developers to store, retrieve, and orchestrate contextual memory for intelligent systems. The service offers persistent memory layers, intelligent retrieval, adaptive orchestration, and enterprise‑grade features such as multi‑tenant isolation, audit logs, and SSO. It integrates with popular AI frameworks like LangChain, LlamaIndex, and CrewAI, and supplies SDKs for Python, Node, and other languages, helping AI applications remember past interactions and improve user experiences.
image: https://memorysync.io/og-image.png
layout: provider
modified: '2026-10-30'
name: memorysync-io
nav: Providers
network: true
overview: 'memorysync-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Memory, Infrastructure, Platform, and DeveloperTools.


  memorysync-io''s developer surface includes CLI, changelog, authentication, signup flow, getting-started guide, documentation, pricing, and 21 more developer resources.'
plans:
- name: Memorysync Io Plans Pricing
  plan_count: 5
  slug: memorysync-io-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Memorysync Io Rate Limits
  slug: memorysync-io-rate-limits
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 63.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Memorysync Io Authentication
  slug: memorysync-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Memorysync Io Domain Security
  slug: memorysync-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Memorysync Io Vulnerability Disclosure
  slug: memorysync-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: memorysync-io
tags:
- AI
- Memory
- Infrastructure
- Platform
- DeveloperTools
- Company
website: https://memorysync.io/
---
