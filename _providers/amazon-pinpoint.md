---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Amazon Pinpoint Agentic Access
  operation_count: 122
  slug: amazon-pinpoint-agentic-access
  summary_line: 122 operations · 70 acting
api_count: 6
apis:
- description: Operations for managing Pinpoint applications (projects)
  name: Amazon Pinpoint Applications API
  slug: amazon-pinpoint-applications-api
- description: The Apps API from Amazon Pinpoint — 48 operation(s) for apps.
  name: Amazon Pinpoint Apps API
  slug: amazon-pinpoint-apps-api
- description: The Phone API from Amazon Pinpoint — 1 operation(s) for phone.
  name: Amazon Pinpoint Phone API
  slug: amazon-pinpoint-phone-api
- description: The Recommenders API from Amazon Pinpoint — 2 operation(s) for recommenders.
  name: Amazon Pinpoint Recommenders API
  slug: amazon-pinpoint-recommenders-api
- description: The Tags API from Amazon Pinpoint — 2 operation(s) for tags.
  name: Amazon Pinpoint Tags API
  slug: amazon-pinpoint-tags-api
- description: The Templates API from Amazon Pinpoint — 8 operation(s) for templates.
  name: Amazon Pinpoint Templates API
  slug: amazon-pinpoint-templates-api
arazzos:
- description: Upsert a batch of endpoints then send a direct message to the project.
  name: Amazon Pinpoint Batch Update Endpoints and Send
  slug: amazon-pinpoint-batch-update-endpoints-send-workflow
- description: Create a project, define an audience segment, then launch a campaign targeting it.
  name: Amazon Pinpoint Build Segment and Campaign
  slug: amazon-pinpoint-build-segment-campaign-workflow
- description: Attach a Kinesis event stream to a project then read it back to confirm.
  name: Amazon Pinpoint Configure Event Stream
  slug: amazon-pinpoint-configure-event-stream-workflow
- description: Create a campaign then poll its status until it leaves the scheduled state.
  name: Amazon Pinpoint Launch Campaign and Await Status
  slug: amazon-pinpoint-launch-campaign-await-status-workflow
- description: Create a draft journey then activate it by updating its state to ACTIVE.
  name: Amazon Pinpoint Launch Journey
  slug: amazon-pinpoint-launch-journey-workflow
- description: Look up all endpoints for a user then send them a message across every channel.
  name: Amazon Pinpoint Message User Across Endpoints
  slug: amazon-pinpoint-message-user-across-endpoints-workflow
- description: Activate a draft journey then immediately pause it for review.
  name: Amazon Pinpoint Pause Active Journey
  slug: amazon-pinpoint-pause-active-journey-workflow
- description: Create a project, define a segment, build a journey on it, and activate it.
  name: Amazon Pinpoint Provision Journey End to End
  slug: amazon-pinpoint-provision-journey-end-to-end-workflow
- description: Create a project then apply its default campaign limits and quiet time settings.
  name: Amazon Pinpoint Provision Project with Settings
  slug: amazon-pinpoint-provision-project-with-settings-workflow
- description: Create a Pinpoint application then verify it appears in the account application list.
  name: Amazon Pinpoint Provision Project
  slug: amazon-pinpoint-provision-project-workflow
- description: Create an SMS template then promote a chosen version to the active version.
  name: Amazon Pinpoint Publish and Activate Template
  slug: amazon-pinpoint-publish-and-activate-template-workflow
- description: Create an in-app message template then read it back to confirm it was stored.
  name: Amazon Pinpoint Publish In-App Template
  slug: amazon-pinpoint-publish-in-app-template-workflow
- description: Create a voice message template then promote a version to active.
  name: Amazon Pinpoint Publish Voice Template
  slug: amazon-pinpoint-publish-voice-template-workflow
- description: Create a push notification template then launch a campaign that uses it.
  name: Amazon Pinpoint Push Template Campaign
  slug: amazon-pinpoint-push-template-campaign-workflow
- description: Update a segment's dimensions then repoint a campaign at the new segment version.
  name: Amazon Pinpoint Reversion Segment and Campaign
  slug: amazon-pinpoint-reversion-segment-campaign-workflow
- description: Send a one-time passcode to a recipient then verify the code they supply.
  name: Amazon Pinpoint Send and Verify OTP
  slug: amazon-pinpoint-send-and-verify-otp-workflow
- description: Create a paused campaign then branch to launch it or leave it staged for review.
  name: Amazon Pinpoint Stage or Launch Campaign
  slug: amazon-pinpoint-stage-or-launch-campaign-workflow
- description: Create an email message template then launch a campaign that uses it.
  name: Amazon Pinpoint Template Driven Campaign
  slug: amazon-pinpoint-template-driven-campaign-workflow
- description: Register or update an endpoint, then send a direct message to it.
  name: Amazon Pinpoint Update Endpoint and Send Message
  slug: amazon-pinpoint-update-endpoint-send-message-workflow
artifact_total: 1075
asyncapis:
- description: ''
  name: Amazon Pinpoint Events
  slug: amazon-pinpoint-events
collections:
- collection_type: postman
  name: Amazon Pinpoint Applications API
  slug: postman-amazon-pinpoint-applications-api
- collection_type: postman
  name: Amazon Pinpoint Applications Apps API
  slug: postman-amazon-pinpoint-apps-api
- collection_type: postman
  name: Amazon Pinpoint
  slug: postman-amazon-pinpoint-openapi-original
- collection_type: postman
  name: Amazon Pinpoint Applications Phone API
  slug: postman-amazon-pinpoint-phone-api
- collection_type: postman
  name: Amazon Pinpoint Applications Recommenders API
  slug: postman-amazon-pinpoint-recommenders-api
- collection_type: postman
  name: Amazon Pinpoint Applications Tags API
  slug: postman-amazon-pinpoint-tags-api
- collection_type: postman
  name: Amazon Pinpoint Applications Templates API
  slug: postman-amazon-pinpoint-templates-api
- collection_type: postman
  name: Amazon Pinpoint API
  slug: postman-amazon-pinpoint
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Pinpoint Applications API
  slug: open-amazon-pinpoint-applications-api
- collection_type: open
  name: Amazon Pinpoint Applications Apps API
  slug: open-amazon-pinpoint-apps-api
- collection_type: open
  name: Amazon Pinpoint Applications Phone API
  slug: open-amazon-pinpoint-phone-api
- collection_type: open
  name: Amazon Pinpoint Applications Recommenders API
  slug: open-amazon-pinpoint-recommenders-api
- collection_type: open
  name: Amazon Pinpoint Applications Tags API
  slug: open-amazon-pinpoint-tags-api
- collection_type: open
  name: Amazon Pinpoint Applications Templates API
  slug: open-amazon-pinpoint-templates-api
- collection_type: open
  name: Amazon Pinpoint API
  slug: open-amazon-pinpoint
common:
- group: build
  title: ''
  type: Packages
  url: packages/amazon-pinpoint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amazon-pinpoint-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-pinpoint-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-pinpoint-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-pinpoint-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-pinpoint-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-pinpoint-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-pinpoint-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html
- group: auth
  title: ''
  type: Security
  url: https://vdp.aws.security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-pinpoint-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/amazon-pinpoint-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-pinpoint-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amazon-pinpoint-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-pinpoint-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amazon-pinpoint-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amazon-pinpoint-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amazon-pinpoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amazon-pinpoint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/amazon-pinpoint-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/pinpoint/latest/apireference/welcome.html
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-pinpoint-applications-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-pinpoint-apps-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-pinpoint-phone-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-pinpoint-recommenders-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-pinpoint-tags-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-pinpoint-templates-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-pinpoint-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-pinpoint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-pinpoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-pinpoint-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-pinpoint/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-batch-update-endpoints-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-build-segment-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-configure-event-stream-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-launch-campaign-await-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-launch-journey-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-message-user-across-endpoints-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-pause-active-journey-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-provision-journey-end-to-end-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-provision-project-with-settings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-provision-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-publish-and-activate-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-publish-in-app-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-publish-voice-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-push-template-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-reversion-segment-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-send-and-verify-otp-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-stage-or-launch-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-template-driven-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-pinpoint-update-endpoint-send-message-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/pinpoint/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/messaging-and-targeting/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/pinpoint/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/pinpoint/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/pinpoint/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/pinpoint/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/pinpoint/faqs/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-pinpoint
- group: build
  title: ''
  type: CodeExamples
  url: https://docs.aws.amazon.com/code-library/latest/ug/pinpoint_code_examples.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-pinpoint-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-pinpoint-vocabulary.yaml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-application-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-message-request-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-campaigns-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-segments-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-journeys-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-messages-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-analytics-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-apps-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-channels-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-endpoints-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-general-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-pinpoint-templates-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-action-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-activities-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-activity-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-address-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-adm-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-adm-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-adm-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-alignment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-android-push-notification-template-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-push-notification-template-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-sandbox-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-sandbox-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-voip-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-voip-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-voip-sandbox-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-apns-voip-sandbox-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-application-date-range-kpi-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-application-settings-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-applications-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-attribute-dimension-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-attribute-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-attributes-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-baidu-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-baidu-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-baidu-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-base-kpi-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-button-action-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-custom-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-date-range-kpi-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-email-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-event-filter-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-hook-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-in-app-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-limits-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-sms-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-state-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaign-status-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-campaigns-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-channel-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-channels-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-closed-days-rule-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-closed-days-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-condition-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-conditional-split-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-contact-center-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-app-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-app-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-application-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-campaign-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-campaign-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-email-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-email-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-export-job-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-export-job-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-import-job-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-import-job-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-in-app-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-in-app-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-journey-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-journey-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-push-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-push-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-recommender-configuration-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-recommender-configuration-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-recommender-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-segment-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-segment-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-sms-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-sms-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-template-message-body-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-voice-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-create-voice-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-custom-delivery-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-custom-message-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-day-of-week-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-default-button-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-default-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-default-push-notification-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-default-push-notification-template-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-adm-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-adm-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-apns-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-apns-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-apns-sandbox-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-apns-sandbox-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-apns-voip-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-apns-voip-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-apns-voip-sandbox-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-apns-voip-sandbox-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-app-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-app-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-baidu-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-baidu-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-campaign-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-campaign-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-email-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-email-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-email-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-email-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-endpoint-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-endpoint-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-event-stream-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-event-stream-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-gcm-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-gcm-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-in-app-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-in-app-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-journey-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-journey-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-push-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-push-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-recommender-configuration-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-recommender-configuration-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-segment-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-segment-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-sms-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-sms-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-sms-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-sms-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-user-endpoints-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-user-endpoints-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-voice-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-voice-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-voice-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delete-voice-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-delivery-status-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-direct-message-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-duration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-email-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-email-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-email-message-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-email-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-email-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-email-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-batch-item-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-batch-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-demographic-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-item-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-location-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-message-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-send-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoint-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-endpoints-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-event-condition-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-event-dimensions-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-event-filter-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-event-item-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-event-start-condition-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-event-stream-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-events-batch-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-events-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-events-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-export-job-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-export-job-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-export-job-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-export-jobs-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-frequency-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-gcm-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-gcm-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-gcm-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-adm-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-adm-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apns-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apns-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apns-sandbox-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apns-sandbox-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apns-voip-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apns-voip-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apns-voip-sandbox-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apns-voip-sandbox-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-app-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-app-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-application-date-range-kpi-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-application-date-range-kpi-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-application-settings-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-application-settings-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apps-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-apps-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-baidu-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-baidu-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-activities-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-activities-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-date-range-kpi-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-date-range-kpi-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-version-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-version-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-versions-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaign-versions-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaigns-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-campaigns-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-channels-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-channels-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-email-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-email-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-email-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-email-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-endpoint-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-endpoint-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-event-stream-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-event-stream-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-export-job-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-export-job-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-export-jobs-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-export-jobs-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-gcm-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-gcm-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-import-job-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-import-job-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-import-jobs-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-import-jobs-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-in-app-messages-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-in-app-messages-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-in-app-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-in-app-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-journey-date-range-kpi-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-journey-date-range-kpi-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-journey-execution-activity-metrics-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-journey-execution-activity-metrics-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-journey-execution-metrics-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-journey-execution-metrics-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-journey-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-journey-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-push-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-push-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-recommender-configuration-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-recommender-configuration-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-recommender-configurations-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-recommender-configurations-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-export-jobs-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-export-jobs-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-import-jobs-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-import-jobs-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-version-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-version-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-versions-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segment-versions-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segments-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-segments-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-sms-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-sms-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-sms-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-sms-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-user-endpoints-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-user-endpoints-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-voice-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-voice-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-voice-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-get-voice-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-gps-coordinates-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-gps-point-dimension-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-holdout-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-import-job-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-import-job-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-import-job-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-import-jobs-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-campaign-schedule-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-message-body-config-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-message-button-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-message-campaign-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-message-content-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-message-header-config-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-messages-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-in-app-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-include-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-item-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-job-status-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-channel-settings-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-custom-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-date-range-kpi-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-email-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-execution-activity-metrics-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-execution-metrics-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-limits-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-push-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-schedule-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-sms-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journey-state-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-journeys-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-layout-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-journeys-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-journeys-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-recommender-configurations-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-tags-for-resource-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-tags-for-resource-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-template-versions-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-template-versions-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-templates-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-list-templates-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-message-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-message-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-message-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-metric-dimension-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-multi-conditional-branch-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-multi-conditional-split-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-number-validate-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-number-validate-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-open-hours-rule-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-open-hours-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-override-button-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-phone-number-validate-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-phone-number-validate-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-public-endpoint-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-push-message-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-push-notification-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-push-notification-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-put-event-stream-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-put-event-stream-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-put-events-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-put-events-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-quiet-time-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-random-split-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-random-split-entry-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-raw-email-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-recency-dimension-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-recommender-configuration-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-remove-attributes-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-remove-attributes-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-result-row-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-result-row-value-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-schedule-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-behaviors-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-condition-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-demographics-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-dimensions-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-group-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-group-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-import-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-location-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segment-reference-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-segments-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-messages-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-messages-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-otp-message-request-parameters-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-otp-message-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-otp-message-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-users-message-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-users-message-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-users-messages-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-send-users-messages-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-session-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-set-dimension-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-simple-condition-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-simple-email-part-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-simple-email-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-sms-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-sms-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-sms-message-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-sms-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-sms-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-sms-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-source-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-start-condition-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-state-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-tag-resource-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-tags-model-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-template-active-version-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-template-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-template-create-message-body-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-template-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-template-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-template-version-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-template-versions-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-templates-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-treatment-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-untag-resource-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-adm-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-adm-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-apns-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-apns-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-apns-sandbox-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-apns-sandbox-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-apns-voip-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-apns-voip-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-apns-voip-sandbox-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-apns-voip-sandbox-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-application-settings-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-application-settings-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-attributes-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-baidu-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-baidu-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-campaign-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-campaign-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-email-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-email-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-email-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-email-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-endpoint-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-endpoint-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-endpoints-batch-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-endpoints-batch-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-gcm-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-gcm-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-in-app-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-in-app-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-journey-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-journey-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-journey-state-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-journey-state-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-push-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-push-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-recommender-configuration-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-recommender-configuration-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-recommender-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-segment-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-segment-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-sms-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-sms-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-sms-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-sms-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-template-active-version-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-template-active-version-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-voice-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-voice-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-voice-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-update-voice-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-verification-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-verify-otp-message-request-parameters-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-verify-otp-message-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-verify-otp-message-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-voice-channel-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-voice-channel-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-voice-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-voice-template-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-voice-template-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-wait-activity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-wait-time-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-write-application-settings-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-write-campaign-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-write-event-stream-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-write-journey-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-write-segment-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-pinpoint-write-treatment-resource-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-action-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-activities-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-activity-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-address-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-adm-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-adm-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-adm-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-alignment-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-android-push-notification-template-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-push-notification-template-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-sandbox-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-sandbox-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-voip-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-voip-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-voip-sandbox-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-apns-voip-sandbox-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-application-date-range-kpi-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-application-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-application-settings-resource-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-applications-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-attribute-dimension-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-attribute-type-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-attributes-resource-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-baidu-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-baidu-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-baidu-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-base-kpi-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-button-action-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-custom-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-date-range-kpi-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-email-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-event-filter-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-hook-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-in-app-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-limits-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-sms-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-state-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaign-status-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-campaigns-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-channel-type-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-channels-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-closed-days-rule-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-closed-days-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-condition-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-conditional-split-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-contact-center-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-app-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-app-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-application-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-campaign-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-campaign-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-email-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-email-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-export-job-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-export-job-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-import-job-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-import-job-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-in-app-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-in-app-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-journey-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-journey-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-push-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-push-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-recommender-configuration-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-recommender-configuration-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-recommender-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-segment-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-segment-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-sms-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-sms-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-template-message-body-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-voice-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-create-voice-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-custom-delivery-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-custom-message-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-day-of-week-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-default-button-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-default-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-default-push-notification-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-default-push-notification-template-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-adm-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-adm-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-apns-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-apns-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-apns-sandbox-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-apns-sandbox-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-apns-voip-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-apns-voip-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-apns-voip-sandbox-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-apns-voip-sandbox-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-app-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-app-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-baidu-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-baidu-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-campaign-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-campaign-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-email-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-email-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-email-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-email-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-endpoint-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-endpoint-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-event-stream-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-event-stream-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-gcm-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-gcm-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-in-app-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-in-app-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-journey-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-journey-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-push-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-push-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-recommender-configuration-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-recommender-configuration-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-segment-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-segment-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-sms-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-sms-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-sms-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-sms-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-user-endpoints-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-user-endpoints-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-voice-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-voice-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-voice-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delete-voice-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-delivery-status-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-direct-message-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-duration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-email-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-email-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-email-message-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-email-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-email-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-email-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-batch-item-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-batch-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-demographic-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-item-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-location-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-message-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-send-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoint-user-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-endpoints-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-event-condition-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-event-dimensions-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-event-filter-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-event-item-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-event-start-condition-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-event-stream-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-event-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-events-batch-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-events-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-events-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-export-job-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-export-job-resource-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-export-job-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-export-jobs-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-frequency-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-gcm-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-gcm-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-gcm-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-adm-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-adm-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apns-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apns-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apns-sandbox-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apns-sandbox-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apns-voip-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apns-voip-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apns-voip-sandbox-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apns-voip-sandbox-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-app-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-app-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-application-date-range-kpi-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-application-date-range-kpi-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-application-settings-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-application-settings-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apps-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-apps-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-baidu-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-baidu-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-activities-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-activities-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-date-range-kpi-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-date-range-kpi-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-version-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-version-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-versions-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaign-versions-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaigns-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-campaigns-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-channels-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-channels-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-email-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-email-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-email-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-email-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-endpoint-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-endpoint-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-event-stream-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-event-stream-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-export-job-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-export-job-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-export-jobs-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-export-jobs-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-gcm-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-gcm-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-import-job-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-import-job-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-import-jobs-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-import-jobs-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-in-app-messages-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-in-app-messages-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-in-app-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-in-app-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-journey-date-range-kpi-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-journey-date-range-kpi-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-journey-execution-activity-metrics-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-journey-execution-activity-metrics-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-journey-execution-metrics-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-journey-execution-metrics-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-journey-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-journey-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-push-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-push-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-recommender-configuration-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-recommender-configuration-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-recommender-configurations-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-recommender-configurations-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-export-jobs-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-export-jobs-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-import-jobs-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-import-jobs-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-version-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-version-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-versions-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segment-versions-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segments-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-segments-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-sms-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-sms-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-sms-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-sms-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-user-endpoints-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-user-endpoints-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-voice-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-voice-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-voice-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-get-voice-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-gps-coordinates-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-gps-point-dimension-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-holdout-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-import-job-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-import-job-resource-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-import-job-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-import-jobs-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-campaign-schedule-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-message-body-config-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-message-button-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-message-campaign-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-message-content-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-message-header-config-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-messages-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-in-app-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-include-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-item-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-job-status-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-channel-settings-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-custom-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-date-range-kpi-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-email-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-execution-activity-metrics-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-execution-metrics-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-limits-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-push-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-schedule-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-sms-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journey-state-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-journeys-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-layout-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-journeys-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-journeys-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-recommender-configurations-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-tags-for-resource-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-tags-for-resource-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-template-versions-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-template-versions-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-templates-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-list-templates-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-message-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-message-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-message-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-message-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-metric-dimension-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-multi-conditional-branch-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-multi-conditional-split-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-number-validate-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-number-validate-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-open-hours-rule-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-open-hours-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-override-button-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-phone-number-validate-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-phone-number-validate-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-public-endpoint-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-push-message-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-push-notification-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-push-notification-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-put-event-stream-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-put-event-stream-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-put-events-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-put-events-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-quiet-time-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-random-split-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-random-split-entry-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-raw-email-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-recency-dimension-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-recommender-configuration-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-remove-attributes-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-remove-attributes-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-result-row-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-result-row-value-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-schedule-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-behaviors-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-condition-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-demographics-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-dimensions-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-group-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-group-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-import-resource-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-location-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-reference-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segment-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-segments-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-messages-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-messages-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-otp-message-request-parameters-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-otp-message-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-otp-message-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-users-message-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-users-message-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-users-messages-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-send-users-messages-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-session-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-set-dimension-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-simple-condition-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-simple-email-part-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-simple-email-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-sms-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-sms-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-sms-message-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-sms-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-sms-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-sms-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-source-type-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-start-condition-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-state-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-tag-resource-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-tags-model-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-template-active-version-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-template-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-template-create-message-body-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-template-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-template-type-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-template-version-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-template-versions-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-templates-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-treatment-resource-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-type-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-untag-resource-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-adm-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-adm-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-apns-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-apns-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-apns-sandbox-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-apns-sandbox-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-apns-voip-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-apns-voip-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-apns-voip-sandbox-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-apns-voip-sandbox-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-application-settings-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-application-settings-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-attributes-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-baidu-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-baidu-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-campaign-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-campaign-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-email-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-email-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-email-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-email-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-endpoint-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-endpoint-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-endpoints-batch-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-endpoints-batch-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-gcm-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-gcm-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-in-app-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-in-app-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-journey-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-journey-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-journey-state-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-journey-state-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-push-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-push-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-recommender-configuration-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-recommender-configuration-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-recommender-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-segment-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-segment-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-sms-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-sms-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-sms-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-sms-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-template-active-version-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-template-active-version-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-voice-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-voice-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-voice-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-update-voice-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-verification-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-verify-otp-message-request-parameters-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-verify-otp-message-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-verify-otp-message-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-voice-channel-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-voice-channel-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-voice-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-voice-template-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-voice-template-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-wait-activity-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-wait-time-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-write-application-settings-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-write-campaign-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-write-event-stream-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-write-journey-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-write-segment-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-pinpoint-write-treatment-resource-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-activity-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-android-push-notification-template-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-apns-channel-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-applications-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-attributes-resource-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-baidu-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-campaign-date-range-kpi-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-campaign-hook-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-campaign-state-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-create-campaign-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-create-sms-template-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-create-voice-template-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-delete-campaign-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-delete-email-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-delete-journey-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-delete-sms-template-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-delete-voice-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-direct-message-configuration-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-email-message-activity-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-email-template-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-endpoint-demographic-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-endpoint-message-result-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-events-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-export-jobs-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-gcm-message-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-adm-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-apns-voip-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-apns-voip-sandbox-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-campaign-activities-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-campaign-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-campaigns-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-email-template-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-gcm-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-import-jobs-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-in-app-messages-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-push-template-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-recommender-configurations-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-segment-versions-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-get-sms-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-gps-coordinates-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-holdout-activity-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-import-job-resource-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-in-app-messages-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-journey-email-message-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-journey-execution-activity-metrics-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-journey-limits-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-journey-state-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-list-journeys-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-list-recommender-configurations-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-message-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-number-validate-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-open-hours-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-open-hours-rule-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-phone-number-validate-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-random-split-entry-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-result-row-value-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-segment-group-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-segment-location-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-send-messages-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-send-otp-message-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-send-otp-message-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-send-users-message-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-session-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-set-dimension-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-simple-condition-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-tag-resource-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-template-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-template-versions-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-treatment-resource-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-apns-channel-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-campaign-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-email-channel-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-email-template-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-in-app-template-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-journey-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-recommender-configuration-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-recommender-configuration-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-update-sms-template-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-verify-otp-message-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-voice-template-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-wait-time-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-write-event-stream-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-pinpoint-write-segment-request-example.json
created: '2024-01-15'
description: Amazon Pinpoint is a flexible and scalable outbound and inbound marketing communications service that enables you to engage with customers across multiple messaging channels including email, SMS, push notifications, and voice messages. Note - AWS will end support for Amazon Pinpoint on October 30, 2026. SMS, voice, mobile push, OTP, and phone number validation APIs will continue through AWS End User Messaging.
examples:
- key_count: 13
  name: Amazon Pinpoint Activity Response Example
  slug: amazon-pinpoint-activity-response-example
- key_count: 9
  name: Amazon Pinpoint Android Push Notification Template Example
  slug: amazon-pinpoint-android-push-notification-template-example
- key_count: 8
  name: Amazon Pinpoint Apns Channel Request Example
  slug: amazon-pinpoint-apns-channel-request-example
- key_count: 2
  name: Amazon Pinpoint Applications Response Example
  slug: amazon-pinpoint-applications-response-example
- key_count: 3
  name: Amazon Pinpoint Attributes Resource Example
  slug: amazon-pinpoint-attributes-resource-example
- key_count: 11
  name: Amazon Pinpoint Baidu Channel Response Example
  slug: amazon-pinpoint-baidu-channel-response-example
- key_count: 7
  name: Amazon Pinpoint Campaign Date Range Kpi Response Example
  slug: amazon-pinpoint-campaign-date-range-kpi-response-example
- key_count: 3
  name: Amazon Pinpoint Campaign Hook Example
  slug: amazon-pinpoint-campaign-hook-example
- key_count: 1
  name: Amazon Pinpoint Campaign State Example
  slug: amazon-pinpoint-campaign-state-example
- key_count: 1
  name: Amazon Pinpoint Create Campaign Request Example
  slug: amazon-pinpoint-create-campaign-request-example
- key_count: 1
  name: Amazon Pinpoint Create Sms Template Response Example
  slug: amazon-pinpoint-create-sms-template-response-example
- key_count: 1
  name: Amazon Pinpoint Create Voice Template Response Example
  slug: amazon-pinpoint-create-voice-template-response-example
- key_count: 1
  name: Amazon Pinpoint Delete Campaign Response Example
  slug: amazon-pinpoint-delete-campaign-response-example
- key_count: 1
  name: Amazon Pinpoint Delete Email Channel Response Example
  slug: amazon-pinpoint-delete-email-channel-response-example
- key_count: 1
  name: Amazon Pinpoint Delete Journey Response Example
  slug: amazon-pinpoint-delete-journey-response-example
- key_count: 1
  name: Amazon Pinpoint Delete Sms Template Response Example
  slug: amazon-pinpoint-delete-sms-template-response-example
- key_count: 1
  name: Amazon Pinpoint Delete Voice Channel Response Example
  slug: amazon-pinpoint-delete-voice-channel-response-example
- key_count: 9
  name: Amazon Pinpoint Direct Message Configuration Example
  slug: amazon-pinpoint-direct-message-configuration-example
- key_count: 4
  name: Amazon Pinpoint Email Message Activity Example
  slug: amazon-pinpoint-email-message-activity-example
- key_count: 7
  name: Amazon Pinpoint Email Template Request Example
  slug: amazon-pinpoint-email-template-request-example
- key_count: 8
  name: Amazon Pinpoint Endpoint Demographic Example
  slug: amazon-pinpoint-endpoint-demographic-example
- key_count: 6
  name: Amazon Pinpoint Endpoint Message Result Example
  slug: amazon-pinpoint-endpoint-message-result-example
- key_count: 1
  name: Amazon Pinpoint Events Request Example
  slug: amazon-pinpoint-events-request-example
- key_count: 2
  name: Amazon Pinpoint Export Jobs Response Example
  slug: amazon-pinpoint-export-jobs-response-example
- key_count: 17
  name: Amazon Pinpoint Gcm Message Example
  slug: amazon-pinpoint-gcm-message-example
- key_count: 1
  name: Amazon Pinpoint Get Adm Channel Response Example
  slug: amazon-pinpoint-get-adm-channel-response-example
- key_count: 1
  name: Amazon Pinpoint Get Apns Voip Channel Response Example
  slug: amazon-pinpoint-get-apns-voip-channel-response-example
- key_count: 1
  name: Amazon Pinpoint Get Apns Voip Sandbox Channel Response Example
  slug: amazon-pinpoint-get-apns-voip-sandbox-channel-response-example
- key_count: 1
  name: Amazon Pinpoint Get Campaign Activities Response Example
  slug: amazon-pinpoint-get-campaign-activities-response-example
- key_count: 1
  name: Amazon Pinpoint Get Campaign Response Example
  slug: amazon-pinpoint-get-campaign-response-example
- key_count: 1
  name: Amazon Pinpoint Get Campaigns Response Example
  slug: amazon-pinpoint-get-campaigns-response-example
- key_count: 1
  name: Amazon Pinpoint Get Email Template Response Example
  slug: amazon-pinpoint-get-email-template-response-example
- key_count: 1
  name: Amazon Pinpoint Get Gcm Channel Response Example
  slug: amazon-pinpoint-get-gcm-channel-response-example
- key_count: 1
  name: Amazon Pinpoint Get Import Jobs Response Example
  slug: amazon-pinpoint-get-import-jobs-response-example
- key_count: 1
  name: Amazon Pinpoint Get In App Messages Response Example
  slug: amazon-pinpoint-get-in-app-messages-response-example
- key_count: 1
  name: Amazon Pinpoint Get Push Template Response Example
  slug: amazon-pinpoint-get-push-template-response-example
- key_count: 1
  name: Amazon Pinpoint Get Recommender Configurations Response Example
  slug: amazon-pinpoint-get-recommender-configurations-response-example
- key_count: 1
  name: Amazon Pinpoint Get Segment Versions Response Example
  slug: amazon-pinpoint-get-segment-versions-response-example
- key_count: 1
  name: Amazon Pinpoint Get Sms Channel Response Example
  slug: amazon-pinpoint-get-sms-channel-response-example
- key_count: 2
  name: Amazon Pinpoint Gps Coordinates Example
  slug: amazon-pinpoint-gps-coordinates-example
- key_count: 2
  name: Amazon Pinpoint Holdout Activity Example
  slug: amazon-pinpoint-holdout-activity-example
- key_count: 8
  name: Amazon Pinpoint Import Job Resource Example
  slug: amazon-pinpoint-import-job-resource-example
- key_count: 1
  name: Amazon Pinpoint In App Messages Response Example
  slug: amazon-pinpoint-in-app-messages-response-example
- key_count: 1
  name: Amazon Pinpoint Journey Email Message Example
  slug: amazon-pinpoint-journey-email-message-example
- key_count: 6
  name: Amazon Pinpoint Journey Execution Activity Metrics Response Example
  slug: amazon-pinpoint-journey-execution-activity-metrics-response-example
- key_count: 4
  name: Amazon Pinpoint Journey Limits Example
  slug: amazon-pinpoint-journey-limits-example
- key_count: 1
  name: Amazon Pinpoint Journey State Request Example
  slug: amazon-pinpoint-journey-state-request-example
- key_count: 1
  name: Amazon Pinpoint List Journeys Response Example
  slug: amazon-pinpoint-list-journeys-response-example
- key_count: 2
  name: Amazon Pinpoint List Recommender Configurations Response Example
  slug: amazon-pinpoint-list-recommender-configurations-response-example
- key_count: 4
  name: Amazon Pinpoint Message Response Example
  slug: amazon-pinpoint-message-response-example
- key_count: 2
  name: Amazon Pinpoint Number Validate Request Example
  slug: amazon-pinpoint-number-validate-request-example
- key_count: 5
  name: Amazon Pinpoint Open Hours Example
  slug: amazon-pinpoint-open-hours-example
- key_count: 2
  name: Amazon Pinpoint Open Hours Rule Example
  slug: amazon-pinpoint-open-hours-rule-example
- key_count: 1
  name: Amazon Pinpoint Phone Number Validate Request Example
  slug: amazon-pinpoint-phone-number-validate-request-example
- key_count: 2
  name: Amazon Pinpoint Random Split Entry Example
  slug: amazon-pinpoint-random-split-entry-example
- key_count: 3
  name: Amazon Pinpoint Result Row Value Example
  slug: amazon-pinpoint-result-row-value-example
- key_count: 4
  name: Amazon Pinpoint Segment Group Example
  slug: amazon-pinpoint-segment-group-example
- key_count: 2
  name: Amazon Pinpoint Segment Location Example
  slug: amazon-pinpoint-segment-location-example
- key_count: 1
  name: Amazon Pinpoint Send Messages Request Example
  slug: amazon-pinpoint-send-messages-request-example
- key_count: 1
  name: Amazon Pinpoint Send Otp Message Request Example
  slug: amazon-pinpoint-send-otp-message-request-example
- key_count: 1
  name: Amazon Pinpoint Send Otp Message Response Example
  slug: amazon-pinpoint-send-otp-message-response-example
- key_count: 5
  name: Amazon Pinpoint Send Users Message Request Example
  slug: amazon-pinpoint-send-users-message-request-example
- key_count: 4
  name: Amazon Pinpoint Session Example
  slug: amazon-pinpoint-session-example
- key_count: 2
  name: Amazon Pinpoint Set Dimension Example
  slug: amazon-pinpoint-set-dimension-example
- key_count: 3
  name: Amazon Pinpoint Simple Condition Example
  slug: amazon-pinpoint-simple-condition-example
- key_count: 1
  name: Amazon Pinpoint Tag Resource Request Example
  slug: amazon-pinpoint-tag-resource-request-example
- key_count: 9
  name: Amazon Pinpoint Template Response Example
  slug: amazon-pinpoint-template-response-example
- key_count: 4
  name: Amazon Pinpoint Template Versions Response Example
  slug: amazon-pinpoint-template-versions-response-example
- key_count: 9
  name: Amazon Pinpoint Treatment Resource Example
  slug: amazon-pinpoint-treatment-resource-example
- key_count: 1
  name: Amazon Pinpoint Update Apns Channel Response Example
  slug: amazon-pinpoint-update-apns-channel-response-example
- key_count: 1
  name: Amazon Pinpoint Update Campaign Response Example
  slug: amazon-pinpoint-update-campaign-response-example
- key_count: 1
  name: Amazon Pinpoint Update Email Channel Request Example
  slug: amazon-pinpoint-update-email-channel-request-example
- key_count: 1
  name: Amazon Pinpoint Update Email Template Response Example
  slug: amazon-pinpoint-update-email-template-response-example
- key_count: 1
  name: Amazon Pinpoint Update In App Template Request Example
  slug: amazon-pinpoint-update-in-app-template-request-example
- key_count: 1
  name: Amazon Pinpoint Update Journey Response Example
  slug: amazon-pinpoint-update-journey-response-example
- key_count: 9
  name: Amazon Pinpoint Update Recommender Configuration Example
  slug: amazon-pinpoint-update-recommender-configuration-example
- key_count: 1
  name: Amazon Pinpoint Update Recommender Configuration Request Example
  slug: amazon-pinpoint-update-recommender-configuration-request-example
- key_count: 1
  name: Amazon Pinpoint Update Sms Template Request Example
  slug: amazon-pinpoint-update-sms-template-request-example
- key_count: 1
  name: Amazon Pinpoint Verify Otp Message Request Example
  slug: amazon-pinpoint-verify-otp-message-request-example
- key_count: 6
  name: Amazon Pinpoint Voice Template Request Example
  slug: amazon-pinpoint-voice-template-request-example
- key_count: 2
  name: Amazon Pinpoint Wait Time Example
  slug: amazon-pinpoint-wait-time-example
- key_count: 2
  name: Amazon Pinpoint Write Event Stream Example
  slug: amazon-pinpoint-write-event-stream-example
- key_count: 4
  name: Amazon Pinpoint Write Segment Request Example
  slug: amazon-pinpoint-write-segment-request-example
features:
- description: Send messages via email, SMS, push notifications, and voice through a unified API.
  name: Multi-Channel Messaging
- description: Create dynamic segments based on app data or import static segments from external sources.
  name: Audience Segmentation
- description: Schedule targeted campaigns with A/B testing and detailed analytics reporting.
  name: Messaging Campaigns
- description: Build multi-step automated engagement workflows triggered by customer events.
  name: Customer Journeys
- description: Send real-time transactional messages such as account confirmations, order updates, and password resets.
  name: Transactional Messaging
- description: Create reusable email, SMS, push, voice, and in-app message templates with personalization.
  name: Message Templates
- description: Track engagement trends, open rates, delivery rates, and campaign performance across all channels.
  name: Analytics and Metrics
- description: Manage customer endpoint profiles including device tokens, email addresses, and phone numbers.
  name: Endpoint Management
finops:
- name: Amazon Pinpoint Finops
  service_category: API
  slug: amazon-pinpoint-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Stream Pinpoint analytics data to Kinesis for real-time processing and external storage.
  name: Amazon Kinesis
- description: Import and export endpoint data and segment definitions using S3 bucket storage.
  name: Amazon S3
- description: Trigger Lambda functions from Pinpoint journey actions and campaign events.
  name: AWS Lambda
- description: Monitor Pinpoint service metrics and set alarms using CloudWatch.
  name: Amazon CloudWatch
- description: The successor service for SMS, voice, push, OTP, and phone number validation APIs continuing after Pinpoint deprecation.
  name: AWS End User Messaging
- description: Amazon Simple Email Service provides the email delivery infrastructure for Pinpoint email campaigns.
  name: Amazon SES
json_schemas:
- name: Action
  property_count: 0
  slug: amazon-pinpoint-action
- name: ActivitiesResponse
  property_count: 2
  slug: amazon-pinpoint-activities-response
- name: ActivityResponse
  property_count: 13
  slug: amazon-pinpoint-activity-response
- name: Activity
  property_count: 11
  slug: amazon-pinpoint-activity
- name: AddressConfiguration
  property_count: 6
  slug: amazon-pinpoint-address-configuration
- name: ADMChannelRequest
  property_count: 3
  slug: amazon-pinpoint-adm-channel-request
- name: ADMChannelResponse
  property_count: 10
  slug: amazon-pinpoint-adm-channel-response
- name: ADMMessage
  property_count: 16
  slug: amazon-pinpoint-adm-message
- name: Alignment
  property_count: 0
  slug: amazon-pinpoint-alignment
- name: AndroidPushNotificationTemplate
  property_count: 9
  slug: amazon-pinpoint-android-push-notification-template
- name: APNSChannelRequest
  property_count: 8
  slug: amazon-pinpoint-apns-channel-request
- name: APNSChannelResponse
  property_count: 12
  slug: amazon-pinpoint-apns-channel-response
- name: APNSMessage
  property_count: 18
  slug: amazon-pinpoint-apns-message
- name: APNSPushNotificationTemplate
  property_count: 7
  slug: amazon-pinpoint-apns-push-notification-template
- name: APNSSandboxChannelRequest
  property_count: 8
  slug: amazon-pinpoint-apns-sandbox-channel-request
- name: APNSSandboxChannelResponse
  property_count: 12
  slug: amazon-pinpoint-apns-sandbox-channel-response
- name: APNSVoipChannelRequest
  property_count: 8
  slug: amazon-pinpoint-apns-voip-channel-request
- name: APNSVoipChannelResponse
  property_count: 12
  slug: amazon-pinpoint-apns-voip-channel-response
- name: APNSVoipSandboxChannelRequest
  property_count: 8
  slug: amazon-pinpoint-apns-voip-sandbox-channel-request
- name: APNSVoipSandboxChannelResponse
  property_count: 12
  slug: amazon-pinpoint-apns-voip-sandbox-channel-response
- name: ApplicationDateRangeKpiResponse
  property_count: 6
  slug: amazon-pinpoint-application-date-range-kpi-response
- name: ApplicationResponse
  property_count: 5
  slug: amazon-pinpoint-application-response
- name: ApplicationSettingsResource
  property_count: 5
  slug: amazon-pinpoint-application-settings-resource
- name: ApplicationsResponse
  property_count: 2
  slug: amazon-pinpoint-applications-response
- name: AttributeDimension
  property_count: 2
  slug: amazon-pinpoint-attribute-dimension
- name: AttributeType
  property_count: 0
  slug: amazon-pinpoint-attribute-type
- name: AttributesResource
  property_count: 3
  slug: amazon-pinpoint-attributes-resource
- name: BaiduChannelRequest
  property_count: 3
  slug: amazon-pinpoint-baidu-channel-request
- name: BaiduChannelResponse
  property_count: 11
  slug: amazon-pinpoint-baidu-channel-response
- name: BaiduMessage
  property_count: 14
  slug: amazon-pinpoint-baidu-message
- name: BaseKpiResult
  property_count: 1
  slug: amazon-pinpoint-base-kpi-result
- name: ButtonAction
  property_count: 0
  slug: amazon-pinpoint-button-action
- name: CampaignCustomMessage
  property_count: 1
  slug: amazon-pinpoint-campaign-custom-message
- name: CampaignDateRangeKpiResponse
  property_count: 7
  slug: amazon-pinpoint-campaign-date-range-kpi-response
- name: CampaignEmailMessage
  property_count: 4
  slug: amazon-pinpoint-campaign-email-message
- name: CampaignEventFilter
  property_count: 2
  slug: amazon-pinpoint-campaign-event-filter
- name: CampaignHook
  property_count: 3
  slug: amazon-pinpoint-campaign-hook
- name: CampaignInAppMessage
  property_count: 4
  slug: amazon-pinpoint-campaign-in-app-message
- name: CampaignLimits
  property_count: 5
  slug: amazon-pinpoint-campaign-limits
- name: CampaignResponse
  property_count: 25
  slug: amazon-pinpoint-campaign-response
- name: CampaignSmsMessage
  property_count: 6
  slug: amazon-pinpoint-campaign-sms-message
- name: CampaignState
  property_count: 1
  slug: amazon-pinpoint-campaign-state
- name: CampaignStatus
  property_count: 0
  slug: amazon-pinpoint-campaign-status
- name: CampaignsResponse
  property_count: 2
  slug: amazon-pinpoint-campaigns-response
- name: ChannelResponse
  property_count: 9
  slug: amazon-pinpoint-channel-response
- name: ChannelType
  property_count: 0
  slug: amazon-pinpoint-channel-type
- name: ChannelsResponse
  property_count: 1
  slug: amazon-pinpoint-channels-response
- name: ClosedDaysRule
  property_count: 3
  slug: amazon-pinpoint-closed-days-rule
- name: ClosedDays
  property_count: 5
  slug: amazon-pinpoint-closed-days
- name: Condition
  property_count: 2
  slug: amazon-pinpoint-condition
- name: ConditionalSplitActivity
  property_count: 4
  slug: amazon-pinpoint-conditional-split-activity
- name: ContactCenterActivity
  property_count: 1
  slug: amazon-pinpoint-contact-center-activity
- name: CreateAppRequest
  property_count: 1
  slug: amazon-pinpoint-create-app-request
- name: CreateAppResponse
  property_count: 1
  slug: amazon-pinpoint-create-app-response
- name: CreateApplicationRequest
  property_count: 2
  slug: amazon-pinpoint-create-application-request
- name: CreateCampaignRequest
  property_count: 1
  slug: amazon-pinpoint-create-campaign-request
- name: CreateCampaignResponse
  property_count: 1
  slug: amazon-pinpoint-create-campaign-response
- name: CreateEmailTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-create-email-template-request
- name: CreateEmailTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-create-email-template-response
- name: CreateExportJobRequest
  property_count: 1
  slug: amazon-pinpoint-create-export-job-request
- name: CreateExportJobResponse
  property_count: 1
  slug: amazon-pinpoint-create-export-job-response
- name: CreateImportJobRequest
  property_count: 1
  slug: amazon-pinpoint-create-import-job-request
- name: CreateImportJobResponse
  property_count: 1
  slug: amazon-pinpoint-create-import-job-response
- name: CreateInAppTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-create-in-app-template-request
- name: CreateInAppTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-create-in-app-template-response
- name: CreateJourneyRequest
  property_count: 1
  slug: amazon-pinpoint-create-journey-request
- name: CreateJourneyResponse
  property_count: 1
  slug: amazon-pinpoint-create-journey-response
- name: CreatePushTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-create-push-template-request
- name: CreatePushTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-create-push-template-response
- name: CreateRecommenderConfigurationRequest
  property_count: 1
  slug: amazon-pinpoint-create-recommender-configuration-request
- name: CreateRecommenderConfigurationResponse
  property_count: 1
  slug: amazon-pinpoint-create-recommender-configuration-response
- name: CreateRecommenderConfiguration
  property_count: 9
  slug: amazon-pinpoint-create-recommender-configuration
- name: CreateSegmentRequest
  property_count: 1
  slug: amazon-pinpoint-create-segment-request
- name: CreateSegmentResponse
  property_count: 1
  slug: amazon-pinpoint-create-segment-response
- name: CreateSmsTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-create-sms-template-request
- name: CreateSmsTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-create-sms-template-response
- name: CreateTemplateMessageBody
  property_count: 3
  slug: amazon-pinpoint-create-template-message-body
- name: CreateVoiceTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-create-voice-template-request
- name: CreateVoiceTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-create-voice-template-response
- name: CustomDeliveryConfiguration
  property_count: 2
  slug: amazon-pinpoint-custom-delivery-configuration
- name: CustomMessageActivity
  property_count: 6
  slug: amazon-pinpoint-custom-message-activity
- name: DayOfWeek
  property_count: 0
  slug: amazon-pinpoint-day-of-week
- name: DefaultButtonConfiguration
  property_count: 6
  slug: amazon-pinpoint-default-button-configuration
- name: DefaultMessage
  property_count: 2
  slug: amazon-pinpoint-default-message
- name: DefaultPushNotificationMessage
  property_count: 7
  slug: amazon-pinpoint-default-push-notification-message
- name: DefaultPushNotificationTemplate
  property_count: 5
  slug: amazon-pinpoint-default-push-notification-template
- name: DeleteAdmChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-adm-channel-request
- name: DeleteAdmChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-adm-channel-response
- name: DeleteApnsChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-apns-channel-request
- name: DeleteApnsChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-apns-channel-response
- name: DeleteApnsSandboxChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-apns-sandbox-channel-request
- name: DeleteApnsSandboxChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-apns-sandbox-channel-response
- name: DeleteApnsVoipChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-apns-voip-channel-request
- name: DeleteApnsVoipChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-apns-voip-channel-response
- name: DeleteApnsVoipSandboxChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-apns-voip-sandbox-channel-request
- name: DeleteApnsVoipSandboxChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-apns-voip-sandbox-channel-response
- name: DeleteAppRequest
  property_count: 0
  slug: amazon-pinpoint-delete-app-request
- name: DeleteAppResponse
  property_count: 1
  slug: amazon-pinpoint-delete-app-response
- name: DeleteBaiduChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-baidu-channel-request
- name: DeleteBaiduChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-baidu-channel-response
- name: DeleteCampaignRequest
  property_count: 0
  slug: amazon-pinpoint-delete-campaign-request
- name: DeleteCampaignResponse
  property_count: 1
  slug: amazon-pinpoint-delete-campaign-response
- name: DeleteEmailChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-email-channel-request
- name: DeleteEmailChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-email-channel-response
- name: DeleteEmailTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-delete-email-template-request
- name: DeleteEmailTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-delete-email-template-response
- name: DeleteEndpointRequest
  property_count: 0
  slug: amazon-pinpoint-delete-endpoint-request
- name: DeleteEndpointResponse
  property_count: 1
  slug: amazon-pinpoint-delete-endpoint-response
- name: DeleteEventStreamRequest
  property_count: 0
  slug: amazon-pinpoint-delete-event-stream-request
- name: DeleteEventStreamResponse
  property_count: 1
  slug: amazon-pinpoint-delete-event-stream-response
- name: DeleteGcmChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-gcm-channel-request
- name: DeleteGcmChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-gcm-channel-response
- name: DeleteInAppTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-delete-in-app-template-request
- name: DeleteInAppTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-delete-in-app-template-response
- name: DeleteJourneyRequest
  property_count: 0
  slug: amazon-pinpoint-delete-journey-request
- name: DeleteJourneyResponse
  property_count: 1
  slug: amazon-pinpoint-delete-journey-response
- name: DeletePushTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-delete-push-template-request
- name: DeletePushTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-delete-push-template-response
- name: DeleteRecommenderConfigurationRequest
  property_count: 0
  slug: amazon-pinpoint-delete-recommender-configuration-request
- name: DeleteRecommenderConfigurationResponse
  property_count: 1
  slug: amazon-pinpoint-delete-recommender-configuration-response
- name: DeleteSegmentRequest
  property_count: 0
  slug: amazon-pinpoint-delete-segment-request
- name: DeleteSegmentResponse
  property_count: 1
  slug: amazon-pinpoint-delete-segment-response
- name: DeleteSmsChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-sms-channel-request
- name: DeleteSmsChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-sms-channel-response
- name: DeleteSmsTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-delete-sms-template-request
- name: DeleteSmsTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-delete-sms-template-response
- name: DeleteUserEndpointsRequest
  property_count: 0
  slug: amazon-pinpoint-delete-user-endpoints-request
- name: DeleteUserEndpointsResponse
  property_count: 1
  slug: amazon-pinpoint-delete-user-endpoints-response
- name: DeleteVoiceChannelRequest
  property_count: 0
  slug: amazon-pinpoint-delete-voice-channel-request
- name: DeleteVoiceChannelResponse
  property_count: 1
  slug: amazon-pinpoint-delete-voice-channel-response
- name: DeleteVoiceTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-delete-voice-template-request
- name: DeleteVoiceTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-delete-voice-template-response
- name: DeliveryStatus
  property_count: 0
  slug: amazon-pinpoint-delivery-status
- name: DirectMessageConfiguration
  property_count: 9
  slug: amazon-pinpoint-direct-message-configuration
- name: Duration
  property_count: 0
  slug: amazon-pinpoint-duration
- name: EmailChannelRequest
  property_count: 5
  slug: amazon-pinpoint-email-channel-request
- name: EmailChannelResponse
  property_count: 15
  slug: amazon-pinpoint-email-channel-response
- name: EmailMessageActivity
  property_count: 4
  slug: amazon-pinpoint-email-message-activity
- name: EmailMessage
  property_count: 7
  slug: amazon-pinpoint-email-message
- name: EmailTemplateRequest
  property_count: 7
  slug: amazon-pinpoint-email-template-request
- name: EmailTemplateResponse
  property_count: 13
  slug: amazon-pinpoint-email-template-response
- name: EndpointBatchItem
  property_count: 12
  slug: amazon-pinpoint-endpoint-batch-item
- name: EndpointBatchRequest
  property_count: 1
  slug: amazon-pinpoint-endpoint-batch-request
- name: EndpointDemographic
  property_count: 8
  slug: amazon-pinpoint-endpoint-demographic
- name: EndpointItemResponse
  property_count: 2
  slug: amazon-pinpoint-endpoint-item-response
- name: EndpointLocation
  property_count: 6
  slug: amazon-pinpoint-endpoint-location
- name: EndpointMessageResult
  property_count: 6
  slug: amazon-pinpoint-endpoint-message-result
- name: EndpointRequest
  property_count: 11
  slug: amazon-pinpoint-endpoint-request
- name: EndpointResponse
  property_count: 15
  slug: amazon-pinpoint-endpoint-response
- name: EndpointSendConfiguration
  property_count: 5
  slug: amazon-pinpoint-endpoint-send-configuration
- name: EndpointUser
  property_count: 2
  slug: amazon-pinpoint-endpoint-user
- name: EndpointsResponse
  property_count: 1
  slug: amazon-pinpoint-endpoints-response
- name: EventCondition
  property_count: 2
  slug: amazon-pinpoint-event-condition
- name: EventDimensions
  property_count: 3
  slug: amazon-pinpoint-event-dimensions
- name: EventFilter
  property_count: 2
  slug: amazon-pinpoint-event-filter
- name: EventItemResponse
  property_count: 2
  slug: amazon-pinpoint-event-item-response
- name: Event
  property_count: 10
  slug: amazon-pinpoint-event
- name: EventStartCondition
  property_count: 2
  slug: amazon-pinpoint-event-start-condition
- name: EventStream
  property_count: 6
  slug: amazon-pinpoint-event-stream
- name: EventsBatch
  property_count: 2
  slug: amazon-pinpoint-events-batch
- name: EventsRequest
  property_count: 1
  slug: amazon-pinpoint-events-request
- name: EventsResponse
  property_count: 1
  slug: amazon-pinpoint-events-response
- name: ExportJobRequest
  property_count: 4
  slug: amazon-pinpoint-export-job-request
- name: ExportJobResource
  property_count: 4
  slug: amazon-pinpoint-export-job-resource
- name: ExportJobResponse
  property_count: 13
  slug: amazon-pinpoint-export-job-response
- name: ExportJobsResponse
  property_count: 2
  slug: amazon-pinpoint-export-jobs-response
- name: Frequency
  property_count: 0
  slug: amazon-pinpoint-frequency
- name: GCMChannelRequest
  property_count: 2
  slug: amazon-pinpoint-gcm-channel-request
- name: GCMChannelResponse
  property_count: 11
  slug: amazon-pinpoint-gcm-channel-response
- name: GCMMessage
  property_count: 17
  slug: amazon-pinpoint-gcm-message
- name: GetAdmChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-adm-channel-request
- name: GetAdmChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-adm-channel-response
- name: GetApnsChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-apns-channel-request
- name: GetApnsChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-apns-channel-response
- name: GetApnsSandboxChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-apns-sandbox-channel-request
- name: GetApnsSandboxChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-apns-sandbox-channel-response
- name: GetApnsVoipChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-apns-voip-channel-request
- name: GetApnsVoipChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-apns-voip-channel-response
- name: GetApnsVoipSandboxChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-apns-voip-sandbox-channel-request
- name: GetApnsVoipSandboxChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-apns-voip-sandbox-channel-response
- name: GetAppRequest
  property_count: 0
  slug: amazon-pinpoint-get-app-request
- name: GetAppResponse
  property_count: 1
  slug: amazon-pinpoint-get-app-response
- name: GetApplicationDateRangeKpiRequest
  property_count: 0
  slug: amazon-pinpoint-get-application-date-range-kpi-request
- name: GetApplicationDateRangeKpiResponse
  property_count: 1
  slug: amazon-pinpoint-get-application-date-range-kpi-response
- name: GetApplicationSettingsRequest
  property_count: 0
  slug: amazon-pinpoint-get-application-settings-request
- name: GetApplicationSettingsResponse
  property_count: 1
  slug: amazon-pinpoint-get-application-settings-response
- name: GetAppsRequest
  property_count: 0
  slug: amazon-pinpoint-get-apps-request
- name: GetAppsResponse
  property_count: 1
  slug: amazon-pinpoint-get-apps-response
- name: GetBaiduChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-baidu-channel-request
- name: GetBaiduChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-baidu-channel-response
- name: GetCampaignActivitiesRequest
  property_count: 0
  slug: amazon-pinpoint-get-campaign-activities-request
- name: GetCampaignActivitiesResponse
  property_count: 1
  slug: amazon-pinpoint-get-campaign-activities-response
- name: GetCampaignDateRangeKpiRequest
  property_count: 0
  slug: amazon-pinpoint-get-campaign-date-range-kpi-request
- name: GetCampaignDateRangeKpiResponse
  property_count: 1
  slug: amazon-pinpoint-get-campaign-date-range-kpi-response
- name: GetCampaignRequest
  property_count: 0
  slug: amazon-pinpoint-get-campaign-request
- name: GetCampaignResponse
  property_count: 1
  slug: amazon-pinpoint-get-campaign-response
- name: GetCampaignVersionRequest
  property_count: 0
  slug: amazon-pinpoint-get-campaign-version-request
- name: GetCampaignVersionResponse
  property_count: 1
  slug: amazon-pinpoint-get-campaign-version-response
- name: GetCampaignVersionsRequest
  property_count: 0
  slug: amazon-pinpoint-get-campaign-versions-request
- name: GetCampaignVersionsResponse
  property_count: 1
  slug: amazon-pinpoint-get-campaign-versions-response
- name: GetCampaignsRequest
  property_count: 0
  slug: amazon-pinpoint-get-campaigns-request
- name: GetCampaignsResponse
  property_count: 1
  slug: amazon-pinpoint-get-campaigns-response
- name: GetChannelsRequest
  property_count: 0
  slug: amazon-pinpoint-get-channels-request
- name: GetChannelsResponse
  property_count: 1
  slug: amazon-pinpoint-get-channels-response
- name: GetEmailChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-email-channel-request
- name: GetEmailChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-email-channel-response
- name: GetEmailTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-get-email-template-request
- name: GetEmailTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-get-email-template-response
- name: GetEndpointRequest
  property_count: 0
  slug: amazon-pinpoint-get-endpoint-request
- name: GetEndpointResponse
  property_count: 1
  slug: amazon-pinpoint-get-endpoint-response
- name: GetEventStreamRequest
  property_count: 0
  slug: amazon-pinpoint-get-event-stream-request
- name: GetEventStreamResponse
  property_count: 1
  slug: amazon-pinpoint-get-event-stream-response
- name: GetExportJobRequest
  property_count: 0
  slug: amazon-pinpoint-get-export-job-request
- name: GetExportJobResponse
  property_count: 1
  slug: amazon-pinpoint-get-export-job-response
- name: GetExportJobsRequest
  property_count: 0
  slug: amazon-pinpoint-get-export-jobs-request
- name: GetExportJobsResponse
  property_count: 1
  slug: amazon-pinpoint-get-export-jobs-response
- name: GetGcmChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-gcm-channel-request
- name: GetGcmChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-gcm-channel-response
- name: GetImportJobRequest
  property_count: 0
  slug: amazon-pinpoint-get-import-job-request
- name: GetImportJobResponse
  property_count: 1
  slug: amazon-pinpoint-get-import-job-response
- name: GetImportJobsRequest
  property_count: 0
  slug: amazon-pinpoint-get-import-jobs-request
- name: GetImportJobsResponse
  property_count: 1
  slug: amazon-pinpoint-get-import-jobs-response
- name: GetInAppMessagesRequest
  property_count: 0
  slug: amazon-pinpoint-get-in-app-messages-request
- name: GetInAppMessagesResponse
  property_count: 1
  slug: amazon-pinpoint-get-in-app-messages-response
- name: GetInAppTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-get-in-app-template-request
- name: GetInAppTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-get-in-app-template-response
- name: GetJourneyDateRangeKpiRequest
  property_count: 0
  slug: amazon-pinpoint-get-journey-date-range-kpi-request
- name: GetJourneyDateRangeKpiResponse
  property_count: 1
  slug: amazon-pinpoint-get-journey-date-range-kpi-response
- name: GetJourneyExecutionActivityMetricsRequest
  property_count: 0
  slug: amazon-pinpoint-get-journey-execution-activity-metrics-request
- name: GetJourneyExecutionActivityMetricsResponse
  property_count: 1
  slug: amazon-pinpoint-get-journey-execution-activity-metrics-response
- name: GetJourneyExecutionMetricsRequest
  property_count: 0
  slug: amazon-pinpoint-get-journey-execution-metrics-request
- name: GetJourneyExecutionMetricsResponse
  property_count: 1
  slug: amazon-pinpoint-get-journey-execution-metrics-response
- name: GetJourneyRequest
  property_count: 0
  slug: amazon-pinpoint-get-journey-request
- name: GetJourneyResponse
  property_count: 1
  slug: amazon-pinpoint-get-journey-response
- name: GetPushTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-get-push-template-request
- name: GetPushTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-get-push-template-response
- name: GetRecommenderConfigurationRequest
  property_count: 0
  slug: amazon-pinpoint-get-recommender-configuration-request
- name: GetRecommenderConfigurationResponse
  property_count: 1
  slug: amazon-pinpoint-get-recommender-configuration-response
- name: GetRecommenderConfigurationsRequest
  property_count: 0
  slug: amazon-pinpoint-get-recommender-configurations-request
- name: GetRecommenderConfigurationsResponse
  property_count: 1
  slug: amazon-pinpoint-get-recommender-configurations-response
- name: GetSegmentExportJobsRequest
  property_count: 0
  slug: amazon-pinpoint-get-segment-export-jobs-request
- name: GetSegmentExportJobsResponse
  property_count: 1
  slug: amazon-pinpoint-get-segment-export-jobs-response
- name: GetSegmentImportJobsRequest
  property_count: 0
  slug: amazon-pinpoint-get-segment-import-jobs-request
- name: GetSegmentImportJobsResponse
  property_count: 1
  slug: amazon-pinpoint-get-segment-import-jobs-response
- name: GetSegmentRequest
  property_count: 0
  slug: amazon-pinpoint-get-segment-request
- name: GetSegmentResponse
  property_count: 1
  slug: amazon-pinpoint-get-segment-response
- name: GetSegmentVersionRequest
  property_count: 0
  slug: amazon-pinpoint-get-segment-version-request
- name: GetSegmentVersionResponse
  property_count: 1
  slug: amazon-pinpoint-get-segment-version-response
- name: GetSegmentVersionsRequest
  property_count: 0
  slug: amazon-pinpoint-get-segment-versions-request
- name: GetSegmentVersionsResponse
  property_count: 1
  slug: amazon-pinpoint-get-segment-versions-response
- name: GetSegmentsRequest
  property_count: 0
  slug: amazon-pinpoint-get-segments-request
- name: GetSegmentsResponse
  property_count: 1
  slug: amazon-pinpoint-get-segments-response
- name: GetSmsChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-sms-channel-request
- name: GetSmsChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-sms-channel-response
- name: GetSmsTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-get-sms-template-request
- name: GetSmsTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-get-sms-template-response
- name: GetUserEndpointsRequest
  property_count: 0
  slug: amazon-pinpoint-get-user-endpoints-request
- name: GetUserEndpointsResponse
  property_count: 1
  slug: amazon-pinpoint-get-user-endpoints-response
- name: GetVoiceChannelRequest
  property_count: 0
  slug: amazon-pinpoint-get-voice-channel-request
- name: GetVoiceChannelResponse
  property_count: 1
  slug: amazon-pinpoint-get-voice-channel-response
- name: GetVoiceTemplateRequest
  property_count: 0
  slug: amazon-pinpoint-get-voice-template-request
- name: GetVoiceTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-get-voice-template-response
- name: GPSCoordinates
  property_count: 2
  slug: amazon-pinpoint-gps-coordinates
- name: GPSPointDimension
  property_count: 2
  slug: amazon-pinpoint-gps-point-dimension
- name: HoldoutActivity
  property_count: 2
  slug: amazon-pinpoint-holdout-activity
- name: ImportJobRequest
  property_count: 8
  slug: amazon-pinpoint-import-job-request
- name: ImportJobResource
  property_count: 8
  slug: amazon-pinpoint-import-job-resource
- name: ImportJobResponse
  property_count: 13
  slug: amazon-pinpoint-import-job-response
- name: ImportJobsResponse
  property_count: 2
  slug: amazon-pinpoint-import-jobs-response
- name: InAppCampaignSchedule
  property_count: 3
  slug: amazon-pinpoint-in-app-campaign-schedule
- name: InAppMessageBodyConfig
  property_count: 3
  slug: amazon-pinpoint-in-app-message-body-config
- name: InAppMessageButton
  property_count: 4
  slug: amazon-pinpoint-in-app-message-button
- name: InAppMessageCampaign
  property_count: 8
  slug: amazon-pinpoint-in-app-message-campaign
- name: InAppMessageContent
  property_count: 6
  slug: amazon-pinpoint-in-app-message-content
- name: InAppMessageHeaderConfig
  property_count: 3
  slug: amazon-pinpoint-in-app-message-header-config
- name: InAppMessage
  property_count: 3
  slug: amazon-pinpoint-in-app-message
- name: InAppMessagesResponse
  property_count: 1
  slug: amazon-pinpoint-in-app-messages-response
- name: InAppTemplateRequest
  property_count: 5
  slug: amazon-pinpoint-in-app-template-request
- name: InAppTemplateResponse
  property_count: 11
  slug: amazon-pinpoint-in-app-template-response
- name: Include
  property_count: 0
  slug: amazon-pinpoint-include
- name: ItemResponse
  property_count: 2
  slug: amazon-pinpoint-item-response
- name: JobStatus
  property_count: 0
  slug: amazon-pinpoint-job-status
- name: JourneyChannelSettings
  property_count: 2
  slug: amazon-pinpoint-journey-channel-settings
- name: JourneyCustomMessage
  property_count: 1
  slug: amazon-pinpoint-journey-custom-message
- name: JourneyDateRangeKpiResponse
  property_count: 7
  slug: amazon-pinpoint-journey-date-range-kpi-response
- name: JourneyEmailMessage
  property_count: 1
  slug: amazon-pinpoint-journey-email-message
- name: JourneyExecutionActivityMetricsResponse
  property_count: 6
  slug: amazon-pinpoint-journey-execution-activity-metrics-response
- name: JourneyExecutionMetricsResponse
  property_count: 4
  slug: amazon-pinpoint-journey-execution-metrics-response
- name: JourneyLimits
  property_count: 4
  slug: amazon-pinpoint-journey-limits
- name: JourneyPushMessage
  property_count: 1
  slug: amazon-pinpoint-journey-push-message
- name: JourneyResponse
  property_count: 21
  slug: amazon-pinpoint-journey-response
- name: JourneySchedule
  property_count: 3
  slug: amazon-pinpoint-journey-schedule
- name: JourneySMSMessage
  property_count: 5
  slug: amazon-pinpoint-journey-sms-message
- name: JourneyStateRequest
  property_count: 1
  slug: amazon-pinpoint-journey-state-request
- name: JourneysResponse
  property_count: 2
  slug: amazon-pinpoint-journeys-response
- name: Layout
  property_count: 0
  slug: amazon-pinpoint-layout
- name: ListJourneysRequest
  property_count: 0
  slug: amazon-pinpoint-list-journeys-request
- name: ListJourneysResponse
  property_count: 1
  slug: amazon-pinpoint-list-journeys-response
- name: ListRecommenderConfigurationsResponse
  property_count: 2
  slug: amazon-pinpoint-list-recommender-configurations-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: amazon-pinpoint-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-pinpoint-list-tags-for-resource-response
- name: ListTemplateVersionsRequest
  property_count: 0
  slug: amazon-pinpoint-list-template-versions-request
- name: ListTemplateVersionsResponse
  property_count: 1
  slug: amazon-pinpoint-list-template-versions-response
- name: ListTemplatesRequest
  property_count: 0
  slug: amazon-pinpoint-list-templates-request
- name: ListTemplatesResponse
  property_count: 1
  slug: amazon-pinpoint-list-templates-response
- name: MessageConfiguration
  property_count: 9
  slug: amazon-pinpoint-message-configuration
- name: MessageRequest
  property_count: 6
  slug: amazon-pinpoint-message-request
- name: MessageResponse
  property_count: 4
  slug: amazon-pinpoint-message-response
- name: MessageResult
  property_count: 5
  slug: amazon-pinpoint-message-result
- name: Message
  property_count: 12
  slug: amazon-pinpoint-message
- name: MetricDimension
  property_count: 2
  slug: amazon-pinpoint-metric-dimension
- name: MultiConditionalBranch
  property_count: 2
  slug: amazon-pinpoint-multi-conditional-branch
- name: MultiConditionalSplitActivity
  property_count: 3
  slug: amazon-pinpoint-multi-conditional-split-activity
- name: NumberValidateRequest
  property_count: 2
  slug: amazon-pinpoint-number-validate-request
- name: NumberValidateResponse
  property_count: 14
  slug: amazon-pinpoint-number-validate-response
- name: OpenHoursRule
  property_count: 2
  slug: amazon-pinpoint-open-hours-rule
- name: OpenHours
  property_count: 5
  slug: amazon-pinpoint-open-hours
- name: OverrideButtonConfiguration
  property_count: 2
  slug: amazon-pinpoint-override-button-configuration
- name: PhoneNumberValidateRequest
  property_count: 1
  slug: amazon-pinpoint-phone-number-validate-request
- name: PhoneNumberValidateResponse
  property_count: 1
  slug: amazon-pinpoint-phone-number-validate-response
- name: PublicEndpoint
  property_count: 11
  slug: amazon-pinpoint-public-endpoint
- name: PushMessageActivity
  property_count: 4
  slug: amazon-pinpoint-push-message-activity
- name: PushNotificationTemplateRequest
  property_count: 9
  slug: amazon-pinpoint-push-notification-template-request
- name: PushNotificationTemplateResponse
  property_count: 15
  slug: amazon-pinpoint-push-notification-template-response
- name: PutEventStreamRequest
  property_count: 1
  slug: amazon-pinpoint-put-event-stream-request
- name: PutEventStreamResponse
  property_count: 1
  slug: amazon-pinpoint-put-event-stream-response
- name: PutEventsRequest
  property_count: 1
  slug: amazon-pinpoint-put-events-request
- name: PutEventsResponse
  property_count: 1
  slug: amazon-pinpoint-put-events-response
- name: QuietTime
  property_count: 2
  slug: amazon-pinpoint-quiet-time
- name: RandomSplitActivity
  property_count: 1
  slug: amazon-pinpoint-random-split-activity
- name: RandomSplitEntry
  property_count: 2
  slug: amazon-pinpoint-random-split-entry
- name: RawEmail
  property_count: 1
  slug: amazon-pinpoint-raw-email
- name: RecencyDimension
  property_count: 2
  slug: amazon-pinpoint-recency-dimension
- name: RecommenderConfigurationResponse
  property_count: 12
  slug: amazon-pinpoint-recommender-configuration-response
- name: RemoveAttributesRequest
  property_count: 1
  slug: amazon-pinpoint-remove-attributes-request
- name: RemoveAttributesResponse
  property_count: 1
  slug: amazon-pinpoint-remove-attributes-response
- name: ResultRow
  property_count: 2
  slug: amazon-pinpoint-result-row
- name: ResultRowValue
  property_count: 3
  slug: amazon-pinpoint-result-row-value
- name: Schedule
  property_count: 7
  slug: amazon-pinpoint-schedule
- name: Amazon Pinpoint Application Definition
  property_count: 8
  slug: amazon-pinpoint
- name: SegmentBehaviors
  property_count: 1
  slug: amazon-pinpoint-segment-behaviors
- name: SegmentCondition
  property_count: 1
  slug: amazon-pinpoint-segment-condition
- name: SegmentDemographics
  property_count: 6
  slug: amazon-pinpoint-segment-demographics
- name: SegmentDimensions
  property_count: 6
  slug: amazon-pinpoint-segment-dimensions
- name: SegmentGroupList
  property_count: 2
  slug: amazon-pinpoint-segment-group-list
- name: SegmentGroup
  property_count: 4
  slug: amazon-pinpoint-segment-group
- name: SegmentImportResource
  property_count: 6
  slug: amazon-pinpoint-segment-import-resource
- name: SegmentLocation
  property_count: 2
  slug: amazon-pinpoint-segment-location
- name: SegmentReference
  property_count: 2
  slug: amazon-pinpoint-segment-reference
- name: SegmentResponse
  property_count: 12
  slug: amazon-pinpoint-segment-response
- name: SegmentsResponse
  property_count: 2
  slug: amazon-pinpoint-segments-response
- name: SendMessagesRequest
  property_count: 1
  slug: amazon-pinpoint-send-messages-request
- name: SendMessagesResponse
  property_count: 1
  slug: amazon-pinpoint-send-messages-response
- name: SendOTPMessageRequestParameters
  property_count: 11
  slug: amazon-pinpoint-send-otp-message-request-parameters
- name: SendOTPMessageRequest
  property_count: 1
  slug: amazon-pinpoint-send-otp-message-request
- name: SendOTPMessageResponse
  property_count: 1
  slug: amazon-pinpoint-send-otp-message-response
- name: SendUsersMessageRequest
  property_count: 5
  slug: amazon-pinpoint-send-users-message-request
- name: SendUsersMessageResponse
  property_count: 3
  slug: amazon-pinpoint-send-users-message-response
- name: SendUsersMessagesRequest
  property_count: 1
  slug: amazon-pinpoint-send-users-messages-request
- name: SendUsersMessagesResponse
  property_count: 1
  slug: amazon-pinpoint-send-users-messages-response
- name: Session
  property_count: 4
  slug: amazon-pinpoint-session
- name: SetDimension
  property_count: 2
  slug: amazon-pinpoint-set-dimension
- name: SimpleCondition
  property_count: 3
  slug: amazon-pinpoint-simple-condition
- name: SimpleEmailPart
  property_count: 2
  slug: amazon-pinpoint-simple-email-part
- name: SimpleEmail
  property_count: 3
  slug: amazon-pinpoint-simple-email
- name: SMSChannelRequest
  property_count: 3
  slug: amazon-pinpoint-sms-channel-request
- name: SMSChannelResponse
  property_count: 14
  slug: amazon-pinpoint-sms-channel-response
- name: SMSMessageActivity
  property_count: 4
  slug: amazon-pinpoint-sms-message-activity
- name: SMSMessage
  property_count: 9
  slug: amazon-pinpoint-sms-message
- name: SMSTemplateRequest
  property_count: 5
  slug: amazon-pinpoint-sms-template-request
- name: SMSTemplateResponse
  property_count: 11
  slug: amazon-pinpoint-sms-template-response
- name: SourceType
  property_count: 0
  slug: amazon-pinpoint-source-type
- name: StartCondition
  property_count: 3
  slug: amazon-pinpoint-start-condition
- name: State
  property_count: 0
  slug: amazon-pinpoint-state
- name: TagResourceRequest
  property_count: 1
  slug: amazon-pinpoint-tag-resource-request
- name: TagsModel
  property_count: 1
  slug: amazon-pinpoint-tags-model
- name: TemplateActiveVersionRequest
  property_count: 1
  slug: amazon-pinpoint-template-active-version-request
- name: TemplateConfiguration
  property_count: 4
  slug: amazon-pinpoint-template-configuration
- name: TemplateCreateMessageBody
  property_count: 3
  slug: amazon-pinpoint-template-create-message-body
- name: TemplateResponse
  property_count: 9
  slug: amazon-pinpoint-template-response
- name: Template
  property_count: 2
  slug: amazon-pinpoint-template
- name: TemplateType
  property_count: 0
  slug: amazon-pinpoint-template-type
- name: TemplateVersionResponse
  property_count: 7
  slug: amazon-pinpoint-template-version-response
- name: TemplateVersionsResponse
  property_count: 4
  slug: amazon-pinpoint-template-versions-response
- name: TemplatesResponse
  property_count: 2
  slug: amazon-pinpoint-templates-response
- name: TreatmentResource
  property_count: 9
  slug: amazon-pinpoint-treatment-resource
- name: Type
  property_count: 0
  slug: amazon-pinpoint-type
- name: UntagResourceRequest
  property_count: 0
  slug: amazon-pinpoint-untag-resource-request
- name: UpdateAdmChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-adm-channel-request
- name: UpdateAdmChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-adm-channel-response
- name: UpdateApnsChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-apns-channel-request
- name: UpdateApnsChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-apns-channel-response
- name: UpdateApnsSandboxChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-apns-sandbox-channel-request
- name: UpdateApnsSandboxChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-apns-sandbox-channel-response
- name: UpdateApnsVoipChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-apns-voip-channel-request
- name: UpdateApnsVoipChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-apns-voip-channel-response
- name: UpdateApnsVoipSandboxChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-apns-voip-sandbox-channel-request
- name: UpdateApnsVoipSandboxChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-apns-voip-sandbox-channel-response
- name: UpdateApplicationSettingsRequest
  property_count: 1
  slug: amazon-pinpoint-update-application-settings-request
- name: UpdateApplicationSettingsResponse
  property_count: 1
  slug: amazon-pinpoint-update-application-settings-response
- name: UpdateAttributesRequest
  property_count: 1
  slug: amazon-pinpoint-update-attributes-request
- name: UpdateBaiduChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-baidu-channel-request
- name: UpdateBaiduChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-baidu-channel-response
- name: UpdateCampaignRequest
  property_count: 1
  slug: amazon-pinpoint-update-campaign-request
- name: UpdateCampaignResponse
  property_count: 1
  slug: amazon-pinpoint-update-campaign-response
- name: UpdateEmailChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-email-channel-request
- name: UpdateEmailChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-email-channel-response
- name: UpdateEmailTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-update-email-template-request
- name: UpdateEmailTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-update-email-template-response
- name: UpdateEndpointRequest
  property_count: 1
  slug: amazon-pinpoint-update-endpoint-request
- name: UpdateEndpointResponse
  property_count: 1
  slug: amazon-pinpoint-update-endpoint-response
- name: UpdateEndpointsBatchRequest
  property_count: 1
  slug: amazon-pinpoint-update-endpoints-batch-request
- name: UpdateEndpointsBatchResponse
  property_count: 1
  slug: amazon-pinpoint-update-endpoints-batch-response
- name: UpdateGcmChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-gcm-channel-request
- name: UpdateGcmChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-gcm-channel-response
- name: UpdateInAppTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-update-in-app-template-request
- name: UpdateInAppTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-update-in-app-template-response
- name: UpdateJourneyRequest
  property_count: 1
  slug: amazon-pinpoint-update-journey-request
- name: UpdateJourneyResponse
  property_count: 1
  slug: amazon-pinpoint-update-journey-response
- name: UpdateJourneyStateRequest
  property_count: 1
  slug: amazon-pinpoint-update-journey-state-request
- name: UpdateJourneyStateResponse
  property_count: 1
  slug: amazon-pinpoint-update-journey-state-response
- name: UpdatePushTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-update-push-template-request
- name: UpdatePushTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-update-push-template-response
- name: UpdateRecommenderConfigurationRequest
  property_count: 1
  slug: amazon-pinpoint-update-recommender-configuration-request
- name: UpdateRecommenderConfigurationResponse
  property_count: 1
  slug: amazon-pinpoint-update-recommender-configuration-response
- name: UpdateRecommenderConfiguration
  property_count: 9
  slug: amazon-pinpoint-update-recommender-configuration
- name: UpdateSegmentRequest
  property_count: 1
  slug: amazon-pinpoint-update-segment-request
- name: UpdateSegmentResponse
  property_count: 1
  slug: amazon-pinpoint-update-segment-response
- name: UpdateSmsChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-sms-channel-request
- name: UpdateSmsChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-sms-channel-response
- name: UpdateSmsTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-update-sms-template-request
- name: UpdateSmsTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-update-sms-template-response
- name: UpdateTemplateActiveVersionRequest
  property_count: 1
  slug: amazon-pinpoint-update-template-active-version-request
- name: UpdateTemplateActiveVersionResponse
  property_count: 1
  slug: amazon-pinpoint-update-template-active-version-response
- name: UpdateVoiceChannelRequest
  property_count: 1
  slug: amazon-pinpoint-update-voice-channel-request
- name: UpdateVoiceChannelResponse
  property_count: 1
  slug: amazon-pinpoint-update-voice-channel-response
- name: UpdateVoiceTemplateRequest
  property_count: 1
  slug: amazon-pinpoint-update-voice-template-request
- name: UpdateVoiceTemplateResponse
  property_count: 1
  slug: amazon-pinpoint-update-voice-template-response
- name: VerificationResponse
  property_count: 1
  slug: amazon-pinpoint-verification-response
- name: VerifyOTPMessageRequestParameters
  property_count: 3
  slug: amazon-pinpoint-verify-otp-message-request-parameters
- name: VerifyOTPMessageRequest
  property_count: 1
  slug: amazon-pinpoint-verify-otp-message-request
- name: VerifyOTPMessageResponse
  property_count: 1
  slug: amazon-pinpoint-verify-otp-message-response
- name: VoiceChannelRequest
  property_count: 1
  slug: amazon-pinpoint-voice-channel-request
- name: VoiceChannelResponse
  property_count: 10
  slug: amazon-pinpoint-voice-channel-response
- name: VoiceMessage
  property_count: 5
  slug: amazon-pinpoint-voice-message
- name: VoiceTemplateRequest
  property_count: 6
  slug: amazon-pinpoint-voice-template-request
- name: VoiceTemplateResponse
  property_count: 12
  slug: amazon-pinpoint-voice-template-response
- name: WaitActivity
  property_count: 2
  slug: amazon-pinpoint-wait-activity
- name: WaitTime
  property_count: 2
  slug: amazon-pinpoint-wait-time
- name: WriteApplicationSettingsRequest
  property_count: 5
  slug: amazon-pinpoint-write-application-settings-request
- name: WriteCampaignRequest
  property_count: 17
  slug: amazon-pinpoint-write-campaign-request
- name: WriteEventStream
  property_count: 2
  slug: amazon-pinpoint-write-event-stream
- name: WriteJourneyRequest
  property_count: 18
  slug: amazon-pinpoint-write-journey-request
- name: WriteSegmentRequest
  property_count: 4
  slug: amazon-pinpoint-write-segment-request
- name: WriteTreatmentResource
  property_count: 7
  slug: amazon-pinpoint-write-treatment-resource
json_structures:
- name: Amazon Pinpoint Action Structure
  property_count: 0
  slug: amazon-pinpoint-action-structure
- name: Amazon Pinpoint Activities Response Structure
  property_count: 2
  slug: amazon-pinpoint-activities-response-structure
- name: Amazon Pinpoint Activity Response Structure
  property_count: 13
  slug: amazon-pinpoint-activity-response-structure
- name: Amazon Pinpoint Activity Structure
  property_count: 11
  slug: amazon-pinpoint-activity-structure
- name: Amazon Pinpoint Address Configuration Structure
  property_count: 6
  slug: amazon-pinpoint-address-configuration-structure
- name: Amazon Pinpoint Adm Channel Request Structure
  property_count: 3
  slug: amazon-pinpoint-adm-channel-request-structure
- name: Amazon Pinpoint Adm Channel Response Structure
  property_count: 10
  slug: amazon-pinpoint-adm-channel-response-structure
- name: Amazon Pinpoint Adm Message Structure
  property_count: 16
  slug: amazon-pinpoint-adm-message-structure
- name: Amazon Pinpoint Alignment Structure
  property_count: 0
  slug: amazon-pinpoint-alignment-structure
- name: Amazon Pinpoint Android Push Notification Template Structure
  property_count: 9
  slug: amazon-pinpoint-android-push-notification-template-structure
- name: Amazon Pinpoint Apns Channel Request Structure
  property_count: 8
  slug: amazon-pinpoint-apns-channel-request-structure
- name: Amazon Pinpoint Apns Channel Response Structure
  property_count: 12
  slug: amazon-pinpoint-apns-channel-response-structure
- name: Amazon Pinpoint Apns Message Structure
  property_count: 18
  slug: amazon-pinpoint-apns-message-structure
- name: Amazon Pinpoint Apns Push Notification Template Structure
  property_count: 7
  slug: amazon-pinpoint-apns-push-notification-template-structure
- name: Amazon Pinpoint Apns Sandbox Channel Request Structure
  property_count: 8
  slug: amazon-pinpoint-apns-sandbox-channel-request-structure
- name: Amazon Pinpoint Apns Sandbox Channel Response Structure
  property_count: 12
  slug: amazon-pinpoint-apns-sandbox-channel-response-structure
- name: Amazon Pinpoint Apns Voip Channel Request Structure
  property_count: 8
  slug: amazon-pinpoint-apns-voip-channel-request-structure
- name: Amazon Pinpoint Apns Voip Channel Response Structure
  property_count: 12
  slug: amazon-pinpoint-apns-voip-channel-response-structure
- name: Amazon Pinpoint Apns Voip Sandbox Channel Request Structure
  property_count: 8
  slug: amazon-pinpoint-apns-voip-sandbox-channel-request-structure
- name: Amazon Pinpoint Apns Voip Sandbox Channel Response Structure
  property_count: 12
  slug: amazon-pinpoint-apns-voip-sandbox-channel-response-structure
- name: Amazon Pinpoint Application Date Range Kpi Response Structure
  property_count: 6
  slug: amazon-pinpoint-application-date-range-kpi-response-structure
- name: Amazon Pinpoint Application Response Structure
  property_count: 5
  slug: amazon-pinpoint-application-response-structure
- name: Amazon Pinpoint Application Settings Resource Structure
  property_count: 5
  slug: amazon-pinpoint-application-settings-resource-structure
- name: Amazon Pinpoint Applications Response Structure
  property_count: 2
  slug: amazon-pinpoint-applications-response-structure
- name: Amazon Pinpoint Attribute Dimension Structure
  property_count: 2
  slug: amazon-pinpoint-attribute-dimension-structure
- name: Amazon Pinpoint Attribute Type Structure
  property_count: 0
  slug: amazon-pinpoint-attribute-type-structure
- name: Amazon Pinpoint Attributes Resource Structure
  property_count: 3
  slug: amazon-pinpoint-attributes-resource-structure
- name: Amazon Pinpoint Baidu Channel Request Structure
  property_count: 3
  slug: amazon-pinpoint-baidu-channel-request-structure
- name: Amazon Pinpoint Baidu Channel Response Structure
  property_count: 11
  slug: amazon-pinpoint-baidu-channel-response-structure
- name: Amazon Pinpoint Baidu Message Structure
  property_count: 14
  slug: amazon-pinpoint-baidu-message-structure
- name: Amazon Pinpoint Base Kpi Result Structure
  property_count: 1
  slug: amazon-pinpoint-base-kpi-result-structure
- name: Amazon Pinpoint Button Action Structure
  property_count: 0
  slug: amazon-pinpoint-button-action-structure
- name: Amazon Pinpoint Campaign Custom Message Structure
  property_count: 1
  slug: amazon-pinpoint-campaign-custom-message-structure
- name: Amazon Pinpoint Campaign Date Range Kpi Response Structure
  property_count: 7
  slug: amazon-pinpoint-campaign-date-range-kpi-response-structure
- name: Amazon Pinpoint Campaign Email Message Structure
  property_count: 4
  slug: amazon-pinpoint-campaign-email-message-structure
- name: Amazon Pinpoint Campaign Event Filter Structure
  property_count: 2
  slug: amazon-pinpoint-campaign-event-filter-structure
- name: Amazon Pinpoint Campaign Hook Structure
  property_count: 3
  slug: amazon-pinpoint-campaign-hook-structure
- name: Amazon Pinpoint Campaign In App Message Structure
  property_count: 4
  slug: amazon-pinpoint-campaign-in-app-message-structure
- name: Amazon Pinpoint Campaign Limits Structure
  property_count: 5
  slug: amazon-pinpoint-campaign-limits-structure
- name: Amazon Pinpoint Campaign Response Structure
  property_count: 25
  slug: amazon-pinpoint-campaign-response-structure
- name: Amazon Pinpoint Campaign Sms Message Structure
  property_count: 6
  slug: amazon-pinpoint-campaign-sms-message-structure
- name: Amazon Pinpoint Campaign State Structure
  property_count: 1
  slug: amazon-pinpoint-campaign-state-structure
- name: Amazon Pinpoint Campaign Status Structure
  property_count: 0
  slug: amazon-pinpoint-campaign-status-structure
- name: Amazon Pinpoint Campaigns Response Structure
  property_count: 2
  slug: amazon-pinpoint-campaigns-response-structure
- name: Amazon Pinpoint Channel Response Structure
  property_count: 9
  slug: amazon-pinpoint-channel-response-structure
- name: Amazon Pinpoint Channel Type Structure
  property_count: 0
  slug: amazon-pinpoint-channel-type-structure
- name: Amazon Pinpoint Channels Response Structure
  property_count: 1
  slug: amazon-pinpoint-channels-response-structure
- name: Amazon Pinpoint Closed Days Rule Structure
  property_count: 3
  slug: amazon-pinpoint-closed-days-rule-structure
- name: Amazon Pinpoint Closed Days Structure
  property_count: 5
  slug: amazon-pinpoint-closed-days-structure
- name: Amazon Pinpoint Condition Structure
  property_count: 2
  slug: amazon-pinpoint-condition-structure
- name: Amazon Pinpoint Conditional Split Activity Structure
  property_count: 4
  slug: amazon-pinpoint-conditional-split-activity-structure
- name: Amazon Pinpoint Contact Center Activity Structure
  property_count: 1
  slug: amazon-pinpoint-contact-center-activity-structure
- name: Amazon Pinpoint Create App Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-app-request-structure
- name: Amazon Pinpoint Create App Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-app-response-structure
- name: Amazon Pinpoint Create Application Request Structure
  property_count: 2
  slug: amazon-pinpoint-create-application-request-structure
- name: Amazon Pinpoint Create Campaign Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-campaign-request-structure
- name: Amazon Pinpoint Create Campaign Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-campaign-response-structure
- name: Amazon Pinpoint Create Email Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-email-template-request-structure
- name: Amazon Pinpoint Create Email Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-email-template-response-structure
- name: Amazon Pinpoint Create Export Job Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-export-job-request-structure
- name: Amazon Pinpoint Create Export Job Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-export-job-response-structure
- name: Amazon Pinpoint Create Import Job Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-import-job-request-structure
- name: Amazon Pinpoint Create Import Job Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-import-job-response-structure
- name: Amazon Pinpoint Create In App Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-in-app-template-request-structure
- name: Amazon Pinpoint Create In App Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-in-app-template-response-structure
- name: Amazon Pinpoint Create Journey Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-journey-request-structure
- name: Amazon Pinpoint Create Journey Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-journey-response-structure
- name: Amazon Pinpoint Create Push Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-push-template-request-structure
- name: Amazon Pinpoint Create Push Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-push-template-response-structure
- name: Amazon Pinpoint Create Recommender Configuration Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-recommender-configuration-request-structure
- name: Amazon Pinpoint Create Recommender Configuration Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-recommender-configuration-response-structure
- name: Amazon Pinpoint Create Recommender Configuration Structure
  property_count: 9
  slug: amazon-pinpoint-create-recommender-configuration-structure
- name: Amazon Pinpoint Create Segment Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-segment-request-structure
- name: Amazon Pinpoint Create Segment Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-segment-response-structure
- name: Amazon Pinpoint Create Sms Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-sms-template-request-structure
- name: Amazon Pinpoint Create Sms Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-sms-template-response-structure
- name: Amazon Pinpoint Create Template Message Body Structure
  property_count: 3
  slug: amazon-pinpoint-create-template-message-body-structure
- name: Amazon Pinpoint Create Voice Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-create-voice-template-request-structure
- name: Amazon Pinpoint Create Voice Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-create-voice-template-response-structure
- name: Amazon Pinpoint Custom Delivery Configuration Structure
  property_count: 2
  slug: amazon-pinpoint-custom-delivery-configuration-structure
- name: Amazon Pinpoint Custom Message Activity Structure
  property_count: 6
  slug: amazon-pinpoint-custom-message-activity-structure
- name: Amazon Pinpoint Day Of Week Structure
  property_count: 0
  slug: amazon-pinpoint-day-of-week-structure
- name: Amazon Pinpoint Default Button Configuration Structure
  property_count: 6
  slug: amazon-pinpoint-default-button-configuration-structure
- name: Amazon Pinpoint Default Message Structure
  property_count: 2
  slug: amazon-pinpoint-default-message-structure
- name: Amazon Pinpoint Default Push Notification Message Structure
  property_count: 7
  slug: amazon-pinpoint-default-push-notification-message-structure
- name: Amazon Pinpoint Default Push Notification Template Structure
  property_count: 5
  slug: amazon-pinpoint-default-push-notification-template-structure
- name: Amazon Pinpoint Delete Adm Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-adm-channel-request-structure
- name: Amazon Pinpoint Delete Adm Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-adm-channel-response-structure
- name: Amazon Pinpoint Delete Apns Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-apns-channel-request-structure
- name: Amazon Pinpoint Delete Apns Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-apns-channel-response-structure
- name: Amazon Pinpoint Delete Apns Sandbox Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-apns-sandbox-channel-request-structure
- name: Amazon Pinpoint Delete Apns Sandbox Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-apns-sandbox-channel-response-structure
- name: Amazon Pinpoint Delete Apns Voip Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-apns-voip-channel-request-structure
- name: Amazon Pinpoint Delete Apns Voip Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-apns-voip-channel-response-structure
- name: Amazon Pinpoint Delete Apns Voip Sandbox Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-apns-voip-sandbox-channel-request-structure
- name: Amazon Pinpoint Delete Apns Voip Sandbox Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-apns-voip-sandbox-channel-response-structure
- name: Amazon Pinpoint Delete App Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-app-request-structure
- name: Amazon Pinpoint Delete App Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-app-response-structure
- name: Amazon Pinpoint Delete Baidu Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-baidu-channel-request-structure
- name: Amazon Pinpoint Delete Baidu Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-baidu-channel-response-structure
- name: Amazon Pinpoint Delete Campaign Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-campaign-request-structure
- name: Amazon Pinpoint Delete Campaign Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-campaign-response-structure
- name: Amazon Pinpoint Delete Email Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-email-channel-request-structure
- name: Amazon Pinpoint Delete Email Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-email-channel-response-structure
- name: Amazon Pinpoint Delete Email Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-email-template-request-structure
- name: Amazon Pinpoint Delete Email Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-email-template-response-structure
- name: Amazon Pinpoint Delete Endpoint Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-endpoint-request-structure
- name: Amazon Pinpoint Delete Endpoint Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-endpoint-response-structure
- name: Amazon Pinpoint Delete Event Stream Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-event-stream-request-structure
- name: Amazon Pinpoint Delete Event Stream Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-event-stream-response-structure
- name: Amazon Pinpoint Delete Gcm Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-gcm-channel-request-structure
- name: Amazon Pinpoint Delete Gcm Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-gcm-channel-response-structure
- name: Amazon Pinpoint Delete In App Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-in-app-template-request-structure
- name: Amazon Pinpoint Delete In App Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-in-app-template-response-structure
- name: Amazon Pinpoint Delete Journey Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-journey-request-structure
- name: Amazon Pinpoint Delete Journey Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-journey-response-structure
- name: Amazon Pinpoint Delete Push Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-push-template-request-structure
- name: Amazon Pinpoint Delete Push Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-push-template-response-structure
- name: Amazon Pinpoint Delete Recommender Configuration Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-recommender-configuration-request-structure
- name: Amazon Pinpoint Delete Recommender Configuration Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-recommender-configuration-response-structure
- name: Amazon Pinpoint Delete Segment Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-segment-request-structure
- name: Amazon Pinpoint Delete Segment Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-segment-response-structure
- name: Amazon Pinpoint Delete Sms Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-sms-channel-request-structure
- name: Amazon Pinpoint Delete Sms Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-sms-channel-response-structure
- name: Amazon Pinpoint Delete Sms Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-sms-template-request-structure
- name: Amazon Pinpoint Delete Sms Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-sms-template-response-structure
- name: Amazon Pinpoint Delete User Endpoints Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-user-endpoints-request-structure
- name: Amazon Pinpoint Delete User Endpoints Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-user-endpoints-response-structure
- name: Amazon Pinpoint Delete Voice Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-voice-channel-request-structure
- name: Amazon Pinpoint Delete Voice Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-voice-channel-response-structure
- name: Amazon Pinpoint Delete Voice Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-delete-voice-template-request-structure
- name: Amazon Pinpoint Delete Voice Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-delete-voice-template-response-structure
- name: Amazon Pinpoint Delivery Status Structure
  property_count: 0
  slug: amazon-pinpoint-delivery-status-structure
- name: Amazon Pinpoint Direct Message Configuration Structure
  property_count: 9
  slug: amazon-pinpoint-direct-message-configuration-structure
- name: Amazon Pinpoint Duration Structure
  property_count: 0
  slug: amazon-pinpoint-duration-structure
- name: Amazon Pinpoint Email Channel Request Structure
  property_count: 5
  slug: amazon-pinpoint-email-channel-request-structure
- name: Amazon Pinpoint Email Channel Response Structure
  property_count: 15
  slug: amazon-pinpoint-email-channel-response-structure
- name: Amazon Pinpoint Email Message Activity Structure
  property_count: 4
  slug: amazon-pinpoint-email-message-activity-structure
- name: Amazon Pinpoint Email Message Structure
  property_count: 7
  slug: amazon-pinpoint-email-message-structure
- name: Amazon Pinpoint Email Template Request Structure
  property_count: 7
  slug: amazon-pinpoint-email-template-request-structure
- name: Amazon Pinpoint Email Template Response Structure
  property_count: 13
  slug: amazon-pinpoint-email-template-response-structure
- name: Amazon Pinpoint Endpoint Batch Item Structure
  property_count: 12
  slug: amazon-pinpoint-endpoint-batch-item-structure
- name: Amazon Pinpoint Endpoint Batch Request Structure
  property_count: 1
  slug: amazon-pinpoint-endpoint-batch-request-structure
- name: Amazon Pinpoint Endpoint Demographic Structure
  property_count: 8
  slug: amazon-pinpoint-endpoint-demographic-structure
- name: Amazon Pinpoint Endpoint Item Response Structure
  property_count: 2
  slug: amazon-pinpoint-endpoint-item-response-structure
- name: Amazon Pinpoint Endpoint Location Structure
  property_count: 6
  slug: amazon-pinpoint-endpoint-location-structure
- name: Amazon Pinpoint Endpoint Message Result Structure
  property_count: 6
  slug: amazon-pinpoint-endpoint-message-result-structure
- name: Amazon Pinpoint Endpoint Request Structure
  property_count: 11
  slug: amazon-pinpoint-endpoint-request-structure
- name: Amazon Pinpoint Endpoint Response Structure
  property_count: 15
  slug: amazon-pinpoint-endpoint-response-structure
- name: Amazon Pinpoint Endpoint Send Configuration Structure
  property_count: 5
  slug: amazon-pinpoint-endpoint-send-configuration-structure
- name: Amazon Pinpoint Endpoint User Structure
  property_count: 2
  slug: amazon-pinpoint-endpoint-user-structure
- name: Amazon Pinpoint Endpoints Response Structure
  property_count: 1
  slug: amazon-pinpoint-endpoints-response-structure
- name: Amazon Pinpoint Event Condition Structure
  property_count: 2
  slug: amazon-pinpoint-event-condition-structure
- name: Amazon Pinpoint Event Dimensions Structure
  property_count: 3
  slug: amazon-pinpoint-event-dimensions-structure
- name: Amazon Pinpoint Event Filter Structure
  property_count: 2
  slug: amazon-pinpoint-event-filter-structure
- name: Amazon Pinpoint Event Item Response Structure
  property_count: 2
  slug: amazon-pinpoint-event-item-response-structure
- name: Amazon Pinpoint Event Start Condition Structure
  property_count: 2
  slug: amazon-pinpoint-event-start-condition-structure
- name: Amazon Pinpoint Event Stream Structure
  property_count: 6
  slug: amazon-pinpoint-event-stream-structure
- name: Amazon Pinpoint Event Structure
  property_count: 10
  slug: amazon-pinpoint-event-structure
- name: Amazon Pinpoint Events Batch Structure
  property_count: 2
  slug: amazon-pinpoint-events-batch-structure
- name: Amazon Pinpoint Events Request Structure
  property_count: 1
  slug: amazon-pinpoint-events-request-structure
- name: Amazon Pinpoint Events Response Structure
  property_count: 1
  slug: amazon-pinpoint-events-response-structure
- name: Amazon Pinpoint Export Job Request Structure
  property_count: 4
  slug: amazon-pinpoint-export-job-request-structure
- name: Amazon Pinpoint Export Job Resource Structure
  property_count: 4
  slug: amazon-pinpoint-export-job-resource-structure
- name: Amazon Pinpoint Export Job Response Structure
  property_count: 13
  slug: amazon-pinpoint-export-job-response-structure
- name: Amazon Pinpoint Export Jobs Response Structure
  property_count: 2
  slug: amazon-pinpoint-export-jobs-response-structure
- name: Amazon Pinpoint Frequency Structure
  property_count: 0
  slug: amazon-pinpoint-frequency-structure
- name: Amazon Pinpoint Gcm Channel Request Structure
  property_count: 2
  slug: amazon-pinpoint-gcm-channel-request-structure
- name: Amazon Pinpoint Gcm Channel Response Structure
  property_count: 11
  slug: amazon-pinpoint-gcm-channel-response-structure
- name: Amazon Pinpoint Gcm Message Structure
  property_count: 17
  slug: amazon-pinpoint-gcm-message-structure
- name: Amazon Pinpoint Get Adm Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-adm-channel-request-structure
- name: Amazon Pinpoint Get Adm Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-adm-channel-response-structure
- name: Amazon Pinpoint Get Apns Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-apns-channel-request-structure
- name: Amazon Pinpoint Get Apns Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-apns-channel-response-structure
- name: Amazon Pinpoint Get Apns Sandbox Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-apns-sandbox-channel-request-structure
- name: Amazon Pinpoint Get Apns Sandbox Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-apns-sandbox-channel-response-structure
- name: Amazon Pinpoint Get Apns Voip Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-apns-voip-channel-request-structure
- name: Amazon Pinpoint Get Apns Voip Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-apns-voip-channel-response-structure
- name: Amazon Pinpoint Get Apns Voip Sandbox Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-apns-voip-sandbox-channel-request-structure
- name: Amazon Pinpoint Get Apns Voip Sandbox Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-apns-voip-sandbox-channel-response-structure
- name: Amazon Pinpoint Get App Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-app-request-structure
- name: Amazon Pinpoint Get App Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-app-response-structure
- name: Amazon Pinpoint Get Application Date Range Kpi Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-application-date-range-kpi-request-structure
- name: Amazon Pinpoint Get Application Date Range Kpi Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-application-date-range-kpi-response-structure
- name: Amazon Pinpoint Get Application Settings Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-application-settings-request-structure
- name: Amazon Pinpoint Get Application Settings Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-application-settings-response-structure
- name: Amazon Pinpoint Get Apps Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-apps-request-structure
- name: Amazon Pinpoint Get Apps Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-apps-response-structure
- name: Amazon Pinpoint Get Baidu Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-baidu-channel-request-structure
- name: Amazon Pinpoint Get Baidu Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-baidu-channel-response-structure
- name: Amazon Pinpoint Get Campaign Activities Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-campaign-activities-request-structure
- name: Amazon Pinpoint Get Campaign Activities Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-campaign-activities-response-structure
- name: Amazon Pinpoint Get Campaign Date Range Kpi Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-campaign-date-range-kpi-request-structure
- name: Amazon Pinpoint Get Campaign Date Range Kpi Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-campaign-date-range-kpi-response-structure
- name: Amazon Pinpoint Get Campaign Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-campaign-request-structure
- name: Amazon Pinpoint Get Campaign Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-campaign-response-structure
- name: Amazon Pinpoint Get Campaign Version Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-campaign-version-request-structure
- name: Amazon Pinpoint Get Campaign Version Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-campaign-version-response-structure
- name: Amazon Pinpoint Get Campaign Versions Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-campaign-versions-request-structure
- name: Amazon Pinpoint Get Campaign Versions Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-campaign-versions-response-structure
- name: Amazon Pinpoint Get Campaigns Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-campaigns-request-structure
- name: Amazon Pinpoint Get Campaigns Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-campaigns-response-structure
- name: Amazon Pinpoint Get Channels Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-channels-request-structure
- name: Amazon Pinpoint Get Channels Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-channels-response-structure
- name: Amazon Pinpoint Get Email Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-email-channel-request-structure
- name: Amazon Pinpoint Get Email Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-email-channel-response-structure
- name: Amazon Pinpoint Get Email Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-email-template-request-structure
- name: Amazon Pinpoint Get Email Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-email-template-response-structure
- name: Amazon Pinpoint Get Endpoint Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-endpoint-request-structure
- name: Amazon Pinpoint Get Endpoint Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-endpoint-response-structure
- name: Amazon Pinpoint Get Event Stream Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-event-stream-request-structure
- name: Amazon Pinpoint Get Event Stream Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-event-stream-response-structure
- name: Amazon Pinpoint Get Export Job Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-export-job-request-structure
- name: Amazon Pinpoint Get Export Job Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-export-job-response-structure
- name: Amazon Pinpoint Get Export Jobs Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-export-jobs-request-structure
- name: Amazon Pinpoint Get Export Jobs Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-export-jobs-response-structure
- name: Amazon Pinpoint Get Gcm Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-gcm-channel-request-structure
- name: Amazon Pinpoint Get Gcm Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-gcm-channel-response-structure
- name: Amazon Pinpoint Get Import Job Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-import-job-request-structure
- name: Amazon Pinpoint Get Import Job Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-import-job-response-structure
- name: Amazon Pinpoint Get Import Jobs Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-import-jobs-request-structure
- name: Amazon Pinpoint Get Import Jobs Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-import-jobs-response-structure
- name: Amazon Pinpoint Get In App Messages Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-in-app-messages-request-structure
- name: Amazon Pinpoint Get In App Messages Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-in-app-messages-response-structure
- name: Amazon Pinpoint Get In App Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-in-app-template-request-structure
- name: Amazon Pinpoint Get In App Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-in-app-template-response-structure
- name: Amazon Pinpoint Get Journey Date Range Kpi Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-journey-date-range-kpi-request-structure
- name: Amazon Pinpoint Get Journey Date Range Kpi Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-journey-date-range-kpi-response-structure
- name: Amazon Pinpoint Get Journey Execution Activity Metrics Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-journey-execution-activity-metrics-request-structure
- name: Amazon Pinpoint Get Journey Execution Activity Metrics Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-journey-execution-activity-metrics-response-structure
- name: Amazon Pinpoint Get Journey Execution Metrics Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-journey-execution-metrics-request-structure
- name: Amazon Pinpoint Get Journey Execution Metrics Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-journey-execution-metrics-response-structure
- name: Amazon Pinpoint Get Journey Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-journey-request-structure
- name: Amazon Pinpoint Get Journey Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-journey-response-structure
- name: Amazon Pinpoint Get Push Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-push-template-request-structure
- name: Amazon Pinpoint Get Push Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-push-template-response-structure
- name: Amazon Pinpoint Get Recommender Configuration Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-recommender-configuration-request-structure
- name: Amazon Pinpoint Get Recommender Configuration Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-recommender-configuration-response-structure
- name: Amazon Pinpoint Get Recommender Configurations Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-recommender-configurations-request-structure
- name: Amazon Pinpoint Get Recommender Configurations Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-recommender-configurations-response-structure
- name: Amazon Pinpoint Get Segment Export Jobs Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-segment-export-jobs-request-structure
- name: Amazon Pinpoint Get Segment Export Jobs Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-segment-export-jobs-response-structure
- name: Amazon Pinpoint Get Segment Import Jobs Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-segment-import-jobs-request-structure
- name: Amazon Pinpoint Get Segment Import Jobs Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-segment-import-jobs-response-structure
- name: Amazon Pinpoint Get Segment Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-segment-request-structure
- name: Amazon Pinpoint Get Segment Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-segment-response-structure
- name: Amazon Pinpoint Get Segment Version Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-segment-version-request-structure
- name: Amazon Pinpoint Get Segment Version Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-segment-version-response-structure
- name: Amazon Pinpoint Get Segment Versions Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-segment-versions-request-structure
- name: Amazon Pinpoint Get Segment Versions Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-segment-versions-response-structure
- name: Amazon Pinpoint Get Segments Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-segments-request-structure
- name: Amazon Pinpoint Get Segments Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-segments-response-structure
- name: Amazon Pinpoint Get Sms Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-sms-channel-request-structure
- name: Amazon Pinpoint Get Sms Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-sms-channel-response-structure
- name: Amazon Pinpoint Get Sms Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-sms-template-request-structure
- name: Amazon Pinpoint Get Sms Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-sms-template-response-structure
- name: Amazon Pinpoint Get User Endpoints Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-user-endpoints-request-structure
- name: Amazon Pinpoint Get User Endpoints Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-user-endpoints-response-structure
- name: Amazon Pinpoint Get Voice Channel Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-voice-channel-request-structure
- name: Amazon Pinpoint Get Voice Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-voice-channel-response-structure
- name: Amazon Pinpoint Get Voice Template Request Structure
  property_count: 0
  slug: amazon-pinpoint-get-voice-template-request-structure
- name: Amazon Pinpoint Get Voice Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-get-voice-template-response-structure
- name: Amazon Pinpoint Gps Coordinates Structure
  property_count: 2
  slug: amazon-pinpoint-gps-coordinates-structure
- name: Amazon Pinpoint Gps Point Dimension Structure
  property_count: 2
  slug: amazon-pinpoint-gps-point-dimension-structure
- name: Amazon Pinpoint Holdout Activity Structure
  property_count: 2
  slug: amazon-pinpoint-holdout-activity-structure
- name: Amazon Pinpoint Import Job Request Structure
  property_count: 8
  slug: amazon-pinpoint-import-job-request-structure
- name: Amazon Pinpoint Import Job Resource Structure
  property_count: 8
  slug: amazon-pinpoint-import-job-resource-structure
- name: Amazon Pinpoint Import Job Response Structure
  property_count: 13
  slug: amazon-pinpoint-import-job-response-structure
- name: Amazon Pinpoint Import Jobs Response Structure
  property_count: 2
  slug: amazon-pinpoint-import-jobs-response-structure
- name: Amazon Pinpoint In App Campaign Schedule Structure
  property_count: 3
  slug: amazon-pinpoint-in-app-campaign-schedule-structure
- name: Amazon Pinpoint In App Message Body Config Structure
  property_count: 3
  slug: amazon-pinpoint-in-app-message-body-config-structure
- name: Amazon Pinpoint In App Message Button Structure
  property_count: 4
  slug: amazon-pinpoint-in-app-message-button-structure
- name: Amazon Pinpoint In App Message Campaign Structure
  property_count: 8
  slug: amazon-pinpoint-in-app-message-campaign-structure
- name: Amazon Pinpoint In App Message Content Structure
  property_count: 6
  slug: amazon-pinpoint-in-app-message-content-structure
- name: Amazon Pinpoint In App Message Header Config Structure
  property_count: 3
  slug: amazon-pinpoint-in-app-message-header-config-structure
- name: Amazon Pinpoint In App Message Structure
  property_count: 3
  slug: amazon-pinpoint-in-app-message-structure
- name: Amazon Pinpoint In App Messages Response Structure
  property_count: 1
  slug: amazon-pinpoint-in-app-messages-response-structure
- name: Amazon Pinpoint In App Template Request Structure
  property_count: 5
  slug: amazon-pinpoint-in-app-template-request-structure
- name: Amazon Pinpoint In App Template Response Structure
  property_count: 11
  slug: amazon-pinpoint-in-app-template-response-structure
- name: Amazon Pinpoint Include Structure
  property_count: 0
  slug: amazon-pinpoint-include-structure
- name: Amazon Pinpoint Item Response Structure
  property_count: 2
  slug: amazon-pinpoint-item-response-structure
- name: Amazon Pinpoint Job Status Structure
  property_count: 0
  slug: amazon-pinpoint-job-status-structure
- name: Amazon Pinpoint Journey Channel Settings Structure
  property_count: 2
  slug: amazon-pinpoint-journey-channel-settings-structure
- name: Amazon Pinpoint Journey Custom Message Structure
  property_count: 1
  slug: amazon-pinpoint-journey-custom-message-structure
- name: Amazon Pinpoint Journey Date Range Kpi Response Structure
  property_count: 7
  slug: amazon-pinpoint-journey-date-range-kpi-response-structure
- name: Amazon Pinpoint Journey Email Message Structure
  property_count: 1
  slug: amazon-pinpoint-journey-email-message-structure
- name: Amazon Pinpoint Journey Execution Activity Metrics Response Structure
  property_count: 6
  slug: amazon-pinpoint-journey-execution-activity-metrics-response-structure
- name: Amazon Pinpoint Journey Execution Metrics Response Structure
  property_count: 4
  slug: amazon-pinpoint-journey-execution-metrics-response-structure
- name: Amazon Pinpoint Journey Limits Structure
  property_count: 4
  slug: amazon-pinpoint-journey-limits-structure
- name: Amazon Pinpoint Journey Push Message Structure
  property_count: 1
  slug: amazon-pinpoint-journey-push-message-structure
- name: Amazon Pinpoint Journey Response Structure
  property_count: 21
  slug: amazon-pinpoint-journey-response-structure
- name: Amazon Pinpoint Journey Schedule Structure
  property_count: 3
  slug: amazon-pinpoint-journey-schedule-structure
- name: Amazon Pinpoint Journey Sms Message Structure
  property_count: 5
  slug: amazon-pinpoint-journey-sms-message-structure
- name: Amazon Pinpoint Journey State Request Structure
  property_count: 1
  slug: amazon-pinpoint-journey-state-request-structure
- name: Amazon Pinpoint Journeys Response Structure
  property_count: 2
  slug: amazon-pinpoint-journeys-response-structure
- name: Amazon Pinpoint Layout Structure
  property_count: 0
  slug: amazon-pinpoint-layout-structure
- name: Amazon Pinpoint List Journeys Request Structure
  property_count: 0
  slug: amazon-pinpoint-list-journeys-request-structure
- name: Amazon Pinpoint List Journeys Response Structure
  property_count: 1
  slug: amazon-pinpoint-list-journeys-response-structure
- name: Amazon Pinpoint List Recommender Configurations Response Structure
  property_count: 2
  slug: amazon-pinpoint-list-recommender-configurations-response-structure
- name: Amazon Pinpoint List Tags For Resource Request Structure
  property_count: 0
  slug: amazon-pinpoint-list-tags-for-resource-request-structure
- name: Amazon Pinpoint List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-pinpoint-list-tags-for-resource-response-structure
- name: Amazon Pinpoint List Template Versions Request Structure
  property_count: 0
  slug: amazon-pinpoint-list-template-versions-request-structure
- name: Amazon Pinpoint List Template Versions Response Structure
  property_count: 1
  slug: amazon-pinpoint-list-template-versions-response-structure
- name: Amazon Pinpoint List Templates Request Structure
  property_count: 0
  slug: amazon-pinpoint-list-templates-request-structure
- name: Amazon Pinpoint List Templates Response Structure
  property_count: 1
  slug: amazon-pinpoint-list-templates-response-structure
- name: Amazon Pinpoint Message Configuration Structure
  property_count: 9
  slug: amazon-pinpoint-message-configuration-structure
- name: Amazon Pinpoint Message Request Structure
  property_count: 6
  slug: amazon-pinpoint-message-request-structure
- name: Amazon Pinpoint Message Response Structure
  property_count: 4
  slug: amazon-pinpoint-message-response-structure
- name: Amazon Pinpoint Message Result Structure
  property_count: 5
  slug: amazon-pinpoint-message-result-structure
- name: Amazon Pinpoint Message Structure
  property_count: 12
  slug: amazon-pinpoint-message-structure
- name: Amazon Pinpoint Metric Dimension Structure
  property_count: 2
  slug: amazon-pinpoint-metric-dimension-structure
- name: Amazon Pinpoint Multi Conditional Branch Structure
  property_count: 2
  slug: amazon-pinpoint-multi-conditional-branch-structure
- name: Amazon Pinpoint Multi Conditional Split Activity Structure
  property_count: 3
  slug: amazon-pinpoint-multi-conditional-split-activity-structure
- name: Amazon Pinpoint Number Validate Request Structure
  property_count: 2
  slug: amazon-pinpoint-number-validate-request-structure
- name: Amazon Pinpoint Number Validate Response Structure
  property_count: 14
  slug: amazon-pinpoint-number-validate-response-structure
- name: Amazon Pinpoint Open Hours Rule Structure
  property_count: 2
  slug: amazon-pinpoint-open-hours-rule-structure
- name: Amazon Pinpoint Open Hours Structure
  property_count: 5
  slug: amazon-pinpoint-open-hours-structure
- name: Amazon Pinpoint Override Button Configuration Structure
  property_count: 2
  slug: amazon-pinpoint-override-button-configuration-structure
- name: Amazon Pinpoint Phone Number Validate Request Structure
  property_count: 1
  slug: amazon-pinpoint-phone-number-validate-request-structure
- name: Amazon Pinpoint Phone Number Validate Response Structure
  property_count: 1
  slug: amazon-pinpoint-phone-number-validate-response-structure
- name: Amazon Pinpoint Public Endpoint Structure
  property_count: 11
  slug: amazon-pinpoint-public-endpoint-structure
- name: Amazon Pinpoint Push Message Activity Structure
  property_count: 4
  slug: amazon-pinpoint-push-message-activity-structure
- name: Amazon Pinpoint Push Notification Template Request Structure
  property_count: 9
  slug: amazon-pinpoint-push-notification-template-request-structure
- name: Amazon Pinpoint Push Notification Template Response Structure
  property_count: 15
  slug: amazon-pinpoint-push-notification-template-response-structure
- name: Amazon Pinpoint Put Event Stream Request Structure
  property_count: 1
  slug: amazon-pinpoint-put-event-stream-request-structure
- name: Amazon Pinpoint Put Event Stream Response Structure
  property_count: 1
  slug: amazon-pinpoint-put-event-stream-response-structure
- name: Amazon Pinpoint Put Events Request Structure
  property_count: 1
  slug: amazon-pinpoint-put-events-request-structure
- name: Amazon Pinpoint Put Events Response Structure
  property_count: 1
  slug: amazon-pinpoint-put-events-response-structure
- name: Amazon Pinpoint Quiet Time Structure
  property_count: 2
  slug: amazon-pinpoint-quiet-time-structure
- name: Amazon Pinpoint Random Split Activity Structure
  property_count: 1
  slug: amazon-pinpoint-random-split-activity-structure
- name: Amazon Pinpoint Random Split Entry Structure
  property_count: 2
  slug: amazon-pinpoint-random-split-entry-structure
- name: Amazon Pinpoint Raw Email Structure
  property_count: 1
  slug: amazon-pinpoint-raw-email-structure
- name: Amazon Pinpoint Recency Dimension Structure
  property_count: 2
  slug: amazon-pinpoint-recency-dimension-structure
- name: Amazon Pinpoint Recommender Configuration Response Structure
  property_count: 12
  slug: amazon-pinpoint-recommender-configuration-response-structure
- name: Amazon Pinpoint Remove Attributes Request Structure
  property_count: 1
  slug: amazon-pinpoint-remove-attributes-request-structure
- name: Amazon Pinpoint Remove Attributes Response Structure
  property_count: 1
  slug: amazon-pinpoint-remove-attributes-response-structure
- name: Amazon Pinpoint Result Row Structure
  property_count: 2
  slug: amazon-pinpoint-result-row-structure
- name: Amazon Pinpoint Result Row Value Structure
  property_count: 3
  slug: amazon-pinpoint-result-row-value-structure
- name: Amazon Pinpoint Schedule Structure
  property_count: 7
  slug: amazon-pinpoint-schedule-structure
- name: Amazon Pinpoint Segment Behaviors Structure
  property_count: 1
  slug: amazon-pinpoint-segment-behaviors-structure
- name: Amazon Pinpoint Segment Condition Structure
  property_count: 1
  slug: amazon-pinpoint-segment-condition-structure
- name: Amazon Pinpoint Segment Demographics Structure
  property_count: 6
  slug: amazon-pinpoint-segment-demographics-structure
- name: Amazon Pinpoint Segment Dimensions Structure
  property_count: 6
  slug: amazon-pinpoint-segment-dimensions-structure
- name: Amazon Pinpoint Segment Group List Structure
  property_count: 2
  slug: amazon-pinpoint-segment-group-list-structure
- name: Amazon Pinpoint Segment Group Structure
  property_count: 4
  slug: amazon-pinpoint-segment-group-structure
- name: Amazon Pinpoint Segment Import Resource Structure
  property_count: 6
  slug: amazon-pinpoint-segment-import-resource-structure
- name: Amazon Pinpoint Segment Location Structure
  property_count: 2
  slug: amazon-pinpoint-segment-location-structure
- name: Amazon Pinpoint Segment Reference Structure
  property_count: 2
  slug: amazon-pinpoint-segment-reference-structure
- name: Amazon Pinpoint Segment Response Structure
  property_count: 12
  slug: amazon-pinpoint-segment-response-structure
- name: Amazon Pinpoint Segments Response Structure
  property_count: 2
  slug: amazon-pinpoint-segments-response-structure
- name: Amazon Pinpoint Send Messages Request Structure
  property_count: 1
  slug: amazon-pinpoint-send-messages-request-structure
- name: Amazon Pinpoint Send Messages Response Structure
  property_count: 1
  slug: amazon-pinpoint-send-messages-response-structure
- name: Amazon Pinpoint Send Otp Message Request Parameters Structure
  property_count: 11
  slug: amazon-pinpoint-send-otp-message-request-parameters-structure
- name: Amazon Pinpoint Send Otp Message Request Structure
  property_count: 1
  slug: amazon-pinpoint-send-otp-message-request-structure
- name: Amazon Pinpoint Send Otp Message Response Structure
  property_count: 1
  slug: amazon-pinpoint-send-otp-message-response-structure
- name: Amazon Pinpoint Send Users Message Request Structure
  property_count: 5
  slug: amazon-pinpoint-send-users-message-request-structure
- name: Amazon Pinpoint Send Users Message Response Structure
  property_count: 3
  slug: amazon-pinpoint-send-users-message-response-structure
- name: Amazon Pinpoint Send Users Messages Request Structure
  property_count: 1
  slug: amazon-pinpoint-send-users-messages-request-structure
- name: Amazon Pinpoint Send Users Messages Response Structure
  property_count: 1
  slug: amazon-pinpoint-send-users-messages-response-structure
- name: Amazon Pinpoint Session Structure
  property_count: 4
  slug: amazon-pinpoint-session-structure
- name: Amazon Pinpoint Set Dimension Structure
  property_count: 2
  slug: amazon-pinpoint-set-dimension-structure
- name: Amazon Pinpoint Simple Condition Structure
  property_count: 3
  slug: amazon-pinpoint-simple-condition-structure
- name: Amazon Pinpoint Simple Email Part Structure
  property_count: 2
  slug: amazon-pinpoint-simple-email-part-structure
- name: Amazon Pinpoint Simple Email Structure
  property_count: 3
  slug: amazon-pinpoint-simple-email-structure
- name: Amazon Pinpoint Sms Channel Request Structure
  property_count: 3
  slug: amazon-pinpoint-sms-channel-request-structure
- name: Amazon Pinpoint Sms Channel Response Structure
  property_count: 14
  slug: amazon-pinpoint-sms-channel-response-structure
- name: Amazon Pinpoint Sms Message Activity Structure
  property_count: 4
  slug: amazon-pinpoint-sms-message-activity-structure
- name: Amazon Pinpoint Sms Message Structure
  property_count: 9
  slug: amazon-pinpoint-sms-message-structure
- name: Amazon Pinpoint Sms Template Request Structure
  property_count: 5
  slug: amazon-pinpoint-sms-template-request-structure
- name: Amazon Pinpoint Sms Template Response Structure
  property_count: 11
  slug: amazon-pinpoint-sms-template-response-structure
- name: Amazon Pinpoint Source Type Structure
  property_count: 0
  slug: amazon-pinpoint-source-type-structure
- name: Amazon Pinpoint Start Condition Structure
  property_count: 3
  slug: amazon-pinpoint-start-condition-structure
- name: Amazon Pinpoint State Structure
  property_count: 0
  slug: amazon-pinpoint-state-structure
- name: Amazon Pinpoint Structure
  property_count: 8
  slug: amazon-pinpoint-structure
- name: Amazon Pinpoint Tag Resource Request Structure
  property_count: 1
  slug: amazon-pinpoint-tag-resource-request-structure
- name: Amazon Pinpoint Tags Model Structure
  property_count: 1
  slug: amazon-pinpoint-tags-model-structure
- name: Amazon Pinpoint Template Active Version Request Structure
  property_count: 1
  slug: amazon-pinpoint-template-active-version-request-structure
- name: Amazon Pinpoint Template Configuration Structure
  property_count: 4
  slug: amazon-pinpoint-template-configuration-structure
- name: Amazon Pinpoint Template Create Message Body Structure
  property_count: 3
  slug: amazon-pinpoint-template-create-message-body-structure
- name: Amazon Pinpoint Template Response Structure
  property_count: 9
  slug: amazon-pinpoint-template-response-structure
- name: Amazon Pinpoint Template Structure
  property_count: 2
  slug: amazon-pinpoint-template-structure
- name: Amazon Pinpoint Template Type Structure
  property_count: 0
  slug: amazon-pinpoint-template-type-structure
- name: Amazon Pinpoint Template Version Response Structure
  property_count: 7
  slug: amazon-pinpoint-template-version-response-structure
- name: Amazon Pinpoint Template Versions Response Structure
  property_count: 4
  slug: amazon-pinpoint-template-versions-response-structure
- name: Amazon Pinpoint Templates Response Structure
  property_count: 2
  slug: amazon-pinpoint-templates-response-structure
- name: Amazon Pinpoint Treatment Resource Structure
  property_count: 9
  slug: amazon-pinpoint-treatment-resource-structure
- name: Amazon Pinpoint Type Structure
  property_count: 0
  slug: amazon-pinpoint-type-structure
- name: Amazon Pinpoint Untag Resource Request Structure
  property_count: 0
  slug: amazon-pinpoint-untag-resource-request-structure
- name: Amazon Pinpoint Update Adm Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-adm-channel-request-structure
- name: Amazon Pinpoint Update Adm Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-adm-channel-response-structure
- name: Amazon Pinpoint Update Apns Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-apns-channel-request-structure
- name: Amazon Pinpoint Update Apns Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-apns-channel-response-structure
- name: Amazon Pinpoint Update Apns Sandbox Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-apns-sandbox-channel-request-structure
- name: Amazon Pinpoint Update Apns Sandbox Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-apns-sandbox-channel-response-structure
- name: Amazon Pinpoint Update Apns Voip Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-apns-voip-channel-request-structure
- name: Amazon Pinpoint Update Apns Voip Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-apns-voip-channel-response-structure
- name: Amazon Pinpoint Update Apns Voip Sandbox Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-apns-voip-sandbox-channel-request-structure
- name: Amazon Pinpoint Update Apns Voip Sandbox Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-apns-voip-sandbox-channel-response-structure
- name: Amazon Pinpoint Update Application Settings Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-application-settings-request-structure
- name: Amazon Pinpoint Update Application Settings Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-application-settings-response-structure
- name: Amazon Pinpoint Update Attributes Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-attributes-request-structure
- name: Amazon Pinpoint Update Baidu Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-baidu-channel-request-structure
- name: Amazon Pinpoint Update Baidu Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-baidu-channel-response-structure
- name: Amazon Pinpoint Update Campaign Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-campaign-request-structure
- name: Amazon Pinpoint Update Campaign Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-campaign-response-structure
- name: Amazon Pinpoint Update Email Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-email-channel-request-structure
- name: Amazon Pinpoint Update Email Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-email-channel-response-structure
- name: Amazon Pinpoint Update Email Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-email-template-request-structure
- name: Amazon Pinpoint Update Email Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-email-template-response-structure
- name: Amazon Pinpoint Update Endpoint Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-endpoint-request-structure
- name: Amazon Pinpoint Update Endpoint Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-endpoint-response-structure
- name: Amazon Pinpoint Update Endpoints Batch Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-endpoints-batch-request-structure
- name: Amazon Pinpoint Update Endpoints Batch Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-endpoints-batch-response-structure
- name: Amazon Pinpoint Update Gcm Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-gcm-channel-request-structure
- name: Amazon Pinpoint Update Gcm Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-gcm-channel-response-structure
- name: Amazon Pinpoint Update In App Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-in-app-template-request-structure
- name: Amazon Pinpoint Update In App Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-in-app-template-response-structure
- name: Amazon Pinpoint Update Journey Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-journey-request-structure
- name: Amazon Pinpoint Update Journey Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-journey-response-structure
- name: Amazon Pinpoint Update Journey State Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-journey-state-request-structure
- name: Amazon Pinpoint Update Journey State Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-journey-state-response-structure
- name: Amazon Pinpoint Update Push Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-push-template-request-structure
- name: Amazon Pinpoint Update Push Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-push-template-response-structure
- name: Amazon Pinpoint Update Recommender Configuration Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-recommender-configuration-request-structure
- name: Amazon Pinpoint Update Recommender Configuration Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-recommender-configuration-response-structure
- name: Amazon Pinpoint Update Recommender Configuration Structure
  property_count: 9
  slug: amazon-pinpoint-update-recommender-configuration-structure
- name: Amazon Pinpoint Update Segment Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-segment-request-structure
- name: Amazon Pinpoint Update Segment Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-segment-response-structure
- name: Amazon Pinpoint Update Sms Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-sms-channel-request-structure
- name: Amazon Pinpoint Update Sms Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-sms-channel-response-structure
- name: Amazon Pinpoint Update Sms Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-sms-template-request-structure
- name: Amazon Pinpoint Update Sms Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-sms-template-response-structure
- name: Amazon Pinpoint Update Template Active Version Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-template-active-version-request-structure
- name: Amazon Pinpoint Update Template Active Version Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-template-active-version-response-structure
- name: Amazon Pinpoint Update Voice Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-voice-channel-request-structure
- name: Amazon Pinpoint Update Voice Channel Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-voice-channel-response-structure
- name: Amazon Pinpoint Update Voice Template Request Structure
  property_count: 1
  slug: amazon-pinpoint-update-voice-template-request-structure
- name: Amazon Pinpoint Update Voice Template Response Structure
  property_count: 1
  slug: amazon-pinpoint-update-voice-template-response-structure
- name: Amazon Pinpoint Verification Response Structure
  property_count: 1
  slug: amazon-pinpoint-verification-response-structure
- name: Amazon Pinpoint Verify Otp Message Request Parameters Structure
  property_count: 3
  slug: amazon-pinpoint-verify-otp-message-request-parameters-structure
- name: Amazon Pinpoint Verify Otp Message Request Structure
  property_count: 1
  slug: amazon-pinpoint-verify-otp-message-request-structure
- name: Amazon Pinpoint Verify Otp Message Response Structure
  property_count: 1
  slug: amazon-pinpoint-verify-otp-message-response-structure
- name: Amazon Pinpoint Voice Channel Request Structure
  property_count: 1
  slug: amazon-pinpoint-voice-channel-request-structure
- name: Amazon Pinpoint Voice Channel Response Structure
  property_count: 10
  slug: amazon-pinpoint-voice-channel-response-structure
- name: Amazon Pinpoint Voice Message Structure
  property_count: 5
  slug: amazon-pinpoint-voice-message-structure
- name: Amazon Pinpoint Voice Template Request Structure
  property_count: 6
  slug: amazon-pinpoint-voice-template-request-structure
- name: Amazon Pinpoint Voice Template Response Structure
  property_count: 12
  slug: amazon-pinpoint-voice-template-response-structure
- name: Amazon Pinpoint Wait Activity Structure
  property_count: 2
  slug: amazon-pinpoint-wait-activity-structure
- name: Amazon Pinpoint Wait Time Structure
  property_count: 2
  slug: amazon-pinpoint-wait-time-structure
- name: Amazon Pinpoint Write Application Settings Request Structure
  property_count: 5
  slug: amazon-pinpoint-write-application-settings-request-structure
- name: Amazon Pinpoint Write Campaign Request Structure
  property_count: 17
  slug: amazon-pinpoint-write-campaign-request-structure
- name: Amazon Pinpoint Write Event Stream Structure
  property_count: 2
  slug: amazon-pinpoint-write-event-stream-structure
- name: Amazon Pinpoint Write Journey Request Structure
  property_count: 18
  slug: amazon-pinpoint-write-journey-request-structure
- name: Amazon Pinpoint Write Segment Request Structure
  property_count: 4
  slug: amazon-pinpoint-write-segment-request-structure
- name: Amazon Pinpoint Write Treatment Resource Structure
  property_count: 7
  slug: amazon-pinpoint-write-treatment-resource-structure
jsonld:
- class_count: 54
  name: Amazon Pinpoint Analytics Context
  property_count: 70
  slug: amazon-pinpoint-analytics-context
- class_count: 9
  name: Amazon Pinpoint Apps Context
  property_count: 9
  slug: amazon-pinpoint-apps-context
- class_count: 34
  name: Amazon Pinpoint Campaigns Context
  property_count: 66
  slug: amazon-pinpoint-campaigns-context
- class_count: 125
  name: Amazon Pinpoint Channels Context
  property_count: 82
  slug: amazon-pinpoint-channels-context
- class_count: 27
  name: Amazon Pinpoint Endpoints Context
  property_count: 41
  slug: amazon-pinpoint-endpoints-context
- class_count: 39
  name: Amazon Pinpoint General Context
  property_count: 68
  slug: amazon-pinpoint-general-context
- class_count: 51
  name: Amazon Pinpoint Journeys Context
  property_count: 89
  slug: amazon-pinpoint-journeys-context
- class_count: 25
  name: Amazon Pinpoint Messages Context
  property_count: 68
  slug: amazon-pinpoint-messages-context
- class_count: 37
  name: Amazon Pinpoint Segments Context
  property_count: 57
  slug: amazon-pinpoint-segments-context
- class_count: 37
  name: Amazon Pinpoint Templates Context
  property_count: 37
  slug: amazon-pinpoint-templates-context
layout: provider
modified: '2026-08-13'
name: Amazon Pinpoint
nav: Providers
network: true
overview: 'Amazon Pinpoint publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Apps API, Phone API, and 3 more. Tagged areas include Campaigns, Communications, Email, Marketing, and Messaging.


  The Amazon Pinpoint catalog on APIs.io includes 1 event-driven AsyncAPI specification, 10 JSON-LD contexts, and 2 Spectral governance rulesets.


  Amazon Pinpoint''s developer surface includes sandbox, changelog, CLI, signup flow, API reference, authentication, developer portal, and 1068 more developer resources.'
plans:
- name: Amazon Pinpoint Plans Pricing
  plan_count: 1
  slug: amazon-pinpoint-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 26
  name: Amazon Pinpoint Rate Limits
  slug: amazon-pinpoint-rate-limits
rules:
- name: Amazon Pinpoint API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-pinpoint-jsonschema-spectral-rules
- name: Amazon Pinpoint API Rules
  rule_count: 39
  severity_counts:
    error: 14
    hint: 0
    info: 6
    warn: 19
  slug: amazon-pinpoint-spectral-rules
score:
  band: exemplar
  composite: 74.1
  delta: 13.5
  facets:
    commercial_clarity: 73.7
    contract_quality: 78.1
    developer_ergonomics: 82.6
    discoverability: 75.9
    governance: 89.6
    operational_transparency: 71.1
  previous_composite: 60.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-pinpoint/refs/heads/main/screenshots/amazon-pinpoint-2026-06-20T171757.png
security:
- kind: authentication
  name: Amazon Pinpoint Authentication
  slug: amazon-pinpoint-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Pinpoint Domain Security
  slug: amazon-pinpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Pinpoint Vulnerability Disclosure
  slug: amazon-pinpoint-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Amazon Pinpoint Trust Center
  slug: amazon-pinpoint-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, FedRAMP, HIPAA, ISO/IEC 27001:2013, ISO/IEC 27017:2015, ISO/IEC 27018:2014, ISO/IEC 9001:2015
slug: amazon-pinpoint
tags:
- Campaigns
- Communications
- Email
- Marketing
- Messaging
- Push Notifications
- SMS
- Voice
- Customer Engagement
- Segmentation
- Journeys
- Analytics
use_cases:
- description: Run scheduled, targeted promotional campaigns across email, SMS, and push channels.
  name: Marketing Campaigns
- description: Automate welcome sequences and onboarding journeys for new users.
  name: Customer Onboarding
- description: Deliver order confirmations, shipping updates, and account alerts in real time.
  name: Transactional Notifications
- description: Win back inactive users with targeted re-engagement messages and offers.
  name: Re-engagement Campaigns
- description: Experiment with different message content, timing, and channels to optimize engagement.
  name: A/B Testing
- description: Trigger personalized messages based on in-app events and user behaviors.
  name: Event-Based Messaging
website: https://console.aws.amazon.com/pinpoint/
---
