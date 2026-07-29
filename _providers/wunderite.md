---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API (v1) for programmatic access to Wunderite risk data and related resources — risk profiles, buildings, vehicles, drivers, contacts, premises, equipment, homes, legal entities, liabilities, sub
  name: Wunderite API
  slug: wunderite-api
artifact_total: 6
asyncapis:
- description: ''
  name: Wunderite Webhooks
  slug: wunderite-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://wunderite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wunderite.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wunderite.com/objects
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wunderite.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.wunderite.com
- group: company
  title: ''
  type: Blog
  url: https://wunderite.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wunderite
- group: commercial
  title: ''
  type: Pricing
  url: https://wunderite.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.wunderite.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wunderite.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wunderite.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wunderite.com/
- group: auth
  title: ''
  type: Security
  url: https://wunderite.com/security/bug-bounty-program/
- group: auth
  title: ''
  type: Compliance
  url: https://wunderite.com/security/
- group: build
  title: ''
  type: Packages
  url: packages/wunderite-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wunderite-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/wunderite-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wunderite-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/wunderite-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wunderite-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wunderite-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wunderite-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wunderite-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wunderite-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wunderite-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wunderite-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wunderite-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wunderite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wunderite-trust-center.yml
created: '2026-07-17'
description: Wunderite is an insurance application automation platform for agencies and brokers that finds, autofills, and digitally signs insurance forms — ACORDs and supplementals — up to 12x faster than manual workflows. The platform pairs a powerful autofill engine with live customer collaboration, spreadsheet-like schedule editors, third-party data enrichment, and built-in e-signature (ESIGN/UETA). The Wunderite REST API (v1) exposes risk profiles and risk data — buildings, vehicles, drivers, contacts, premises, equipment, workers' comp, subjects of insurance and more — with bearer-token auth, cursor pagination, field inclusion, and HMAC-signed webhooks, plus direct integrations with Vertafore AMS360, ImageRight, and Zapier. Wunderite is SOC 2 Type II audited and a Techstars portfolio company.
image: https://wunderite.com/wp-content/uploads/2021/12/wunderite-logo-white-bg-3x2-1.png
layout: provider
modified: '2026-07-21'
name: Wunderite
nav: Providers
network: true
overview: 'Wunderite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, ACORD Forms, and Risk Data.


  The Wunderite catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wunderite''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 23
score:
  band: developing
  composite: 51.6
  delta: 3.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 43.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 48.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wunderite Authentication
  slug: wunderite-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wunderite Domain Security
  slug: wunderite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wunderite Vulnerability Disclosure
  slug: wunderite-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Wunderite Trust Center
  slug: wunderite-trust-center
  summary_line: SOC 2 Type II
slug: wunderite
tags:
- Company
- Insurance
- Insurtech
- ACORD Forms
- Risk Data
- Digital Signatures
- Insurance Applications
- Webhooks
website: https://wunderite.com/
---
