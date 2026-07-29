---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Verifone Agentic Access
  operation_count: 78
  slug: verifone-agentic-access
  summary_line: 78 operations · 60 acting
api_count: 27
apis:
- description: Global payments, recurring billing, and digital wallets — tokenized and PCI compliant. The eCommerce API handles customer payment info capture and order placement via direct server-to-server API calls
  name: Verifone eCommerce API
  slug: verifone-ecommerce-api
- description: SCA-compliant cardholder authentication with frictionless and challenge flows. The 3D Secure API provides Strong Customer Authentication (SCA) compliance through JWT-based flows, lookup functionality,
  name: Verifone 3D Secure API
  slug: verifone-3d-secure-api
- description: Programmatically retrieve and download settlement, transaction, and financial reports from Verifone's cloud platform. The Reporting API provides access to settlement reports, transaction data, and fin
  name: Verifone Reporting API
  slug: verifone-reporting-api
- description: Process PayPal and alternative payments through a single, globally unified checkout integration. The PayPal eCom API supports PayPal transactions, billing agreements, subscription products, billing pl
  name: Verifone PayPal eCommerce API
  slug: verifone-paypal-ecommerce-api
- description: Remote device control and maintenance for POS terminal estates. The VHQ (VerifoneHQ) API enables automated device management, software deployment, health monitoring, application configuration, and rea
  name: Verifone VHQ Device Management API
  slug: verifone-vhq-device-management-api
- description: Operations for listing and retrieving 3DS authentication records. Use these endpoints to query historical authentication results filtered by amount, currency, card, status, and more.
  name: Verifone 3DS Authentication API
  slug: verifone-3ds-authentication-api
- description: The Batch API from Verifone — 1 operation(s) for batch.
  name: Verifone Batch API
  slug: verifone-batch-api
- description: The Billing Agreement API from Verifone — 5 operation(s) for billing agreement.
  name: Verifone Billing Agreement API
  slug: verifone-billing-agreement-api
- description: The Billing Plans API from Verifone — 5 operation(s) for billing plans.
  name: Verifone Billing Plans API
  slug: verifone-billing-plans-api
- description: Create, retrieve, update, and manage checkout sessions. A checkout session generates a hosted payment page URL that the customer visits to complete payment.
  name: Verifone Checkout API
  slug: verifone-checkout-api
- description: Operations for creating, retrieving, updating, and deleting customer records.
  name: Verifone Customer API
  slug: verifone-customer-api
- description: The Ecom Payments API from Verifone — 10 operation(s) for ecom payments.
  name: Verifone Ecom Payments API
  slug: verifone-ecom-payments-api
- description: The Hardware Orders API from Verifone — 1 operation(s) for hardware orders.
  name: Verifone Hardware Orders API
  slug: verifone-hardware-orders-api
- description: The Lookup API from Verifone — 1 operation(s) for lookup.
  name: Verifone Lookup API
  slug: verifone-lookup-api
- description: The Merchant Maintenance API from Verifone — 1 operation(s) for merchant maintenance.
  name: Verifone Merchant Maintenance API
  slug: verifone-merchant-maintenance-api
- description: Operations to manage merchant orders.
  name: Verifone Merchant Orders API
  slug: verifone-merchant-orders-api
- description: The Payment Modifications API from Verifone — 12 operation(s) for payment modifications.
  name: Verifone Payment Modifications API
  slug: verifone-payment-modifications-api
- description: The POI Maintenance API from Verifone — 1 operation(s) for poi maintenance.
  name: Verifone POI Maintenance API
  slug: verifone-poi-maintenance-api
- description: The POI Orders API from Verifone — 1 operation(s) for poi orders.
  name: Verifone POI Orders API
  slug: verifone-poi-orders-api
- description: The Products API from Verifone — 2 operation(s) for products.
  name: Verifone Products API
  slug: verifone-products-api
- description: The Reports API from Verifone — 1 operation(s) for reports.
  name: Verifone Reports API
  slug: verifone-reports-api
- description: The Subscriptions API from Verifone — 7 operation(s) for subscriptions.
  name: Verifone Subscriptions API
  slug: verifone-subscriptions-api
- description: The Templating API from Verifone — 1 operation(s) for templating.
  name: Verifone Templating API
  slug: verifone-templating-api
- description: The Theming API from Verifone — 1 operation(s) for theming.
  name: Verifone Theming API
  slug: verifone-theming-api
- description: The Token Management API from Verifone — 4 operation(s) for token management.
  name: Verifone Token Management API
  slug: verifone-token-management-api
- description: The Transaction API from Verifone — 3 operation(s) for transaction.
  name: Verifone Transaction API
  slug: verifone-transaction-api
- description: The Transactions API from Verifone — 7 operation(s) for transactions.
  name: Verifone Transactions API
  slug: verifone-transactions-api
artifact_total: 542
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/verifone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verifone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/verifone-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.verifone.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.verifone.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.verifone.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.verifone.com/online-payments/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.verifone.com/online-payments/api-integration-methods-auth-and-endpoints/api-authentication
- group: start
  title: ''
  type: Sandbox
  url: https://cst.test-gsc.vfims.com
- group: company
  title: ''
  type: Blog
  url: https://verifone.cloud/blog
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/verifone/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/verifone/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/verifone/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Verifone is a global payment technology company providing REST APIs for POS terminal management, online payment processing, commerce platform integration, and omnichannel payment acceptance. Their developer platform covers in-person payments, eCommerce, hosted checkout, 3D Secure authentication, customer management, device management via VHQ, hardware ordering, and financial reporting across EMEA, Americas, and Asia-Pacific regions.
examples:
- key_count: 5
  name: 3Ds Authentication Api Getv23D
  slug: 3ds-authentication-api-getv23d
- key_count: 5
  name: 3Ds Authentication Api Postv2Lookup
  slug: 3ds-authentication-api-postv2lookup
- key_count: 5
  name: Checkout Api Listv2Template
  slug: checkout-api-listv2template
- key_count: 5
  name: Customer Api Getv2Customer
  slug: customer-api-getv2customer
- key_count: 5
  name: Customer Api Getv2Customerbyid
  slug: customer-api-getv2customerbyid
- key_count: 5
  name: Customer Api Postv2Customer
  slug: customer-api-postv2customer
- key_count: 5
  name: Customer Api Postv2Customerbyid
  slug: customer-api-postv2customerbyid
- key_count: 5
  name: Ecommerce Api Adjust Payment
  slug: ecommerce-api-adjust-payment
- key_count: 5
  name: Ecommerce Api Affirmcompletetransaction
  slug: ecommerce-api-affirmcompletetransaction
- key_count: 5
  name: Ecommerce Api Affirminittransaction
  slug: ecommerce-api-affirminittransaction
- key_count: 5
  name: Ecommerce Api Captureauthorization
  slug: ecommerce-api-captureauthorization
- key_count: 5
  name: Ecommerce Api Counttransactions
  slug: ecommerce-api-counttransactions
- key_count: 5
  name: Ecommerce Api Createupdatetoken
  slug: ecommerce-api-createupdatetoken
- key_count: 5
  name: Ecommerce Api Extendauthorization
  slug: ecommerce-api-extendauthorization
- key_count: 5
  name: Ecommerce Api Getopbanks
  slug: ecommerce-api-getopbanks
- key_count: 5
  name: Ecommerce Api Gettoken
  slug: ecommerce-api-gettoken
- key_count: 5
  name: Ecommerce Api Issuerinstalmentselection
  slug: ecommerce-api-issuerinstalmentselection
- key_count: 5
  name: Ecommerce Api Klarnainittransaction
  slug: ecommerce-api-klarnainittransaction
- key_count: 5
  name: Ecommerce Api Klarnapaymenttransaction
  slug: ecommerce-api-klarnapaymenttransaction
- key_count: 5
  name: Ecommerce Api Listtransactions
  slug: ecommerce-api-listtransactions
- key_count: 5
  name: Ecommerce Api Mobilepaytransaction
  slug: ecommerce-api-mobilepaytransaction
- key_count: 5
  name: Ecommerce Api Oponlinepaymenttransaction
  slug: ecommerce-api-oponlinepaymenttransaction
- key_count: 5
  name: Ecommerce Api Readtransaction
  slug: ecommerce-api-readtransaction
- key_count: 5
  name: Ecommerce Api Refundpayment
  slug: ecommerce-api-refundpayment
- key_count: 5
  name: Ecommerce Api Releasepreauthorization
  slug: ecommerce-api-releasepreauthorization
- key_count: 5
  name: Ecommerce Api Saletransaction
  slug: ecommerce-api-saletransaction
- key_count: 5
  name: Ecommerce Api Swishtransaction
  slug: ecommerce-api-swishtransaction
- key_count: 5
  name: Ecommerce Api Unmatchedrefund
  slug: ecommerce-api-unmatchedrefund
- key_count: 5
  name: Ecommerce Api Updatetoken
  slug: ecommerce-api-updatetoken
- key_count: 5
  name: Ecommerce Api Vippstransaction
  slug: ecommerce-api-vippstransaction
- key_count: 5
  name: Ecommerce Api Voidauthorization
  slug: ecommerce-api-voidauthorization
- key_count: 5
  name: Ecommerce Api Voidcapture
  slug: ecommerce-api-voidcapture
- key_count: 5
  name: Order Service Api Listbatches
  slug: order-service-api-listbatches
- key_count: 5
  name: Order Service Api Updateentityaddress
  slug: order-service-api-updateentityaddress
- key_count: 5
  name: Paypal Ecommerce Api Getbillingagreementagreementid
  slug: paypal-ecommerce-api-getbillingagreementagreementid
- key_count: 5
  name: Paypal Ecommerce Api Getbillingagreementtokentokenid
  slug: paypal-ecommerce-api-getbillingagreementtokentokenid
- key_count: 5
  name: Paypal Ecommerce Api Getbillingplans
  slug: paypal-ecommerce-api-getbillingplans
- key_count: 5
  name: Paypal Ecommerce Api Getbillingplansplanid
  slug: paypal-ecommerce-api-getbillingplansplanid
- key_count: 5
  name: Paypal Ecommerce Api Getproducts
  slug: paypal-ecommerce-api-getproducts
- key_count: 5
  name: Paypal Ecommerce Api Getproductsid
  slug: paypal-ecommerce-api-getproductsid
- key_count: 5
  name: Paypal Ecommerce Api Getsubscriptionsid
  slug: paypal-ecommerce-api-getsubscriptionsid
- key_count: 5
  name: Paypal Ecommerce Api Postbillingagreementagreementidcancel
  slug: paypal-ecommerce-api-postbillingagreementagreementidcancel
- key_count: 5
  name: Paypal Ecommerce Api Postbillingagreementcreate
  slug: paypal-ecommerce-api-postbillingagreementcreate
- key_count: 5
  name: Paypal Ecommerce Api Postbillingagreementinitiate
  slug: paypal-ecommerce-api-postbillingagreementinitiate
- key_count: 5
  name: Paypal Ecommerce Api Postbillingplanscreate
  slug: paypal-ecommerce-api-postbillingplanscreate
- key_count: 5
  name: Paypal Ecommerce Api Postproducts
  slug: paypal-ecommerce-api-postproducts
- key_count: 5
  name: Paypal Ecommerce Api Postsubscriptions
  slug: paypal-ecommerce-api-postsubscriptions
- key_count: 5
  name: Paypal Ecommerce Api Postsubscriptionsidrevise
  slug: paypal-ecommerce-api-postsubscriptionsidrevise
- key_count: 5
  name: Paypal Ecommerce Api Posttransactions
  slug: paypal-ecommerce-api-posttransactions
- key_count: 5
  name: Paypal Ecommerce Api Posttransactionsidauthorize
  slug: paypal-ecommerce-api-posttransactionsidauthorize
- key_count: 5
  name: Paypal Ecommerce Api Posttransactionsidcapture
  slug: paypal-ecommerce-api-posttransactionsidcapture
- key_count: 5
  name: Paypal Ecommerce Api Posttransactionsidrefund
  slug: paypal-ecommerce-api-posttransactionsidrefund
- key_count: 5
  name: Paypal Ecommerce Api Posttransactionsriskcontext
  slug: paypal-ecommerce-api-posttransactionsriskcontext
- key_count: 5
  name: Reporting Api Get_The_List_Of_All_Reports_Get
  slug: reporting-api-get_the_list_of_all_reports_get
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verifone.png
json_schemas:
- name: AuthenticationResult
  property_count: 26
  slug: 3ds-authentication-api-authenticationresult
- name: DeviceDataInfo
  property_count: 10
  slug: 3ds-authentication-api-devicedatainfo
- name: ErrorDetails
  property_count: 0
  slug: 3ds-authentication-api-errordetails
- name: ErrorResponse
  property_count: 4
  slug: 3ds-authentication-api-errorresponse
- name: LookupRequest
  property_count: 87
  slug: 3ds-authentication-api-lookuprequest
- name: LookupResponse
  property_count: 29
  slug: 3ds-authentication-api-lookupresponse
- name: ThreeDSAuthentication
  property_count: 9
  slug: 3ds-authentication-api-threedsauthentication
- name: ThreeDSAuthenticationList
  property_count: 0
  slug: 3ds-authentication-api-threedsauthenticationlist
- name: additional_business_data
  property_count: 2
  slug: checkout-api-additional_business_data
- name: address_details
  property_count: 11
  slug: checkout-api-address_details
- name: apple_pay
  property_count: 4
  slug: checkout-api-apple_pay
- name: ApplePayCardConfig
  property_count: 6
  slug: checkout-api-applepaycardconfig
- name: application_context
  property_count: 3
  slug: checkout-api-application_context
- name: bank
  property_count: 5
  slug: checkout-api-bank
- name: basic_card
  property_count: 4
  slug: checkout-api-basic_card
- name: billing
  property_count: 11
  slug: checkout-api-billing
- name: card_capture_mode
  property_count: 0
  slug: checkout-api-card_capture_mode
- name: card_mode
  property_count: 0
  slug: checkout-api-card_mode
- name: card_req
  property_count: 6
  slug: checkout-api-card_req
- name: CardCaptureRequest
  property_count: 13
  slug: checkout-api-cardcapturerequest
- name: CardConfiguration
  property_count: 4
  slug: checkout-api-cardconfiguration
- name: CardMode3DS
  property_count: 0
  slug: checkout-api-cardmode3ds
- name: CardMode3DSPayment
  property_count: 0
  slug: checkout-api-cardmode3dspayment
- name: CardModeCapture
  property_count: 0
  slug: checkout-api-cardmodecapture
- name: CardModePayment
  property_count: 0
  slug: checkout-api-cardmodepayment
- name: CreateTemplateRequest
  property_count: 5
  slug: checkout-api-checkouttemplate
- name: config
  property_count: 1
  slug: checkout-api-config
- name: consentTextDynamicValues
  property_count: 0
  slug: checkout-api-consenttextdynamicvalues
- name: StandardRequest
  property_count: 31
  slug: checkout-api-createcheckoutrequest
- name: CreateCheckoutResponse
  property_count: 2
  slug: checkout-api-createcheckoutresponse
- name: customer_details
  property_count: 10
  slug: checkout-api-customer_details
- name: details
  property_count: 0
  slug: checkout-api-details
- name: EmailNotification
  property_count: 1
  slug: checkout-api-emailnotification
- name: ErrorResponse
  property_count: 4
  slug: checkout-api-errorresponse
- name: gift_card
  property_count: 2
  slug: checkout-api-gift_card
- name: GiftCardCardConfig
  property_count: 5
  slug: checkout-api-giftcardcardconfig
- name: GooglePayCardConfigRequest
  property_count: 6
  slug: checkout-api-googlepaycardconfigrequest
- name: GooglePayPaymentConfig
  property_count: 4
  slug: checkout-api-googlepaypaymentconfig
- name: GPP2PaymentConfig
  property_count: 2
  slug: checkout-api-gpp2paymentconfig
- name: I18nConfiguration
  property_count: 3
  slug: checkout-api-i18nconfiguration
- name: InstalmentConfiguration
  property_count: 2
  slug: checkout-api-instalmentconfiguration
- name: KlarnaPaymentConfig
  property_count: 1
  slug: checkout-api-klarnapaymentconfig
- name: LineItem
  property_count: 12
  slug: checkout-api-lineitem
- name: mobile_pay_req
  property_count: 4
  slug: checkout-api-mobile_pay_req
- name: notification_methods
  property_count: 2
  slug: checkout-api-notification_methods
- name: op
  property_count: 2
  slug: checkout-api-op
- name: payment_contract_id
  property_count: 0
  slug: checkout-api-payment_contract_id
- name: payment_frequency
  property_count: 2
  slug: checkout-api-payment_frequency
- name: PaymentConfigurations
  property_count: 12
  slug: checkout-api-paymentconfigurations
- name: PaypalPaymentConfig
  property_count: 5
  slug: checkout-api-paypalpaymentconfig
- name: plcc
  property_count: 5
  slug: checkout-api-plcc
- name: plcc_mode
  property_count: 0
  slug: checkout-api-plcc_mode
- name: processing_model_details
  property_count: 6
  slug: checkout-api-processing_model_details
- name: promo_financing_details
  property_count: 3
  slug: checkout-api-promo_financing_details
- name: shipping
  property_count: 11
  slug: checkout-api-shipping
- name: shopper_interaction
  property_count: 0
  slug: checkout-api-shopper_interaction
- name: SMSNotification
  property_count: 1
  slug: checkout-api-smsnotification
- name: stored_credential
  property_count: 7
  slug: checkout-api-stored_credential
- name: swish_req
  property_count: 2
  slug: checkout-api-swish_req
- name: tax
  property_count: 1
  slug: checkout-api-tax
- name: template_field_mode
  property_count: 1
  slug: checkout-api-template_field_mode
- name: TemplateList
  property_count: 0
  slug: checkout-api-templatelist
- name: Theme
  property_count: 21
  slug: checkout-api-theme
- name: threed_secure
  property_count: 54
  slug: checkout-api-threed_secure
- name: ThreeDSData
  property_count: 52
  slug: checkout-api-threedsdata
- name: UpdateThemeRequest
  property_count: 18
  slug: checkout-api-updatethemerequest
- name: VippsCardConfigRequest
  property_count: 3
  slug: checkout-api-vippscardconfigrequest
- name: VippsPaymentConfigRequest
  property_count: 6
  slug: checkout-api-vippspaymentconfigrequest
- name: Billing
  property_count: 11
  slug: customer-api-billing
- name: CustomerListResponse
  property_count: 0
  slug: customer-api-customerlistresponse
- name: CustomerRequest
  property_count: 11
  slug: customer-api-customerrequest
- name: CustomerResponse
  property_count: 14
  slug: customer-api-customerresponse
- name: ErrorResponse
  property_count: 4
  slug: customer-api-errorresponse
- name: Shipping
  property_count: 11
  slug: customer-api-shipping
- name: Tax
  property_count: 1
  slug: customer-api-tax
- name: acquirerAuthorizingNetworkID
  property_count: 0
  slug: ecommerce-api-acquirerauthorizingnetworkid
- name: acquirerAuthorizingNetworkIdDescriptor
  property_count: 0
  slug: ecommerce-api-acquirerauthorizingnetworkiddescriptor
- name: acquirerResponseCode
  property_count: 0
  slug: ecommerce-api-acquirerresponsecode
- name: acquirerResponseMessage
  property_count: 0
  slug: ecommerce-api-acquirerresponsemessage
- name: AdditionalData
  property_count: 7
  slug: ecommerce-api-additionaldata
- name: AdditionalDataDto
  property_count: 10
  slug: ecommerce-api-additionaldatadto
- name: AdjustDto
  property_count: 2
  slug: ecommerce-api-adjustdto
- name: Affirm basket line items
  property_count: 12
  slug: ecommerce-api-affirmlineitem
- name: Affirm Complete Payment Request
  property_count: 2
  slug: ecommerce-api-affirmpaymentcompletionrequest
- name: Affirm Complete Payment Response
  property_count: 15
  slug: ecommerce-api-affirmpaymentcompletionresponse
- name: Affirm Initiate Payment Request
  property_count: 15
  slug: ecommerce-api-affirmpaymentinitiationrequest
- name: Affirm Initiate Payment Result
  property_count: 16
  slug: ecommerce-api-affirmpaymentinitiationresponse
- name: amountDecimal
  property_count: 0
  slug: ecommerce-api-amountdecimal
- name: amountString
  property_count: 0
  slug: ecommerce-api-amountstring
- name: ApplePayMerchantValidationDto
  property_count: 3
  slug: ecommerce-api-applepaymerchantvalidationdto
- name: BadRequestV2Docs
  property_count: 5
  slug: ecommerce-api-badrequestv2docs
- name: BillingDto
  property_count: 8
  slug: ecommerce-api-billingdto
- name: BinDetails
  property_count: 7
  slug: ecommerce-api-bindetails
- name: CaptureCardTransactionDto
  property_count: 8
  slug: ecommerce-api-capturecardtransactiondto
- name: The Card Type
  property_count: 0
  slug: ecommerce-api-cardbrand
- name: CardResponse
  property_count: 17
  slug: ecommerce-api-cardresponse
- name: CountTransactionResponse
  property_count: 1
  slug: ecommerce-api-counttransactionresponse
- name: CreateWalletDto
  property_count: 32
  slug: ecommerce-api-createwalletdto
- name: Currency Code
  property_count: 0
  slug: ecommerce-api-currencycodeenum
- name: Customer
  property_count: 10
  slug: ecommerce-api-customerdetailsdto
- name: Shipping Address
  property_count: 9
  slug: ecommerce-api-customerdetailsshippinginformationdto
- name: Detailed Amount
  property_count: 3
  slug: ecommerce-api-detailedamount
- name: Details
  property_count: 2
  slug: ecommerce-api-details
- name: ecomPaymentResponse_details
  property_count: 2
  slug: ecommerce-api-ecompaymentresponse_details
- name: ecomPaymentResponse_issuer_instalment_result
  property_count: 12
  slug: ecommerce-api-ecompaymentresponse_issuer_instalment_result
- name: EcomResponse
  property_count: 40
  slug: ecommerce-api-ecomresponse
- name: EcomResponseCard
  property_count: 42
  slug: ecommerce-api-ecomresponsecard
- name: EcomReverseTransactionResponse
  property_count: 2
  slug: ecommerce-api-ecomreversetransactionresponse
- name: EncryptedCardPaymentRequest
  property_count: 32
  slug: ecommerce-api-encryptedcardpaymentrequest
- name: ForbiddenV2Docs
  property_count: 5
  slug: ecommerce-api-forbiddenv2docs
- name: GatewayTransaction
  property_count: 47
  slug: ecommerce-api-gatewaytransaction
- name: GatewayTransactions
  property_count: 47
  slug: ecommerce-api-gatewaytransactions
- name: initiatorTraceId
  property_count: 0
  slug: ecommerce-api-initiatortraceid
- name: instalment
  property_count: 9
  slug: ecommerce-api-instalment
- name: InstalmentDto
  property_count: 3
  slug: ecommerce-api-instalmentdto
- name: InternalErrorV2Docs
  property_count: 5
  slug: ecommerce-api-internalerrorv2docs
- name: issuerCountryEnum
  property_count: 0
  slug: ecommerce-api-issuercountryenum
- name: Issuer Instalment Option Selection Request.
  property_count: 1
  slug: ecommerce-api-issuerinstalmentselectionrequest
- name: Klarna Complete Payment Request
  property_count: 3
  slug: ecommerce-api-klarnapaymentcompletionrequest
- name: Klarna Complete Payment Response
  property_count: 20
  slug: ecommerce-api-klarnapaymentcompletionresponse
- name: klarnaPaymentCompletionResponse_authorized_payment_method
  property_count: 3
  slug: ecommerce-api-klarnapaymentcompletionresponse_authorized_payment_method
- name: Klarna Initiate Payment Request
  property_count: 15
  slug: ecommerce-api-klarnapaymentinitiationrequest
- name: Klarna Initiate Payment Result
  property_count: 21
  slug: ecommerce-api-klarnapaymentinitiationresponse
- name: Language
  property_count: 0
  slug: ecommerce-api-language
- name: Ecommerce basket line items
  property_count: 12
  slug: ecommerce-api-lineitem
- name: Detailed Amount
  property_count: 5
  slug: ecommerce-api-listdetailedamount
- name: Locale
  property_count: 3
  slug: ecommerce-api-locale
- name: MobilePay Payment Initiation Request
  property_count: 16
  slug: ecommerce-api-mobilepaypaymentinitiationrequest
- name: MobilePay Payment Initiation Response
  property_count: 19
  slug: ecommerce-api-mobilepaypaymentinitiationresponse
- name: MultipleCapturesDto
  property_count: 3
  slug: ecommerce-api-multiplecapturesdto
- name: NotFoundV2Docs
  property_count: 5
  slug: ecommerce-api-notfoundv2docs
- name: OP Online Payment list of Banks Response
  property_count: 0
  slug: ecommerce-api-oponlinepaymentgetbanksresponse
- name: OP Online Payment Initiation Request
  property_count: 16
  slug: ecommerce-api-oponlinepaymentinitiationrequest
- name: OP Online Payment Payment Initiation Response
  property_count: 15
  slug: ecommerce-api-oponlinepaymentinitiationresponse
- name: PatchDto
  property_count: 9
  slug: ecommerce-api-patchdto
- name: PatchTokenResponse
  property_count: 14
  slug: ecommerce-api-patchtokenresponse
- name: PaymentFrequency
  property_count: 2
  slug: ecommerce-api-paymentfrequency
- name: Instalment payment plan option
  property_count: 7
  slug: ecommerce-api-paymentplanoption
- name: Payment Product Type
  property_count: 0
  slug: ecommerce-api-paymentproducttype
- name: ProcessingModelDetailsDto
  property_count: 8
  slug: ecommerce-api-processingmodeldetailsdto
- name: Promo Financing
  property_count: 3
  slug: ecommerce-api-promofinancingdetails
- name: Promo Financing Results
  property_count: 7
  slug: ecommerce-api-promofinancingresults
- name: PutDto
  property_count: 8
  slug: ecommerce-api-putdto
- name: RefundCardTransactionDto
  property_count: 7
  slug: ecommerce-api-refundcardtransactiondto
- name: Refusal Reason
  property_count: 0
  slug: ecommerce-api-refusalreason
- name: ReleasePreauthDto
  property_count: 1
  slug: ecommerce-api-releasepreauthdto
- name: SchemeToken
  property_count: 5
  slug: ecommerce-api-schemetoken
- name: settlementDate
  property_count: 0
  slug: ecommerce-api-settlementdate
- name: ShippingInformation
  property_count: 9
  slug: ecommerce-api-shippinginformation
- name: Shipping Address
  property_count: 9
  slug: ecommerce-api-shippinginformationdto
- name: StoredCredential
  property_count: 5
  slug: ecommerce-api-storedcredential
- name: StoredCredentialDto
  property_count: 4
  slug: ecommerce-api-storedcredentialdto
- name: Swish Payment Initiation Request
  property_count: 11
  slug: ecommerce-api-swishpaymentinitiationrequest
- name: Swish Payment Initiation Response
  property_count: 19
  slug: ecommerce-api-swishpaymentinitiationresponse
- name: ThreedAuthentication
  property_count: 8
  slug: ecommerce-api-threedauthentication
- name: ThreedAuthenticationDto
  property_count: 14
  slug: ecommerce-api-threedauthenticationdto
- name: ThreeDSecure
  property_count: 8
  slug: ecommerce-api-threedsecure
- name: TimeZone
  property_count: 0
  slug: ecommerce-api-timezone
- name: token_context
  property_count: 2
  slug: ecommerce-api-tokencontextdto
- name: TokenDetails
  property_count: 19
  slug: ecommerce-api-tokendetails
- name: TokenDetailsPartial
  property_count: 3
  slug: ecommerce-api-tokendetailspartial
- name: Reuse Token Details
  property_count: 2
  slug: ecommerce-api-tokendetailsrequestbody
- name: TokenPaymentRequest
  property_count: 35
  slug: ecommerce-api-tokenpaymentrequest
- name: TokenPreferenceDto
  property_count: 4
  slug: ecommerce-api-tokenpreferencedto
- name: TokenResponse
  property_count: 21
  slug: ecommerce-api-tokenresponse
- name: Transaction State
  property_count: 0
  slug: ecommerce-api-transactionstate
- name: TransactionType
  property_count: 0
  slug: ecommerce-api-transactiontype
- name: UnauthorizedV2Docs
  property_count: 5
  slug: ecommerce-api-unauthorizedv2docs
- name: Ecommerce basket line items
  property_count: 12
  slug: ecommerce-api-unmatchedlineitem
- name: unmatchedRefundBaseRequest
  property_count: 16
  slug: ecommerce-api-unmatchedrefundbaserequest
- name: Using Encrypted Card
  property_count: 0
  slug: ecommerce-api-unmatchedrefundencryptedcardrequest
- name: Using Reuse Token
  property_count: 0
  slug: ecommerce-api-unmatchedrefundtokenrequest
- name: VerificationAdvice
  property_count: 3
  slug: ecommerce-api-verificationadvice
- name: Vipps Payment Initiation Request
  property_count: 18
  slug: ecommerce-api-vippspaymentinitiationrequest
- name: Vipps Payment Initiation Response
  property_count: 19
  slug: ecommerce-api-vippspaymentinitiationresponse
- name: Account
  property_count: 4
  slug: order-service-api-account
- name: AddressWithoutType
  property_count: 0
  slug: order-service-api-addresswithouttype
- name: AdjustedPriceType
  property_count: 2
  slug: order-service-api-adjustedpricetype
- name: AltVfiEntityId
  property_count: 0
  slug: order-service-api-altvfientityid
- name: AltVfiPoiId
  property_count: 0
  slug: order-service-api-altvfipoiid
- name: Amount Simple Type
  property_count: 0
  slug: order-service-api-amountsimple
- name: BaseAddress
  property_count: 10
  slug: order-service-api-baseaddress
- name: BaseAddressWithoutType
  property_count: 5
  slug: order-service-api-baseaddresswithouttype
- name: BaseMerchant
  property_count: 19
  slug: order-service-api-basemerchant
- name: BaseOrderData
  property_count: 7
  slug: order-service-api-baseorderdata
- name: Point of Interaction
  property_count: 19
  slug: order-service-api-basepoitype
- name: BaseProcessorParameters
  property_count: 2
  slug: order-service-api-baseprocessorparameters
- name: Payment Parameters - Regional specific options
  property_count: 1
  slug: order-service-api-baseregionalparameters
- name: BatchDetails
  property_count: 0
  slug: order-service-api-batchdetails
- name: BatchDetailsUpdatable
  property_count: 3
  slug: order-service-api-batchdetailsupdatable
- name: BatchId
  property_count: 0
  slug: order-service-api-batchid
- name: BatchLineItem
  property_count: 10
  slug: order-service-api-batchlineitem
- name: BatchSearchResponse
  property_count: 2
  slug: order-service-api-batchsearchresponse
- name: BatchStatus
  property_count: 0
  slug: order-service-api-batchstatus
- name: Bank Identifier Code
  property_count: 0
  slug: order-service-api-bicidentifier
- name: BundleAndPrice
  property_count: 2
  slug: order-service-api-bundleandprice
- name: BundleAndPriceAndData
  property_count: 3
  slug: order-service-api-bundleandpriceanddata
- name: BundleAndSerialNumberAndQuantity
  property_count: 4
  slug: order-service-api-bundleandserialnumberandquantity
- name: BusinessTitle
  property_count: 0
  slug: order-service-api-businesstitle
- name: CancelAdditionalReason
  property_count: 0
  slug: order-service-api-canceladditionalreason
- name: CancelReasonEnum
  property_count: 0
  slug: order-service-api-cancelreasonenum
- name: CardProductSurcharge
  property_count: 8
  slug: order-service-api-cardproductsurcharge
- name: ContactAddressType
  property_count: 11
  slug: order-service-api-contactaddresstype
- name: ContactName
  property_count: 0
  slug: order-service-api-contactname
- name: ContactType
  property_count: 5
  slug: order-service-api-contacttype
- name: Contact Type
  property_count: 0
  slug: order-service-api-contacttypeenum
- name: ContentTypeEnum
  property_count: 0
  slug: order-service-api-contenttypeenum
- name: ContractContactType
  property_count: 9
  slug: order-service-api-contractcontacttype
- name: Country Code
  property_count: 0
  slug: order-service-api-countrycode3enum
- name: CreatedUserId
  property_count: 0
  slug: order-service-api-createduserid
- name: Currency Code
  property_count: 0
  slug: order-service-api-currencycodeenum
- name: CustomerOrderLink
  property_count: 8
  slug: order-service-api-customerorderlink
- name: CutoverTime
  property_count: 0
  slug: order-service-api-cutovertime
- name: Day of the Week
  property_count: 0
  slug: order-service-api-dayofweekenum
- name: DetailedStatusEnum
  property_count: 0
  slug: order-service-api-detailedstatusenum
- name: DocumentStatusEnum
  property_count: 0
  slug: order-service-api-documentstatusenum
- name: Domestic Bank Account
  property_count: 0
  slug: order-service-api-domesticaccount
- name: DomesticSettlementAccount
  property_count: 0
  slug: order-service-api-domesticsettlementaccount
- name: Email Address
  property_count: 0
  slug: order-service-api-emailaddress
- name: Opening Hours
  property_count: 2
  slug: order-service-api-entityopeninghours
- name: Opening Period
  property_count: 2
  slug: order-service-api-entityopeningperiod
- name: EntityUid
  property_count: 0
  slug: order-service-api-entityuid
- name: EntityUidDeprecated
  property_count: 0
  slug: order-service-api-entityuiddeprecated
- name: Error
  property_count: 1
  slug: order-service-api-errorresp
- name: ExtendedDetails
  property_count: 5
  slug: order-service-api-extendeddetails
- name: ExternalOnboarding
  property_count: 3
  slug: order-service-api-externalonboarding
- name: HardwareMerchant
  property_count: 12
  slug: order-service-api-hardwaremerchant
- name: HardwareOrder
  property_count: 0
  slug: order-service-api-hardwareorder
- name: HardwareOrderData
  property_count: 7
  slug: order-service-api-hardwareorderdata
- name: HardwareOrderResponse
  property_count: 0
  slug: order-service-api-hardwareorderresponse
- name: Point of Interaction
  property_count: 2
  slug: order-service-api-hardwarepoitype
- name: HTTP 400 Error
  property_count: 0
  slug: order-service-api-httperror400
- name: HTTP 401 Error
  property_count: 0
  slug: order-service-api-httperror401
- name: HTTP 403 Error
  property_count: 0
  slug: order-service-api-httperror403
- name: HTTP 404 Error
  property_count: 0
  slug: order-service-api-httperror404
- name: HTTP 429 Error
  property_count: 0
  slug: order-service-api-httperror429
- name: HTTP 500 Error
  property_count: 0
  slug: order-service-api-httperror500
- name: HTTP 503 Error
  property_count: 0
  slug: order-service-api-httperror503
- name: HTTP 504 Error
  property_count: 0
  slug: order-service-api-httperror504
- name: IBAN
  property_count: 0
  slug: order-service-api-ibanidentifier
- name: Industry Type
  property_count: 0
  slug: order-service-api-industry
- name: InternalAllocatedInformation
  property_count: 15
  slug: order-service-api-internalallocatedinformation
- name: InternalAllocatedInformationNewCompanyAndSite
  property_count: 0
  slug: order-service-api-internalallocatedinformationnewcompanyandsite
- name: IpAddressv4v6
  property_count: 0
  slug: order-service-api-ipaddressv4v6
- name: LastChangeTime
  property_count: 0
  slug: order-service-api-lastchangetime
- name: MCC
  property_count: 0
  slug: order-service-api-mcc
- name: MerchantCompanyEntityUid
  property_count: 0
  slug: order-service-api-merchantcompanyentityuid
- name: MerchantContract
  property_count: 10
  slug: order-service-api-merchantcontract
- name: MerchantDocument
  property_count: 0
  slug: order-service-api-merchantdocument
- name: MerchantName
  property_count: 0
  slug: order-service-api-merchantname
- name: MerchantNameWrapper
  property_count: 1
  slug: order-service-api-merchantnamewrapper
- name: MerchantOrder
  property_count: 0
  slug: order-service-api-merchantorder
- name: MerchantOrderResponse
  property_count: 0
  slug: order-service-api-merchantorderresponse
- name: Name Details
  property_count: 6
  slug: order-service-api-name
- name: Notification
  property_count: 3
  slug: order-service-api-notification
- name: NotificationReminder
  property_count: 4
  slug: order-service-api-notificationreminder
- name: NotificationReminders
  property_count: 3
  slug: order-service-api-notificationreminders
- name: OrderCancellation
  property_count: 5
  slug: order-service-api-ordercancellation
- name: OrderId
  property_count: 0
  slug: order-service-api-orderid
- name: OrderReference
  property_count: 0
  slug: order-service-api-orderreference
- name: OrderStats
  property_count: 2
  slug: order-service-api-orderstats
- name: OrderStatusEnum
  property_count: 0
  slug: order-service-api-orderstatusenum
- name: OrderType
  property_count: 0
  slug: order-service-api-ordertype
- name: PackageBundleId
  property_count: 0
  slug: order-service-api-packagebundleid
- name: PackageDetails
  property_count: 4
  slug: order-service-api-packagedetails
- name: Paging Metadata Details
  property_count: 4
  slug: order-service-api-pagingmetadata
- name: PagingPageNumber
  property_count: 0
  slug: order-service-api-pagingpagenumber
- name: PagingPageSize
  property_count: 0
  slug: order-service-api-pagingpagesize
- name: PagingTotalItems
  property_count: 0
  slug: order-service-api-pagingtotalitems
- name: PagingTotalPages
  property_count: 0
  slug: order-service-api-pagingtotalpages
- name: Base Parameters
  property_count: 79
  slug: order-service-api-paymentappparameters
- name: PaymentDetails
  property_count: 1
  slug: order-service-api-paymentdetails
- name: Payment Type
  property_count: 0
  slug: order-service-api-paymenttypeenum
- name: Phone number
  property_count: 5
  slug: order-service-api-phone
- name: Phone Type
  property_count: 0
  slug: order-service-api-phonetypeenum
- name: PoiLaneInformation
  property_count: 3
  slug: order-service-api-poilaneinformation
- name: PoiNetworkConfig
  property_count: 9
  slug: order-service-api-poinetworkconfig
- name: PoiOrder
  property_count: 0
  slug: order-service-api-poiorder
- name: PoiOrderResponse
  property_count: 0
  slug: order-service-api-poiorderresponse
- name: PoiStatusEnum
  property_count: 0
  slug: order-service-api-poistatusenum
- name: Point of Interaction Type
  property_count: 0
  slug: order-service-api-poitypeenum
- name: PoiUid
  property_count: 0
  slug: order-service-api-poiuid
- name: PostCode
  property_count: 0
  slug: order-service-api-postcode
- name: Receipt Printing Option
  property_count: 0
  slug: order-service-api-printoptionsenum
- name: Receipt Options
  property_count: 6
  slug: order-service-api-receiptoptions
- name: ReplacedDevice
  property_count: 2
  slug: order-service-api-replaceddevice
- name: ReplacementAgreement
  property_count: 2
  slug: order-service-api-replacementagreement
- name: RequestedDateOfShipment
  property_count: 0
  slug: order-service-api-requesteddateofshipment
- name: RequiredDocument
  property_count: 7
  slug: order-service-api-requireddocument
- name: SEPA Bank Account
  property_count: 0
  slug: order-service-api-sepaaccount
- name: SerialNumber
  property_count: 0
  slug: order-service-api-serialnumber
- name: ServicePackages
  property_count: 5
  slug: order-service-api-servicepackages
- name: SettlementAccount
  property_count: 0
  slug: order-service-api-settlementaccount
- name: SettlementDetails
  property_count: 1
  slug: order-service-api-settlementdetails
- name: SignersInformation
  property_count: 5
  slug: order-service-api-signersinformation
- name: SigningInformation
  property_count: 4
  slug: order-service-api-signinginformation
- name: SiteName
  property_count: 0
  slug: order-service-api-sitename
- name: SiteReferenceId
  property_count: 0
  slug: order-service-api-sitereferenceid
- name: Parameters
  property_count: 4
  slug: order-service-api-terminalparameters
- name: Merchant Identifier
  property_count: 2
  slug: order-service-api-threedsecuremerchantidentifiers
- name: TimeZone
  property_count: 0
  slug: order-service-api-timezone
- name: Tip Options
  property_count: 3
  slug: order-service-api-tipoptions
- name: TransactionLimits
  property_count: 5
  slug: order-service-api-transactionlimits
- name: TransactionOptions
  property_count: 12
  slug: order-service-api-transactionoptions
- name: UserName
  property_count: 0
  slug: order-service-api-username
- name: VariableResponseType
  property_count: 2
  slug: order-service-api-variableresponsetype
- name: VmssApplication
  property_count: 5
  slug: order-service-api-vmssapplication
- name: VmssSchemeMatches
  property_count: 0
  slug: order-service-api-vmssschemematches
- name: VmssSchemeStatus
  property_count: 0
  slug: order-service-api-vmssschemestatus
- name: address
  property_count: 6
  slug: paypal-ecommerce-api-address
- name: allowedCountries
  property_count: 0
  slug: paypal-ecommerce-api-allowedcountries
- name: amount
  property_count: 2
  slug: paypal-ecommerce-api-amount
- name: application_context
  property_count: 8
  slug: paypal-ecommerce-api-application_context
- name: applicationContext
  property_count: 7
  slug: paypal-ecommerce-api-applicationcontext
- name: Auth_Payer_Info
  property_count: 6
  slug: paypal-ecommerce-api-auth_payer_info
- name: billingAddress
  property_count: 6
  slug: paypal-ecommerce-api-billingaddress
- name: billingCycles
  property_count: 0
  slug: paypal-ecommerce-api-billingcycles
- name: billingInfo
  property_count: 7
  slug: paypal-ecommerce-api-billinginfo
- name: billingInfoOutstandingBalance
  property_count: 2
  slug: paypal-ecommerce-api-billinginfooutstandingbalance
- name: Capture_Payer_Info
  property_count: 6
  slug: paypal-ecommerce-api-capture_payer_info
- name: category
  property_count: 2
  slug: paypal-ecommerce-api-category
- name: customer
  property_count: 8
  slug: paypal-ecommerce-api-customer
- name: customId
  property_count: 2
  slug: paypal-ecommerce-api-customid
- name: cycleExecutions
  property_count: 0
  slug: paypal-ecommerce-api-cycleexecutions
- name: description
  property_count: 2
  slug: paypal-ecommerce-api-description
- name: detailedAmount
  property_count: 5
  slug: paypal-ecommerce-api-detailedamount
- name: details
  property_count: 0
  slug: paypal-ecommerce-api-details
- name: discount
  property_count: 2
  slug: paypal-ecommerce-api-discount
- name: fixedPrice
  property_count: 2
  slug: paypal-ecommerce-api-fixedprice
- name: frequency
  property_count: 2
  slug: paypal-ecommerce-api-frequency
- name: handling
  property_count: 2
  slug: paypal-ecommerce-api-handling
- name: homeUrl
  property_count: 2
  slug: paypal-ecommerce-api-homeurl
- name: identification
  property_count: 2
  slug: paypal-ecommerce-api-identification
- name: imageUrl
  property_count: 2
  slug: paypal-ecommerce-api-imageurl
- name: insurance
  property_count: 2
  slug: paypal-ecommerce-api-insurance
- name: items
  property_count: 0
  slug: paypal-ecommerce-api-items
- name: lastFailedPayment
  property_count: 4
  slug: paypal-ecommerce-api-lastfailedpayment
- name: lastPayment
  property_count: 3
  slug: paypal-ecommerce-api-lastpayment
- name: merchant
  property_count: 1
  slug: paypal-ecommerce-api-merchant
- name: merchantPreferences
  property_count: 5
  slug: paypal-ecommerce-api-merchantpreferences
- name: Model1
  property_count: 3
  slug: paypal-ecommerce-api-model1
- name: Model10
  property_count: 9
  slug: paypal-ecommerce-api-model10
- name: Model11
  property_count: 1
  slug: paypal-ecommerce-api-model11
- name: Model12
  property_count: 2
  slug: paypal-ecommerce-api-model12
- name: Model13
  property_count: 6
  slug: paypal-ecommerce-api-model13
- name: Model14
  property_count: 2
  slug: paypal-ecommerce-api-model14
- name: Model15
  property_count: 2
  slug: paypal-ecommerce-api-model15
- name: Model16
  property_count: 14
  slug: paypal-ecommerce-api-model16
- name: Model17
  property_count: 9
  slug: paypal-ecommerce-api-model17
- name: Model18
  property_count: 8
  slug: paypal-ecommerce-api-model18
- name: Model19
  property_count: 2
  slug: paypal-ecommerce-api-model19
- name: Model2
  property_count: 5
  slug: paypal-ecommerce-api-model2
- name: Model20
  property_count: 8
  slug: paypal-ecommerce-api-model20
- name: Model21
  property_count: 12
  slug: paypal-ecommerce-api-model21
- name: Model22
  property_count: 2
  slug: paypal-ecommerce-api-model22
- name: Model24
  property_count: 7
  slug: paypal-ecommerce-api-model24
- name: Model25
  property_count: 2
  slug: paypal-ecommerce-api-model25
- name: Model26
  property_count: 11
  slug: paypal-ecommerce-api-model26
- name: Model28
  property_count: 6
  slug: paypal-ecommerce-api-model28
- name: Model29
  property_count: 2
  slug: paypal-ecommerce-api-model29
- name: Model3
  property_count: 10
  slug: paypal-ecommerce-api-model3
- name: Model30
  property_count: 8
  slug: paypal-ecommerce-api-model30
- name: Model31
  property_count: 6
  slug: paypal-ecommerce-api-model31
- name: Model32
  property_count: 10
  slug: paypal-ecommerce-api-model32
- name: Model33
  property_count: 2
  slug: paypal-ecommerce-api-model33
- name: Model34
  property_count: 5
  slug: paypal-ecommerce-api-model34
- name: Model35
  property_count: 0
  slug: paypal-ecommerce-api-model35
- name: Model36
  property_count: 9
  slug: paypal-ecommerce-api-model36
- name: Model37
  property_count: 11
  slug: paypal-ecommerce-api-model37
- name: Model38
  property_count: 1
  slug: paypal-ecommerce-api-model38
- name: Model39
  property_count: 7
  slug: paypal-ecommerce-api-model39
- name: Model4
  property_count: 3
  slug: paypal-ecommerce-api-model4
- name: Model40
  property_count: 3
  slug: paypal-ecommerce-api-model40
- name: Model41
  property_count: 3
  slug: paypal-ecommerce-api-model41
- name: Model42
  property_count: 2
  slug: paypal-ecommerce-api-model42
- name: Model43
  property_count: 2
  slug: paypal-ecommerce-api-model43
- name: Model44
  property_count: 3
  slug: paypal-ecommerce-api-model44
- name: Model45
  property_count: 1
  slug: paypal-ecommerce-api-model45
- name: Model46
  property_count: 2
  slug: paypal-ecommerce-api-model46
- name: Model47
  property_count: 7
  slug: paypal-ecommerce-api-model47
- name: Model48
  property_count: 2
  slug: paypal-ecommerce-api-model48
- name: Model49
  property_count: 4
  slug: paypal-ecommerce-api-model49
- name: Model5
  property_count: 4
  slug: paypal-ecommerce-api-model5
- name: Model50
  property_count: 7
  slug: paypal-ecommerce-api-model50
- name: Model51
  property_count: 2
  slug: paypal-ecommerce-api-model51
- name: Model52
  property_count: 3
  slug: paypal-ecommerce-api-model52
- name: Model53
  property_count: 5
  slug: paypal-ecommerce-api-model53
- name: Model54
  property_count: 5
  slug: paypal-ecommerce-api-model54
- name: Model55
  property_count: 2
  slug: paypal-ecommerce-api-model55
- name: Model56
  property_count: 3
  slug: paypal-ecommerce-api-model56
- name: Model57
  property_count: 0
  slug: paypal-ecommerce-api-model57
- name: Model58
  property_count: 2
  slug: paypal-ecommerce-api-model58
- name: Model59
  property_count: 12
  slug: paypal-ecommerce-api-model59
- name: Model6
  property_count: 9
  slug: paypal-ecommerce-api-model6
- name: Model60
  property_count: 1
  slug: paypal-ecommerce-api-model60
- name: Model61
  property_count: 4
  slug: paypal-ecommerce-api-model61
- name: Model7
  property_count: 3
  slug: paypal-ecommerce-api-model7
- name: Model8
  property_count: 9
  slug: paypal-ecommerce-api-model8
- name: Model9
  property_count: 11
  slug: paypal-ecommerce-api-model9
- name: name
  property_count: 2
  slug: paypal-ecommerce-api-name
- name: outstandingBalance
  property_count: 2
  slug: paypal-ecommerce-api-outstandingbalance
- name: payeeInfo
  property_count: 1
  slug: paypal-ecommerce-api-payeeinfo
- name: payer
  property_count: 1
  slug: paypal-ecommerce-api-payer
- name: Payer_Name
  property_count: 2
  slug: paypal-ecommerce-api-payer_name
- name: payerInfo
  property_count: 7
  slug: paypal-ecommerce-api-payerinfo
- name: paymentMethod
  property_count: 2
  slug: paypal-ecommerce-api-paymentmethod
- name: paymentPreferences
  property_count: 4
  slug: paypal-ecommerce-api-paymentpreferences
- name: phone
  property_count: 2
  slug: paypal-ecommerce-api-phone
- name: Phone_number
  property_count: 2
  slug: paypal-ecommerce-api-phone_number
- name: phoneNumber
  property_count: 1
  slug: paypal-ecommerce-api-phonenumber
- name: plan
  property_count: 1
  slug: paypal-ecommerce-api-plan
- name: planBillingCyclesPricingSchemeFixedPrice
  property_count: 3
  slug: paypal-ecommerce-api-planbillingcyclespricingschemefixedprice
- name: planBillingCyclesPricingSchemeTiers
  property_count: 3
  slug: paypal-ecommerce-api-planbillingcyclespricingschemetiers
- name: planBillingCyclesTotalCycles
  property_count: 3
  slug: paypal-ecommerce-api-planbillingcyclestotalcycles
- name: planPaymentPreferencesAutoBillOutstanding
  property_count: 2
  slug: paypal-ecommerce-api-planpaymentpreferencesautobilloutstanding
- name: plans
  property_count: 0
  slug: paypal-ecommerce-api-plans
- name: planTaxesInclusive
  property_count: 2
  slug: paypal-ecommerce-api-plantaxesinclusive
- name: planTaxesPercentage
  property_count: 2
  slug: paypal-ecommerce-api-plantaxespercentage
- name: pricingScheme
  property_count: 4
  slug: paypal-ecommerce-api-pricingscheme
- name: products
  property_count: 0
  slug: paypal-ecommerce-api-products
- name: redirectUrls
  property_count: 2
  slug: paypal-ecommerce-api-redirecturls
- name: setupFee
  property_count: 2
  slug: paypal-ecommerce-api-setupfee
- name: Shipping-Address
  property_count: 7
  slug: paypal-ecommerce-api-shipping-address
- name: shipping
  property_count: 2
  slug: paypal-ecommerce-api-shipping
- name: shippingAddress
  property_count: 7
  slug: paypal-ecommerce-api-shippingaddress
- name: shippingAmount
  property_count: 2
  slug: paypal-ecommerce-api-shippingamount
- name: shippingDiscount
  property_count: 2
  slug: paypal-ecommerce-api-shippingdiscount
- name: startTime
  property_count: 2
  slug: paypal-ecommerce-api-starttime
- name: subscriber
  property_count: 5
  slug: paypal-ecommerce-api-subscriber
- name: subscriberShippingAddress
  property_count: 2
  slug: paypal-ecommerce-api-subscribershippingaddress
- name: tax
  property_count: 2
  slug: paypal-ecommerce-api-tax
- name: taxes
  property_count: 2
  slug: paypal-ecommerce-api-taxes
- name: tiers
  property_count: 0
  slug: paypal-ecommerce-api-tiers
- name: unitAmount
  property_count: 2
  slug: paypal-ecommerce-api-unitamount
- name: updateTransaction
  property_count: 8
  slug: paypal-ecommerce-api-updatetransaction
- name: value
  property_count: 2
  slug: paypal-ecommerce-api-value
- name: Banking partner
  property_count: 0
  slug: reporting-api-bankingpartner
- name: HTTP 400 Error
  property_count: 6
  slug: reporting-api-genericerror400
- name: HTTP 401 Error
  property_count: 6
  slug: reporting-api-genericerror401
- name: HTTP 403 Error
  property_count: 6
  slug: reporting-api-genericerror403
- name: HTTP 404 Error
  property_count: 6
  slug: reporting-api-genericerror404
- name: HTTP 429 Error
  property_count: 6
  slug: reporting-api-genericerror429
- name: HTTP 500 Error
  property_count: 6
  slug: reporting-api-genericerror500
- name: HTTP 503 Error
  property_count: 6
  slug: reporting-api-genericerror503
- name: HTTP 504 Error
  property_count: 6
  slug: reporting-api-genericerror504
- name: MimeType
  property_count: 0
  slug: reporting-api-mimetype
- name: Base report details
  property_count: 5
  slug: reporting-api-report
- name: Report Parameters
  property_count: 19
  slug: reporting-api-reportparameters
- name: ReportRecord
  property_count: 0
  slug: reporting-api-reportrecord
- name: ReportsResponse
  property_count: 2
  slug: reporting-api-reportsresponse
- name: Report status enumeration
  property_count: 0
  slug: reporting-api-reportstatusenum
- name: Report type enumeration
  property_count: 0
  slug: reporting-api-reporttypeenum
- name: Report UID
  property_count: 0
  slug: reporting-api-reportuid
jsonld:
- class_count: 8
  name: Apis Context
  property_count: 18
  slug: apis
layout: provider
modified: '2026-06-13'
name: Verifone
nav: Providers
network: true
overview: 'Verifone publishes 22 APIs on the [APIs.io](https://apis.io/) network, including 3DS Authentication API, Batch API, Billing Agreement API, and 19 more. Tagged areas include Payments, POS, Terminal Management, eCommerce, and FinTech.


  The Verifone catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Verifone''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, sandbox, engineering blog, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Verifone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: verifone-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.3
  delta: -5.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.6
    developer_ergonomics: 54.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/verifone/refs/heads/main/screenshots/verifone-2026-06-20T200926.png
security:
- kind: authentication
  name: Verifone Authentication
  slug: verifone-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Verifone Domain Security
  slug: verifone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verifone
tags:
- Payments
- POS
- Terminal Management
- eCommerce
- FinTech
- Payment Processing
- Omnichannel
website: https://docs.verifone.com
---
