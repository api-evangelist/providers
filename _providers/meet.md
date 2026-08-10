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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Meet Agentic Access
  operation_count: 16
  slug: meet-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 5
apis:
- description: The Conference Records API from Google Meet — 2 operation(s) for conference records.
  name: Google Meet Conference Records API
  slug: meet-conference-records-api
- description: The Participants API from Google Meet — 4 operation(s) for participants.
  name: Google Meet Participants API
  slug: meet-participants-api
- description: The Recordings API from Google Meet — 2 operation(s) for recordings.
  name: Google Meet Recordings API
  slug: meet-recordings-api
- description: The Spaces API from Google Meet — 3 operation(s) for spaces.
  name: Google Meet Spaces API
  slug: meet-spaces-api
- description: The Transcripts API from Google Meet — 4 operation(s) for transcripts.
  name: Google Meet Transcripts API
  slug: meet-transcripts-api
artifact_total: 11
collections:
- collection_type: open
  name: Google Meet REST API
  slug: open-meet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/meet-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://meet.google.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/workspace/meet
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing.html
- group: start
  title: ''
  type: Signup
  url: https://accounts.google.com/signup
created: '2026-05-11'
description: Google Meet is Google Workspace's secure video conferencing service for one-on-one calls, team meetings, large webinars, and live streamed events with features like noise cancellation, captions, recordings, and transcripts. The Google Meet REST API enables developers to programmatically create and manage meeting spaces, access conference records, list participants, and fetch artifacts such as recordings and transcripts directly from their apps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meet.png
layout: provider
modified: '2026-05-11'
name: Google Meet
nav: Providers
network: true
overview: 'Google Meet publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Conference Records API, Participants API, Recordings API, and 2 more. Tagged areas include Video Conferencing, Meetings, Communication, Collaboration, and Google Workspace.


  Google Meet''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 79
scopes:
- name: Meet Scopes
  scope_count: 3
  slug: meet-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: emerging
  composite: 27.0
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meet/refs/heads/main/screenshots/meet-2026-06-20T185127.png
security:
- kind: authentication
  name: Meet Authentication
  slug: meet-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Meet Domain Security
  slug: meet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meet Vulnerability Disclosure
  slug: meet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meet
tags:
- Video Conferencing
- Meetings
- Communication
- Collaboration
- Google Workspace
- Recordings
- Transcripts
website: https://meet.google.com/
---
