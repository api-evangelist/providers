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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 3
  name: Pinwheel Agentic Access
  operation_count: 46
  slug: pinwheel-agentic-access
  summary_line: 46 operations · 13 acting · 3 human-in-the-loop
api_count: 14
apis:
- description: The Accounts API from Pinwheel — 4 operation(s) for accounts.
  name: Pinwheel Accounts API
  slug: pinwheel-accounts-api
- description: The API Keys API from Pinwheel — 3 operation(s) for api keys.
  name: Pinwheel API Keys API
  slug: pinwheel-api-keys-api
- description: The Company Connect API from Pinwheel — 7 operation(s) for company connect.
  name: Pinwheel Company Connect API
  slug: pinwheel-company-connect-api
- description: The Direct Deposit Allocations API from Pinwheel — 1 operation(s) for direct deposit allocations.
  name: Pinwheel Direct Deposit Allocations API
  slug: pinwheel-direct-deposit-allocations-api
- description: The Earnings Stream API from Pinwheel — 1 operation(s) for earnings stream.
  name: Pinwheel Earnings Stream API
  slug: pinwheel-earnings-stream-api
- description: The Employers and Platforms API from Pinwheel — 6 operation(s) for employers and platforms.
  name: Pinwheel Employers and Platforms API
  slug: pinwheel-employers-and-platforms-api
- description: The End Users API from Pinwheel — 4 operation(s) for end users.
  name: Pinwheel End Users API
  slug: pinwheel-end-users-api
- description: The Income and Employment API from Pinwheel — 6 operation(s) for income and employment.
  name: Pinwheel Income and Employment API
  slug: pinwheel-income-and-employment-api
- description: The Jobs API from Pinwheel — 1 operation(s) for jobs.
  name: Pinwheel Jobs API
  slug: pinwheel-jobs-api
- description: The Link Tokens API from Pinwheel — 1 operation(s) for link tokens.
  name: Pinwheel Link Tokens API
  slug: pinwheel-link-tokens-api
- description: The Sandbox API from Pinwheel — 1 operation(s) for sandbox.
  name: Pinwheel Sandbox API
  slug: pinwheel-sandbox-api
- description: The Tax Forms API from Pinwheel — 2 operation(s) for tax forms.
  name: Pinwheel Tax Forms API
  slug: pinwheel-tax-forms-api
- description: The Verification Reports API from Pinwheel — 2 operation(s) for verification reports.
  name: Pinwheel Verification Reports API
  slug: pinwheel-verification-reports-api
- description: The Webhooks API from Pinwheel — 2 operation(s) for webhooks.
  name: Pinwheel Webhooks API
  slug: pinwheel-webhooks-api
artifact_total: 188
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pinwheel Accounts API
  slug: open-pinwheel-accounts-api
- collection_type: open
  name: Pinwheel Accounts API Keys API
  slug: open-pinwheel-api-keys-api
- collection_type: open
  name: Pinwheel Accounts Company Connect API
  slug: open-pinwheel-company-connect-api
- collection_type: open
  name: Pinwheel Accounts Direct Deposit Allocations API
  slug: open-pinwheel-direct-deposit-allocations-api
- collection_type: open
  name: Pinwheel Accounts Earnings Stream API
  slug: open-pinwheel-earnings-stream-api
- collection_type: open
  name: Pinwheel Accounts Employers and Platforms API
  slug: open-pinwheel-employers-and-platforms-api
- collection_type: open
  name: Pinwheel Accounts End Users API
  slug: open-pinwheel-end-users-api
- collection_type: open
  name: Pinwheel Accounts Income and Employment API
  slug: open-pinwheel-income-and-employment-api
- collection_type: open
  name: Pinwheel Accounts Jobs API
  slug: open-pinwheel-jobs-api
- collection_type: open
  name: Pinwheel Accounts Link Tokens API
  slug: open-pinwheel-link-tokens-api
- collection_type: open
  name: Pinwheel Accounts Sandbox API
  slug: open-pinwheel-sandbox-api
- collection_type: open
  name: Pinwheel Accounts Tax Forms API
  slug: open-pinwheel-tax-forms-api
- collection_type: open
  name: Pinwheel Accounts Verification Reports API
  slug: open-pinwheel-verification-reports-api
- collection_type: open
  name: Pinwheel Accounts Webhooks API
  slug: open-pinwheel-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pinwheel-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pinwheel-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinwheel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pinwheel-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pinwheelapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pinwheelapi.com/public/docs/getting-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/underdog-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pinwheelhq/
- group: company
  title: ''
  type: Blog
  url: https://www.pinwheelapi.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pinwheelapi.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pinwheelapistatus.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/PinwheelAPI
- group: commercial
  title: ''
  type: Plans
  url: plans/pinwheel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pinwheel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pinwheel-finops.yml
created: '2026-06-13'
description: Pinwheel is the leading payroll connectivity platform providing a REST API for direct deposit switching, income verification, employment history, and tax form retrieval from 1,800+ payroll providers and 40+ time-and-attendance systems. Financial institutions and fintechs use Pinwheel to activate customer accounts, verify income and employment, automate bill switching, and build primary banking relationships through a single, SOC 2 Type 2 and ISO 27001 certified integration.
examples:
- key_count: 2
  name: Auth_V1_Admin_Token_Post Request
  slug: auth_v1_admin_token_post-request
- key_count: 1
  name: Auth_V1_Admin_Token_Post Response 200
  slug: auth_v1_admin_token_post-response-200
- key_count: 1
  name: Create_Key_V1_Admin_Api_Keys_Post Request
  slug: create_key_v1_admin_api_keys_post-request
- key_count: 1
  name: Create_Key_V1_Admin_Api_Keys_Post Response 200
  slug: create_key_v1_admin_api_keys_post-response-200
- key_count: 1
  name: Get_Account_V1_Accounts__Account_Id__Get Response 200
  slug: get_account_v1_accounts__account_id__get-response-200
- key_count: 2
  name: Get_Direct_Deposit_Allocations_V1_Accounts__Account_Id__Direct_Deposit_Allocations_Get Response 200
  slug: get_direct_deposit_allocations_v1_accounts__account_id__direct_deposit_allocations_get-response-200
- key_count: 2
  name: Get_Earnings_Stream_Payouts_V1_End_Users__End_User_Id__Earnings_Stream_Payouts_Get Response 200
  slug: get_earnings_stream_payouts_v1_end_users__end_user_id__earnings_stream_payouts_get-response-200
- key_count: 1
  name: Get_Employer_V1_Employers__Employer_Id__Get Response 200
  slug: get_employer_v1_employers__employer_id__get-response-200
- key_count: 1
  name: Get_Employers_Lookup_V1_Employers_Lookup_Get Response 200
  slug: get_employers_lookup_v1_employers_lookup_get-response-200
- key_count: 2
  name: Get_Employment_V1_Accounts__Account_Id__Employment_Get Response 200
  slug: get_employment_v1_accounts__account_id__employment_get-response-200
- key_count: 2
  name: Get_End_User_Accounts_V1_End_Users__End_User_Id__Accounts_Get Response 200
  slug: get_end_user_accounts_v1_end_users__end_user_id__accounts_get-response-200
- key_count: 1
  name: Get_End_User_Document_V1_End_Users__End_User_Id__Documents__Document_Id__Get Response 200
  slug: get_end_user_document_v1_end_users__end_user_id__documents__document_id__get-response-200
- key_count: 2
  name: Get_End_User_Documents_V1_End_Users__End_User_Id__Documents_Get Response 200
  slug: get_end_user_documents_v1_end_users__end_user_id__documents_get-response-200
- key_count: 1
  name: Get_End_User_Verification_Reports_Voe_V1_End_Users__End_User_Id__Verification_Reports_Voe_Get Response 200
  slug: get_end_user_verification_reports_voe_v1_end_users__end_user_id__verification_reports_voe_get-response-200
- key_count: 1
  name: Get_End_User_Verification_Reports_Voie_V1_End_Users__End_User_Id__Verification_Reports_Voie_Get Response 200
  slug: get_end_user_verification_reports_voie_v1_end_users__end_user_id__verification_reports_voie_get-response-200
- key_count: 2
  name: Get_Identity_V1_Accounts__Account_Id__Identity_Get Response 200
  slug: get_identity_v1_accounts__account_id__identity_get-response-200
- key_count: 2
  name: Get_Income_V1_Accounts__Account_Id__Income_Get Response 200
  slug: get_income_v1_accounts__account_id__income_get-response-200
- key_count: 2
  name: Get_Jobs_V1_Jobs_Get Response 200
  slug: get_jobs_v1_jobs_get-response-200
- key_count: 1
  name: Get_Paystub_V1_Accounts__Account_Id__Paystubs__Paystub_Id__Get Response 200
  slug: get_paystub_v1_accounts__account_id__paystubs__paystub_id__get-response-200
- key_count: 1
  name: Get_Platform_V1_Platforms__Platform_Id__Get Response 200
  slug: get_platform_v1_platforms__platform_id__get-response-200
- key_count: 1
  name: Get_Tax_Form_V1_Accounts__Account_Id__Tax_Forms__Tax_Form_Id__Get Response 200
  slug: get_tax_form_v1_accounts__account_id__tax_forms__tax_form_id__get-response-200
- key_count: 2
  name: Get_V1_Company_Connections__Company_Connection_Id__Census_Get Response 200
  slug: get_v1_company_connections__company_connection_id__census_get-response-200
- key_count: 2
  name: Get_V1_Company_Connections__Company_Connection_Id__Employments_Get Response 200
  slug: get_v1_company_connections__company_connection_id__employments_get-response-200
- key_count: 1
  name: Get_V1_Company_Connections__Company_Connection_Id__Get Response 200
  slug: get_v1_company_connections__company_connection_id__get-response-200
- key_count: 2
  name: Get_V1_Company_Connections__Company_Connection_Id__Incomes_Get Response 200
  slug: get_v1_company_connections__company_connection_id__incomes_get-response-200
- key_count: 2
  name: Get_V1_Company_Connections__Company_Connection_Id__Paystubs__Employee_External_Id__Get Response 200
  slug: get_v1_company_connections__company_connection_id__paystubs__employee_external_id__get-response-200
- key_count: 2
  name: Get_V1_Employers_Get Response 200
  slug: get_v1_employers_get-response-200
- key_count: 2
  name: Get_V1_Search_Get Response 200
  slug: get_v1_search_get-response-200
- key_count: 2
  name: Get_V1_Webhooks_Get Response 200
  slug: get_v1_webhooks_get-response-200
- key_count: 1
  name: Get_Webhook_By_Id_V1_Webhooks__Webhook_Id__Get Response 200
  slug: get_webhook_by_id_v1_webhooks__webhook_id__get-response-200
- key_count: 2
  name: List_Accounts_V1_Accounts_Get Response 200
  slug: list_accounts_v1_accounts_get-response-200
- key_count: 2
  name: List_Keys_V1_Admin_Api_Keys_Get Response 200
  slug: list_keys_v1_admin_api_keys_get-response-200
- key_count: 2
  name: List_Paystubs_V1_Accounts__Account_Id__Paystubs_Get Response 200
  slug: list_paystubs_v1_accounts__account_id__paystubs_get-response-200
- key_count: 2
  name: List_Platforms_V1_Platforms_Get Response 200
  slug: list_platforms_v1_platforms_get-response-200
- key_count: 2
  name: List_Shifts_V1_Accounts__Account_Id__Shifts_Get Response 200
  slug: list_shifts_v1_accounts__account_id__shifts_get-response-200
- key_count: 2
  name: List_Tax_Forms_V1_Accounts__Account_Id__Tax_Forms_Get Response 200
  slug: list_tax_forms_v1_accounts__account_id__tax_forms_get-response-200
- key_count: 2
  name: List_V1_Company_Connections_Get Response 200
  slug: list_v1_company_connections_get-response-200
- key_count: 0
  name: Patch_Monitoring_Status_V1_Sandbox_Accounts__Account_Id__Patch Request
  slug: patch_monitoring_status_v1_sandbox_accounts__account_id__patch-request
- key_count: 1
  name: Patch_Monitoring_Status_V1_Sandbox_Accounts__Account_Id__Patch Response 200
  slug: patch_monitoring_status_v1_sandbox_accounts__account_id__patch-response-200
- key_count: 5
  name: Post_V1_Company_Connect_Link_Tokens_Post Request
  slug: post_v1_company_connect_link_tokens_post-request
- key_count: 1
  name: Post_V1_Company_Connect_Link_Tokens_Post Response 200
  slug: post_v1_company_connect_link_tokens_post-response-200
- key_count: 1
  name: Post_V1_Company_Connections_Post Request
  slug: post_v1_company_connections_post-request
- key_count: 1
  name: Post_V1_Company_Connections_Post Response 200
  slug: post_v1_company_connections_post-response-200
- key_count: 12
  name: Post_V1_Link_Tokens_Post Request
  slug: post_v1_link_tokens_post-request
- key_count: 1
  name: Post_V1_Link_Tokens_Post Response 200
  slug: post_v1_link_tokens_post-response-200
- key_count: 3
  name: Post_V1_Webhooks_Post Request
  slug: post_v1_webhooks_post-request
- key_count: 1
  name: Post_V1_Webhooks_Post Response 200
  slug: post_v1_webhooks_post-response-200
- key_count: 3
  name: Put_V1_Webhooks__Webhook_Id__Put Request
  slug: put_v1_webhooks__webhook_id__put-request
- key_count: 1
  name: Put_V1_Webhooks__Webhook_Id__Put Response 200
  slug: put_v1_webhooks__webhook_id__put-response-200
- key_count: 1
  name: Revoke_Key_V1_Admin_Api_Keys__Api_Key__Revoke_Post Response 200
  slug: revoke_key_v1_admin_api_keys__api_key__revoke_post-response-200
- key_count: 1
  name: Update_Bill_Navigator_User_Status_V1_End_Users__End_User_Id__Bill_Navigator_Status_Put Request
  slug: update_bill_navigator_user_status_v1_end_users__end_user_id__bill_navigator_status_put-request
finops:
- name: Pinwheel Finops
  service_category: ''
  slug: pinwheel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pinwheel.png
json_schemas:
- name: Address
  property_count: 7
  slug: addressgetresponseitem
- name: Allocation
  property_count: 4
  slug: allocation
- name: Allocation
  property_count: 10
  slug: allocationaccountobjresponse
- name: AnnualIncomeResponseObj
  property_count: 7
  slug: annualincomeresponseobj
- name: ApplicantNameAndAddress
  property_count: 2
  slug: applicantnameandaddress
- name: BankAccount
  property_count: 8
  slug: bankaccount
- name: BankAccountDetails
  property_count: 4
  slug: bankaccountdetails
- name: BankAccountTransaction
  property_count: 5
  slug: bankaccounttransaction
- name: Bill Navigator Status Update Request
  property_count: 2
  slug: billnavigatorstatusupdaterequest
- name: object
  property_count: 10
  slug: carddetails
- name: CompanyConnect
  property_count: 1
  slug: companyconnect
- name: CompanyConnectionBase
  property_count: 5
  slug: companyconnectionbase
- name: CompanyConnectionPostBody
  property_count: 1
  slug: companyconnectioncreate
- name: LinkTokenPostBody
  property_count: 6
  slug: companyconnectlinktokencreate
- name: CompanyConnect Link Token Response Data
  property_count: 4
  slug: companyconnectlinktokenobjresponse
- name: CompanyEmploymentObjResponse
  property_count: 12
  slug: companyemploymentobjresponse
- name: CompanyIdentityObjResponse
  property_count: 11
  slug: companyidentityobjresponse
- name: CompanyIncomeObjResponse
  property_count: 6
  slug: companyincomeobjresponse
- name: CompanyPaystubObjResponse
  property_count: 15
  slug: companypaystubobjresponse
- name: object
  property_count: 2
  slug: createadmintokenrequest
- name: CreateAdminTokenResponse
  property_count: 1
  slug: createadmintokenresponse
- name: object
  property_count: 5
  slug: createadmintokenresponsedata
- name: object
  property_count: 1
  slug: createapikeyoptions
- name: CreateAPIKeyResponse
  property_count: 1
  slug: createapikeyresponse
- name: object
  property_count: 5
  slug: createapikeyresponsedata
- name: Direct Deposit Allocations
  property_count: 5
  slug: ddallocationobjresponse
- name: Deduction
  property_count: 4
  slug: deductionobjpublicresponseitem
- name: DirectDepositAllocationDetail
  property_count: 3
  slug: directdepositallocationdetail
- name: Document
  property_count: 3
  slug: documentobjpublicresponseitem
- name: Earning
  property_count: 5
  slug: earningobjpublicresponseitem
- name: EarningsStreamPayoutsResponse
  property_count: 4
  slug: earningsstreampayoutobjresponse-v2023-04-18
- name: EarningsYtds
  property_count: 2
  slug: earningsytds
- name: EmployeeName
  property_count: 4
  slug: employeename
- name: EmployeeNameAndAddress
  property_count: 2
  slug: employeenameandaddress
- name: EmployeeResponseObj
  property_count: 5
  slug: employeeresponseobj
- name: EmployerNameAndAddress
  property_count: 2
  slug: employernameandaddress
- name: Employer
  property_count: 12
  slug: employerobjresponse
- name: Employment
  property_count: 11
  slug: employmentobjresponse
- name: EmploymentResponseObj
  property_count: 9
  slug: employmentresponseobj
- name: EndUser
  property_count: 1
  slug: enduser
- name: Document for end user
  property_count: 8
  slug: enduserdocumentobjresponse
- name: FieldWarning
  property_count: 3
  slug: fieldwarning
- name: FreshnessPaginationListMeta
  property_count: 4
  slug: freshnesspaginationlistmeta
- name: Identity
  property_count: 10
  slug: identityobjresponse
- name: IncomeAndEmploymentResponseObj
  property_count: 10
  slug: incomeandemploymentresponseobj
- name: Income
  property_count: 8
  slug: incomeobjresponse
- name: IncomeResponseObj
  property_count: 6
  slug: incomeresponseobj
- name: Job
  property_count: 9
  slug: jobobjresponse-v2023-11-22
- name: Job
  property_count: 9
  slug: jobobjresponse
- name: LinkTokenPostBody
  property_count: 19
  slug: linktokencreate-v2025-07-08
- name: LinkToken
  property_count: 5
  slug: linktokenobjresponse-v2021-07-28
- name: object
  property_count: 8
  slug: linkuserauthenticationdataobjcreate
- name: object
  property_count: 7
  slug: listapikeyresponsedata
- name: ListMeta
  property_count: 1
  slug: listmeta
- name: MerchantPayment
  property_count: 5
  slug: merchantpayment
- name: NetPayObjResponse
  property_count: 2
  slug: netpayobjresponse
- name: PaginationMeta
  property_count: 2
  slug: paginationmeta
- name: ParamsPayload_v2023_11_22
  property_count: 22
  slug: paramspayload-v2023-11-22
- name: object
  property_count: 23
  slug: paramspayload
- name: PayrollAccountDataRefreshed
  property_count: 6
  slug: payrollaccountdatarefreshed
- name: PayrollAccountDataUpdated
  property_count: 6
  slug: payrollaccountdataupdated
- name: Account
  property_count: 12
  slug: payrollaccountobjresponse
- name: object
  property_count: 1
  slug: payrollaccountpatchmonitoringstatus
- name: Paystub
  property_count: 22
  slug: paystubobjresponse-v2022-03-02
- name: PaystubWithEarningsResponseObj
  property_count: 18
  slug: paystubwithearningsresponseobj
- name: Phone
  property_count: 2
  slug: phonenumbergetresponseitem
- name: Platform
  property_count: 14
  slug: platformobjresponse
- name: RefreshableMeta
  property_count: 1
  slug: refreshablemeta
- name: RefreshablePaginationListMeta
  property_count: 3
  slug: refreshablepaginationlistmeta
- name: RevokeAPIKeyResponse
  property_count: 1
  slug: revokeapikeyresponse
- name: object
  property_count: 5
  slug: revokeapikeyresponsedata
- name: SearchResult
  property_count: 14
  slug: searchresultobjresponse
- name: SharedFraud
  property_count: 1
  slug: sharedfraud
- name: Earning
  property_count: 5
  slug: shiftearningobjpublicresponseitem
- name: Shift
  property_count: 10
  slug: shiftobjresponse
- name: ShiftTimestamp
  property_count: 2
  slug: shifttimestamp
- name: TargetAccount
  property_count: 3
  slug: targetaccount
- name: TaxForm
  property_count: 8
  slug: taxformobjresponse-v2022-06-22
- name: TaxForm
  property_count: 5
  slug: taxformobjresponsenodocument-v2022-06-22
- name: TaxFormW2
  property_count: 22
  slug: taxformw2
- name: Tax
  property_count: 3
  slug: taxobjpublicresponseitem
- name: TimeOff
  property_count: 5
  slug: timeoffobjpublicresponseitem
- name: UploadedBankStatement
  property_count: 8
  slug: uploadedbankstatement
- name: UploadedDeduction
  property_count: 4
  slug: uploadeddeduction
- name: UploadedEarning
  property_count: 4
  slug: uploadedearning
- name: UploadedPaystub
  property_count: 14
  slug: uploadedpaystub
- name: UploadedSSIAwardLetter
  property_count: 8
  slug: uploadedssiawardletter
- name: UploadedTax
  property_count: 4
  slug: uploadedtax
- name: UploadedTimeOff
  property_count: 5
  slug: uploadedtimeoff
- name: UploadedW2Informed
  property_count: 12
  slug: uploadedw2informed
- name: Verification of Employment Report for an end user
  property_count: 7
  slug: verificationreportsvoeobjresponse
- name: Verification of Income and Employment Report for an end user
  property_count: 7
  slug: verificationreportsvoieobjresponse
- name: W2Box12
  property_count: 2
  slug: w2box12
- name: W2Box13
  property_count: 3
  slug: w2box13
- name: W2Box15To20
  property_count: 7
  slug: w2box15to20
- name: W2BoxC
  property_count: 2
  slug: w2boxc
- name: WebhookPostBody
  property_count: 5
  slug: webhookcreate-v2023-04-18
- name: Webhook
  property_count: 8
  slug: webhookobjresponse
- name: WebhookPatchBody
  property_count: 4
  slug: webhookupdate
jsonld:
- class_count: 135
  name: Pinwheel Context
  property_count: 9
  slug: pinwheel-context
layout: provider
modified: '2026-06-13'
name: Pinwheel
nav: Providers
network: true
overview: 'Pinwheel publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API Keys API, Company Connect API, and 11 more. Tagged areas include Payroll, Direct Deposit, Income Verification, Employment, and Tax Forms.


  The Pinwheel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pinwheel''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Pinwheel Plans Pricing
  plan_count: 3
  slug: pinwheel-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Pinwheel Rate Limits
  slug: pinwheel-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pinwheel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pinwheel-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.8
  delta: -2.2
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 70.1
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 27.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pinwheel/refs/heads/main/screenshots/pinwheel-2026-06-20T191723.png
security:
- kind: authentication
  name: Pinwheel Authentication
  slug: pinwheel-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Pinwheel Domain Security
  slug: pinwheel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pinwheel Trust Center
  slug: pinwheel-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: pinwheel
tags:
- Payroll
- Direct Deposit
- Income Verification
- Employment
- Tax Forms
- Fintech
- Open Finance
- Bill Switching
- Financial Data
website: https://www.pinwheelapi.com
---
