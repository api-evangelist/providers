---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: A write-only HTTP collector that ingests customer behavioral events in real time so Movable Ink Studio can use them for targeting and content generation. Callers POST Segment-shaped JSON events (type,
  name: Movable Ink Customer Data API
  slug: customer-data-api
- description: The OpenID Connect provider that fronts the Movable Ink Studio and Da Vinci web application at app.movableink.com. It publishes a full OIDC discovery document and an RFC 8414 authorization-server meta
  name: Movable Ink Platform Identity (OpenID Connect)
  slug: identity
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/movable-ink-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/movable-ink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://movableink.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sdk-mobile.movableink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sdk-mobile.movableink.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://sdk-mobile.movableink.com/
- group: operate
  title: ''
  type: Support
  url: https://support.movableink.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://learning.movableink.com/
- group: company
  title: ''
  type: Blog
  url: https://movableink.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/movableink
- group: start
  title: ''
  type: SignUp
  url: https://app.movableink.com/
- group: start
  title: ''
  type: Login
  url: https://app.movableink.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://movableink.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://movableink.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://movableink.com/privacy-security-and-compliance
- group: auth
  title: ''
  type: Security
  url: security/movable-ink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/movable-ink-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/movable-ink-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/movable-ink-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/movable-ink-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/movable-ink-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/movable-ink-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/movable-ink-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/movable-ink-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/movable-ink-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/movable-ink-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/movable-ink-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/movable-ink-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/movable-ink-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/movable-ink-problem-types.yml
created: '2026-08-04'
description: Movable Ink is a New York-headquartered marketing technology company that turns customer data into personalized content across email, mobile and web. Its two products are Studio, which generates composite images and interactive content at the moment a message is opened, and Da Vinci, an AI decisioning layer that chooses what content each customer sees. The integration surface is a write-only Customer Data API that streams behavioral events into Studio, a family of native and wrapper mobile SDKs (iOS, Android, React Native, Cordova, Flutter, Expo), a Studio app toolchain built around the `movable` CLI and the cropduster library, and dozens of ESP/CDP connectors. API reference material is customer-gated; no OpenAPI is published.
image: https://cdn.prod.website-files.com/6601ecc67f6256b863e8143f/6655e1590788a6b11d9441a3_MovableInk-Share.jpeg
layout: provider
modified: '2026-08-04'
name: Movable Ink
nav: Providers
network: true
overview: 'Movable Ink publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Personalization, Email, and Customer Data.


  Movable Ink''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, changelog, CLI, and 23 more developer resources.'
random_paper: 65
scopes:
- name: Movable Ink Scopes
  scope_count: 0
  slug: movable-ink-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.0
  delta: -1.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 38.1
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/movable-ink/refs/heads/main/screenshots/movable-ink-2026-08-07T184344.png
security:
- kind: authentication
  name: Movable Ink Authentication
  slug: movable-ink-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Movable Ink Domain Security
  slug: movable-ink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Movable Ink Vulnerability Disclosure
  slug: movable-ink-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Movable Ink Trust Center
  slug: movable-ink-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 42001 (AI Management System), SOC 2 Type II, GDPR, CCPA, EU-U.S. Data Privacy Framework (incl. UK Extension and Swiss-U.S. DPF)
slug: movable-ink
tags:
- Company
- Marketing
- Personalization
- Email
- Customer Data
- Mobile SDK
- Artificial Intelligence
- Advertising Technology
- Content
- Events
website: https://movableink.com/
---
