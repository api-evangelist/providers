---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for Synento video platform
  name: Synento API
  slug: synento-api
artifact_total: 5
asyncapis:
- description: ''
  name: Synento Com Webhooks
  slug: synento-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/synento-com/plans/synento-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/synento-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/synento-com/asyncapi/synento-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/synento-com-webhooks.yml
- group: build
  href: https://artifacts.apis.io/synento-com/cli/synento-com-cli.yml
  title: ''
  type: CLI
  url: cli/synento-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/synento-com/changelog/synento-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/synento-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/synento-com/conformance/synento-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/synento-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/synento-com/llms/synento-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synento-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/synento-com/well-known/synento-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/synento-com-security.txt
- group: auth
  href: https://artifacts.apis.io/synento-com/well-known/synento-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/synento-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/synento-com/well-known/synento-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/synento-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/synento-com/hosts/synento-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/synento-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/synento-com/vendors/synento-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/synento-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/synento-com/packages/synento-com-packages.yml
  title: ''
  type: SDKs
  url: packages/synento-com-packages.yml
- group: build
  href: https://artifacts.apis.io/synento-com/packages/synento-com-packages.yml
  title: ''
  type: Packages
  url: packages/synento-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://synento.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://synento.com/changelog
- group: start
  title: ''
  type: SignUp
  url: https://synento.com/signup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.synento.com`
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Synento
- group: auth
  href: https://artifacts.apis.io/synento-com/security/synento-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/synento-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/synento-com/security/synento-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synento-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://synento.com
- group: docs
  title: ''
  type: Documentation
  url: https://synento.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://synento.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://synento.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://synento.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://synento.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://synento.com/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: https://synento.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://synento.com/pricing
- group: docs
  title: ''
  type: OpenAPI
  url: https://synento.com/openapi.json
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://synento.com/openapi.json
  - status: 401
    url: https://api.synento.com/mcp
  - status: 200
    url: https://synento.com
  reason: partner-login
  state: gated
created: '2026-11-04'
description: Synento provides an agent‑native video API that lets developers capture live video streams directly from browsers using WebCodecs, transmit binary frames over WebSocket, and store each session as a durable stream. The platform offers replay, windowed playback, and MP4 export, all accessible via REST, webhooks, and SDKs without requiring separate media servers. Documentation, pricing, and an OpenAPI 3.1 spec are publicly available.
image: https://synento.com/og/en/home
layout: provider
modified: '2026-11-04'
name: Synento
nav: Providers
network: true
overview: 'Synento is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video, WebRTC, WebCodecs, WebSocket, and Streaming.


  The Synento catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Synento''s developer surface includes CLI, changelog, signup flow, documentation, API reference, getting-started guide, pricing, and 23 more developer resources.'
plans:
- name: Synento Com Plans Pricing
  plan_count: 2
  slug: synento-com-plans-pricing
random_paper: 20
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 39.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Synento Com Domain Security
  slug: synento-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Synento Com Vulnerability Disclosure
  slug: synento-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: synento-com
tags:
- Video
- WebRTC
- WebCodecs
- WebSocket
- Streaming
website: https://synento.com
---
