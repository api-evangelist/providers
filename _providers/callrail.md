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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Callrail Agentic Access
  operation_count: 8
  slug: callrail-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 3
apis:
- description: REST API providing programmatic access to CallRail accounts, companies, tracking numbers, calls, text messages, form submissions, users, tags, and integrations. Requests authenticate via the HTTP head
  name: CallRail v3 API
  slug: v3-api
- description: The Accounts API from CallRail — 2 operation(s) for accounts.
  name: CallRail Accounts API
  slug: callrail-accounts-api
- description: The Calls API from CallRail — 4 operation(s) for calls.
  name: CallRail Calls API
  slug: callrail-calls-api
artifact_total: 7
collections:
- collection_type: open
  name: CallRail v3 API
  slug: open-callrail
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/callrail-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/callrail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/callrail-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.callrail.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.callrail.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.callrail.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.callrail.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.callrail.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.callrail.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CallRail
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/callrail
created: '2026-05-11'
description: CallRail is a call tracking and conversation intelligence platform that attributes phone calls, texts, and form fills to marketing campaigns and applies AI-powered transcription, sentiment, and lead scoring to inbound conversations. The CallRail v3 API is a REST/JSON interface exposing accounts, companies, trackers, calls, texts, form submissions, and integrations. Authentication uses an account API key passed in the HTTP Authorization header against a base URL of https://api.callrail.com/v3/.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/callrail.png
layout: provider
modified: '2026-05-11'
name: CallRail
nav: Providers
network: true
overview: 'CallRail publishes 2 APIs on the [APIs.io](https://apis.io/) network: Accounts API and Calls API. Tagged areas include Call Tracking, Conversation Intelligence, Marketing Attribution, Lead Tracking, and Telephony.


  CallRail''s developer surface includes authentication, documentation, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 24
score:
  band: thin
  composite: 33.9
  delta: 2.1
  facets:
    commercial_clarity: 23.7
    contract_quality: 58.2
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/callrail/refs/heads/main/screenshots/callrail-2026-06-20T173850.png
security:
- kind: authentication
  name: Callrail Authentication
  slug: callrail-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Callrail Domain Security
  slug: callrail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: callrail
tags:
- Call Tracking
- Conversation Intelligence
- Marketing Attribution
- Lead Tracking
- Telephony
- Analytics
- Form Tracking
website: https://www.callrail.com
---
