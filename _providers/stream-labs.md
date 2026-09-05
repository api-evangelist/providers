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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'REST API to access a user''s Streamlabs account: donations, custom alerts, loyalty points, media share, alert profiles, credits, tip jar, wheel spin, and a real-time Socket API. OAuth 2.0 with per-feat'
  name: Streamlabs API
  slug: streamlabs-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stream-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stream-labs-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/logitech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.streamlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.streamlabs.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.streamlabs.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.streamlabs.com/docs/oauth-2
- group: auth
  title: ''
  type: Authentication
  url: authentication/stream-labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stream-labs-scopes.yml
- group: operate
  title: ''
  type: Support
  url: https://support.streamlabs.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/streamlabs
- group: company
  title: ''
  type: Website
  url: https://streamlabs.com/
- group: start
  title: ''
  type: SignUp
  url: https://streamlabs.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://streamlabs.com/ultra
- group: commercial
  title: ''
  type: TermsOfService
  url: https://streamlabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://streamlabs.com/privacy
- group: design
  title: ''
  type: Conventions
  url: conventions/stream-labs-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stream-labs-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/stream-labs-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stream-labs-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stream-labs-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/stream-labs-security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stream-labs-lifecycle.yml
created: '2026-07-17'
description: Streamlabs is a live-streaming toolkit for content creators, providing alerts, donations/tips, loyalty points, media share, chat and stream widgets across Twitch, YouTube and other platforms. The Streamlabs API lets developers access a user's Streamlabs account and trigger custom alerts, read and create donations, manage loyalty points, control media-share playback, spin the wheel, empty the tip jar, roll credits, and open a real-time Socket API for live events. Access is authorized with OAuth 2.0 using granular per-feature scopes, and requests are made against the versioned REST base at streamlabs.com/api/v2.0. Streamlabs is backed by Battery Ventures and was acquired by Logitech in 2019.
image: https://cdn.streamlabs.com/static/imgs/logos/kevin-logo.png
layout: provider
modified: '2026-07-21'
name: Stream Labs
nav: Providers
network: true
overview: 'Stream Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Live Streaming, Creator Economy, Alerts, and Donations.


  Stream Labs'' developer surface includes documentation, API reference, getting-started guide, authentication, support, signup flow, pricing, and 16 more developer resources.'
random_paper: 2
scopes:
- name: Stream Labs Scopes
  scope_count: 13
  slug: stream-labs-scopes
  summary_line: 13 scopes
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 25.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stream-labs/refs/heads/main/screenshots/stream-labs-2026-09-02T160957.png
security:
- kind: authentication
  name: Stream Labs Authentication
  slug: stream-labs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Stream Labs Domain Security
  slug: stream-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stream Labs Vulnerability Disclosure
  slug: stream-labs-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: stream-labs
tags:
- Company
- Live Streaming
- Creator Economy
- Alerts
- Donations
- Loyalty Points
- Media Share
- Authentication
- Real-Time
- Streaming Tools
website: https://streamlabs.com/
---
