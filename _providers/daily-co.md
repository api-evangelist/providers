---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 4
  name: Daily Co Agentic Access
  operation_count: 53
  slug: daily-co-agentic-access
  summary_line: 53 operations · 33 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: REST API for managing Daily domains, rooms, meeting tokens, recordings, transcripts, meetings, participants, presence, batch operations, dial-in/dial-out (PSTN/SIP), webhooks, live streaming and Daily
  name: Daily REST API
  slug: rest-api
- description: REST API and SDKs for deploying and managing voice AI agents built with the open-source Pipecat framework on Daily's infrastructure.
  name: Pipecat Cloud (Daily Bots) API
  slug: pipecat-cloud
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Domain API from Daily — 1 operation(s) for domain.
  name: Daily Domain API
  slug: daily-co-domain-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Meetings API from Daily — 3 operation(s) for meetings.
  name: Daily Meetings API
  slug: daily-co-meetings-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Presence API from Daily — 1 operation(s) for presence.
  name: Daily Presence API
  slug: daily-co-presence-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Recordings API from Daily — 6 operation(s) for recordings.
  name: Daily Recordings API
  slug: daily-co-recordings-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Rooms API from Daily — 9 operation(s) for rooms.
  name: Daily Rooms API
  slug: daily-co-rooms-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Webhooks API from Daily — 2 operation(s) for webhooks.
  name: Daily Webhooks API
  slug: daily-co-webhooks-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Meeting Tokens API from Daily — 2 operation(s) for meeting tokens.
  name: Daily Meeting Tokens API
  slug: daily-co-meeting-tokens-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Phone Numbers API from Daily — 4 operation(s) for phone numbers.
  name: Daily Phone Numbers API
  slug: daily-co-phone-numbers-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The batch/rooms API from Daily — 1 operation(s) for batch/rooms.
  name: Daily Batch/rooms API
  slug: daily-co-batch-rooms-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The domain-dialin-config API from Daily — 2 operation(s) for domain-dialin-config.
  name: Daily Domain Dialin Config API
  slug: daily-co-domain-dialin-config-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The logs API from Daily — 2 operation(s) for logs.
  name: Daily Logs API
  slug: daily-co-logs-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The transcript API from Daily — 3 operation(s) for transcript.
  name: Daily Transcript API
  slug: daily-co-transcript-api
- baseURL: https://api.daily.co/v1
  baseurl_source: declared
  description: The Dial In API from Daily — 6 operation(s) for dial in.
  name: Daily Dial In API
  slug: daily-co-dial-in-api
artifact_total: 38
asyncapis:
- description: ''
  name: Review
  slug: review
collections:
- collection_type: open
  name: Daily REST CallTransfer API
  slug: open-daily-co-calltransfer-api
- collection_type: open
  name: Daily REST CallTransfer DialIn API
  slug: open-daily-co-dialin-api
- collection_type: open
  name: Daily REST CallTransfer DialOut API
  slug: open-daily-co-dialout-api
- collection_type: open
  name: Daily REST CallTransfer Domain API
  slug: open-daily-co-domain-api
- collection_type: open
  name: Daily REST CallTransfer LiveStreaming API
  slug: open-daily-co-livestreaming-api
- collection_type: open
  name: Daily REST CallTransfer Meetings API
  slug: open-daily-co-meetings-api
- collection_type: open
  name: Daily REST CallTransfer MeetingTokens API
  slug: open-daily-co-meetingtokens-api
- collection_type: open
  name: Daily REST CallTransfer PhoneNumbers API
  slug: open-daily-co-phonenumbers-api
- collection_type: open
  name: Daily REST CallTransfer Presence API
  slug: open-daily-co-presence-api
- collection_type: open
  name: Daily REST CallTransfer Recordings API
  slug: open-daily-co-recordings-api
- collection_type: open
  name: Daily REST CallTransfer Rooms API
  slug: open-daily-co-rooms-api
- collection_type: open
  name: Daily REST CallTransfer Transcription API
  slug: open-daily-co-transcription-api
- collection_type: open
  name: Daily REST CallTransfer Webhooks API
  slug: open-daily-co-webhooks-api
- collection_type: open
  name: Daily REST API
  slug: open-daily-co
common:
- group: other
  href: https://artifacts.apis.io/daily-co/capabilities/daily-co-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/daily-co-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pipecat-ai/pipecat/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/pipecat-ai/pipecat/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/pipecat-ai/pipecat/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/pipecat-ai/pipecat/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/pipecat-ai/pipecat/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/daily-co/agentic-access/daily-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/daily-co-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/daily-co/security/daily-co-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/daily-co-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/daily-co/security/daily-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daily-co-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/daily-co/authentication/daily-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/daily-co-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dailyco
- group: company
  title: ''
  type: Website
  url: https://www.daily.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.daily.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.daily.co/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.daily.co/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/daily-co
- group: operate
  title: ''
  type: StatusPage
  url: https://status.daily.co/
- group: commercial
  href: https://artifacts.apis.io/daily-co/plans/daily-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/daily-co-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/daily-co/rate-limits/daily-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/daily-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/daily-co/finops/daily-co-finops.yml
  title: ''
  type: FinOps
  url: finops/daily-co-finops.yml
created: '2026-05-08'
description: Daily provides WebRTC video and audio infrastructure for developers — REST APIs for rooms, recordings, transcripts, meetings, dial-out and Daily Bots / Pipecat Cloud (voice AI agents), plus client SDKs for Web, iOS, Android, React Native and Flutter.
finops:
- has_sources: true
  method: derived
  name: Daily Co Finops
  primary_unit: ''
  service_category: ''
  slug: daily-co-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/daily-co.png
layout: provider
modified: '2026-05-08'
name: Daily
nav: Providers
network: true
overview: 'Daily publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Domain API, Meetings API, Presence API, and 12 more. Tagged areas include Daily, Real-Time, WebRTC, Video, and Audio.


  The Daily catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Daily''s developer surface includes authentication, documentation, pricing, engineering blog, GitHub presence, and 15 more developer resources.'
plans:
- name: Daily Co Plans Pricing
  plan_count: 2
  slug: daily-co-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Daily Co Rate Limits
  slug: daily-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Daily API Rules
  rule_count: 63
  severity_counts:
    error: 46
    hint: 0
    info: 5
    warn: 12
  slug: daily-co-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 65.2
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 63.2
  open_source:
    applies: true
    score: 85.0
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 48.1
      total: 27
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/daily-co/daily-co-2026-06-20T175440.png
security:
- kind: authentication
  name: Daily Co Authentication
  slug: daily-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Daily Co Domain Security
  slug: daily-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Daily Co Trust Center
  slug: daily-co-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: daily-co
tags:
- Daily
- Real-Time
- WebRTC
- Video
- Audio
- SDK
- Voice AI
- Recording
- Transcription
- Voice
website: https://www.daily.co/
---
