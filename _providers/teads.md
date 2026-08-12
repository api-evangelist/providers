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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Server-side API for sending advertiser conversion events (Purchase, AddToCart, Lead, ViewContent, etc.) to Teads for measurement and optimization, using a Conversion API Token generated in Teads Ad Ma
  name: Teads Conversions API
  slug: teads-conversions-api
- description: V2.0 REST API that lets chatbot and LLM publishers programmatically retrieve contextually relevant sponsored and organic ad recommendations and inject them into conversational interfaces, authenticate
  name: Teads In-Chat API
  slug: teads-in-chat-api
artifact_total: 6
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
  type: MCPServer
  url: mcp/teads-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teads-llms.txt
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
created: '2026-07-17'
description: Teads is an omnichannel advertising technology platform (combined with Outbrain since 2024) that helps brands reach audiences across video, display, CTV, and conversational surfaces on 10,000+ premium publisher properties in 50+ markets. For developers and advertisers Teads exposes a server-side Conversions API for privacy-safe conversion event delivery, an In-Chat Recommendations API (V2.0) for injecting contextual ad recommendations into chatbots and LLM experiences, and first-party mobile ad SDKs for iOS, Android, React Native, and Flutter used to build premium outstream inventory inside apps. This profile catalogs those developer-facing surfaces for API discovery.
image: https://www.teads.com/wp-content/themes/teads/assets/img/teads-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: teads-mcp.yml
  slug: teads-mcpyml
modified: '2026-07-21'
name: Teads
nav: Providers
network: true
overview: 'Teads publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Advertising Technology, and Video Advertising.


  Teads'' developer surface includes authentication, changelog, documentation, support, engineering blog, and 15 more developer resources.'
random_paper: 65
score:
  band: emerging
  composite: 21.8
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 39.5
  previous_composite: 22.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
