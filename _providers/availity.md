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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Availity Agentic Access
  operation_count: 19
  slug: availity-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 12
apis:
- description: The Availity Healthcare HIPAA Transactions API provides a unified interface for standard HIPAA EDI transactions. REST APIs enable healthcare providers and vendors to submit and receive X12 EDI transac
  name: Availity Healthcare HIPAA Transactions API
  slug: availity-hipaa-transactions-api
- description: The Availity Patient Cost Estimator API enables healthcare providers and institutions to estimate service costs before delivery for both institutional and professional services. REST APIs support vers
  name: Availity Patient Cost Estimator API
  slug: availity-patient-cost-estimator-api
- description: The Availity Eligibility & Benefits Value-Add APIs provide supplementary data during eligibility transactions. The Care Reminders API retrieves real-time care gap information from multiple payers. The
  name: Availity Eligibility & Benefits Value-Add APIs
  slug: availity-eb-value-adds-api
- description: The Availity Payer List API (v1.0.4) allows healthcare organizations to query available payers and the transactions they support. Returns payer identifiers, names, and supported transaction types incl
  name: Availity Payer List API
  slug: availity-payer-list-api
- description: The Availity Configurations API (v1.0.0) provides provider details and payer-specific validation requirements. Returns configuration rules for enhanced claim status, prior authorization, and other tra
  name: Availity Configurations API
  slug: availity-configurations-api
- description: Attach documentation to authorization requests
  name: availity Auth Attachments API
  slug: availity-auth-attachments-api
- description: Electronic claim attachment submission and retrieval
  name: availity Claim Attachments API
  slug: availity-claim-attachments-api
- description: Claim status inquiries and tracking
  name: availity Claim Status API
  slug: availity-claim-status-api
- description: Real-time eligibility and benefits verification
  name: availity Eligibility API
  slug: availity-eligibility-api
- description: Enhanced claim status with value-add data
  name: availity Enhanced Claim Status API
  slug: availity-enhanced-claim-status-api
- description: Check if authorization is required before submission
  name: availity Is Auth Required API
  slug: availity-is-auth-required-api
- description: Prior authorization and service review requests
  name: availity Service Reviews API
  slug: availity-service-reviews-api
arazzos:
- description: Submit an X12 275 claim attachment, then poll for its processing status until the payer accepts it.
  name: Availity Claim Attachment (X12 275)
  slug: availity-claim-attachment-workflow
- description: Submit an X12 276 claim status request, then poll for the X12 277 claim status response until the payer finalizes it.
  name: Availity Claim Status Inquiry (X12 276/277)
  slug: availity-claim-status-inquiry-workflow
- description: Locate a payer that supports the 270 transaction, submit an X12 270 eligibility request, then retrieve the resulting 271 benefit response.
  name: Availity Eligibility and Benefits (X12 270/271)
  slug: availity-eligibility-benefits-workflow
- description: Determine whether authorization is required, create the X12 278 service review, attach supporting clinical documentation, then read back the authorization decision.
  name: Availity Prior Authorization (X12 278)
  slug: availity-prior-authorization-workflow
artifact_total: 164
collections:
- collection_type: open
  name: Availity Claim Attachments API
  slug: open-availity-claim-attachments
- collection_type: open
  name: Availity Claim Status API
  slug: open-availity-claim-status
- collection_type: open
  name: Availity Eligibility & Benefits API
  slug: open-availity-eligibility
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/availity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/availity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/availity-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/availity-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://developer.availity.com/blog
description: Availity is a healthcare information network and clearinghouse providing REST APIs for real-time HIPAA EDI transactions. The platform processes over 11 billion annual healthcare transactions connecting providers, health plans, and vendors nationwide. Create your application and subscribe to a plan to make use of Availity APIs for eligibility verification, claims management, prior authorization, and patient cost estimation.
examples:
- key_count: 6
  name: Availity Createclaimstatusinquiry Example
  slug: availity-createclaimstatusinquiry-example
- key_count: 6
  name: Availity Createservicereview Example
  slug: availity-createservicereview-example
- key_count: 5
  name: Availity Eligibility Example
  slug: availity-eligibility-example
- key_count: 6
  name: Availity Submitclaimattachment Example
  slug: availity-submitclaimattachment-example
- key_count: 5
  name: Claim Attachments Claim Attachment Request Example
  slug: claim-attachments-claim-attachment-request-example
- key_count: 3
  name: Claim Attachments Claim Attachment Response Example
  slug: claim-attachments-claim-attachment-response-example
- key_count: 2
  name: Claim Status Async Job Response Example
  slug: claim-status-async-job-response-example
- key_count: 3
  name: Claim Status Claim Status List Example
  slug: claim-status-claim-status-list-example
- key_count: 6
  name: Claim Status Claim Status Request Example
  slug: claim-status-claim-status-request-example
- key_count: 6
  name: Claim Status Claim Status Response Example
  slug: claim-status-claim-status-response-example
- key_count: 6
  name: Claim Status Detail Search Request Example
  slug: claim-status-detail-search-request-example
- key_count: 8
  name: Claim Status Search By276 Request Example
  slug: claim-status-search-by276-request-example
- key_count: 8
  name: Claim Status Summary Search Request Example
  slug: claim-status-summary-search-request-example
- key_count: 7
  name: Eligibility Benefit Example
  slug: eligibility-benefit-example
- key_count: 8
  name: Eligibility Coverage Example
  slug: eligibility-coverage-example
- key_count: 5
  name: Eligibility Dependent Example
  slug: eligibility-dependent-example
- key_count: 4
  name: Eligibility Eligibility Error Example
  slug: eligibility-eligibility-error-example
- key_count: 3
  name: Eligibility Eligibility List Example
  slug: eligibility-eligibility-list-example
- key_count: 2
  name: Eligibility Eligibility Request Example
  slug: eligibility-eligibility-request-example
- key_count: 5
  name: Eligibility Eligibility Response Example
  slug: eligibility-eligibility-response-example
- key_count: 2
  name: Eligibility Payer Example
  slug: eligibility-payer-example
- key_count: 3
  name: Eligibility Payer Info Example
  slug: eligibility-payer-info-example
- key_count: 1
  name: Eligibility Payer List Example
  slug: eligibility-payer-list-example
- key_count: 5
  name: Eligibility Plan Information Example
  slug: eligibility-plan-information-example
- key_count: 6
  name: Eligibility Provider Example
  slug: eligibility-provider-example
- key_count: 7
  name: Eligibility Subscriber Example
  slug: eligibility-subscriber-example
- key_count: 7
  name: Eligibility Subscriber Info Example
  slug: eligibility-subscriber-info-example
- key_count: 2
  name: Service Reviews Async Job Response Example
  slug: service-reviews-async-job-response-example
- key_count: 6
  name: Service Reviews Attachment Request Example
  slug: service-reviews-attachment-request-example
- key_count: 2
  name: Service Reviews Attachment Status Response Example
  slug: service-reviews-attachment-status-response-example
- key_count: 1
  name: Service Reviews Is Auth Required Request Example
  slug: service-reviews-is-auth-required-request-example
- key_count: 3
  name: Service Reviews Is Auth Required Response Example
  slug: service-reviews-is-auth-required-response-example
- key_count: 3
  name: Service Reviews Service Review List Example
  slug: service-reviews-service-review-list-example
- key_count: 5
  name: Service Reviews Service Review Request Example
  slug: service-reviews-service-review-request-example
- key_count: 5
  name: Service Reviews Service Review Response Example
  slug: service-reviews-service-review-response-example
finops:
- name: Availity Finops
  service_category: Healthcare Network / Clearinghouse
  slug: availity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/availity.png
json_schemas:
- name: AsyncJobResponse
  property_count: 2
  slug: availity-asyncjobresponse
- name: AttachmentRequest
  property_count: 6
  slug: availity-attachmentrequest
- name: AttachmentStatusResponse
  property_count: 2
  slug: availity-attachmentstatusresponse
- name: Benefit
  property_count: 7
  slug: availity-benefit
- name: ClaimAttachmentRequest
  property_count: 5
  slug: availity-claimattachmentrequest
- name: ClaimAttachmentResponse
  property_count: 3
  slug: availity-claimattachmentresponse
- name: ClaimStatusList
  property_count: 3
  slug: availity-claimstatuslist
- name: ClaimStatusRequest
  property_count: 6
  slug: availity-claimstatusrequest
- name: ClaimStatusResponse
  property_count: 6
  slug: availity-claimstatusresponse
- name: Coverage
  property_count: 8
  slug: availity-coverage
- name: Dependent
  property_count: 5
  slug: availity-dependent
- name: DetailSearchRequest
  property_count: 6
  slug: availity-detailsearchrequest
- name: Availity Eligibility Response
  property_count: 8
  slug: availity-eligibility
- name: EligibilityError
  property_count: 4
  slug: availity-eligibilityerror
- name: EligibilityList
  property_count: 3
  slug: availity-eligibilitylist
- name: EligibilityRequest
  property_count: 6
  slug: availity-eligibilityrequest
- name: EligibilityResponse
  property_count: 8
  slug: availity-eligibilityresponse
- name: Error
  property_count: 3
  slug: availity-error
- name: IsAuthRequiredRequest
  property_count: 1
  slug: availity-isauthrequiredrequest
- name: IsAuthRequiredResponse
  property_count: 3
  slug: availity-isauthrequiredresponse
- name: Payer
  property_count: 2
  slug: availity-payer
- name: PayerInfo
  property_count: 3
  slug: availity-payerinfo
- name: PayerList
  property_count: 1
  slug: availity-payerlist
- name: PlanInformation
  property_count: 5
  slug: availity-planinformation
- name: Provider
  property_count: 6
  slug: availity-provider
- name: SearchBy276Request
  property_count: 8
  slug: availity-searchby276request
- name: ServiceReviewList
  property_count: 3
  slug: availity-servicereviewlist
- name: ServiceReviewRequest
  property_count: 5
  slug: availity-servicereviewrequest
- name: ServiceReviewResponse
  property_count: 5
  slug: availity-servicereviewresponse
- name: Subscriber
  property_count: 7
  slug: availity-subscriber
- name: SubscriberInfo
  property_count: 7
  slug: availity-subscriberinfo
- name: SummarySearchRequest
  property_count: 8
  slug: availity-summarysearchrequest
- name: ClaimAttachmentRequest
  property_count: 5
  slug: claim-attachments-claim-attachment-request
- name: ClaimAttachmentResponse
  property_count: 3
  slug: claim-attachments-claim-attachment-response
- name: AsyncJobResponse
  property_count: 2
  slug: claim-status-async-job-response
- name: ClaimStatusList
  property_count: 3
  slug: claim-status-claim-status-list
- name: ClaimStatusRequest
  property_count: 6
  slug: claim-status-claim-status-request
- name: ClaimStatusResponse
  property_count: 6
  slug: claim-status-claim-status-response
- name: DetailSearchRequest
  property_count: 6
  slug: claim-status-detail-search-request
- name: SearchBy276Request
  property_count: 8
  slug: claim-status-search-by276-request
- name: SummarySearchRequest
  property_count: 8
  slug: claim-status-summary-search-request
- name: Benefit
  property_count: 7
  slug: eligibility-benefit
- name: Coverage
  property_count: 8
  slug: eligibility-coverage
- name: Dependent
  property_count: 5
  slug: eligibility-dependent
- name: EligibilityError
  property_count: 4
  slug: eligibility-eligibility-error
- name: EligibilityList
  property_count: 3
  slug: eligibility-eligibility-list
- name: EligibilityRequest
  property_count: 6
  slug: eligibility-eligibility-request
- name: EligibilityResponse
  property_count: 8
  slug: eligibility-eligibility-response
- name: PayerInfo
  property_count: 3
  slug: eligibility-payer-info
- name: PayerList
  property_count: 1
  slug: eligibility-payer-list
- name: Payer
  property_count: 2
  slug: eligibility-payer
- name: PlanInformation
  property_count: 5
  slug: eligibility-plan-information
- name: Provider
  property_count: 6
  slug: eligibility-provider
- name: SubscriberInfo
  property_count: 7
  slug: eligibility-subscriber-info
- name: Subscriber
  property_count: 7
  slug: eligibility-subscriber
- name: AsyncJobResponse
  property_count: 2
  slug: service-reviews-async-job-response
- name: AttachmentRequest
  property_count: 6
  slug: service-reviews-attachment-request
- name: AttachmentStatusResponse
  property_count: 2
  slug: service-reviews-attachment-status-response
- name: IsAuthRequiredRequest
  property_count: 1
  slug: service-reviews-is-auth-required-request
- name: IsAuthRequiredResponse
  property_count: 3
  slug: service-reviews-is-auth-required-response
- name: ServiceReviewList
  property_count: 3
  slug: service-reviews-service-review-list
- name: ServiceReviewRequest
  property_count: 5
  slug: service-reviews-service-review-request
- name: ServiceReviewResponse
  property_count: 5
  slug: service-reviews-service-review-response
json_structures:
- name: Availity Eligibility Structure
  property_count: 8
  slug: availity-eligibility-structure
- name: Availity Structure
  property_count: 0
  slug: availity-structure
- name: Claim Attachments Claim Attachment Request Structure
  property_count: 5
  slug: claim-attachments-claim-attachment-request-structure
- name: Claim Attachments Claim Attachment Response Structure
  property_count: 3
  slug: claim-attachments-claim-attachment-response-structure
- name: Claim Status Async Job Response Structure
  property_count: 2
  slug: claim-status-async-job-response-structure
- name: Claim Status Claim Status List Structure
  property_count: 3
  slug: claim-status-claim-status-list-structure
- name: Claim Status Claim Status Request Structure
  property_count: 6
  slug: claim-status-claim-status-request-structure
- name: Claim Status Claim Status Response Structure
  property_count: 6
  slug: claim-status-claim-status-response-structure
- name: Claim Status Detail Search Request Structure
  property_count: 6
  slug: claim-status-detail-search-request-structure
- name: Claim Status Search By276 Request Structure
  property_count: 8
  slug: claim-status-search-by276-request-structure
- name: Claim Status Summary Search Request Structure
  property_count: 8
  slug: claim-status-summary-search-request-structure
- name: Eligibility Benefit Structure
  property_count: 7
  slug: eligibility-benefit-structure
- name: Eligibility Coverage Structure
  property_count: 8
  slug: eligibility-coverage-structure
- name: Eligibility Dependent Structure
  property_count: 5
  slug: eligibility-dependent-structure
- name: Eligibility Eligibility Error Structure
  property_count: 4
  slug: eligibility-eligibility-error-structure
- name: Eligibility Eligibility List Structure
  property_count: 3
  slug: eligibility-eligibility-list-structure
- name: Eligibility Eligibility Request Structure
  property_count: 6
  slug: eligibility-eligibility-request-structure
- name: Eligibility Eligibility Response Structure
  property_count: 8
  slug: eligibility-eligibility-response-structure
- name: Eligibility Payer Info Structure
  property_count: 3
  slug: eligibility-payer-info-structure
- name: Eligibility Payer List Structure
  property_count: 1
  slug: eligibility-payer-list-structure
- name: Eligibility Payer Structure
  property_count: 2
  slug: eligibility-payer-structure
- name: Eligibility Plan Information Structure
  property_count: 5
  slug: eligibility-plan-information-structure
- name: Eligibility Provider Structure
  property_count: 6
  slug: eligibility-provider-structure
- name: Eligibility Subscriber Info Structure
  property_count: 7
  slug: eligibility-subscriber-info-structure
- name: Eligibility Subscriber Structure
  property_count: 7
  slug: eligibility-subscriber-structure
- name: Service Reviews Async Job Response Structure
  property_count: 2
  slug: service-reviews-async-job-response-structure
- name: Service Reviews Attachment Request Structure
  property_count: 6
  slug: service-reviews-attachment-request-structure
- name: Service Reviews Attachment Status Response Structure
  property_count: 2
  slug: service-reviews-attachment-status-response-structure
- name: Service Reviews Is Auth Required Request Structure
  property_count: 1
  slug: service-reviews-is-auth-required-request-structure
- name: Service Reviews Is Auth Required Response Structure
  property_count: 3
  slug: service-reviews-is-auth-required-response-structure
- name: Service Reviews Service Review List Structure
  property_count: 3
  slug: service-reviews-service-review-list-structure
- name: Service Reviews Service Review Request Structure
  property_count: 5
  slug: service-reviews-service-review-request-structure
- name: Service Reviews Service Review Response Structure
  property_count: 5
  slug: service-reviews-service-review-response-structure
jsonld:
- class_count: 2
  name: Availity Availity Context
  property_count: 32
  slug: availity-availity-context
- class_count: 9
  name: Availity Claim Context
  property_count: 45
  slug: availity-claim-context
- class_count: 0
  name: Availity Context
  property_count: 5
  slug: availity-context
- class_count: 15
  name: Availity Eligibility Context
  property_count: 58
  slug: availity-eligibility-context
- class_count: 8
  name: Availity Service Context
  property_count: 30
  slug: availity-service-context
layout: provider
modified: '2026-05-19'
name: availity
nav: Providers
network: true
overview: 'availity publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Auth Attachments API, Claim Attachments API, Claim Status API, and 4 more.


  The availity catalog on APIs.io includes 5 JSON-LD contexts and 2 Spectral governance rulesets.


  availity''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Availity Plans Pricing
  plan_count: 5
  slug: availity-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 3
  name: Availity Rate Limits
  slug: availity-rate-limits
rules:
- name: availity API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: availity-jsonschema-spectral-rules
- name: availity API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 7
  slug: availity-spectral-rules
scopes:
- name: Availity Scopes
  scope_count: 1
  slug: availity-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 39.6
  delta: -8.5
  facets:
    commercial_clarity: 15.8
    contract_quality: 77.2
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/screenshots/availity-2026-06-20T172716.png
security:
- kind: authentication
  name: Availity Authentication
  slug: availity-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Availity Domain Security
  slug: availity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: availity
---
