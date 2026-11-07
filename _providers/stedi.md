---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Stedi Agentic Access
  operation_count: 75
  slug: stedi-agentic-access
  summary_line: 75 operations · 31 acting
api_count: 7
apis:
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Claim acknowledgments API from Stedi — 1 operation(s) for claim acknowledgments.
  name: Stedi Claim acknowledgments API
  phrasing_intents:
  - id: ConvertReport277
    intent: Get a 277CA claim acknowledgment as JSON
    question: How do I see whether a payer accepted or rejected my claim in the 277CA acknowledgment?
  phrasing_ops: 1
  slug: stedi-claim-acknowledgments-api
- baseURL: https://claims.us.stedi.com/2025-03-07
  baseurl_source: declared
  description: The Claim Attachments API from Stedi — 2 operation(s) for claim attachments.
  name: Stedi Claim Attachments API
  phrasing_intents:
  - id: CreateClaimAttachmentFile
    intent: Get an upload URL for a claim attachment
    question: How do I upload supporting documents like medical records for a 275 claim attachment?
  - id: SubmitClaimAttachmentRawX12
    intent: Submit a 275 claim attachment in X12
    question: Can I send a 275 claim attachment as raw X12 EDI?
  phrasing_ops: 2
  slug: stedi-claim-attachments-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Claim submission API from Stedi — 8 operation(s) for claim submission.
  name: Stedi Claim submission API
  phrasing_intents:
  - id: InstitutionalClaimsRawX12Submission
    intent: Submit an 837I institutional claim in X12
    question: How do I send a hospital (837I institutional) claim that I already have as raw X12?
  - id: InstitutionalClaimsSubmission
    intent: Submit an 837I institutional claim as JSON
    question: How do I file a hospital or facility claim using JSON in Stedi?
  - id: ClaimsRawX12Submission
    intent: Submit an 837P professional claim in X12
    question: Can I submit a professional 837P claim that's already formatted as X12 EDI?
  - id: ClaimsSubmission
    intent: Submit an 837P professional claim as JSON
    question: How do I submit a doctor's office claim to an insurance payer using JSON?
  - id: DentalClaimsRawX12Submission
    intent: Submit an 837D dental claim in X12
    question: Can I send a dental claim that's already in 837D X12 format?
  - id: DentalClaimsSubmission
    intent: Submit an 837D dental claim as JSON
    question: How do I submit a dental claim to an insurer using JSON?
  - id: ExportPDF
    intent: Get a CMS-1500 PDF by claim business ID
    question: Can I get a printable CMS-1500 form for a claim using its correlation ID?
  - id: GetPDF1500
    intent: Get a CMS-1500 PDF by transaction ID
    question: How do I get the CMS-1500 claim form PDF for a professional claim from its transaction ID?
  phrasing_ops: 8
  slug: stedi-claim-submission-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Coordination of benefits API from Stedi — 1 operation(s) for coordination of benefits.
  name: Stedi Coordination of benefits API
  phrasing_intents:
  - id: CoordinationOfBenefits
    intent: Check coordination of benefits
    question: How can I find out whether a patient has other insurance that should pay first?
  phrasing_ops: 1
  slug: stedi-coordination-of-benefits-api
- baseURL: https://enrollments.us.stedi.com/2024-09-01
  baseurl_source: declared
  description: The Documents API from Stedi — 2 operation(s) for documents.
  name: Stedi Documents API
  phrasing_intents:
  - id: DeleteEnrollmentDocument
    intent: Delete an enrollment document
    question: How do I remove a PDF I uploaded to a transaction enrollment?
  - id: CreateEnrollmentDocumentDownload
    intent: Get a download link for an enrollment document
    question: How do I download a PDF that's attached to an enrollment?
  phrasing_ops: 2
  slug: stedi-documents-api
- baseURL: https://enrollments.us.stedi.com/2024-09-01
  baseurl_source: declared
  description: The Enrollments API from Stedi — 4 operation(s) for enrollments.
  name: Stedi Enrollments API
  phrasing_intents:
  - id: ListEnrollments
    intent: List transaction enrollments
    question: Which of my providers' payer enrollments are still in progress?
  - id: CreateEnrollment
    intent: Create a payer transaction enrollment
    question: How do I enroll a provider with a payer so they can receive ERAs?
  - id: ExportEnrollmentsCsv
    intent: Export enrollments to CSV
    question: Can I download my enrollment records as a spreadsheet?
  - id: DeleteEnrollment
    intent: Delete a draft enrollment
    question: How do I throw away an enrollment request I never submitted?
  - id: GetEnrollment
    intent: Get an enrollment
    question: What's the current status of a specific enrollment request?
  - id: UpdateEnrollment
    intent: Update a draft enrollment
    question: Can I edit an enrollment after it has been submitted?
  - id: CreateEnrollmentDocumentUpload
    intent: Get an upload URL for an enrollment PDF
    question: How do I attach a signed PDF form to an enrollment task?
  phrasing_ops: 7
  slug: stedi-enrollments-api
- baseURL: https://events.us.stedi.com/2026-02-01
  baseurl_source: declared
  description: The Events API from Stedi — 3 operation(s) for events.
  name: Stedi Events API
  phrasing_intents:
  - id: RetryEvent
    intent: Re-send a processing event
    question: My webhook missed an event -- can I have it sent again?
  - id: EventDestinationsListEvents
    intent: List events
    question: Which events failed to deliver on my account?
  - id: EventDestinationsGetEvent
    intent: Get an event
    question: What payload and delivery status does a particular event have?
  phrasing_ops: 3
  slug: stedi-events-api
- baseURL: https://core.us.stedi.com/2023-08-01
  baseurl_source: declared
  description: The Executions API from Stedi — 11 operation(s) for executions.
  name: Stedi Executions API
  phrasing_intents:
  - id: ListExecutions
    intent: List file executions
    question: Which EDI files did Stedi process recently?
  - id: RetryExecutions
    intent: Retry failed file executions
    question: How do I reprocess all the EDI files that failed?
  - id: GetExecution
    intent: Get a file execution
    question: What is the status of one specific file execution?
  - id: ListExecutionFaults
    intent: List a file execution's faults
    question: Why did my EDI file fail to process?
  - id: GetExecutionInputDocument
    intent: Get a file execution's input document
    question: Can I see the original EDI file a file execution received before translation?
  - id: GetExecutionInputDocumentUrl
    intent: Get a download URL for an execution's input
    question: How do I download a very large original input file from a file execution?
  - id: GetExecutionMetadataDocument
    intent: Get a file execution's metadata document
    question: Where can I see the metadata Stedi recorded about a processed file?
  - id: GetExecutionMetadataDocumentUrl
    intent: Get a download URL for execution metadata
    question: How do I download the metadata for a large X12 file execution?
  phrasing_ops: 11
  slug: stedi-executions-api
- baseURL: https://core.us.stedi.com/2023-08-01
  baseurl_source: declared
  description: The Fragments API from Stedi — 1 operation(s) for fragments.
  name: Stedi Fragments API
  phrasing_intents:
  - id: CreateOutboundFragment
    intent: Stage an EDI fragment for outbound delivery
    question: How do I build a large outbound EDI transaction piece by piece using fragments?
  phrasing_ops: 1
  slug: stedi-fragments-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Insurance discovery API from Stedi — 2 operation(s) for insurance discovery.
  name: Stedi Insurance discovery API
  phrasing_intents:
  - id: InsuranceDiscoveryCheck
    intent: Run an insurance discovery check
    question: How can I find a patient's health insurance when they don't know who their payer is?
  - id: GetInsuranceDiscoveryCheck
    intent: Get insurance discovery results
    question: Did my insurance discovery check find any coverage for the patient?
  phrasing_ops: 2
  slug: stedi-insurance-discovery-api
- baseURL: https://core.us.stedi.com/2023-08-01
  baseurl_source: declared
  description: The Partnerships API from Stedi — 3 operation(s) for partnerships.
  name: Stedi Partnerships API
  phrasing_intents:
  - id: GenerateTransactionGroupEdi
    intent: Generate EDI from a staged transaction group
    question: Once I've staged several transactions, how do I bundle them into one EDI file for my trading partner?
  - id: CreateTransactionGroup
    intent: Stage a transaction in a transaction group
    question: How do I queue up outbound transactions so they can be sent together later?
  - id: CreatePartnershipOutboundTransaction
    intent: Send a single transaction as an EDI file
    question: What's the simplest way to send one EDI transaction to a trading partner?
  phrasing_ops: 3
  slug: stedi-partnerships-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Payers API from Stedi — 4 operation(s) for payers.
  name: Stedi Payers API
  phrasing_intents:
  - id: GetPayerRecord
    intent: Get a payer by Stedi payer ID
    question: What transactions does a specific payer support?
  - id: ListPayerRecords
    intent: List supported payers
    question: Which insurance payers does Stedi support?
  - id: ListPayerRecordsCsv
    intent: Download the payer list as CSV
    question: Can I get the complete payer list as a CSV spreadsheet?
  - id: SearchPayers
    intent: Search payers
    question: Which payers support real-time eligibility checks in Texas?
  phrasing_ops: 4
  slug: stedi-payers-api
- baseURL: https://core.us.stedi.com/2023-08-01
  baseurl_source: declared
  description: The Polling API from Stedi — 2 operation(s) for polling.
  name: Stedi Polling API
  phrasing_intents:
  - id: ListPollingExecutions
    intent: Poll for newly processed file executions
    question: How can I check for new EDI files Stedi has processed without using webhooks?
  - id: ListPollingTransactions
    intent: Poll for newly processed transactions
    question: Is there a way to poll for new transactions instead of receiving events?
  phrasing_ops: 2
  slug: stedi-polling-api
- baseURL: https://enrollments.us.stedi.com/2024-09-01
  baseurl_source: declared
  description: The Providers API from Stedi — 2 operation(s) for providers.
  name: Stedi Providers API
  phrasing_intents:
  - id: ListProviders
    intent: List providers
    question: Which providers have I set up for enrollment?
  - id: CreateProvider
    intent: Create a provider record
    question: How do I add a new provider before enrolling them with payers?
  - id: DeleteProvider
    intent: Delete a provider
    question: How do I remove a provider record I no longer need?
  - id: GetProvider
    intent: Get a provider
    question: What contact details are on a specific provider record?
  - id: UpdateProvider
    intent: Update a provider's name or contacts
    question: Can I change a provider's NPI or tax ID after creating it?
  phrasing_ops: 5
  slug: stedi-providers-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Real-time claim status API from Stedi — 2 operation(s) for real-time claim status.
  name: Stedi Real-time claim status API
  phrasing_intents:
  - id: ClaimStatus
    intent: Check a claim's status in real time
    question: How do I find out whether a payer has paid or denied a claim I submitted?
  - id: ClaimStatusRawX12
    intent: Check claim status with raw X12
    question: Can I send a 276 claim status request as raw X12 EDI?
  phrasing_ops: 2
  slug: stedi-real-time-claim-status-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Real-time eligibility check API from Stedi — 2 operation(s) for real-time eligibility check.
  name: Stedi Real-time eligibility check API
  phrasing_intents:
  - id: EligibilityCheck
    intent: Check a patient's eligibility in real time
    question: How do I verify a patient's insurance coverage and benefits before an appointment?
  - id: EligibilityRawX12Check
    intent: Check eligibility with raw X12
    question: Can I send a 270 eligibility request as raw X12 and get a 271 back?
  phrasing_ops: 2
  slug: stedi-real-time-eligibility-check-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Remittances API from Stedi — 2 operation(s) for remittances.
  name: Stedi Remittances API
  phrasing_intents:
  - id: ConvertReport835
    intent: Get an 835 remittance advice as JSON
    question: How do I see what a payer paid and adjusted on my claims from an ERA?
  - id: GetElectronicRemittanceAdvicePdf
    intent: Get an 835 remittance advice as a PDF
    question: Can I get a printable PDF of an ERA?
  phrasing_ops: 2
  slug: stedi-remittances-api
- baseURL: https://enrollments.us.stedi.com/2024-09-01
  baseurl_source: declared
  description: The Tasks API from Stedi — 1 operation(s) for tasks.
  name: Stedi Tasks API
  phrasing_intents:
  - id: UpdateTaskPost
    intent: Complete an enrollment task
    question: How do I mark an enrollment task as done?
  phrasing_ops: 1
  slug: stedi-tasks-api
- baseURL: https://core.us.stedi.com/2023-08-01
  baseurl_source: declared
  description: The Transactions API from Stedi — 11 operation(s) for transactions.
  name: Stedi Transactions API
  phrasing_intents:
  - id: ListTransactions
    intent: List transactions
    question: Which EDI transactions did I exchange with a trading partner this month?
  - id: GetTransaction
    intent: Get a transaction
    question: What are the details of one processed transaction?
  - id: GetTransactionAttachmentDocument
    intent: Get a transaction attachment document
    question: How do I read an attachment artifact produced for a transaction?
  - id: GetTransactionAttachmentDocumentUrl
    intent: Get a download URL for a transaction attachment
    question: How do I download a large transaction attachment?
  - id: GetTransactionFragment
    intent: Get a transaction fragment's metadata
    question: What metadata is recorded for one fragment of a large transaction?
  - id: GetTransactionFragmentOutputDocument
    intent: Get a fragment's translated output
    question: What does a single transaction fragment look like after translation?
  - id: GetTransactionFragmentOutputDocumentUrl
    intent: Get a download URL for a fragment's output
    question: How do I download the translated output of a large transaction fragment?
  - id: GetTransactionInputDocument
    intent: Get a transaction's input document
    question: What did a transaction look like before Stedi translated it?
  phrasing_ops: 11
  slug: stedi-transactions-api
- baseURL: https://core.us.stedi.com/2023-08-01
  baseurl_source: declared
  description: The X12 API from Stedi — 1 operation(s) for x12.
  name: Stedi X12 API
  phrasing_intents:
  - id: GenerateEdi
    intent: Generate and deliver EDI to a trading partner
    question: How do I turn JSON transaction data into X12 EDI and send it to a trading partner?
  phrasing_ops: 1
  slug: stedi-x12-api
- baseURL: https://manager.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Batch Eligibility Check API from Stedi — 4 operation(s) for submitting and polling asynchronous batches of X12 270 eligibility checks.
  name: Stedi Batch Eligibility Check API
  phrasing_intents:
  - id: BatchEligibilityChecks
    intent: Submit a batch of eligibility checks
    question: How do I run eligibility checks for a whole list of patients at once in Stedi?
  - id: GetBatch
    intent: Check the status of an eligibility batch
    question: Has my batch of eligibility checks finished processing yet?
  - id: GetBatchItems
    intent: List the checks inside an eligibility batch
    question: Which individual eligibility checks in my batch are still pending?
  - id: BatchEligibilityPolling
    intent: Poll for completed batch eligibility results
    question: How do I pull the actual benefits responses from my asynchronous eligibility checks?
  phrasing_ops: 4
  slug: stedi-batch-eligibility-check-api
- baseURL: https://manager.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Eligibility PDF API from Stedi — 1 operation(s) for retrieving a rendered PDF of an X12 271 eligibility response.
  name: Stedi Eligibility PDF API
  phrasing_intents:
  - id: GetEligibilityCheckPdf
    intent: Get an eligibility check result as a PDF
    question: Can I get a patient's eligibility and benefits response as a PDF to share with staff?
  phrasing_ops: 1
  slug: stedi-eligibility-pdf-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Destinations API from Stedi — 4 operation(s) for destinations.
  name: Stedi Destinations API
  phrasing_intents:
  - id: EventDestinationsListDestinations
    intent: List event destinations
    question: Which webhook destinations are set up on my account?
  - id: EventDestinationsCreateDestination
    intent: Create an event destination
    question: How do I get Stedi to send event notifications to my own webhook URL?
  - id: EventDestinationsDeleteDestination
    intent: Delete an event destination
    question: How do I permanently remove a webhook destination?
  - id: EventDestinationsGetDestination
    intent: Get an event destination
    question: What URL and event types is a specific destination configured with?
  - id: EventDestinationsUpdateDestination
    intent: Update an event destination
    question: Can I change the URL an existing destination sends events to?
  - id: EventDestinationsGetDestinationSecret
    intent: Get a destination's signing secret
    question: Where do I find the secret to verify that event payloads really came from Stedi?
  - id: EventDestinationsRotateDestinationSecret
    intent: Rotate a destination's signing secret
    question: How do I rotate the signing secret on a webhook destination?
  phrasing_ops: 7
  slug: stedi-destinations-api
- baseURL: https://healthcare.us.stedi.com/2024-04-01
  baseurl_source: declared
  description: The Eligibility Check API from Stedi — 1 operation(s) for eligibility check.
  name: Stedi Eligibility Check API
  phrasing_intents:
  - id: postEligibilityCheck
    intent: Run a healthcare eligibility check
    question: How do I check whether a patient's insurance coverage is active before an appointment?
  phrasing_ops: 1
  slug: stedi-eligibility-check-api
arazzos:
- description: Resolve a claim-status-capable payer, run an X12 276 inquiry, and convert the X12 277 status report.
  name: Stedi X12 276/277 Claim Status Inquiry
  slug: stedi-claim-status-inquiry-workflow
- description: Locate the right payer in the Stedi network, then run an X12 270 eligibility inquiry and read the 271 benefits response.
  name: Stedi X12 270/271 Eligibility and Benefits Check
  slug: stedi-eligibility-check-workflow
- description: Start an insurance discovery check for a patient, then poll until the X12 270/271 coverage search completes and read the discovered coverage.
  name: Stedi Insurance Discovery
  slug: stedi-insurance-discovery-workflow
- description: Submit an X12 837 professional claim, check its 277 status, and retrieve the converted X12 835 remittance.
  name: Stedi X12 837 Professional Claim Lifecycle
  slug: stedi-professional-claim-lifecycle-workflow
- description: Create a provider, open an enrollment, upload the signed agreement, and read the enrollment status for X12 835 ERA/EFT transactions.
  name: Stedi Provider Enrollment for X12 835 ERA/EFT
  slug: stedi-provider-enrollment-workflow
artifact_total: 82
asyncapis:
- description: 'Stedi publishes NO AsyncAPI document of its own. This document was assembled by API Evangelist from Stedi''s own published sources: the V1EventPayload schema in Stedi''s OpenAPI for the Events API, the '
  name: Stedi Event Destinations (webhooks)
  slug: stedi-event-destinations-asyncapi
collections:
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments API
  slug: open-stedi-claim-acknowledgments-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Claim Attachments API
  slug: open-stedi-claim-attachments-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Claim submission API
  slug: open-stedi-claim-submission-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Coordination of benefits API
  slug: open-stedi-coordination-of-benefits-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Documents API
  slug: open-stedi-documents-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Enrollments API
  slug: open-stedi-enrollments-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Events API
  slug: open-stedi-events-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Executions API
  slug: open-stedi-executions-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Fragments API
  slug: open-stedi-fragments-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Insurance discovery API
  slug: open-stedi-insurance-discovery-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Partnerships API
  slug: open-stedi-partnerships-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Payer API
  slug: open-stedi-payer-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Payers API
  slug: open-stedi-payers-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Polling API
  slug: open-stedi-polling-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Providers API
  slug: open-stedi-providers-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Real-time claim status API
  slug: open-stedi-real-time-claim-status-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Real-time eligibility check API
  slug: open-stedi-real-time-eligibility-check-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Remittances API
  slug: open-stedi-remittances-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Tasks API
  slug: open-stedi-tasks-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments Transactions API
  slug: open-stedi-transactions-api
- collection_type: open
  name: Stedi Healthcare Claims Claim acknowledgments X12 API
  slug: open-stedi-x12-api
common:
- group: other
  href: https://artifacts.apis.io/stedi/overlays/stedi-payer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stedi-payer-overlay.yaml
- group: other
  href: https://artifacts.apis.io/stedi/capabilities/stedi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stedi-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/stedi/overlays/stedi-event-destinations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stedi-event-destinations-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/stedi/agentic-access/stedi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stedi-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/stedi/security/stedi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stedi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stedi/security/stedi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stedi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/stedi/authentication/stedi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stedi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.stedi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.stedi.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stedi
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/Stedi/openApi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stedi-inc
- group: other
  title: ''
  type: X
  url: https://x.com/stedi
- group: company
  title: ''
  type: Blog
  url: https://www.stedi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stedi.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stedi.com
- group: design
  href: https://artifacts.apis.io/stedi/vocabulary/stedi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stedi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stedi/json-ld/stedi-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/stedi-context.jsonld
- group: commercial
  href: https://artifacts.apis.io/stedi/plans/stedi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stedi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/stedi/rate-limits/stedi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stedi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/stedi/finops/stedi-finops.yml
  title: ''
  type: FinOps
  url: finops/stedi-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
- group: build
  href: https://artifacts.apis.io/stedi/packages/stedi-packages.yml
  title: ''
  type: Packages
  url: packages/stedi-packages.yml
- group: build
  href: https://artifacts.apis.io/stedi/packages/stedi-packages.yml
  title: ''
  type: SDKs
  url: packages/stedi-packages.yml
- group: agent
  href: https://artifacts.apis.io/stedi/mcp/stedi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stedi-mcp.yml
- group: build
  href: https://artifacts.apis.io/stedi/mcp/stedi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/stedi-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/stedi/well-known/stedi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stedi-well-known.yml
- group: auth
  href: https://artifacts.apis.io/stedi/well-known/stedi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stedi-security.txt
- group: agent
  href: https://artifacts.apis.io/stedi/llms/stedi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stedi-llms.txt
- group: design
  href: https://artifacts.apis.io/stedi/conformance/stedi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stedi-conformance.yml
- group: auth
  href: https://artifacts.apis.io/stedi/security/stedi-trust-center.yml
  title: ''
  type: Compliance
  url: security/stedi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/stedi/security/stedi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stedi-trust-center.yml
- group: design
  href: https://artifacts.apis.io/stedi/conventions/stedi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stedi-conventions.yml
- group: design
  href: https://artifacts.apis.io/stedi/conventions/stedi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/stedi-conventions.yml
- group: design
  href: https://artifacts.apis.io/stedi/errors/stedi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stedi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stedi/lifecycle/stedi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stedi-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/stedi/lifecycle/stedi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/stedi-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/stedi/security/stedi-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/stedi-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/stedi/sandbox/stedi-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/stedi-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/stedi/changelog/stedi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/stedi-changelog.yml
- group: design
  href: https://artifacts.apis.io/stedi/data-model/stedi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stedi-data-model.yml
- group: auth
  href: https://artifacts.apis.io/stedi/scopes/stedi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/stedi-scopes.yml
- group: design
  href: https://artifacts.apis.io/stedi/asyncapi/stedi-event-destinations-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/stedi-event-destinations-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/stedi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.stedi.com/docs/healthcare
- group: docs
  title: ''
  type: APIReference
  url: https://www.stedi.com/docs/healthcare/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stedi.com/docs/healthcare/intro-eligibility-checks
- group: operate
  title: ''
  type: Support
  url: https://www.stedi.com/support
- group: start
  title: ''
  type: SignUp
  url: https://portal.stedi.com/auth/sign-up
- group: start
  title: ''
  type: Login
  url: https://portal.stedi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stedi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.stedi.com/legal/privacy-notice-b91ef9d6
- group: operate
  title: ''
  type: ChangeLogRSS
  url: https://www.stedi.com/changelog/feed.xml
created: 2026-06-12
description: Stedi is the only API-first programmable healthcare clearinghouse, enabling health tech companies to submit claims, verify eligibility, and process electronic remittance advice (ERA) through a modern JSON API. The platform supports real-time X12 EDI transaction processing including eligibility checks (270/271), professional and institutional claim submissions (837), claim status inquiries (276/277), and electronic remittance advice (835). Stedi provides both SFTP and REST API access, webhooks for event-driven workflows, a sandbox test environment, and an MCP server for AI-assisted integration. Public OpenAPI specifications are available for all core APIs via the Stedi GitHub organization, and pricing is purely metered with no monthly minimums or setup fees.
examples:
- key_count: 4
  name: Stedi Claims Examples
  slug: stedi-claims-examples
- key_count: 35
  name: Stedi Core Examples
  slug: stedi-core-examples
- key_count: 18
  name: Stedi Enrollment Examples
  slug: stedi-enrollment-examples
- key_count: 2
  name: Stedi Event Destinations Examples
  slug: stedi-event-destinations-examples
- key_count: 36
  name: Stedi Healthcare Examples
  slug: stedi-healthcare-examples
- key_count: 4
  name: Stedi Payers Examples
  slug: stedi-payers-examples
finops:
- has_sources: true
  method: derived
  name: Stedi Finops
  primary_unit: discovery check
  service_category: ''
  slug: stedi-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stedi.png
json_schemas:
- name: Stedi Claims Schemas
  property_count: 0
  slug: stedi-claims-schemas
- name: Stedi Core Schemas
  property_count: 0
  slug: stedi-core-schemas
- name: Stedi Enrollment Schemas
  property_count: 0
  slug: stedi-enrollment-schemas
- name: Stedi Event-Destinations Schemas
  property_count: 0
  slug: stedi-event-destinations-schemas
- name: Stedi Healthcare Schemas
  property_count: 0
  slug: stedi-healthcare-schemas
- name: Stedi Payers Schemas
  property_count: 0
  slug: stedi-payers-schemas
jsonld:
- class_count: 854
  name: Stedi Context
  property_count: 0
  slug: stedi-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.us.stedi.com over HTTP requiring an API key; 2 tools listed.
  name: Stedi MCP Server
  slug: stedi-healthcare
modified: '2026-08-15'
name: Stedi
nav: Providers
network: true
overview: 'Stedi publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Claim acknowledgments API, Claim Attachments API, Claim submission API, and 21 more. Tagged areas include EDI, Electronic Data Interchange, Healthcare, Clearinghouse, and X12.


  The Stedi catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Stedi''s developer surface includes authentication, documentation, engineering blog, pricing, sandbox, changelog, API reference, and 45 more developer resources.'
plans:
- name: Stedi Plans Pricing
  plan_count: 26
  slug: stedi-plans-pricing
- name: Stedi Price Estimates
  plan_count: 0
  slug: stedi-price-estimates
random_paper: 9
rate_limits:
- limit_count: 7
  name: Stedi Rate Limits
  slug: stedi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Stedi — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: stedi-jsonschema-spectral-rules
scopes:
- name: Stedi Scopes
  scope_count: 1
  slug: stedi-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 79.4
  coverage:
    artifact_dirs: 36
    catalog_earned: 82.8
    catalog_earned_first_party: 24.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 100.0
    contract_governance: 41.7
    contract_quality: 68.0
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 84.2
  previous_composite: 78.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 36.0
      total: 25
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 46.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stedi/stedi-2026-06-20T194534.png
security:
- kind: authentication
  name: Stedi Authentication
  slug: stedi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stedi Domain Security
  slug: stedi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stedi Vulnerability Disclosure
  slug: stedi-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Stedi Trust Center
  slug: stedi-trust-center
  summary_line: SOC 2 Type II, HIPAA
skill_count: 6
skills:
- name: Check the status of a submitted claim
  slug: stedi-check-claim-status
- name: Check patient eligibility and benefits
  slug: stedi-check-eligibility
- name: Discover a patient's insurance coverage
  slug: stedi-discover-insurance
- name: Enroll a provider for ERA/EFT
  slug: stedi-enroll-provider-for-era
- name: Receive and verify Stedi events
  slug: stedi-receive-events
- name: Submit a professional claim and collect the remittance
  slug: stedi-submit-professional-claim
slug: stedi
tags:
- EDI
- Electronic Data Interchange
- Healthcare
- Clearinghouse
- X12
- Claims
- Eligibility
- HIPAA
- Revenue Cycle Management
- B2B Integration
- Health Insurance
website: https://www.stedi.com
---
