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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 128
  human_in_the_loop: 1
  name: Root Agentic Access
  operation_count: 198
  slug: root-agentic-access
  summary_line: 198 operations · 128 acting · 1 human-in-the-loop
api_count: 18
apis:
- description: 'The Root Bind API enables distribution partners to embed auto insurance quoting, checkout, and servicing within their own applications. Supports both a hosted experience (Root-managed checkout) and a '
  name: Root Bind API
  slug: root-bind-api
- description: The Applications API from Root Insurance — 16 operation(s) for applications.
  name: Root Insurance Applications API
  slug: root-applications-api
- description: The Calls API from Root Insurance — 4 operation(s) for calls.
  name: Root Insurance Calls API
  slug: root-calls-api
- description: The Claims API from Root Insurance — 31 operation(s) for claims.
  name: Root Insurance Claims API
  slug: root-claims-api
- description: The Complaints API from Root Insurance — 10 operation(s) for complaints.
  name: Root Insurance Complaints API
  slug: root-complaints-api
- description: The Data exports API from Root Insurance — 9 operation(s) for data exports.
  name: Root Insurance Data exports API
  slug: root-data-exports-api
- description: The Data stores API from Root Insurance — 4 operation(s) for data stores.
  name: Root Insurance Data stores API
  slug: root-data-stores-api
- description: The Embed API from Root Insurance — 2 operation(s) for embed.
  name: Root Insurance Embed API
  slug: root-embed-api
- description: The Files API from Root Insurance — 1 operation(s) for files.
  name: Root Insurance Files API
  slug: root-files-api
- description: The Leads API from Root Insurance — 2 operation(s) for leads.
  name: Root Insurance Leads API
  slug: root-leads-api
- description: The Notifications API from Root Insurance — 3 operation(s) for notifications.
  name: Root Insurance Notifications API
  slug: root-notifications-api
- description: The Payment Methods API from Root Insurance — 7 operation(s) for payment methods.
  name: Root Insurance Payment Methods API
  slug: root-payment-methods-api
- description: The Payments API from Root Insurance — 6 operation(s) for payments.
  name: Root Insurance Payments API
  slug: root-payments-api
- description: The Policies API from Root Insurance — 32 operation(s) for policies.
  name: Root Insurance Policies API
  slug: root-policies-api
- description: The Policyholders API from Root Insurance — 7 operation(s) for policyholders.
  name: Root Insurance Policyholders API
  slug: root-policyholders-api
- description: The Quotes API from Root Insurance — 1 operation(s) for quotes.
  name: Root Insurance Quotes API
  slug: root-quotes-api
- description: The Secret keys API from Root Insurance — 2 operation(s) for secret keys.
  name: Root Insurance Secret keys API
  slug: root-secret-keys-api
- description: The Webhooks API from Root Insurance — 9 operation(s) for webhooks.
  name: Root Insurance Webhooks API
  slug: root-webhooks-api
artifact_total: 329
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Root Applications API
  slug: open-root-applications-api
- collection_type: open
  name: Root Applications Calls API
  slug: open-root-calls-api
- collection_type: open
  name: Root Applications Claims API
  slug: open-root-claims-api
- collection_type: open
  name: Root Applications Complaints API
  slug: open-root-complaints-api
- collection_type: open
  name: Root Applications Data exports API
  slug: open-root-data-exports-api
- collection_type: open
  name: Root Applications Data stores API
  slug: open-root-data-stores-api
- collection_type: open
  name: Root Applications Embed API
  slug: open-root-embed-api
- collection_type: open
  name: Root Applications Files API
  slug: open-root-files-api
- collection_type: open
  name: Root Applications Leads API
  slug: open-root-leads-api
- collection_type: open
  name: Root Applications Notifications API
  slug: open-root-notifications-api
- collection_type: open
  name: Root Applications Payment Methods API
  slug: open-root-payment-methods-api
- collection_type: open
  name: Root Applications Payments API
  slug: open-root-payments-api
- collection_type: open
  name: Root Applications Policies API
  slug: open-root-policies-api
- collection_type: open
  name: Root Applications Policyholders API
  slug: open-root-policyholders-api
- collection_type: open
  name: Root Applications Quotes API
  slug: open-root-quotes-api
- collection_type: open
  name: Root Applications Secret keys API
  slug: open-root-secret-keys-api
- collection_type: open
  name: Root Applications Webhooks API
  slug: open-root-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/root-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/root-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/root-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/root-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.joinroot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rootplatform.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Root-App
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rootinsurance
- group: company
  title: ''
  type: Blog
  url: https://blog.joinroot.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://rootplatform.com/plans
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rootplatform.com/
- group: other
  title: ''
  type: X
  url: https://x.com/joinroot
- group: commercial
  title: ''
  type: Plans
  url: plans/root-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/root-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/root-finops.yml
created: '2026-06-13'
description: Root Insurance is a usage-based auto insurance company that prices policies primarily based on driving behavior captured via smartphone telematics. Root provides a REST API platform for insurers, MGAs, and distribution partners to build, embed, and operate insurance products — covering quoting, policy administration, claims processing, premium collections, and data management. The Root Bind API enables partners to embed auto insurance quoting and checkout directly into their applications.
examples:
- key_count: 1
  name: Acknowledge Approved Request
  slug: acknowledge-approved-request
- key_count: 12
  name: Acknowledge Approved Response 200
  slug: acknowledge-approved-response-200
- key_count: 1
  name: Acknowledge Goodwill Request
  slug: acknowledge-goodwill-request
- key_count: 13
  name: Acknowledge Goodwill Response 200
  slug: acknowledge-goodwill-response-200
- key_count: 1
  name: Acknowledge No Claim Request
  slug: acknowledge-no-claim-request
- key_count: 14
  name: Acknowledge No Claim Response 200
  slug: acknowledge-no-claim-response-200
- key_count: 1
  name: Acknowledge Repudiated Request
  slug: acknowledge-repudiated-request
- key_count: 13
  name: Acknowledge Repudiated Response 200
  slug: acknowledge-repudiated-response-200
- key_count: 23
  name: Activate Policy Response 200
  slug: activate-policy-response-200
- key_count: 8
  name: Add Application Attachments Response 200
  slug: add-application-attachments-response-200
- key_count: 14
  name: Apply Alteration Package Response 200
  slug: apply-alteration-package-response-200
- key_count: 14
  name: Apply Application Alteration Package Response 200
  slug: apply-application-alteration-package-response-200
- key_count: 2
  name: Approve Claim Request
  slug: approve-claim-request
- key_count: 12
  name: Approve Claim Response 200
  slug: approve-claim-response-200
- key_count: 11
  name: Approve Fulfillment Request Response 200
  slug: approve-fulfillment-request-response-200
- key_count: 8
  name: Archive Application Attachment Response 200
  slug: archive-application-attachment-response-200
- key_count: 8
  name: Archive Data Store Entity Response 200
  slug: archive-data-store-entity-response-200
- key_count: 7
  name: Archive Data Store Response 200
  slug: archive-data-store-response-200
- key_count: 10
  name: Archive Scheduled Data Export Response 200
  slug: archive-scheduled-data-export-response-200
- key_count: 1
  name: Archive Webhook Response 200
  slug: archive-webhook-response-200
- key_count: 1
  name: Assign Policy Payment Method Request
  slug: assign-policy-payment-method-request
- key_count: 3
  name: Assign Policy Payment Method Response 200
  slug: assign-policy-payment-method-response-200
- key_count: 1
  name: Bulk Reassign Policy User Groups Request
  slug: bulk-reassign-policy-user-groups-request
- key_count: 2
  name: Bulk Reassign Policy User Groups Response 200
  slug: bulk-reassign-policy-user-groups-response-200
- key_count: 9
  name: Cancel Payment Coupon Response 200
  slug: cancel-payment-coupon-response-200
- key_count: 1
  name: Cancel Policy Request
  slug: cancel-policy-request
- key_count: 26
  name: Cancel Policy Response 200
  slug: cancel-policy-response-200
- key_count: 1
  name: Claim Add Note Request
  slug: claim-add-note-request
- key_count: 5
  name: Claim Add Note Response 200
  slug: claim-add-note-response-200
- key_count: 4
  name: Claim Archive Attachment Response 200
  slug: claim-archive-attachment-response-200
- key_count: 4
  name: Claim Create Attachment Request
  slug: claim-create-attachment-request
- key_count: 8
  name: Claim Create Attachment Response 200
  slug: claim-create-attachment-response-200
- key_count: 3
  name: Claim Link Policy Request
  slug: claim-link-policy-request
- key_count: 13
  name: Claim Link Policy Response 200
  slug: claim-link-policy-response-200
- key_count: 1
  name: Close Claim Request
  slug: close-claim-request
- key_count: 12
  name: Close Claim Response 200
  slug: close-claim-response-200
- key_count: 8
  name: Close Complaint Response 200
  slug: close-complaint-response-200
- key_count: 4
  name: Complaint Archive Attachment Response 200
  slug: complaint-archive-attachment-response-200
- key_count: 8
  name: Complaint Create Attachment Response 200
  slug: complaint-create-attachment-response-200
- key_count: 5
  name: Complaint Create Note Response 200
  slug: complaint-create-note-response-200
- key_count: 9
  name: Complaint Link Policy Response 200
  slug: complaint-link-policy-response-200
- key_count: 10
  name: Complaint Update Complainant Response 200
  slug: complaint-update-complainant-response-200
- key_count: 10
  name: Create A Complaint Response 200
  slug: create-a-complaint-response-200
- key_count: 2
  name: Create Alteration Package Request
  slug: create-alteration-package-request
- key_count: 11
  name: Create Call Request
  slug: create-call-request
- key_count: 11
  name: Create Call Response 200
  slug: create-call-response-200
- key_count: 9
  name: Create Claim Request
  slug: create-claim-request
- key_count: 15
  name: Create Claim Response 200
  slug: create-claim-response-200
- key_count: 2
  name: Create Data Store Entity Request
  slug: create-data-store-entity-request
- key_count: 8
  name: Create Data Store Entity Response 200
  slug: create-data-store-entity-response-200
- key_count: 4
  name: Create Data Store Request
  slug: create-data-store-request
- key_count: 10
  name: Create Data Store Response 200
  slug: create-data-store-response-200
- key_count: 5
  name: Create External Notification Request
  slug: create-external-notification-request
- key_count: 11
  name: Create External Notification Response 200
  slug: create-external-notification-response-200
- key_count: 7
  name: Create Lead Request
  slug: create-lead-request
- key_count: 12
  name: Create Lead Response 200
  slug: create-lead-response-200
- key_count: 7
  name: Create Or Update Lead Request
  slug: create-or-update-lead-request
- key_count: 12
  name: Create Or Update Lead Response 200
  slug: create-or-update-lead-response-200
- key_count: 1
  name: Create Policy Payment Request
  slug: create-policy-payment-request
- key_count: 22
  name: Create Policy Payment Response 200
  slug: create-policy-payment-response-200
- key_count: 4
  name: Create Policyholder Payment Method Request Collection_Module
  slug: create-policyholder-payment-method-request-collection_module
- key_count: 4
  name: Create Policyholder Payment Method Request Debit_Order
  slug: create-policyholder-payment-method-request-debit_order
- key_count: 2
  name: Create Policyholder Payment Method Request Eft
  slug: create-policyholder-payment-method-request-eft
- key_count: 3
  name: Create Policyholder Payment Method Request External
  slug: create-policyholder-payment-method-request-external
- key_count: 3
  name: Create Policyholder Payment Method Response 200 Card
  slug: create-policyholder-payment-method-response-200-card
- key_count: 3
  name: Create Policyholder Payment Method Response 200 Debit_Order
  slug: create-policyholder-payment-method-response-200-debit_order
- key_count: 2
  name: Create Policyholder Payment Method Response 200 Eft
  slug: create-policyholder-payment-method-response-200-eft
- key_count: 11
  name: Create Policyholder Request Company
  slug: create-policyholder-request-company
- key_count: 11
  name: Create Policyholder Request Individual
  slug: create-policyholder-request-individual
- key_count: 2
  name: Create Quote Request
  slug: create-quote-request
- key_count: 6
  name: Create Scheduled Data Export Request
  slug: create-scheduled-data-export-request
- key_count: 10
  name: Create Scheduled Data Export Response 200
  slug: create-scheduled-data-export-response-200
- key_count: 3
  name: Create Secret Key Request
  slug: create-secret-key-request
- key_count: 9
  name: Create Secret Key Response 200
  slug: create-secret-key-response-200
- key_count: 5
  name: Create Webhook Request
  slug: create-webhook-request
- key_count: 1
  name: Create Webhook Response 200
  slug: create-webhook-response-200
- key_count: 2
  name: Creating Policy Receipt Request
  slug: creating-policy-receipt-request
- key_count: 9
  name: Disable Webhook Response 200
  slug: disable-webhook-response-200
- key_count: 7
  name: Dismiss Payment Method Response 200
  slug: dismiss-payment-method-response-200
- key_count: 1
  name: Do Not Acknowledge Approved Request
  slug: do-not-acknowledge-approved-request
- key_count: 12
  name: Do Not Acknowledge Approved Response 200
  slug: do-not-acknowledge-approved-response-200
- key_count: 1
  name: Do Not Acknowledge Goodwill Request
  slug: do-not-acknowledge-goodwill-request
- key_count: 12
  name: Do Not Acknowledge Goodwill Response 200
  slug: do-not-acknowledge-goodwill-response-200
- key_count: 1
  name: Do Not Acknowledge No Claim Request
  slug: do-not-acknowledge-no-claim-request
- key_count: 12
  name: Do Not Acknowledge No Claim Response 200
  slug: do-not-acknowledge-no-claim-response-200
- key_count: 1
  name: Do Not Acknowledge Repudiated Request
  slug: do-not-acknowledge-repudiated-request
- key_count: 12
  name: Do Not Acknowledge Repudiated Response 200
  slug: do-not-acknowledge-repudiated-response-200
- key_count: 1
  name: Download File Response 400
  slug: download-file-response-400
- key_count: 1
  name: Download File Response 404
  slug: download-file-response-404
- key_count: 9
  name: Enable Webhook Response 200
  slug: enable-webhook-response-200
- key_count: 2
  name: Goodwill Claim Request
  slug: goodwill-claim-request
- key_count: 12
  name: Goodwill Claim Response 200
  slug: goodwill-claim-response-200
- key_count: 2
  name: Issue A Policy Request
  slug: issue-a-policy-request
- key_count: 24
  name: Issue A Policy Response 200
  slug: issue-a-policy-response-200
- key_count: 7
  name: Issue Aggregated Policy Response 200
  slug: issue-aggregated-policy-response-200
- key_count: 4
  name: Lookup Embed Session Response 200
  slug: lookup-embed-session-response-200
- key_count: 7
  name: Manual Verify Payment Method Response 200
  slug: manual-verify-payment-method-response-200
- key_count: 1
  name: No Claim Request
  slug: no-claim-request
- key_count: 12
  name: No Claim Response 200
  slug: no-claim-response-200
- key_count: 8
  name: Paid Out Claim Response 200
  slug: paid-out-claim-response-200
- key_count: 10
  name: Pause Scheduled Data Export Response 200
  slug: pause-scheduled-data-export-response-200
- key_count: 1
  name: Ping Webhook Response 200
  slug: ping-webhook-response-200
- key_count: 1
  name: Policy Add Note Request
  slug: policy-add-note-request
- key_count: 5
  name: Policy Add Note Response 200
  slug: policy-add-note-response-200
- key_count: 5
  name: Policy Allocate Eft Payment Request
  slug: policy-allocate-eft-payment-request
- key_count: 16
  name: Policy Allocate Eft Payment Response 200
  slug: policy-allocate-eft-payment-response-200
- key_count: 4
  name: Policy Archive Attachment Response 200
  slug: policy-archive-attachment-response-200
- key_count: 4
  name: Policy Collection Request Request
  slug: policy-collection-request-request
- key_count: 16
  name: Policy Collection Request Response 200
  slug: policy-collection-request-response-200
- key_count: 4
  name: Policy Create Attachment Request
  slug: policy-create-attachment-request
- key_count: 8
  name: Policy Create Attachment Response 200
  slug: policy-create-attachment-response-200
- key_count: 17
  name: Policy Debicheck Mandate Response 200
  slug: policy-debicheck-mandate-response-200
- key_count: 1
  name: Policyholder Add Note Request
  slug: policyholder-add-note-request
- key_count: 5
  name: Policyholder Add Note Response 200
  slug: policyholder-add-note-response-200
- key_count: 4
  name: Policyholder Create Attachment Request
  slug: policyholder-create-attachment-request
- key_count: 8
  name: Policyholder Create Attachment Response 200
  slug: policyholder-create-attachment-response-200
- key_count: 5
  name: Prevent Policy Lapse And Ntu Request Preventlapse
  slug: prevent-policy-lapse-and-NTU-request-preventLapse
- key_count: 2
  name: Prevent Policy Lapse And Ntu Request Resumelapse
  slug: prevent-policy-lapse-and-NTU-request-resumeLapse
- key_count: 26
  name: Reactivate Policy Response 200
  slug: reactivate-policy-response-200
- key_count: 1
  name: Redeem Payment Coupons Request
  slug: redeem-payment-coupons-request
- key_count: 11
  name: Reject A Fulfillment Request Response 200
  slug: reject-a-fulfillment-request-response-200
- key_count: 1
  name: Reopen Claim Request
  slug: reopen-claim-request
- key_count: 12
  name: Reopen Claim Response 200
  slug: reopen-claim-response-200
- key_count: 9
  name: Reopen Complaint Response 200
  slug: reopen-complaint-response-200
- key_count: 1
  name: Repudiate Claim Request
  slug: repudiate-claim-request
- key_count: 13
  name: Repudiate Claim Response 200
  slug: repudiate-claim-response-200
- key_count: 10
  name: Requote Application Response 200
  slug: requote-application-response-200
- key_count: 1
  name: Requote Policy Request
  slug: requote-policy-request
- key_count: 26
  name: Requote Policy Response 200
  slug: requote-policy-response-200
- key_count: 1
  name: Reschedule Scheduled Payment Response 200
  slug: reschedule-scheduled-payment-response-200
- key_count: 10
  name: Resume Scheduled Data Export Response 200
  slug: resume-scheduled-data-export-response-200
- key_count: 3
  name: Retrieve A Block State Response 200
  slug: retrieve-a-block-state-response-200
- key_count: 16
  name: Retrieve A Claim Response 200
  slug: retrieve-a-claim-response-200
- key_count: 9
  name: Retrieve A Complaint Response 200
  slug: retrieve-a-complaint-response-200
- key_count: 10
  name: Retrieve An Application Response 200
  slug: retrieve-an-application-response-200
- key_count: 14
  name: Retrieve Application Alteration Package Response 200
  slug: retrieve-application-alteration-package-response-200
- key_count: 1
  name: Retrieve Call Playback Url Response 200 Legacy_Url
  slug: retrieve-call-playback-url-response-200-legacy_url
- key_count: 6
  name: Retrieve Call Playback Url Response 200 With_Attachment
  slug: retrieve-call-playback-url-response-200-with_attachment
- key_count: 2
  name: Retrieve Call Playback Url Response 404
  slug: retrieve-call-playback-url-response-404
- key_count: 11
  name: Retrieve Call Response 200
  slug: retrieve-call-response-200
- key_count: 7
  name: Retrieve Claim Attachments Response 200
  slug: retrieve-claim-attachments-response-200
- key_count: 6
  name: Retrieve Data Export Run Response 200
  slug: retrieve-data-export-run-response-200
- key_count: 8
  name: Retrieve Data Store Entity Response 200
  slug: retrieve-data-store-entity-response-200
- key_count: 10
  name: Retrieve Data Store Response 200
  slug: retrieve-data-store-response-200
- key_count: 7
  name: Retrieve Policy Attachments Response 200
  slug: retrieve-policy-attachments-response-200
- key_count: 3
  name: Retrieve Policy Notes Response 200
  slug: retrieve-policy-notes-response-200
- key_count: 3
  name: Retrieve Policy Payment Method Response 200
  slug: retrieve-policy-payment-method-response-200
- key_count: 26
  name: Retrieve Policy Response 200
  slug: retrieve-policy-response-200
- key_count: 14
  name: Retrieve Policyholder Response 200
  slug: retrieve-policyholder-response-200
- key_count: 10
  name: Retrieve Scheduled Data Export Response 200
  slug: retrieve-scheduled-data-export-response-200
- key_count: 1
  name: Retrieve Webhook Response 200
  slug: retrieve-webhook-response-200
- key_count: 12
  name: Retry Webhook Queue Event Response 200
  slug: retry-webhook-queue-event-response-200
- key_count: 2
  name: Sandbox Only Update Policy Request
  slug: sandbox-only-update-policy-request
- key_count: 22
  name: Sandbox Only Update Policy Response 200
  slug: sandbox-only-update-policy-response-200
- key_count: 1
  name: Sandbox Only Update Policy Response 403
  slug: sandbox-only-update-policy-response-403
- key_count: 1
  name: Send To Capture Request
  slug: send-to-capture-request
- key_count: 9
  name: Send To Capture Response 200
  slug: send-to-capture-response-200
- key_count: 1
  name: Send To Review Request
  slug: send-to-review-request
- key_count: 12
  name: Send To Review Response 200
  slug: send-to-review-response-200
- key_count: 10
  name: Trigger Scheduled Data Export Response 200
  slug: trigger-scheduled-data-export-response-200
- key_count: 1
  name: Unschedule Scheduled Payment Response 200
  slug: unschedule-scheduled-payment-response-200
- key_count: 2
  name: Update A Payout Request Request
  slug: update-a-payout-request-request
- key_count: 14
  name: Update A Payout Request Response 200
  slug: update-a-payout-request-response-200
- key_count: 1
  name: Update Application Beneficiaries Request
  slug: update-application-beneficiaries-request
- key_count: 11
  name: Update Application Beneficiaries Response 200
  slug: update-application-beneficiaries-response-200
- key_count: 1
  name: Update Billing Amount Request
  slug: update-billing-amount-request
- key_count: 26
  name: Update Billing Amount Response 200
  slug: update-billing-amount-response-200
- key_count: 6
  name: Update Claimant Request
  slug: update-claimant-request
- key_count: 9
  name: Update Claimant Response 200
  slug: update-claimant-response-200
- key_count: 9
  name: Update Complaint Response 200
  slug: update-complaint-response-200
- key_count: 2
  name: Update Data Store Entity Request
  slug: update-data-store-entity-request
- key_count: 8
  name: Update Data Store Entity Response 200
  slug: update-data-store-entity-response-200
- key_count: 1
  name: Update Data Store Request
  slug: update-data-store-request
- key_count: 8
  name: Update Data Store Response 200
  slug: update-data-store-response-200
- key_count: 2
  name: Update External Notification Request
  slug: update-external-notification-request
- key_count: 11
  name: Update External Notification Response 200
  slug: update-external-notification-response-200
- key_count: 3
  name: Update Multiple Block States Response 200
  slug: update-multiple-block-states-response-200
- key_count: 2
  name: Update Payment Batch Request
  slug: update-payment-batch-request
- key_count: 18
  name: Update Payment Batch Response 200
  slug: update-payment-batch-response-200
- key_count: 1
  name: Update Payment Request
  slug: update-payment-request
- key_count: 22
  name: Update Payment Response 200
  slug: update-payment-response-200
- key_count: 1
  name: Update Policy Beneficiaries Request
  slug: update-policy-beneficiaries-request
- key_count: 23
  name: Update Policy Beneficiaries Response 200
  slug: update-policy-beneficiaries-response-200
- key_count: 2
  name: Update Policy Request
  slug: update-policy-request
- key_count: 22
  name: Update Policy Response 200
  slug: update-policy-response-200
- key_count: 6
  name: Update Policyholder Request
  slug: update-policyholder-request
- key_count: 14
  name: Update Policyholder Response 200
  slug: update-policyholder-response-200
- key_count: 7
  name: Update Scheduled Data Export Request
  slug: update-scheduled-data-export-request
- key_count: 10
  name: Update Scheduled Data Export Response 200
  slug: update-scheduled-data-export-response-200
- key_count: 3
  name: Update Webhook Request
  slug: update-webhook-request
- key_count: 7
  name: Update Webhook Response 200
  slug: update-webhook-response-200
- key_count: 3
  name: Updating A Block State Request
  slug: updating-a-block-state-request
- key_count: 1
  name: Updating A Block State Response 200
  slug: updating-a-block-state-response-200
- key_count: 5
  name: Updating A Claim Request
  slug: updating-a-claim-request
- key_count: 10
  name: Updating A Claim Response 200
  slug: updating-a-claim-response-200
- key_count: 11
  name: Upsert Policyholder Request Company
  slug: upsert-policyholder-request-company
- key_count: 11
  name: Upsert Policyholder Request Individual
  slug: upsert-policyholder-request-individual
- key_count: 2
  name: Upsert Secret Key Request
  slug: upsert-secret-key-request
- key_count: 9
  name: Upsert Secret Key Response 200
  slug: upsert-secret-key-response-200
finops:
- name: Root Finops
  service_category: ''
  slug: root-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/root.png
json_schemas:
- name: actor-type
  property_count: 0
  slug: actor-type
- name: alteration-package
  property_count: 5
  slug: alteration-package
- name: alteration-packages
  property_count: 0
  slug: alteration-packages
- name: application-alteration-hook
  property_count: 9
  slug: application-alteration-hook
- name: application-alteration-hooks
  property_count: 0
  slug: application-alteration-hooks
- name: application-alteration-package
  property_count: 14
  slug: application-alteration-package
- name: application-alteration-packages
  property_count: 0
  slug: application-alteration-packages
- name: application
  property_count: 27
  slug: application
- name: applications
  property_count: 0
  slug: applications
- name: attachment
  property_count: 7
  slug: attachment
- name: attachments
  property_count: 0
  slug: attachments
- name: bank-name
  property_count: 0
  slug: bank-name
- name: beneficiaries-request
  property_count: 0
  slug: beneficiaries-request
- name: beneficiaries
  property_count: 0
  slug: beneficiaries
- name: beneficiary-relationship
  property_count: 0
  slug: beneficiary-relationship
- name: call
  property_count: 12
  slug: call
- name: calls
  property_count: 0
  slug: calls
- name: cellphone-string
  property_count: 0
  slug: cellphone-string
- name: cellphone
  property_count: 2
  slug: cellphone
- name: claim
  property_count: 27
  slug: claim
- name: claims
  property_count: 0
  slug: claims
- name: collection-type
  property_count: 0
  slug: collection-type
- name: complaint
  property_count: 13
  slug: complaint
- name: complaints
  property_count: 0
  slug: complaints
- name: custom-event-type
  property_count: 0
  slug: custom-event-type
- name: daily-frequency
  property_count: 1
  slug: daily-frequency
- name: data-export-run-log-item
  property_count: 4
  slug: data-export-run-log-item
- name: data-export-run-log-items
  property_count: 0
  slug: data-export-run-log-items
- name: data-export-run
  property_count: 6
  slug: data-export-run
- name: data-export-runs
  property_count: 0
  slug: data-export-runs
- name: data-store-entities
  property_count: 0
  slug: data-store-entities
- name: data-store-entity
  property_count: 8
  slug: data-store-entity
- name: data-store
  property_count: 10
  slug: data-store
- name: data-stores
  property_count: 0
  slug: data-stores
- name: failure-action
  property_count: 0
  slug: failure-action
- name: fulfillment-request
  property_count: 12
  slug: fulfillment-request
- name: https-adapter
  property_count: 5
  slug: https-adapter
- name: lead
  property_count: 17
  slug: lead
- name: leads
  property_count: 0
  slug: leads
- name: monthly-frequency
  property_count: 2
  slug: monthly-frequency
- name: note
  property_count: 2
  slug: note
- name: notes
  property_count: 0
  slug: notes
- name: notification-data
  property_count: 0
  slug: notification-data
- name: notification-email-data
  property_count: 7
  slug: notification-email-data
- name: notification-other-data
  property_count: 4
  slug: notification-other-data
- name: notification-sms-data
  property_count: 4
  slug: notification-sms-data
- name: notification
  property_count: 11
  slug: notification
- name: notifications
  property_count: 0
  slug: notifications
- name: payment-batch
  property_count: 18
  slug: payment-batch
- name: payment-batches
  property_count: 0
  slug: payment-batches
- name: payment-charge-type
  property_count: 0
  slug: payment-charge-type
- name: payment-coupon
  property_count: 12
  slug: payment-coupon
- name: payment-coupons
  property_count: 0
  slug: payment-coupons
- name: payment-create-async
  property_count: 0
  slug: payment-create-async
- name: payment-create
  property_count: 15
  slug: payment-create
- name: payment-creates-async-array
  property_count: 0
  slug: payment-creates-async-array
- name: payment-details
  property_count: 2
  slug: payment-details
- name: payment-method
  property_count: 18
  slug: payment-method
- name: payment-response
  property_count: 26
  slug: payment-response
- name: payment-status
  property_count: 0
  slug: payment-status
- name: payment-type
  property_count: 0
  slug: payment-type
- name: payment-update
  property_count: 5
  slug: payment-update
- name: payment-updates
  property_count: 0
  slug: payment-updates
- name: payment
  property_count: 30
  slug: payment
- name: policies
  property_count: 0
  slug: policies
- name: policy-status
  property_count: 0
  slug: policy-status
- name: policy
  property_count: 41
  slug: policy
- name: policyholder-request
  property_count: 20
  slug: policyholder-request
- name: policyholder
  property_count: 26
  slug: policyholder
- name: policyholders
  property_count: 0
  slug: policyholders
- name: premium-type
  property_count: 0
  slug: premium-type
- name: quote-package
  property_count: 12
  slug: quote-package
- name: quote-packages
  property_count: 0
  slug: quote-packages
- name: s3-adapter
  property_count: 6
  slug: s3-adapter
- name: scheduled-data-export
  property_count: 11
  slug: scheduled-data-export
- name: scheduled-data-exports
  property_count: 0
  slug: scheduled-data-exports
- name: secret-keys-list
  property_count: 0
  slug: secret-keys-list
- name: secret-keys
  property_count: 10
  slug: secret-keys
- name: sftp-adapter
  property_count: 6
  slug: sftp-adapter
- name: webhook-queue-event
  property_count: 13
  slug: webhook-queue-event
- name: webhook-subscription-event
  property_count: 0
  slug: webhook-subscription-event
- name: webhook-subscription-events
  property_count: 0
  slug: webhook-subscription-events
- name: webhook
  property_count: 14
  slug: webhook
- name: webhooks
  property_count: 0
  slug: webhooks
- name: weekly-frequency
  property_count: 2
  slug: weekly-frequency
jsonld:
- class_count: 0
  name: Root Platform Api Context
  property_count: 272
  slug: root-platform-api-context
layout: provider
modified: '2026-06-13'
name: Root Insurance
nav: Providers
network: true
overview: 'Root Insurance publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Calls API, Claims API, and 14 more. Tagged areas include Insurance, Auto Insurance, Telematics, Embedded Insurance, and Policy Administration.


  The Root Insurance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Root Insurance''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Root Plans Pricing
  plan_count: 4
  slug: root-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Root Rate Limits
  slug: root-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Root Insurance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: root-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.2
  delta: 2.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 62.0
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 34.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/root/refs/heads/main/screenshots/root-2026-06-20T193217.png
security:
- kind: authentication
  name: Root Authentication
  slug: root-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Root Domain Security
  slug: root-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Root Vulnerability Disclosure
  slug: root-vulnerability-disclosure
  summary_line: disclosure policy published
slug: root
tags:
- Insurance
- Auto Insurance
- Telematics
- Embedded Insurance
- Policy Administration
- Claims
- Usage-Based Insurance
- Insurtech
website: https://www.joinroot.com/
---
