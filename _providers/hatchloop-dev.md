---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Agent-callable service for discovering, verifying, communicating with, scheduling, and transacting with small/mid businesses.
  name: SMB Transaction & Communication Broker API
  slug: smb-transaction-communication-broker-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/hatchloop-dev/plans/hatchloop-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hatchloop-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hatchloop-dev/changelog/hatchloop-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hatchloop-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/hatchloop-dev/authentication/hatchloop-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hatchloop-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/hatchloop-dev/conformance/hatchloop-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hatchloop-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hatchloop-dev/llms/hatchloop-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hatchloop-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/hatchloop-dev/a2a/hatchloop-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hatchloop-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hatchloop-dev/well-known/hatchloop-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hatchloop-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/hatchloop-dev/hosts/hatchloop-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hatchloop-dev-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hatchloop.dev/terms
- group: operate
  title: ''
  type: Support
  url: https://hatchloop.dev/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hatchloop.dev/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://hatchloop.dev/changelog/
- group: docs
  title: ''
  type: APIReference
  url: https://hatchloop.dev/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/hatchloop-dev/security/hatchloop-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hatchloop-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hatchloop.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://hatchloop.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://hatchloop.dev/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hatchloop.dev/portal
- group: start
  title: ''
  type: GettingStarted
  url: https://hatchloop.dev/docs/#key
- group: operate
  title: ''
  type: Changelog
  url: https://hatchloop.dev/changelog
created: '2026-10-29'
description: Hatchloop.dev is a technology company focused on providing developers with a robust platform for building, testing, and deploying loop-based automation workflows. The service offers a comprehensive API suite that enables integration with various cloud services, real-time monitoring, and extensive documentation for developers. Hatchloop aims to simplify complex automation scenarios, offering scalable solutions for enterprises and startups alike, with a strong emphasis on security, reliability, and developer experience.
image: https://hatchloop.dev/og?title=Verify%2C+message+and+book+with+real+businesses
layout: provider
modified: '2026-10-29'
name: hatchloop-dev
nav: Providers
network: true
overview: 'hatchloop-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, API, Platform, and DeveloperTools.


  hatchloop-dev''s developer surface includes changelog, authentication, support, API reference, documentation, pricing, getting-started guide, and 13 more developer resources.'
plans:
- name: Hatchloop Dev Plans Pricing
  plan_count: 2
  slug: hatchloop-dev-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: derived
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
- kind: authentication
  name: Hatchloop Dev Authentication
  slug: hatchloop-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hatchloop Dev Domain Security
  slug: hatchloop-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hatchloop-dev
tags:
- Company
- Automation
- API
- Platform
- DeveloperTools
website: https://hatchloop.dev/
---
