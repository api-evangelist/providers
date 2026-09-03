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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 109
  human_in_the_loop: 1
  name: Lithic Com Agentic Access
  operation_count: 215
  slug: lithic-com-agentic-access
  summary_line: 215 operations · 109 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: 3D Secure e-commerce authentication and decisioning.
  name: Lithic 3DS API
  slug: lithic-com-3ds-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Top-level program accounts and their spend limits.
  name: Lithic Account API
  slug: lithic-com-account-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: KYC/KYB onboarding and management of individual and business account holders.
  name: Lithic Account Holder API
  slug: lithic-com-account-holder-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Programmable v2 authorization rules, versions, drafts, backtests, and evaluation results.
  name: Lithic Auth Rules API
  slug: lithic-com-auth-rules-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Real-time HTTP webhook authorization decisioning in the transaction path.
  name: Lithic Auth Stream Access (ASA) API
  slug: lithic-com-auth-stream-access-asa-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Available and pending balances for financial accounts.
  name: Lithic Balance API
  slug: lithic-com-balance-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Internal ledger transfers between financial accounts.
  name: Lithic Book Transfer API
  slug: lithic-com-book-transfer-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Virtual and physical card issuance, lifecycle, and digital wallet provisioning.
  name: Lithic Card API
  slug: lithic-com-card-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Responses to real-time authorization challenges.
  name: Lithic Card Authorizations API
  slug: lithic-com-card-authorizations-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Bulk physical card ordering.
  name: Lithic Card Bulk Orders API
  slug: lithic-com-card-bulk-orders-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Legacy v1 dispute (chargeback) submission and evidence.
  name: Lithic Chargeback API
  slug: lithic-com-chargeback-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Credit product configuration, extended credit, and prime rates.
  name: Lithic Credit Product API
  slug: lithic-com-credit-product-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Events API and webhook event subscription management.
  name: Lithic Event API
  slug: lithic-com-event-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: External bank accounts used for ACH payments, with prenote and micro-deposit verification.
  name: Lithic External Bank Account API
  slug: lithic-com-external-bank-account-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Recording and reconciling payments that move outside of Lithic-initiated rails.
  name: Lithic External Payments API
  slug: lithic-com-external-payments-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Ledgered financial accounts, credit configuration, and account activity.
  name: Lithic Financial Account API
  slug: lithic-com-financial-account-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Fraud reporting on card transactions.
  name: Lithic Fraud Report API
  slug: lithic-com-fraud-report-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Card program funding event reporting.
  name: Lithic Funding Events API
  slug: lithic-com-funding-events-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Holds placed against financial account balances.
  name: Lithic Hold API
  slug: lithic-com-hold-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: v2 managed disputes (read surface for Lithic-managed dispute handling).
  name: Lithic Managed Disputes API
  slug: lithic-com-managed-disputes-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Manual ledger adjustments and corrections.
  name: Lithic Management Operations API
  slug: lithic-com-management-operations-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Card network program metadata.
  name: Lithic Network Program API
  slug: lithic-com-network-program-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: ACH payments between Lithic financial accounts and external bank accounts.
  name: Lithic Payment API
  slug: lithic-com-payment-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Registration of HTTP endpoints that receive Auth Stream Access (ASA) requests.
  name: Lithic Responder Endpoints API
  slug: lithic-com-responder-endpoints-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Daily settlement detail, summary, and network total reporting.
  name: Lithic Settlement Report API
  slug: lithic-com-settlement-report-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Financial account statements, line items, and loan tapes for credit products.
  name: Lithic Statements API
  slug: lithic-com-statements-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: API status check.
  name: Lithic Status API
  slug: lithic-com-status-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Digital wallet tokenization (Apple Pay / Google Pay / Samsung Pay) lifecycle and decisioning.
  name: Lithic Tokenization API
  slug: lithic-com-tokenization-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Card transaction authorization, clearing, and simulation.
  name: Lithic Transaction API
  slug: lithic-com-transaction-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: Fraud/AML case and queue management for flagged transactions.
  name: Lithic Transaction Monitoring API
  slug: lithic-com-transaction-monitoring-api
- baseURL: https://api.lithic.com/v1
  baseurl_source: declared
  description: The Transfer Limits API from Lithic — 1 operation(s) for transfer limits.
  name: Lithic Transfer Limits API
  slug: lithic-com-transfer-limits-api
artifact_total: 522
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lithic 3DS API
  slug: open-lithic-com-3ds-api
- collection_type: open
  name: Lithic 3DS Account API
  slug: open-lithic-com-account-api
- collection_type: open
  name: Lithic 3DS Account Holder API
  slug: open-lithic-com-account-holder-api
- collection_type: open
  name: Lithic 3DS Auth Rules API
  slug: open-lithic-com-auth-rules-api
- collection_type: open
  name: Lithic 3DS Auth Stream Access (ASA) API
  slug: open-lithic-com-auth-stream-access-asa-api
- collection_type: open
  name: Lithic 3DS Balance API
  slug: open-lithic-com-balance-api
- collection_type: open
  name: Lithic 3DS Book Transfer API
  slug: open-lithic-com-book-transfer-api
- collection_type: open
  name: Lithic 3DS Card API
  slug: open-lithic-com-card-api
- collection_type: open
  name: Lithic 3DS Card Authorizations API
  slug: open-lithic-com-card-authorizations-api
- collection_type: open
  name: Lithic 3DS Card Bulk Orders API
  slug: open-lithic-com-card-bulk-orders-api
- collection_type: open
  name: Lithic 3DS Chargeback API
  slug: open-lithic-com-chargeback-api
- collection_type: open
  name: Lithic 3DS Credit Product API
  slug: open-lithic-com-credit-product-api
- collection_type: open
  name: Lithic 3DS Event API
  slug: open-lithic-com-event-api
- collection_type: open
  name: Lithic 3DS External Bank Account API
  slug: open-lithic-com-external-bank-account-api
- collection_type: open
  name: Lithic 3DS External Payments API
  slug: open-lithic-com-external-payments-api
- collection_type: open
  name: Lithic 3DS Financial Account API
  slug: open-lithic-com-financial-account-api
- collection_type: open
  name: Lithic 3DS Fraud Report API
  slug: open-lithic-com-fraud-report-api
- collection_type: open
  name: Lithic 3DS Funding Events API
  slug: open-lithic-com-funding-events-api
- collection_type: open
  name: Lithic 3DS Hold API
  slug: open-lithic-com-hold-api
- collection_type: open
  name: Lithic 3DS Managed Disputes API
  slug: open-lithic-com-managed-disputes-api
- collection_type: open
  name: Lithic 3DS Management Operations API
  slug: open-lithic-com-management-operations-api
- collection_type: open
  name: Lithic 3DS Network Program API
  slug: open-lithic-com-network-program-api
- collection_type: open
  name: Lithic 3DS Payment API
  slug: open-lithic-com-payment-api
- collection_type: open
  name: Lithic 3DS Responder Endpoints API
  slug: open-lithic-com-responder-endpoints-api
- collection_type: open
  name: Lithic 3DS Settlement Report API
  slug: open-lithic-com-settlement-report-api
- collection_type: open
  name: Lithic 3DS Statements API
  slug: open-lithic-com-statements-api
- collection_type: open
  name: Lithic 3DS Status API
  slug: open-lithic-com-status-api
- collection_type: open
  name: Lithic 3DS Tokenization API
  slug: open-lithic-com-tokenization-api
- collection_type: open
  name: Lithic 3DS Transaction API
  slug: open-lithic-com-transaction-api
- collection_type: open
  name: Lithic 3DS Transaction Monitoring API
  slug: open-lithic-com-transaction-monitoring-api
- collection_type: open
  name: Lithic 3DS Transfer Limits API
  slug: open-lithic-com-transfer-limits-api
- collection_type: open
  name: Lithic API
  slug: open-lithic-com
- collection_type: open
  name: Lithic Developer API
  slug: open-lithic
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lithic-com-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.lithic.com/docs/mcp
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lithic.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lithic.com/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lithic.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lithic.com/legal/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lithic.com/docs/Quickstart
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lithic-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lithic-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lithic-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lithic-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lithic-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lithic-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lithic
- group: company
  title: ''
  type: Website
  url: https://www.lithic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lithic.com
- group: commercial
  title: ''
  type: Plans
  url: plans/lithic-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lithic-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lithic-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lithic.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lithic.com/llms.txt
created: '2026-07-02'
description: Lithic is a card issuing and issuer-processor API platform for building virtual and physical card programs - authorization, clearing, KYC/KYB account holder onboarding, programmable authorization rules, real-time Auth Stream Access (ASA) decisioning, disputes, digital wallet tokenization, 3DS authentication, ACH payments, ledgered financial accounts, and settlement reporting. Lithic publishes a full OpenAPI 3.1 specification (github.com/lithic-com/lithic-openapi) backing official Node, Python, Go, Java, and Kotlin SDKs, with a sandbox at sandbox.lithic.com that mirrors production functionality.
examples:
- key_count: 6
  name: Lithic Com Createeventsubscription Example
  slug: lithic-com-createeventsubscription-example
- key_count: 6
  name: Lithic Com Createexternalbankaccount Example
  slug: lithic-com-createexternalbankaccount-example
- key_count: 6
  name: Lithic Com Deleteaccountholderentity Example
  slug: lithic-com-deleteaccountholderentity-example
- key_count: 6
  name: Lithic Com Get V2Auth Rulesresults Example
  slug: lithic-com-get-v2auth-rulesresults-example
- key_count: 6
  name: Lithic Com Getaccountholder Example
  slug: lithic-com-getaccountholder-example
- key_count: 6
  name: Lithic Com Getaccountholders Example
  slug: lithic-com-getaccountholders-example
- key_count: 6
  name: Lithic Com Getaccounts Example
  slug: lithic-com-getaccounts-example
- key_count: 6
  name: Lithic Com Getembedcard Example
  slug: lithic-com-getembedcard-example
- key_count: 6
  name: Lithic Com Getenhancedtransactiondata Example
  slug: lithic-com-getenhancedtransactiondata-example
- key_count: 6
  name: Lithic Com Getevents Example
  slug: lithic-com-getevents-example
- key_count: 6
  name: Lithic Com Geteventsubscription Example
  slug: lithic-com-geteventsubscription-example
- key_count: 6
  name: Lithic Com Geteventsubscriptions Example
  slug: lithic-com-geteventsubscriptions-example
- key_count: 6
  name: Lithic Com Geteventsubscriptionsecret Example
  slug: lithic-com-geteventsubscriptionsecret-example
- key_count: 6
  name: Lithic Com Getnetworkprogram Example
  slug: lithic-com-getnetworkprogram-example
- key_count: 6
  name: Lithic Com Getsettlementdetails Example
  slug: lithic-com-getsettlementdetails-example
- key_count: 6
  name: Lithic Com Gettokenization Example
  slug: lithic-com-gettokenization-example
- key_count: 6
  name: Lithic Com Gettokenizations Example
  slug: lithic-com-gettokenizations-example
- key_count: 6
  name: Lithic Com Listenhancedtransactiondata Example
  slug: lithic-com-listenhancedtransactiondata-example
- key_count: 6
  name: Lithic Com Patchaccountbytoken Example
  slug: lithic-com-patchaccountbytoken-example
- key_count: 6
  name: Lithic Com Patchaccountholder Example
  slug: lithic-com-patchaccountholder-example
- key_count: 6
  name: Lithic Com Patchcardbulkorder Example
  slug: lithic-com-patchcardbulkorder-example
- key_count: 6
  name: Lithic Com Patchcardbytoken Example
  slug: lithic-com-patchcardbytoken-example
- key_count: 6
  name: Lithic Com Post V1Three Ds Decisioningsimulateenter Otp Example
  slug: lithic-com-post-v1three-ds-decisioningsimulateenter-otp-example
- key_count: 6
  name: Lithic Com Postaccountholderdocuments Example
  slug: lithic-com-postaccountholderdocuments-example
- key_count: 6
  name: Lithic Com Postaccountholderentities Example
  slug: lithic-com-postaccountholderentities-example
- key_count: 6
  name: Lithic Com Postaccountholders Example
  slug: lithic-com-postaccountholders-example
- key_count: 6
  name: Lithic Com Postcardbulkorder Example
  slug: lithic-com-postcardbulkorder-example
- key_count: 6
  name: Lithic Com Postcardprovision Example
  slug: lithic-com-postcardprovision-example
- key_count: 6
  name: Lithic Com Postcardreissue Example
  slug: lithic-com-postcardreissue-example
- key_count: 6
  name: Lithic Com Postcardrenew Example
  slug: lithic-com-postcardrenew-example
- key_count: 6
  name: Lithic Com Postcards Example
  slug: lithic-com-postcards-example
- key_count: 6
  name: Lithic Com Postcardwebprovision Example
  slug: lithic-com-postcardwebprovision-example
- key_count: 6
  name: Lithic Com Postconvertphysical Example
  slug: lithic-com-postconvertphysical-example
- key_count: 6
  name: Lithic Com Postdisputes Example
  slug: lithic-com-postdisputes-example
- key_count: 6
  name: Lithic Com Postsimulateauthentication Example
  slug: lithic-com-postsimulateauthentication-example
- key_count: 6
  name: Lithic Com Postsimulateauthorizationadvice Example
  slug: lithic-com-postsimulateauthorizationadvice-example
- key_count: 6
  name: Lithic Com Postsimulateauthorize Example
  slug: lithic-com-postsimulateauthorize-example
- key_count: 6
  name: Lithic Com Postsimulateclearing Example
  slug: lithic-com-postsimulateclearing-example
- key_count: 6
  name: Lithic Com Postsimulatecreditauthorizationadvice Example
  slug: lithic-com-postsimulatecreditauthorizationadvice-example
- key_count: 6
  name: Lithic Com Postsimulatereturn Example
  slug: lithic-com-postsimulatereturn-example
- key_count: 6
  name: Lithic Com Postsimulatereturnreversal Example
  slug: lithic-com-postsimulatereturnreversal-example
- key_count: 6
  name: Lithic Com Postsimulatetokenizations Example
  slug: lithic-com-postsimulatetokenizations-example
- key_count: 6
  name: Lithic Com Postsimulatevoid Example
  slug: lithic-com-postsimulatevoid-example
- key_count: 6
  name: Lithic Com Resendactivationcodefortokenization Example
  slug: lithic-com-resendactivationcodefortokenization-example
- key_count: 6
  name: Lithic Com Searchcardbypan Example
  slug: lithic-com-searchcardbypan-example
- key_count: 6
  name: Lithic Com Simulateaccountholderenrollmentdocumentreview Example
  slug: lithic-com-simulateaccountholderenrollmentdocumentreview-example
- key_count: 6
  name: Lithic Com Simulateaccountholderenrollmentreview Example
  slug: lithic-com-simulateaccountholderenrollmentreview-example
- key_count: 6
  name: Lithic Com Updatedigitalcardartfortokenization Example
  slug: lithic-com-updatedigitalcardartfortokenization-example
- key_count: 6
  name: Lithic Com Updateeventsubscription Example
  slug: lithic-com-updateeventsubscription-example
finops:
- name: Lithic Com Finops
  service_category: Fintech and Payments
  slug: lithic-com-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Lithic card-issuing and program-management platform. Lithic provides a REST API; this schema represents the same domain expressed as GraphQL
  name: Lithic GraphQL Schema
  slug: lithic-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lithic-com.png
json_schemas:
- name: Account Financial Account Type
  property_count: 0
  slug: lithic-com-account-financial-account-type
- name: Account Holder Created
  property_count: 6
  slug: lithic-com-account-holder-created
- name: Account Holder Document Updated
  property_count: 6
  slug: lithic-com-account-holder-document-updated
- name: Account Holder
  property_count: 20
  slug: lithic-com-account-holder-response
- name: Account Holder Updated
  property_count: 0
  slug: lithic-com-account-holder-updated
- name: Account Holder Verification
  property_count: 5
  slug: lithic-com-account-holder-verification
- name: Account Standing
  property_count: 8
  slug: lithic-com-account-standing
- name: Account State
  property_count: 0
  slug: lithic-com-account-state
- name: Auth Rule Account Tokens
  property_count: 0
  slug: lithic-com-account-tokens
- name: Account Type External
  property_count: 0
  slug: lithic-com-account-type-external
- name: Searchable Account Type
  property_count: 0
  slug: lithic-com-account-type
- name: AccountConfiguration
  property_count: 10
  slug: lithic-com-accountconfiguration
- name: AccountHolder
  property_count: 20
  slug: lithic-com-accountholder
- name: AccountHolderBusinessResponse
  property_count: 7
  slug: lithic-com-accountholderbusinessresponse
- name: AccountHolderIndividualResponse
  property_count: 7
  slug: lithic-com-accountholderindividualresponse
- name: AccountHolderVerificationApplication
  property_count: 4
  slug: lithic-com-accountholderverificationapplication
- name: AccountSpendLimits
  property_count: 3
  slug: lithic-com-accountspendlimits
- name: ACH Action
  property_count: 0
  slug: lithic-com-ach-action
- name: AchMethodAttributes
  property_count: 9
  slug: lithic-com-achmethodattributes
- name: action_explanation
  property_count: 1
  slug: lithic-com-action-explanation
- name: Address Match Result
  property_count: 0
  slug: lithic-com-address-match-result
- name: Address
  property_count: 6
  slug: lithic-com-address-patch
- name: Address
  property_count: 6
  slug: lithic-com-address
- name: Amount Due
  property_count: 2
  slug: lithic-com-amount-due
- name: Amount
  property_count: 2
  slug: lithic-com-amount
- name: AmountTotals
  property_count: 3
  slug: lithic-com-amount-totals
- name: AppleWebPushProvisioningResponse
  property_count: 2
  slug: lithic-com-applewebpushprovisioningresponse
- name: asa_network_specific_data_mastercard
  property_count: 3
  slug: lithic-com-asa-network-specific-data-mastercard
- name: Network Specific Data
  property_count: 2
  slug: lithic-com-asa-network-specific-data
- name: asa_network_specific_data_visa
  property_count: 1
  slug: lithic-com-asa-network-specific-data-visa
- name: Point of Sale Terminal
  property_count: 8
  slug: lithic-com-asa-pos-terminal
- name: asa_request_card
  property_count: 7
  slug: lithic-com-asa-request-card
- name: Fleet Info
  property_count: 4
  slug: lithic-com-asa-request-fleet-info
- name: asa_request_pos_entry_mode
  property_count: 4
  slug: lithic-com-asa-request-pos-entry-mode
- name: asa-request
  property_count: 30
  slug: lithic-com-asa-request
- name: asa_request_status
  property_count: 0
  slug: lithic-com-asa-request-status
- name: asa-response
  property_count: 6
  slug: lithic-com-asa-response
- name: Auth Rule Feature State
  property_count: 2
  slug: lithic-com-auth-rule-feature-state
- name: Auth Rule Name
  property_count: 0
  slug: lithic-com-auth-rule-name
- name: Auth Rule Parameters
  property_count: 0
  slug: lithic-com-auth-rule-parameters
- name: Auth Rule Result
  property_count: 7
  slug: lithic-com-auth-rule-result
- name: Auth Rule
  property_count: 15
  slug: lithic-com-auth-rule
- name: Auth Rule State
  property_count: 0
  slug: lithic-com-auth-rule-state
- name: Auth Rule Token
  property_count: 0
  slug: lithic-com-auth-rule-token
- name: Auth Rule Types
  property_count: 0
  slug: lithic-com-auth-rule-type
- name: Auth Rule Version
  property_count: 0
  slug: lithic-com-auth-rule-version-id
- name: Auth Rule Version
  property_count: 4
  slug: lithic-com-auth-rule-version
- name: Auth Rule Version State
  property_count: 0
  slug: lithic-com-auth-rule-version-state
- name: Authentication (3DS) Action
  property_count: 0
  slug: lithic-com-authentication-3ds-action
- name: 3DS Authentication object
  property_count: 20
  slug: lithic-com-authentication
- name: Authorization Action
  property_count: 0
  slug: lithic-com-authorization-action
- name: Auto Collection Configuration Request
  property_count: 1
  slug: lithic-com-auto-collection-configuration-request
- name: Auto Collection Configuration Response
  property_count: 1
  slug: lithic-com-auto-collection-configuration-response
- name: Address Verification Service
  property_count: 2
  slug: lithic-com-avs
- name: Backtest List Item
  property_count: 4
  slug: lithic-com-backtest-list-item
- name: Auth Rules Backtest Report
  property_count: 0
  slug: lithic-com-backtest-report
- name: Backtest Request Parameters
  property_count: 2
  slug: lithic-com-backtest-request
- name: Auth Rules Backtest Results
  property_count: 3
  slug: lithic-com-backtest-results
- name: Backtest Simulation Parameters
  property_count: 2
  slug: lithic-com-backtest-simulation-parameters
- name: Auth Rule Backtest Statistics
  property_count: 5
  slug: lithic-com-backtest-stats
- name: Backtest Status
  property_count: 0
  slug: lithic-com-backtest-status
- name: Auth Rule Backtest Token
  property_count: 0
  slug: lithic-com-backtest-token
- name: Balance Details
  property_count: 2
  slug: lithic-com-balance-details
- name: balance
  property_count: 10
  slug: lithic-com-balance
- name: Balance Updated
  property_count: 1
  slug: lithic-com-balance-updated
- name: Balances
  property_count: 4
  slug: lithic-com-balances
- name: Bank Account Api Response
  property_count: 22
  slug: lithic-com-bank-account-api-response
- name: Bank Account Api Response
  property_count: 22
  slug: lithic-com-bank-account-api-response-unlinked
- name: Bank Accounts Api Response
  property_count: 2
  slug: lithic-com-bank-accounts-api-response
- name: Bank Verified Create Bank Account Api Request
  property_count: 17
  slug: lithic-com-bank-verified-create-bank-account-api-request
- name: Bank Verified Verification Methods
  property_count: 0
  slug: lithic-com-bank-verified-verification-method
- name: Transaction Response
  property_count: 0
  slug: lithic-com-base-transaction-response
- name: base_transaction
  property_count: 4
  slug: lithic-com-base-transaction
- name: Activity Response
  property_count: 2
  slug: lithic-com-base-transactions-response
- name: Book Transfer Category
  property_count: 0
  slug: lithic-com-book-transfer-category
- name: Book Transfer Detailed Results
  property_count: 0
  slug: lithic-com-book-transfer-detailed-results
- name: Book Transfer Event
  property_count: 8
  slug: lithic-com-book-transfer-event
- name: Book Transfer Transaction Created
  property_count: 0
  slug: lithic-com-book-transfer-transaction-created
- name: Book Transfer Transaction
  property_count: 0
  slug: lithic-com-book-transfer-transaction
- name: Book Transfer Transaction Updated
  property_count: 0
  slug: lithic-com-book-transfer-transaction-updated
- name: Book Transfer Type
  property_count: 0
  slug: lithic-com-book-transfer-type
- name: Bulk Order Response
  property_count: 8
  slug: lithic-com-bulk-order-response
- name: Auth Rule Business Account Tokens
  property_count: 0
  slug: lithic-com-business-account-tokens
- name: BusinessEntity
  property_count: 6
  slug: lithic-com-businessentity
- name: Card Authorization Challenge Response
  property_count: 8
  slug: lithic-com-card-authorization-challenge-response
- name: Card Converted
  property_count: 1
  slug: lithic-com-card-converted
- name: Card Created
  property_count: 2
  slug: lithic-com-card-created
- name: Card Reissued
  property_count: 1
  slug: lithic-com-card-reissued
- name: Card Renewed
  property_count: 5
  slug: lithic-com-card-renewed
- name: Card Shipped
  property_count: 4
  slug: lithic-com-card-shipped
- name: Auth Rule Card Tokens
  property_count: 0
  slug: lithic-com-card-tokens
- name: Card Transaction Enhanced Data Created
  property_count: 0
  slug: lithic-com-card-transaction-enhanced-data-created
- name: Card Transaction Enhanced Data Updated
  property_count: 0
  slug: lithic-com-card-transaction-enhanced-data-updated
- name: Card Transaction
  property_count: 28
  slug: lithic-com-card-transaction
- name: Card Transaction Status Filter
  property_count: 0
  slug: lithic-com-card-transaction-status-filter
- name: Card Transaction Update Action
  property_count: 0
  slug: lithic-com-card-transaction-update-action
- name: card-type
  property_count: 0
  slug: lithic-com-card-type
- name: Card Updated
  property_count: 3
  slug: lithic-com-card-updated
- name: Cardholder Authentication
  property_count: 5
  slug: lithic-com-cardholder-authentication
- name: Cardholder Liability Event Data
  property_count: 4
  slug: lithic-com-cardholder-liability-event-data
- name: CardProgram
  property_count: 8
  slug: lithic-com-cardprogram
- name: CardSpendLimits
  property_count: 3
  slug: lithic-com-cardspendlimits
- name: Carrier
  property_count: 1
  slug: lithic-com-carrier
- name: Category Balances
  property_count: 3
  slug: lithic-com-category-balances
- name: Category Details
  property_count: 3
  slug: lithic-com-category-details
- name: Category Tier
  property_count: 2
  slug: lithic-com-category-tier
- name: 3DS Challenge webhook event
  property_count: 3
  slug: lithic-com-challenge-event
- name: Challenge Response object
  property_count: 2
  slug: lithic-com-challenge-response
- name: Challenge Response Unprocessable
  property_count: 1
  slug: lithic-com-challenge-response-unprocessable
- name: 3DS Challenge object
  property_count: 4
  slug: lithic-com-challenge
- name: CommonData
  property_count: 5
  slug: lithic-com-common-data
- name: Conditional Action (3DS) Parameters
  property_count: 2
  slug: lithic-com-conditional-3ds-action-parameters
- name: Conditional Action (ACH) Parameters
  property_count: 2
  slug: lithic-com-conditional-ach-action-parameters
- name: Conditional Action (Authorization) Parameters
  property_count: 2
  slug: lithic-com-conditional-authorization-action-parameters
- name: Conditional Block Parameters
  property_count: 1
  slug: lithic-com-conditional-block-parameters
- name: Conditional Action (Card Transaction Update) Parameters
  property_count: 2
  slug: lithic-com-conditional-card-transaction-update-action-parameters
- name: Conditional Operation
  property_count: 0
  slug: lithic-com-conditional-operation
- name: Conditional Action (Tokenization) Parameters
  property_count: 2
  slug: lithic-com-conditional-tokenization-action-parameters
- name: Conditional Value
  property_count: 0
  slug: lithic-com-conditional-value
- name: Converted Amount
  property_count: 3
  slug: lithic-com-converted-amount
- name: Auth Rule Parameters
  property_count: 0
  slug: lithic-com-create-auth-rule-request
- name: Create Book Transfer Request
  property_count: 11
  slug: lithic-com-create-book-transfer-request
- name: Create Bulk Order Request
  property_count: 3
  slug: lithic-com-create-bulk-order-request
- name: Account Holder Entity Create Request
  property_count: 0
  slug: lithic-com-create-entity-request
- name: Account Holder Entity Create Response
  property_count: 6
  slug: lithic-com-create-entity-response
- name: Create External Bank Account Api Response Context
  property_count: 1
  slug: lithic-com-create-external-bank-account-error-response-context
- name: Create External Bank Account Api Response
  property_count: 3
  slug: lithic-com-create-external-bank-account-error-response
- name: Create External Payment Request
  property_count: 9
  slug: lithic-com-create-external-payment-request
- name: Create Hold Request
  property_count: 5
  slug: lithic-com-create-hold-request
- name: Create Management Operation Request
  property_count: 11
  slug: lithic-com-create-management-operation-request
- name: CreateFinancialAccountRequest
  property_count: 4
  slug: lithic-com-createfinancialaccountrequest
- name: CreatePaymentRequest
  property_count: 10
  slug: lithic-com-createpaymentrequest
- name: Credit Details
  property_count: 0
  slug: lithic-com-credit-details
- name: Currency
  property_count: 0
  slug: lithic-com-currency
- name: Auth Rule Current Version
  property_count: 0
  slug: lithic-com-current-version
- name: customer-tokenization-decision
  property_count: 4
  slug: lithic-com-customer-tokenization-decision
- name: Debit Details
  property_count: 0
  slug: lithic-com-debit-details
- name: Result of the transaction
  property_count: 0
  slug: lithic-com-decline-result
- name: Detailed Result
  property_count: 0
  slug: lithic-com-detailed-result
- name: Detailed Results
  property_count: 0
  slug: lithic-com-detailed-results
- name: device
  property_count: 3
  slug: lithic-com-device
- name: digital-wallet-token-metadata
  property_count: 5
  slug: lithic-com-digital-wallet-token-metadata
- name: digital-wallet-tokenization-approval-request
  property_count: 0
  slug: lithic-com-digital-wallet-tokenization-approval-request
- name: Digital Wallet Tokenization Result
  property_count: 5
  slug: lithic-com-digital-wallet-tokenization-result
- name: Digital Wallet Tokenization Two Factor Authentication Code Sent
  property_count: 5
  slug: lithic-com-digital-wallet-tokenization-two-factor-authentication-code-s
- name: Digital Wallet Tokenization Two Factor Authentication Code
  property_count: 6
  slug: lithic-com-digital-wallet-tokenization-two-factor-authentication-code
- name: Digital Wallet Tokenization Updated
  property_count: 4
  slug: lithic-com-digital-wallet-tokenization-updated
- name: DigitalCardArt
  property_count: 7
  slug: lithic-com-digitalcardart
- name: Directional Limits
  property_count: 2
  slug: lithic-com-directional-limits
- name: Dispute Evidence
  property_count: 7
  slug: lithic-com-dispute-evidence
- name: Dispute Evidence Upload Failed
  property_count: 0
  slug: lithic-com-dispute-evidence-upload-failed
- name: Dispute
  property_count: 14
  slug: lithic-com-dispute
- name: Dispute Updated
  property_count: 0
  slug: lithic-com-dispute-updated
- name: Dispute
  property_count: 18
  slug: lithic-com-dispute-v1
- name: Disputes Response
  property_count: 2
  slug: lithic-com-disputes-response
- name: Account Holder KYC Document
  property_count: 5
  slug: lithic-com-document
- name: Account Holder document types
  property_count: 0
  slug: lithic-com-document-type
- name: Account holder document upload status reasons
  property_count: 0
  slug: lithic-com-document-upload-status-reasons
- name: Account holder document upload status
  property_count: 0
  slug: lithic-com-document-upload-status
- name: Auth Rule Draft Version
  property_count: 0
  slug: lithic-com-draft-version
- name: EnhancedData
  property_count: 5
  slug: lithic-com-enhanced-data
- name: EnhancedDataListResponse
  property_count: 1
  slug: lithic-com-enhanceddatalistresponse
- name: Account Holder Entity
  property_count: 10
  slug: lithic-com-entity-response
- name: Account Holder Entity Status
  property_count: 0
  slug: lithic-com-entity-status
- name: Account Holder Entity Type
  property_count: 0
  slug: lithic-com-entity-type
- name: error
  property_count: 2
  slug: lithic-com-error
- name: Event
  property_count: 4
  slug: lithic-com-event
- name: Event Stream Types
  property_count: 0
  slug: lithic-com-event-stream
- name: event_type
  property_count: 0
  slug: lithic-com-event-type
- name: EventSubscription
  property_count: 5
  slug: lithic-com-eventsubscription
- name: Auth Rule Excluded Account Tokens
  property_count: 0
  slug: lithic-com-excluded-account-tokens
- name: Auth Rule Excluded Business Account Tokens
  property_count: 0
  slug: lithic-com-excluded-business-account-tokens
- name: Auth Rule Excluded Card Tokens
  property_count: 0
  slug: lithic-com-excluded-card-tokens
- name: Extended Credit
  property_count: 1
  slug: lithic-com-extended-credit
- name: External Bank Account Address
  property_count: 6
  slug: lithic-com-external-bank-account-address
- name: External Payment Action Request
  property_count: 2
  slug: lithic-com-external-payment-action-request
- name: External Payment Action with Progress to Request
  property_count: 3
  slug: lithic-com-external-payment-action-with-progress-to-request
- name: External Payment Category
  property_count: 0
  slug: lithic-com-external-payment-category
- name: External Payment Direction
  property_count: 0
  slug: lithic-com-external-payment-direction
- name: External Payment Event
  property_count: 8
  slug: lithic-com-external-payment-event
- name: External Payment Event Type
  property_count: 0
  slug: lithic-com-external-payment-event-type
- name: External Payment Progress To
  property_count: 0
  slug: lithic-com-external-payment-progress-to
- name: External Payment Response
  property_count: 0
  slug: lithic-com-external-payment-response
- name: External Payments Response
  property_count: 2
  slug: lithic-com-external-payments-response
- name: ExternalResource
  property_count: 3
  slug: lithic-com-external-resource
- name: ExternalResourceType
  property_count: 0
  slug: lithic-com-external-resource-type
- name: Externally Verified Create Bank Account Api Request
  property_count: 15
  slug: lithic-com-externally-verified-create-bank-account-api-request
- name: Externally Verified Verification Methods
  property_count: 0
  slug: lithic-com-externally-verified-verification-method
- name: Financial Account Balance
  property_count: 10
  slug: lithic-com-financial-account-balance
- name: Financial Account Credit Configuration Request
  property_count: 5
  slug: lithic-com-financial-account-credit-config-request
- name: Financial Account Credit Configuration Response
  property_count: 6
  slug: lithic-com-financial-account-credit-config-response
- name: Financial Account Credit Config
  property_count: 5
  slug: lithic-com-financial-account-credit-config
- name: Financial Account Response
  property_count: 13
  slug: lithic-com-financial-account-response
- name: Financial Account State
  property_count: 2
  slug: lithic-com-financial-account-state
- name: Financial Account Status
  property_count: 0
  slug: lithic-com-financial-account-status
- name: Financial Account Substatus
  property_count: 0
  slug: lithic-com-financial-account-substatus
- name: financial-account-transaction
  property_count: 11
  slug: lithic-com-financial-account-transaction
- name: Financial Accounts Response
  property_count: 2
  slug: lithic-com-financial-accounts-response
- name: Financial Event Data
  property_count: 4
  slug: lithic-com-financial-event-data
- name: Financial Event
  property_count: 5
  slug: lithic-com-financial-event
- name: Financial Event Type
  property_count: 0
  slug: lithic-com-financial-event-type
- name: Financial Transaction
  property_count: 0
  slug: lithic-com-financial-transaction
- name: Fleet
  property_count: 6
  slug: lithic-com-fleet
- name: Fraud Report Parameters
  property_count: 3
  slug: lithic-com-fraud-report-request
- name: Fraud Report Response
  property_count: 6
  slug: lithic-com-fraud-report-response
- name: FuelData
  property_count: 4
  slug: lithic-com-fuel-data
- name: FuelType
  property_count: 0
  slug: lithic-com-fuel-type
- name: FuelUnitOfMeasure
  property_count: 0
  slug: lithic-com-fuel-unit-of-measure
- name: funding_account
  property_count: 7
  slug: lithic-com-funding-account
- name: Funding Event Details Response
  property_count: 3
  slug: lithic-com-funding-event-details-response
- name: Funding Event Response
  property_count: 8
  slug: lithic-com-funding-event-response
- name: Funding Event Responses
  property_count: 2
  slug: lithic-com-funding-event-responses
- name: Funding Event Settlement
  property_count: 2
  slug: lithic-com-funding-event-settlement
- name: Funding Event Webhook
  property_count: 1
  slug: lithic-com-funding-events-created-webhook
- name: GoogleWebPushProvisioningResponse
  property_count: 2
  slug: lithic-com-googlewebpushprovisioningresponse
- name: Hold Event
  property_count: 8
  slug: lithic-com-hold-event
- name: Hold Event Type
  property_count: 0
  slug: lithic-com-hold-event-type
- name: Hold Status
  property_count: 0
  slug: lithic-com-hold-status
- name: Hold Transaction
  property_count: 0
  slug: lithic-com-hold-transaction
- name: Holds Response
  property_count: 2
  slug: lithic-com-holds-response
- name: Individual
  property_count: 8
  slug: lithic-com-individual-patch
- name: Individual
  property_count: 7
  slug: lithic-com-individual
- name: Instance Financial Account Type
  property_count: 0
  slug: lithic-com-instance-financial-account-type
- name: Interest Calculation method
  property_count: 0
  slug: lithic-com-interest-calculation-method
- name: Interest Details
  property_count: 7
  slug: lithic-com-interest-details
- name: Interest Rate
  property_count: 2
  slug: lithic-com-interest-rate
- name: Internal Adjustment Event
  property_count: 5
  slug: lithic-com-internal-adjustment-event
- name: Internal Adjustment Transaction
  property_count: 11
  slug: lithic-com-internal-adjustment-transaction
- name: KYB Business Entity
  property_count: 7
  slug: lithic-com-kyb-business-entity-patch
- name: KYB Business Entity
  property_count: 6
  slug: lithic-com-kyb-business-entity
- name: KYB Individual
  property_count: 0
  slug: lithic-com-kyb-individual-patch
- name: Business/Individual Patch Response
  property_count: 20
  slug: lithic-com-kyb-kyc-patch-response
- name: Business Patch Request
  property_count: 7
  slug: lithic-com-kyb-patch-request
- name: Kyb
  property_count: 10
  slug: lithic-com-kyb
- name: KybDelegated
  property_count: 9
  slug: lithic-com-kybdelegated
- name: KybDelegatedBusinessEntity
  property_count: 6
  slug: lithic-com-kybdelegatedbusinessentity
- name: KybDelegatedIndividual
  property_count: 0
  slug: lithic-com-kybdelegatedindividual
- name: KybIndividual
  property_count: 0
  slug: lithic-com-kybindividual
- name: Individuals associated with a KYC application.
  property_count: 0
  slug: lithic-com-kyc-individual-patch
- name: Individual Patch Request
  property_count: 2
  slug: lithic-com-kyc-patch-request
- name: Kyc
  property_count: 5
  slug: lithic-com-kyc
- name: KycExempt
  property_count: 9
  slug: lithic-com-kycexempt
- name: KycIndividual
  property_count: 0
  slug: lithic-com-kycindividual
- name: Liability Allocation
  property_count: 5
  slug: lithic-com-liability-allocation
- name: Limit With Progress
  property_count: 2
  slug: lithic-com-limit-with-progress
- name: LineItem
  property_count: 4
  slug: lithic-com-line-item
- name: List Transactions Response
  property_count: 2
  slug: lithic-com-list-transactions-response
- name: Loan Tape Configuration
  property_count: 7
  slug: lithic-com-loan-tape-configuration
- name: Loan Tape Rebuild Configuration
  property_count: 3
  slug: lithic-com-loan-tape-rebuild-configuration
- name: Loan Tape Response
  property_count: 22
  slug: lithic-com-loan-tape-response
- name: Loan Tapes Response
  property_count: 2
  slug: lithic-com-loan-tapes-response
- name: Management Operation Action Request
  property_count: 2
  slug: lithic-com-management-operation-action-request
- name: Management Operation Category
  property_count: 0
  slug: lithic-com-management-operation-category
- name: Management Operation Direction
  property_count: 0
  slug: lithic-com-management-operation-direction
- name: Management Operation Event
  property_count: 9
  slug: lithic-com-management-operation-event
- name: Management Operation Event Type
  property_count: 0
  slug: lithic-com-management-operation-event-type
- name: Management Operation Transaction
  property_count: 0
  slug: lithic-com-management-operation-transaction
- name: Management Operation Transactions Response
  property_count: 2
  slug: lithic-com-management-operation-transactions-response
- name: Mastercard Network Specific Data
  property_count: 3
  slug: lithic-com-mastercard-network-specific-data
- name: Merchant Currency
  property_count: 0
  slug: lithic-com-merchant-currency
- name: Merchant Lock Inputs
  property_count: 1
  slug: lithic-com-merchant-lock-parameters
- name: Merchant
  property_count: 7
  slug: lithic-com-merchant
- name: MessageAttempt
  property_count: 8
  slug: lithic-com-messageattempt
- name: Micro Deposit Verification Request
  property_count: 1
  slug: lithic-com-micro-deposit-verification-request
- name: Network Information
  property_count: 4
  slug: lithic-com-network-info
- name: Network Risk Score
  property_count: 0
  slug: lithic-com-network-risk-score
- name: Network Specific Data
  property_count: 2
  slug: lithic-com-network-specific-data
- name: Network Total
  property_count: 12
  slug: lithic-com-network-total
- name: Network Totals Response
  property_count: 2
  slug: lithic-com-network-totals-list
- name: NetworkProgram
  property_count: 4
  slug: lithic-com-networkprogram
- name: non_pci_card_response
  property_count: 25
  slug: lithic-com-non-pci-card-response
- name: On Closed Account
  property_count: 0
  slug: lithic-com-on-closed-account
- name: Owner Type
  property_count: 0
  slug: lithic-com-owner-type
- name: Auth Rule Patch Request
  property_count: 2
  slug: lithic-com-patch-auth-rule-request
- name: Legacy Patch Request
  property_count: 7
  slug: lithic-com-patch-request
- name: Legacy Patch Response
  property_count: 8
  slug: lithic-com-patch-response
- name: Payment Allocation
  property_count: 6
  slug: lithic-com-payment-allocation
- name: Payment Details
  property_count: 0
  slug: lithic-com-payment-details
- name: Payment Event
  property_count: 7
  slug: lithic-com-payment-event
- name: Payment Event Type
  property_count: 0
  slug: lithic-com-payment-event-type
- name: Payment Return Request
  property_count: 5
  slug: lithic-com-payment-return-request
- name: Payment Transaction Created
  property_count: 0
  slug: lithic-com-payment-transaction-created
- name: Payment Transaction
  property_count: 0
  slug: lithic-com-payment-transaction
- name: Payment Transaction Updated
  property_count: 0
  slug: lithic-com-payment-transaction-updated
- name: PaymentMethodRequestAttributes
  property_count: 4
  slug: lithic-com-paymentmethodrequestattributes
- name: Payoff Details
  property_count: 5
  slug: lithic-com-payoff-details
- name: pci_card_response
  property_count: 0
  slug: lithic-com-pci-card-response
- name: Auth Rule Performance Report V2
  property_count: 4
  slug: lithic-com-performance-report-v2
- name: Period State
  property_count: 0
  slug: lithic-com-period-state
- name: Point of Sale Entry Mode
  property_count: 4
  slug: lithic-com-pos-entry-mode
- name: Point of Sale
  property_count: 2
  slug: lithic-com-pos
- name: Point of Sale Terminal
  property_count: 8
  slug: lithic-com-pos-terminal
- name: PostPaymentResponse
  property_count: 0
  slug: lithic-com-postpaymentresponse
- name: Prime Rates Response
  property_count: 2
  slug: lithic-com-prime-rates-response
- name: Auth Rule Program Level Parameter
  property_count: 0
  slug: lithic-com-program-level
- name: Register Account Number Request
  property_count: 1
  slug: lithic-com-register-account-number-request
- name: Related Account Tokens
  property_count: 2
  slug: lithic-com-related-account-tokens
- name: Auth Rule Version Report Statistics
  property_count: 4
  slug: lithic-com-report-stats-v2
- name: Account Holder Required Document
  property_count: 3
  slug: lithic-com-required-document
- name: Authentication (3DS) Action (Result)
  property_count: 1
  slug: lithic-com-result-authentication-3ds-action
- name: Authorization Action (Result)
  property_count: 0
  slug: lithic-com-result-authorization-action
- name: Result
  property_count: 0
  slug: lithic-com-result
- name: Retry Book Transfer Request
  property_count: 1
  slug: lithic-com-retry-book-transfer-request
- name: Retry Micro Deposit Verification Request
  property_count: 1
  slug: lithic-com-retry-micro-deposit-verification-request
- name: Retry Prenote Verification Request
  property_count: 1
  slug: lithic-com-retry-prenote-verification-request
- name: Rule Feature
  property_count: 0
  slug: lithic-com-rule-feature
- name: Detailed Rule Result
  property_count: 4
  slug: lithic-com-rule-result
- name: Service Location
  property_count: 5
  slug: lithic-com-service-location
- name: FuelServiceType
  property_count: 0
  slug: lithic-com-service-type
- name: Set Verification Method Allowed Verification Methods
  property_count: 0
  slug: lithic-com-set-verification-method-allowed-verification-methods
- name: Set Verification Method Request
  property_count: 2
  slug: lithic-com-set-verification-method-request
- name: Settlement Report
  property_count: 11
  slug: lithic-com-settlement-report
- name: settlement Summary Details
  property_count: 8
  slug: lithic-com-settlement-summary-details
- name: SettlementDetail
  property_count: 21
  slug: lithic-com-settlementdetail
- name: ShippingAddress
  property_count: 11
  slug: lithic-com-shippingaddress
- name: Signals Response
  property_count: 31
  slug: lithic-com-signals-response
- name: Simulate Action Request
  property_count: 5
  slug: lithic-com-simulate-action-request
- name: 3DS Simulation Request object
  property_count: 4
  slug: lithic-com-simulate-authentication-request
- name: Simulate account holder enrollment document review request body
  property_count: 4
  slug: lithic-com-simulate-enrollment-document-review-request
- name: Simulate account holder enrollment review request body
  property_count: 3
  slug: lithic-com-simulate-enrollment-review-request
- name: Simulate Origination Release Request
  property_count: 1
  slug: lithic-com-simulate-origination-release-request
- name: Simulate Origination Return Request
  property_count: 2
  slug: lithic-com-simulate-origination-return-request
- name: Simulate Payment Response
  property_count: 3
  slug: lithic-com-simulate-payment-response
- name: Simulate Receipt Request
  property_count: 5
  slug: lithic-com-simulate-receipt-request
- name: Spend Feature State
  property_count: 4
  slug: lithic-com-spend-feature-state
- name: spend_limit_duration
  property_count: 0
  slug: lithic-com-spend-limit-duration
- name: Spend Velocity Filters
  property_count: 0
  slug: lithic-com-spend-velocity-filters
- name: Statement Line Item Response
  property_count: 14
  slug: lithic-com-statement-line-item-response
- name: Statement Line Items Response
  property_count: 2
  slug: lithic-com-statement-line-items-response
- name: Statement Response
  property_count: 23
  slug: lithic-com-statement-response
- name: Statement Totals
  property_count: 11
  slug: lithic-com-statement-totals
- name: Statement Type
  property_count: 0
  slug: lithic-com-statement-type
- name: Statement Webhook
  property_count: 1
  slug: lithic-com-statements-created-webhook
- name: Statements Response
  property_count: 2
  slug: lithic-com-statements-response
- name: KYC/KYB Status Reasons
  property_count: 0
  slug: lithic-com-status-reasons
- name: KYC/KYB Status
  property_count: 0
  slug: lithic-com-status
- name: Supported Simulation Decline Reasons
  property_count: 0
  slug: lithic-com-supported-simulation-decline-reasons
- name: Supported Simulation Types
  property_count: 0
  slug: lithic-com-supported-simulation-types
- name: Tags
  property_count: 0
  slug: lithic-com-tags
- name: TaxData
  property_count: 3
  slug: lithic-com-tax-data
- name: TaxExemptIndicator
  property_count: 0
  slug: lithic-com-tax-exempt-indicator
- name: 3DS Decision Response object
  property_count: 2
  slug: lithic-com-three-ds-decisioning
- name: Tier Schedule Entry
  property_count: 5
  slug: lithic-com-tier-schedule-entry
- name: Tier Schedule Response
  property_count: 2
  slug: lithic-com-tier-schedule-response
- name: Token Info
  property_count: 1
  slug: lithic-com-token-info
- name: Tokenization Action
  property_count: 0
  slug: lithic-com-tokenization-action
- name: tokenization-approval-request
  property_count: 0
  slug: lithic-com-tokenization-approval-request
- name: tokenization-decisioning-response
  property_count: 4
  slug: lithic-com-tokenization-decisioning-response
- name: Tokenization Decline Reason
  property_count: 0
  slug: lithic-com-tokenization-decline-reason
- name: Tokenization Event Outcome
  property_count: 0
  slug: lithic-com-tokenization-event-outcome
- name: Tokenization Event
  property_count: 7
  slug: lithic-com-tokenization-event
- name: tokenization-request-base
  property_count: 9
  slug: lithic-com-tokenization-request-base
- name: Tokenization Result
  property_count: 5
  slug: lithic-com-tokenization-result
- name: Tokenization Rule Result
  property_count: 4
  slug: lithic-com-tokenization-rule-result
- name: Tokenization
  property_count: 14
  slug: lithic-com-tokenization
- name: Tokenization TFA Reason
  property_count: 0
  slug: lithic-com-tokenization-tfa-reason
- name: Tokenization Two Factor Authentication Code
  property_count: 6
  slug: lithic-com-tokenization-two-factor-authentication-code
- name: Tokenization Two Factor Authentication Code Sent
  property_count: 5
  slug: lithic-com-tokenization-two-factor-authentication-code-sent
- name: Tokenization Updated
  property_count: 4
  slug: lithic-com-tokenization-updated
- name: Transaction Amounts
  property_count: 4
  slug: lithic-com-transaction-amounts
- name: Transaction Category
  property_count: 0
  slug: lithic-com-transaction-category
- name: Transaction Event Amounts
  property_count: 3
  slug: lithic-com-transaction-event-amounts
- name: Transaction Event
  property_count: 12
  slug: lithic-com-transaction-event
- name: Transaction Merchant
  property_count: 0
  slug: lithic-com-transaction-merchant
- name: Transaction Result
  property_count: 0
  slug: lithic-com-transaction-result
- name: Transaction Series
  property_count: 3
  slug: lithic-com-transaction-series
- name: Transaction Status
  property_count: 0
  slug: lithic-com-transaction-status
- name: Transfer Limit Item
  property_count: 6
  slug: lithic-com-transfer-limit-item
- name: Transfer Limits Response
  property_count: 2
  slug: lithic-com-transfer-limits-response
- name: Transfer
  property_count: 13
  slug: lithic-com-transfer
- name: Transfer Type
  property_count: 0
  slug: lithic-com-transfer-type
- name: TypeScript Code Parameters
  property_count: 2
  slug: lithic-com-typescript-code-parameters
- name: Unverified Create Bank Account Api Request
  property_count: 15
  slug: lithic-com-unverified-create-bank-account-api-request
- name: Unverified Verification Methods
  property_count: 0
  slug: lithic-com-unverified-verification-method
- name: Update Bank Account Api Request
  property_count: 9
  slug: lithic-com-update-bank-account-api-request
- name: Update Bulk Order Request
  property_count: 1
  slug: lithic-com-update-bulk-order-request
- name: Update financial account status request
  property_count: 3
  slug: lithic-com-update-financial-account-status-request
- name: Update Financial Account Substatus
  property_count: 0
  slug: lithic-com-update-financial-account-substatus
- name: Update Tier Schedule Entry Request
  property_count: 3
  slug: lithic-com-update-tier-schedule-entry-request
- name: UpdateFinancialAccountRequest
  property_count: 1
  slug: lithic-com-updatefinancialaccountrequest
- name: Velocity Limits Filters
  property_count: 5
  slug: lithic-com-velocity-limit-filters
- name: Velocity Limit Parameters
  property_count: 5
  slug: lithic-com-velocity-limit-parameters
- name: Velocity Limit Period
  property_count: 0
  slug: lithic-com-velocity-limit-period
- name: Velocity Limits Scope
  property_count: 0
  slug: lithic-com-velocity-scope
- name: Verification Application
  property_count: 5
  slug: lithic-com-verification-application
- name: Verification Method
  property_count: 0
  slug: lithic-com-verification-method
- name: Verification State
  property_count: 0
  slug: lithic-com-verification-state
- name: Visa Network Specific Data
  property_count: 1
  slug: lithic-com-visa-network-specific-data
- name: Void Hold Request
  property_count: 1
  slug: lithic-com-void-hold-request
- name: wallet-decisioning-info
  property_count: 4
  slug: lithic-com-wallet-decisioning-info
- name: WebPushProvisioningResponse
  property_count: 0
  slug: lithic-com-webpushprovisioningresponse
- name: WebPushProvisioningResponseHeader
  property_count: 1
  slug: lithic-com-webpushprovisioningresponseheader
- name: WebPushProvisioningResponseJws
  property_count: 4
  slug: lithic-com-webpushprovisioningresponsejws
- name: Wire Party Details
  property_count: 4
  slug: lithic-com-wire-party-details
- name: WireMethodAttributes
  property_count: 6
  slug: lithic-com-wiremethodattributes
- name: Workflow Event Data
  property_count: 6
  slug: lithic-com-workflow-event-data
json_structures:
- name: Lithic Com Structure
  property_count: 0
  slug: lithic-com-structure
layout: provider
mcp_servers:
- description: ''
  name: Lithic MCP Server
  slug: lithic-mcp-server
modified: '2026-08-08'
name: Lithic
nav: Providers
network: true
overview: 'Lithic publishes 31 APIs on the [APIs.io](https://apis.io/) network, including 3DS API, Account API, Account Holder API, and 28 more. Tagged areas include Fintech, Card Issuing, Payments, Issuer Processor, and KYC.


  The Lithic catalog on APIs.io includes 1 Spectral governance ruleset.


  Lithic''s developer surface includes changelog, getting-started guide, authentication, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Lithic Com Plans Pricing
  plan_count: 4
  slug: lithic-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 13
  name: Lithic Com Rate Limits
  slug: lithic-com-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Lithic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: lithic-com-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 50.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 9.8
    contract_quality: 61.7
    developer_ergonomics: 33.3
    discoverability: 70.4
    governance: 9.8
    operational_transparency: 57.9
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lithic-com/refs/heads/main/screenshots/lithic-com-2026-07-25T225335.png
security:
- kind: authentication
  name: Lithic Com Authentication
  slug: lithic-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lithic Com Domain Security
  slug: lithic-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lithic Com Vulnerability Disclosure
  slug: lithic-com-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lithic Com Trust Center
  slug: lithic-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: lithic-com
tags:
- Fintech
- Card Issuing
- Payments
- Issuer Processor
- KYC
- Banking as a Service
website: https://www.lithic.com
---
