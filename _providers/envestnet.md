---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 76
  human_in_the_loop: 2
  name: Envestnet Agentic Access
  operation_count: 150
  slug: envestnet-agentic-access
  summary_line: 150 operations · 76 acting · 2 human-in-the-loop
api_count: 21
apis:
- description: Account verification customers looking to integrate with one of our payment partners can use the Account Token endpoints. These APIs allow creating a secure processor token for your user's verified fi
  name: Envestnet Account Token API
  slug: envestnet-account-token-api
- description: Accounts API
  name: Envestnet Accounts API
  slug: envestnet-accounts-api
- description: The Associated Details API from Envestnet — 2 operation(s) for associated details.
  name: Envestnet Associated Details API
  slug: envestnet-associated-details-api
- description: Auth API
  name: Envestnet Auth API
  slug: envestnet-auth-api
- description: Configs API
  name: Envestnet Configs API
  slug: envestnet-configs-api
- description: Consents API
  name: Envestnet Consents API
  slug: envestnet-consents-api
- description: CreditAcceleratorFile API
  name: Envestnet CreditAcceleratorFile API
  slug: envestnet-creditacceleratorfile-api
- description: The Customer API from Envestnet — 1 operation(s) for customer.
  name: Envestnet Customer API
  slug: envestnet-customer-api
- description: DataExtracts API
  name: Envestnet DataExtracts API
  slug: envestnet-dataextracts-api
- description: Derived API
  name: Envestnet Derived API
  slug: envestnet-derived-api
- description: Documents API
  name: Envestnet Documents API
  slug: envestnet-documents-api
- description: Holdings API
  name: Envestnet Holdings API
  slug: envestnet-holdings-api
- description: Envestnet | Yodlee's payment processor partners can use the Payment Processor endpoints to access verified account details using the <code>processorToken</code> created and shared by mutual customers.
  name: Envestnet Payment Processor API
  slug: envestnet-payment-processor-api
- description: Provider Accounts API
  name: Envestnet ProviderAccounts API
  slug: envestnet-provideraccounts-api
- description: Providers API
  name: Envestnet Providers API
  slug: envestnet-providers-api
- description: Statements API
  name: Envestnet Statements API
  slug: envestnet-statements-api
- description: Transactions API
  name: Envestnet Transactions API
  slug: envestnet-transactions-api
- description: Users API
  name: Envestnet User API
  slug: envestnet-user-api
- description: Verification API
  name: Envestnet Verification API
  slug: envestnet-verification-api
- description: Verify Account API
  name: Envestnet Verify Account API
  slug: envestnet-verify-account-api
- description: The View API from Envestnet — 11 operation(s) for view.
  name: Envestnet View API
  slug: envestnet-view-api
artifact_total: 425
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/envestnet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/envestnet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envestnet-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yodlee
- group: company
  title: ''
  type: Website
  url: https://www.envestnet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.envestnet.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.envestnet.com/resources?type=release
- group: company
  title: ''
  type: Blog
  url: https://developer.envestnet.com/resources?type=blog
- group: other
  title: ''
  type: Events
  url: https://developer.envestnet.com/resources?type=events
- group: operate
  title: ''
  type: Contact
  url: https://developer.envestnet.com/contact-us
- group: company
  title: ''
  type: Press
  url: https://www.envestnet.com/press
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.envestnet.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.envestnet.com/legal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/envestnet/
created: '2023-11-20'
description: Envestnet is an ever-evolving network of data-driven services, products, tools, and technologies designed to enable the Intelligent Financial Life. Our robust financial wellness ecosystem offers solutions for every role in the financial advice industry, including the Yodlee account aggregation, verification, credit, insights, and personalized view APIs.
finops:
- name: Envestnet Finops
  service_category: Financial Data / Open Banking
  slug: envestnet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envestnet.png
json_schemas:
- name: AbstractAddress
  property_count: 7
  slug: envestnet-abstractaddress
- name: AccessTokens
  property_count: 3
  slug: envestnet-accesstokens
- name: Account
  property_count: 108
  slug: envestnet-account
- name: AccountAddress
  property_count: 10
  slug: envestnet-accountaddress
- name: AccountBalanceResponse
  property_count: 1
  slug: envestnet-accountbalanceresponse
- name: AccountDataset
  property_count: 6
  slug: envestnet-accountdataset
- name: AccountDerived
  property_count: 5
  slug: envestnet-accountderived
- name: AccountDetail
  property_count: 2
  slug: envestnet-accountdetail
- name: AccountHistoricalBalancesResponse
  property_count: 1
  slug: envestnet-accounthistoricalbalancesresponse
- name: AccountHistory
  property_count: 2
  slug: envestnet-accounthistory
- name: AccountHolder
  property_count: 4
  slug: envestnet-accountholder
- name: AccountHolderData
  property_count: 4
  slug: envestnet-accountholderdata
- name: AccountInfo
  property_count: 9
  slug: envestnet-accountinfo
- name: AccountLatestBalance
  property_count: 16
  slug: envestnet-accountlatestbalance
- name: AccountProfile
  property_count: 4
  slug: envestnet-accountprofile
- name: AccountProfileDetail
  property_count: 4
  slug: envestnet-accountprofiledetail
- name: AccountResponse
  property_count: 1
  slug: envestnet-accountresponse
- name: AccountToken
  property_count: 2
  slug: envestnet-accounttoken
- name: Address
  property_count: 11
  slug: envestnet-address
- name: AmountRange
  property_count: 3
  slug: envestnet-amountrange
- name: ApiKeyOutput
  property_count: 4
  slug: envestnet-apikeyoutput
- name: ApiKeyRequest
  property_count: 1
  slug: envestnet-apikeyrequest
- name: ApiKeyResponse
  property_count: 1
  slug: envestnet-apikeyresponse
- name: AssetClassification
  property_count: 3
  slug: envestnet-assetclassification
- name: AssetClassificationList
  property_count: 2
  slug: envestnet-assetclassificationlist
- name: AssetDetail
  property_count: 1
  slug: envestnet-assetdetail
- name: Attribute
  property_count: 7
  slug: envestnet-attribute
- name: auth_token_body
  property_count: 2
  slug: envestnet-auth-token-body
- name: AutoRefresh
  property_count: 3
  slug: envestnet-autorefresh
- name: BankAccount
  property_count: 7
  slug: envestnet-bankaccount
- name: BankTransferCode
  property_count: 2
  slug: envestnet-banktransfercode
- name: BasicAccount
  property_count: 9
  slug: envestnet-basicaccount
- name: BasicBenchMark
  property_count: 4
  slug: envestnet-basicbenchmark
- name: BasicCategoryDetail
  property_count: 7
  slug: envestnet-basiccategorydetail
- name: BasicCategoryTypeDetail
  property_count: 6
  slug: envestnet-basiccategorytypedetail
- name: BasicCreditCardUtilization
  property_count: 4
  slug: envestnet-basiccreditcardutilization
- name: BasicHolding
  property_count: 9
  slug: envestnet-basicholding
- name: BasicHoldingLink
  property_count: 3
  slug: envestnet-basicholdinglink
- name: BasicMerchant
  property_count: 3
  slug: envestnet-basicmerchant
- name: BasicMerchantDetail
  property_count: 7
  slug: envestnet-basicmerchantdetail
- name: BasicPeerDetail
  property_count: 3
  slug: envestnet-basicpeerdetail
- name: BasicPredictedEvent
  property_count: 13
  slug: envestnet-basicpredictedevent
- name: BasicPredictedEventLink
  property_count: 3
  slug: envestnet-basicpredictedeventlink
- name: BasicStatement
  property_count: 12
  slug: envestnet-basicstatement
- name: BasicStatementLink
  property_count: 3
  slug: envestnet-basicstatementlink
- name: BasicTransaction
  property_count: 13
  slug: envestnet-basictransaction
- name: BasicTransactionLink
  property_count: 3
  slug: envestnet-basictransactionlink
- name: BasicTrend
  property_count: 13
  slug: envestnet-basictrend
- name: BasicView
  property_count: 6
  slug: envestnet-basicview
- name: BudgetDetail
  property_count: 10
  slug: envestnet-budgetdetail
- name: BudgetInfo
  property_count: 4
  slug: envestnet-budgetinfo
- name: BudgetInfos
  property_count: 2
  slug: envestnet-budgetinfos
- name: BudgetSummary
  property_count: 3
  slug: envestnet-budgetsummary
- name: Capability
  property_count: 2
  slug: envestnet-capability
- name: CardAccount
  property_count: 11
  slug: envestnet-cardaccount
- name: CashFlowDetail
  property_count: 8
  slug: envestnet-cashflowdetail
- name: CashFlowTrend
  property_count: 8
  slug: envestnet-cashflowtrend
- name: CategoryDerived
  property_count: 2
  slug: envestnet-categoryderived
- name: CategoryTrend
  property_count: 10
  slug: envestnet-categorytrend
- name: CategoryTypeDerived
  property_count: 4
  slug: envestnet-categorytypederived
- name: CdrPolicy
  property_count: 2
  slug: envestnet-cdrpolicy
- name: ChangeAPR
  property_count: 3
  slug: envestnet-changeapr
- name: ChangeValue
  property_count: 7
  slug: envestnet-changevalue
- name: ClientCredentialToken
  property_count: 3
  slug: envestnet-clientcredentialtoken
- name: ClientCredentialTokenResponse
  property_count: 1
  slug: envestnet-clientcredentialtokenresponse
- name: ClientTrustedAdvisor
  property_count: 3
  slug: envestnet-clienttrustedadvisor
- name: ClientTrustedAdvisorTxt
  property_count: 1
  slug: envestnet-clienttrustedadvisortxt
- name: ConfigsNotificationEvent
  property_count: 2
  slug: envestnet-configsnotificationevent
- name: ConfigsNotificationResponse
  property_count: 1
  slug: envestnet-configsnotificationresponse
- name: Consent
  property_count: 25
  slug: envestnet-consent
- name: ConsentConfirmation
  property_count: 2
  slug: envestnet-consentconfirmation
- name: ConsentHistory
  property_count: 8
  slug: envestnet-consenthistory
- name: ConsentHistoryCount
  property_count: 1
  slug: envestnet-consenthistorycount
- name: ConsentHistoryCountResponse
  property_count: 1
  slug: envestnet-consenthistorycountresponse
- name: ConsentHistoryResponse
  property_count: 1
  slug: envestnet-consenthistoryresponse
- name: ConsentPreferencesResponse
  property_count: 3
  slug: envestnet-consentpreferencesresponse
- name: ConsentResponse
  property_count: 1
  slug: envestnet-consentresponse
- name: Contact
  property_count: 2
  slug: envestnet-contact
- name: ContainerAttributes
  property_count: 5
  slug: envestnet-containerattributes
- name: Coordinates
  property_count: 2
  slug: envestnet-coordinates
- name: Coverage
  property_count: 5
  slug: envestnet-coverage
- name: CoverageAmount
  property_count: 5
  slug: envestnet-coverageamount
- name: CreateAccountInfo
  property_count: 13
  slug: envestnet-createaccountinfo
- name: CreateAccountRequest
  property_count: 1
  slug: envestnet-createaccountrequest
- name: CreateConfigsNotificationEvent
  property_count: 1
  slug: envestnet-createconfigsnotificationevent
- name: CreateConfigsNotificationEventRequest
  property_count: 1
  slug: envestnet-createconfigsnotificationeventrequest
- name: CreateConsent
  property_count: 24
  slug: envestnet-createconsent
- name: CreateConsentRequest
  property_count: 3
  slug: envestnet-createconsentrequest
- name: CreatedAccountInfo
  property_count: 3
  slug: envestnet-createdaccountinfo
- name: CreatedAccountResponse
  property_count: 1
  slug: envestnet-createdaccountresponse
- name: CreatedConsentResponse
  property_count: 1
  slug: envestnet-createdconsentresponse
- name: CreditAcceleratorAccount
  property_count: 110
  slug: envestnet-creditacceleratoraccount
- name: CreditAcceleratorAccountAddress
  property_count: 11
  slug: envestnet-creditacceleratoraccountaddress
- name: CreditAcceleratorAccountAnalysis
  property_count: 3
  slug: envestnet-creditacceleratoraccountanalysis
- name: CreditAcceleratorAccountAsset
  property_count: 14
  slug: envestnet-creditacceleratoraccountasset
- name: CreditAcceleratorAccountExpense
  property_count: 12
  slug: envestnet-creditacceleratoraccountexpense
- name: CreditAcceleratorAccountHolder
  property_count: 5
  slug: envestnet-creditacceleratoraccountholder
- name: CreditAcceleratorAccountIncome
  property_count: 5
  slug: envestnet-creditacceleratoraccountincome
- name: CreditAcceleratorAccountProfile
  property_count: 4
  slug: envestnet-creditacceleratoraccountprofile
- name: CreditAcceleratorAccountSummary
  property_count: 5
  slug: envestnet-creditacceleratoraccountsummary
- name: CreditAcceleratorAccountVerification
  property_count: 8
  slug: envestnet-creditacceleratoraccountverification
- name: CreditAcceleratorAllAccountAnalysis
  property_count: 3
  slug: envestnet-creditacceleratorallaccountanalysis
- name: CreditAcceleratorAllAccountAsset
  property_count: 15
  slug: envestnet-creditacceleratorallaccountasset
- name: CreditAcceleratorAllAccountBalanceOccurrence
  property_count: 2
  slug: envestnet-creditacceleratorallaccountbalanceoccurrence
- name: CreditAcceleratorAllAccountBalanceSummary
  property_count: 2
  slug: envestnet-creditacceleratorallaccountbalancesummary
- name: CreditAcceleratorAllAccountBalanceTxnSummary
  property_count: 2
  slug: envestnet-creditacceleratorallaccountbalancetxnsummary
- name: CreditAcceleratorAllAccountCashFlow
  property_count: 2
  slug: envestnet-creditacceleratorallaccountcashflow
- name: CreditAcceleratorAllAccountCashFlowAnalysis
  property_count: 37
  slug: envestnet-creditacceleratorallaccountcashflowanalysis
- name: CreditAcceleratorAllAccountExpense
  property_count: 12
  slug: envestnet-creditacceleratorallaccountexpense
- name: CreditAcceleratorAllAccountIncome
  property_count: 6
  slug: envestnet-creditacceleratorallaccountincome
- name: CreditAcceleratorAllAccountInvestmentHoldingSummary
  property_count: 2
  slug: envestnet-creditacceleratorallaccountinvestmentholdingsummary
- name: CreditAcceleratorBalance
  property_count: 3
  slug: envestnet-creditacceleratorbalance
- name: CreditAcceleratorBalanceAnalysis
  property_count: 4
  slug: envestnet-creditacceleratorbalanceanalysis
- name: CreditAcceleratorBalanceOccurrence
  property_count: 2
  slug: envestnet-creditacceleratorbalanceoccurrence
- name: CreditAcceleratorBalanceOccurrenceWithTxn
  property_count: 3
  slug: envestnet-creditacceleratorbalanceoccurrencewithtxn
- name: CreditAcceleratorBalanceSummary
  property_count: 3
  slug: envestnet-creditacceleratorbalancesummary
- name: CreditAcceleratorBankTransferCode
  property_count: 3
  slug: envestnet-creditacceleratorbanktransfercode
- name: CreditAcceleratorCashFlow
  property_count: 2
  slug: envestnet-creditacceleratorcashflow
- name: CreditAcceleratorCashFlowAnalysis
  property_count: 31
  slug: envestnet-creditacceleratorcashflowanalysis
- name: CreditAcceleratorClassification
  property_count: 2
  slug: envestnet-creditacceleratorclassification
- name: CreditAcceleratorClassificationType
  property_count: 3
  slug: envestnet-creditacceleratorclassificationtype
- name: CreditAcceleratorClassificationValue
  property_count: 3
  slug: envestnet-creditacceleratorclassificationvalue
- name: CreditAcceleratorDailyBalance
  property_count: 3
  slug: envestnet-creditacceleratordailybalance
- name: CreditAcceleratorDailyBalanceAnalysis
  property_count: 2
  slug: envestnet-creditacceleratordailybalanceanalysis
- name: CreditAcceleratorDailyBalanceSummary
  property_count: 2
  slug: envestnet-creditacceleratordailybalancesummary
- name: CreditAcceleratorDailySummary
  property_count: 6
  slug: envestnet-creditacceleratordailysummary
- name: CreditAcceleratorData
  property_count: 2
  slug: envestnet-creditacceleratordata
- name: CreditAcceleratorDocument
  property_count: 10
  slug: envestnet-creditacceleratordocument
- name: CreditAcceleratorFile
  property_count: 10
  slug: envestnet-creditacceleratorfile
- name: CreditAcceleratorFileResponse
  property_count: 5
  slug: envestnet-creditacceleratorfileresponse
- name: CreditAcceleratorGenerateRequest
  property_count: 3
  slug: envestnet-creditacceleratorgeneraterequest
- name: CreditAcceleratorHolder
  property_count: 2
  slug: envestnet-creditacceleratorholder
- name: CreditAcceleratorInvestmentHoldingSummary
  property_count: 2
  slug: envestnet-creditacceleratorinvestmentholdingsummary
- name: CreditAcceleratorLowBalanceOccurenceALL
  property_count: 4
  slug: envestnet-creditacceleratorlowbalanceoccurenceall
- name: CreditAcceleratorLowBalanceOccurrence
  property_count: 4
  slug: envestnet-creditacceleratorlowbalanceoccurrence
- name: CreditAcceleratorMerchant
  property_count: 9
  slug: envestnet-creditacceleratormerchant
- name: CreditAcceleratorOccurence
  property_count: 2
  slug: envestnet-creditacceleratoroccurence
- name: CreditAcceleratorPaymentBankTransferCode
  property_count: 3
  slug: envestnet-creditacceleratorpaymentbanktransfercode
- name: CreditAcceleratorPaymentProfile
  property_count: 3
  slug: envestnet-creditacceleratorpaymentprofile
- name: CreditAcceleratorRefreshRequest
  property_count: 1
  slug: envestnet-creditacceleratorrefreshrequest
- name: CreditAcceleratorReportConfig
  property_count: 7
  slug: envestnet-creditacceleratorreportconfig
- name: CreditAcceleratorRequestingFirm
  property_count: 4
  slug: envestnet-creditacceleratorrequestingfirm
- name: CreditAcceleratorSelectedAccount
  property_count: 2
  slug: envestnet-creditacceleratorselectedaccount
- name: CreditAcceleratorStatement
  property_count: 4
  slug: envestnet-creditacceleratorstatement
- name: CreditAcceleratorStatementResponse
  property_count: 5
  slug: envestnet-creditacceleratorstatementresponse
- name: CreditAcceleratorStatusResponse
  property_count: 6
  slug: envestnet-creditacceleratorstatusresponse
- name: CreditAcceleratorSummary
  property_count: 4
  slug: envestnet-creditacceleratorsummary
- name: CreditAcceleratorTransaction
  property_count: 46
  slug: envestnet-creditacceleratortransaction
- name: CreditAcceleratorTxnSummary
  property_count: 2
  slug: envestnet-creditacceleratortxnsummary
- name: CreditAcceleratorUser
  property_count: 4
  slug: envestnet-creditacceleratoruser
- name: CustomDisplayData
  property_count: 5
  slug: envestnet-customdisplaydata
- name: CustomerConfiguration
  property_count: 6
  slug: envestnet-customerconfiguration
- name: CustomerSubscription
  property_count: 1
  slug: envestnet-customersubscription
- name: customerSubscriptions
  property_count: 1
  slug: envestnet-customersubscriptions
- name: DataExtractsAccount
  property_count: 105
  slug: envestnet-dataextractsaccount
- name: DataExtractsEvent
  property_count: 2
  slug: envestnet-dataextractsevent
- name: DataExtractsEventData
  property_count: 4
  slug: envestnet-dataextractseventdata
- name: DataExtractsEventLinks
  property_count: 3
  slug: envestnet-dataextractseventlinks
- name: DataExtractsEventResponse
  property_count: 1
  slug: envestnet-dataextractseventresponse
- name: DataExtractsEventUserData
  property_count: 2
  slug: envestnet-dataextractseventuserdata
- name: DataExtractsHolding
  property_count: 39
  slug: envestnet-dataextractsholding
- name: DataExtractsProviderAccount
  property_count: 14
  slug: envestnet-dataextractsprovideraccount
- name: DataExtractsTransaction
  property_count: 44
  slug: envestnet-dataextractstransaction
- name: DataExtractsUser
  property_count: 1
  slug: envestnet-dataextractsuser
- name: DataExtractsUserData
  property_count: 6
  slug: envestnet-dataextractsuserdata
- name: DataExtractsUserDataResponse
  property_count: 1
  slug: envestnet-dataextractsuserdataresponse
- name: DataHandling
  property_count: 2
  slug: envestnet-datahandling
- name: DateRange
  property_count: 2
  slug: envestnet-daterange
- name: DeletePreference
  property_count: 3
  slug: envestnet-deletepreference
- name: DerivedCategorySummary
  property_count: 6
  slug: envestnet-derivedcategorysummary
- name: DerivedCategorySummaryDetails
  property_count: 3
  slug: envestnet-derivedcategorysummarydetails
- name: DerivedHolding
  property_count: 40
  slug: envestnet-derivedholding
- name: DerivedHoldingsAccount
  property_count: 2
  slug: envestnet-derivedholdingsaccount
- name: DerivedHoldingsLinks
  property_count: 1
  slug: envestnet-derivedholdingslinks
- name: DerivedHoldingsSummary
  property_count: 5
  slug: envestnet-derivedholdingssummary
- name: DerivedHoldingSummaryResponse
  property_count: 2
  slug: envestnet-derivedholdingsummaryresponse
- name: DerivedNetworth
  property_count: 5
  slug: envestnet-derivednetworth
- name: DerivedNetworthHistoricalBalance
  property_count: 6
  slug: envestnet-derivednetworthhistoricalbalance
- name: DerivedNetworthResponse
  property_count: 1
  slug: envestnet-derivednetworthresponse
- name: DerivedTransactionsLinks
  property_count: 1
  slug: envestnet-derivedtransactionslinks
- name: DerivedTransactionsSummary
  property_count: 5
  slug: envestnet-derivedtransactionssummary
- name: DerivedTransactionSummaryResponse
  property_count: 2
  slug: envestnet-derivedtransactionsummaryresponse
- name: Description
  property_count: 4
  slug: envestnet-description
- name: descriptions
  property_count: 3
  slug: envestnet-descriptions
- name: Detail
  property_count: 12
  slug: envestnet-detail
- name: DetailCategory
  property_count: 2
  slug: envestnet-detailcategory
- name: DetailCategoryTrend
  property_count: 11
  slug: envestnet-detailcategorytrend
- name: Document
  property_count: 8
  slug: envestnet-document
- name: DocumentDownload
  property_count: 2
  slug: envestnet-documentdownload
- name: DocumentDownloadResponse
  property_count: 1
  slug: envestnet-documentdownloadresponse
- name: DocumentResponse
  property_count: 1
  slug: envestnet-documentresponse
- name: EligibleDetail
  property_count: 2
  slug: envestnet-eligibledetail
- name: EligibleInsight
  property_count: 2
  slug: envestnet-eligibleinsight
- name: Email
  property_count: 2
  slug: envestnet-email
- name: entityconfig
  property_count: 2
  slug: envestnet-entityconfig
- name: EntityDetail
  property_count: 5
  slug: envestnet-entitydetail
- name: EntityDetailResponse
  property_count: 1
  slug: envestnet-entitydetailresponse
- name: Error
  property_count: 3
  slug: envestnet-error
- name: ErrorInfo
  property_count: 4
  slug: envestnet-errorinfo
- name: EvaluateAccountAddress
  property_count: 10
  slug: envestnet-evaluateaccountaddress
- name: EvaluateAddressRequest
  property_count: 1
  slug: envestnet-evaluateaddressrequest
- name: EvaluateAddressResponse
  property_count: 2
  slug: envestnet-evaluateaddressresponse
- name: feed
  property_count: 30
  slug: envestnet-feed
- name: feeds
  property_count: 1
  slug: envestnet-feeds
- name: feedsCount
  property_count: 1
  slug: envestnet-feedscount
- name: Field
  property_count: 13
  slug: envestnet-field
- name: FieldOperation
  property_count: 3
  slug: envestnet-fieldoperation
- name: FullAccountNumberList
  property_count: 2
  slug: envestnet-fullaccountnumberlist
- name: FullAccountNumbers
  property_count: 2
  slug: envestnet-fullaccountnumbers
- name: Geo
  property_count: 2
  slug: envestnet-geo
- name: GeoData
  property_count: 2
  slug: envestnet-geodata
- name: Geography
  property_count: 2
  slug: envestnet-geography
- name: GeographyWithDataArray
  property_count: 3
  slug: envestnet-geographywithdataarray
- name: HistoricalBalance
  property_count: 5
  slug: envestnet-historicalbalance
- name: HolderProfileResponse
  property_count: 1
  slug: envestnet-holderprofileresponse
- name: Holding
  property_count: 41
  slug: envestnet-holding
- name: HoldingAssetClassificationListResponse
  property_count: 1
  slug: envestnet-holdingassetclassificationlistresponse
- name: HoldingId
  property_count: 1
  slug: envestnet-holdingid
- name: HoldingIdListResponse
  property_count: 1
  slug: envestnet-holdingidlistresponse
- name: HoldingRequest
  property_count: 1
  slug: envestnet-holdingrequest
- name: HoldingRequestInfo
  property_count: 29
  slug: envestnet-holdingrequestinfo
- name: HoldingResponse
  property_count: 1
  slug: envestnet-holdingresponse
- name: HoldingSecuritiesResponse
  property_count: 1
  slug: envestnet-holdingsecuritiesresponse
- name: HoldingTypeListResponse
  property_count: 1
  slug: envestnet-holdingtypelistresponse
- name: Identifier
  property_count: 2
  slug: envestnet-identifier
- name: InsightDetail
  property_count: 4
  slug: envestnet-insightdetail
- name: InsightDetailsResponse
  property_count: 1
  slug: envestnet-insightdetailsresponse
- name: InvestmentAccount
  property_count: 2
  slug: envestnet-investmentaccount
- name: LiabilityDetail
  property_count: 1
  slug: envestnet-liabilitydetail
- name: Link
  property_count: 3
  slug: envestnet-link
- name: Links
  property_count: 3
  slug: envestnet-links
- name: LoanAccount
  property_count: 1
  slug: envestnet-loanaccount
- name: LoanPayoffDetails
  property_count: 3
  slug: envestnet-loanpayoffdetails
- name: LoginForm
  property_count: 9
  slug: envestnet-loginform
- name: Merchant
  property_count: 9
  slug: envestnet-merchant
- name: MerchantAddress
  property_count: 3
  slug: envestnet-merchantaddress
- name: MerchantTrend
  property_count: 9
  slug: envestnet-merchanttrend
- name: Message
  property_count: 1
  slug: envestnet-message
- name: Money
  property_count: 4
  slug: envestnet-money
- name: Name
  property_count: 4
  slug: envestnet-name
- name: NetworthDetail
  property_count: 1
  slug: envestnet-networthdetail
- name: NetWorthTrend
  property_count: 4
  slug: envestnet-networthtrend
- name: NetWorthTrendDetail
  property_count: 4
  slug: envestnet-networthtrenddetail
- name: Option
  property_count: 3
  slug: envestnet-option
- name: PaymentAccount
  property_count: 9
  slug: envestnet-paymentaccount
- name: PaymentAccountBalance
  property_count: 7
  slug: envestnet-paymentaccountbalance
- name: PaymentAccountBalanceResponse
  property_count: 1
  slug: envestnet-paymentaccountbalanceresponse
- name: PaymentAccountHolder
  property_count: 7
  slug: envestnet-paymentaccountholder
- name: PaymentAccountHolderResponse
  property_count: 1
  slug: envestnet-paymentaccountholderresponse
- name: PaymentAccountResponse
  property_count: 1
  slug: envestnet-paymentaccountresponse
- name: PaymentBankTransferCode
  property_count: 2
  slug: envestnet-paymentbanktransfercode
- name: PaymentBankTransferCodeData
  property_count: 2
  slug: envestnet-paymentbanktransfercodedata
- name: PaymentIdentifier
  property_count: 2
  slug: envestnet-paymentidentifier
- name: PaymentProcessorTokenRequest
  property_count: 2
  slug: envestnet-paymentprocessortokenrequest
- name: PaymentProcessorTokenResponse
  property_count: 1
  slug: envestnet-paymentprocessortokenresponse
- name: PaymentProfile
  property_count: 3
  slug: envestnet-paymentprofile
- name: PeerData
  property_count: 8
  slug: envestnet-peerdata
- name: PeerDataAtGeo
  property_count: 2
  slug: envestnet-peerdataatgeo
- name: PeerDataResponse
  property_count: 1
  slug: envestnet-peerdataresponse
- name: peerDetailCategorySummary
  property_count: 3
  slug: envestnet-peerdetailcategorysummary
- name: PeerMerchantSummary
  property_count: 2
  slug: envestnet-peermerchantsummary
- name: PeerSpendingComparison
  property_count: 4
  slug: envestnet-peerspendingcomparison
- name: PhoneNumber
  property_count: 2
  slug: envestnet-phonenumber
- name: PredictedInfo
  property_count: 7
  slug: envestnet-predictedinfo
- name: PredictedInfoDerived
  property_count: 3
  slug: envestnet-predictedinfoderived
- name: Preferences
  property_count: 5
  slug: envestnet-preferences
- name: ProviderAccount
  property_count: 14
  slug: envestnet-provideraccount
- name: ProviderAccountDetail
  property_count: 14
  slug: envestnet-provideraccountdetail
- name: ProviderAccountDetailResponse
  property_count: 1
  slug: envestnet-provideraccountdetailresponse
- name: ProviderAccountPreferences
  property_count: 3
  slug: envestnet-provideraccountpreferences
- name: ProviderAccountPreferencesRequest
  property_count: 1
  slug: envestnet-provideraccountpreferencesrequest
- name: ProviderAccountRefreshRequest
  property_count: 2
  slug: envestnet-provideraccountrefreshrequest
- name: ProviderAccountRequest
  property_count: 6
  slug: envestnet-provideraccountrequest
- name: ProviderAccountResponse
  property_count: 1
  slug: envestnet-provideraccountresponse
- name: ProviderDetail
  property_count: 24
  slug: envestnet-providerdetail
- name: ProviderDetailResponse
  property_count: 1
  slug: envestnet-providerdetailresponse
- name: ProviderResponse
  property_count: 1
  slug: envestnet-providerresponse
- name: Providers
  property_count: 25
  slug: envestnet-providers
- name: ProvidersCount
  property_count: 1
  slug: envestnet-providerscount
- name: ProvidersCountResponse
  property_count: 1
  slug: envestnet-providerscountresponse
- name: ProvidersDataset
  property_count: 2
  slug: envestnet-providersdataset
- name: RealEstateAccount
  property_count: 2
  slug: envestnet-realestateaccount
- name: Recommendation
  property_count: 3
  slug: envestnet-recommendation
- name: RecommendationDateRange
  property_count: 2
  slug: envestnet-recommendationdaterange
- name: RecommendationMetadata
  property_count: 3
  slug: envestnet-recommendationmetadata
- name: RecommendationResponse
  property_count: 1
  slug: envestnet-recommendationresponse
- name: RefreshProviderAccountResponse
  property_count: 1
  slug: envestnet-refreshprovideraccountresponse
- name: Renewal
  property_count: 2
  slug: envestnet-renewal
- name: RenewalConsent
  property_count: 2
  slug: envestnet-renewalconsent
- name: RenewConsentPreferences
  property_count: 2
  slug: envestnet-renewconsentpreferences
- name: RenewConsentRequest
  property_count: 3
  slug: envestnet-renewconsentrequest
- name: RenewConsentResponse
  property_count: 3
  slug: envestnet-renewconsentresponse
- name: RewardBalance
  property_count: 7
  slug: envestnet-rewardbalance
- name: Row
  property_count: 5
  slug: envestnet-row
- name: RuleClause
  property_count: 5
  slug: envestnet-ruleclause
- name: Scope
  property_count: 4
  slug: envestnet-scope
- name: Security
  property_count: 38
  slug: envestnet-security
- name: SecurityHolding
  property_count: 2
  slug: envestnet-securityholding
- name: SegementationParameter
  property_count: 2
  slug: envestnet-segementationparameter
- name: Statement
  property_count: 19
  slug: envestnet-statement
- name: StatementDerived
  property_count: 1
  slug: envestnet-statementderived
- name: StatementResponse
  property_count: 1
  slug: envestnet-statementresponse
- name: StatusLink
  property_count: 3
  slug: envestnet-statuslink
- name: StockExchangeDetail
  property_count: 4
  slug: envestnet-stockexchangedetail
- name: Subscription
  property_count: 7
  slug: envestnet-subscription
- name: subscriptionModel
  property_count: 5
  slug: envestnet-subscriptionmodel
- name: SummaryDetails
  property_count: 8
  slug: envestnet-summarydetails
- name: ThirdParty
  property_count: 2
  slug: envestnet-thirdparty
- name: ThirdPartyADR
  property_count: 2
  slug: envestnet-thirdpartyadr
- name: Threshold
  property_count: 3
  slug: envestnet-threshold
- name: total
  property_count: 1
  slug: envestnet-total
- name: TotalCount
  property_count: 1
  slug: envestnet-totalcount
- name: Transaction
  property_count: 43
  slug: envestnet-transaction
- name: TransactionCategorizationRule
  property_count: 6
  slug: envestnet-transactioncategorizationrule
- name: TransactionCategorizationRuleInfo
  property_count: 4
  slug: envestnet-transactioncategorizationruleinfo
- name: TransactionCategorizationRuleRequest
  property_count: 1
  slug: envestnet-transactioncategorizationrulerequest
- name: TransactionCategorizationRuleResponse
  property_count: 1
  slug: envestnet-transactioncategorizationruleresponse
- name: TransactionCategory
  property_count: 10
  slug: envestnet-transactioncategory
- name: TransactionCategoryRequest
  property_count: 3
  slug: envestnet-transactioncategoryrequest
- name: TransactionCategoryResponse
  property_count: 1
  slug: envestnet-transactioncategoryresponse
- name: TransactionCount
  property_count: 1
  slug: envestnet-transactioncount
- name: TransactionCountResponse
  property_count: 1
  slug: envestnet-transactioncountresponse
- name: TransactionDays
  property_count: 2
  slug: envestnet-transactiondays
- name: TransactionDerived
  property_count: 11
  slug: envestnet-transactionderived
- name: TransactionLink
  property_count: 2
  slug: envestnet-transactionlink
- name: TransactionRequest
  property_count: 1
  slug: envestnet-transactionrequest
- name: TransactionResponse
  property_count: 1
  slug: envestnet-transactionresponse
- name: Transactions
  property_count: 1
  slug: envestnet-transactions
- name: TransactionSummary
  property_count: 7
  slug: envestnet-transactionsummary
- name: TransactionSummaryDetails
  property_count: 9
  slug: envestnet-transactionsummarydetails
- name: TransactionSummaryResponse
  property_count: 1
  slug: envestnet-transactionsummaryresponse
- name: TransactionTotal
  property_count: 1
  slug: envestnet-transactiontotal
- name: TransactionTrend
  property_count: 6
  slug: envestnet-transactiontrend
- name: TransactionSummaryDetails
  property_count: 6
  slug: envestnet-transactiontrenddetails
- name: TransactionTrendResponse
  property_count: 1
  slug: envestnet-transactiontrendresponse
- name: TransactionTrendSummaryLink
  property_count: 2
  slug: envestnet-transactiontrendsummarylink
- name: trigger
  property_count: 3
  slug: envestnet-trigger
- name: Triggers
  property_count: 1
  slug: envestnet-triggers
- name: UpdateAccountInfo
  property_count: 15
  slug: envestnet-updateaccountinfo
- name: UpdateAccountRequest
  property_count: 1
  slug: envestnet-updateaccountrequest
- name: UpdateCategoryRequest
  property_count: 4
  slug: envestnet-updatecategoryrequest
- name: UpdateConfigsNotificationEvent
  property_count: 1
  slug: envestnet-updateconfigsnotificationevent
- name: UpdateConfigsNotificationEventRequest
  property_count: 1
  slug: envestnet-updateconfigsnotificationeventrequest
- name: UpdateConsent
  property_count: 3
  slug: envestnet-updateconsent
- name: UpdateConsentRequest
  property_count: 3
  slug: envestnet-updateconsentrequest
- name: UpdatedConsentResponse
  property_count: 1
  slug: envestnet-updatedconsentresponse
- name: UpdatedProviderAccount
  property_count: 12
  slug: envestnet-updatedprovideraccount
- name: UpdatedProviderAccountResponse
  property_count: 1
  slug: envestnet-updatedprovideraccountresponse
- name: UpdateTransaction
  property_count: 8
  slug: envestnet-updatetransaction
- name: UpdateUserRegistration
  property_count: 7
  slug: envestnet-updateuserregistration
- name: UpdateUserRequest
  property_count: 1
  slug: envestnet-updateuserrequest
- name: UpdateVerification
  property_count: 9
  slug: envestnet-updateverification
- name: UpdateVerificationRequest
  property_count: 1
  slug: envestnet-updateverificationrequest
- name: User
  property_count: 6
  slug: envestnet-user
- name: UserAccessToken
  property_count: 1
  slug: envestnet-useraccesstoken
- name: UserAccessTokensResponse
  property_count: 1
  slug: envestnet-useraccesstokensresponse
- name: UserAddress
  property_count: 7
  slug: envestnet-useraddress
- name: userConfiguration
  property_count: 7
  slug: envestnet-userconfiguration
- name: UserDataTreatment
  property_count: 3
  slug: envestnet-userdatatreatment
- name: UserDetail
  property_count: 9
  slug: envestnet-userdetail
- name: UserDetailResponse
  property_count: 1
  slug: envestnet-userdetailresponse
- name: UserRegistration
  property_count: 7
  slug: envestnet-userregistration
- name: UserRequest
  property_count: 1
  slug: envestnet-userrequest
- name: UserRequestPreferences
  property_count: 4
  slug: envestnet-userrequestpreferences
- name: UserResponse
  property_count: 1
  slug: envestnet-userresponse
- name: UserResponsePreferences
  property_count: 4
  slug: envestnet-userresponsepreferences
- name: UserSession
  property_count: 1
  slug: envestnet-usersession
- name: UserSubscription
  property_count: 2
  slug: envestnet-usersubscription
- name: UserSubscriptions
  property_count: 1
  slug: envestnet-usersubscriptions
- name: Verification
  property_count: 8
  slug: envestnet-verification
- name: VerificationAccount
  property_count: 5
  slug: envestnet-verificationaccount
- name: VerificationBankTransferCode
  property_count: 2
  slug: envestnet-verificationbanktransfercode
- name: VerificationHolder
  property_count: 2
  slug: envestnet-verificationholder
- name: VerificationHolderProfile
  property_count: 6
  slug: envestnet-verificationholderprofile
- name: VerificationRequest
  property_count: 1
  slug: envestnet-verificationrequest
- name: VerificationResponse
  property_count: 1
  slug: envestnet-verificationresponse
- name: VerificationStatus
  property_count: 9
  slug: envestnet-verificationstatus
- name: VerificationStatusResponse
  property_count: 1
  slug: envestnet-verificationstatusresponse
- name: VerificationTransaction
  property_count: 2
  slug: envestnet-verificationtransaction
- name: VerifiedAccount
  property_count: 8
  slug: envestnet-verifiedaccount
- name: VerifiedAccountResponse
  property_count: 5
  slug: envestnet-verifiedaccountresponse
- name: VerifiedAccounts
  property_count: 21
  slug: envestnet-verifiedaccounts
- name: VerifyAccount
  property_count: 2
  slug: envestnet-verifyaccount
- name: VerifyAccountRequest
  property_count: 3
  slug: envestnet-verifyaccountrequest
- name: VerifyAccountResponse
  property_count: 1
  slug: envestnet-verifyaccountresponse
- name: VerifyTransactionCriteria
  property_count: 7
  slug: envestnet-verifytransactioncriteria
- name: View
  property_count: 10
  slug: envestnet-view
- name: ViewCreationResponse
  property_count: 1
  slug: envestnet-viewcreationresponse
- name: ViewDerived
  property_count: 3
  slug: envestnet-viewderived
- name: ViewLink
  property_count: 3
  slug: envestnet-viewlink
- name: ViewResponse
  property_count: 1
  slug: envestnet-viewresponse
- name: ViewRule
  property_count: 8
  slug: envestnet-viewrule
- name: ViewRuleExclude
  property_count: 8
  slug: envestnet-viewruleexclude
- name: ViewRuleInclude
  property_count: 9
  slug: envestnet-viewruleinclude
- name: Views
  property_count: 1
  slug: envestnet-views
- name: YodleeError
  property_count: 3
  slug: envestnet-yodleeerror
json_structures:
- name: Envestnet Structure
  property_count: 0
  slug: envestnet-structure
layout: provider
modified: '2026-05-19'
name: Envestnet
nav: Providers
network: true
overview: 'Envestnet publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Account Token API, Accounts API, Associated Details API, and 18 more. Tagged areas include Financial, Wealth Management, Open Banking, and Account Aggregation.


  The Envestnet catalog on APIs.io includes 1 Spectral governance ruleset.


  Envestnet''s developer surface includes release notes, engineering blog, and 12 more developer resources.'
plans:
- name: Envestnet Plans Pricing
  plan_count: 2
  slug: envestnet-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Envestnet Rate Limits
  slug: envestnet-rate-limits
rules:
- name: Envestnet API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: envestnet-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.1
  delta: -6.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.1
    developer_ergonomics: 10.9
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/envestnet/refs/heads/main/screenshots/envestnet-2026-06-20T180737.png
security:
- kind: domain-security
  name: Envestnet Domain Security
  slug: envestnet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Envestnet Vulnerability Disclosure
  slug: envestnet-vulnerability-disclosure
  summary_line: disclosure policy published
slug: envestnet
tags:
- Financial
- Wealth Management
- Open Banking
- Account Aggregation
website: https://www.envestnet.com/
---
