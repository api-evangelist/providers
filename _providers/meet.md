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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Meet Agentic Access
  operation_count: 16
  slug: meet-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 1
apis:
- baseURL: https://meet.googleapis.com/v2
  baseurl_source: declared
  description: The Conference Records API from Google Meet — 2 operation(s) for conference records.
  name: Google Meet Conference Records API
  slug: meet-conference-records-api
- baseURL: https://meet.googleapis.com/v2
  baseurl_source: declared
  description: The Participants API from Google Meet — 4 operation(s) for participants.
  name: Google Meet Participants API
  slug: meet-participants-api
- baseURL: https://meet.googleapis.com/v2
  baseurl_source: declared
  description: The Recordings API from Google Meet — 2 operation(s) for recordings.
  name: Google Meet Recordings API
  slug: meet-recordings-api
- baseURL: https://meet.googleapis.com/v2
  baseurl_source: declared
  description: The Spaces API from Google Meet — 3 operation(s) for spaces.
  name: Google Meet Spaces API
  slug: meet-spaces-api
- baseURL: https://meet.googleapis.com/v2
  baseurl_source: declared
  description: The Transcripts API from Google Meet — 4 operation(s) for transcripts.
  name: Google Meet Transcripts API
  slug: meet-transcripts-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Meet REST Conference Records API
  slug: open-meet-conference-records-api
- collection_type: open
  name: Google Meet REST Conference Records Participants API
  slug: open-meet-participants-api
- collection_type: open
  name: Google Meet REST Conference Records Recordings API
  slug: open-meet-recordings-api
- collection_type: open
  name: Google Meet REST Conference Records Spaces API
  slug: open-meet-spaces-api
- collection_type: open
  name: Google Meet REST Conference Records Transcripts API
  slug: open-meet-transcripts-api
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
overview: 'Google Meet publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Conference Records API, Participants API, Recordings API, and 2 more. Tagged areas include Video Conferencing, Meetings, Communications, Collaboration, and Google Workspace.


  Google Meet''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 7
scopes:
- name: Meet Scopes
  scope_count: 3
  slug: meet-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Communications
- Collaboration
- Google Workspace
- Recordings
- Transcripts
website: https://meet.google.com/
---
