---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Whoop Agentic Access
  operation_count: 21
  slug: whoop-agentic-access
  summary_line: 21 operations · 6 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Utility endpoints for activity ID mapping
  name: WHOOP Activity ID Mapping API
  slug: whoop-activity-id-mapping-api
- description: The Cycle API from WHOOP — 3 operation(s) for cycle.
  name: WHOOP Cycle API
  slug: whoop-cycle-api
- description: Endpoints for trusted WHOOP partner operations
  name: WHOOP Partner API
  slug: whoop-partner-api
- description: The Recovery API from WHOOP — 2 operation(s) for recovery.
  name: WHOOP Recovery API
  slug: whoop-recovery-api
- description: The Sleep API from WHOOP — 3 operation(s) for sleep.
  name: WHOOP Sleep API
  slug: whoop-sleep-api
- description: Endpoints for retrieving user profile and measurement data.
  name: WHOOP User API
  slug: whoop-user-api
- description: The Workout API from WHOOP — 2 operation(s) for workout.
  name: WHOOP Workout API
  slug: whoop-workout-api
artifact_total: 55
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whoop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whoop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whoop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/whoop-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.whoop.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.whoop.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/WhoopInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whoop
- group: company
  title: ''
  type: Blog
  url: https://engineering.prod.whoop.com
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.whoop.com/docs/developing/getting-started/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.whoop.com
- group: other
  title: ''
  type: X
  url: https://x.com/whoop
- group: commercial
  title: ''
  type: Plans
  url: plans/whoop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whoop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/whoop-finops.yml
created: '2026-06-13'
description: WHOOP is a fitness and recovery wearable platform providing a REST API for accessing sleep, recovery, strain, and workout metrics from the WHOOP band. The API uses OAuth 2.0 authorization code flow with Bearer tokens to allow developers to build applications that access member health and performance data including physiological cycles, sleep stages, recovery scores, strain, heart rate, body measurements, and workout records.
examples:
- key_count: 4
  name: Whoop Cycle Example
  slug: whoop-cycle-example
- key_count: 4
  name: Whoop Recovery Example
  slug: whoop-recovery-example
- key_count: 4
  name: Whoop Sleep Example
  slug: whoop-sleep-example
- key_count: 4
  name: Whoop User Profile Example
  slug: whoop-user-profile-example
- key_count: 4
  name: Whoop Workout Example
  slug: whoop-workout-example
finops:
- name: Whoop Finops
  service_category: ''
  slug: whoop-finops
graphqls:
- description: WHOOP is a fitness wearable tracking recovery, strain, and sleep. The API covers physiological metrics (HRV, resting heart rate, SpO2), recovery scores, sleep stages, workout strain, and cycle data fo
  name: WHOOP GraphQL API
  slug: whoop-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whoop.png
json_schemas:
- name: ActivityIdMappingResponse
  property_count: 1
  slug: whoop-activityidmappingresponse
- name: Appointment
  property_count: 2
  slug: whoop-appointment
- name: CreateObservationRequest
  property_count: 5
  slug: whoop-createobservationrequest
- name: Cycle
  property_count: 9
  slug: whoop-cycle
- name: CycleScore
  property_count: 4
  slug: whoop-cyclescore
- name: DiagnosticReportCreateRequest
  property_count: 2
  slug: whoop-diagnosticreportcreaterequest
- name: LabRequisition
  property_count: 6
  slug: whoop-labrequisition
- name: PaginatedCycleResponse
  property_count: 2
  slug: whoop-paginatedcycleresponse
- name: PaginatedSleepResponse
  property_count: 2
  slug: whoop-paginatedsleepresponse
- name: PartnerTokenRequest
  property_count: 4
  slug: whoop-partnertokenrequest
- name: PartnerTokenResponse
  property_count: 3
  slug: whoop-partnertokenresponse
- name: Patient
  property_count: 1
  slug: whoop-patient
- name: PatientCore
  property_count: 1
  slug: whoop-patientcore
- name: Recovery
  property_count: 7
  slug: whoop-recovery
- name: RecoveryCollection
  property_count: 2
  slug: whoop-recoverycollection
- name: RecoveryScore
  property_count: 6
  slug: whoop-recoveryscore
- name: ServiceRequest
  property_count: 6
  slug: whoop-servicerequest
- name: ServiceRequestStatusRequest
  property_count: 2
  slug: whoop-servicerequeststatusrequest
- name: Sleep
  property_count: 12
  slug: whoop-sleep
- name: SleepNeeded
  property_count: 4
  slug: whoop-sleepneeded
- name: SleepScore
  property_count: 6
  slug: whoop-sleepscore
- name: SleepStageSummary
  property_count: 8
  slug: whoop-sleepstagesummary
- name: SleepStreamDataPoint
  property_count: 7
  slug: whoop-sleepstreamdatapoint
- name: SleepStreamResponse
  property_count: 2
  slug: whoop-sleepstreamresponse
- name: UnilabsAppointment
  property_count: 4
  slug: whoop-unilabsappointment
- name: UnilabsCollectionAddress
  property_count: 5
  slug: whoop-unilabscollectionaddress
- name: UnilabsPatient
  property_count: 10
  slug: whoop-unilabspatient
- name: UserBasicProfile
  property_count: 4
  slug: whoop-userbasicprofile
- name: UserBodyMeasurement
  property_count: 3
  slug: whoop-userbodymeasurement
- name: WorkoutCollection
  property_count: 2
  slug: whoop-workoutcollection
- name: WorkoutScore
  property_count: 9
  slug: whoop-workoutscore
- name: WorkoutV2
  property_count: 12
  slug: whoop-workoutv2
- name: ZoneDurations
  property_count: 6
  slug: whoop-zonedurations
jsonld:
- class_count: 2
  name: Whoop Context
  property_count: 16
  slug: whoop-context
layout: provider
modified: '2026-06-13'
name: WHOOP
nav: Providers
network: true
overview: 'WHOOP publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Activity ID Mapping API, Cycle API, Partner API, and 4 more. Tagged areas include Fitness, Wearables, Health, Recovery, and Sleep.


  The WHOOP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WHOOP''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Whoop Plans Pricing
  plan_count: 1
  slug: whoop-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 2
  name: Whoop Rate Limits
  slug: whoop-rate-limits
rules:
- name: WHOOP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: whoop-jsonschema-spectral-rules
scopes:
- name: Whoop Scopes
  scope_count: 7
  slug: whoop-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.6
  delta: -5.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/whoop/refs/heads/main/screenshots/whoop-2026-06-20T201453.png
security:
- kind: authentication
  name: Whoop Authentication
  slug: whoop-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Whoop Domain Security
  slug: whoop-domain-security
  summary_line: TLSv1.3 · DMARC
slug: whoop
tags:
- Fitness
- Wearables
- Health
- Recovery
- Sleep
- Workout
- Strain
- Heart Rate
- Performance
website: https://www.whoop.com
---
