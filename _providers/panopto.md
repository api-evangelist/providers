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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Panopto Agentic Access
  operation_count: 89
  slug: panopto-agentic-access
  summary_line: 89 operations · 50 acting
api_count: 1
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
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Panopto Public Accessibility API
  slug: open-panopto-accessibility-api
- collection_type: open
  name: Panopto Public Accessibility Auth API
  slug: open-panopto-auth-api
- collection_type: open
  name: Panopto Public Accessibility CaptionProviders API
  slug: open-panopto-captionproviders-api
- collection_type: open
  name: Panopto Public Accessibility Folders API
  slug: open-panopto-folders-api
- collection_type: open
  name: Panopto Public Accessibility Groups API
  slug: open-panopto-groups-api
- collection_type: open
  name: Panopto Public Accessibility Playlists API
  slug: open-panopto-playlists-api
- collection_type: open
  name: Panopto Public Accessibility RemoteRecorderAPI API
  slug: open-panopto-remoterecorderapi-api
- collection_type: open
  name: Panopto Public Accessibility RemoteRecorders API
  slug: open-panopto-remoterecorders-api
- collection_type: open
  name: Panopto Public Accessibility Reports API
  slug: open-panopto-reports-api
- collection_type: open
  name: Panopto Public Accessibility ScheduledRecordings API
  slug: open-panopto-scheduledrecordings-api
- collection_type: open
  name: Panopto Public Accessibility SearchIndexSyncUpdates API
  slug: open-panopto-searchindexsyncupdates-api
- collection_type: open
  name: Panopto Public Accessibility Sessions API
  slug: open-panopto-sessions-api
- collection_type: open
  name: Panopto Public Accessibility Streams API
  slug: open-panopto-streams-api
- collection_type: open
  name: Panopto Public Accessibility Tags API
  slug: open-panopto-tags-api
- collection_type: open
  name: Panopto Public Accessibility Users API
  slug: open-panopto-users-api
- collection_type: open
  name: Panopto Public Accessibility XfpUserProfiles API
  slug: open-panopto-xfpuserprofiles-api
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
random_paper: 13
rate_limits:
- limit_count: 1
  name: Panopto Rate Limits
  slug: panopto-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Panopto API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: panopto-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 45.1
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 33.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
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
