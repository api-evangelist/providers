---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-09-08'
api_count: 1
apis:
- baseURL: https://api.vettly.dev
  baseurl_source: declared
  description: Content moderation REST API for evaluating text, images, and video against policies, with batch checks, webhooks, and OpenClaw Guardrails endpoints for agent skill vetting and action authorization.
  name: Vettly REST API
  slug: vettly-rest-api
artifact_total: 8
asyncapis:
- description: ''
  name: Vettly Webhooks
  slug: vettly-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://vettly.dev
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vettly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vettly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vettly-authentication.yml
- group: auth
  title: ''
  type: Security
  url: security/vettly-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/vettly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vettly-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vettly-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vettly-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vettly-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/vettly-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vettly-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vettly.dev
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vettly-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/vettly-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vettly-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vettly-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vettly-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vettly-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vettly-plans-pricing.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vettly.dev/guide/getting-started.html
- group: company
  title: ''
  type: Blog
  url: https://vettly.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://vettly.dev/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://vettly.dev/sign-up
- group: start
  title: ''
  type: Login
  url: https://vettly.dev/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vettly.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vettly.dev/privacy
created: '2026-09-06'
description: Developer-first content moderation for text, images, and video with policy versioning, appeals, and audit trails. Also offers OpenClaw Guardrails for vetting agent skills and authorizing runtime actions.
image: https://vettly.dev/vettly-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Vettly MCP Server
  slug: vettly-mcp-server
modified: '2026-09-07'
name: Vettly
nav: Providers
network: true
overview: 'Vettly publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include content-moderation, trust-and-safety, security, text-analysis, and image-moderation.


  The Vettly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vettly''s developer surface includes authentication, changelog, sandbox, getting-started guide, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Vettly Plans Pricing
  plan_count: 3
  slug: vettly-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Vettly Rate Limits
  slug: vettly-rate-limits
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 4.5
    contract_quality: 59.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 52.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Vettly Authentication
  slug: vettly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vettly Domain Security
  slug: vettly-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vettly Vulnerability Disclosure
  slug: vettly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vettly
tags:
- content-moderation
- trust-and-safety
- security
- text-analysis
- image-moderation
- video-moderation
- UGC
- compliance
- agent-guardrails
- MCP
website: https://vettly.dev
---
