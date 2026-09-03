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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'OAuth 2.0 REST API for programmatic access to Burner line management, messaging (SMS/MMS) and configuration, plus a webhook system for real-time event notifications. Requests use `Authorization: Beare'
  name: Burner API
  slug: burner-api
artifact_total: 4
asyncapis:
- description: ''
  name: Burner Webhooks
  slug: burner-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.burnerapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/adhoclabs/burner-app-starter-kit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adhoclabs
- group: company
  title: ''
  type: Blog
  url: https://www.burnerapp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.burnerapp.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.burnerapp.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.burnerapp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.burnerapp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adhoclabs.co/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.burnerapp.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/burner-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/burner-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/burner-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/burner-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/burner-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/burner-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/burner-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/burner-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/burner-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/burner-domain-security.yml
created: '2026-07-17'
description: Burner is the original second-phone-number app from Ad Hoc Labs (founded 2012, Los Angeles), letting people create multiple temporary or permanent phone numbers on a single iOS or Android device for privacy, communication management, and boundary-setting. Burner supports voice calls, SMS and MMS over VoIP/PSTN, with spam blocking, voicemail transcription, auto-reply and multi-line management. For developers, Burner exposes an OAuth 2.0 REST API (api.burnerapp.com) for programmatic line management and messaging, a webhook system for real-time event notifications, and the open-source Burner App Starter Kit (BASK) for building Burner-integrated apps and bots such as Hostbot and Ghostbot.
image: https://cdn.prod.website-files.com/61a66db931b63404b86e2ae5/61c08c40a49820520cc24482_OpenGraph.jpg
layout: provider
modified: '2026-07-18'
name: Burner
nav: Providers
network: true
overview: 'Burner publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Phone Numbers, SMS, MMS, and Voice.


  The Burner catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Burner''s developer surface includes documentation, engineering blog, pricing, support, authentication, and 15 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 39.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/burner/refs/heads/main/screenshots/burner-2026-07-25T204111.png
security:
- kind: authentication
  name: Burner Authentication
  slug: burner-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Burner Domain Security
  slug: burner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: burner
tags:
- Company
- Phone Numbers
- SMS
- MMS
- Voice
- Messaging
- Telephony
- Privacy
- Communications
- Second Phone Number
- Authentication
- Webhook
website: https://www.burnerapp.com
---
