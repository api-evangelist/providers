---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Amplitude Agentic Access
  operation_count: 73
  slug: amplitude-agentic-access
  summary_line: 73 operations · 35 acting
api_count: 10
apis:
- description: The Amplitude Batch Event Upload API is optimized for high-volume server-side event ingestion. It accepts batches of events up to 20MB per request and is designed for use cases where data volume may e
  name: Amplitude Batch Event Upload API
  slug: batch-event-upload-api
- description: The Amplitude Group Identify API allows developers to set or update properties on groups within Amplitude. Groups are entities such as companies, teams, or accounts that users belong to. This API enab
  name: Amplitude Group Identify API
  slug: group-identify-api
- description: The Amplitude Releases API allows developers to programmatically track software releases and deployments in Amplitude. By recording release events, teams can correlate product changes with analytics m
  name: Amplitude Releases API
  slug: releases-api
- description: 'The Amplitude Session Replay API enables developers to upload and manage session replay data for playback within Amplitude. Session replays provide qualitative insights by recording user interactions '
  name: Amplitude Session Replay API
  slug: session-replay-api
- description: The Amplitude User Privacy API provides endpoints for managing user data in compliance with privacy regulations such as GDPR and CCPA. It supports requesting the deletion or suppression of user data b
  name: Amplitude User Privacy API
  slug: user-privacy-api
- description: The Webhooks Streaming destination forwards Amplitude event and user payloads to a customer-configured HTTPS endpoint, and the Cohort Sync family of destinations pushes cohort membership changes to do
  name: Amplitude Webhooks and Cohort Sync
  slug: webhooks-cohort-sync
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Chart annotation management operations
  name: Amplitude Annotations API
  slug: amplitude-annotations-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Cohort management and export operations
  name: Amplitude Cohorts API
  slug: amplitude-cohorts-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Data subject access request operations
  name: Amplitude Data Access API
  slug: amplitude-data-access-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: User data deletion request operations
  name: Amplitude Data Deletion API
  slug: amplitude-data-deletion-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Deployment management operations
  name: Amplitude Deployments API
  slug: amplitude-deployments-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Remote flag and experiment evaluation operations
  name: Amplitude Evaluation API
  slug: amplitude-evaluation-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Operations for managing event categories
  name: Amplitude Event Categories API
  slug: amplitude-event-categories-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Event listing operations
  name: Amplitude Event List API
  slug: amplitude-event-list-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Operations for managing event properties
  name: Amplitude Event Properties API
  slug: amplitude-event-properties-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Event segmentation analysis operations
  name: Amplitude Event Segmentation API
  slug: amplitude-event-segmentation-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Operations for managing event types
  name: Amplitude Event Types API
  slug: amplitude-event-types-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Event ingestion operations
  name: Amplitude Events API
  slug: amplitude-events-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Experiment management operations
  name: Amplitude Experiments API
  slug: amplitude-experiments-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Flag configuration retrieval for local evaluation
  name: Amplitude Flags API
  slug: amplitude-flags-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Funnel analysis operations
  name: Amplitude Funnel Analysis API
  slug: amplitude-funnel-analysis-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: SCIM group management operations
  name: Amplitude Groups API
  slug: amplitude-groups-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: User profile retrieval operations
  name: Amplitude Profiles API
  slug: amplitude-profiles-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Retention analysis operations
  name: Amplitude Retention Analysis API
  slug: amplitude-retention-analysis-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Revenue analysis operations
  name: Amplitude Revenue Analysis API
  slug: amplitude-revenue-analysis-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: User activity lookup operations
  name: Amplitude User Activity API
  slug: amplitude-user-activity-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Operations for managing user properties
  name: Amplitude User Properties API
  slug: amplitude-user-properties-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: SCIM user provisioning operations
  name: Amplitude Users API
  slug: amplitude-users-api
- baseURL: https://api2.amplitude.com
  baseurl_source: declared
  description: Flag and experiment version history operations
  name: Amplitude Versions API
  slug: amplitude-versions-api
arazzos:
- description: Create a chart annotation, read it back, update its details, and confirm it in the annotation list.
  name: Amplitude Chart Annotation Lifecycle
  slug: amplitude-annotation-lifecycle-workflow
- description: Request an asynchronous cohort export, poll until it is ready, then download the membership file.
  name: Amplitude Behavioral Cohort Export
  slug: amplitude-cohort-export-workflow
- description: Upload an externally-sourced cohort of user IDs into Amplitude and confirm it appears in the cohort list.
  name: Amplitude Cohort Upload and Verify
  slug: amplitude-cohort-upload-verify-workflow
- description: Submit a data subject access request, poll its status until complete, and capture the download URL.
  name: Amplitude DSAR Request and Poll
  slug: amplitude-dsar-request-workflow
- description: Create an event property on an event type, read it back, update its metadata, and list all properties for the event.
  name: Amplitude Event Property Lifecycle
  slug: amplitude-event-property-lifecycle-workflow
- description: Create an A/B experiment, read it back, start it by enabling, and confirm it in the experiment list.
  name: Amplitude Experiment Lifecycle
  slug: amplitude-experiment-lifecycle-workflow
- description: Create a feature flag, read it back, enable it, and confirm it appears in the flag list.
  name: Amplitude Feature Flag Rollout
  slug: amplitude-flag-rollout-workflow
- description: Set user properties on an account, alias an anonymous identity into it, then read the merged profile back.
  name: Amplitude Identity Merge and Verify
  slug: amplitude-identity-merge-workflow
- description: Upload a batch of events through the HTTP V2 API, then query event segmentation to verify the metric.
  name: Amplitude Ingest Events and Segment
  slug: amplitude-ingest-and-segment-workflow
- description: Provision a SCIM user, read the account back, then deactivate it via a SCIM patch.
  name: Amplitude SCIM User Provisioning
  slug: amplitude-scim-user-provisioning-workflow
- description: Plan a tracking event end to end by creating its category, the event type, and an event property, then reading the event back.
  name: Amplitude Taxonomy Event Governance
  slug: amplitude-taxonomy-event-governance-workflow
- description: Search for a user, pull their recent activity, and retrieve their enriched profile with recommendations.
  name: Amplitude User 360 Lookup
  slug: amplitude-user-360-lookup-workflow
- description: Download flag configurations for local evaluation, then remotely evaluate variant assignments for a user.
  name: Amplitude Variant Evaluation
  slug: amplitude-variant-evaluation-workflow
artifact_total: 535
asyncapis:
- description: 'AsyncAPI description of two outbound, push-style surfaces offered by Amplitude''s Data destination catalog: 1. Webhooks Streaming destination - a generic event/user forwarding destination that delivers'
  name: Amplitude Webhooks and Cohort Sync
  slug: amplitude-webhooks-cohort-sync-asyncapi
collections:
- collection_type: postman
  name: Amplitude Attribution API
  slug: postman-amplitude-attribution-api
- collection_type: postman
  name: Amplitude Behavioral Cohorts API
  slug: postman-amplitude-behavioral-cohorts-api
- collection_type: postman
  name: Amplitude Chart Annotations API
  slug: postman-amplitude-chart-annotations-api
- collection_type: postman
  name: Amplitude Dashboard REST API
  slug: postman-amplitude-dashboard-rest-api
- collection_type: postman
  name: Amplitude Data Subject Access Request API
  slug: postman-amplitude-dsar-api
- collection_type: postman
  name: Amplitude Experiment Evaluation API
  slug: postman-amplitude-experiment-evaluation-api
- collection_type: postman
  name: Amplitude Experiment Management API
  slug: postman-amplitude-experiment-management-api
- collection_type: postman
  name: Amplitude Export API
  slug: postman-amplitude-export-api
- collection_type: postman
  name: Amplitude HTTP V2 API
  slug: postman-amplitude-http-v2-api
- collection_type: postman
  name: Amplitude Identify API
  slug: postman-amplitude-identify-api
- collection_type: postman
  name: Amplitude SCIM API
  slug: postman-amplitude-scim-api
- collection_type: postman
  name: Amplitude Taxonomy API
  slug: postman-amplitude-taxonomy-api
- collection_type: postman
  name: Amplitude User Mapping API
  slug: postman-amplitude-user-mapping-api
- collection_type: postman
  name: Amplitude User Profile API
  slug: postman-amplitude-user-profile-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amplitude Attribution Annotations API
  slug: open-amplitude-annotations-api
- collection_type: open
  name: Amplitude Annotations Attribution API
  slug: open-amplitude-attribution-api
- collection_type: open
  name: Amplitude Behavioral Cohorts API
  slug: open-amplitude-behavioral-cohorts-api
- collection_type: open
  name: Amplitude Chart Annotations API
  slug: open-amplitude-chart-annotations-api
- collection_type: open
  name: Amplitude Attribution Annotations Cohorts API
  slug: open-amplitude-cohorts-api
- collection_type: open
  name: Amplitude Dashboard REST API
  slug: open-amplitude-dashboard-rest-api
- collection_type: open
  name: Amplitude Attribution Annotations Data Access API
  slug: open-amplitude-data-access-api
- collection_type: open
  name: Amplitude Attribution Annotations Data Deletion API
  slug: open-amplitude-data-deletion-api
- collection_type: open
  name: Amplitude Attribution Annotations Deployments API
  slug: open-amplitude-deployments-api
- collection_type: open
  name: Amplitude Data Subject Access Request API
  slug: open-amplitude-dsar-api
- collection_type: open
  name: Amplitude Attribution Annotations Evaluation API
  slug: open-amplitude-evaluation-api
- collection_type: open
  name: Amplitude Attribution Annotations Event Categories API
  slug: open-amplitude-event-categories-api
- collection_type: open
  name: Amplitude Attribution Annotations Event List API
  slug: open-amplitude-event-list-api
- collection_type: open
  name: Amplitude Attribution Annotations Event Properties API
  slug: open-amplitude-event-properties-api
- collection_type: open
  name: Amplitude Attribution Annotations Event Segmentation API
  slug: open-amplitude-event-segmentation-api
- collection_type: open
  name: Amplitude Attribution Annotations Event Types API
  slug: open-amplitude-event-types-api
- collection_type: open
  name: Amplitude Attribution Annotations Events API
  slug: open-amplitude-events-api
- collection_type: open
  name: Amplitude Experiment Evaluation API
  slug: open-amplitude-experiment-evaluation-api
- collection_type: open
  name: Amplitude Experiment Management API
  slug: open-amplitude-experiment-management-api
- collection_type: open
  name: Amplitude Attribution Annotations Experiments API
  slug: open-amplitude-experiments-api
- collection_type: open
  name: Amplitude Attribution Annotations Export API
  slug: open-amplitude-export-api
- collection_type: open
  name: Amplitude Attribution Annotations Flags API
  slug: open-amplitude-flags-api
- collection_type: open
  name: Amplitude Attribution Annotations Funnel Analysis API
  slug: open-amplitude-funnel-analysis-api
- collection_type: open
  name: Amplitude Attribution Annotations Groups API
  slug: open-amplitude-groups-api
- collection_type: open
  name: Amplitude HTTP V2 API
  slug: open-amplitude-http-v2-api
- collection_type: open
  name: Amplitude Attribution Annotations Identify API
  slug: open-amplitude-identify-api
- collection_type: open
  name: Amplitude Attribution Annotations Profiles API
  slug: open-amplitude-profiles-api
- collection_type: open
  name: Amplitude Attribution Annotations Retention Analysis API
  slug: open-amplitude-retention-analysis-api
- collection_type: open
  name: Amplitude Attribution Annotations Revenue Analysis API
  slug: open-amplitude-revenue-analysis-api
- collection_type: open
  name: Amplitude SCIM API
  slug: open-amplitude-scim-api
- collection_type: open
  name: Amplitude Taxonomy API
  slug: open-amplitude-taxonomy-api
- collection_type: open
  name: Amplitude Attribution Annotations User Activity API
  slug: open-amplitude-user-activity-api
- collection_type: open
  name: Amplitude Attribution Annotations User Mapping API
  slug: open-amplitude-user-mapping-api
- collection_type: open
  name: Amplitude User Profile API
  slug: open-amplitude-user-profile-api
- collection_type: open
  name: Amplitude Attribution Annotations User Properties API
  slug: open-amplitude-user-properties-api
- collection_type: open
  name: Amplitude Attribution Annotations Users API
  slug: open-amplitude-users-api
- collection_type: open
  name: Amplitude Attribution Annotations Versions API
  slug: open-amplitude-versions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amplitude-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amplitude-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amplitude-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amplitude-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amplitude-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amplitude/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-annotation-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-cohort-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-cohort-upload-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-dsar-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-event-property-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-experiment-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-flag-rollout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-identity-merge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-ingest-and-segment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-scim-user-provisioning-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-taxonomy-event-governance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-user-360-lookup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amplitude-variant-evaluation-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amplitude-analytics
- group: start
  title: ''
  type: Portal
  url: https://amplitude.com
- group: docs
  title: ''
  type: Documentation
  url: https://amplitude.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://amplitude.com/docs/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://amplitude.com/docs/apis/authentication
- group: build
  title: ''
  type: SDKs
  url: https://amplitude.com/docs/sdks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amplitude
- group: company
  title: ''
  type: Blog
  url: https://amplitude.com/blog
- group: learn
  title: ''
  type: Academy
  url: https://academy.amplitude.com
- group: operate
  title: ''
  type: Support
  url: https://help.amplitude.com
- group: commercial
  title: ''
  type: Pricing
  url: https://amplitude.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.amplitude.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amplitude.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amplitude.com/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amplitude-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amplitude-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amplitude-cohort-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amplitude-experiment-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amplitude-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amplitude-vocabulary.yaml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/behavioral-cohorts-api-cohort-request-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/dashboard-rest-api-user-search-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/scim-api-scim-group-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/http-v2-api-event-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/experiment-evaluation-api-flag-configuration-structure.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/amplitude/mcp-marketplace
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/amplitude/builder-skills
description: Amplitude is a digital analytics platform that helps product teams understand user behavior, run experiments, and drive growth. It provides a suite of APIs for event ingestion, user management, cohort syncing, taxonomy governance, A/B testing, and data export. Amplitude is widely used by product, data, and engineering teams to build better digital experiences through data-driven insights.
examples:
- key_count: 9
  name: Amplitude Cohort Example
  slug: amplitude-cohort-example
- key_count: 6
  name: Amplitude Createannotation Example
  slug: amplitude-createannotation-example
- key_count: 6
  name: Amplitude Createdeletionrequest Example
  slug: amplitude-createdeletionrequest-example
- key_count: 6
  name: Amplitude Createdsarrequest Example
  slug: amplitude-createdsarrequest-example
- key_count: 6
  name: Amplitude Createeventcategory Example
  slug: amplitude-createeventcategory-example
- key_count: 6
  name: Amplitude Createeventproperty Example
  slug: amplitude-createeventproperty-example
- key_count: 6
  name: Amplitude Createeventtype Example
  slug: amplitude-createeventtype-example
- key_count: 6
  name: Amplitude Createexperiment Example
  slug: amplitude-createexperiment-example
- key_count: 6
  name: Amplitude Createflag Example
  slug: amplitude-createflag-example
- key_count: 6
  name: Amplitude Createuserproperty Example
  slug: amplitude-createuserproperty-example
- key_count: 6
  name: Amplitude Deleteeventcategory Example
  slug: amplitude-deleteeventcategory-example
- key_count: 6
  name: Amplitude Deleteeventproperty Example
  slug: amplitude-deleteeventproperty-example
- key_count: 6
  name: Amplitude Deleteeventtype Example
  slug: amplitude-deleteeventtype-example
- key_count: 6
  name: Amplitude Deleteuserproperty Example
  slug: amplitude-deleteuserproperty-example
- key_count: 6
  name: Amplitude Downloadcohortexport Example
  slug: amplitude-downloadcohortexport-example
- key_count: 6
  name: Amplitude Evaluatevariants Example
  slug: amplitude-evaluatevariants-example
- key_count: 6
  name: Amplitude Evaluatevariantsget Example
  slug: amplitude-evaluatevariantsget-example
- key_count: 36
  name: Amplitude Event Example
  slug: amplitude-event-example
- key_count: 17
  name: Amplitude Experiment Example
  slug: amplitude-experiment-example
- key_count: 6
  name: Amplitude Getannotation Example
  slug: amplitude-getannotation-example
- key_count: 6
  name: Amplitude Getcohortexportstatus Example
  slug: amplitude-getcohortexportstatus-example
- key_count: 6
  name: Amplitude Getdeployment Example
  slug: amplitude-getdeployment-example
- key_count: 6
  name: Amplitude Getdsarrequeststatus Example
  slug: amplitude-getdsarrequeststatus-example
- key_count: 6
  name: Amplitude Geteventcategory Example
  slug: amplitude-geteventcategory-example
- key_count: 6
  name: Amplitude Geteventproperty Example
  slug: amplitude-geteventproperty-example
- key_count: 6
  name: Amplitude Geteventsegmentation Example
  slug: amplitude-geteventsegmentation-example
- key_count: 6
  name: Amplitude Geteventtype Example
  slug: amplitude-geteventtype-example
- key_count: 6
  name: Amplitude Getexperiment Example
  slug: amplitude-getexperiment-example
- key_count: 6
  name: Amplitude Getflag Example
  slug: amplitude-getflag-example
- key_count: 6
  name: Amplitude Getflags Example
  slug: amplitude-getflags-example
- key_count: 6
  name: Amplitude Getfunnelanalysis Example
  slug: amplitude-getfunnelanalysis-example
- key_count: 6
  name: Amplitude Getretentionanalysis Example
  slug: amplitude-getretentionanalysis-example
- key_count: 6
  name: Amplitude Getrevenueltv Example
  slug: amplitude-getrevenueltv-example
- key_count: 6
  name: Amplitude Getuseractivity Example
  slug: amplitude-getuseractivity-example
- key_count: 6
  name: Amplitude Getuserprofile Example
  slug: amplitude-getuserprofile-example
- key_count: 6
  name: Amplitude Getuserproperty Example
  slug: amplitude-getuserproperty-example
- key_count: 6
  name: Amplitude Identifyuser Example
  slug: amplitude-identifyuser-example
- key_count: 6
  name: Amplitude Listannotations Example
  slug: amplitude-listannotations-example
- key_count: 6
  name: Amplitude Listcohorts Example
  slug: amplitude-listcohorts-example
- key_count: 6
  name: Amplitude Listdeletionrequests Example
  slug: amplitude-listdeletionrequests-example
- key_count: 6
  name: Amplitude Listdeployments Example
  slug: amplitude-listdeployments-example
- key_count: 6
  name: Amplitude Listeventcategories Example
  slug: amplitude-listeventcategories-example
- key_count: 6
  name: Amplitude Listeventproperties Example
  slug: amplitude-listeventproperties-example
- key_count: 6
  name: Amplitude Listeventtypes Example
  slug: amplitude-listeventtypes-example
- key_count: 6
  name: Amplitude Listexperiments Example
  slug: amplitude-listexperiments-example
- key_count: 6
  name: Amplitude Listflags Example
  slug: amplitude-listflags-example
- key_count: 6
  name: Amplitude Listuserproperties Example
  slug: amplitude-listuserproperties-example
- key_count: 6
  name: Amplitude Listversions Example
  slug: amplitude-listversions-example
- key_count: 6
  name: Amplitude Mapuser Example
  slug: amplitude-mapuser-example
- key_count: 6
  name: Amplitude Requestcohortexport Example
  slug: amplitude-requestcohortexport-example
- key_count: 6
  name: Amplitude Searchusers Example
  slug: amplitude-searchusers-example
- key_count: 6
  name: Amplitude Sendattribution Example
  slug: amplitude-sendattribution-example
- key_count: 6
  name: Amplitude Unmapuser Example
  slug: amplitude-unmapuser-example
- key_count: 6
  name: Amplitude Updateannotation Example
  slug: amplitude-updateannotation-example
- key_count: 6
  name: Amplitude Updateeventcategory Example
  slug: amplitude-updateeventcategory-example
- key_count: 6
  name: Amplitude Updateeventproperty Example
  slug: amplitude-updateeventproperty-example
- key_count: 6
  name: Amplitude Updateeventtype Example
  slug: amplitude-updateeventtype-example
- key_count: 6
  name: Amplitude Updateexperiment Example
  slug: amplitude-updateexperiment-example
- key_count: 6
  name: Amplitude Updateflag Example
  slug: amplitude-updateflag-example
- key_count: 6
  name: Amplitude Updateuserproperty Example
  slug: amplitude-updateuserproperty-example
- key_count: 6
  name: Amplitude Uploadcohort Example
  slug: amplitude-uploadcohort-example
- key_count: 6
  name: Amplitude Uploadevents Example
  slug: amplitude-uploadevents-example
- key_count: 20
  name: Attribution Api Attribution Event Example
  slug: attribution-api-attribution-event-example
- key_count: 2
  name: Attribution Api Attribution Request Example
  slug: attribution-api-attribution-request-example
- key_count: 3
  name: Attribution Api Attribution Response Example
  slug: attribution-api-attribution-response-example
- key_count: 8
  name: Behavioral Cohorts Api Cohort Example
  slug: behavioral-cohorts-api-cohort-example
- key_count: 1
  name: Behavioral Cohorts Api Cohort List Response Example
  slug: behavioral-cohorts-api-cohort-list-response-example
- key_count: 2
  name: Behavioral Cohorts Api Cohort Request Response Example
  slug: behavioral-cohorts-api-cohort-request-response-example
- key_count: 2
  name: Behavioral Cohorts Api Cohort Status Response Example
  slug: behavioral-cohorts-api-cohort-status-response-example
- key_count: 4
  name: Behavioral Cohorts Api Cohort Upload Request Example
  slug: behavioral-cohorts-api-cohort-upload-request-example
- key_count: 1
  name: Behavioral Cohorts Api Cohort Upload Response Example
  slug: behavioral-cohorts-api-cohort-upload-response-example
- key_count: 9
  name: Chart Annotations Api Annotation Example
  slug: chart-annotations-api-annotation-example
- key_count: 1
  name: Chart Annotations Api Annotation List Response Example
  slug: chart-annotations-api-annotation-list-response-example
- key_count: 6
  name: Chart Annotations Api Create Annotation Request Example
  slug: chart-annotations-api-create-annotation-request-example
- key_count: 6
  name: Chart Annotations Api Update Annotation Request Example
  slug: chart-annotations-api-update-annotation-request-example
- key_count: 1
  name: Dashboard Rest Api Event List Result Example
  slug: dashboard-rest-api-event-list-result-example
- key_count: 1
  name: Dashboard Rest Api Funnel Result Example
  slug: dashboard-rest-api-funnel-result-example
- key_count: 1
  name: Dashboard Rest Api Retention Result Example
  slug: dashboard-rest-api-retention-result-example
- key_count: 1
  name: Dashboard Rest Api Segmentation Result Example
  slug: dashboard-rest-api-segmentation-result-example
- key_count: 2
  name: Dashboard Rest Api User Activity Result Example
  slug: dashboard-rest-api-user-activity-result-example
- key_count: 1
  name: Dashboard Rest Api User Search Result Example
  slug: dashboard-rest-api-user-search-result-example
- key_count: 1
  name: Dsar Api Deletion List Response Example
  slug: dsar-api-deletion-list-response-example
- key_count: 3
  name: Dsar Api Deletion Request Example
  slug: dsar-api-deletion-request-example
- key_count: 2
  name: Dsar Api Deletion Response Example
  slug: dsar-api-deletion-response-example
- key_count: 1
  name: Dsar Api Dsar Request Example
  slug: dsar-api-dsar-request-example
- key_count: 2
  name: Dsar Api Dsar Response Example
  slug: dsar-api-dsar-response-example
- key_count: 3
  name: Dsar Api Dsar Status Response Example
  slug: dsar-api-dsar-status-response-example
- key_count: 5
  name: Experiment Evaluation Api Evaluation Request Example
  slug: experiment-evaluation-api-evaluation-request-example
- key_count: 0
  name: Experiment Evaluation Api Evaluation Response Example
  slug: experiment-evaluation-api-evaluation-response-example
- key_count: 4
  name: Experiment Evaluation Api Flag Configuration Example
  slug: experiment-evaluation-api-flag-configuration-example
- key_count: 4
  name: Experiment Evaluation Api Variant Example
  slug: experiment-evaluation-api-variant-example
- key_count: 5
  name: Experiment Management Api Create Experiment Request Example
  slug: experiment-management-api-create-experiment-request-example
- key_count: 5
  name: Experiment Management Api Create Flag Request Example
  slug: experiment-management-api-create-flag-request-example
- key_count: 5
  name: Experiment Management Api Deployment Example
  slug: experiment-management-api-deployment-example
- key_count: 1
  name: Experiment Management Api Deployment List Response Example
  slug: experiment-management-api-deployment-list-response-example
- key_count: 16
  name: Experiment Management Api Experiment Example
  slug: experiment-management-api-experiment-example
- key_count: 2
  name: Experiment Management Api Experiment List Response Example
  slug: experiment-management-api-experiment-list-response-example
- key_count: 13
  name: Experiment Management Api Flag Example
  slug: experiment-management-api-flag-example
- key_count: 2
  name: Experiment Management Api Flag List Response Example
  slug: experiment-management-api-flag-list-response-example
- key_count: 4
  name: Experiment Management Api Segment Example
  slug: experiment-management-api-segment-example
- key_count: 5
  name: Experiment Management Api Update Experiment Request Example
  slug: experiment-management-api-update-experiment-request-example
- key_count: 5
  name: Experiment Management Api Update Flag Request Example
  slug: experiment-management-api-update-flag-request-example
- key_count: 5
  name: Experiment Management Api Variant Config Example
  slug: experiment-management-api-variant-config-example
- key_count: 2
  name: Experiment Management Api Version List Response Example
  slug: experiment-management-api-version-list-response-example
- key_count: 36
  name: Http V2 Api Event Example
  slug: http-v2-api-event-example
- key_count: 1
  name: Http V2 Api Upload Options Example
  slug: http-v2-api-upload-options-example
- key_count: 3
  name: Http V2 Api Upload Request Body Example
  slug: http-v2-api-upload-request-body-example
- key_count: 4
  name: Http V2 Api Upload Response Example
  slug: http-v2-api-upload-response-example
- key_count: 3
  name: Identify Api Identification Example
  slug: identify-api-identification-example
- key_count: 2
  name: Identify Api Identify Request Body Example
  slug: identify-api-identify-request-body-example
- key_count: 2
  name: Identify Api Identify Request Form Example
  slug: identify-api-identify-request-form-example
- key_count: 3
  name: Identify Api Identify Response Example
  slug: identify-api-identify-response-example
- key_count: 7
  name: Identify Api User Property Operations Example
  slug: identify-api-user-property-operations-example
- key_count: 5
  name: Scim Api Scim Group Example
  slug: scim-api-scim-group-example
- key_count: 3
  name: Scim Api Scim Group List Response Example
  slug: scim-api-scim-group-list-response-example
- key_count: 3
  name: Scim Api Scim Group Request Example
  slug: scim-api-scim-group-request-example
- key_count: 2
  name: Scim Api Scim Patch Request Example
  slug: scim-api-scim-patch-request-example
- key_count: 8
  name: Scim Api Scim User Example
  slug: scim-api-scim-user-example
- key_count: 5
  name: Scim Api Scim User List Response Example
  slug: scim-api-scim-user-list-response-example
- key_count: 5
  name: Scim Api Scim User Request Example
  slug: scim-api-scim-user-request-example
- key_count: 2
  name: Taxonomy Api Category Example
  slug: taxonomy-api-category-example
- key_count: 1
  name: Taxonomy Api Category List Response Example
  slug: taxonomy-api-category-list-response-example
- key_count: 5
  name: Taxonomy Api Event Property Example
  slug: taxonomy-api-event-property-example
- key_count: 1
  name: Taxonomy Api Event Property List Response Example
  slug: taxonomy-api-event-property-list-response-example
- key_count: 3
  name: Taxonomy Api Event Type Example
  slug: taxonomy-api-event-type-example
- key_count: 1
  name: Taxonomy Api Event Type List Response Example
  slug: taxonomy-api-event-type-list-response-example
- key_count: 1
  name: Taxonomy Api Success Response Example
  slug: taxonomy-api-success-response-example
- key_count: 3
  name: Taxonomy Api User Property Example
  slug: taxonomy-api-user-property-example
- key_count: 1
  name: Taxonomy Api User Property List Response Example
  slug: taxonomy-api-user-property-list-response-example
- key_count: 1
  name: User Mapping Api User Map Request Example
  slug: user-mapping-api-user-map-request-example
- key_count: 2
  name: User Mapping Api User Map Response Example
  slug: user-mapping-api-user-map-response-example
- key_count: 3
  name: User Mapping Api User Mapping Example
  slug: user-mapping-api-user-mapping-example
- key_count: 1
  name: User Mapping Api User Unmap Request Example
  slug: user-mapping-api-user-unmap-request-example
- key_count: 5
  name: User Profile Api Recommendation Example
  slug: user-profile-api-recommendation-example
- key_count: 6
  name: User Profile Api User Data Example
  slug: user-profile-api-user-data-example
- key_count: 1
  name: User Profile Api User Profile Response Example
  slug: user-profile-api-user-profile-response-example
features:
- 'Starter: 10K MTUs or 2M events free, unlimited sources'
- 'Plus from $49/mo: 300K MTUs or 25M events, behavioral cohorts'
- 'Growth custom: advanced analysis, Feature Experimentation'
- 'Enterprise custom: cross-product, multi-armed bandit experiments'
- 'HTTP V2 ingest: 10 events/sec per device/user_id'
- 'Batch ingest: 2,000 events per request'
- 'Dashboard REST: 360 queries/hr'
- Webhooks via destinations and Cohort Sync
- OAuth + API keys per project
- Session Replay across web/mobile
- Web Experimentation and Feature Experimentation
- AI Feedback for natural-language analysis
- Predictive audiences (Growth+)
- Causal insights
- Mutual exclusion groups for A/B test scaling
- Cross-product analysis on Enterprise
finops:
- name: Amplitude Finops
  service_category: Product Analytics
  slug: amplitude-finops
graphqls:
- description: Amplitude does not expose a native public GraphQL endpoint. This schema is a conceptual GraphQL representation of the Amplitude analytics platform data model, derived from the full surface area of Amp
  name: Amplitude GraphQL
  slug: amplitude-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amplitude.png
json_schemas:
- name: Annotation
  property_count: 9
  slug: amplitude-annotation
- name: AnnotationListResponse
  property_count: 1
  slug: amplitude-annotationlistresponse
- name: AttributionEvent
  property_count: 20
  slug: amplitude-attributionevent
- name: AttributionRequest
  property_count: 2
  slug: amplitude-attributionrequest
- name: AttributionResponse
  property_count: 3
  slug: amplitude-attributionresponse
- name: Category
  property_count: 2
  slug: amplitude-category
- name: CategoryListResponse
  property_count: 1
  slug: amplitude-categorylistresponse
- name: Amplitude Cohort
  property_count: 9
  slug: amplitude-cohort
- name: CohortListResponse
  property_count: 1
  slug: amplitude-cohortlistresponse
- name: CohortRequestResponse
  property_count: 2
  slug: amplitude-cohortrequestresponse
- name: CohortStatusResponse
  property_count: 2
  slug: amplitude-cohortstatusresponse
- name: CohortUploadRequest
  property_count: 4
  slug: amplitude-cohortuploadrequest
- name: CohortUploadResponse
  property_count: 1
  slug: amplitude-cohortuploadresponse
- name: CreateAnnotationRequest
  property_count: 6
  slug: amplitude-createannotationrequest
- name: CreateExperimentRequest
  property_count: 5
  slug: amplitude-createexperimentrequest
- name: CreateFlagRequest
  property_count: 5
  slug: amplitude-createflagrequest
- name: DeletionListResponse
  property_count: 1
  slug: amplitude-deletionlistresponse
- name: DeletionRequest
  property_count: 3
  slug: amplitude-deletionrequest
- name: DeletionResponse
  property_count: 2
  slug: amplitude-deletionresponse
- name: Deployment
  property_count: 5
  slug: amplitude-deployment
- name: DeploymentListResponse
  property_count: 1
  slug: amplitude-deploymentlistresponse
- name: DsarRequest
  property_count: 1
  slug: amplitude-dsarrequest
- name: DsarResponse
  property_count: 2
  slug: amplitude-dsarresponse
- name: DsarStatusResponse
  property_count: 3
  slug: amplitude-dsarstatusresponse
- name: ErrorResponse
  property_count: 5
  slug: amplitude-errorresponse
- name: EvaluationRequest
  property_count: 5
  slug: amplitude-evaluationrequest
- name: EvaluationResponse
  property_count: 0
  slug: amplitude-evaluationresponse
- name: Amplitude Event
  property_count: 36
  slug: amplitude-event
- name: EventListResult
  property_count: 1
  slug: amplitude-eventlistresult
- name: EventProperty
  property_count: 5
  slug: amplitude-eventproperty
- name: EventPropertyListResponse
  property_count: 1
  slug: amplitude-eventpropertylistresponse
- name: EventType
  property_count: 3
  slug: amplitude-eventtype
- name: EventTypeListResponse
  property_count: 1
  slug: amplitude-eventtypelistresponse
- name: Amplitude Experiment
  property_count: 17
  slug: amplitude-experiment
- name: ExperimentListResponse
  property_count: 2
  slug: amplitude-experimentlistresponse
- name: Flag
  property_count: 13
  slug: amplitude-flag
- name: FlagConfiguration
  property_count: 4
  slug: amplitude-flagconfiguration
- name: FlagListResponse
  property_count: 2
  slug: amplitude-flaglistresponse
- name: FunnelResult
  property_count: 1
  slug: amplitude-funnelresult
- name: Identification
  property_count: 3
  slug: amplitude-identification
- name: IdentifyRequestBody
  property_count: 2
  slug: amplitude-identifyrequestbody
- name: IdentifyRequestForm
  property_count: 2
  slug: amplitude-identifyrequestform
- name: IdentifyResponse
  property_count: 3
  slug: amplitude-identifyresponse
- name: Recommendation
  property_count: 5
  slug: amplitude-recommendation
- name: RetentionResult
  property_count: 1
  slug: amplitude-retentionresult
- name: ScimGroup
  property_count: 5
  slug: amplitude-scimgroup
- name: ScimGroupListResponse
  property_count: 3
  slug: amplitude-scimgrouplistresponse
- name: ScimGroupRequest
  property_count: 3
  slug: amplitude-scimgrouprequest
- name: ScimPatchRequest
  property_count: 2
  slug: amplitude-scimpatchrequest
- name: ScimUser
  property_count: 8
  slug: amplitude-scimuser
- name: ScimUserListResponse
  property_count: 5
  slug: amplitude-scimuserlistresponse
- name: ScimUserRequest
  property_count: 5
  slug: amplitude-scimuserrequest
- name: Segment
  property_count: 4
  slug: amplitude-segment
- name: SegmentationResult
  property_count: 1
  slug: amplitude-segmentationresult
- name: SuccessResponse
  property_count: 1
  slug: amplitude-successresponse
- name: UpdateAnnotationRequest
  property_count: 6
  slug: amplitude-updateannotationrequest
- name: UpdateExperimentRequest
  property_count: 5
  slug: amplitude-updateexperimentrequest
- name: UpdateFlagRequest
  property_count: 5
  slug: amplitude-updateflagrequest
- name: UploadOptions
  property_count: 1
  slug: amplitude-uploadoptions
- name: UploadRequestBody
  property_count: 3
  slug: amplitude-uploadrequestbody
- name: UploadResponse
  property_count: 4
  slug: amplitude-uploadresponse
- name: UserActivityResult
  property_count: 2
  slug: amplitude-useractivityresult
- name: UserData
  property_count: 6
  slug: amplitude-userdata
- name: UserMapping
  property_count: 3
  slug: amplitude-usermapping
- name: UserMapRequest
  property_count: 1
  slug: amplitude-usermaprequest
- name: UserMapResponse
  property_count: 2
  slug: amplitude-usermapresponse
- name: UserProfileResponse
  property_count: 1
  slug: amplitude-userprofileresponse
- name: UserProperty
  property_count: 3
  slug: amplitude-userproperty
- name: UserPropertyListResponse
  property_count: 1
  slug: amplitude-userpropertylistresponse
- name: UserPropertyOperations
  property_count: 7
  slug: amplitude-userpropertyoperations
- name: UserSearchResult
  property_count: 1
  slug: amplitude-usersearchresult
- name: UserUnmapRequest
  property_count: 1
  slug: amplitude-userunmaprequest
- name: Variant
  property_count: 4
  slug: amplitude-variant
- name: VariantConfig
  property_count: 5
  slug: amplitude-variantconfig
- name: VersionListResponse
  property_count: 2
  slug: amplitude-versionlistresponse
- name: AttributionEvent
  property_count: 20
  slug: attribution-api-attribution-event
- name: AttributionRequest
  property_count: 2
  slug: attribution-api-attribution-request
- name: AttributionResponse
  property_count: 3
  slug: attribution-api-attribution-response
- name: CohortListResponse
  property_count: 1
  slug: behavioral-cohorts-api-cohort-list-response
- name: CohortRequestResponse
  property_count: 2
  slug: behavioral-cohorts-api-cohort-request-response
- name: Cohort
  property_count: 8
  slug: behavioral-cohorts-api-cohort
- name: CohortStatusResponse
  property_count: 2
  slug: behavioral-cohorts-api-cohort-status-response
- name: CohortUploadRequest
  property_count: 4
  slug: behavioral-cohorts-api-cohort-upload-request
- name: CohortUploadResponse
  property_count: 1
  slug: behavioral-cohorts-api-cohort-upload-response
- name: AnnotationListResponse
  property_count: 1
  slug: chart-annotations-api-annotation-list-response
- name: Annotation
  property_count: 9
  slug: chart-annotations-api-annotation
- name: CreateAnnotationRequest
  property_count: 6
  slug: chart-annotations-api-create-annotation-request
- name: UpdateAnnotationRequest
  property_count: 6
  slug: chart-annotations-api-update-annotation-request
- name: EventListResult
  property_count: 1
  slug: dashboard-rest-api-event-list-result
- name: FunnelResult
  property_count: 1
  slug: dashboard-rest-api-funnel-result
- name: RetentionResult
  property_count: 1
  slug: dashboard-rest-api-retention-result
- name: SegmentationResult
  property_count: 1
  slug: dashboard-rest-api-segmentation-result
- name: UserActivityResult
  property_count: 2
  slug: dashboard-rest-api-user-activity-result
- name: UserSearchResult
  property_count: 1
  slug: dashboard-rest-api-user-search-result
- name: DeletionListResponse
  property_count: 1
  slug: dsar-api-deletion-list-response
- name: DeletionRequest
  property_count: 3
  slug: dsar-api-deletion-request
- name: DeletionResponse
  property_count: 2
  slug: dsar-api-deletion-response
- name: DsarRequest
  property_count: 1
  slug: dsar-api-dsar-request
- name: DsarResponse
  property_count: 2
  slug: dsar-api-dsar-response
- name: DsarStatusResponse
  property_count: 3
  slug: dsar-api-dsar-status-response
- name: EvaluationRequest
  property_count: 5
  slug: experiment-evaluation-api-evaluation-request
- name: EvaluationResponse
  property_count: 0
  slug: experiment-evaluation-api-evaluation-response
- name: FlagConfiguration
  property_count: 4
  slug: experiment-evaluation-api-flag-configuration
- name: Variant
  property_count: 4
  slug: experiment-evaluation-api-variant
- name: CreateExperimentRequest
  property_count: 5
  slug: experiment-management-api-create-experiment-request
- name: CreateFlagRequest
  property_count: 5
  slug: experiment-management-api-create-flag-request
- name: DeploymentListResponse
  property_count: 1
  slug: experiment-management-api-deployment-list-response
- name: Deployment
  property_count: 5
  slug: experiment-management-api-deployment
- name: ExperimentListResponse
  property_count: 2
  slug: experiment-management-api-experiment-list-response
- name: Experiment
  property_count: 16
  slug: experiment-management-api-experiment
- name: FlagListResponse
  property_count: 2
  slug: experiment-management-api-flag-list-response
- name: Flag
  property_count: 13
  slug: experiment-management-api-flag
- name: Segment
  property_count: 4
  slug: experiment-management-api-segment
- name: UpdateExperimentRequest
  property_count: 5
  slug: experiment-management-api-update-experiment-request
- name: UpdateFlagRequest
  property_count: 5
  slug: experiment-management-api-update-flag-request
- name: VariantConfig
  property_count: 5
  slug: experiment-management-api-variant-config
- name: VersionListResponse
  property_count: 2
  slug: experiment-management-api-version-list-response
- name: Event
  property_count: 36
  slug: http-v2-api-event
- name: UploadOptions
  property_count: 1
  slug: http-v2-api-upload-options
- name: UploadRequestBody
  property_count: 3
  slug: http-v2-api-upload-request-body
- name: UploadResponse
  property_count: 4
  slug: http-v2-api-upload-response
- name: Identification
  property_count: 3
  slug: identify-api-identification
- name: IdentifyRequestBody
  property_count: 2
  slug: identify-api-identify-request-body
- name: IdentifyRequestForm
  property_count: 2
  slug: identify-api-identify-request-form
- name: IdentifyResponse
  property_count: 3
  slug: identify-api-identify-response
- name: UserPropertyOperations
  property_count: 7
  slug: identify-api-user-property-operations
- name: ScimGroupListResponse
  property_count: 3
  slug: scim-api-scim-group-list-response
- name: ScimGroupRequest
  property_count: 3
  slug: scim-api-scim-group-request
- name: ScimGroup
  property_count: 5
  slug: scim-api-scim-group
- name: ScimPatchRequest
  property_count: 2
  slug: scim-api-scim-patch-request
- name: ScimUserListResponse
  property_count: 5
  slug: scim-api-scim-user-list-response
- name: ScimUserRequest
  property_count: 5
  slug: scim-api-scim-user-request
- name: ScimUser
  property_count: 8
  slug: scim-api-scim-user
- name: CategoryListResponse
  property_count: 1
  slug: taxonomy-api-category-list-response
- name: Category
  property_count: 2
  slug: taxonomy-api-category
- name: EventPropertyListResponse
  property_count: 1
  slug: taxonomy-api-event-property-list-response
- name: EventProperty
  property_count: 5
  slug: taxonomy-api-event-property
- name: EventTypeListResponse
  property_count: 1
  slug: taxonomy-api-event-type-list-response
- name: EventType
  property_count: 3
  slug: taxonomy-api-event-type
- name: SuccessResponse
  property_count: 1
  slug: taxonomy-api-success-response
- name: UserPropertyListResponse
  property_count: 1
  slug: taxonomy-api-user-property-list-response
- name: UserProperty
  property_count: 3
  slug: taxonomy-api-user-property
- name: UserMapRequest
  property_count: 1
  slug: user-mapping-api-user-map-request
- name: UserMapResponse
  property_count: 2
  slug: user-mapping-api-user-map-response
- name: UserMapping
  property_count: 3
  slug: user-mapping-api-user-mapping
- name: UserUnmapRequest
  property_count: 1
  slug: user-mapping-api-user-unmap-request
- name: Recommendation
  property_count: 5
  slug: user-profile-api-recommendation
- name: UserData
  property_count: 6
  slug: user-profile-api-user-data
- name: UserProfileResponse
  property_count: 1
  slug: user-profile-api-user-profile-response
json_structures:
- name: Amplitude Cohort Structure
  property_count: 9
  slug: amplitude-cohort-structure
- name: Amplitude Event Structure
  property_count: 36
  slug: amplitude-event-structure
- name: Amplitude Experiment Structure
  property_count: 17
  slug: amplitude-experiment-structure
- name: Amplitude Structure
  property_count: 0
  slug: amplitude-structure
- name: Attribution Api Attribution Event Structure
  property_count: 20
  slug: attribution-api-attribution-event-structure
- name: Attribution Api Attribution Request Structure
  property_count: 2
  slug: attribution-api-attribution-request-structure
- name: Attribution Api Attribution Response Structure
  property_count: 3
  slug: attribution-api-attribution-response-structure
- name: Behavioral Cohorts Api Cohort List Response Structure
  property_count: 1
  slug: behavioral-cohorts-api-cohort-list-response-structure
- name: Behavioral Cohorts Api Cohort Request Response Structure
  property_count: 2
  slug: behavioral-cohorts-api-cohort-request-response-structure
- name: Behavioral Cohorts Api Cohort Status Response Structure
  property_count: 2
  slug: behavioral-cohorts-api-cohort-status-response-structure
- name: Behavioral Cohorts Api Cohort Structure
  property_count: 8
  slug: behavioral-cohorts-api-cohort-structure
- name: Behavioral Cohorts Api Cohort Upload Request Structure
  property_count: 4
  slug: behavioral-cohorts-api-cohort-upload-request-structure
- name: Behavioral Cohorts Api Cohort Upload Response Structure
  property_count: 1
  slug: behavioral-cohorts-api-cohort-upload-response-structure
- name: Chart Annotations Api Annotation List Response Structure
  property_count: 1
  slug: chart-annotations-api-annotation-list-response-structure
- name: Chart Annotations Api Annotation Structure
  property_count: 9
  slug: chart-annotations-api-annotation-structure
- name: Chart Annotations Api Create Annotation Request Structure
  property_count: 6
  slug: chart-annotations-api-create-annotation-request-structure
- name: Chart Annotations Api Update Annotation Request Structure
  property_count: 6
  slug: chart-annotations-api-update-annotation-request-structure
- name: Dashboard Rest Api Event List Result Structure
  property_count: 1
  slug: dashboard-rest-api-event-list-result-structure
- name: Dashboard Rest Api Funnel Result Structure
  property_count: 1
  slug: dashboard-rest-api-funnel-result-structure
- name: Dashboard Rest Api Retention Result Structure
  property_count: 1
  slug: dashboard-rest-api-retention-result-structure
- name: Dashboard Rest Api Segmentation Result Structure
  property_count: 1
  slug: dashboard-rest-api-segmentation-result-structure
- name: Dashboard Rest Api User Activity Result Structure
  property_count: 2
  slug: dashboard-rest-api-user-activity-result-structure
- name: Dashboard Rest Api User Search Result Structure
  property_count: 1
  slug: dashboard-rest-api-user-search-result-structure
- name: Dsar Api Deletion List Response Structure
  property_count: 1
  slug: dsar-api-deletion-list-response-structure
- name: Dsar Api Deletion Request Structure
  property_count: 3
  slug: dsar-api-deletion-request-structure
- name: Dsar Api Deletion Response Structure
  property_count: 2
  slug: dsar-api-deletion-response-structure
- name: Dsar Api Dsar Request Structure
  property_count: 1
  slug: dsar-api-dsar-request-structure
- name: Dsar Api Dsar Response Structure
  property_count: 2
  slug: dsar-api-dsar-response-structure
- name: Dsar Api Dsar Status Response Structure
  property_count: 3
  slug: dsar-api-dsar-status-response-structure
- name: Experiment Evaluation Api Evaluation Request Structure
  property_count: 5
  slug: experiment-evaluation-api-evaluation-request-structure
- name: Experiment Evaluation Api Evaluation Response Structure
  property_count: 0
  slug: experiment-evaluation-api-evaluation-response-structure
- name: Experiment Evaluation Api Flag Configuration Structure
  property_count: 4
  slug: experiment-evaluation-api-flag-configuration-structure
- name: Experiment Evaluation Api Variant Structure
  property_count: 4
  slug: experiment-evaluation-api-variant-structure
- name: Experiment Management Api Create Experiment Request Structure
  property_count: 5
  slug: experiment-management-api-create-experiment-request-structure
- name: Experiment Management Api Create Flag Request Structure
  property_count: 5
  slug: experiment-management-api-create-flag-request-structure
- name: Experiment Management Api Deployment List Response Structure
  property_count: 1
  slug: experiment-management-api-deployment-list-response-structure
- name: Experiment Management Api Deployment Structure
  property_count: 5
  slug: experiment-management-api-deployment-structure
- name: Experiment Management Api Experiment List Response Structure
  property_count: 2
  slug: experiment-management-api-experiment-list-response-structure
- name: Experiment Management Api Experiment Structure
  property_count: 16
  slug: experiment-management-api-experiment-structure
- name: Experiment Management Api Flag List Response Structure
  property_count: 2
  slug: experiment-management-api-flag-list-response-structure
- name: Experiment Management Api Flag Structure
  property_count: 13
  slug: experiment-management-api-flag-structure
- name: Experiment Management Api Segment Structure
  property_count: 4
  slug: experiment-management-api-segment-structure
- name: Experiment Management Api Update Experiment Request Structure
  property_count: 5
  slug: experiment-management-api-update-experiment-request-structure
- name: Experiment Management Api Update Flag Request Structure
  property_count: 5
  slug: experiment-management-api-update-flag-request-structure
- name: Experiment Management Api Variant Config Structure
  property_count: 5
  slug: experiment-management-api-variant-config-structure
- name: Experiment Management Api Version List Response Structure
  property_count: 2
  slug: experiment-management-api-version-list-response-structure
- name: Http V2 Api Event Structure
  property_count: 36
  slug: http-v2-api-event-structure
- name: Http V2 Api Upload Options Structure
  property_count: 1
  slug: http-v2-api-upload-options-structure
- name: Http V2 Api Upload Request Body Structure
  property_count: 3
  slug: http-v2-api-upload-request-body-structure
- name: Http V2 Api Upload Response Structure
  property_count: 4
  slug: http-v2-api-upload-response-structure
- name: Identify Api Identification Structure
  property_count: 3
  slug: identify-api-identification-structure
- name: Identify Api Identify Request Body Structure
  property_count: 2
  slug: identify-api-identify-request-body-structure
- name: Identify Api Identify Request Form Structure
  property_count: 2
  slug: identify-api-identify-request-form-structure
- name: Identify Api Identify Response Structure
  property_count: 3
  slug: identify-api-identify-response-structure
- name: Identify Api User Property Operations Structure
  property_count: 7
  slug: identify-api-user-property-operations-structure
- name: Scim Api Scim Group List Response Structure
  property_count: 3
  slug: scim-api-scim-group-list-response-structure
- name: Scim Api Scim Group Request Structure
  property_count: 3
  slug: scim-api-scim-group-request-structure
- name: Scim Api Scim Group Structure
  property_count: 5
  slug: scim-api-scim-group-structure
- name: Scim Api Scim Patch Request Structure
  property_count: 2
  slug: scim-api-scim-patch-request-structure
- name: Scim Api Scim User List Response Structure
  property_count: 5
  slug: scim-api-scim-user-list-response-structure
- name: Scim Api Scim User Request Structure
  property_count: 5
  slug: scim-api-scim-user-request-structure
- name: Scim Api Scim User Structure
  property_count: 8
  slug: scim-api-scim-user-structure
- name: Taxonomy Api Category List Response Structure
  property_count: 1
  slug: taxonomy-api-category-list-response-structure
- name: Taxonomy Api Category Structure
  property_count: 2
  slug: taxonomy-api-category-structure
- name: Taxonomy Api Event Property List Response Structure
  property_count: 1
  slug: taxonomy-api-event-property-list-response-structure
- name: Taxonomy Api Event Property Structure
  property_count: 5
  slug: taxonomy-api-event-property-structure
- name: Taxonomy Api Event Type List Response Structure
  property_count: 1
  slug: taxonomy-api-event-type-list-response-structure
- name: Taxonomy Api Event Type Structure
  property_count: 3
  slug: taxonomy-api-event-type-structure
- name: Taxonomy Api Success Response Structure
  property_count: 1
  slug: taxonomy-api-success-response-structure
- name: Taxonomy Api User Property List Response Structure
  property_count: 1
  slug: taxonomy-api-user-property-list-response-structure
- name: Taxonomy Api User Property Structure
  property_count: 3
  slug: taxonomy-api-user-property-structure
- name: User Mapping Api User Map Request Structure
  property_count: 1
  slug: user-mapping-api-user-map-request-structure
- name: User Mapping Api User Map Response Structure
  property_count: 2
  slug: user-mapping-api-user-map-response-structure
- name: User Mapping Api User Mapping Structure
  property_count: 3
  slug: user-mapping-api-user-mapping-structure
- name: User Mapping Api User Unmap Request Structure
  property_count: 1
  slug: user-mapping-api-user-unmap-request-structure
- name: User Profile Api Recommendation Structure
  property_count: 5
  slug: user-profile-api-recommendation-structure
- name: User Profile Api User Data Structure
  property_count: 6
  slug: user-profile-api-user-data-structure
- name: User Profile Api User Profile Response Structure
  property_count: 1
  slug: user-profile-api-user-profile-response-structure
jsonld:
- class_count: 3
  name: Amplitude Amplitude Cohort Context
  property_count: 7
  slug: amplitude-amplitude-cohort-context
- class_count: 1
  name: Amplitude Amplitude Event Context
  property_count: 36
  slug: amplitude-amplitude-event-context
- class_count: 3
  name: Amplitude Amplitude Experiment Context
  property_count: 15
  slug: amplitude-amplitude-experiment-context
- class_count: 3
  name: Amplitude Attribution Api Context
  property_count: 25
  slug: amplitude-attribution-api-context
- class_count: 8
  name: Amplitude Behavioral Cohorts Api Context
  property_count: 12
  slug: amplitude-behavioral-cohorts-api-context
- class_count: 6
  name: Amplitude Chart Annotations Api Context
  property_count: 8
  slug: amplitude-chart-annotations-api-context
- class_count: 0
  name: Amplitude Context
  property_count: 7
  slug: amplitude-context
- class_count: 7
  name: Amplitude Dashboard Rest Api Context
  property_count: 10
  slug: amplitude-dashboard-rest-api-context
- class_count: 6
  name: Amplitude Dsar Api Context
  property_count: 8
  slug: amplitude-dsar-api-context
- class_count: 4
  name: Amplitude Experiment Evaluation Api Context
  property_count: 19
  slug: amplitude-experiment-evaluation-api-context
- class_count: 16
  name: Amplitude Experiment Management Api Context
  property_count: 32
  slug: amplitude-experiment-management-api-context
- class_count: 4
  name: Amplitude Http V2 Api Context
  property_count: 44
  slug: amplitude-http-v2-api-context
- class_count: 5
  name: Amplitude Identify Api Context
  property_count: 15
  slug: amplitude-identify-api-context
- class_count: 8
  name: Amplitude Scim Api Context
  property_count: 25
  slug: amplitude-scim-api-context
- class_count: 11
  name: Amplitude Taxonomy Api Context
  property_count: 9
  slug: amplitude-taxonomy-api-context
- class_count: 4
  name: Amplitude User Mapping Api Context
  property_count: 6
  slug: amplitude-user-mapping-api-context
- class_count: 3
  name: Amplitude User Profile Api Context
  property_count: 12
  slug: amplitude-user-profile-api-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Amplitude
nav: Providers
network: true
overview: 'Amplitude publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Webhooks and Cohort Sync, Annotations API, Cohorts API, and 21 more. Tagged areas include A/B Testing, Analytics, Experimentation, Feature Flags, and Product Analytics.


  The Amplitude catalog on APIs.io includes 1 event-driven AsyncAPI specification, 17 JSON-LD contexts, and 3 Spectral governance rulesets.


  Amplitude''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, academy / training, support, and 39 more developer resources.'
plans:
- name: Amplitude Plans Pricing
  plan_count: 4
  slug: amplitude-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Amplitude Rate Limits
  slug: amplitude-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Amplitude API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: amplitude-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Amplitude API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amplitude-jsonschema-spectral-rules
- effective_rule_count: 71
  extends:
  - spectral:oas
  name: Amplitude API Rules
  rule_count: 30
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 15
  slug: amplitude-spectral-rules
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 28.8
    contract_quality: 80.7
    developer_ergonomics: 69.0
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/screenshots/amplitude-2026-06-20T171944.png
security:
- kind: authentication
  name: Amplitude Authentication
  slug: amplitude-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Amplitude Domain Security
  slug: amplitude-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amplitude Vulnerability Disclosure
  slug: amplitude-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Amplitude Trust Center
  slug: amplitude-trust-center
  summary_line: trust center published
skill_count: 57
skills:
- name: 7-powers-analysis
  slug: 7-powers-analysis
- name: amazon-working-backwards
  slug: amazon-working-backwards
- name: analyze-account-health
  slug: analyze-account-health
- name: analyze-chart
  slug: analyze-chart
- name: analyze-dashboard
  slug: analyze-dashboard
- name: analyze-experiments
  slug: analyze-experiments
- name: analyze-feedback
  slug: analyze-feedback
- name: build-metric-tree
  slug: build-metric-tree
- name: build-plg-strategy
  slug: build-plg-strategy
- name: churn-lost-deal-analysis
  slug: churn-lost-deal-analysis
- name: citation-recovery-optimizer
  slug: citation-recovery-optimizer
- name: competitor-monitoring
  slug: competitor-monitoring
- name: competitor-prompt-hijacker
  slug: competitor-prompt-hijacker
- name: craft-discovery-synthesis
  slug: craft-discovery-synthesis
- name: craft-experiment-design
  slug: craft-experiment-design
- name: craft-experiment-readout
  slug: craft-experiment-readout
- name: craft-spec
  slug: craft-spec
- name: create-chart
  slug: create-chart
- name: create-dashboard
  slug: create-dashboard
- name: create-user-stories
  slug: create-user-stories
- name: diagnose-acquisition
  slug: diagnose-acquisition
- name: diagnose-activation
  slug: diagnose-activation
- name: diagnose-monetization
  slug: diagnose-monetization
- name: diagnose-retention
  slug: diagnose-retention
slug: amplitude
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
use_cases:
- description: Understand how users interact with your product to prioritize features and reduce churn.
  name: Product Analytics
- description: Run controlled A/B tests to measure the causal impact of product changes.
  name: Growth Experimentation
- description: Track campaign performance and ROI by connecting acquisition events to user behavior.
  name: Marketing Attribution
- description: Export raw event data to Snowflake, BigQuery, or Redshift for custom analysis.
  name: Data Warehouse Integration
- description: Sync behavioral cohorts to ad platforms and CRMs for targeted marketing.
  name: Audience Syndication
- description: Automate GDPR and CCPA data deletion workflows for privacy compliance.
  name: Compliance Automation
- description: Automate user provisioning and deprovisioning via SCIM integration with IdPs.
  name: Enterprise Identity Management
website: https://amplitude.com
---
