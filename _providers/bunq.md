---
access_model:
  confidence: medium
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
  - security
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Bunq Agentic Access
  operation_count: 28
  slug: bunq-agentic-access
  summary_line: 28 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: Upload and retrieve attachment content.
  name: bunq Attachment API
  slug: bunq-attachment-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: Debit and credit cards linked to monetary accounts.
  name: bunq Card API
  slug: bunq-card-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: Generate and download account statement exports (CSV, MT940, PDF).
  name: bunq Customer Statement API
  slug: bunq-customer-statement-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: Bank, savings, and joint accounts holding money.
  name: bunq Monetary Account API
  slug: bunq-monetary-account-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: Execute and read payments (including SEPA) for a monetary account.
  name: bunq Payment API
  slug: bunq-payment-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: Create and read payment requests (money you ask another party to pay).
  name: bunq Request Inquiry API
  slug: bunq-request-inquiry-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The authenticated user (person, company, or payment service provider).
  name: bunq User API
  slug: bunq-user-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The additional-transaction-information-category API from bunq — 1 operation(s) for additional-transaction-information-category.
  name: bunq Additional Transaction Information Category API
  slug: bunq-additional-transaction-information-category-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The additional-transaction-information-category-user-defined API from bunq — 1 operation(s) for additional-transaction-information-category-user-defined.
  name: bunq Additional Transaction Information Category User Defined API
  slug: bunq-additional-transaction-information-category-user-defined-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The attachment-public API from bunq — 2 operation(s) for attachment-public.
  name: bunq Attachment Public API
  slug: bunq-attachment-public-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The avatar API from bunq — 2 operation(s) for avatar.
  name: bunq Avatar API
  slug: bunq-avatar-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The billing-contract-subscription API from bunq — 1 operation(s) for billing-contract-subscription.
  name: bunq Billing Contract Subscription API
  slug: bunq-billing-contract-subscription-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The bunqme-fundraiser-profile API from bunq — 2 operation(s) for bunqme-fundraiser-profile.
  name: bunq Bunqme Fundraiser Profile API
  slug: bunq-bunqme-fundraiser-profile-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The bunqme-fundraiser-result API from bunq — 1 operation(s) for bunqme-fundraiser-result.
  name: bunq Bunqme Fundraiser Result API
  slug: bunq-bunqme-fundraiser-result-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The bunqme-tab API from bunq — 2 operation(s) for bunqme-tab.
  name: bunq Bunqme Tab API
  slug: bunq-bunqme-tab-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The bunqme-tab-result-response API from bunq — 1 operation(s) for bunqme-tab-result-response.
  name: bunq Bunqme Tab Result Response API
  slug: bunq-bunqme-tab-result-response-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The callback-url API from bunq — 2 operation(s) for callback-url.
  name: bunq Callback URL API
  slug: bunq-callback-url-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The card-batch API from bunq — 1 operation(s) for card-batch.
  name: bunq Card Batch API
  slug: bunq-card-batch-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The card-batch-replace API from bunq — 1 operation(s) for card-batch-replace.
  name: bunq Card Batch Replace API
  slug: bunq-card-batch-replace-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The card-credit API from bunq — 1 operation(s) for card-credit.
  name: bunq Card Credit API
  slug: bunq-card-credit-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The card-debit API from bunq — 1 operation(s) for card-debit.
  name: bunq Card Debit API
  slug: bunq-card-debit-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The card-name API from bunq — 1 operation(s) for card-name.
  name: bunq Card Name API
  slug: bunq-card-name-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The certificate-pinned API from bunq — 2 operation(s) for certificate-pinned.
  name: bunq Certificate Pinned API
  slug: bunq-certificate-pinned-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The challenge-request API from bunq — 1 operation(s) for challenge-request.
  name: bunq Challenge Request API
  slug: bunq-challenge-request-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The company API from bunq — 2 operation(s) for company.
  name: bunq Company API
  slug: bunq-company-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The confirmation-of-funds API from bunq — 1 operation(s) for confirmation-of-funds.
  name: bunq Confirmation Of Funds API
  slug: bunq-confirmation-of-funds-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The content API from bunq — 9 operation(s) for content.
  name: bunq Content API
  slug: bunq-content-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The credential-password-ip API from bunq — 2 operation(s) for credential-password-ip.
  name: bunq Credential Password Ip API
  slug: bunq-credential-password-ip-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The currency-cloud-beneficiary API from bunq — 2 operation(s) for currency-cloud-beneficiary.
  name: bunq Currency Cloud Beneficiary API
  slug: bunq-currency-cloud-beneficiary-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The currency-cloud-beneficiary-requirement API from bunq — 1 operation(s) for currency-cloud-beneficiary-requirement.
  name: bunq Currency Cloud Beneficiary Requirement API
  slug: bunq-currency-cloud-beneficiary-requirement-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The currency-cloud-payment-quote API from bunq — 1 operation(s) for currency-cloud-payment-quote.
  name: bunq Currency Cloud Payment Quote API
  slug: bunq-currency-cloud-payment-quote-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The currency-conversion API from bunq — 2 operation(s) for currency-conversion.
  name: bunq Currency Conversion API
  slug: bunq-currency-conversion-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The currency-conversion-quote API from bunq — 2 operation(s) for currency-conversion-quote.
  name: bunq Currency Conversion Quote API
  slug: bunq-currency-conversion-quote-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The definition API from bunq — 1 operation(s) for definition.
  name: bunq Definition API
  slug: bunq-definition-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The device API from bunq — 2 operation(s) for device.
  name: bunq Device API
  slug: bunq-device-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The device-server API from bunq — 2 operation(s) for device-server.
  name: bunq Device Server API
  slug: bunq-device-server-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The draft-payment API from bunq — 2 operation(s) for draft-payment.
  name: bunq Draft Payment API
  slug: bunq-draft-payment-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The event API from bunq — 2 operation(s) for event.
  name: bunq Event API
  slug: bunq-event-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The export-annual-overview API from bunq — 2 operation(s) for export-annual-overview.
  name: bunq Export Annual Overview API
  slug: bunq-export-annual-overview-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The export-rib API from bunq — 2 operation(s) for export-rib.
  name: bunq Export Rib API
  slug: bunq-export-rib-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The export-statement-card API from bunq — 2 operation(s) for export-statement-card.
  name: bunq Export Statement Card API
  slug: bunq-export-statement-card-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The export-statement-card-csv API from bunq — 2 operation(s) for export-statement-card-csv.
  name: bunq Export Statement Card CSV API
  slug: bunq-export-statement-card-csv-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The export-statement-card-pdf API from bunq — 2 operation(s) for export-statement-card-pdf.
  name: bunq Export Statement Card PDF API
  slug: bunq-export-statement-card-pdf-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The feature-announcement API from bunq — 1 operation(s) for feature-announcement.
  name: bunq Feature Announcement API
  slug: bunq-feature-announcement-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The generated-cvc2 API from bunq — 2 operation(s) for generated-cvc2.
  name: bunq Generated Cvc2 API
  slug: bunq-generated-cvc2-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The health-check API from bunq — 1 operation(s) for health-check.
  name: bunq Health Check API
  slug: bunq-health-check-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The ideal-merchant-transaction API from bunq — 2 operation(s) for ideal-merchant-transaction.
  name: bunq Ideal Merchant Transaction API
  slug: bunq-ideal-merchant-transaction-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The insight-preference-date API from bunq — 1 operation(s) for insight-preference-date.
  name: bunq Insight Preference Date API
  slug: bunq-insight-preference-date-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The insights API from bunq — 1 operation(s) for insights.
  name: bunq Insights API
  slug: bunq-insights-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The insights-search API from bunq — 1 operation(s) for insights-search.
  name: bunq Insights Search API
  slug: bunq-insights-search-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The installation API from bunq — 2 operation(s) for installation.
  name: bunq Installation API
  slug: bunq-installation-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The instance API from bunq — 2 operation(s) for instance.
  name: bunq Instance API
  slug: bunq-instance-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The invoice API from bunq — 4 operation(s) for invoice.
  name: bunq Invoice API
  slug: bunq-invoice-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The invoice-export API from bunq — 2 operation(s) for invoice-export.
  name: bunq Invoice Export API
  slug: bunq-invoice-export-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The ip API from bunq — 2 operation(s) for ip.
  name: bunq Ip API
  slug: bunq-ip-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The legal-name API from bunq — 1 operation(s) for legal-name.
  name: bunq Legal Name API
  slug: bunq-legal-name-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The limit API from bunq — 1 operation(s) for limit.
  name: bunq Limit API
  slug: bunq-limit-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The mastercard-action API from bunq — 2 operation(s) for mastercard-action.
  name: bunq Mastercard Action API
  slug: bunq-mastercard-action-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The monetary-account-bank API from bunq — 2 operation(s) for monetary-account-bank.
  name: bunq Monetary Account Bank API
  slug: bunq-monetary-account-bank-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The monetary-account-card API from bunq — 2 operation(s) for monetary-account-card.
  name: bunq Monetary Account Card API
  slug: bunq-monetary-account-card-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The monetary-account-external API from bunq — 2 operation(s) for monetary-account-external.
  name: bunq Monetary Account External API
  slug: bunq-monetary-account-external-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The monetary-account-external-savings API from bunq — 2 operation(s) for monetary-account-external-savings.
  name: bunq Monetary Account External Savings API
  slug: bunq-monetary-account-external-savings-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The monetary-account-joint API from bunq — 2 operation(s) for monetary-account-joint.
  name: bunq Monetary Account Joint API
  slug: bunq-monetary-account-joint-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The monetary-account-savings API from bunq — 2 operation(s) for monetary-account-savings.
  name: bunq Monetary Account Savings API
  slug: bunq-monetary-account-savings-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The name API from bunq — 1 operation(s) for name.
  name: bunq Name API
  slug: bunq-name-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The note-attachment API from bunq — 40 operation(s) for note-attachment.
  name: bunq Note Attachment API
  slug: bunq-note-attachment-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The note-text API from bunq — 40 operation(s) for note-text.
  name: bunq Note Text API
  slug: bunq-note-text-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The notification-filter-email API from bunq — 1 operation(s) for notification-filter-email.
  name: bunq Notification Filter Email API
  slug: bunq-notification-filter-email-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The notification-filter-failure API from bunq — 1 operation(s) for notification-filter-failure.
  name: bunq Notification Filter Failure API
  slug: bunq-notification-filter-failure-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The notification-filter-push API from bunq — 1 operation(s) for notification-filter-push.
  name: bunq Notification Filter Push API
  slug: bunq-notification-filter-push-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The notification-filter-url API from bunq — 2 operation(s) for notification-filter-url.
  name: bunq Notification Filter URL API
  slug: bunq-notification-filter-url-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The oauth-client API from bunq — 2 operation(s) for oauth-client.
  name: bunq OAUTH Client API
  slug: bunq-oauth-client-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The payment-auto-allocate API from bunq — 3 operation(s) for payment-auto-allocate.
  name: bunq Payment Auto Allocate API
  slug: bunq-payment-auto-allocate-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The payment-batch API from bunq — 2 operation(s) for payment-batch.
  name: bunq Payment Batch API
  slug: bunq-payment-batch-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The payment-service-provider-credential API from bunq — 2 operation(s) for payment-service-provider-credential.
  name: bunq Payment Service Provider Credential API
  slug: bunq-payment-service-provider-credential-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The payment-service-provider-draft-payment API from bunq — 2 operation(s) for payment-service-provider-draft-payment.
  name: bunq Payment Service Provider Draft Payment API
  slug: bunq-payment-service-provider-draft-payment-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The payment-service-provider-issuer-transaction API from bunq — 2 operation(s) for payment-service-provider-issuer-transaction.
  name: bunq Payment Service Provider Issuer Transaction API
  slug: bunq-payment-service-provider-issuer-transaction-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The pdf-content API from bunq — 1 operation(s) for pdf-content.
  name: bunq PDF Content API
  slug: bunq-pdf-content-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The replace API from bunq — 1 operation(s) for replace.
  name: bunq Replace API
  slug: bunq-replace-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The request-inquiry-batch API from bunq — 2 operation(s) for request-inquiry-batch.
  name: bunq Request Inquiry Batch API
  slug: bunq-request-inquiry-batch-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The request-response API from bunq — 2 operation(s) for request-response.
  name: bunq Request Response API
  slug: bunq-request-response-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The sandbox-user-company API from bunq — 1 operation(s) for sandbox-user-company.
  name: bunq Sandbox User Company API
  slug: bunq-sandbox-user-company-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The sandbox-user-person API from bunq — 1 operation(s) for sandbox-user-person.
  name: bunq Sandbox User Person API
  slug: bunq-sandbox-user-person-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The schedule API from bunq — 3 operation(s) for schedule.
  name: bunq Schedule API
  slug: bunq-schedule-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The schedule-instance API from bunq — 2 operation(s) for schedule-instance.
  name: bunq Schedule Instance API
  slug: bunq-schedule-instance-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The schedule-payment API from bunq — 2 operation(s) for schedule-payment.
  name: bunq Schedule Payment API
  slug: bunq-schedule-payment-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The schedule-payment-batch API from bunq — 2 operation(s) for schedule-payment-batch.
  name: bunq Schedule Payment Batch API
  slug: bunq-schedule-payment-batch-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The server-error API from bunq — 1 operation(s) for server-error.
  name: bunq Server Error API
  slug: bunq-server-error-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The server-public-key API from bunq — 1 operation(s) for server-public-key.
  name: bunq Server Public Key API
  slug: bunq-server-public-key-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The session API from bunq — 1 operation(s) for session.
  name: bunq Session API
  slug: bunq-session-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The session-server API from bunq — 1 operation(s) for session-server.
  name: bunq Session Server API
  slug: bunq-session-server-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The share-invite-monetary-account-inquiry API from bunq — 2 operation(s) for share-invite-monetary-account-inquiry.
  name: bunq Share Invite Monetary Account Inquiry API
  slug: bunq-share-invite-monetary-account-inquiry-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The share-invite-monetary-account-response API from bunq — 2 operation(s) for share-invite-monetary-account-response.
  name: bunq Share Invite Monetary Account Response API
  slug: bunq-share-invite-monetary-account-response-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The sofort-merchant-transaction API from bunq — 2 operation(s) for sofort-merchant-transaction.
  name: bunq Sofort Merchant Transaction API
  slug: bunq-sofort-merchant-transaction-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The statement API from bunq — 2 operation(s) for statement.
  name: bunq Statement API
  slug: bunq-statement-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The switch-service-payment API from bunq — 1 operation(s) for switch-service-payment.
  name: bunq Switch Service Payment API
  slug: bunq-switch-service-payment-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The token-qr-request-ideal API from bunq — 1 operation(s) for token-qr-request-ideal.
  name: bunq Token Qr Request Ideal API
  slug: bunq-token-qr-request-ideal-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The token-qr-request-sofort API from bunq — 1 operation(s) for token-qr-request-sofort.
  name: bunq Token Qr Request Sofort API
  slug: bunq-token-qr-request-sofort-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The transferwise-currency API from bunq — 1 operation(s) for transferwise-currency.
  name: bunq Transferwise Currency API
  slug: bunq-transferwise-currency-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The transferwise-quote API from bunq — 2 operation(s) for transferwise-quote.
  name: bunq Transferwise Quote API
  slug: bunq-transferwise-quote-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The transferwise-quote-temporary API from bunq — 2 operation(s) for transferwise-quote-temporary.
  name: bunq Transferwise Quote Temporary API
  slug: bunq-transferwise-quote-temporary-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The transferwise-recipient API from bunq — 2 operation(s) for transferwise-recipient.
  name: bunq Transferwise Recipient API
  slug: bunq-transferwise-recipient-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The transferwise-recipient-requirement API from bunq — 1 operation(s) for transferwise-recipient-requirement.
  name: bunq Transferwise Recipient Requirement API
  slug: bunq-transferwise-recipient-requirement-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The transferwise-transfer API from bunq — 2 operation(s) for transferwise-transfer.
  name: bunq Transferwise Transfer API
  slug: bunq-transferwise-transfer-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The transferwise-transfer-requirement API from bunq — 1 operation(s) for transferwise-transfer-requirement.
  name: bunq Transferwise Transfer Requirement API
  slug: bunq-transferwise-transfer-requirement-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The transferwise-user API from bunq — 1 operation(s) for transferwise-user.
  name: bunq Transferwise User API
  slug: bunq-transferwise-user-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The tree-progress API from bunq — 1 operation(s) for tree-progress.
  name: bunq Tree Progress API
  slug: bunq-tree-progress-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The user-company API from bunq — 1 operation(s) for user-company.
  name: bunq User Company API
  slug: bunq-user-company-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The user-payment-service-provider API from bunq — 1 operation(s) for user-payment-service-provider.
  name: bunq User Payment Service Provider API
  slug: bunq-user-payment-service-provider-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The user-person API from bunq — 1 operation(s) for user-person.
  name: bunq User Person API
  slug: bunq-user-person-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The whitelist-sdd API from bunq — 4 operation(s) for whitelist-sdd.
  name: bunq Whitelist Sdd API
  slug: bunq-whitelist-sdd-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The whitelist-sdd-one-off API from bunq — 2 operation(s) for whitelist-sdd-one-off.
  name: bunq Whitelist Sdd One Off API
  slug: bunq-whitelist-sdd-one-off-api
- baseURL: https://api.bunq.com/v1
  baseurl_source: declared
  description: The whitelist-sdd-recurring API from bunq — 2 operation(s) for whitelist-sdd-recurring.
  name: bunq Whitelist Sdd Recurring API
  slug: bunq-whitelist-sdd-recurring-api
artifact_total: 131
collections:
- collection_type: open
  name: bunq Public Attachment API
  slug: open-bunq-attachment-api
- collection_type: open
  name: bunq Public Attachment Card API
  slug: open-bunq-card-api
- collection_type: open
  name: bunq Public Attachment Customer Statement API
  slug: open-bunq-customer-statement-api
- collection_type: open
  name: bunq Public Attachment Handshake API
  slug: open-bunq-handshake-api
- collection_type: open
  name: bunq Public Attachment Monetary Account API
  slug: open-bunq-monetary-account-api
- collection_type: open
  name: bunq Public Attachment Notification Filter API
  slug: open-bunq-notification-filter-api
- collection_type: open
  name: bunq Public Attachment Payment API
  slug: open-bunq-payment-api
- collection_type: open
  name: bunq Public Attachment Request Inquiry API
  slug: open-bunq-request-inquiry-api
- collection_type: open
  name: bunq Public Attachment User API
  slug: open-bunq-user-api
- collection_type: open
  name: bunq Public API
  slug: open-bunq
common:
- group: other
  href: https://artifacts.apis.io/bunq/capabilities/bunq-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bunq-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bunq/agentic-access/bunq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bunq-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bunq/authentication/bunq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bunq-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bunq/security/bunq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bunq-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bunq/security/bunq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bunq-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bunq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bunq
- group: company
  title: ''
  type: Website
  url: https://www.bunq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.bunq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bunq.com/
- group: commercial
  href: https://artifacts.apis.io/bunq/plans/bunq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bunq-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bunq/rate-limits/bunq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bunq-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bunq/finops/bunq-finops.yml
  title: ''
  type: FinOps
  url: finops/bunq-finops.yml
- group: start
  title: ''
  type: Sandbox
  url: https://beta.doc.bunq.com/basics/sandbox
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bunq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bunq.com/en-us/documents/pricing-sheet
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bunq.com/documents/terms-conditions
- group: company
  title: ''
  type: Blog
  url: https://medium.com/bunq-developers-corner
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/bunq-developers-corner
created: '2023-11-13'
description: bunq is a European (Dutch) neobank offering personal and business accounts across the EU. Its Public API is a REST API over HTTPS (https://api.bunq.com/v1, sandbox https://public-api.sandbox.bunq.com/v1) that lets account holders and licensed third parties read accounts, initiate SEPA and internal payments, send and answer payment requests, manage cards, export statements, upload attachments, and subscribe to event callbacks. bunq uses a distinctive multi-step handshake - installation (register an RSA public key), device-server, then session-server - after which requests are RSA-signed with X-Bunq-Client-Signature and authenticated with a session token in X-Bunq-Client-Authentication.
finops:
- has_sources: true
  method: generated
  name: Bunq Finops
  primary_unit: ''
  service_category: Banking / Fintech
  slug: bunq-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bunq.png
layout: provider
modified: '2026-07-12'
name: bunq
nav: Providers
network: true
overview: 'bunq publishes 113 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attachment API, Card API, Customer Statement API, and 110 more. Tagged areas include Banking, Neobank, Payments, Account, and SEPA.


  The bunq catalog on APIs.io includes 1 Spectral governance ruleset.


  bunq''s developer surface includes authentication, documentation, sandbox, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Bunq Plans Pricing
  plan_count: 7
  slug: bunq-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Bunq Rate Limits
  slug: bunq-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: bunq API Rules
  rule_count: 61
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 5
  slug: bunq-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 52.2
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 91.9
      total: 123
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bunq/bunq-2026-06-20T173803.png
security:
- kind: authentication
  name: Bunq Authentication
  slug: bunq-authentication
  summary_line: apiKey/signature · 3 schemes
- kind: domain-security
  name: Bunq Domain Security
  slug: bunq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bunq Vulnerability Disclosure
  slug: bunq-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bunq
tags:
- Banking
- Neobank
- Payments
- Account
- SEPA
- Open Banking
- Fintech
- Europe
- Netherlands
website: https://www.bunq.com/
---
