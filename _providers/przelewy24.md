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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 2
  name: Przelewy24 Agentic Access
  operation_count: 67
  slug: przelewy24-agentic-access
  summary_line: 67 operations · 32 acting · 2 human-in-the-loop
api_count: 13
apis:
- description: The Additional API functionality API from Przelewy24 — 9 operation(s) for additional api functionality.
  name: Przelewy24 Additional API functionality API
  slug: przelewy24-additional-api-functionality-api
- description: Mass Payment Identification System is an easy way for a payer to make a payment to an individual bank account created. For a payer wishing to make a traditional transfer, an individual bank account is
  name: Przelewy24 Additional services Mass Payments Transactions API
  slug: przelewy24-additional-services-mass-payments-transactions-api
- description: The APay API API from Przelewy24 — 1 operation(s) for apay api.
  name: Przelewy24 APay API API
  slug: przelewy24-apay-api-api
- description: The BLIK API API from Przelewy24 — 4 operation(s) for blik api.
  name: Przelewy24 BLIK API API
  slug: przelewy24-blik-api-api
- description: The Card API API from Przelewy24 — 5 operation(s) for card api.
  name: Przelewy24 Card API API
  slug: przelewy24-card-api-api
- description: The Ekspres P24 API API from Przelewy24 — 10 operation(s) for ekspres p24 api.
  name: Przelewy24 Ekspres P24 API API
  slug: przelewy24-ekspres-p24-api-api
- description: The GPay API API from Przelewy24 — 1 operation(s) for gpay api.
  name: Przelewy24 GPay API API
  slug: przelewy24-gpay-api-api
- description: The Marketplace Management API API from Przelewy24 — 5 operation(s) for marketplace management api.
  name: Przelewy24 Marketplace Management API API
  slug: przelewy24-marketplace-management-api-api
- description: The Marketplace Merchant API API from Przelewy24 — 2 operation(s) for marketplace merchant api.
  name: Przelewy24 Marketplace Merchant API API
  slug: przelewy24-marketplace-merchant-api-api
- description: The Marketplace Partner API API from Przelewy24 — 2 operation(s) for marketplace partner api.
  name: Przelewy24 Marketplace Partner API API
  slug: przelewy24-marketplace-partner-api-api
- description: In order to register a recurring transaction, it is necessary to send transaction registration request first to <a href="#tag/Transaction-service-API/paths/~1api~1v1~1transaction~1register/post">/tran
  name: Przelewy24 Recursion (doPayment) API
  slug: przelewy24-recursion-dopayment-api
- description: The Report API API from Przelewy24 — 3 operation(s) for report api.
  name: Przelewy24 Report API API
  slug: przelewy24-report-api-api
- description: The Transaction service API API from Przelewy24 — 2 operation(s) for transaction service api.
  name: Przelewy24 Transaction service API API
  slug: przelewy24-transaction-service-api-api
artifact_total: 435
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/przelewy24-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/przelewy24-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/przelewy24-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.przelewy24.pl/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.przelewy24.pl/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.przelewy24.pl/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.przelewy24.pl/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.przelewy24.pl/en/offer/commissions-and-fees
- group: other
  title: ''
  type: Registration
  url: https://www.przelewy24.pl/en/start-cooperation
- group: operate
  title: ''
  type: Support
  url: https://www.przelewy24.pl/en/help-center/api-technical-support
- group: company
  title: ''
  type: Blog
  url: https://www.przelewy24.pl/en/news
- group: other
  title: ''
  type: PaymentMethods
  url: https://www.przelewy24.pl/en/payment-methods
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.przelewy24.pl/en/partner-program
- group: other
  title: ''
  type: Marketplace
  url: https://www.przelewy24.pl/en/payment-solutions/marketplace
- group: operate
  title: ''
  type: StatusPage
  url: https://status.przelewy24.pl/
created: '2026-06-13'
description: Przelewy24 is Poland's leading online payment gateway, providing REST APIs for bank transfer payments, card processing, BLIK mobile payments, and multi-currency payment processing for e-commerce merchants. With 91% brand recognition among Polish online customers, the platform connects merchants to over 165 Polish banks and supports payment methods including online bank transfers, credit and debit cards, BLIK, Google Pay, digital wallets, and prepaid cards. The API supports PLN and EUR currencies and enables transaction registration, payment verification, refunds, and real-time webhook notifications for payment events.
examples:
- key_count: 2
  name: Additionalproperties_Example
  slug: AdditionalProperties_example
- key_count: 2
  name: Availabilityhoursresponse_Example
  slug: AvailabilityHoursResponse_example
- key_count: 2
  name: Basicresponse_Example
  slug: BasicResponse_example
- key_count: 2
  name: Batchdetails200Responsebody_Example
  slug: BatchDetails200ResponseBody_example
- key_count: 2
  name: Batchdetailserror400Body_Example
  slug: BatchDetailsError400Body_example
- key_count: 2
  name: Batchobject_Example
  slug: BatchObject_example
- key_count: 2
  name: Batch_Example
  slug: Batch_example
- key_count: 2
  name: Blikalias200_Example
  slug: BlikAlias200_example
- key_count: 2
  name: Blikchargebyaliasresponse_Example
  slug: BlikChargeByAliasResponse_example
- key_count: 2
  name: Blikchargebycoderesponse_Example
  slug: BlikChargeByCodeResponse_example
- key_count: 2
  name: Blikoneclick_Example
  slug: BlikOneClick_example
- key_count: 2
  name: Cardchargerequestbody_Example
  slug: CardChargeRequestBody_example
- key_count: 2
  name: Cardnotificationextn_Example
  slug: CardNotificationExtN_example
- key_count: 2
  name: Cardnotificationext_Example
  slug: CardNotificationExt_example
- key_count: 2
  name: Cardpayresponse409_Example
  slug: CardPayResponse409_example
- key_count: 2
  name: Cardpaysuccessresponse_Example
  slug: CardPaySuccessResponse_example
- key_count: 2
  name: Cardpaythreedsecureresponse_Example
  slug: CardPayThreeDSecureResponse_example
- key_count: 2
  name: Cardregisterrequestbody_Example
  slug: CardRegisterRequestBody_example
- key_count: 2
  name: Cartparameters_Example
  slug: CartParameters_example
- key_count: 2
  name: Chargebyalias409_Example
  slug: ChargeByAlias409_example
- key_count: 2
  name: Chargecard3Dssuccessresponse_Example
  slug: ChargeCard3dsSuccessResponse_example
- key_count: 2
  name: Chargecardsuccessresponse_Example
  slug: ChargeCardSuccessResponse_example
- key_count: 2
  name: Databatchdetailsobject_Example
  slug: DataBatchDetailsObject_example
- key_count: 2
  name: Errorcoderesponse_Example
  slug: ErrorCodeResponse_example
- key_count: 2
  name: Generalerrorresponse_Example
  slug: GeneralErrorResponse_example
- key_count: 2
  name: Historyerror400Body_Example
  slug: HistoryError400Body_example
- key_count: 2
  name: Historyresponse200Body_Example
  slug: HistoryResponse200Body_example
- key_count: 2
  name: Inforesponse_Example
  slug: InfoResponse_example
- key_count: 2
  name: Invalidinputdatarefund_Example
  slug: InvalidInputDataRefund_example
- key_count: 2
  name: Invalidinputdata_Example
  slug: InvalidInputData_example
- key_count: 2
  name: Pageinformationobject_Example
  slug: PageInformationObject_example
- key_count: 2
  name: Paymentmethodsresponsemethod_Example
  slug: PaymentMethodsResponseMethod_example
- key_count: 2
  name: Paymentmethodsresponse_Example
  slug: PaymentMethodsResponse_example
- key_count: 2
  name: Recurringparamsin_Example
  slug: RecurringParamsIn_example
- key_count: 2
  name: Recurringparams_Example
  slug: RecurringParams_example
- key_count: 2
  name: Refund500Response_Example
  slug: Refund500Response_example
- key_count: 2
  name: Refundobject_Example
  slug: RefundObject_example
- key_count: 2
  name: Refundrequestarraydatabasic_Example
  slug: RefundRequestArrayDataBasic_example
- key_count: 2
  name: Refund_Example
  slug: Refund_example
- key_count: 2
  name: Refundscollection_Example
  slug: RefundsCollection_example
- key_count: 2
  name: Transaction200Blik_Example
  slug: Transaction200Blik_example
- key_count: 2
  name: Transactionbysessionidresponse_Example
  slug: TransactionBySessionIdResponse_example
- key_count: 2
  name: Transactionbysessionidsuccessresponse_Example
  slug: TransactionBySessionIdSuccessResponse_example
- key_count: 2
  name: Transactionnotfoundresponse_Example
  slug: TransactionNotFoundResponse_example
- key_count: 2
  name: Transactionobject_Example
  slug: TransactionObject_example
- key_count: 2
  name: Transactionrefund201Item_Example
  slug: TransactionRefund201Item_example
- key_count: 2
  name: Transactionrefund201_Example
  slug: TransactionRefund201_example
- key_count: 2
  name: Transactionrefund409Item_Example
  slug: TransactionRefund409Item_example
- key_count: 2
  name: Transactionrefund409_Example
  slug: TransactionRefund409_example
- key_count: 2
  name: Transactionrefundjsonrequestbody_Example
  slug: TransactionRefundJsonRequestBody_example
- key_count: 2
  name: Transactionrefundresult_Example
  slug: TransactionRefundResult_example
- key_count: 2
  name: Transactionrefundsinforesponse_Example
  slug: TransactionRefundsInfoResponse_example
- key_count: 2
  name: Transactionregisterofflinerequest_Example
  slug: TransactionRegisterOfflineRequest_example
- key_count: 2
  name: Transactionregistrationoffline200_Example
  slug: TransactionRegistrationOffline200_example
- key_count: 2
  name: Transactionregistrationoffline409_Example
  slug: TransactionRegistrationOffline409_example
- key_count: 2
  name: Transactionregistrationresponse_Example
  slug: TransactionRegistrationResponse_example
- key_count: 2
  name: Transactionrequestbody1_Example
  slug: TransactionRequestBody1_example
- key_count: 2
  name: Transactionresult_Example
  slug: TransactionResult_example
- key_count: 2
  name: Transactiontestaccess200_Example
  slug: TransactionTestAccess200_example
- key_count: 2
  name: Transactionverificationbody_Example
  slug: TransactionVerificationBody_example
- key_count: 2
  name: Transactionverificationresponse_Example
  slug: TransactionVerificationResponse_example
- key_count: 2
  name: Transactionwithrefundsresponse_Example
  slug: TransactionWithRefundsResponse_example
- key_count: 2
  name: Transaction_Example
  slug: Transaction_example
- key_count: 2
  name: Transtactionsplitpayment_Example
  slug: TranstactionSplitPayment_example
- key_count: 2
  name: Unauthorizedresponse_Example
  slug: UnauthorizedResponse_example
- key_count: 2
  name: Validationobject_Example
  slug: ValidationObject_example
- key_count: 2
  name: Alternativekeysitem_Example
  slug: alternativeKeysItem_example
- key_count: 2
  name: Availabilityhours_Example
  slug: availabilityHours_example
- key_count: 2
  name: Blikadnotification_Example
  slug: blikadnotification_example
- key_count: 2
  name: Bliknotification_Example
  slug: bliknotification_example
- key_count: 2
  name: Cardinfores_Example
  slug: cardinfores_example
- key_count: 2
  name: Cardpayjson_Example
  slug: cardpayjson_example
- key_count: 2
  name: Ekspres_Balanceobjectbody_Example
  slug: ekspres_BalanceObjectBody_example
- key_count: 2
  name: Ekspres_Bankavailabilityobjectresponsebody_Example
  slug: ekspres_BankAvailabilityObjectResponseBody_example
- key_count: 2
  name: Ekspres_Generalerrorobjectresponsebody_Example
  slug: ekspres_GeneralErrorObjectResponseBody_example
- key_count: 2
  name: Ekspres_Generalerrorobject_Example
  slug: ekspres_GeneralErrorObject_example
- key_count: 2
  name: Ekspres_Getbankcheck_Example
  slug: ekspres_GetBankCheck_example
- key_count: 2
  name: Ekspres_Historyoutobjectbody_Example
  slug: ekspres_HistoryOutObjectBody_example
- key_count: 2
  name: Ekspres_Notificationtransferstatusbody_Example
  slug: ekspres_NotificationTransferStatusBody_example
- key_count: 2
  name: Ekspres_Paymentmethodobjectresponsebody_Example
  slug: ekspres_PaymentMethodObjectResponseBody_example
- key_count: 2
  name: Ekspres_Personobjectbody_Example
  slug: ekspres_PersonObjectBody_example
- key_count: 2
  name: Ekspres_Posttransferrefundbody_Example
  slug: ekspres_PostTransferRefundBody_example
- key_count: 2
  name: Ekspres_Putpaymentrefundbody_Example
  slug: ekspres_PutPaymentRefundBody_example
- key_count: 2
  name: Ekspres_Putpaymentrefundresponse_Example
  slug: ekspres_PutPaymentRefundResponse_example
- key_count: 2
  name: Ekspres_Transferbasketoutobjectbody_Example
  slug: ekspres_TransferBasketOutObjectBody_example
- key_count: 2
  name: Ekspres_Transferbasketpostbody_Example
  slug: ekspres_TransferBasketPostBody_example
- key_count: 2
  name: Ekspres_Transferbasketresultbody_Example
  slug: ekspres_TransferBasketResultBody_example
- key_count: 2
  name: Ekspres_Transferhistory200Responsebody_Example
  slug: ekspres_TransferHistory200ResponseBody_example
- key_count: 2
  name: Ekspres_Transferobjectbody_Example
  slug: ekspres_TransferObjectBody_example
- key_count: 2
  name: Ekspres_Transferoutobjectbody_Example
  slug: ekspres_TransferOutObjectBody_example
- key_count: 2
  name: Ekspres_Transferp24Refundobject_Example
  slug: ekspres_TransferP24RefundObject_example
- key_count: 2
  name: Ekspres_Transferrequestpostbody_Example
  slug: ekspres_TransferRequestPostBody_example
- key_count: 2
  name: Ekspres_Transferrequestresultobjectbody_Example
  slug: ekspres_TransferRequestResultObjectBody_example
- key_count: 2
  name: Ekspres_Userbalanceresponse200Body_Example
  slug: ekspres_UserBalanceResponse200Body_example
- key_count: 2
  name: Marketplace_403Forbiddengeneralerror_Example
  slug: marketplace_403ForbiddenGeneralError_example
- key_count: 2
  name: Marketplace_500Undefinedgeneralerror_Example
  slug: marketplace_500UndefinedGeneralError_example
- key_count: 2
  name: Marketplace_Affiliatesresponse200_Example
  slug: marketplace_AffiliatesResponse200_example
- key_count: 2
  name: Marketplace_Affiliatesresponse400_Example
  slug: marketplace_AffiliatesResponse400_example
- key_count: 2
  name: Marketplace_Affiliatesresponse404_Example
  slug: marketplace_AffiliatesResponse404_example
- key_count: 2
  name: Marketplace_Apikeyresponse200_Example
  slug: marketplace_ApiKeyResponse200_example
- key_count: 2
  name: Marketplace_Apikeyresponse400_Example
  slug: marketplace_ApiKeyResponse400_example
- key_count: 2
  name: Marketplace_Apikeyresponse404_Example
  slug: marketplace_ApiKeyResponse404_example
- key_count: 2
  name: Marketplace_Arraydetailsdispatchtransaction_Example
  slug: marketplace_ArrayDetailsDispatchTransaction_example
- key_count: 2
  name: Marketplace_Authorizationrequired_Example
  slug: marketplace_AuthorizationRequired_example
- key_count: 2
  name: Marketplace_Crcdataobject_Example
  slug: marketplace_CrcDataObject_example
- key_count: 2
  name: Marketplace_Crcresponse200_Example
  slug: marketplace_CrcResponse200_example
- key_count: 2
  name: Marketplace_Crcresponse400_Example
  slug: marketplace_CrcResponse400_example
- key_count: 2
  name: Marketplace_Crcresponse404_Example
  slug: marketplace_CrcResponse404_example
- key_count: 2
  name: Marketplace_Dataaffarrayobject_Example
  slug: marketplace_DataAffArrayObject_example
- key_count: 2
  name: Marketplace_Dataarrayobjectrefundbody_Example
  slug: marketplace_DataArrayObjectRefundBody_example
- key_count: 2
  name: Marketplace_Datadispatchinfoobject_Example
  slug: marketplace_DataDispatchInfoObject_example
- key_count: 2
  name: Marketplace_Dispatcharrayobject_Example
  slug: marketplace_DispatchArrayObject_example
- key_count: 2
  name: Marketplace_Dispatcherrorobjectbody_Example
  slug: marketplace_DispatchErrorObjectBody_example
- key_count: 2
  name: Marketplace_Dispatchinforesponse200_Example
  slug: marketplace_DispatchInfoResponse200_example
- key_count: 2
  name: Marketplace_Dispatchinforesponse404_Example
  slug: marketplace_DispatchInfoResponse404_example
- key_count: 2
  name: Marketplace_Dispatchresult600Objectarraybody_Example
  slug: marketplace_DispatchResult600ObjectArrayBody_example
- key_count: 2
  name: Marketplace_Dispatchresultobjectarraybody_Example
  slug: marketplace_DispatchResultObjectArrayBody_example
- key_count: 2
  name: Marketplace_Dispatchtransactionbody_Example
  slug: marketplace_DispatchTransactionBody_example
- key_count: 2
  name: Marketplace_Dispatchtransactionresponse200_Example
  slug: marketplace_DispatchTransactionResponse200_example
- key_count: 2
  name: Marketplace_Dispatchtransactionresponse400_Example
  slug: marketplace_DispatchTransactionResponse400_example
- key_count: 2
  name: Marketplace_Errordispatch400Object_Example
  slug: marketplace_ErrorDispatch400Object_example
- key_count: 2
  name: Marketplace_Errorrefundarrayobject_Example
  slug: marketplace_ErrorRefundArrayObject_example
- key_count: 2
  name: Marketplace_Fundsresponse200_Example
  slug: marketplace_FundsResponse200_example
- key_count: 2
  name: Marketplace_Fundsresponse400_Example
  slug: marketplace_FundsResponse400_example
- key_count: 2
  name: Marketplace_Fundsresponse403_Example
  slug: marketplace_FundsResponse403_example
- key_count: 2
  name: Marketplace_Merchanexistsresponse200_Example
  slug: marketplace_MerchanExistsResponse200_example
- key_count: 2
  name: Marketplace_Merchantexistsresponse400_Example
  slug: marketplace_MerchantExistsResponse400_example
- key_count: 2
  name: Marketplace_Merchantexistsresponse404_Example
  slug: marketplace_MerchantExistsResponse404_example
- key_count: 2
  name: Marketplace_Merchantregisterbody_Example
  slug: marketplace_MerchantRegisterBody_example
- key_count: 2
  name: Marketplace_Merchantregisterdataobject_Example
  slug: marketplace_MerchantRegisterDataObject_example
- key_count: 2
  name: Marketplace_Merchantregisterresponse200_Example
  slug: marketplace_MerchantRegisterResponse200_example
- key_count: 2
  name: Marketplace_Merchantregisterresponse201_Example
  slug: marketplace_MerchantRegisterResponse201_example
- key_count: 2
  name: Marketplace_Merchantregisterresponse400_Example
  slug: marketplace_MerchantRegisterResponse400_example
- key_count: 2
  name: Marketplace_Refundarrayobjectbody_Example
  slug: marketplace_RefundArrayObjectBody_example
- key_count: 2
  name: Marketplace_Refundresponse201_Example
  slug: marketplace_RefundResponse201_example
- key_count: 2
  name: Marketplace_Refundresponse400_Example
  slug: marketplace_RefundResponse400_example
- key_count: 2
  name: Marketplace_Refundresponsearrdataobj_Example
  slug: marketplace_RefundResponseArrDataObj_example
- key_count: 2
  name: Marketplace_Refundresponsearrayobject_Example
  slug: marketplace_RefundResponseArrayObject_example
- key_count: 2
  name: Marketplace_Refundrsponse409_Example
  slug: marketplace_RefundRsponse409_example
- key_count: 2
  name: Marketplace_Representativesarray_Example
  slug: marketplace_RepresentativesArray_example
- key_count: 2
  name: Marketplace_Transactionrefundbody_Example
  slug: marketplace_TransactionRefundBody_example
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/przelewy24.png
json_schemas:
- name: 403ForbiddenGeneralError
  property_count: 2
  slug: 403ForbiddenGeneralError
- name: 409ErrorResponse
  property_count: 2
  slug: 409ErrorResponse
- name: 500UndefinedGeneralError
  property_count: 2
  slug: 500UndefinedGeneralError
- name: AdditionalProperties
  property_count: 2
  slug: AdditionalProperties
- name: AffiliatesResponse200
  property_count: 2
  slug: AffiliatesResponse200
- name: AffiliatesResponse400
  property_count: 2
  slug: AffiliatesResponse400
- name: AffiliatesResponse404
  property_count: 2
  slug: AffiliatesResponse404
- name: Alias
  property_count: 0
  slug: Alias
- name: Alternativekey
  property_count: 0
  slug: Alternativekey
- name: ApiKeyResponse200
  property_count: 3
  slug: ApiKeyResponse200
- name: ApiKeyResponse400
  property_count: 2
  slug: ApiKeyResponse400
- name: ApiKeyResponse404
  property_count: 2
  slug: ApiKeyResponse404
- name: ArrayDetailsDispatchTransaction
  property_count: 4
  slug: ArrayDetailsDispatchTransaction
- name: AuthorizationRequired
  property_count: 2
  slug: AuthorizationRequired
- name: AvailabilityHoursResponse
  property_count: 3
  slug: AvailabilityHoursResponse
- name: BalanceObjectBody
  property_count: 2
  slug: BalanceObjectBody
- name: BankAvailabilityObjectResponseBody
  property_count: 5
  slug: BankAvailabilityObjectResponseBody
- name: BasicResponse
  property_count: 2
  slug: BasicResponse
- name: Batch
  property_count: 4
  slug: Batch
- name: BatchDetails200ResponseBody
  property_count: 4
  slug: BatchDetails200ResponseBody
- name: BatchDetailsError400Body
  property_count: 2
  slug: BatchDetailsError400Body
- name: BatchObject
  property_count: 6
  slug: BatchObject
- name: BlikAlias200
  property_count: 4
  slug: BlikAlias200
- name: BlikChargeByAliasResponse
  property_count: 1
  slug: BlikChargeByAliasResponse
- name: BlikChargeByCodeResponse
  property_count: 2
  slug: BlikChargeByCodeResponse
- name: BlikOneClick
  property_count: 5
  slug: BlikOneClick
- name: CardChargeRequestBody
  property_count: 1
  slug: CardChargeRequestBody
- name: CardNotificationExt
  property_count: 14
  slug: CardNotificationExt
- name: CardNotificationExtN
  property_count: 8
  slug: CardNotificationExtN
- name: CardPayResponse409
  property_count: 2
  slug: CardPayResponse409
- name: CardPaySuccessResponse
  property_count: 2
  slug: CardPaySuccessResponse
- name: CardPayThreeDSecureResponse
  property_count: 2
  slug: CardPayThreeDSecureResponse
- name: CardPaymentNegativeNotification
  property_count: 6
  slug: CardPaymentNegativeNotification
- name: CardPaymentNegativeNotificationResult
  property_count: 5
  slug: CardPaymentNegativeNotificationResult
- name: CardPaymentPositiveNotification
  property_count: 7
  slug: CardPaymentPositiveNotification
- name: CardPaymentPositiveNotificationCardInfoData
  property_count: 9
  slug: CardPaymentPositiveNotificationCardInfoData
- name: CardPaymentPositiveNotificationResult
  property_count: 3
  slug: CardPaymentPositiveNotificationResult
- name: CardPaymentPositiveNotificationSecurity
  property_count: 7
  slug: CardPaymentPositiveNotificationSecurity
- name: CardRegisterRequestBody
  property_count: 5
  slug: CardRegisterRequestBody
- name: CartParameters
  property_count: 7
  slug: CartParameters
- name: ChargeByAlias409
  property_count: 2
  slug: ChargeByAlias409
- name: ChargeCard3dsSuccessResponse
  property_count: 2
  slug: ChargeCard3dsSuccessResponse
- name: ChargeCardSuccessResponse
  property_count: 2
  slug: ChargeCardSuccessResponse
- name: CrcDataObject
  property_count: 2
  slug: CrcDataObject
- name: CrcResponse200
  property_count: 2
  slug: CrcResponse200
- name: CrcResponse400
  property_count: 2
  slug: CrcResponse400
- name: CrcResponse404
  property_count: 2
  slug: CrcResponse404
- name: DataAffArrayObject
  property_count: 6
  slug: DataAffArrayObject
- name: DataArrayObjectRefundBody
  property_count: 2
  slug: DataArrayObjectRefundBody
- name: DataBatchDetailsObject
  property_count: 3
  slug: DataBatchDetailsObject
- name: DataDispatchInfoObject
  property_count: 2
  slug: DataDispatchInfoObject
- name: DispatchArrayObject
  property_count: 5
  slug: DispatchArrayObject
- name: DispatchErrorObjectBody
  property_count: 2
  slug: DispatchErrorObjectBody
- name: DispatchInfoResponse200
  property_count: 2
  slug: DispatchInfoResponse200
- name: DispatchInfoResponse404
  property_count: 2
  slug: DispatchInfoResponse404
- name: DispatchResult600ObjectArrayBody
  property_count: 6
  slug: DispatchResult600ObjectArrayBody
- name: DispatchResultObjectArrayBody
  property_count: 7
  slug: DispatchResultObjectArrayBody
- name: DispatchTransactionBody
  property_count: 2
  slug: DispatchTransactionBody
- name: DispatchTransactionResponse200
  property_count: 2
  slug: DispatchTransactionResponse200
- name: DispatchTransactionResponse400
  property_count: 2
  slug: DispatchTransactionResponse400
- name: ErrorCodeResponse
  property_count: 2
  slug: ErrorCodeResponse
- name: ErrorDispatch400Object
  property_count: 2
  slug: ErrorDispatch400Object
- name: ErrorRefundArrayObject
  property_count: 6
  slug: ErrorRefundArrayObject
- name: FundsResponse200
  property_count: 2
  slug: FundsResponse200
- name: FundsResponse400
  property_count: 2
  slug: FundsResponse400
- name: FundsResponse403
  property_count: 2
  slug: FundsResponse403
- name: GeneralErrorObject
  property_count: 2
  slug: GeneralErrorObject
- name: GeneralErrorObjectResponseBody
  property_count: 1
  slug: GeneralErrorObjectResponseBody
- name: GeneralErrorResponse
  property_count: 2
  slug: GeneralErrorResponse
- name: GetBankCheck
  property_count: 1
  slug: GetBankCheck
- name: HistoryDataObject
  property_count: 0
  slug: HistoryDataObject
- name: HistoryError400Body
  property_count: 3
  slug: HistoryError400Body
- name: HistoryOutObjectBody
  property_count: 9
  slug: HistoryOutObjectBody
- name: HistoryResponse200Body
  property_count: 4
  slug: HistoryResponse200Body
- name: InfoResponse
  property_count: 2
  slug: InfoResponse
- name: InvalidInputData
  property_count: 2
  slug: InvalidInputData
- name: InvalidInputDataRefund
  property_count: 2
  slug: InvalidInputDataRefund
- name: IssueWithdrawalRequestBody
  property_count: 3
  slug: IssueWithdrawalRequestBody
- name: MerchanExistsResponse200
  property_count: 2
  slug: MerchanExistsResponse200
- name: MerchantExistsResponse400
  property_count: 2
  slug: MerchantExistsResponse400
- name: MerchantExistsResponse404
  property_count: 2
  slug: MerchantExistsResponse404
- name: MerchantRegisterBody
  property_count: 29
  slug: MerchantRegisterBody
- name: MerchantRegisterDataObject
  property_count: 2
  slug: MerchantRegisterDataObject
- name: MerchantRegisterResponse200
  property_count: 3
  slug: MerchantRegisterResponse200
- name: MerchantRegisterResponse201
  property_count: 3
  slug: MerchantRegisterResponse201
- name: MerchantRegisterResponse400
  property_count: 3
  slug: MerchantRegisterResponse400
- name: NetworkTokenNotification
  property_count: 6
  slug: NetworkTokenNotification
- name: NetworkTokenNotificationCard
  property_count: 3
  slug: NetworkTokenNotificationCard
- name: NetworkTokenNotificationCardArt
  property_count: 3
  slug: NetworkTokenNotificationCardArt
- name: NetworkTokenNotificationCardExpireDate
  property_count: 2
  slug: NetworkTokenNotificationCardExpireDate
- name: NetworkTokenNotificationCardLogotype
  property_count: 3
  slug: NetworkTokenNotificationCardLogotype
- name: NetworkTokenNotificationTokenExpire
  property_count: 2
  slug: NetworkTokenNotificationTokenExpire
- name: NotificationTransferStatusBody
  property_count: 6
  slug: NotificationTransferStatusBody
- name: OverallObject
  property_count: 0
  slug: OverallObject
- name: PageInformationObject
  property_count: 3
  slug: PageInformationObject
- name: PaymentMethodObjectResponseBody
  property_count: 3
  slug: PaymentMethodObjectResponseBody
- name: PaymentMethodsResponse
  property_count: 7
  slug: PaymentMethodsResponse
- name: PaymentMethodsResponseMethod
  property_count: 9
  slug: PaymentMethodsResponseMethod
- name: PersonObjectBody
  property_count: 6
  slug: PersonObjectBody
- name: PostTransferRefundBody
  property_count: 3
  slug: PostTransferRefundBody
- name: PutPaymentRefundBody
  property_count: 2
  slug: PutPaymentRefundBody
- name: PutPaymentRefundResponse
  property_count: 4
  slug: PutPaymentRefundResponse
- name: RecurringParametersA
  property_count: 0
  slug: RecurringParametersA
- name: RecurringParametersM
  property_count: 0
  slug: RecurringParametersM
- name: RecurringParametersO
  property_count: 0
  slug: RecurringParametersO
- name: RecurringParams
  property_count: 5
  slug: RecurringParams
- name: RecurringParamsIn
  property_count: 8
  slug: RecurringParamsIn
- name: Refund
  property_count: 4
  slug: Refund
- name: Refund500Response
  property_count: 2
  slug: Refund500Response
- name: RefundArrayObjectBody
  property_count: 5
  slug: RefundArrayObjectBody
- name: RefundObject
  property_count: 7
  slug: RefundObject
- name: RefundRequestArrayDataBasic
  property_count: 4
  slug: RefundRequestArrayDataBasic
- name: RefundResponse201
  property_count: 2
  slug: RefundResponse201
- name: RefundResponse400
  property_count: 2
  slug: RefundResponse400
- name: RefundResponseArrDataObj
  property_count: 2
  slug: RefundResponseArrDataObj
- name: RefundResponseArrayObject
  property_count: 7
  slug: RefundResponseArrayObject
- name: RefundRsponse409
  property_count: 2
  slug: RefundRsponse409
- name: RefundsCollection
  property_count: 7
  slug: RefundsCollection
- name: RepresentativesArray
  property_count: 2
  slug: RepresentativesArray
- name: SIMPConflict
  property_count: 2
  slug: SIMPConflict
- name: SIMPGetTransactionBySessionId200
  property_count: 2
  slug: SIMPGetTransactionBySessionId200
- name: SIMPResponse400
  property_count: 2
  slug: SIMPResponse400
- name: SIMPTransactionBySessionIdResponse200
  property_count: 18
  slug: SIMPTransactionBySessionIdResponse200
- name: SIMPTransactionRegistrationResponse
  property_count: 2
  slug: SIMPTransactionRegistrationResponse
- name: Transaction
  property_count: 4
  slug: Transaction
- name: Transaction200Blik
  property_count: 2
  slug: Transaction200Blik
- name: TransactionBySessionIdResponse
  property_count: 18
  slug: TransactionBySessionIdResponse
- name: TransactionBySessionIdSuccessResponse
  property_count: 2
  slug: TransactionBySessionIdSuccessResponse
- name: TransactionNotFoundResponse
  property_count: 2
  slug: TransactionNotFoundResponse
- name: TransactionObject
  property_count: 17
  slug: TransactionObject
- name: TransactionRefund201
  property_count: 2
  slug: TransactionRefund201
- name: TransactionRefund201Item
  property_count: 6
  slug: TransactionRefund201Item
- name: TransactionRefund409
  property_count: 2
  slug: TransactionRefund409
- name: TransactionRefund409Item
  property_count: 6
  slug: TransactionRefund409Item
- name: TransactionRefundBody
  property_count: 4
  slug: TransactionRefundBody
- name: TransactionRefundJsonRequestBody
  property_count: 4
  slug: TransactionRefundJsonRequestBody
- name: TransactionRefundResult
  property_count: 10
  slug: TransactionRefundResult
- name: TransactionRefundsInfoResponse
  property_count: 2
  slug: TransactionRefundsInfoResponse
- name: TransactionRegisterOfflineRequest
  property_count: 1
  slug: TransactionRegisterOfflineRequest
- name: TransactionRegisterTtl
  property_count: 28
  slug: TransactionRegisterTtl
- name: TransactionRegistrationOffline200
  property_count: 2
  slug: TransactionRegistrationOffline200
- name: TransactionRegistrationOffline409
  property_count: 2
  slug: TransactionRegistrationOffline409
- name: TransactionRegistrationResponse
  property_count: 2
  slug: TransactionRegistrationResponse
- name: TransactionRegistrationSIMPBody
  property_count: 33
  slug: TransactionRegistrationSIMPBody
- name: TransactionReject200
  property_count: 2
  slug: TransactionReject200
- name: TransactionRejectJsonRequestBodyV11
  property_count: 3
  slug: TransactionRejectJsonRequestBodyV11
- name: TransactionRequestBody1
  property_count: 30
  slug: TransactionRequestBody1
- name: TransactionResult
  property_count: 10
  slug: TransactionResult
- name: TransactionTestAccess200
  property_count: 2
  slug: TransactionTestAccess200
- name: TransactionVerificationBody
  property_count: 7
  slug: TransactionVerificationBody
- name: TransactionVerificationResponse
  property_count: 2
  slug: TransactionVerificationResponse
- name: TransactionWithRefundsResponse
  property_count: 5
  slug: TransactionWithRefundsResponse
- name: TransferBasketOutObjectBody
  property_count: 3
  slug: TransferBasketOutObjectBody
- name: TransferBasketPostBody
  property_count: 13
  slug: TransferBasketPostBody
- name: TransferBasketResultBody
  property_count: 1
  slug: TransferBasketResultBody
- name: TransferHistory200ResponseBody
  property_count: 1
  slug: TransferHistory200ResponseBody
- name: TransferObjectBody
  property_count: 10
  slug: TransferObjectBody
- name: TransferOutObjectBody
  property_count: 3
  slug: TransferOutObjectBody
- name: TransferP24RefundObject
  property_count: 5
  slug: TransferP24RefundObject
- name: TransferRequestPostBody
  property_count: 13
  slug: TransferRequestPostBody
- name: TransferRequestResultObjectBody
  property_count: 1
  slug: TransferRequestResultObjectBody
- name: TranstactionSplitPayment
  property_count: 27
  slug: TranstactionSplitPayment
- name: UnauthorizedResponse
  property_count: 2
  slug: UnauthorizedResponse
- name: UserBalanceResponse200Body
  property_count: 2
  slug: UserBalanceResponse200Body
- name: ValidationObject
  property_count: 1
  slug: ValidationObject
- name: WithdrawalResponseBody
  property_count: 2
  slug: WithdrawalResponseBody
- name: alternativeKeysItem
  property_count: 2
  slug: alternativeKeysItem
- name: availabilityHours
  property_count: 3
  slug: availabilityHours
- name: blikadnotification
  property_count: 4
  slug: blikadnotification
- name: bliknotification
  property_count: 1
  slug: bliknotification
- name: cardData
  property_count: 2
  slug: cardData
- name: cardinfores
  property_count: 2
  slug: cardinfores
- name: cardpayjson
  property_count: 6
  slug: cardpayjson
- name: clear_new
  property_count: 4
  slug: clear_new
- name: eventFail
  property_count: 1
  slug: eventFail
- name: eventFailData
  property_count: 3
  slug: eventFailData
- name: eventLoading
  property_count: 1
  slug: eventLoading
- name: eventLoadingData
  property_count: 2
  slug: eventLoadingData
- name: eventReady
  property_count: 1
  slug: eventReady
- name: eventReadyData
  property_count: 4
  slug: eventReadyData
- name: eventStart
  property_count: 1
  slug: eventStart
- name: eventStartData
  property_count: 2
  slug: eventStartData
- name: eventSuccess
  property_count: 1
  slug: eventSuccess
- name: eventSuccessData
  property_count: 3
  slug: eventSuccessData
- name: eventSuccessDataData
  property_count: 9
  slug: eventSuccessDataData
- name: extended_AdditionalProperties
  property_count: 2
  slug: extended_AdditionalProperties
- name: extended_Alias
  property_count: 0
  slug: extended_Alias
- name: extended_Alternativekey
  property_count: 0
  slug: extended_Alternativekey
- name: extended_AvailabilityHoursResponse
  property_count: 3
  slug: extended_AvailabilityHoursResponse
- name: extended_BasicResponse
  property_count: 2
  slug: extended_BasicResponse
- name: extended_Batch
  property_count: 4
  slug: extended_Batch
- name: extended_BatchDetails200ResponseBody
  property_count: 4
  slug: extended_BatchDetails200ResponseBody
- name: extended_BatchDetailsError400Body
  property_count: 2
  slug: extended_BatchDetailsError400Body
- name: extended_BatchObject
  property_count: 6
  slug: extended_BatchObject
- name: extended_BlikAlias200
  property_count: 4
  slug: extended_BlikAlias200
- name: extended_BlikChargeByAliasResponse
  property_count: 1
  slug: extended_BlikChargeByAliasResponse
- name: extended_BlikChargeByCodeResponse
  property_count: 2
  slug: extended_BlikChargeByCodeResponse
- name: extended_BlikOneClick
  property_count: 5
  slug: extended_BlikOneClick
- name: extended_CardChargeRequestBody
  property_count: 1
  slug: extended_CardChargeRequestBody
- name: extended_CardNotificationExt
  property_count: 14
  slug: extended_CardNotificationExt
- name: extended_CardNotificationExtN
  property_count: 8
  slug: extended_CardNotificationExtN
- name: extended_CardPayResponse409
  property_count: 2
  slug: extended_CardPayResponse409
- name: extended_CardPaySuccessResponse
  property_count: 2
  slug: extended_CardPaySuccessResponse
- name: extended_CardPayThreeDSecureResponse
  property_count: 2
  slug: extended_CardPayThreeDSecureResponse
- name: extended_CardRegisterRequestBody
  property_count: 5
  slug: extended_CardRegisterRequestBody
- name: extended_CartParameters
  property_count: 7
  slug: extended_CartParameters
- name: extended_ChargeByAlias409
  property_count: 2
  slug: extended_ChargeByAlias409
- name: extended_ChargeCard3dsSuccessResponse
  property_count: 2
  slug: extended_ChargeCard3dsSuccessResponse
- name: extended_ChargeCardSuccessResponse
  property_count: 2
  slug: extended_ChargeCardSuccessResponse
- name: extended_DataBatchDetailsObject
  property_count: 3
  slug: extended_DataBatchDetailsObject
- name: extended_ErrorCodeResponse
  property_count: 2
  slug: extended_ErrorCodeResponse
- name: extended_GeneralErrorResponse
  property_count: 2
  slug: extended_GeneralErrorResponse
- name: extended_HistoryDataObject
  property_count: 0
  slug: extended_HistoryDataObject
- name: extended_HistoryError400Body
  property_count: 3
  slug: extended_HistoryError400Body
- name: extended_HistoryResponse200Body
  property_count: 4
  slug: extended_HistoryResponse200Body
- name: extended_InvalidInputData
  property_count: 2
  slug: extended_InvalidInputData
- name: extended_InvalidInputDataRefund
  property_count: 2
  slug: extended_InvalidInputDataRefund
- name: extended_OverallObject
  property_count: 0
  slug: extended_OverallObject
- name: extended_PageInformationObject
  property_count: 3
  slug: extended_PageInformationObject
- name: extended_PaymentMethodsResponse
  property_count: 7
  slug: extended_PaymentMethodsResponse
- name: extended_PaymentMethodsResponseMethod
  property_count: 9
  slug: extended_PaymentMethodsResponseMethod
- name: extended_RecurringParametersA
  property_count: 0
  slug: extended_RecurringParametersA
- name: extended_RecurringParametersM
  property_count: 0
  slug: extended_RecurringParametersM
- name: extended_RecurringParametersO
  property_count: 0
  slug: extended_RecurringParametersO
- name: extended_RecurringParams
  property_count: 5
  slug: extended_RecurringParams
- name: extended_RecurringParamsIn
  property_count: 8
  slug: extended_RecurringParamsIn
- name: extended_Refund
  property_count: 4
  slug: extended_Refund
- name: extended_Refund500Response
  property_count: 2
  slug: extended_Refund500Response
- name: extended_RefundObject
  property_count: 7
  slug: extended_RefundObject
- name: extended_RefundRequestArrayDataBasic
  property_count: 4
  slug: extended_RefundRequestArrayDataBasic
- name: extended_RefundsCollection
  property_count: 7
  slug: extended_RefundsCollection
- name: extended_Transaction
  property_count: 4
  slug: extended_Transaction
- name: extended_Transaction200Blik
  property_count: 2
  slug: extended_Transaction200Blik
- name: extended_TransactionBySessionIdResponse
  property_count: 18
  slug: extended_TransactionBySessionIdResponse
- name: extended_TransactionBySessionIdSuccessResponse
  property_count: 2
  slug: extended_TransactionBySessionIdSuccessResponse
- name: extended_TransactionNotFoundResponse
  property_count: 2
  slug: extended_TransactionNotFoundResponse
- name: extended_TransactionObject
  property_count: 17
  slug: extended_TransactionObject
- name: extended_TransactionRefund201
  property_count: 2
  slug: extended_TransactionRefund201
- name: extended_TransactionRefund201Item
  property_count: 6
  slug: extended_TransactionRefund201Item
- name: extended_TransactionRefund409
  property_count: 2
  slug: extended_TransactionRefund409
- name: extended_TransactionRefund409Item
  property_count: 6
  slug: extended_TransactionRefund409Item
- name: extended_TransactionRefundJsonRequestBody
  property_count: 4
  slug: extended_TransactionRefundJsonRequestBody
- name: extended_TransactionRefundResult
  property_count: 10
  slug: extended_TransactionRefundResult
- name: extended_TransactionRefundsInfoResponse
  property_count: 2
  slug: extended_TransactionRefundsInfoResponse
- name: extended_TransactionRegisterOfflineRequest
  property_count: 1
  slug: extended_TransactionRegisterOfflineRequest
- name: extended_TransactionRegistrationOffline200
  property_count: 2
  slug: extended_TransactionRegistrationOffline200
- name: extended_TransactionRegistrationOffline409
  property_count: 2
  slug: extended_TransactionRegistrationOffline409
- name: extended_TransactionRegistrationResponse
  property_count: 2
  slug: extended_TransactionRegistrationResponse
- name: extended_TransactionRequestBody1
  property_count: 32
  slug: extended_TransactionRequestBody1
- name: extended_TransactionResult
  property_count: 10
  slug: extended_TransactionResult
- name: extended_TransactionTestAccess200
  property_count: 2
  slug: extended_TransactionTestAccess200
- name: extended_TransactionVerificationBody
  property_count: 7
  slug: extended_TransactionVerificationBody
- name: extended_TransactionVerificationResponse
  property_count: 2
  slug: extended_TransactionVerificationResponse
- name: extended_TransactionWithRefundsResponse
  property_count: 5
  slug: extended_TransactionWithRefundsResponse
- name: extended_TranstactionSplitPayment
  property_count: 27
  slug: extended_TranstactionSplitPayment
- name: extended_UnauthorizedResponse
  property_count: 2
  slug: extended_UnauthorizedResponse
- name: extended_ValidationObject
  property_count: 1
  slug: extended_ValidationObject
- name: extended_alternativeKeysItem
  property_count: 2
  slug: extended_alternativeKeysItem
- name: extended_availabilityHours
  property_count: 3
  slug: extended_availabilityHours
- name: extended_blikadnotification
  property_count: 4
  slug: extended_blikadnotification
- name: extended_bliknotification
  property_count: 1
  slug: extended_bliknotification
- name: extended_cardinfores
  property_count: 2
  slug: extended_cardinfores
- name: extended_cardpayjson
  property_count: 6
  slug: extended_cardpayjson
- name: options
  property_count: 7
  slug: options
- name: other
  property_count: 0
  slug: other
- name: other2
  property_count: 1
  slug: other2
- name: przelewy24
  property_count: 3
  slug: przelewy24
- name: przelewy24_new
  property_count: 4
  slug: przelewy24_new
- name: recurring
  property_count: 1
  slug: recurring
- name: render
  property_count: 3
  slug: render
- name: renderOptions
  property_count: 14
  slug: renderOptions
- name: render_new
  property_count: 3
  slug: render_new
jsonld:
- class_count: 28
  name: context Context
  property_count: 4
  slug: context
- class_count: 0
  name: Provider Context
  property_count: 0
  slug: provider
layout: provider
modified: '2026-06-13'
name: Przelewy24
nav: Providers
network: true
overview: 'Przelewy24 publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Additional API functionality API, Additional services Mass Payments Transactions API, APay API API, and 10 more. Tagged areas include Payments, Payment Gateway, Bank Transfer, BLIK, and Card Payments.


  The Przelewy24 catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Przelewy24''s developer surface includes authentication, documentation, sandbox, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 28
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Przelewy24 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: przelewy24-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.5
  delta: -5.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 15.8
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/przelewy24/refs/heads/main/screenshots/przelewy24-2026-06-20T192230.png
security:
- kind: authentication
  name: Przelewy24 Authentication
  slug: przelewy24-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Przelewy24 Domain Security
  slug: przelewy24-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: przelewy24
tags:
- Payments
- Payment Gateway
- Bank Transfer
- BLIK
- Card Payments
- E-Commerce
- Poland
- Polish
- Multi-Currency
- Fintech
website: https://www.przelewy24.pl/en
---
