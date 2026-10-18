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
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Telesign Agentic Access
  operation_count: 63
  slug: telesign-agentic-access
  summary_line: 63 operations · 44 acting
api_count: 28
apis:
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: Use this API to programmatically manage your Telesign accounts and their configurations.
  name: Telesign Accounts API
  slug: accounts-api
- baseURL: https://deact-api.telesign.com
  baseurl_source: declared
  description: 'Encoding: Accepts only UTF-8 encoded unicode characters as inputs. The Deactivated Numbers API can be used to get lists of deactivated numbers. These can be used to ensure you don''t send SMS messages '
  name: Telesign Deactivated Numbers API
  slug: deactivated-numbers-api
- baseURL: https://detect.telesign.com
  baseurl_source: declared
  description: 'Email Intelligence API (1 operations): Email Intelligence - Submit an email address to evaluate.'
  name: Telesign Email Intelligence API
  slug: email-intelligence-api
- baseURL: https://us-east-1.di-hub.telesign.com
  baseurl_source: declared
  description: The Flow Builder solution is designed to streamline the creation, execution, and management of transactional flows. By leveraging business rules and data from both internal and external sources, the F
  name: Telesign Flow Builder API
  slug: flow-builder-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The API Keys API from Telesign — 2 operation(s) for api keys.
  name: Telesign API Keys API
  slug: telesign-api-keys-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Bulk SMS API from Telesign — 1 operation(s) for bulk sms.
  name: Telesign Bulk SMS API
  slug: telesign-bulk-sms-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Bulk SMS Callbacks API from Telesign — 1 operation(s) for bulk sms callbacks.
  name: Telesign Bulk SMS Callbacks API
  slug: telesign-bulk-sms-callbacks-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Calls API from Telesign — 1 operation(s) for calls.
  name: Telesign Calls API
  slug: telesign-calls-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Completions API from Telesign — 1 operation(s) for completions.
  name: Telesign Completions API
  slug: telesign-completions-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Delivery Reports API from Telesign — 2 operation(s) for delivery reports.
  name: Telesign Delivery Reports API
  slug: telesign-delivery-reports-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Email Intelligence Extended Response API from Telesign — 1 operation(s) for email intelligence extended response.
  name: Telesign Email Intelligence Extended Response API
  slug: telesign-email-intelligence-extended-response-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Finalize API from Telesign — 4 operation(s) for finalize.
  name: Telesign Finalize API
  slug: telesign-finalize-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Initiate API from Telesign — 2 operation(s) for initiate.
  name: Telesign Initiate API
  slug: telesign-initiate-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Intelligence API from Telesign — 2 operation(s) for intelligence.
  name: Telesign Intelligence API
  slug: telesign-intelligence-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Messages API from Telesign — 1 operation(s) for messages.
  name: Telesign Messages API
  slug: telesign-messages-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Messaging API from Telesign — 4 operation(s) for messaging.
  name: Telesign Messaging API
  slug: telesign-messaging-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Messaging Callbacks API from Telesign — 6 operation(s) for messaging callbacks.
  name: Telesign Messaging Callbacks API
  slug: telesign-messaging-callbacks-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Number Masking API from Telesign — 2 operation(s) for number masking.
  name: Telesign Number Masking API
  slug: telesign-number-masking-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The One-time passcodes API from Telesign — 1 operation(s) for one-time passcodes.
  name: Telesign One-time passcodes API
  slug: telesign-one-time-passcodes-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Phone ID API from Telesign — 3 operation(s) for phone id.
  name: Telesign Phone ID API
  slug: telesign-phone-id-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Phone ID Contact API from Telesign — 1 operation(s) for phone id contact.
  name: Telesign Phone ID Contact API
  slug: telesign-phone-id-contact-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Phone ID Number Deactivation API from Telesign — 1 operation(s) for phone id number deactivation.
  name: Telesign Phone ID Number Deactivation API
  slug: telesign-phone-id-number-deactivation-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Protect API Authentication API from Telesign — 1 operation(s) for protect api authentication.
  name: Telesign Protect API Authentication API
  slug: telesign-protect-api-authentication-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Recordings API from Telesign — 2 operation(s) for recordings.
  name: Telesign Recordings API
  slug: telesign-recordings-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The SMS API from Telesign — 3 operation(s) for sms.
  name: Telesign SMS API
  slug: telesign-sms-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The SMS Callbacks API from Telesign — 1 operation(s) for sms callbacks.
  name: Telesign SMS Callbacks API
  slug: telesign-sms-callbacks-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Templates API from Telesign — 2 operation(s) for templates.
  name: Telesign Templates API
  slug: telesign-templates-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Templates Callbacks API from Telesign — 1 operation(s) for templates callbacks.
  name: Telesign Templates Callbacks API
  slug: telesign-templates-callbacks-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Transaction Status API from Telesign — 2 operation(s) for transaction status.
  name: Telesign Transaction Status API
  slug: telesign-transaction-status-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Verification Process API from Telesign — 3 operation(s) for verification process.
  name: Telesign Verification Process API
  slug: telesign-verification-process-api
- baseURL: https://accounts.telesign.com
  baseurl_source: declared
  description: The Voice API from Telesign — 1 operation(s) for voice.
  name: Telesign Voice API
  slug: telesign-voice-api
artifact_total: 89
asyncapis:
- description: ''
  name: Telesign Webhooks
  slug: telesign-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/capabilities/telesign-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/telesign-capability-edges.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/asyncapi/telesign-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/telesign-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/finops/telesign-finops.yml
  title: ''
  type: FinOps
  url: finops/telesign-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/rate-limits/telesign-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/telesign-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/plans/telesign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/telesign-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/rules/telesign-rules.yml
  title: ''
  type: Spectral
  url: rules/telesign-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/rules/telesign-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/telesign-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/json-ld/telesign-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/telesign-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/vocabulary/telesign-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/telesign-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/data-model/telesign-data-model.yml
  title: ''
  type: DataModel
  url: data-model/telesign-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/changelog/telesign-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/telesign-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/conventions/telesign-conventions.yml
  title: ''
  type: Conventions
  url: conventions/telesign-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.telesign.com/security
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/lifecycle/telesign-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/telesign-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/lifecycle/telesign-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/telesign-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/errors/telesign-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/telesign-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/errors/telesign-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/telesign-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/conformance/telesign-conformance.yml
  title: ''
  type: Conformance
  url: conformance/telesign-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/overlays/telesign-accounts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/telesign-accounts-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/well-known/telesign-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/telesign-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/well-known/telesign-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/telesign-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/hosts/telesign-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telesign-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/vendors/telesign-vendors.yml
  title: ''
  type: Vendors
  url: vendors/telesign-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/packages/telesign-packages.yml
  title: ''
  type: SDKs
  url: packages/telesign-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/packages/telesign-packages.yml
  title: ''
  type: Packages
  url: packages/telesign-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/agentic-access/telesign-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/telesign-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/security/telesign-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/telesign-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/security/telesign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telesign-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/authentication/telesign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/telesign-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telesign
- group: company
  title: ''
  type: Website
  url: https://www.telesign.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.telesign.com/enterprise
- group: auth
  title: ''
  type: Authentication
  url: https://developer.telesign.com/enterprise/docs/authentication
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telesign.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telesign.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telesign.com/terms-conditions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TeleSign
- group: company
  title: ''
  type: Blog
  url: https://www.telesign.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developer.telesign.com/enterprise/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.telesign.com/enterprise/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.telesign.com/enterprise/docs/get-started-with-docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.telesign.com/enterprise/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.telesign.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telesign.com/privacy-notice
- group: auth
  title: ''
  type: Security
  url: https://www.telesign.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.telesign.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://my.telesign.com/login
description: Telesign provides a comprehensive suite of communications and security APIs enabling businesses to verify phone numbers, send SMS, omnichannel and voice messages, and assess fraud risk. The developer portal publishes 22 OpenAPI contracts (65 operations) covering SMS Verify, Voice Verify, Silent Verify, App Verify and the multi-channel Verify API; Messaging (SMS, WhatsApp, Viber, RCS, MMS, email), Voice, Number Masking and Bulk SMS; Phone ID, Intelligence Cloud and Email Intelligence risk signals; and Accounts, Deactivated Numbers, Flow Builder and Protect Platform management surfaces, plus an RFC 9727 API catalog and callback (webhook) payload contracts.
examples:
- key_count: 4
  name: Telesign Create Verification Example
  slug: telesign-create-verification-example
- key_count: 4
  name: Telesign Phoneid Lookup Example
  slug: telesign-phoneid-lookup-example
- key_count: 4
  name: Telesign Send Sms Example
  slug: telesign-send-sms-example
finops:
- has_sources: true
  method: generated
  name: Telesign Finops
  primary_unit: ''
  service_category: Communications
  slug: telesign-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telesign.png
json_schemas:
- name: 200-av-response
  property_count: 5
  slug: telesign-200-av-response
- name: AccountDetails
  property_count: 2
  slug: telesign-account-details
- name: Account
  property_count: 0
  slug: telesign-account
- name: Action
  property_count: 2
  slug: telesign-action
- name: CallerIDAVResponse
  property_count: 5
  slug: telesign-caller-id-av-response
- name: Carrier
  property_count: 2
  slug: telesign-carrier
- name: DeactResFileList
  property_count: 3
  slug: telesign-deact-res-file-list
- name: FinalizeAVResponse
  property_count: 6
  slug: telesign-finalize-av-response
- name: GetAVStatusResponse
  property_count: 4
  slug: telesign-get-av-status-response
- name: getPhoneIdLiveResponse
  property_count: 9
  slug: telesign-get-phone-id-live-response
- name: getPhoneIdNDResponse
  property_count: 5
  slug: telesign-get-phone-id-ndresponse
- name: getPhoneIdResponse
  property_count: 9
  slug: telesign-get-phone-id-response
- name: getStatusResponse
  property_count: 6
  slug: telesign-get-status-response
- name: GET Verification Response
  property_count: 9
  slug: telesign-get-verification-response
- name: InitiateAVResponse
  property_count: 7
  slug: telesign-initiate-av-response
- name: NumMaskInputs
  property_count: 3
  slug: telesign-num-mask-inputs
- name: OmniReqChannelObj
  property_count: 2
  slug: telesign-omni-req-channel-obj
- name: OmniReqDetailsForRCS
  property_count: 2
  slug: telesign-omni-req-details-for-rcs
- name: OmniReqDetailsForViber
  property_count: 2
  slug: telesign-omni-req-details-for-viber
- name: OmniReqDetailsForWA
  property_count: 2
  slug: telesign-omni-req-details-for-wa
- name: PATCH Verification State Change Request
  property_count: 2
  slug: telesign-patch-verification-state-request
- name: PatchVerificationStateResponse
  property_count: 1
  slug: telesign-patch-verification-state-response
- name: postEmailIDRequestBody
  property_count: 5
  slug: telesign-post-email-idrequest-body
- name: postEmailIntResponse
  property_count: 5
  slug: telesign-post-email-int-response
- name: postPhoneIDRequestBody
  property_count: 5
  slug: telesign-post-phone-idrequest-body
- name: postScoreResponse
  property_count: 10
  slug: telesign-post-score-response
- name: postSMSSuccessResponse
  property_count: 0
  slug: telesign-post-smssuccess-response
- name: POST Verification request
  property_count: 7
  slug: telesign-post-verification-request
- name: POST Verification Response
  property_count: 0
  slug: telesign-post-verification-response
- name: putCompletionResponse
  property_count: 4
  slug: telesign-put-completion-response
- name: Recording
  property_count: 4
  slug: telesign-recording
- name: RecordingWithDetail
  property_count: 0
  slug: telesign-recording-with-detail
- name: RestAPIKey
  property_count: 0
  slug: telesign-rest-apikey
- name: ScoreNumbering
  property_count: 2
  slug: telesign-score-numbering
- name: ScorePhoneType
  property_count: 2
  slug: telesign-score-phone-type
- name: sendVoiceCodeResponse
  property_count: 0
  slug: telesign-send-voice-code-response
- name: SharedResponseFields
  property_count: 2
  slug: telesign-shared-response-fields
- name: sharedResponseSchema
  property_count: 4
  slug: telesign-shared-response-schema
- name: SIMSwapResponse
  property_count: 4
  slug: telesign-simswap-response
- name: SVResponse
  property_count: 2
  slug: telesign-svresponse
json_structures:
- name: Telesign Messaging Structure
  property_count: 0
  slug: telesign-messaging-structure
- name: Telesign Structure
  property_count: 0
  slug: telesign-structure
jsonld:
- class_count: 3
  name: Telesign Context
  property_count: 5
  slug: telesign-context
layout: provider
mcp_servers:
- description: developer.telesign.com is a ReadMe-hosted portal and serves ReadMe's MCP endpoint at /mcp under Telesign's own documentation domain. An unauthenticated JSON-RPC tools/list is refused with "Authorizati
  name: Telesign developer portal MCP server (ReadMe-hosted)
  slug: telesign-developer-portal-mcp-server-readme-hosted
modified: '2026-10-07'
name: Telesign
nav: Providers
network: true
overview: 'Telesign publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Deactivated Numbers API, Email Intelligence API, and 28 more. Tagged areas include Authentication, Communications, Fraud Prevention, Phone Intelligence, and SMS.


  The Telesign catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Telesign''s developer surface includes changelog, authentication, pricing, engineering blog, documentation, API reference, getting-started guide, and 41 more developer resources.'
plans:
- name: Telesign Plans Pricing
  plan_count: 3
  slug: telesign-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 16
  name: Telesign Rate Limits
  slug: telesign-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Telesign — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: telesign-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 12
  extends: []
  name: Telesign API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 7
  slug: telesign-rules
score:
  band: exemplar
  composite: 72.0
  coverage:
    artifact_dirs: 34
    catalog_earned: 82.5
    catalog_earned_first_party: 24.0
    catalog_gap: 32.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 72.4
    developer_ergonomics: 55.4
    discoverability: 75.0
    operational_transparency: 92.1
  previous_composite: 73.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/screenshots/telesign-2026-06-20T195043.png
security:
- kind: authentication
  name: Telesign Authentication
  slug: telesign-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Telesign Domain Security
  slug: telesign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Telesign Trust Center
  slug: telesign-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: telesign
tags:
- Authentication
- Communications
- Fraud Prevention
- Phone Intelligence
- SMS
- Verification
- Telecommunications
- Messaging
- Voice
- Email Intelligence
- Identity
- Number Masking
- Account
website: https://www.telesign.com/
---
