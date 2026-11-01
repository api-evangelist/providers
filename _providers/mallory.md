---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API - Threat intelligence platform API (private endpoints excluded)
  name: Core API
  slug: core-api
artifact_total: 6
asyncapis:
- description: ''
  name: Mallory Webhooks
  slug: mallory-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/mallory/plans/mallory-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mallory-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mallory/asyncapi/mallory-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mallory-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/mallory/security/mallory-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mallory-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mallory/authentication/mallory-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mallory-authentication.yml
- group: design
  href: https://artifacts.apis.io/mallory/conformance/mallory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mallory-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mallory/llms/mallory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mallory-llms.txt
- group: other
  href: https://artifacts.apis.io/mallory/a2a/mallory-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mallory-a2a.yml
- group: auth
  href: https://artifacts.apis.io/mallory/well-known/mallory-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mallory-security.txt
- group: agent
  href: https://artifacts.apis.io/mallory/well-known/mallory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mallory-well-known.yml
- group: other
  href: https://artifacts.apis.io/mallory/hosts/mallory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mallory-hosts.yml
- group: other
  href: https://artifacts.apis.io/mallory/vendors/mallory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mallory-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.mallory.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mallory.ai
- group: company
  title: ''
  type: Newsroom
  url: https://mallory.ai/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mallory.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mallory.ai/quickstart
- group: auth
  href: https://artifacts.apis.io/mallory/security/mallory-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mallory-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mallory/security/mallory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mallory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mallory.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mallory.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mallory.ai/api-reference/introduction
- group: company
  title: ''
  type: Blog
  url: https://mallory.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/malloryai
- group: commercial
  title: ''
  type: Pricing
  url: https://mallory.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mallory.ai/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mallory.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mallory.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.mallory.ai/mcp
  - status: 401
    url: https://app.mallory.ai/api/mcp
  - status: 200
    url: https://mallory.ai
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Mallory provides an AI‑native threat intelligence and exposure management platform that aggregates data from numerous sources into a unified intelligence graph. It helps security teams prioritize real adversary activity over raw CVSS scores, offering use‑case driven workflows, integrations with existing tools, and live dashboards to monitor emerging threats and vulnerabilities across the enterprise.
image: https://mallory.ai/opengraph-image?9b69806d880b0874
layout: provider
modified: '2026-10-29'
name: Mallory
nav: Providers
network: true
overview: 'Mallory is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Threat Intelligence, AI, Platform, and Exposure Management.


  The Mallory catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mallory''s developer surface includes authentication, changelog, getting-started guide, documentation, API reference, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Mallory Plans Pricing
  plan_count: 2
  slug: mallory-plans-pricing
random_paper: 0
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 42.9
    discoverability: 67.9
    operational_transparency: 55.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mallory Authentication
  slug: mallory-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mallory Domain Security
  slug: mallory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mallory Vulnerability Disclosure
  slug: mallory-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mallory
tags:
- Security
- Threat Intelligence
- AI
- Platform
- Exposure Management
website: https://mallory.ai
---
