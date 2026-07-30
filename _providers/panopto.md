---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Panopto Agentic Access
  operation_count: 89
  slug: panopto-agentic-access
  summary_line: 89 operations · 50 acting
api_count: 16
apis:
- description: Accessibility API
  name: Panopto Accessibility API
  slug: panopto-accessibility-api
- description: Authentication API
  name: Panopto Auth API
  slug: panopto-auth-api
- description: Caption Providers API
  name: Panopto CaptionProviders API
  slug: panopto-captionproviders-api
- description: Folder API
  name: Panopto Folders API
  slug: panopto-folders-api
- description: Group API
  name: Panopto Groups API
  slug: panopto-groups-api
- description: Playlist API
  name: Panopto Playlists API
  slug: panopto-playlists-api
- description: 'Remote Recorder Device API. Warning: this endpoint is for Panopto''s hardware partners only and cannot be used without a partner API key.'
  name: Panopto RemoteRecorderAPI API
  slug: panopto-remoterecorderapi-api
- description: Remote Recorder Management API
  name: Panopto RemoteRecorders API
  slug: panopto-remoterecorders-api
- description: Reports API
  name: Panopto Reports API
  slug: panopto-reports-api
- description: Scheduled Recording API
  name: Panopto ScheduledRecordings API
  slug: panopto-scheduledrecordings-api
- description: Search Index Integration API
  name: Panopto SearchIndexSyncUpdates API
  slug: panopto-searchindexsyncupdates-api
- description: Session API
  name: Panopto Sessions API
  slug: panopto-sessions-api
- description: Stream API
  name: Panopto Streams API
  slug: panopto-streams-api
- description: Tag API
  name: Panopto Tags API
  slug: panopto-tags-api
- description: User API
  name: Panopto Users API
  slug: panopto-users-api
- description: Portals API
  name: Panopto XfpUserProfiles API
  slug: panopto-xfpuserprofiles-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/panopto-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/panopto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/panopto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.panopto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.panopto.com/s/topic/0TO39000000EowMGAS/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Panopto
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/panopto
- group: company
  title: ''
  type: Blog
  url: https://www.panopto.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.panopto.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.panopto.com/
- group: other
  title: ''
  type: X
  url: https://x.com/Panopto
- group: commercial
  title: ''
  type: Plans
  url: plans/panopto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/panopto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/panopto-finops.yml
created: '2026-06-13'
description: Panopto is a video management platform for education and enterprise that provides a REST API for managing recordings, folders, sessions, users, and video analytics. Organizations use Panopto to capture, store, search, and share video content in corporate training and academic settings. The API supports OAuth2 authentication and enables automation of recording schedules, user and group provisioning, content organization, and integration with LMS platforms such as Canvas, Blackboard, Moodle, and D2L.
finops:
- name: Panopto Finops
  service_category: ''
  slug: panopto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/panopto.png
json_schemas:
- name: Panopto REST API Schemas
  property_count: 0
  slug: panopto-rest-api
layout: provider
modified: '2026-06-13'
name: Panopto
nav: Providers
network: true
overview: 'Panopto publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Accessibility API, Auth API, CaptionProviders API, and 13 more. Tagged areas include Video Management, Education Technology, Enterprise Video, Recording, and Learning Management.


  The Panopto catalog on APIs.io includes 1 Spectral governance ruleset.


  Panopto''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Panopto Plans Pricing
  plan_count: 2
  slug: panopto-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 1
  name: Panopto Rate Limits
  slug: panopto-rate-limits
rules:
- name: Panopto API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: panopto-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.0
  delta: -5.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/panopto/refs/heads/main/screenshots/panopto-2026-06-20T191340.png
security:
- kind: domain-security
  name: Panopto Domain Security
  slug: panopto-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Panopto Vulnerability Disclosure
  slug: panopto-vulnerability-disclosure
  summary_line: disclosure policy published
slug: panopto
tags:
- Video Management
- Education Technology
- Enterprise Video
- Recording
- Learning Management
- Video Analytics
- Content Management
website: https://www.panopto.com/
---
