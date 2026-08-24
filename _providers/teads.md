---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.1
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Server-side API for sending advertiser conversion events (Purchase, AddToCart, Lead, ViewContent, etc.) to Teads for measurement and optimization, using a Conversion API Token generated in Teads Ad Ma
  name: Teads Conversions API
  slug: teads-conversions-api
- description: V2.0 REST API that lets chatbot and LLM publishers programmatically retrieve contextually relevant sponsored and organic ad recommendations and inject them into conversational interfaces, authenticate
  name: Teads In-Chat API
  slug: teads-in-chat-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/teads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teads-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/teads-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/teads-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/teads-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/teads-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teads-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teads-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teads-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/teads-security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/teads-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/teads-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/teads-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teads-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/teads-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/teads-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teads-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teads-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/teads-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/teads-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/teads-conformance.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.teads.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.teads.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.teads.com/docs/Chatbot-AI-SDK/Getting-Started/integration-guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.teads.com/docs/Chatbot-AI-SDK/Getting-Started/
- group: company
  title: ''
  type: Website
  url: https://www.teads.com/
- group: operate
  title: ''
  type: Support
  url: https://support.teads.tv/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teads
- group: company
  title: ''
  type: Blog
  url: https://www.teads.com/blog/
- group: start
  title: ''
  type: Login
  url: https://login.teads.tv/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teads.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teads.com/privacy-policy/
created: '2026-07-17'
description: Teads is an omnichannel advertising technology platform (combined with Outbrain since 2024) that helps brands reach audiences across video, display, CTV, and conversational surfaces on 10,000+ premium publisher properties in 50+ markets. For developers and advertisers Teads exposes a server-side Conversions API for privacy-safe conversion event delivery, an In-Chat Recommendations API (V2.0) for injecting contextual ad recommendations into chatbots and LLM experiences, and first-party mobile ad SDKs for iOS, Android, React Native, and Flutter used to build premium outstream inventory inside apps. This profile catalogs those developer-facing surfaces for API discovery.
image: https://www.teads.com/wp-content/themes/teads/assets/img/teads-logo.svg
layout: provider
modified: '2026-08-13'
name: Teads
nav: Providers
network: true
overview: 'Teads publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Advertising Technology, and Video Advertising.


  Teads'' developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 25 more developer resources.'
plans:
- name: Teads Plans Pricing
  plan_count: 0
  slug: teads-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Teads Rate Limits
  slug: teads-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 38.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Teads Authentication
  slug: teads-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Teads Domain Security
  slug: teads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Teads Vulnerability Disclosure
  slug: teads-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Teads Trust Center
  slug: teads-trust-center
  summary_line: SOX (Sarbanes-Oxley), unnamed security accreditations
slug: teads
tags:
- Company
- Advertising
- AdTech
- Advertising Technology
- Video Advertising
- Conversions API
- Contextual Advertising
- Mobile SDK
- Conversational AI
website: https://www.teads.com/
---
