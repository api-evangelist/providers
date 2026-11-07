---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 60
  human_in_the_loop: 3
  name: Barclays Agentic Access
  operation_count: 182
  slug: barclays-agentic-access
  summary_line: 182 operations · 60 acting · 3 human-in-the-loop
api_count: 52
apis:
- description: Barclays Smartpay Web Payment API enables businesses to accept payments on their website with real-time processing, secure encryption, and fraud prevention.
  name: Barclays Smartpay Web Payment API
  slug: barclaycard-smartpay-web-payment-api
- description: Barclaycard Smartpay Connect (v1.33.0) integrates card payment terminals and point-of-sale systems with Barclaycard acquiring. Listed in the Barclays API Exchange catalogue with no machine-readable co
  name: Barclaycard Smartpay Connect API
  slug: barclaycard-smartpay-connect-api
- description: 'Corporate, bank and PSP clients initiate payments in real time (v2.7). Listed in the Barclays API Exchange catalogue with no machine-readable contract published — its OpenAPI design export returns an '
  name: Barclays Corporate Payment Initiation API
  slug: corporate-payment-initiation-api
- description: Corporate, bank and PSP clients retrieve account balance and transaction reporting (v1.3). Listed in the Barclays API Exchange catalogue with no machine-readable contract published — its OpenAPI desig
  name: Barclays Balances and Transactions Reporting API
  slug: balances-and-transactions-reporting-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Create Account Access Consents
  name: Barclays Account Access Consents API
  slug: barclays-account-access-consents-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Accounts
  name: Barclays Accounts API
  slug: barclays-accounts-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Apply Product External API
  name: Barclays Apply Product External API OAS API
  slug: barclays-applyproductexternalapi-oas-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Atms API from Barclays — 1 operation(s) for atms.
  name: Barclays Atms API
  slug: barclays-atms-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Balances
  name: Barclays Balances API
  slug: barclays-balances-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Beneficiaries
  name: Barclays Beneficiaries API
  slug: barclays-beneficiaries-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Branches API from Barclays — 1 operation(s) for branches.
  name: Barclays Branches API
  slug: barclays-branches-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Business Current Accounts API from Barclays — 1 operation(s) for business current accounts.
  name: Barclays Business Current Accounts API
  slug: barclays-business-current-accounts-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The card account details inquiry external API is Barclays US’s credit cards acquisitions solution which will orchestrate the Internal API calls providing account information, such as account peek/summ
  name: Barclays Card Account Details Inquiry External API
  slug: barclays-card-account-details-inquiry-external-api-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: API for locking and unlocking cards and retrieving card lock/unlock status based on account ID with fraud verification.
  name: Barclays Card Controls API
  slug: barclays-card-controls-api-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: API for activating cards and retrieving activation status based on account ID with eligibility and fraud verification.
  name: Barclays Cards Activation API
  slug: barclays-cards-activation-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Commercial Credit Cards API from Barclays — 1 operation(s) for commercial credit cards.
  name: Barclays Commercial Credit Cards API
  slug: barclays-commercial-credit-cards-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Consents API from Barclays — 10 operation(s) for consents.
  name: Barclays Consents API
  slug: barclays-consents-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Provisions credit cards to digital wallets with eligibility verification and fraud assessment
  name: Barclays Digital Wallet Provision API
  slug: barclays-digital-wallet-provision-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Direct Debits
  name: Barclays Direct Debits API
  slug: barclays-direct-debits-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Domestic Payments
  name: Barclays Domestic Payments API
  slug: barclays-domestic-payments-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Domestic Scheduled Payments
  name: Barclays Domestic Scheduled Payments API
  slug: barclays-domestic-scheduled-payments-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Domestic Standing Orders
  name: Barclays Domestic Standing Orders API
  slug: barclays-domestic-standing-orders-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Domestic VRP Consents
  name: Barclays Domestic VRP Consents API
  slug: barclays-domestic-vrp-consents-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Domestic VRP
  name: Barclays Domestic VRPs API
  slug: barclays-domestic-vrps-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Event Subscriptions
  name: Barclays Event Subscriptions API
  slug: barclays-event-subscriptions-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Events
  name: Barclays Events API
  slug: barclays-events-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Endpoint for getting FCA Business Current Accounts Service Metrics data
  name: Barclays FCSSRVMBCA API
  slug: barclays-fcssrvmbca-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Endpoint for getting FCA Personal Current Accounts Service Metrics data
  name: Barclays FCSSRVMPCA API
  slug: barclays-fcssrvmpca-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: File Payments
  name: Barclays File Payments API
  slug: barclays-file-payments-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Funds Confirmation Consents API from Barclays — 2 operation(s) for funds confirmation consents.
  name: Barclays Funds Confirmation Consents API
  slug: barclays-funds-confirmation-consents-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Funds Confirmations API from Barclays — 1 operation(s) for funds confirmations.
  name: Barclays Funds Confirmations API
  slug: barclays-funds-confirmations-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Authorization transactions operations
  name: Barclays Get Authorizations API
  slug: barclays-getauthorizations-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: International Payments
  name: Barclays International Payments API
  slug: barclays-international-payments-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: International Scheduled Payments
  name: Barclays International Scheduled Payments API
  slug: barclays-international-scheduled-payments-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: International Standing Orders
  name: Barclays International Standing Orders API
  slug: barclays-international-standing-orders-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Key Exchange Fetch Operation APIs
  name: Barclays Key Exchange Fetch JSON Web Keys API
  slug: barclays-key-exchange-fetch-json-web-keys-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Offers
  name: Barclays Offers API
  slug: barclays-offers-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Parties
  name: Barclays Parties API
  slug: barclays-parties-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Payment Details
  name: Barclays Payment Details API
  slug: barclays-payment-details-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: OAS3 External AutoPay APIs
  name: Barclays Payment Product External API Auto Pay API
  slug: barclays-paymentproductexternalapi-autopay-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: OAS3 External Account APIs
  name: Barclays Payment Product External API External Account API
  slug: barclays-paymentproductexternalapi-externalaccount-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: OAS3 External Onetime Payment APIs
  name: Barclays Payment Product External API One Time Payment API
  slug: barclays-paymentproductexternalapi-onetimepayment-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Payments API from Barclays — 15 operation(s) for payments.
  name: Barclays Payments API
  slug: barclays-payments-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Personal Current Accounts API from Barclays — 1 operation(s) for personal current accounts.
  name: Barclays Personal Current Accounts API
  slug: barclays-personal-current-accounts-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Posted transactions operations
  name: Barclays Posted Transaction API
  slug: barclays-postedtransactionapi-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Products
  name: Barclays Products API
  slug: barclays-products-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Register API from Barclays — 1 operation(s) for register.
  name: Barclays Register API
  slug: barclays-register-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Rewards-Balance API from Barclays — 1 operation(s) for rewards-balance.
  name: Barclays Rewards Balance API
  slug: barclays-rewards-balance-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Rewards-Redemption API from Barclays — 1 operation(s) for rewards-redemption.
  name: Barclays Rewards Redemption API
  slug: barclays-rewards-redemption-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Rewards-Redemption-Capabilities API from Barclays — 1 operation(s) for rewards-redemption-capabilities.
  name: Barclays Rewards Redemption Capabilities API
  slug: barclays-rewards-redemption-capabilities-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Rewards-Redemption-Eligibility API from Barclays — 1 operation(s) for rewards-redemption-eligibility.
  name: Barclays Rewards Redemption Eligibility API
  slug: barclays-rewards-redemption-eligibility-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Rewards-Redemption-History API from Barclays — 1 operation(s) for rewards-redemption-history.
  name: Barclays Rewards Redemption History API
  slug: barclays-rewards-redemption-history-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Rewards Earn History Details
  name: Barclays Rewards Earn History API
  slug: barclays-rewardsearnhistory-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Scheduled Payments
  name: Barclays Scheduled Payments API
  slug: barclays-scheduled-payments-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Transaction search options operations
  name: Barclays Search Options API
  slug: barclays-searchoptionsapi-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Standing Orders
  name: Barclays Standing Orders API
  slug: barclays-standing-orders-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Statement cycle dates operations
  name: Barclays Statement Cycle Dates API
  slug: barclays-statementcycledatesapi-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Statements
  name: Barclays Statements API
  slug: barclays-statements-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Returns list of statements
  name: Barclays Statements List API
  slug: barclays-statements-list-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The tier-update-xapi API from Barclays — 1 operation(s) for tier-update-xapi.
  name: Barclays Tier Update Xapi API
  slug: barclays-tier-update-xapi-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: Get Transactions
  name: Barclays Transactions API
  slug: barclays-transactions-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: The Unsecured Sme Loans API from Barclays — 1 operation(s) for unsecured sme loans.
  name: Barclays Unsecured Sme Loans API
  slug: barclays-unsecured-sme-loans-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: User identity context API
  name: Barclays User Identity Context API
  slug: barclays-user-identity-context-api
- baseURL: https://telesto.api.barclays/open-banking/v3.1
  baseurl_source: declared
  description: User sso context API
  name: Barclays User SSO Context API
  slug: barclays-user-sso-context-api
artifact_total: 171
asyncapis:
- description: ''
  name: Barclays Webhooks
  slug: barclays-webhooks
common:
- group: build
  href: https://artifacts.apis.io/barclays/integrations/barclays-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/barclays-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/barclays/agentic-access/barclays-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/barclays-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/barclays/rules/barclays-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/barclays-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/barclays/rules/barclays-rules.yml
  title: ''
  type: Spectral
  url: rules/barclays-rules.yml
- group: design
  href: https://artifacts.apis.io/barclays/rules/barclays-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/barclays-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/barclays/vocabulary/barclays-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/barclays-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/barclays/lifecycle/barclays-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/barclays-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/barclays/well-known/barclays-www-barclays-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barclays-www-barclays-com-security.txt
- group: auth
  href: https://artifacts.apis.io/barclays/well-known/barclays-www-barclays-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barclays-www-barclays-co-uk-security.txt
- group: auth
  href: https://artifacts.apis.io/barclays/well-known/barclays-www-barclaycard-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barclays-www-barclaycard-co-uk-security.txt
- group: other
  href: https://artifacts.apis.io/barclays/hosts/barclays-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barclays-hosts.yml
- group: other
  href: https://artifacts.apis.io/barclays/vendors/barclays-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barclays-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/barclays/finops/barclays-finops.yml
  title: ''
  type: FinOps
  url: finops/barclays-finops.yml
- group: other
  href: https://artifacts.apis.io/barclays/capabilities/barclays-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/barclays-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-bank-ireland-confirmation-of-funds-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-bank-ireland-confirmation-of-funds-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-account-and-transactions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-account-and-transactions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-bank-ireland-account-information-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-bank-ireland-account-information-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-bank-ireland-payment-initiation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-bank-ireland-payment-initiation-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-confirmation-of-funds-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-confirmation-of-funds-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-dynamic-client-registration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-dynamic-client-registration-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-event-notification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-event-notification-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-payment-initiation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-payment-initiation-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-atm-locator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-atm-locator-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-branch-locator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-branch-locator-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-fca-service-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-fca-service-metrics-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-product-details-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-product-details-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-accounts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-accounts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-authentication-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-card-application-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-card-application-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-cryptography-key-exchange-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-cryptography-key-exchange-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-digital-wallet-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-digital-wallet-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-payments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-payments-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-rewards-loyalty-sync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-rewards-loyalty-sync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-benefits-redemption-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-benefits-redemption-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-transactions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-transactions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-variable-recurring-payment-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-variable-recurring-payment-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-card-control-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-card-control-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-account-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-account-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-statements-retriever-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-statements-retriever-overlay.yaml
- group: other
  href: https://artifacts.apis.io/barclays/overlays/barclays-rewards-earn-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/barclays-rewards-earn-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.barclays.co.uk/
- group: auth
  href: https://artifacts.apis.io/barclays/scopes/barclays-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/barclays-scopes.yml
- group: auth
  href: https://artifacts.apis.io/barclays/authentication/barclays-authentication.yml
  title: ''
  type: Authentication
  url: authentication/barclays-authentication.yml
- group: auth
  href: https://artifacts.apis.io/barclays/security/barclays-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/barclays-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/barclays/security/barclays-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barclays-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://home.barclays/insights/barclays-insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Barclays
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/barclays-bank
- group: start
  title: ''
  type: Portal
  url: https://developer.barclays.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.barclays.com/catalogue
- group: operate
  title: ''
  type: Support
  url: https://developer.barclays.com/support/help-guides
- group: start
  title: ''
  type: Login
  url: https://developer.barclays.com/login
- group: start
  title: ''
  type: Signup
  url: https://drm.developer.barclays.com/s/registration
- group: other
  title: ''
  type: Knowledgebase
  url: https://developer.barclays.com/support/knowledge-base
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.barclays.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.barclays.com/privacy-policy
- group: design
  href: https://artifacts.apis.io/barclays/rules/barclays-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/barclays-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/barclays/vocabulary/barclays-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/barclays-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/barclays/json-ld/barclays-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/barclays-context.jsonld
- group: design
  href: https://artifacts.apis.io/barclays/conventions/barclays-conventions.yml
  title: ''
  type: Conventions
  url: conventions/barclays-conventions.yml
- group: design
  href: https://artifacts.apis.io/barclays/conventions/barclays-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/barclays-conventions.yml
- group: design
  href: https://artifacts.apis.io/barclays/errors/barclays-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/barclays-problem-types.yml
- group: design
  href: https://artifacts.apis.io/barclays/lifecycle/barclays-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/barclays-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/barclays/changelog/barclays-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/barclays-changelog.yml
- group: design
  href: https://artifacts.apis.io/barclays/conformance/barclays-conformance.yml
  title: ''
  type: Conformance
  url: conformance/barclays-conformance.yml
- group: auth
  href: https://artifacts.apis.io/barclays/conformance/barclays-conformance.yml
  title: ''
  type: Compliance
  url: conformance/barclays-conformance.yml
- group: auth
  href: https://artifacts.apis.io/barclays/security/barclays-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/barclays-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/barclays/well-known/barclays-barclays-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barclays-barclays-com-security.txt
- group: agent
  href: https://artifacts.apis.io/barclays/well-known/barclays-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barclays-well-known.yml
- group: design
  href: https://artifacts.apis.io/barclays/asyncapi/barclays-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/barclays-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/barclays/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/barclays/data-model/barclays-data-model.yml
  title: ''
  type: DataModel
  url: data-model/barclays-data-model.yml
- group: start
  href: https://artifacts.apis.io/barclays/sandbox/barclays-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/barclays-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/barclays/plans/barclays-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/barclays-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/barclays/rate-limits/barclays-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/barclays-rate-limits.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.barclays.com/support/help-guides
created: '2025-02-21'
description: 'Barclays is a British multinational bank providing retail and commercial banking, investment banking, wealth management and credit cards. Its developer surface is the Barclays API Exchange (developer.barclays.com), which publishes 30 API versions across three distinct families: UK Open Banking (OBIE Read/Write v3.1 and v4.0), Barclays Bank Ireland (Berlin Group NextGenPSD2), and Barclaycard US card servicing. 26 of them ship a first-party OpenAPI 3.1 contract covering 184 operations, served anonymously from the portal registry. Nothing is callable without registration, access approval, an OAuth 2.0 token and — on the UK Open Banking surface — an Open Banking-issued mTLS transport certificate.'
examples:
- key_count: 3
  name: Account Example
  slug: account-example
- key_count: 3
  name: Transaction Example
  slug: transaction-example
features:
- description: PSD2 and UK Open Banking compliant account balance and transaction access.
  name: Open Banking Account Information
- description: Secure third-party payment initiation from customer accounts.
  name: Payment Initiation
- description: Real-time verification of available funds for payment authorization.
  name: Confirmation of Funds
- description: Location services for Barclays ATMs and branches worldwide.
  name: ATM and Branch Locator
- description: Real-time webhook notifications for account and transaction events.
  name: Event Notifications
- description: Automated TPP registration for Open Banking API access.
  name: Dynamic Client Registration
- description: Loyalty program integration and pay-with-points capabilities.
  name: Rewards and Loyalty
- description: Mobile payment and digital wallet integration.
  name: Digital Wallet
- description: Credit card application submission and status tracking.
  name: Card Applications
- description: Mandated service performance metrics for regulatory reporting.
  name: FCA Compliance Metrics
finops:
- has_sources: true
  method: derived
  name: Barclays Finops
  primary_unit: ''
  service_category: ''
  slug: barclays-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/barclays.png
json_schemas:
- name: Account
  property_count: 7
  slug: account
- name: AccountLookupRequestDataV2
  property_count: 1
  slug: barclays-account-lookup-request-data-v2
- name: ActivateCardRequestData
  property_count: 1
  slug: barclays-activate-card-request-data
- name: AddSubscriptionReqData
  property_count: 1
  slug: barclays-add-subscription-req-data
- name: ApplicationConsentRequest
  property_count: 1
  slug: barclays-application-consent-request
- name: ApplicationVerificationRequest
  property_count: 1
  slug: barclays-application-verification-request
- name: business_account_response
  property_count: 2
  slug: barclays-business-account-response
- name: commercial_credit_cards_response
  property_count: 2
  slug: barclays-commercial-credit-cards-response
- name: create_cof_consent_request
  property_count: 5
  slug: barclays-create-cof-consent-request
- name: create_cof_consent_response
  property_count: 3
  slug: barclays-create-cof-consent-response
- name: create_cof_request
  property_count: 4
  slug: barclays-create-cof-request
- name: create_cof_response
  property_count: 1
  slug: barclays-create-cof-response
- name: create_consent_request
  property_count: 5
  slug: barclays-create-consent-request
- name: create_consent_response
  property_count: 3
  slug: barclays-create-consent-response
- name: DCRRequestType
  property_count: 20
  slug: barclays-dcrrequest-type
- name: DCRResponseType
  property_count: 24
  slug: barclays-dcrresponse-type
- name: get_account_balance_details_response
  property_count: 2
  slug: barclays-get-account-balance-details-response
- name: get_account_details_response
  property_count: 7
  slug: barclays-get-account-details-response
- name: get_account_transaction_details_response
  property_count: 4
  slug: barclays-get-account-transaction-details-response
- name: get_account_transactions_response
  property_count: 2
  slug: barclays-get-account-transactions-response
- name: get_cof_consent_details_response
  property_count: 6
  slug: barclays-get-cof-consent-details-response
- name: get_consent_details_response
  property_count: 6
  slug: barclays-get-consent-details-response
- name: get__fca-service-metrics_bcaResponseMessage_200_schema_
  property_count: 2
  slug: barclays-get-fca-service-metrics-bca-response-message-200-schema
- name: get__fca-service-metrics_pcaResponseMessage_200_schema_
  property_count: 2
  slug: barclays-get-fca-service-metrics-pca-response-message-200-schema
- name: get_payment-auth-status_response
  property_count: 1
  slug: barclays-get-payment-auth-status-response
- name: get_payment-details_response
  property_count: 11
  slug: barclays-get-payment-details-response
- name: initiate_payment_request
  property_count: 10
  slug: barclays-initiate-payment-request
- name: initiate_payment_response
  property_count: 4
  slug: barclays-initiate-payment-response
- name: InstantCreditByAccountRequest
  property_count: 1
  slug: barclays-instant-credit-by-account-request
- name: JWKSKeySetBody
  property_count: 1
  slug: barclays-jwkskey-set-body
- name: LockCardRequestData
  property_count: 1
  slug: barclays-lock-card-request-data
- name: LoyaltyTierRequestData
  property_count: 1
  slug: barclays-loyalty-tier-request-data
- name: LoyaltyTierResponseData
  property_count: 1
  slug: barclays-loyalty-tier-response-data
- name: ModifyPaymentRequestData
  property_count: 1
  slug: barclays-modify-payment-request-data
- name: ModifySubscriptionReqData
  property_count: 1
  slug: barclays-modify-subscription-req-data
- name: OBDomesticVRPConsentRequest
  property_count: 2
  slug: barclays-obdomestic-vrpconsent-request
- name: OBDomesticVRPRequest
  property_count: 2
  slug: barclays-obdomestic-vrprequest
- name: OBEventPolling1
  property_count: 4
  slug: barclays-obevent-polling1
- name: OBEventSubscriptionResponse1
  property_count: 3
  slug: barclays-obevent-subscription-response1
- name: OBEventSubscription1
  property_count: 1
  slug: barclays-obevent-subscription1
- name: OBFundsConfirmationConsent1
  property_count: 1
  slug: barclays-obfunds-confirmation-consent1
- name: OBReadConsent1
  property_count: 2
  slug: barclays-obread-consent1
- name: OBVRPFundsConfirmationRequest
  property_count: 1
  slug: barclays-obvrpfunds-confirmation-request
- name: OBWriteDomesticConsent4
  property_count: 2
  slug: barclays-obwrite-domestic-consent4
- name: OBWriteDomesticScheduledConsent4
  property_count: 2
  slug: barclays-obwrite-domestic-scheduled-consent4
- name: OBWriteDomesticScheduled2
  property_count: 2
  slug: barclays-obwrite-domestic-scheduled2
- name: OBWriteDomesticStandingOrderConsent5
  property_count: 2
  slug: barclays-obwrite-domestic-standing-order-consent5
- name: OBWriteDomesticStandingOrder3
  property_count: 2
  slug: barclays-obwrite-domestic-standing-order3
- name: OBWriteDomestic2
  property_count: 2
  slug: barclays-obwrite-domestic2
- name: OBWriteFileConsent3
  property_count: 1
  slug: barclays-obwrite-file-consent3
- name: OBWriteFileConsent4
  property_count: 1
  slug: barclays-obwrite-file-consent4
- name: OBWriteFile2
  property_count: 1
  slug: barclays-obwrite-file2
- name: OBWriteInternationalConsent5
  property_count: 2
  slug: barclays-obwrite-international-consent5
- name: OBWriteInternationalScheduledConsent5
  property_count: 2
  slug: barclays-obwrite-international-scheduled-consent5
- name: OBWriteInternationalScheduled3
  property_count: 2
  slug: barclays-obwrite-international-scheduled3
- name: OBWriteInternationalStandingOrderConsent6
  property_count: 2
  slug: barclays-obwrite-international-standing-order-consent6
- name: OBWriteInternationalStandingOrder4
  property_count: 2
  slug: barclays-obwrite-international-standing-order4
- name: OBWriteInternational3
  property_count: 2
  slug: barclays-obwrite-international3
- name: personal_account_response
  property_count: 2
  slug: barclays-personal-account-response
- name: PrequalRequest
  property_count: 1
  slug: barclays-prequal-request
- name: PrescreenOffersCaptureRequest
  property_count: 1
  slug: barclays-prescreen-offers-capture-request
- name: PrescreenOffersRequest
  property_count: 1
  slug: barclays-prescreen-offers-request
- name: RedemptionRequestDataV3
  property_count: 1
  slug: barclays-redemption-request-data-v3
- name: RetrieveCardDetailsRequestData
  property_count: 1
  slug: barclays-retrieve-card-details-request-data
- name: SchedulePaymentRequestData
  property_count: 1
  slug: barclays-schedule-payment-request-data
- name: sme_lending_response
  property_count: 2
  slug: barclays-sme-lending-response
- name: UnlockCardRequestData
  property_count: 1
  slug: barclays-unlock-card-request-data
- name: UserIdentityContextRequest
  property_count: 1
  slug: barclays-user-identity-context-request
- name: UserSSOContextRequest
  property_count: 1
  slug: barclays-user-ssocontext-request
- name: WalletProvisionRequestData
  property_count: 1
  slug: barclays-wallet-provision-request-data
- name: PaymentRequest
  property_count: 5
  slug: payment
- name: Transaction
  property_count: 9
  slug: transaction
json_structures:
- name: Barclays Json Structure
  property_count: 0
  slug: barclays-json-structure
jsonld:
- class_count: 2
  name: Barclays Context
  property_count: 17
  slug: barclays-context
layout: provider
modified: '2026-09-04'
name: Barclays
nav: Providers
network: true
overview: 'Barclays publishes 64 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, Apply Product External API OAS API, and 61 more. Tagged areas include Banking, Credit Cards, FAPI, Finance, and Open Banking.


  The Barclays catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Barclays'' developer surface includes authentication, engineering blog, developer portal, documentation, support, signup flow, changelog, and 69 more developer resources.'
plans:
- name: Barclays Plans Pricing
  plan_count: 0
  slug: barclays-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Barclays Rate Limits
  slug: barclays-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Barclays — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: barclays-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Barclays API Rules
  rule_count: 59
  severity_counts:
    error: 40
    hint: 0
    info: 5
    warn: 14
  slug: barclays-rules
- authorship: unmarked
  effective_rule_count: 7
  extends: []
  name: Barclays API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: barclays-spectral-rules
scopes:
- name: Barclays Scopes
  scope_count: 19
  slug: barclays-scopes
  summary_line: 19 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 36
    catalog_earned: 61.0
    catalog_earned_first_party: 0.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 63.0
    developer_ergonomics: 66.1
    discoverability: 62.5
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 60
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 55.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/barclays/barclays-2026-06-20T173004.png
security:
- kind: authentication
  name: Barclays Authentication
  slug: barclays-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Barclays Domain Security
  slug: barclays-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Barclays Vulnerability Disclosure
  slug: barclays-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: barclays-account-information-access
  slug: barclays-account-information-access
- name: barclays-domestic-payment
  slug: barclays-domestic-payment
- name: barclays-open-data-lookup
  slug: barclays-open-data-lookup
slug: barclays
tags:
- Banking
- Credit Cards
- FAPI
- Finance
- Open Banking
- Open Data
- PSD2
- Payments
- UK Banking
- Variable Recurring Payments
use_cases:
- description: Aggregate Barclays account data in budgeting and financial planning apps.
  name: Personal Finance Management
- description: Initiate payments directly from customer bank accounts via PSD2.
  name: Open Banking Payments
- description: Accept Barclays-branded payments via Smartpay Web Payment API.
  name: E-Commerce Checkout
- description: Embed ATM and branch location search in apps and websites.
  name: Branch and ATM Finder
- description: Integrate Barclays Rewards with merchant loyalty programs.
  name: Loyalty Integration
- description: Enable online credit card applications through partner platforms.
  name: Credit Card Origination
website: https://www.barclays.co.uk/
---
