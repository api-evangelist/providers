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
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 294
  human_in_the_loop: 2
  name: Adyen Agentic Access
  operation_count: 424
  slug: adyen-agentic-access
  summary_line: 424 operations · 294 acting · 2 human-in-the-loop
api_count: 25
apis:
- description: The acceptDispute API from Adyen — 1 operation(s) for acceptdispute.
  name: Adyen acceptDispute API
  slug: adyen-acceptdispute-api
- description: The Account API from Adyen — 7 operation(s) for account.
  name: Adyen Account API
  slug: adyen-account-api
- description: The accountHolderBalance API from Adyen — 1 operation(s) for accountholderbalance.
  name: Adyen accountHolderBalance API
  slug: adyen-accountholderbalance-api
- description: The accountHolderTransactionList API from Adyen — 1 operation(s) for accountholdertransactionlist.
  name: Adyen accountHolderTransactionList API
  slug: adyen-accountholdertransactionlist-api
- description: The Accounts API from Adyen — 17 operation(s) for accounts.
  name: Adyen Accounts API
  slug: adyen-accounts-api
- description: The adjustAuthorisation API from Adyen — 1 operation(s) for adjustauthorisation.
  name: Adyen adjustAuthorisation API
  slug: adyen-adjustauthorisation-api
- description: The Admin API from Adyen — 1 operation(s) for admin.
  name: Adyen Admin API
  slug: adyen-admin-api
- description: The Amount API from Adyen — 1 operation(s) for amount.
  name: Adyen Amount API
  slug: adyen-amount-api
- description: The Apple API from Adyen — 1 operation(s) for apple.
  name: Adyen Apple API
  slug: adyen-apple-api
- description: The assignTerminals API from Adyen — 1 operation(s) for assignterminals.
  name: Adyen assignTerminals API
  slug: adyen-assignterminals-api
- description: The Authorise API from Adyen — 1 operation(s) for authorise.
  name: Adyen Authorise API
  slug: adyen-authorise-api
- description: The Authorise3d API from Adyen — 1 operation(s) for authorise3d.
  name: Adyen Authorise3d API
  slug: adyen-authorise3d-api
- description: The Authorise3ds2 API from Adyen — 1 operation(s) for authorise3ds2.
  name: Adyen Authorise3ds2 API
  slug: adyen-authorise3ds2-api
- description: The Availability API from Adyen — 1 operation(s) for availability.
  name: Adyen Availability API
  slug: adyen-availability-api
- description: The Balance API from Adyen — 10 operation(s) for balance.
  name: Adyen Balance API
  slug: adyen-balance-api
- description: The Balanceinquiry API from Adyen — 1 operation(s) for balanceinquiry.
  name: Adyen Balanceinquiry API
  slug: adyen-balanceinquiry-api
- description: The businessLines API from Adyen — 2 operation(s) for businesslines.
  name: Adyen businessLines API
  slug: adyen-businesslines-api
- description: The Calculate API from Adyen — 1 operation(s) for calculate.
  name: Adyen Calculate API
  slug: adyen-calculate-api
- description: The Cancel API from Adyen — 1 operation(s) for cancel.
  name: Adyen Cancel API
  slug: adyen-cancel-api
- description: The cancelOrRefund API from Adyen — 1 operation(s) for cancelorrefund.
  name: Adyen cancelOrRefund API
  slug: adyen-cancelorrefund-api
- description: The Cancels API from Adyen — 3 operation(s) for cancels.
  name: Adyen Cancels API
  slug: adyen-cancels-api
- description: The Capture API from Adyen — 1 operation(s) for capture.
  name: Adyen Capture API
  slug: adyen-capture-api
- description: The Captures API from Adyen — 1 operation(s) for captures.
  name: Adyen Captures API
  slug: adyen-captures-api
- description: The Card API from Adyen — 1 operation(s) for card.
  name: Adyen Card API
  slug: adyen-card-api
- description: The Card Orders API from Adyen — 2 operation(s) for card orders.
  name: Adyen Card Orders API
  slug: adyen-card-orders-api
- description: The Cardacquisition API from Adyen — 1 operation(s) for cardacquisition.
  name: Adyen Cardacquisition API
  slug: adyen-cardacquisition-api
- description: The Cardreaderapdu API from Adyen — 1 operation(s) for cardreaderapdu.
  name: Adyen Cardreaderapdu API
  slug: adyen-cardreaderapdu-api
- description: The Changes API from Adyen — 1 operation(s) for changes.
  name: Adyen Changes API
  slug: adyen-changes-api
- description: The changeStatus API from Adyen — 1 operation(s) for changestatus.
  name: Adyen changeStatus API
  slug: adyen-changestatus-api
- description: The checkAccountHolder API from Adyen — 1 operation(s) for checkaccountholder.
  name: Adyen checkAccountHolder API
  slug: adyen-checkaccountholder-api
- description: The checkBalance API from Adyen — 1 operation(s) for checkbalance.
  name: Adyen checkBalance API
  slug: adyen-checkbalance-api
- description: The closeAccount API from Adyen — 1 operation(s) for closeaccount.
  name: Adyen closeAccount API
  slug: adyen-closeaccount-api
- description: The closeAccountHolder API from Adyen — 1 operation(s) for closeaccountholder.
  name: Adyen closeAccountHolder API
  slug: adyen-closeaccountholder-api
- description: The closeStores API from Adyen — 1 operation(s) for closestores.
  name: Adyen closeStores API
  slug: adyen-closestores-api
- description: The Companies API from Adyen — 29 operation(s) for companies.
  name: Adyen Companies API
  slug: adyen-companies-api
- description: The confirmThirdParty API from Adyen — 1 operation(s) for confirmthirdparty.
  name: Adyen confirmThirdParty API
  slug: adyen-confirmthirdparty-api
- description: The Cost API from Adyen — 1 operation(s) for cost.
  name: Adyen Cost API
  slug: adyen-cost-api
- description: The createAccount API from Adyen — 1 operation(s) for createaccount.
  name: Adyen createAccount API
  slug: adyen-createaccount-api
- description: The createAccountHolder API from Adyen — 1 operation(s) for createaccountholder.
  name: Adyen createAccountHolder API
  slug: adyen-createaccountholder-api
- description: The createNotificationConfiguration API from Adyen — 1 operation(s) for createnotificationconfiguration.
  name: Adyen createNotificationConfiguration API
  slug: adyen-createnotificationconfiguration-api
- description: The createPermit API from Adyen — 1 operation(s) for createpermit.
  name: Adyen createPermit API
  slug: adyen-createpermit-api
- description: The createTestCardRanges API from Adyen — 1 operation(s) for createtestcardranges.
  name: Adyen createTestCardRanges API
  slug: adyen-createtestcardranges-api
- description: The debitAccountHolder API from Adyen — 1 operation(s) for debitaccountholder.
  name: Adyen debitAccountHolder API
  slug: adyen-debitaccountholder-api
- description: The declineThirdParty API from Adyen — 1 operation(s) for declinethirdparty.
  name: Adyen declineThirdParty API
  slug: adyen-declinethirdparty-api
- description: The defendDispute API from Adyen — 1 operation(s) for defenddispute.
  name: Adyen defendDispute API
  slug: adyen-defenddispute-api
- description: The deleteBankAccounts API from Adyen — 1 operation(s) for deletebankaccounts.
  name: Adyen deleteBankAccounts API
  slug: adyen-deletebankaccounts-api
- description: The deleteDisputeDefenseDocument API from Adyen — 1 operation(s) for deletedisputedefensedocument.
  name: Adyen deleteDisputeDefenseDocument API
  slug: adyen-deletedisputedefensedocument-api
- description: The deleteLegalArrangements API from Adyen — 1 operation(s) for deletelegalarrangements.
  name: Adyen deleteLegalArrangements API
  slug: adyen-deletelegalarrangements-api
- description: The deleteNotificationConfigurations API from Adyen — 1 operation(s) for deletenotificationconfigurations.
  name: Adyen deleteNotificationConfigurations API
  slug: adyen-deletenotificationconfigurations-api
- description: The deletePayoutMethods API from Adyen — 1 operation(s) for deletepayoutmethods.
  name: Adyen deletePayoutMethods API
  slug: adyen-deletepayoutmethods-api
- description: The deleteShareholders API from Adyen — 1 operation(s) for deleteshareholders.
  name: Adyen deleteShareholders API
  slug: adyen-deleteshareholders-api
- description: The deleteSignatories API from Adyen — 1 operation(s) for deletesignatories.
  name: Adyen deleteSignatories API
  slug: adyen-deletesignatories-api
- description: The Diagnosis API from Adyen — 1 operation(s) for diagnosis.
  name: Adyen Diagnosis API
  slug: adyen-diagnosis-api
- description: The Disable API from Adyen — 1 operation(s) for disable.
  name: Adyen Disable API
  slug: adyen-disable-api
- description: The disablePermit API from Adyen — 1 operation(s) for disablepermit.
  name: Adyen disablePermit API
  slug: adyen-disablepermit-api
- description: The Display API from Adyen — 1 operation(s) for display.
  name: Adyen Display API
  slug: adyen-display-api
- description: The Documents API from Adyen — 4 operation(s) for documents.
  name: Adyen Documents API
  slug: adyen-documents-api
- description: The Donate API from Adyen — 1 operation(s) for donate.
  name: Adyen Donate API
  slug: adyen-donate-api
- description: The Donations API from Adyen — 1 operation(s) for donations.
  name: Adyen Donations API
  slug: adyen-donations-api
- description: The Enableservice API from Adyen — 1 operation(s) for enableservice.
  name: Adyen Enableservice API
  slug: adyen-enableservice-api
- description: The Erasure API from Adyen — 1 operation(s) for erasure.
  name: Adyen Erasure API
  slug: adyen-erasure-api
- description: The findTerminal API from Adyen — 1 operation(s) for findterminal.
  name: Adyen findTerminal API
  slug: adyen-findterminal-api
- description: The getAccountHolder API from Adyen — 1 operation(s) for getaccountholder.
  name: Adyen getAccountHolder API
  slug: adyen-getaccountholder-api
- description: The getAuthenticationResult API from Adyen — 1 operation(s) for getauthenticationresult.
  name: Adyen getAuthenticationResult API
  slug: adyen-getauthenticationresult-api
- description: The getNotificationConfiguration API from Adyen — 1 operation(s) for getnotificationconfiguration.
  name: Adyen getNotificationConfiguration API
  slug: adyen-getnotificationconfiguration-api
- description: The getNotificationConfigurationList API from Adyen — 1 operation(s) for getnotificationconfigurationlist.
  name: Adyen getNotificationConfigurationList API
  slug: adyen-getnotificationconfigurationlist-api
- description: The getOnboardingUrl API from Adyen — 1 operation(s) for getonboardingurl.
  name: Adyen getOnboardingUrl API
  slug: adyen-getonboardingurl-api
- description: The getPciQuestionnaireUrl API from Adyen — 1 operation(s) for getpciquestionnaireurl.
  name: Adyen getPciQuestionnaireUrl API
  slug: adyen-getpciquestionnaireurl-api
- description: The getStoresUnderAccount API from Adyen — 1 operation(s) for getstoresunderaccount.
  name: Adyen getStoresUnderAccount API
  slug: adyen-getstoresunderaccount-api
- description: The getTaxForm API from Adyen — 1 operation(s) for gettaxform.
  name: Adyen getTaxForm API
  slug: adyen-gettaxform-api
- description: The getTerminalDetails API from Adyen — 1 operation(s) for getterminaldetails.
  name: Adyen getTerminalDetails API
  slug: adyen-getterminaldetails-api
- description: The getTerminalsUnderAccount API from Adyen — 1 operation(s) for getterminalsunderaccount.
  name: Adyen getTerminalsUnderAccount API
  slug: adyen-getterminalsunderaccount-api
- description: The Gettotals API from Adyen — 1 operation(s) for gettotals.
  name: Adyen Gettotals API
  slug: adyen-gettotals-api
- description: The getUploadedDocuments API from Adyen — 1 operation(s) for getuploadeddocuments.
  name: Adyen getUploadedDocuments API
  slug: adyen-getuploadeddocuments-api
- description: The Grants API from Adyen — 2 operation(s) for grants.
  name: Adyen Grants API
  slug: adyen-grants-api
- description: The Input API from Adyen — 1 operation(s) for input.
  name: Adyen Input API
  slug: adyen-input-api
- description: The Instruments API from Adyen — 9 operation(s) for instruments.
  name: Adyen Instruments API
  slug: adyen-instruments-api
- description: The Issue API from Adyen — 1 operation(s) for issue.
  name: Adyen Issue API
  slug: adyen-issue-api
- description: The Keys API from Adyen — 2 operation(s) for keys.
  name: Adyen Keys API
  slug: adyen-keys-api
- description: The legalEntities API from Adyen — 14 operation(s) for legalentities.
  name: Adyen legalEntities API
  slug: adyen-legalentities-api
- description: The Links API from Adyen — 2 operation(s) for links.
  name: Adyen Links API
  slug: adyen-links-api
- description: The listRecurringDetails API from Adyen — 1 operation(s) for listrecurringdetails.
  name: Adyen listRecurringDetails API
  slug: adyen-listrecurringdetails-api
- description: The Load API from Adyen — 1 operation(s) for load.
  name: Adyen Load API
  slug: adyen-load-api
- description: The Login API from Adyen — 1 operation(s) for login.
  name: Adyen Login API
  slug: adyen-login-api
- description: The Logout API from Adyen — 1 operation(s) for logout.
  name: Adyen Logout API
  slug: adyen-logout-api
- description: The Loyalty API from Adyen — 1 operation(s) for loyalty.
  name: Adyen Loyalty API
  slug: adyen-loyalty-api
- description: The Me API from Adyen — 4 operation(s) for me.
  name: Adyen Me API
  slug: adyen-me-api
- description: The Merchants API from Adyen — 38 operation(s) for merchants.
  name: Adyen Merchants API
  slug: adyen-merchants-api
- description: The mergeBalance API from Adyen — 1 operation(s) for mergebalance.
  name: Adyen mergeBalance API
  slug: adyen-mergebalance-api
- description: The Method API from Adyen — 1 operation(s) for method.
  name: Adyen Method API
  slug: adyen-method-api
- description: The Methods API from Adyen — 5 operation(s) for methods.
  name: Adyen Methods API
  slug: adyen-methods-api
- description: The Networks API from Adyen — 1 operation(s) for networks.
  name: Adyen Networks API
  slug: adyen-networks-api
- description: The notifyShopper API from Adyen — 1 operation(s) for notifyshopper.
  name: Adyen notifyShopper API
  slug: adyen-notifyshopper-api
- description: The Offer API from Adyen — 1 operation(s) for offer.
  name: Adyen Offer API
  slug: adyen-offer-api
- description: The Offers API from Adyen — 2 operation(s) for offers.
  name: Adyen Offers API
  slug: adyen-offers-api
- description: The Orders API from Adyen — 2 operation(s) for orders.
  name: Adyen Orders API
  slug: adyen-orders-api
- description: The Payment API from Adyen — 2 operation(s) for payment.
  name: Adyen Payment API
  slug: adyen-payment-api
- description: The Payments API from Adyen — 23 operation(s) for payments.
  name: Adyen Payments API
  slug: adyen-payments-api
- description: The Payout API from Adyen — 1 operation(s) for payout.
  name: Adyen Payout API
  slug: adyen-payout-api
- description: The payoutAccountHolder API from Adyen — 1 operation(s) for payoutaccountholder.
  name: Adyen payoutAccountHolder API
  slug: adyen-payoutaccountholder-api
- description: The Pins API from Adyen — 3 operation(s) for pins.
  name: Adyen Pins API
  slug: adyen-pins-api
- description: The Print API from Adyen — 1 operation(s) for print.
  name: Adyen Print API
  slug: adyen-print-api
- description: The Reconciliation API from Adyen — 1 operation(s) for reconciliation.
  name: Adyen Reconciliation API
  slug: adyen-reconciliation-api
- description: The Refund API from Adyen — 1 operation(s) for refund.
  name: Adyen Refund API
  slug: adyen-refund-api
- description: The refundFundsTransfer API from Adyen — 1 operation(s) for refundfundstransfer.
  name: Adyen refundFundsTransfer API
  slug: adyen-refundfundstransfer-api
- description: The refundNotPaidOutTransfers API from Adyen — 1 operation(s) for refundnotpaidouttransfers.
  name: Adyen refundNotPaidOutTransfers API
  slug: adyen-refundnotpaidouttransfers-api
- description: The retrieve3ds2Result API from Adyen — 1 operation(s) for retrieve3ds2result.
  name: Adyen retrieve3ds2Result API
  slug: adyen-retrieve3ds2result-api
- description: The retrieveApplicableDefenseReasons API from Adyen — 1 operation(s) for retrieveapplicabledefensereasons.
  name: Adyen retrieveApplicableDefenseReasons API
  slug: adyen-retrieveapplicabledefensereasons-api
- description: The Reversal API from Adyen — 1 operation(s) for reversal.
  name: Adyen Reversal API
  slug: adyen-reversal-api
- description: The Rules API from Adyen — 4 operation(s) for rules.
  name: Adyen Rules API
  slug: adyen-rules-api
- description: The scheduleAccountUpdater API from Adyen — 1 operation(s) for scheduleaccountupdater.
  name: Adyen scheduleAccountUpdater API
  slug: adyen-scheduleaccountupdater-api
- description: The Session API from Adyen — 2 operation(s) for session.
  name: Adyen Session API
  slug: adyen-session-api
- description: The Sessions API from Adyen — 3 operation(s) for sessions.
  name: Adyen Sessions API
  slug: adyen-sessions-api
- description: The setupBeneficiary API from Adyen — 1 operation(s) for setupbeneficiary.
  name: Adyen setupBeneficiary API
  slug: adyen-setupbeneficiary-api
- description: The storeDetail API from Adyen — 1 operation(s) for storedetail.
  name: Adyen storeDetail API
  slug: adyen-storedetail-api
- description: The storeDetailAndSubmitThirdParty API from Adyen — 1 operation(s) for storedetailandsubmitthirdparty.
  name: Adyen storeDetailAndSubmitThirdParty API
  slug: adyen-storedetailandsubmitthirdparty-api
- description: The Storedvalue API from Adyen — 1 operation(s) for storedvalue.
  name: Adyen Storedvalue API
  slug: adyen-storedvalue-api
- description: The Stores API from Adyen — 5 operation(s) for stores.
  name: Adyen Stores API
  slug: adyen-stores-api
- description: The submitThirdParty API from Adyen — 1 operation(s) for submitthirdparty.
  name: Adyen submitThirdParty API
  slug: adyen-submitthirdparty-api
- description: The supplyDefenseDocument API from Adyen — 1 operation(s) for supplydefensedocument.
  name: Adyen supplyDefenseDocument API
  slug: adyen-supplydefensedocument-api
- description: The suspendAccountHolder API from Adyen — 1 operation(s) for suspendaccountholder.
  name: Adyen suspendAccountHolder API
  slug: adyen-suspendaccountholder-api
- description: The technicalCancel API from Adyen — 1 operation(s) for technicalcancel.
  name: Adyen technicalCancel API
  slug: adyen-technicalcancel-api
- description: The Terminals API from Adyen — 5 operation(s) for terminals.
  name: Adyen Terminals API
  slug: adyen-terminals-api
- description: The testNotificationConfiguration API from Adyen — 1 operation(s) for testnotificationconfiguration.
  name: Adyen testNotificationConfiguration API
  slug: adyen-testnotificationconfiguration-api
- description: The Themes API from Adyen — 2 operation(s) for themes.
  name: Adyen Themes API
  slug: adyen-themes-api
- description: The Transactions API from Adyen — 2 operation(s) for transactions.
  name: Adyen Transactions API
  slug: adyen-transactions-api
- description: The Transactionstatus API from Adyen — 1 operation(s) for transactionstatus.
  name: Adyen Transactionstatus API
  slug: adyen-transactionstatus-api
- description: The transferFunds API from Adyen — 1 operation(s) for transferfunds.
  name: Adyen transferFunds API
  slug: adyen-transferfunds-api
- description: The transferInstruments API from Adyen — 2 operation(s) for transferinstruments.
  name: Adyen transferInstruments API
  slug: adyen-transferinstruments-api
- description: The Transfers API from Adyen — 4 operation(s) for transfers.
  name: Adyen Transfers API
  slug: adyen-transfers-api
- description: The unSuspendAccountHolder API from Adyen — 1 operation(s) for unsuspendaccountholder.
  name: Adyen unSuspendAccountHolder API
  slug: adyen-unsuspendaccountholder-api
- description: The updateAccount API from Adyen — 1 operation(s) for updateaccount.
  name: Adyen updateAccount API
  slug: adyen-updateaccount-api
- description: The updateAccountHolder API from Adyen — 1 operation(s) for updateaccountholder.
  name: Adyen updateAccountHolder API
  slug: adyen-updateaccountholder-api
- description: The updateAccountHolderState API from Adyen — 1 operation(s) for updateaccountholderstate.
  name: Adyen updateAccountHolderState API
  slug: adyen-updateaccountholderstate-api
- description: The updateNotificationConfiguration API from Adyen — 1 operation(s) for updatenotificationconfiguration.
  name: Adyen updateNotificationConfiguration API
  slug: adyen-updatenotificationconfiguration-api
- description: The uploadDocument API from Adyen — 1 operation(s) for uploaddocument.
  name: Adyen uploadDocument API
  slug: adyen-uploaddocument-api
- description: The voidPendingRefund API from Adyen — 1 operation(s) for voidpendingrefund.
  name: Adyen voidPendingRefund API
  slug: adyen-voidpendingrefund-api
- description: The voidTransaction API from Adyen — 1 operation(s) for voidtransaction.
  name: Adyen voidTransaction API
  slug: adyen-voidtransaction-api
arazzos:
- description: Authorise a card payment then adjust the authorised amount.
  name: Adyen Checkout Payment and Amount Update
  slug: adyen-checkout-payment-and-amount-update-workflow
- description: Authorise a card payment then cancel the authorisation.
  name: Adyen Checkout Payment and Cancel
  slug: adyen-checkout-payment-and-cancel-workflow
- description: Authorise a card payment then capture the authorised amount.
  name: Adyen Checkout Payment and Capture
  slug: adyen-checkout-payment-and-capture-workflow
- description: Make a captured card payment then refund all or part of it.
  name: Adyen Checkout Payment and Refund
  slug: adyen-checkout-payment-and-refund-workflow
- description: Make a card payment then reverse it with a single request.
  name: Adyen Checkout Payment and Reverse
  slug: adyen-checkout-payment-and-reverse-workflow
- description: Create a hosted checkout payment session and poll for its final status.
  name: Adyen Create Checkout Session and Poll Result
  slug: adyen-checkout-session-create-and-poll-workflow
- description: Authorise a payment then cancel or refund it without tracking its state.
  name: Adyen Classic Authorise and Cancel or Refund
  slug: adyen-classic-authorise-and-cancel-or-refund-workflow
- description: Authorise a payment with the classic Payment API then cancel it.
  name: Adyen Classic Authorise and Cancel
  slug: adyen-classic-authorise-and-cancel-workflow
- description: Authorise a payment with the classic Payment API then capture it.
  name: Adyen Classic Authorise and Capture
  slug: adyen-classic-authorise-and-capture-workflow
- description: Authorise a payment with the classic Payment API then refund it.
  name: Adyen Classic Authorise and Refund
  slug: adyen-classic-authorise-and-refund-workflow
- description: Create a merchant account under a company then request its activation.
  name: Adyen Management Create Merchant Account and Request Activation
  slug: adyen-management-merchant-create-and-activate-workflow
- description: Add a payment method to a merchant account then read its settings back.
  name: Adyen Management Add Payment Method and Get Its Settings
  slug: adyen-management-payment-method-add-and-get-workflow
- description: Register a merchant webhook, generate its HMAC key, then send a test event.
  name: Adyen Management Create Webhook, Generate HMAC and Test
  slug: adyen-management-webhook-create-hmac-and-test-workflow
- description: Create a Pay by Link payment link then expire it when no longer needed.
  name: Adyen Create Payment Link and Expire It
  slug: adyen-payment-link-create-and-expire-workflow
- description: Create a Pay by Link payment link then read its current status.
  name: Adyen Create Payment Link and Get Status
  slug: adyen-payment-link-create-and-get-workflow
- description: Store payout details, submit a third party payout, then confirm or decline it.
  name: Adyen Third Party Payout Store, Submit and Confirm
  slug: adyen-payout-store-submit-and-confirm-workflow
- description: List a shopper's stored payment tokens then disable one of them.
  name: Adyen List Recurring Details and Disable a Token
  slug: adyen-recurring-list-and-disable-workflow
artifact_total: 7006
asyncapis:
- description: 'AsyncAPI description of Adyen''s webhook surface. Adyen pushes event-driven messages to a customer-defined HTTPS endpoint using HTTP POST. This document models two webhook surfaces: * Standard Notifica'
  name: Adyen Webhooks (Standard Notifications and Platforms)
  slug: adyen-webhooks-asyncapi
collections:
- collection_type: postman
  name: Adyen Account API
  slug: postman-accounts-openapi-original
- collection_type: postman
  name: Adyen Balance Control API
  slug: postman-balance-control-openapi-original
- collection_type: postman
  name: Adyen BinLookup API
  slug: postman-binlookup-openapi-original
- collection_type: postman
  name: Adyen Checkout API
  slug: postman-checkout-openapi-original
- collection_type: postman
  name: Adyen Configuration API
  slug: postman-configuration-openapi-original
- collection_type: postman
  name: Adyen Data Protection API
  slug: postman-data-protection-openapi-original
- collection_type: postman
  name: Adyen Disputes API
  slug: postman-disputes-openapi-original
- collection_type: postman
  name: Adyen Fund API
  slug: postman-funds-openapi-original
- collection_type: postman
  name: Adyen Hosted Onboarding API
  slug: postman-hosted-onboarding-openapi-original
- collection_type: postman
  name: Adyen Legal Entity Management API
  slug: postman-legal-entity-openapi-original
- collection_type: postman
  name: Adyen Management API
  slug: postman-management-openapi-original
- collection_type: postman
  name: Adyen Notification Configuration API
  slug: postman-notification-configurations-openapi-original
- collection_type: postman
  name: Adyen Payment API
  slug: postman-payments-openapi-original
- collection_type: postman
  name: Adyen Payout API
  slug: postman-payouts-openapi-original
- collection_type: postman
  name: Adyen POS Terminal Management API
  slug: postman-pos-terminal-openapi-original
- collection_type: postman
  name: Adyen Recurring API
  slug: postman-recurring-openapi-original
- collection_type: postman
  name: Adyen Stored Value API
  slug: postman-stored-value-openapi-original
- collection_type: postman
  name: Adyen Terminal API
  slug: postman-terminal-openapi-original
- collection_type: postman
  name: Adyen Test Cards API
  slug: postman-test-cards-openapi-original
- collection_type: postman
  name: Adyen Transfers API
  slug: postman-transfers-openapi-original
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adyen Account acceptDispute API
  slug: open-adyen-acceptdispute-api
- collection_type: open
  name: Adyen acceptDispute Account API
  slug: open-adyen-account-api
- collection_type: open
  name: Adyen Account acceptDispute accountHolderBalance API
  slug: open-adyen-accountholderbalance-api
- collection_type: open
  name: Adyen Account acceptDispute accountHolders API
  slug: open-adyen-accountholders-api
- collection_type: open
  name: Adyen Account acceptDispute accountHolderTransactionList API
  slug: open-adyen-accountholdertransactionlist-api
- collection_type: open
  name: Adyen Accounting Notifications API
  slug: open-adyen-accounting-notifications-api
- collection_type: open
  name: Adyen Account acceptDispute Accounts API
  slug: open-adyen-accounts-api
- collection_type: open
  name: Adyen Account acceptDispute adjustAuthorisation API
  slug: open-adyen-adjustauthorisation-api
- collection_type: open
  name: Adyen Account acceptDispute Admin API
  slug: open-adyen-admin-api
- collection_type: open
  name: Adyen Account acceptDispute Amount API
  slug: open-adyen-amount-api
- collection_type: open
  name: Adyen Account acceptDispute Apple API
  slug: open-adyen-apple-api
- collection_type: open
  name: Adyen Account acceptDispute applePay API
  slug: open-adyen-applepay-api
- collection_type: open
  name: Adyen Account acceptDispute Arrangements API
  slug: open-adyen-arrangements-api
- collection_type: open
  name: Adyen Account acceptDispute assignTerminals API
  slug: open-adyen-assignterminals-api
- collection_type: open
  name: Adyen Authentication Webhooks API
  slug: open-adyen-authentication-webhooks-api
- collection_type: open
  name: Adyen Account acceptDispute Authorise API
  slug: open-adyen-authorise-api
- collection_type: open
  name: Adyen Account acceptDispute Authorise3d API
  slug: open-adyen-authorise3d-api
- collection_type: open
  name: Adyen Account acceptDispute Authorise3ds2 API
  slug: open-adyen-authorise3ds2-api
- collection_type: open
  name: Adyen Account acceptDispute Availability API
  slug: open-adyen-availability-api
- collection_type: open
  name: Adyen Account acceptDispute Balance API
  slug: open-adyen-balance-api
- collection_type: open
  name: Adyen Balance Control API
  slug: open-adyen-balance-control-api
- collection_type: open
  name: Adyen Account acceptDispute balanceAccounts API
  slug: open-adyen-balanceaccounts-api
- collection_type: open
  name: Adyen Account acceptDispute Balanceinquiry API
  slug: open-adyen-balanceinquiry-api
- collection_type: open
  name: Adyen Account acceptDispute balancePlatforms API
  slug: open-adyen-balanceplatforms-api
- collection_type: open
  name: Adyen Account acceptDispute balanceTransfer API
  slug: open-adyen-balancetransfer-api
- collection_type: open
  name: Adyen Account acceptDispute Bank API
  slug: open-adyen-bank-api
- collection_type: open
  name: Adyen BinLookup API
  slug: open-adyen-binlookup-api
- collection_type: open
  name: Adyen Account acceptDispute businessLines API
  slug: open-adyen-businesslines-api
- collection_type: open
  name: Adyen Account acceptDispute Calculate API
  slug: open-adyen-calculate-api
- collection_type: open
  name: Adyen Account acceptDispute Cancel API
  slug: open-adyen-cancel-api
- collection_type: open
  name: Adyen Account acceptDispute cancelOrRefund API
  slug: open-adyen-cancelorrefund-api
- collection_type: open
  name: Adyen Account acceptDispute Cancels API
  slug: open-adyen-cancels-api
- collection_type: open
  name: Adyen Account acceptDispute Capture API
  slug: open-adyen-capture-api
- collection_type: open
  name: Adyen Account acceptDispute Captures API
  slug: open-adyen-captures-api
- collection_type: open
  name: Adyen Account acceptDispute Card API
  slug: open-adyen-card-api
- collection_type: open
  name: Adyen Account acceptDispute Card Orders API
  slug: open-adyen-card-orders-api
- collection_type: open
  name: Adyen Account acceptDispute Cardacquisition API
  slug: open-adyen-cardacquisition-api
- collection_type: open
  name: Adyen Account acceptDispute cardDetails API
  slug: open-adyen-carddetails-api
- collection_type: open
  name: Adyen Account acceptDispute Cardorders API
  slug: open-adyen-cardorders-api
- collection_type: open
  name: Adyen Account acceptDispute Cardreaderapdu API
  slug: open-adyen-cardreaderapdu-api
- collection_type: open
  name: Adyen Account acceptDispute Changes API
  slug: open-adyen-changes-api
- collection_type: open
  name: Adyen Account acceptDispute changeStatus API
  slug: open-adyen-changestatus-api
- collection_type: open
  name: Adyen Account acceptDispute checkAccountHolder API
  slug: open-adyen-checkaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute checkBalance API
  slug: open-adyen-checkbalance-api
- collection_type: open
  name: API Collection
  slug: open-adyen-checkout-api
- collection_type: open
  name: Adyen Account acceptDispute Checks API
  slug: open-adyen-checks-api
- collection_type: open
  name: Adyen Account acceptDispute Close API
  slug: open-adyen-close-api
- collection_type: open
  name: Adyen Account acceptDispute closeAccount API
  slug: open-adyen-closeaccount-api
- collection_type: open
  name: Adyen Account acceptDispute closeAccountHolder API
  slug: open-adyen-closeaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute closeStores API
  slug: open-adyen-closestores-api
- collection_type: open
  name: Adyen Account acceptDispute Companies API
  slug: open-adyen-companies-api
- collection_type: open
  name: API Collection
  slug: open-adyen-configuration-api
- collection_type: open
  name: Adyen Configuration Webhooks API
  slug: open-adyen-configuration-webhooks-api
- collection_type: open
  name: Adyen Account acceptDispute confirmThirdParty API
  slug: open-adyen-confirmthirdparty-api
- collection_type: open
  name: Adyen Account acceptDispute Cost API
  slug: open-adyen-cost-api
- collection_type: open
  name: Adyen Account acceptDispute createAccount API
  slug: open-adyen-createaccount-api
- collection_type: open
  name: Adyen Account acceptDispute createAccountHolder API
  slug: open-adyen-createaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute createNotificationConfiguration API
  slug: open-adyen-createnotificationconfiguration-api
- collection_type: open
  name: Adyen Account acceptDispute createPermit API
  slug: open-adyen-createpermit-api
- collection_type: open
  name: Adyen Account acceptDispute createTestCardRanges API
  slug: open-adyen-createtestcardranges-api
- collection_type: open
  name: Adyen Data Protection API
  slug: open-adyen-data-protection-api
- collection_type: open
  name: Adyen Account acceptDispute debitAccountHolder API
  slug: open-adyen-debitaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute declineThirdParty API
  slug: open-adyen-declinethirdparty-api
- collection_type: open
  name: Adyen Account acceptDispute defendDispute API
  slug: open-adyen-defenddispute-api
- collection_type: open
  name: Adyen Account acceptDispute deleteBankAccounts API
  slug: open-adyen-deletebankaccounts-api
- collection_type: open
  name: Adyen Account acceptDispute deleteDisputeDefenseDocument API
  slug: open-adyen-deletedisputedefensedocument-api
- collection_type: open
  name: Adyen Account acceptDispute deleteLegalArrangements API
  slug: open-adyen-deletelegalarrangements-api
- collection_type: open
  name: Adyen Account acceptDispute deleteNotificationConfigurations API
  slug: open-adyen-deletenotificationconfigurations-api
- collection_type: open
  name: Adyen Account acceptDispute deletePayoutMethods API
  slug: open-adyen-deletepayoutmethods-api
- collection_type: open
  name: Adyen Account acceptDispute deleteShareholders API
  slug: open-adyen-deleteshareholders-api
- collection_type: open
  name: Adyen Account acceptDispute deleteSignatories API
  slug: open-adyen-deletesignatories-api
- collection_type: open
  name: Adyen Account acceptDispute Diagnosis API
  slug: open-adyen-diagnosis-api
- collection_type: open
  name: Adyen Account acceptDispute Disable API
  slug: open-adyen-disable-api
- collection_type: open
  name: Adyen Account acceptDispute disablePermit API
  slug: open-adyen-disablepermit-api
- collection_type: open
  name: Adyen Account acceptDispute Display API
  slug: open-adyen-display-api
- collection_type: open
  name: Adyen Account acceptDispute Documents API
  slug: open-adyen-documents-api
- collection_type: open
  name: Adyen Account acceptDispute Donate API
  slug: open-adyen-donate-api
- collection_type: open
  name: Adyen Account acceptDispute Donations API
  slug: open-adyen-donations-api
- collection_type: open
  name: Adyen Account acceptDispute Enableservice API
  slug: open-adyen-enableservice-api
- collection_type: open
  name: Adyen Account acceptDispute Erasure API
  slug: open-adyen-erasure-api
- collection_type: open
  name: Adyen Account acceptDispute Estimates API
  slug: open-adyen-estimates-api
- collection_type: open
  name: Adyen Account acceptDispute findTerminal API
  slug: open-adyen-findterminal-api
- collection_type: open
  name: Adyen Account acceptDispute Forms API
  slug: open-adyen-forms-api
- collection_type: open
  name: Adyen Account acceptDispute get3dsAvailability API
  slug: open-adyen-get3dsavailability-api
- collection_type: open
  name: Adyen Account acceptDispute getAccountHolder API
  slug: open-adyen-getaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute getAuthenticationResult API
  slug: open-adyen-getauthenticationresult-api
- collection_type: open
  name: Adyen Account acceptDispute getCostEstimate API
  slug: open-adyen-getcostestimate-api
- collection_type: open
  name: Adyen Account acceptDispute getNotificationConfiguration API
  slug: open-adyen-getnotificationconfiguration-api
- collection_type: open
  name: Adyen Account acceptDispute getNotificationConfigurationList API
  slug: open-adyen-getnotificationconfigurationlist-api
- collection_type: open
  name: Adyen Account acceptDispute getOnboardingUrl API
  slug: open-adyen-getonboardingurl-api
- collection_type: open
  name: Adyen Account acceptDispute getPciQuestionnaireUrl API
  slug: open-adyen-getpciquestionnaireurl-api
- collection_type: open
  name: Adyen Account acceptDispute getStoresUnderAccount API
  slug: open-adyen-getstoresunderaccount-api
- collection_type: open
  name: Adyen Account acceptDispute getTaxForm API
  slug: open-adyen-gettaxform-api
- collection_type: open
  name: Adyen Account acceptDispute getTerminalDetails API
  slug: open-adyen-getterminaldetails-api
- collection_type: open
  name: Adyen Account acceptDispute getTerminalsUnderAccount API
  slug: open-adyen-getterminalsunderaccount-api
- collection_type: open
  name: Adyen Account acceptDispute Gettotals API
  slug: open-adyen-gettotals-api
- collection_type: open
  name: Adyen Account acceptDispute getUploadedDocuments API
  slug: open-adyen-getuploadeddocuments-api
- collection_type: open
  name: Adyen Account acceptDispute grantAccounts API
  slug: open-adyen-grantaccounts-api
- collection_type: open
  name: Adyen Account acceptDispute grantOffers API
  slug: open-adyen-grantoffers-api
- collection_type: open
  name: Adyen Account acceptDispute Grants API
  slug: open-adyen-grants-api
- collection_type: open
  name: Adyen Account acceptDispute Holders API
  slug: open-adyen-holders-api
- collection_type: open
  name: Adyen Account acceptDispute Identification API
  slug: open-adyen-identification-api
- collection_type: open
  name: Adyen Account acceptDispute Input API
  slug: open-adyen-input-api
- collection_type: open
  name: Adyen Account acceptDispute Instruments API
  slug: open-adyen-instruments-api
- collection_type: open
  name: Adyen Account acceptDispute Issue API
  slug: open-adyen-issue-api
- collection_type: open
  name: Adyen Account acceptDispute Items API
  slug: open-adyen-items-api
- collection_type: open
  name: Adyen Account acceptDispute Keys API
  slug: open-adyen-keys-api
- collection_type: open
  name: Adyen Account acceptDispute Legal API
  slug: open-adyen-legal-api
- collection_type: open
  name: Adyen Account acceptDispute legalEntities API
  slug: open-adyen-legalentities-api
- collection_type: open
  name: Adyen Account acceptDispute Links API
  slug: open-adyen-links-api
- collection_type: open
  name: Adyen Account acceptDispute listRecurringDetails API
  slug: open-adyen-listrecurringdetails-api
- collection_type: open
  name: Adyen Account acceptDispute Load API
  slug: open-adyen-load-api
- collection_type: open
  name: Adyen Account acceptDispute Login API
  slug: open-adyen-login-api
- collection_type: open
  name: Adyen Account acceptDispute Logout API
  slug: open-adyen-logout-api
- collection_type: open
  name: Adyen Account acceptDispute Loyalty API
  slug: open-adyen-loyalty-api
- collection_type: open
  name: Adyen Account acceptDispute Me API
  slug: open-adyen-me-api
- collection_type: open
  name: Adyen Account acceptDispute Merchants API
  slug: open-adyen-merchants-api
- collection_type: open
  name: Adyen Account acceptDispute mergeBalance API
  slug: open-adyen-mergebalance-api
- collection_type: open
  name: Adyen Account acceptDispute Method API
  slug: open-adyen-method-api
- collection_type: open
  name: Adyen Account acceptDispute Methods API
  slug: open-adyen-methods-api
- collection_type: open
  name: Adyen Account acceptDispute Network API
  slug: open-adyen-network-api
- collection_type: open
  name: Adyen Account acceptDispute Networks API
  slug: open-adyen-networks-api
- collection_type: open
  name: Adyen Account acceptDispute networkTokens API
  slug: open-adyen-networktokens-api
- collection_type: open
  name: Adyen Account acceptDispute notifyShopper API
  slug: open-adyen-notifyshopper-api
- collection_type: open
  name: Adyen Account acceptDispute Offer API
  slug: open-adyen-offer-api
- collection_type: open
  name: Adyen Account acceptDispute Offers API
  slug: open-adyen-offers-api
- collection_type: open
  name: Adyen Account acceptDispute Orders API
  slug: open-adyen-orders-api
- collection_type: open
  name: Adyen Account acceptDispute Origin API
  slug: open-adyen-origin-api
- collection_type: open
  name: Adyen Account acceptDispute originKeys API
  slug: open-adyen-originkeys-api
- collection_type: open
  name: Adyen Account acceptDispute Pay API
  slug: open-adyen-pay-api
- collection_type: open
  name: Adyen Account acceptDispute Payment API
  slug: open-adyen-payment-api
- collection_type: open
  name: Adyen Account acceptDispute paymentInstrumentGroups API
  slug: open-adyen-paymentinstrumentgroups-api
- collection_type: open
  name: Adyen Account acceptDispute paymentInstruments API
  slug: open-adyen-paymentinstruments-api
- collection_type: open
  name: Adyen Account acceptDispute paymentLinks API
  slug: open-adyen-paymentlinks-api
- collection_type: open
  name: Adyen Account acceptDispute paymentMethods API
  slug: open-adyen-paymentmethods-api
- collection_type: open
  name: Adyen Account acceptDispute Payments API
  slug: open-adyen-payments-api
- collection_type: open
  name: Adyen Account acceptDispute paymentSession API
  slug: open-adyen-paymentsession-api
- collection_type: open
  name: Adyen Account acceptDispute Payout API
  slug: open-adyen-payout-api
- collection_type: open
  name: Adyen Account acceptDispute payoutAccountHolder API
  slug: open-adyen-payoutaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute Pins API
  slug: open-adyen-pins-api
- collection_type: open
  name: Adyen Account acceptDispute Platforms API
  slug: open-adyen-platforms-api
- collection_type: open
  name: Adyen Account acceptDispute Print API
  slug: open-adyen-print-api
- collection_type: open
  name: Adyen Account acceptDispute Psp API
  slug: open-adyen-psp-api
- collection_type: open
  name: Adyen Account acceptDispute Public API
  slug: open-adyen-public-api
- collection_type: open
  name: Adyen Account acceptDispute Reconciliation API
  slug: open-adyen-reconciliation-api
- collection_type: open
  name: Adyen Account acceptDispute References API
  slug: open-adyen-references-api
- collection_type: open
  name: Adyen Account acceptDispute Refund API
  slug: open-adyen-refund-api
- collection_type: open
  name: Adyen Account acceptDispute refundFundsTransfer API
  slug: open-adyen-refundfundstransfer-api
- collection_type: open
  name: Adyen Account acceptDispute refundNotPaidOutTransfers API
  slug: open-adyen-refundnotpaidouttransfers-api
- collection_type: open
  name: Adyen Account acceptDispute Refunds API
  slug: open-adyen-refunds-api
- collection_type: open
  name: Adyen Account acceptDispute Request API
  slug: open-adyen-request-api
- collection_type: open
  name: Adyen Account acceptDispute requestSubjectErasure API
  slug: open-adyen-requestsubjecterasure-api
- collection_type: open
  name: Adyen Account acceptDispute Results API
  slug: open-adyen-results-api
- collection_type: open
  name: Adyen Account acceptDispute retrieve3ds2Result API
  slug: open-adyen-retrieve3ds2result-api
- collection_type: open
  name: Adyen Account acceptDispute retrieveApplicableDefenseReasons API
  slug: open-adyen-retrieveapplicabledefensereasons-api
- collection_type: open
  name: Adyen Account acceptDispute Reveal API
  slug: open-adyen-reveal-api
- collection_type: open
  name: Adyen Account acceptDispute Reversal API
  slug: open-adyen-reversal-api
- collection_type: open
  name: Adyen Account acceptDispute Reversals API
  slug: open-adyen-reversals-api
- collection_type: open
  name: Adyen Account acceptDispute Routes API
  slug: open-adyen-routes-api
- collection_type: open
  name: Adyen Account acceptDispute Rules API
  slug: open-adyen-rules-api
- collection_type: open
  name: Adyen Account acceptDispute scheduleAccountUpdater API
  slug: open-adyen-scheduleaccountupdater-api
- collection_type: open
  name: Adyen Account acceptDispute Session API
  slug: open-adyen-session-api
- collection_type: open
  name: Adyen Account acceptDispute Sessions API
  slug: open-adyen-sessions-api
- collection_type: open
  name: Adyen Account acceptDispute setupBeneficiary API
  slug: open-adyen-setupbeneficiary-api
- collection_type: open
  name: Adyen Account acceptDispute Shareholders API
  slug: open-adyen-shareholders-api
- collection_type: open
  name: Adyen Account acceptDispute Signatories API
  slug: open-adyen-signatories-api
- collection_type: open
  name: Adyen Account acceptDispute State API
  slug: open-adyen-state-api
- collection_type: open
  name: Adyen Account acceptDispute Stored API
  slug: open-adyen-stored-api
- collection_type: open
  name: Adyen Account acceptDispute storeDetail API
  slug: open-adyen-storedetail-api
- collection_type: open
  name: Adyen Account acceptDispute storeDetailAndSubmitThirdParty API
  slug: open-adyen-storedetailandsubmitthirdparty-api
- collection_type: open
  name: Adyen Account acceptDispute storedPaymentMethods API
  slug: open-adyen-storedpaymentmethods-api
- collection_type: open
  name: Adyen Account acceptDispute Storedvalue API
  slug: open-adyen-storedvalue-api
- collection_type: open
  name: Adyen Account acceptDispute Stores API
  slug: open-adyen-stores-api
- collection_type: open
  name: Adyen Account acceptDispute Subjects API
  slug: open-adyen-subjects-api
- collection_type: open
  name: Adyen Account acceptDispute submitThirdParty API
  slug: open-adyen-submitthirdparty-api
- collection_type: open
  name: Adyen Account acceptDispute supplyDefenseDocument API
  slug: open-adyen-supplydefensedocument-api
- collection_type: open
  name: Adyen Account acceptDispute Suspend API
  slug: open-adyen-suspend-api
- collection_type: open
  name: Adyen Account acceptDispute suspendAccountHolder API
  slug: open-adyen-suspendaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute Sweep API
  slug: open-adyen-sweep-api
- collection_type: open
  name: Adyen Account acceptDispute Sweeps API
  slug: open-adyen-sweeps-api
- collection_type: open
  name: Adyen Account acceptDispute Tax API
  slug: open-adyen-tax-api
- collection_type: open
  name: Adyen Account acceptDispute technicalCancel API
  slug: open-adyen-technicalcancel-api
- collection_type: open
  name: Adyen Account acceptDispute Terminals API
  slug: open-adyen-terminals-api
- collection_type: open
  name: Adyen Account acceptDispute testNotificationConfiguration API
  slug: open-adyen-testnotificationconfiguration-api
- collection_type: open
  name: Adyen Account acceptDispute Themes API
  slug: open-adyen-themes-api
- collection_type: open
  name: Adyen Account acceptDispute Token API
  slug: open-adyen-token-api
- collection_type: open
  name: Adyen Account acceptDispute Tokens API
  slug: open-adyen-tokens-api
- collection_type: open
  name: Adyen Account acceptDispute Transaction API
  slug: open-adyen-transaction-api
- collection_type: open
  name: Adyen Account acceptDispute transactionRules API
  slug: open-adyen-transactionrules-api
- collection_type: open
  name: Adyen Account acceptDispute Transactions API
  slug: open-adyen-transactions-api
- collection_type: open
  name: Adyen Account acceptDispute Transactionstatus API
  slug: open-adyen-transactionstatus-api
- collection_type: open
  name: Adyen Account acceptDispute transferFunds API
  slug: open-adyen-transferfunds-api
- collection_type: open
  name: Adyen Account acceptDispute transferInstruments API
  slug: open-adyen-transferinstruments-api
- collection_type: open
  name: Adyen Account acceptDispute transferRoutes API
  slug: open-adyen-transferroutes-api
- collection_type: open
  name: Adyen Account acceptDispute Transfers API
  slug: open-adyen-transfers-api
- collection_type: open
  name: Adyen Account acceptDispute unSuspendAccountHolder API
  slug: open-adyen-unsuspendaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute updateAccount API
  slug: open-adyen-updateaccount-api
- collection_type: open
  name: Adyen Account acceptDispute updateAccountHolder API
  slug: open-adyen-updateaccountholder-api
- collection_type: open
  name: Adyen Account acceptDispute updateAccountHolderState API
  slug: open-adyen-updateaccountholderstate-api
- collection_type: open
  name: Adyen Account acceptDispute updateNotificationConfiguration API
  slug: open-adyen-updatenotificationconfiguration-api
- collection_type: open
  name: Adyen Account acceptDispute uploadDocument API
  slug: open-adyen-uploaddocument-api
- collection_type: open
  name: Adyen Account acceptDispute Uploaded API
  slug: open-adyen-uploaded-api
- collection_type: open
  name: Adyen Account acceptDispute Uploads API
  slug: open-adyen-uploads-api
- collection_type: open
  name: Adyen Account acceptDispute Validate API
  slug: open-adyen-validate-api
- collection_type: open
  name: Adyen Account acceptDispute validateBankAccountIdentification API
  slug: open-adyen-validatebankaccountidentification-api
- collection_type: open
  name: Adyen Account acceptDispute voidPendingRefund API
  slug: open-adyen-voidpendingrefund-api
- collection_type: open
  name: Adyen Account acceptDispute voidTransaction API
  slug: open-adyen-voidtransaction-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/adyen-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adyen-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/adyen-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adyen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adyen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adyen-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/adyen-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adyen-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adyen-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/adyen-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adyen-data-model.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/adyen-decline-codes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adyen/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-checkout-payment-and-amount-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-checkout-payment-and-cancel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-checkout-payment-and-capture-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-checkout-payment-and-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-checkout-payment-and-reverse-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-checkout-session-create-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-classic-authorise-and-cancel-or-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-classic-authorise-and-cancel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-classic-authorise-and-capture-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-classic-authorise-and-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-management-merchant-create-and-activate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-management-payment-method-add-and-get-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-management-webhook-create-hmac-and-test-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-payment-link-create-and-expire-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-payment-link-create-and-get-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-payout-store-submit-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adyen-recurring-list-and-disable-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adyen
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adyen.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adyen.com/policies-and-disclaimer/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: https://docs.adyen.com/development-resources/api-credentials
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adyen.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adyen.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adyen.com/get-started-with-adyen/
- group: company
  title: ''
  type: Blog
  url: https://www.adyen.com/knowledge-hub
- group: start
  title: ''
  type: Login
  url: https://authn-live.adyen.com/authn/ui/login
- group: start
  title: ''
  type: Sandbox
  url: https://ca-test.adyen.com
- group: operate
  title: ''
  type: Support
  url: https://help.adyen.com/en_US
- group: operate
  title: ''
  type: Contact
  url: https://help.adyen.com/en_US/contact
- group: learn
  title: ''
  type: Webinars
  url: https://help.adyen.com/en_US/academy/webinars
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adyen.com
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.adyen.com/development-resources/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Adyen
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Adyen/adyen-openapi
- group: company
  title: ''
  type: Newsletter
  url: https://www.adyen.com/newsletter
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/adyen
- group: build
  title: Web SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-web
- group: build
  title: iOS SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-ios
- group: build
  title: Android SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-android
- group: build
  title: React Native SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-react-native
- group: build
  title: Flutter SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-flutter
- group: build
  title: PHP SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-php-api-library
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-java-api-library
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-node-api-library
- group: build
  title: .NET SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-dotnet-api-library
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-go-api-library
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-python-api-library
- group: build
  title: Ruby SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-ruby-api-library
- group: build
  title: Apex SDK
  type: SDKs
  url: https://github.com/Adyen/adyen-apex-api-library
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/Adyen/adyen-mcp
- group: build
  title: Postman Collection
  type: Tools
  url: https://github.com/Adyen/adyen-postman
- group: design
  title: ''
  type: SpectralRules
  url: rules/adyen-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/adyen-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Adyen/adyen-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.adyen.com/llms.txt
created: '2023-11-13'
description: Adyen is a global payment company that provides businesses with a single platform to accept payments from customers worldwide. Their technology enables companies to accept a wide range of payment methods, including credit cards, digital wallets, and local payment methods, in multiple currencies and countries. Adyen also offers services such as fraud prevention, data analytics, and optimization tools to help businesses streamline their payment processes and improve their overall performance.
examples:
- key_count: 2
  name: Accounting Notifications Additional Bank Identification Example
  slug: accounting-notifications-additional-bank-identification-example
- key_count: 6
  name: Accounting Notifications Address 2 Example
  slug: accounting-notifications-address-2-example
- key_count: 3
  name: Accounting Notifications Amount Adjustment Example
  slug: accounting-notifications-amount-adjustment-example
- key_count: 2
  name: Accounting Notifications Amount Example
  slug: accounting-notifications-amount-example
- key_count: 3
  name: Accounting Notifications Au Local Account Identification Example
  slug: accounting-notifications-au-local-account-identification-example
- key_count: 4
  name: Accounting Notifications Balance Mutation Example
  slug: accounting-notifications-balance-mutation-example
- key_count: 1
  name: Accounting Notifications Balance Platform Notification Response Example
  slug: accounting-notifications-balance-platform-notification-response-example
- key_count: 2
  name: Accounting Notifications Bank Account V3 Example
  slug: accounting-notifications-bank-account-v3-example
- key_count: 4
  name: Accounting Notifications Br Local Account Identification Example
  slug: accounting-notifications-br-local-account-identification-example
- key_count: 4
  name: Accounting Notifications Ca Local Account Identification Example
  slug: accounting-notifications-ca-local-account-identification-example
- key_count: 4
  name: Accounting Notifications Counterparty V3 Example
  slug: accounting-notifications-counterparty-v3-example
- key_count: 3
  name: Accounting Notifications Cz Local Account Identification Example
  slug: accounting-notifications-cz-local-account-identification-example
- key_count: 3
  name: Accounting Notifications Dk Local Account Identification Example
  slug: accounting-notifications-dk-local-account-identification-example
- key_count: 2
  name: Accounting Notifications Hu Local Account Identification Example
  slug: accounting-notifications-hu-local-account-identification-example
- key_count: 2
  name: Accounting Notifications Iban Account Identification Example
  slug: accounting-notifications-iban-account-identification-example
- key_count: 4
  name: Accounting Notifications Merchant Data Example
  slug: accounting-notifications-merchant-data-example
- key_count: 6
  name: Accounting Notifications Name Location Example
  slug: accounting-notifications-name-location-example
- key_count: 2
  name: Accounting Notifications No Local Account Identification Example
  slug: accounting-notifications-no-local-account-identification-example
- key_count: 4
  name: Accounting Notifications Number And Bic Account Identification Example
  slug: accounting-notifications-number-and-bic-account-identification-example
- key_count: 5
  name: Accounting Notifications Party Identification 2 Example
  slug: accounting-notifications-party-identification-2-example
- key_count: 4
  name: Accounting Notifications Payment Instrument Example
  slug: accounting-notifications-payment-instrument-example
- key_count: 2
  name: Accounting Notifications Pl Local Account Identification Example
  slug: accounting-notifications-pl-local-account-identification-example
- key_count: 2
  name: Accounting Notifications Relayed Authorisation Data 2 Example
  slug: accounting-notifications-relayed-authorisation-data-2-example
- key_count: 3
  name: Accounting Notifications Resource Example
  slug: accounting-notifications-resource-example
- key_count: 3
  name: Accounting Notifications Resource Reference Example
  slug: accounting-notifications-resource-reference-example
- key_count: 3
  name: Accounting Notifications Se Local Account Identification Example
  slug: accounting-notifications-se-local-account-identification-example
- key_count: 3
  name: Accounting Notifications Sg Local Account Identification Example
  slug: accounting-notifications-sg-local-account-identification-example
- key_count: 3
  name: Accounting Notifications Transaction Event Violation Example
  slug: accounting-notifications-transaction-event-violation-example
- key_count: 3
  name: Accounting Notifications Transaction Rule Reference Example
  slug: accounting-notifications-transaction-rule-reference-example
- key_count: 2
  name: Accounting Notifications Transaction Rule Source Example
  slug: accounting-notifications-transaction-rule-source-example
- key_count: 4
  name: Accounting Notifications Transaction Rules Result Example
  slug: accounting-notifications-transaction-rules-result-example
- key_count: 11
  name: Accounting Notifications Transfer Event Example
  slug: accounting-notifications-transfer-event-example
- key_count: 31
  name: Accounting Notifications Transfer Notification Data Example
  slug: accounting-notifications-transfer-notification-data-example
- key_count: 3
  name: Accounting Notifications Transfer Notification Request Example
  slug: accounting-notifications-transfer-notification-request-example
- key_count: 1
  name: Accounting Notifications Transfer Notification Transfer Tracking Example
  slug: accounting-notifications-transfer-notification-transfer-tracking-example
- key_count: 2
  name: Accounting Notifications Transfer Notification Validation Fact Example
  slug: accounting-notifications-transfer-notification-validation-fact-example
- key_count: 3
  name: Accounting Notifications Uk Local Account Identification Example
  slug: accounting-notifications-uk-local-account-identification-example
- key_count: 4
  name: Accounting Notifications Us Local Account Identification Example
  slug: accounting-notifications-us-local-account-identification-example
- key_count: 3
  name: Accounts Account Event Example
  slug: accounts-account-event-example
- key_count: 10
  name: Accounts Account Example
  slug: accounts-account-example
- key_count: 15
  name: Accounts Account Holder Details Example
  slug: accounts-account-holder-details-example
- key_count: 5
  name: Accounts Account Holder Status Example
  slug: accounts-account-holder-status-example
- key_count: 6
  name: Accounts Account Payout State Example
  slug: accounts-account-payout-state-example
- key_count: 5
  name: Accounts Account Processing State Example
  slug: accounts-account-processing-state-example
- key_count: 2
  name: Accounts Amount Example
  slug: accounts-amount-example
- key_count: 26
  name: Accounts Bank Account Detail Example
  slug: accounts-bank-account-detail-example
- key_count: 10
  name: Accounts Business Details Example
  slug: accounts-business-details-example
- key_count: 1
  name: Accounts Close Account Holder Request Example
  slug: accounts-close-account-holder-request-example
- key_count: 4
  name: Accounts Close Account Holder Response Example
  slug: accounts-close-account-holder-response-example
- key_count: 1
  name: Accounts Close Account Request Example
  slug: accounts-close-account-request-example
- key_count: 5
  name: Accounts Close Account Response Example
  slug: accounts-close-account-response-example
- key_count: 2
  name: Accounts Close Stores Request Example
  slug: accounts-close-stores-request-example
- key_count: 8
  name: Accounts Create Account Holder Request Example
  slug: accounts-create-account-holder-request-example
- key_count: 12
  name: Accounts Create Account Holder Response Example
  slug: accounts-create-account-holder-response-example
- key_count: 8
  name: Accounts Create Account Request Example
  slug: accounts-create-account-request-example
- key_count: 12
  name: Accounts Create Account Response Example
  slug: accounts-create-account-response-example
- key_count: 2
  name: Accounts Delete Bank Account Request Example
  slug: accounts-delete-bank-account-request-example
- key_count: 2
  name: Accounts Delete Legal Arrangement Request Example
  slug: accounts-delete-legal-arrangement-request-example
- key_count: 2
  name: Accounts Delete Payout Method Request Example
  slug: accounts-delete-payout-method-request-example
- key_count: 2
  name: Accounts Delete Shareholder Request Example
  slug: accounts-delete-shareholder-request-example
- key_count: 2
  name: Accounts Delete Signatories Request Example
  slug: accounts-delete-signatories-request-example
- key_count: 9
  name: Accounts Document Detail Example
  slug: accounts-document-detail-example
- key_count: 3
  name: Accounts Error Field Type Example
  slug: accounts-error-field-type-example
- key_count: 3
  name: Accounts Field Type Example
  slug: accounts-field-type-example
- key_count: 3
  name: Accounts Generic Response Example
  slug: accounts-generic-response-example
- key_count: 3
  name: Accounts Get Account Holder Request Example
  slug: accounts-get-account-holder-request-example
- key_count: 14
  name: Accounts Get Account Holder Response Example
  slug: accounts-get-account-holder-response-example
- key_count: 5
  name: Accounts Get Account Holder Status Response Example
  slug: accounts-get-account-holder-status-response-example
- key_count: 3
  name: Accounts Get Tax Form Request Example
  slug: accounts-get-tax-form-request-example
- key_count: 5
  name: Accounts Get Tax Form Response Example
  slug: accounts-get-tax-form-response-example
- key_count: 3
  name: Accounts Get Uploaded Documents Request Example
  slug: accounts-get-uploaded-documents-request-example
- key_count: 4
  name: Accounts Get Uploaded Documents Response Example
  slug: accounts-get-uploaded-documents-response-example
- key_count: 2
  name: Accounts Individual Details Example
  slug: accounts-individual-details-example
- key_count: 1
  name: Accounts Kyc Check Result Example
  slug: accounts-kyc-check-result-example
- key_count: 4
  name: Accounts Kyc Check Status Data Example
  slug: accounts-kyc-check-status-data-example
- key_count: 2
  name: Accounts Kyc Check Summary Example
  slug: accounts-kyc-check-summary-example
- key_count: 2
  name: Accounts Kyc Legal Arrangement Check Result Example
  slug: accounts-kyc-legal-arrangement-check-result-example
- key_count: 3
  name: Accounts Kyc Legal Arrangement Entity Check Result Example
  slug: accounts-kyc-legal-arrangement-entity-check-result-example
- key_count: 2
  name: Accounts Kyc Payout Method Check Result Example
  slug: accounts-kyc-payout-method-check-result-example
- key_count: 4
  name: Accounts Kyc Shareholder Check Result Example
  slug: accounts-kyc-shareholder-check-result-example
- key_count: 2
  name: Accounts Kyc Signatory Check Result Example
  slug: accounts-kyc-signatory-check-result-example
- key_count: 2
  name: Accounts Kyc Ultimate Parent Company Check Result Example
  slug: accounts-kyc-ultimate-parent-company-check-result-example
- key_count: 7
  name: Accounts Kyc Verification Result Example
  slug: accounts-kyc-verification-result-example
- key_count: 9
  name: Accounts Legal Arrangement Detail Example
  slug: accounts-legal-arrangement-detail-example
- key_count: 11
  name: Accounts Legal Arrangement Entity Detail Example
  slug: accounts-legal-arrangement-entity-detail-example
- key_count: 2
  name: Accounts Legal Arrangement Request Example
  slug: accounts-legal-arrangement-request-example
- key_count: 2
  name: Accounts Migrated Accounts Example
  slug: accounts-migrated-accounts-example
- key_count: 2
  name: Accounts Migrated Shareholders Example
  slug: accounts-migrated-shareholders-example
- key_count: 4
  name: Accounts Migrated Stores Example
  slug: accounts-migrated-stores-example
- key_count: 7
  name: Accounts Migration Data Example
  slug: accounts-migration-data-example
- key_count: 5
  name: Accounts Payout Method Example
  slug: accounts-payout-method-example
- key_count: 2
  name: Accounts Payout Schedule Response Example
  slug: accounts-payout-schedule-response-example
- key_count: 3
  name: Accounts Perform Verification Request Example
  slug: accounts-perform-verification-request-example
- key_count: 5
  name: Accounts Personal Document Data Example
  slug: accounts-personal-document-data-example
- key_count: 11
  name: Accounts Shareholder Contact Example
  slug: accounts-shareholder-contact-example
- key_count: 10
  name: Accounts Signatory Contact Example
  slug: accounts-signatory-contact-example
- key_count: 15
  name: Accounts Store Detail Example
  slug: accounts-store-detail-example
- key_count: 1
  name: Accounts Suspend Account Holder Request Example
  slug: accounts-suspend-account-holder-request-example
- key_count: 4
  name: Accounts Suspend Account Holder Response Example
  slug: accounts-suspend-account-holder-response-example
- key_count: 5
  name: Accounts Ultimate Parent Company Business Details Example
  slug: accounts-ultimate-parent-company-business-details-example
- key_count: 3
  name: Accounts Ultimate Parent Company Example
  slug: accounts-ultimate-parent-company-example
- key_count: 1
  name: Accounts Un Suspend Account Holder Request Example
  slug: accounts-un-suspend-account-holder-request-example
- key_count: 4
  name: Accounts Un Suspend Account Holder Response Example
  slug: accounts-un-suspend-account-holder-response-example
- key_count: 7
  name: Accounts Update Account Holder Request Example
  slug: accounts-update-account-holder-request-example
- key_count: 11
  name: Accounts Update Account Holder Response Example
  slug: accounts-update-account-holder-response-example
- key_count: 4
  name: Accounts Update Account Holder State Request Example
  slug: accounts-update-account-holder-state-request-example
- key_count: 7
  name: Accounts Update Account Request Example
  slug: accounts-update-account-request-example
- key_count: 10
  name: Accounts Update Account Response Example
  slug: accounts-update-account-response-example
- key_count: 3
  name: Accounts Update Payout Schedule Request Example
  slug: accounts-update-payout-schedule-request-example
- key_count: 2
  name: Accounts Upload Document Request Example
  slug: accounts-upload-document-request-example
- key_count: 6
  name: Accounts Vias Address Example
  slug: accounts-vias-address-example
- key_count: 4
  name: Accounts Vias Name Example
  slug: accounts-vias-name-example
- key_count: 3
  name: Accounts Vias Personal Data Example
  slug: accounts-vias-personal-data-example
- key_count: 3
  name: Accounts Vias Phone Number Example
  slug: accounts-vias-phone-number-example
- key_count: 6
  name: Adyen Delete Businesslines Id Example
  slug: adyen-delete-businesslines-id-example
- key_count: 6
  name: Adyen Delete Companies Companyid Apicredentials Apicredentialid Al Example
  slug: adyen-delete-companies-companyid-apicredentials-apicredentialid-al-example
- key_count: 6
  name: Adyen Delete Companies Companyid Webhooks Webhookid Example
  slug: adyen-delete-companies-companyid-webhooks-webhookid-example
- key_count: 6
  name: Adyen Delete Documents Id Example
  slug: adyen-delete-documents-id-example
- key_count: 6
  name: Adyen Delete Me Allowedorigins Originid Example
  slug: adyen-delete-me-allowedorigins-originid-example
- key_count: 6
  name: Adyen Delete Merchants Merchantid Apicredentials Apicredentialid A Example
  slug: adyen-delete-merchants-merchantid-apicredentials-apicredentialid-a-example
- key_count: 6
  name: Adyen Delete Merchants Merchantid Payoutsettings Payoutsettingsid Example
  slug: adyen-delete-merchants-merchantid-payoutsettings-payoutsettingsid-example
- key_count: 6
  name: Adyen Delete Merchants Merchantid Splitconfigurations Splitconfigu Example
  slug: adyen-delete-merchants-merchantid-splitconfigurations-splitconfigu-example
- key_count: 6
  name: Adyen Delete Merchants Merchantid Webhooks Webhookid Example
  slug: adyen-delete-merchants-merchantid-webhooks-webhookid-example
- key_count: 6
  name: Adyen Delete Transferinstruments Id Example
  slug: adyen-delete-transferinstruments-id-example
- key_count: 6
  name: Adyen Get Businesslines Id Example
  slug: adyen-get-businesslines-id-example
- key_count: 6
  name: Adyen Get Companies Companyid Androidapps Example
  slug: adyen-get-companies-companyid-androidapps-example
- key_count: 6
  name: Adyen Get Companies Companyid Androidapps Id Example
  slug: adyen-get-companies-companyid-androidapps-id-example
- key_count: 6
  name: Adyen Get Companies Companyid Androidcertificates Example
  slug: adyen-get-companies-companyid-androidcertificates-example
- key_count: 6
  name: Adyen Get Companies Companyid Apicredentials Apicredentialid Allow Example
  slug: adyen-get-companies-companyid-apicredentials-apicredentialid-allow-example
- key_count: 6
  name: Adyen Get Companies Companyid Apicredentials Apicredentialid Example
  slug: adyen-get-companies-companyid-apicredentials-apicredentialid-example
- key_count: 6
  name: Adyen Get Companies Companyid Apicredentials Example
  slug: adyen-get-companies-companyid-apicredentials-example
- key_count: 6
  name: Adyen Get Companies Companyid Billingentities Example
  slug: adyen-get-companies-companyid-billingentities-example
- key_count: 6
  name: Adyen Get Companies Companyid Example
  slug: adyen-get-companies-companyid-example
- key_count: 6
  name: Adyen Get Companies Companyid Merchants Example
  slug: adyen-get-companies-companyid-merchants-example
- key_count: 6
  name: Adyen Get Companies Companyid Shippinglocations Example
  slug: adyen-get-companies-companyid-shippinglocations-example
- key_count: 6
  name: Adyen Get Companies Companyid Terminalactions Actionid Example
  slug: adyen-get-companies-companyid-terminalactions-actionid-example
- key_count: 6
  name: Adyen Get Companies Companyid Terminalactions Example
  slug: adyen-get-companies-companyid-terminalactions-example
- key_count: 6
  name: Adyen Get Companies Companyid Terminallogos Example
  slug: adyen-get-companies-companyid-terminallogos-example
- key_count: 6
  name: Adyen Get Companies Companyid Terminalmodels Example
  slug: adyen-get-companies-companyid-terminalmodels-example
- key_count: 6
  name: Adyen Get Companies Companyid Terminalorders Example
  slug: adyen-get-companies-companyid-terminalorders-example
- key_count: 6
  name: Adyen Get Companies Companyid Terminalorders Orderid Example
  slug: adyen-get-companies-companyid-terminalorders-orderid-example
- key_count: 6
  name: Adyen Get Companies Companyid Terminalproducts Example
  slug: adyen-get-companies-companyid-terminalproducts-example
- key_count: 6
  name: Adyen Get Companies Companyid Terminalsettings Example
  slug: adyen-get-companies-companyid-terminalsettings-example
- key_count: 6
  name: Adyen Get Companies Companyid Users Example
  slug: adyen-get-companies-companyid-users-example
- key_count: 6
  name: Adyen Get Companies Companyid Users Userid Example
  slug: adyen-get-companies-companyid-users-userid-example
- key_count: 6
  name: Adyen Get Companies Companyid Webhooks Example
  slug: adyen-get-companies-companyid-webhooks-example
- key_count: 6
  name: Adyen Get Companies Companyid Webhooks Webhookid Example
  slug: adyen-get-companies-companyid-webhooks-webhookid-example
- key_count: 6
  name: Adyen Get Companies Example
  slug: adyen-get-companies-example
- key_count: 6
  name: Adyen Get Documents Id Example
  slug: adyen-get-documents-id-example
- key_count: 6
  name: Adyen Get Grantaccounts Id Example
  slug: adyen-get-grantaccounts-id-example
- key_count: 6
  name: Adyen Get Grantoffers Example
  slug: adyen-get-grantoffers-example
- key_count: 6
  name: Adyen Get Grantoffers Grantofferid Example
  slug: adyen-get-grantoffers-grantofferid-example
- key_count: 6
  name: Adyen Get Grants Example
  slug: adyen-get-grants-example
- key_count: 6
  name: Adyen Get Grants Id Example
  slug: adyen-get-grants-id-example
- key_count: 6
  name: Adyen Get Legalentities Id Businesslines Example
  slug: adyen-get-legalentities-id-businesslines-example
- key_count: 6
  name: Adyen Get Legalentities Id Example
  slug: adyen-get-legalentities-id-example
- key_count: 6
  name: Adyen Get Legalentities Id Pciquestionnaires Example
  slug: adyen-get-legalentities-id-pciquestionnaires-example
- key_count: 6
  name: Adyen Get Legalentities Id Pciquestionnaires Pciid Example
  slug: adyen-get-legalentities-id-pciquestionnaires-pciid-example
- key_count: 6
  name: Adyen Get Legalentities Id Termsofserviceacceptanceinfos Example
  slug: adyen-get-legalentities-id-termsofserviceacceptanceinfos-example
- key_count: 6
  name: Adyen Get Legalentities Id Termsofservicestatus Example
  slug: adyen-get-legalentities-id-termsofservicestatus-example
- key_count: 6
  name: Adyen Get Me Allowedorigins Example
  slug: adyen-get-me-allowedorigins-example
- key_count: 6
  name: Adyen Get Me Allowedorigins Originid Example
  slug: adyen-get-me-allowedorigins-originid-example
- key_count: 6
  name: Adyen Get Me Example
  slug: adyen-get-me-example
- key_count: 6
  name: Adyen Get Merchants Example
  slug: adyen-get-merchants-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Apicredentials Apicredentialid Allo Example
  slug: adyen-get-merchants-merchantid-apicredentials-apicredentialid-allo-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Apicredentials Apicredentialid Example
  slug: adyen-get-merchants-merchantid-apicredentials-apicredentialid-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Apicredentials Example
  slug: adyen-get-merchants-merchantid-apicredentials-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Billingentities Example
  slug: adyen-get-merchants-merchantid-billingentities-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Example
  slug: adyen-get-merchants-merchantid-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Paymentmethodsettings Example
  slug: adyen-get-merchants-merchantid-paymentmethodsettings-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Paymentmethodsettings Paymentmethod Example
  slug: adyen-get-merchants-merchantid-paymentmethodsettings-paymentmethod-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Payoutsettings Example
  slug: adyen-get-merchants-merchantid-payoutsettings-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Payoutsettings Payoutsettingsid Example
  slug: adyen-get-merchants-merchantid-payoutsettings-payoutsettingsid-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Shippinglocations Example
  slug: adyen-get-merchants-merchantid-shippinglocations-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Splitconfigurations Example
  slug: adyen-get-merchants-merchantid-splitconfigurations-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Splitconfigurations Splitconfigurat Example
  slug: adyen-get-merchants-merchantid-splitconfigurations-splitconfigurat-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Stores Example
  slug: adyen-get-merchants-merchantid-stores-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Stores Reference Terminallogos Example
  slug: adyen-get-merchants-merchantid-stores-reference-terminallogos-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Stores Reference Terminalsettings Example
  slug: adyen-get-merchants-merchantid-stores-reference-terminalsettings-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Stores Storeid Example
  slug: adyen-get-merchants-merchantid-stores-storeid-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Terminallogos Example
  slug: adyen-get-merchants-merchantid-terminallogos-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Terminalmodels Example
  slug: adyen-get-merchants-merchantid-terminalmodels-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Terminalorders Example
  slug: adyen-get-merchants-merchantid-terminalorders-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Terminalorders Orderid Example
  slug: adyen-get-merchants-merchantid-terminalorders-orderid-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Terminalproducts Example
  slug: adyen-get-merchants-merchantid-terminalproducts-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Terminalsettings Example
  slug: adyen-get-merchants-merchantid-terminalsettings-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Users Example
  slug: adyen-get-merchants-merchantid-users-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Users Userid Example
  slug: adyen-get-merchants-merchantid-users-userid-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Webhooks Example
  slug: adyen-get-merchants-merchantid-webhooks-example
- key_count: 6
  name: Adyen Get Merchants Merchantid Webhooks Webhookid Example
  slug: adyen-get-merchants-merchantid-webhooks-webhookid-example
- key_count: 6
  name: Adyen Get Networktokens Networktokenid Example
  slug: adyen-get-networktokens-networktokenid-example
- key_count: 6
  name: Adyen Get Paymentinstruments Id Networktokens Example
  slug: adyen-get-paymentinstruments-id-networktokens-example
- key_count: 6
  name: Adyen Get Pins Publickey Example
  slug: adyen-get-pins-publickey-example
- key_count: 6
  name: Adyen Get Stores Example
  slug: adyen-get-stores-example
- key_count: 6
  name: Adyen Get Stores Storeid Example
  slug: adyen-get-stores-storeid-example
- key_count: 6
  name: Adyen Get Stores Storeid Terminallogos Example
  slug: adyen-get-stores-storeid-terminallogos-example
- key_count: 6
  name: Adyen Get Stores Storeid Terminalsettings Example
  slug: adyen-get-stores-storeid-terminalsettings-example
- key_count: 6
  name: Adyen Get Terminals Example
  slug: adyen-get-terminals-example
- key_count: 6
  name: Adyen Get Terminals Terminalid Terminallogos Example
  slug: adyen-get-terminals-terminalid-terminallogos-example
- key_count: 6
  name: Adyen Get Terminals Terminalid Terminalsettings Example
  slug: adyen-get-terminals-terminalid-terminalsettings-example
- key_count: 6
  name: Adyen Get Themes Example
  slug: adyen-get-themes-example
- key_count: 6
  name: Adyen Get Themes Id Example
  slug: adyen-get-themes-id-example
- key_count: 6
  name: Adyen Get Transactions Example
  slug: adyen-get-transactions-example
- key_count: 6
  name: Adyen Get Transactions Id Example
  slug: adyen-get-transactions-id-example
- key_count: 6
  name: Adyen Get Transferinstruments Id Example
  slug: adyen-get-transferinstruments-id-example
- key_count: 6
  name: Adyen Patch Businesslines Id Example
  slug: adyen-patch-businesslines-id-example
- key_count: 6
  name: Adyen Patch Companies Companyid Apicredentials Apicredentialid Example
  slug: adyen-patch-companies-companyid-apicredentials-apicredentialid-example
- key_count: 6
  name: Adyen Patch Companies Companyid Terminallogos Example
  slug: adyen-patch-companies-companyid-terminallogos-example
- key_count: 6
  name: Adyen Patch Companies Companyid Terminalorders Orderid Example
  slug: adyen-patch-companies-companyid-terminalorders-orderid-example
- key_count: 6
  name: Adyen Patch Companies Companyid Terminalsettings Example
  slug: adyen-patch-companies-companyid-terminalsettings-example
- key_count: 6
  name: Adyen Patch Companies Companyid Users Userid Example
  slug: adyen-patch-companies-companyid-users-userid-example
- key_count: 6
  name: Adyen Patch Companies Companyid Webhooks Webhookid Example
  slug: adyen-patch-companies-companyid-webhooks-webhookid-example
- key_count: 6
  name: Adyen Patch Documents Id Example
  slug: adyen-patch-documents-id-example
- key_count: 6
  name: Adyen Patch Legalentities Id Example
  slug: adyen-patch-legalentities-id-example
- key_count: 6
  name: Adyen Patch Legalentities Id Termsofservice Termsofservicedocument Example
  slug: adyen-patch-legalentities-id-termsofservice-termsofservicedocument-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Apicredentials Apicredentialid Example
  slug: adyen-patch-merchants-merchantid-apicredentials-apicredentialid-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Paymentmethodsettings Paymentmeth Example
  slug: adyen-patch-merchants-merchantid-paymentmethodsettings-paymentmeth-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Payoutsettings Payoutsettingsid Example
  slug: adyen-patch-merchants-merchantid-payoutsettings-payoutsettingsid-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Splitconfigurations Splitconfigur Example
  slug: adyen-patch-merchants-merchantid-splitconfigurations-splitconfigur-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Stores Reference Terminallogos Example
  slug: adyen-patch-merchants-merchantid-stores-reference-terminallogos-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Stores Reference Terminalsettings Example
  slug: adyen-patch-merchants-merchantid-stores-reference-terminalsettings-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Stores Storeid Example
  slug: adyen-patch-merchants-merchantid-stores-storeid-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Terminallogos Example
  slug: adyen-patch-merchants-merchantid-terminallogos-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Terminalorders Orderid Example
  slug: adyen-patch-merchants-merchantid-terminalorders-orderid-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Terminalsettings Example
  slug: adyen-patch-merchants-merchantid-terminalsettings-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Users Userid Example
  slug: adyen-patch-merchants-merchantid-users-userid-example
- key_count: 6
  name: Adyen Patch Merchants Merchantid Webhooks Webhookid Example
  slug: adyen-patch-merchants-merchantid-webhooks-webhookid-example
- key_count: 6
  name: Adyen Patch Stores Storeid Example
  slug: adyen-patch-stores-storeid-example
- key_count: 6
  name: Adyen Patch Stores Storeid Terminallogos Example
  slug: adyen-patch-stores-storeid-terminallogos-example
- key_count: 6
  name: Adyen Patch Stores Storeid Terminalsettings Example
  slug: adyen-patch-stores-storeid-terminalsettings-example
- key_count: 6
  name: Adyen Patch Terminals Terminalid Terminallogos Example
  slug: adyen-patch-terminals-terminalid-terminallogos-example
- key_count: 6
  name: Adyen Patch Terminals Terminalid Terminalsettings Example
  slug: adyen-patch-terminals-terminalid-terminalsettings-example
- key_count: 6
  name: Adyen Patch Transferinstruments Id Example
  slug: adyen-patch-transferinstruments-id-example
- key_count: 6
  name: Adyen Post Acceptdispute Example
  slug: adyen-post-acceptdispute-example
- key_count: 6
  name: Adyen Post Accountholderbalance Example
  slug: adyen-post-accountholderbalance-example
- key_count: 6
  name: Adyen Post Accountholdertransactionlist Example
  slug: adyen-post-accountholdertransactionlist-example
- key_count: 6
  name: Adyen Post Adjustauthorisation Example
  slug: adyen-post-adjustauthorisation-example
- key_count: 6
  name: Adyen Post Admin Example
  slug: adyen-post-admin-example
- key_count: 6
  name: Adyen Post Assignterminals Example
  slug: adyen-post-assignterminals-example
- key_count: 6
  name: Adyen Post Authorise Example
  slug: adyen-post-authorise-example
- key_count: 6
  name: Adyen Post Authorise3D Example
  slug: adyen-post-authorise3d-example
- key_count: 6
  name: Adyen Post Authorise3Ds2 Example
  slug: adyen-post-authorise3ds2-example
- key_count: 6
  name: Adyen Post Balanceinquiry Example
  slug: adyen-post-balanceinquiry-example
- key_count: 6
  name: Adyen Post Businesslines Example
  slug: adyen-post-businesslines-example
- key_count: 6
  name: Adyen Post Cancel Example
  slug: adyen-post-cancel-example
- key_count: 6
  name: Adyen Post Cancelorrefund Example
  slug: adyen-post-cancelorrefund-example
- key_count: 6
  name: Adyen Post Capture Example
  slug: adyen-post-capture-example
- key_count: 6
  name: Adyen Post Cardacquisition Example
  slug: adyen-post-cardacquisition-example
- key_count: 6
  name: Adyen Post Cardreaderapdu Example
  slug: adyen-post-cardreaderapdu-example
- key_count: 6
  name: Adyen Post Changestatus Example
  slug: adyen-post-changestatus-example
- key_count: 6
  name: Adyen Post Checkaccountholder Example
  slug: adyen-post-checkaccountholder-example
- key_count: 6
  name: Adyen Post Checkbalance Example
  slug: adyen-post-checkbalance-example
- key_count: 6
  name: Adyen Post Closeaccount Example
  slug: adyen-post-closeaccount-example
- key_count: 6
  name: Adyen Post Closeaccountholder Example
  slug: adyen-post-closeaccountholder-example
- key_count: 6
  name: Adyen Post Closestores Example
  slug: adyen-post-closestores-example
- key_count: 6
  name: Adyen Post Companies Companyid Androidapps Example
  slug: adyen-post-companies-companyid-androidapps-example
- key_count: 6
  name: Adyen Post Companies Companyid Apicredentials Apicredentialid Allo Example
  slug: adyen-post-companies-companyid-apicredentials-apicredentialid-allo-example
- key_count: 6
  name: Adyen Post Companies Companyid Apicredentials Apicredentialid Gene Example
  slug: adyen-post-companies-companyid-apicredentials-apicredentialid-gene-example
- key_count: 6
  name: Adyen Post Companies Companyid Apicredentials Example
  slug: adyen-post-companies-companyid-apicredentials-example
- key_count: 6
  name: Adyen Post Companies Companyid Shippinglocations Example
  slug: adyen-post-companies-companyid-shippinglocations-example
- key_count: 6
  name: Adyen Post Companies Companyid Terminalorders Example
  slug: adyen-post-companies-companyid-terminalorders-example
- key_count: 6
  name: Adyen Post Companies Companyid Terminalorders Orderid Cancel Example
  slug: adyen-post-companies-companyid-terminalorders-orderid-cancel-example
- key_count: 6
  name: Adyen Post Companies Companyid Users Example
  slug: adyen-post-companies-companyid-users-example
- key_count: 6
  name: Adyen Post Companies Companyid Webhooks Example
  slug: adyen-post-companies-companyid-webhooks-example
- key_count: 6
  name: Adyen Post Companies Companyid Webhooks Webhookid Generatehmac Example
  slug: adyen-post-companies-companyid-webhooks-webhookid-generatehmac-example
- key_count: 6
  name: Adyen Post Companies Companyid Webhooks Webhookid Test Example
  slug: adyen-post-companies-companyid-webhooks-webhookid-test-example
- key_count: 6
  name: Adyen Post Confirmthirdparty Example
  slug: adyen-post-confirmthirdparty-example
- key_count: 6
  name: Adyen Post Createaccount Example
  slug: adyen-post-createaccount-example
- key_count: 6
  name: Adyen Post Createaccountholder Example
  slug: adyen-post-createaccountholder-example
- key_count: 6
  name: Adyen Post Createnotificationconfiguration Example
  slug: adyen-post-createnotificationconfiguration-example
- key_count: 6
  name: Adyen Post Createpermit Example
  slug: adyen-post-createpermit-example
- key_count: 6
  name: Adyen Post Createtestcardranges Example
  slug: adyen-post-createtestcardranges-example
- key_count: 6
  name: Adyen Post Debitaccountholder Example
  slug: adyen-post-debitaccountholder-example
- key_count: 6
  name: Adyen Post Declinethirdparty Example
  slug: adyen-post-declinethirdparty-example
- key_count: 6
  name: Adyen Post Defenddispute Example
  slug: adyen-post-defenddispute-example
- key_count: 6
  name: Adyen Post Deletebankaccounts Example
  slug: adyen-post-deletebankaccounts-example
- key_count: 6
  name: Adyen Post Deletedisputedefensedocument Example
  slug: adyen-post-deletedisputedefensedocument-example
- key_count: 6
  name: Adyen Post Deletelegalarrangements Example
  slug: adyen-post-deletelegalarrangements-example
- key_count: 6
  name: Adyen Post Deletenotificationconfigurations Example
  slug: adyen-post-deletenotificationconfigurations-example
- key_count: 6
  name: Adyen Post Deletepayoutmethods Example
  slug: adyen-post-deletepayoutmethods-example
- key_count: 6
  name: Adyen Post Deleteshareholders Example
  slug: adyen-post-deleteshareholders-example
- key_count: 6
  name: Adyen Post Deletesignatories Example
  slug: adyen-post-deletesignatories-example
- key_count: 6
  name: Adyen Post Diagnosis Example
  slug: adyen-post-diagnosis-example
- key_count: 6
  name: Adyen Post Disable Example
  slug: adyen-post-disable-example
- key_count: 6
  name: Adyen Post Disablepermit Example
  slug: adyen-post-disablepermit-example
- key_count: 6
  name: Adyen Post Display Example
  slug: adyen-post-display-example
- key_count: 6
  name: Adyen Post Documents Example
  slug: adyen-post-documents-example
- key_count: 6
  name: Adyen Post Donate Example
  slug: adyen-post-donate-example
- key_count: 6
  name: Adyen Post Enableservice Example
  slug: adyen-post-enableservice-example
- key_count: 6
  name: Adyen Post Findterminal Example
  slug: adyen-post-findterminal-example
- key_count: 6
  name: Adyen Post Get3Dsavailability Example
  slug: adyen-post-get3dsavailability-example
- key_count: 6
  name: Adyen Post Getaccountholder Example
  slug: adyen-post-getaccountholder-example
- key_count: 6
  name: Adyen Post Getauthenticationresult Example
  slug: adyen-post-getauthenticationresult-example
- key_count: 6
  name: Adyen Post Getcostestimate Example
  slug: adyen-post-getcostestimate-example
- key_count: 6
  name: Adyen Post Getnotificationconfiguration Example
  slug: adyen-post-getnotificationconfiguration-example
- key_count: 6
  name: Adyen Post Getnotificationconfigurationlist Example
  slug: adyen-post-getnotificationconfigurationlist-example
- key_count: 6
  name: Adyen Post Getonboardingurl Example
  slug: adyen-post-getonboardingurl-example
- key_count: 6
  name: Adyen Post Getpciquestionnaireurl Example
  slug: adyen-post-getpciquestionnaireurl-example
- key_count: 6
  name: Adyen Post Getstoresunderaccount Example
  slug: adyen-post-getstoresunderaccount-example
- key_count: 6
  name: Adyen Post Gettaxform Example
  slug: adyen-post-gettaxform-example
- key_count: 6
  name: Adyen Post Getterminaldetails Example
  slug: adyen-post-getterminaldetails-example
- key_count: 6
  name: Adyen Post Getterminalsunderaccount Example
  slug: adyen-post-getterminalsunderaccount-example
- key_count: 6
  name: Adyen Post Gettotals Example
  slug: adyen-post-gettotals-example
- key_count: 6
  name: Adyen Post Getuploadeddocuments Example
  slug: adyen-post-getuploadeddocuments-example
- key_count: 6
  name: Adyen Post Grants Example
  slug: adyen-post-grants-example
- key_count: 6
  name: Adyen Post Input Example
  slug: adyen-post-input-example
- key_count: 6
  name: Adyen Post Issue Example
  slug: adyen-post-issue-example
- key_count: 6
  name: Adyen Post Legalentities Example
  slug: adyen-post-legalentities-example
- key_count: 6
  name: Adyen Post Legalentities Id Checkverificationerrors Example
  slug: adyen-post-legalentities-id-checkverificationerrors-example
- key_count: 6
  name: Adyen Post Legalentities Id Confirmdatareview Example
  slug: adyen-post-legalentities-id-confirmdatareview-example
- key_count: 6
  name: Adyen Post Legalentities Id Onboardinglinks Example
  slug: adyen-post-legalentities-id-onboardinglinks-example
- key_count: 6
  name: Adyen Post Legalentities Id Pciquestionnaires Generatepcitemplates Example
  slug: adyen-post-legalentities-id-pciquestionnaires-generatepcitemplates-example
- key_count: 6
  name: Adyen Post Legalentities Id Pciquestionnaires Signpcitemplates Example
  slug: adyen-post-legalentities-id-pciquestionnaires-signpcitemplates-example
- key_count: 6
  name: Adyen Post Legalentities Id Termsofservice Example
  slug: adyen-post-legalentities-id-termsofservice-example
- key_count: 6
  name: Adyen Post Listrecurringdetails Example
  slug: adyen-post-listrecurringdetails-example
- key_count: 6
  name: Adyen Post Load Example
  slug: adyen-post-load-example
- key_count: 6
  name: Adyen Post Login Example
  slug: adyen-post-login-example
- key_count: 6
  name: Adyen Post Logout Example
  slug: adyen-post-logout-example
- key_count: 6
  name: Adyen Post Loyalty Example
  slug: adyen-post-loyalty-example
- key_count: 6
  name: Adyen Post Me Allowedorigins Example
  slug: adyen-post-me-allowedorigins-example
- key_count: 6
  name: Adyen Post Me Generateclientkey Example
  slug: adyen-post-me-generateclientkey-example
- key_count: 6
  name: Adyen Post Merchants Example
  slug: adyen-post-merchants-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Activate Example
  slug: adyen-post-merchants-merchantid-activate-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Apicredentials Apicredentialid All Example
  slug: adyen-post-merchants-merchantid-apicredentials-apicredentialid-all-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Apicredentials Apicredentialid Gen Example
  slug: adyen-post-merchants-merchantid-apicredentials-apicredentialid-gen-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Apicredentials Example
  slug: adyen-post-merchants-merchantid-apicredentials-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Paymentmethodsettings Example
  slug: adyen-post-merchants-merchantid-paymentmethodsettings-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Paymentmethodsettings Paymentmetho Example
  slug: adyen-post-merchants-merchantid-paymentmethodsettings-paymentmetho-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Payoutsettings Example
  slug: adyen-post-merchants-merchantid-payoutsettings-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Shippinglocations Example
  slug: adyen-post-merchants-merchantid-shippinglocations-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Splitconfigurations Example
  slug: adyen-post-merchants-merchantid-splitconfigurations-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Splitconfigurations Splitconfigura Example
  slug: adyen-post-merchants-merchantid-splitconfigurations-splitconfigura-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Stores Example
  slug: adyen-post-merchants-merchantid-stores-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Terminalorders Example
  slug: adyen-post-merchants-merchantid-terminalorders-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Terminalorders Orderid Cancel Example
  slug: adyen-post-merchants-merchantid-terminalorders-orderid-cancel-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Users Example
  slug: adyen-post-merchants-merchantid-users-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Webhooks Example
  slug: adyen-post-merchants-merchantid-webhooks-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Webhooks Webhookid Generatehmac Example
  slug: adyen-post-merchants-merchantid-webhooks-webhookid-generatehmac-example
- key_count: 6
  name: Adyen Post Merchants Merchantid Webhooks Webhookid Test Example
  slug: adyen-post-merchants-merchantid-webhooks-webhookid-test-example
- key_count: 6
  name: Adyen Post Mergebalance Example
  slug: adyen-post-mergebalance-example
- key_count: 6
  name: Adyen Post Notifyshopper Example
  slug: adyen-post-notifyshopper-example
- key_count: 6
  name: Adyen Post Payment Example
  slug: adyen-post-payment-example
- key_count: 6
  name: Adyen Post Payout Example
  slug: adyen-post-payout-example
- key_count: 6
  name: Adyen Post Payoutaccountholder Example
  slug: adyen-post-payoutaccountholder-example
- key_count: 6
  name: Adyen Post Pins Change Example
  slug: adyen-post-pins-change-example
- key_count: 6
  name: Adyen Post Pins Reveal Example
  slug: adyen-post-pins-reveal-example
- key_count: 6
  name: Adyen Post Print Example
  slug: adyen-post-print-example
- key_count: 6
  name: Adyen Post Reconciliation Example
  slug: adyen-post-reconciliation-example
- key_count: 6
  name: Adyen Post Refund Example
  slug: adyen-post-refund-example
- key_count: 6
  name: Adyen Post Refundfundstransfer Example
  slug: adyen-post-refundfundstransfer-example
- key_count: 6
  name: Adyen Post Refundnotpaidouttransfers Example
  slug: adyen-post-refundnotpaidouttransfers-example
- key_count: 6
  name: Adyen Post Requestsubjecterasure Example
  slug: adyen-post-requestsubjecterasure-example
- key_count: 6
  name: Adyen Post Retrieve3Ds2Result Example
  slug: adyen-post-retrieve3ds2result-example
- key_count: 6
  name: Adyen Post Retrieveapplicabledefensereasons Example
  slug: adyen-post-retrieveapplicabledefensereasons-example
- key_count: 6
  name: Adyen Post Reversal Example
  slug: adyen-post-reversal-example
- key_count: 6
  name: Adyen Post Scheduleaccountupdater Example
  slug: adyen-post-scheduleaccountupdater-example
- key_count: 6
  name: Adyen Post Setupbeneficiary Example
  slug: adyen-post-setupbeneficiary-example
- key_count: 6
  name: Adyen Post Storedetail Example
  slug: adyen-post-storedetail-example
- key_count: 6
  name: Adyen Post Storedetailandsubmitthirdparty Example
  slug: adyen-post-storedetailandsubmitthirdparty-example
- key_count: 6
  name: Adyen Post Storedvalue Example
  slug: adyen-post-storedvalue-example
- key_count: 6
  name: Adyen Post Stores Example
  slug: adyen-post-stores-example
- key_count: 6
  name: Adyen Post Submitthirdparty Example
  slug: adyen-post-submitthirdparty-example
- key_count: 6
  name: Adyen Post Supplydefensedocument Example
  slug: adyen-post-supplydefensedocument-example
- key_count: 6
  name: Adyen Post Suspendaccountholder Example
  slug: adyen-post-suspendaccountholder-example
- key_count: 6
  name: Adyen Post Technicalcancel Example
  slug: adyen-post-technicalcancel-example
- key_count: 6
  name: Adyen Post Terminals Scheduleactions Example
  slug: adyen-post-terminals-scheduleactions-example
- key_count: 6
  name: Adyen Post Terminals Terminalid Reassign Example
  slug: adyen-post-terminals-terminalid-reassign-example
- key_count: 6
  name: Adyen Post Testnotificationconfiguration Example
  slug: adyen-post-testnotificationconfiguration-example
- key_count: 6
  name: Adyen Post Transactionstatus Example
  slug: adyen-post-transactionstatus-example
- key_count: 6
  name: Adyen Post Transferfunds Example
  slug: adyen-post-transferfunds-example
- key_count: 6
  name: Adyen Post Transferinstruments Example
  slug: adyen-post-transferinstruments-example
- key_count: 6
  name: Adyen Post Transfers Example
  slug: adyen-post-transfers-example
- key_count: 6
  name: Adyen Post Transfers Transferid Returns Example
  slug: adyen-post-transfers-transferid-returns-example
- key_count: 6
  name: Adyen Post Unsuspendaccountholder Example
  slug: adyen-post-unsuspendaccountholder-example
- key_count: 6
  name: Adyen Post Updateaccount Example
  slug: adyen-post-updateaccount-example
- key_count: 6
  name: Adyen Post Updateaccountholder Example
  slug: adyen-post-updateaccountholder-example
- key_count: 6
  name: Adyen Post Updateaccountholderstate Example
  slug: adyen-post-updateaccountholderstate-example
- key_count: 6
  name: Adyen Post Updatenotificationconfiguration Example
  slug: adyen-post-updatenotificationconfiguration-example
- key_count: 6
  name: Adyen Post Uploaddocument Example
  slug: adyen-post-uploaddocument-example
- key_count: 6
  name: Adyen Post Voidpendingrefund Example
  slug: adyen-post-voidpendingrefund-example
- key_count: 6
  name: Adyen Post Voidtransaction Example
  slug: adyen-post-voidtransaction-example
- key_count: 2
  name: Authentication Webhooks Amount Example
  slug: authentication-webhooks-amount-example
- key_count: 15
  name: Authentication Webhooks Authentication Info Example
  slug: authentication-webhooks-authentication-info-example
- key_count: 6
  name: Authentication Webhooks Authentication Notification Data Example
  slug: authentication-webhooks-authentication-notification-data-example
- key_count: 3
  name: Authentication Webhooks Authentication Notification Request Example
  slug: authentication-webhooks-authentication-notification-request-example
- key_count: 1
  name: Authentication Webhooks Balance Platform Notification Response Example
  slug: authentication-webhooks-balance-platform-notification-response-example
- key_count: 6
  name: Authentication Webhooks Challenge Info Example
  slug: authentication-webhooks-challenge-info-example
- key_count: 3
  name: Authentication Webhooks Purchase Info Example
  slug: authentication-webhooks-purchase-info-example
- key_count: 3
  name: Authentication Webhooks Resource Example
  slug: authentication-webhooks-resource-example
- key_count: 2
  name: Balance Control Amount Example
  slug: balance-control-amount-example
- key_count: 6
  name: Balance Control Balance Transfer Request Example
  slug: balance-control-balance-transfer-request-example
- key_count: 9
  name: Balance Control Balance Transfer Response Example
  slug: balance-control-balance-transfer-response-example
- key_count: 2
  name: Binlookup Amount Example
  slug: binlookup-amount-example
- key_count: 1
  name: Binlookup Bin Detail Example
  slug: binlookup-bin-detail-example
- key_count: 11
  name: Binlookup Card Bin Example
  slug: binlookup-card-bin-example
- key_count: 3
  name: Binlookup Cost Estimate Assumptions Example
  slug: binlookup-cost-estimate-assumptions-example
- key_count: 10
  name: Binlookup Cost Estimate Request Example
  slug: binlookup-cost-estimate-request-example
- key_count: 5
  name: Binlookup Cost Estimate Response Example
  slug: binlookup-cost-estimate-response-example
- key_count: 5
  name: Binlookup Ds Public Key Detail Example
  slug: binlookup-ds-public-key-detail-example
- key_count: 3
  name: Binlookup Merchant Details Example
  slug: binlookup-merchant-details-example
- key_count: 5
  name: Binlookup Recurring Example
  slug: binlookup-recurring-example
- key_count: 6
  name: Binlookup Three Ds Availability Request Example
  slug: binlookup-three-ds-availability-request-example
- key_count: 5
  name: Binlookup Three Ds Availability Response Example
  slug: binlookup-three-ds-availability-response-example
- key_count: 6
  name: Binlookup Three Ds2 Card Range Detail Example
  slug: binlookup-three-ds2-card-range-detail-example
- key_count: 19
  name: Checkout Account Info Example
  slug: checkout-account-info-example
- key_count: 16
  name: Checkout Acct Info Example
  slug: checkout-acct-info-example
- key_count: 10
  name: Checkout Ach Details Example
  slug: checkout-ach-details-example
- key_count: 28
  name: Checkout Additional Data Airline Example
  slug: checkout-additional-data-airline-example
- key_count: 23
  name: Checkout Additional Data Car Rental Example
  slug: checkout-additional-data-car-rental-example
- key_count: 16
  name: Checkout Additional Data Common Example
  slug: checkout-additional-data-common-example
- key_count: 17
  name: Checkout Additional Data Level23 Example
  slug: checkout-additional-data-level23-example
- key_count: 16
  name: Checkout Additional Data Lodging Example
  slug: checkout-additional-data-lodging-example
- key_count: 18
  name: Checkout Additional Data Open Invoice Example
  slug: checkout-additional-data-open-invoice-example
- key_count: 1
  name: Checkout Additional Data Opi Example
  slug: checkout-additional-data-opi-example
- key_count: 8
  name: Checkout Additional Data Ratepay Example
  slug: checkout-additional-data-ratepay-example
- key_count: 3
  name: Checkout Additional Data Retry Example
  slug: checkout-additional-data-retry-example
- key_count: 21
  name: Checkout Additional Data Risk Example
  slug: checkout-additional-data-risk-example
- key_count: 15
  name: Checkout Additional Data Risk Standalone Example
  slug: checkout-additional-data-risk-standalone-example
- key_count: 10
  name: Checkout Additional Data Sub Merchant Example
  slug: checkout-additional-data-sub-merchant-example
- key_count: 9
  name: Checkout Additional Data Temporary Services Example
  slug: checkout-additional-data-temporary-services-example
- key_count: 6
  name: Checkout Additional Data Wallets Example
  slug: checkout-additional-data-wallets-example
- key_count: 6
  name: Checkout Additional Data3 D Secure Example
  slug: checkout-additional-data3-d-secure-example
- key_count: 6
  name: Checkout Address Example
  slug: checkout-address-example
- key_count: 7
  name: Checkout Afterpay Details Example
  slug: checkout-afterpay-details-example
- key_count: 4
  name: Checkout Amazon Pay Details Example
  slug: checkout-amazon-pay-details-example
- key_count: 2
  name: Checkout Amount Example
  slug: checkout-amount-example
- key_count: 2
  name: Checkout Android Pay Details Example
  slug: checkout-android-pay-details-example
- key_count: 6
  name: Checkout Apple Pay Details Example
  slug: checkout-apple-pay-details-example
- key_count: 6
  name: Checkout Apple Pay Donations Example
  slug: checkout-apple-pay-donations-example
- key_count: 3
  name: Checkout Apple Pay Session Request Example
  slug: checkout-apple-pay-session-request-example
- key_count: 1
  name: Checkout Apple Pay Session Response Example
  slug: checkout-apple-pay-session-response-example
- key_count: 6
  name: Checkout Application Info Example
  slug: checkout-application-info-example
- key_count: 3
  name: Checkout Authentication Data Example
  slug: checkout-authentication-data-example
- key_count: 2
  name: Checkout Avs Example
  slug: checkout-avs-example
- key_count: 7
  name: Checkout Bacs Direct Debit Details Example
  slug: checkout-bacs-direct-debit-details-example
- key_count: 44
  name: Checkout Balance Check Request Example
  slug: checkout-balance-check-request-example
- key_count: 7
  name: Checkout Balance Check Response Example
  slug: checkout-balance-check-response-example
- key_count: 9
  name: Checkout Bank Account Example
  slug: checkout-bank-account-example
- key_count: 3
  name: Checkout Bill Desk Details Example
  slug: checkout-bill-desk-details-example
- key_count: 6
  name: Checkout Billing Address Example
  slug: checkout-billing-address-example
- key_count: 5
  name: Checkout Blik Details Example
  slug: checkout-blik-details-example
- key_count: 9
  name: Checkout Browser Info Example
  slug: checkout-browser-info-example
- key_count: 2
  name: Checkout Cancel Order Request Example
  slug: checkout-cancel-order-request-example
- key_count: 2
  name: Checkout Cancel Order Response Example
  slug: checkout-cancel-order-response-example
- key_count: 2
  name: Checkout Card Brand Details Example
  slug: checkout-card-brand-details-example
- key_count: 19
  name: Checkout Card Details Example
  slug: checkout-card-details-example
- key_count: 5
  name: Checkout Card Details Request Example
  slug: checkout-card-details-request-example
- key_count: 1
  name: Checkout Card Details Response Example
  slug: checkout-card-details-response-example
- key_count: 19
  name: Checkout Card Donations Example
  slug: checkout-card-donations-example
- key_count: 8
  name: Checkout Card Example
  slug: checkout-card-example
- key_count: 3
  name: Checkout Cellulant Details Example
  slug: checkout-cellulant-details-example
- key_count: 4
  name: Checkout Checkout Await Action Example
  slug: checkout-checkout-await-action-example
- key_count: 6
  name: Checkout Checkout Delegated Authentication Action Example
  slug: checkout-checkout-delegated-authentication-action-example
- key_count: 6
  name: Checkout Checkout Native Redirect Action Example
  slug: checkout-checkout-native-redirect-action-example
- key_count: 6
  name: Checkout Checkout Order Response Example
  slug: checkout-checkout-order-response-example
- key_count: 6
  name: Checkout Checkout Qr Code Action Example
  slug: checkout-checkout-qr-code-action-example
- key_count: 5
  name: Checkout Checkout Redirect Action Example
  slug: checkout-checkout-redirect-action-example
- key_count: 5
  name: Checkout Checkout Sdk Action Example
  slug: checkout-checkout-sdk-action-example
- key_count: 3
  name: Checkout Checkout Session Installment Option Example
  slug: checkout-checkout-session-installment-option-example
- key_count: 7
  name: Checkout Checkout Three Ds2 Action Example
  slug: checkout-checkout-three-ds2-action-example
- key_count: 21
  name: Checkout Checkout Voucher Action Example
  slug: checkout-checkout-voucher-action-example
- key_count: 2
  name: Checkout Common Field Example
  slug: checkout-common-field-example
- key_count: 6
  name: Checkout Company Example
  slug: checkout-company-example
- key_count: 4
  name: Checkout Configuration Example
  slug: checkout-configuration-example
- key_count: 59
  name: Checkout Create Checkout Session Request Example
  slug: checkout-create-checkout-session-request-example
- key_count: 62
  name: Checkout Create Checkout Session Response Example
  slug: checkout-create-checkout-session-response-example
- key_count: 4
  name: Checkout Create Order Request Example
  slug: checkout-create-order-request-example
- key_count: 10
  name: Checkout Create Order Response Example
  slug: checkout-create-order-response-example
- key_count: 8
  name: Checkout Delivery Address Example
  slug: checkout-delivery-address-example
- key_count: 1
  name: Checkout Details Request Authentication Data Example
  slug: checkout-details-request-authentication-data-example
- key_count: 2
  name: Checkout Device Render Options Example
  slug: checkout-device-render-options-example
- key_count: 5
  name: Checkout Doku Details Example
  slug: checkout-doku-details-example
- key_count: 41
  name: Checkout Donation Payment Request Example
  slug: checkout-donation-payment-request-example
- key_count: 7
  name: Checkout Donation Payment Response Example
  slug: checkout-donation-payment-response-example
- key_count: 3
  name: Checkout Dotpay Details Example
  slug: checkout-dotpay-details-example
- key_count: 4
  name: Checkout Dragonpay Details Example
  slug: checkout-dragonpay-details-example
- key_count: 6
  name: Checkout Econtext Voucher Details Example
  slug: checkout-econtext-voucher-details-example
- key_count: 2
  name: Checkout Encrypted Order Data Example
  slug: checkout-encrypted-order-data-example
- key_count: 3
  name: Checkout External Platform Example
  slug: checkout-external-platform-example
- key_count: 12
  name: Checkout Forex Quote Example
  slug: checkout-forex-quote-example
- key_count: 3
  name: Checkout Fraud Check Result Example
  slug: checkout-fraud-check-result-example
- key_count: 2
  name: Checkout Fraud Result Example
  slug: checkout-fraud-result-example
- key_count: 5
  name: Checkout Fund Origin Example
  slug: checkout-fund-origin-example
- key_count: 10
  name: Checkout Fund Recipient Example
  slug: checkout-fund-recipient-example
- key_count: 5
  name: Checkout Generic Issuer Payment Method Details Example
  slug: checkout-generic-issuer-payment-method-details-example
- key_count: 4
  name: Checkout Giropay Details Example
  slug: checkout-giropay-details-example
- key_count: 7
  name: Checkout Google Pay Details Example
  slug: checkout-google-pay-details-example
- key_count: 7
  name: Checkout Google Pay Donations Example
  slug: checkout-google-pay-donations-example
- key_count: 5
  name: Checkout Ideal Details Example
  slug: checkout-ideal-details-example
- key_count: 5
  name: Checkout Ideal Donations Example
  slug: checkout-ideal-donations-example
- key_count: 9
  name: Checkout Input Detail Example
  slug: checkout-input-detail-example
- key_count: 4
  name: Checkout Installment Option Example
  slug: checkout-installment-option-example
- key_count: 2
  name: Checkout Installments Example
  slug: checkout-installments-example
- key_count: 1
  name: Checkout Installments Number Example
  slug: checkout-installments-number-example
- key_count: 2
  name: Checkout Item Example
  slug: checkout-item-example
- key_count: 8
  name: Checkout Klarna Details Example
  slug: checkout-klarna-details-example
- key_count: 17
  name: Checkout Line Item Example
  slug: checkout-line-item-example
- key_count: 3
  name: Checkout List Stored Payment Methods Response Example
  slug: checkout-list-stored-payment-methods-response-example
- key_count: 8
  name: Checkout Mandate Example
  slug: checkout-mandate-example
- key_count: 4
  name: Checkout Masterpass Details Example
  slug: checkout-masterpass-details-example
- key_count: 4
  name: Checkout Mbway Details Example
  slug: checkout-mbway-details-example
- key_count: 3
  name: Checkout Merchant Device Example
  slug: checkout-merchant-device-example
- key_count: 14
  name: Checkout Merchant Risk Indicator Example
  slug: checkout-merchant-risk-indicator-example
- key_count: 2
  name: Checkout Mobile Pay Details Example
  slug: checkout-mobile-pay-details-example
- key_count: 3
  name: Checkout Mol Pay Details Example
  slug: checkout-mol-pay-details-example
- key_count: 2
  name: Checkout Name Example
  slug: checkout-name-example
- key_count: 7
  name: Checkout Open Invoice Details Example
  slug: checkout-open-invoice-details-example
- key_count: 9
  name: Checkout Pay Pal Details Example
  slug: checkout-pay-pal-details-example
- key_count: 6
  name: Checkout Pay U Upi Details Example
  slug: checkout-pay-u-upi-details-example
- key_count: 6
  name: Checkout Pay With Google Details Example
  slug: checkout-pay-with-google-details-example
- key_count: 6
  name: Checkout Pay With Google Donations Example
  slug: checkout-pay-with-google-donations-example
- key_count: 7
  name: Checkout Payment Amount Update Request Example
  slug: checkout-payment-amount-update-request-example
- key_count: 9
  name: Checkout Payment Amount Update Response Example
  slug: checkout-payment-amount-update-response-example
- key_count: 3
  name: Checkout Payment Cancel Request Example
  slug: checkout-payment-cancel-request-example
- key_count: 5
  name: Checkout Payment Cancel Response Example
  slug: checkout-payment-cancel-response-example
- key_count: 8
  name: Checkout Payment Capture Request Example
  slug: checkout-payment-capture-request-example
- key_count: 10
  name: Checkout Payment Capture Response Example
  slug: checkout-payment-capture-response-example
- key_count: 18
  name: Checkout Payment Completion Details Example
  slug: checkout-payment-completion-details-example
- key_count: 2
  name: Checkout Payment Details Example
  slug: checkout-payment-details-example
- key_count: 4
  name: Checkout Payment Details Request Example
  slug: checkout-payment-details-request-example
- key_count: 15
  name: Checkout Payment Details Response Example
  slug: checkout-payment-details-response-example
- key_count: 38
  name: Checkout Payment Link Request Example
  slug: checkout-payment-link-request-example
- key_count: 42
  name: Checkout Payment Link Response Example
  slug: checkout-payment-link-response-example
- key_count: 9
  name: Checkout Payment Method Example
  slug: checkout-payment-method-example
- key_count: 3
  name: Checkout Payment Method Group Example
  slug: checkout-payment-method-group-example
- key_count: 3
  name: Checkout Payment Method Issuer Example
  slug: checkout-payment-method-issuer-example
- key_count: 12
  name: Checkout Payment Methods Request Example
  slug: checkout-payment-methods-request-example
- key_count: 2
  name: Checkout Payment Methods Response Example
  slug: checkout-payment-methods-response-example
- key_count: 8
  name: Checkout Payment Refund Request Example
  slug: checkout-payment-refund-request-example
- key_count: 10
  name: Checkout Payment Refund Response Example
  slug: checkout-payment-refund-response-example
- key_count: 67
  name: Checkout Payment Request Example
  slug: checkout-payment-request-example
- key_count: 15
  name: Checkout Payment Response Example
  slug: checkout-payment-response-example
- key_count: 3
  name: Checkout Payment Reversal Request Example
  slug: checkout-payment-reversal-request-example
- key_count: 5
  name: Checkout Payment Reversal Response Example
  slug: checkout-payment-reversal-response-example
- key_count: 56
  name: Checkout Payment Setup Request Example
  slug: checkout-payment-setup-request-example
- key_count: 2
  name: Checkout Payment Setup Response Example
  slug: checkout-payment-setup-response-example
- key_count: 1
  name: Checkout Payment Verification Request Example
  slug: checkout-payment-verification-request-example
- key_count: 10
  name: Checkout Payment Verification Response Example
  slug: checkout-payment-verification-response-example
- key_count: 2
  name: Checkout Phone Example
  slug: checkout-phone-example
- key_count: 3
  name: Checkout Platform Chargeback Logic Example
  slug: checkout-platform-chargeback-logic-example
- key_count: 7
  name: Checkout Ratepay Details Example
  slug: checkout-ratepay-details-example
- key_count: 11
  name: Checkout Recurring Detail Example
  slug: checkout-recurring-detail-example
- key_count: 5
  name: Checkout Recurring Example
  slug: checkout-recurring-example
- key_count: 6
  name: Checkout Response Additional Data Billing Address Example
  slug: checkout-response-additional-data-billing-address-example
- key_count: 8
  name: Checkout Response Additional Data Card Example
  slug: checkout-response-additional-data-card-example
- key_count: 59
  name: Checkout Response Additional Data Common Example
  slug: checkout-response-additional-data-common-example
- key_count: 2
  name: Checkout Response Additional Data Domestic Error Example
  slug: checkout-response-additional-data-domestic-error-example
- key_count: 12
  name: Checkout Response Additional Data Installments Example
  slug: checkout-response-additional-data-installments-example
- key_count: 3
  name: Checkout Response Additional Data Network Tokens Example
  slug: checkout-response-additional-data-network-tokens-example
- key_count: 1
  name: Checkout Response Additional Data Opi Example
  slug: checkout-response-additional-data-opi-example
- key_count: 3
  name: Checkout Response Additional Data Sepa Example
  slug: checkout-response-additional-data-sepa-example
- key_count: 5
  name: Checkout Response Additional Data3 D Secure Example
  slug: checkout-response-additional-data3-d-secure-example
- key_count: 2
  name: Checkout Response Payment Method Example
  slug: checkout-response-payment-method-example
- key_count: 4
  name: Checkout Risk Data Example
  slug: checkout-risk-data-example
- key_count: 6
  name: Checkout Samsung Pay Details Example
  slug: checkout-samsung-pay-details-example
- key_count: 4
  name: Checkout Sdk Ephem Pub Key Example
  slug: checkout-sdk-ephem-pub-key-example
- key_count: 6
  name: Checkout Sepa Direct Debit Details Example
  slug: checkout-sepa-direct-debit-details-example
- key_count: 4
  name: Checkout Service Error Details Example
  slug: checkout-service-error-details-example
- key_count: 2
  name: Checkout Session Result Response Example
  slug: checkout-session-result-response-example
- key_count: 3
  name: Checkout Shopper Input Example
  slug: checkout-shopper-input-example
- key_count: 3
  name: Checkout Shopper Interaction Device Example
  slug: checkout-shopper-interaction-device-example
- key_count: 2
  name: Checkout Split Amount Example
  slug: checkout-split-amount-example
- key_count: 5
  name: Checkout Split Example
  slug: checkout-split-example
- key_count: 4
  name: Checkout Standalone Payment Cancel Request Example
  slug: checkout-standalone-payment-cancel-request-example
- key_count: 5
  name: Checkout Standalone Payment Cancel Response Example
  slug: checkout-standalone-payment-cancel-response-example
- key_count: 3
  name: Checkout Stored Details Example
  slug: checkout-stored-details-example
- key_count: 4
  name: Checkout Stored Payment Method Details Example
  slug: checkout-stored-payment-method-details-example
- key_count: 17
  name: Checkout Stored Payment Method Example
  slug: checkout-stored-payment-method-example
- key_count: 17
  name: Checkout Stored Payment Method Resource Example
  slug: checkout-stored-payment-method-resource-example
- key_count: 6
  name: Checkout Sub Input Detail Example
  slug: checkout-sub-input-detail-example
- key_count: 5
  name: Checkout Sub Merchant Example
  slug: checkout-sub-merchant-example
- key_count: 5
  name: Checkout Sub Merchant Info Example
  slug: checkout-sub-merchant-info-example
- key_count: 12
  name: Checkout Three D Secure Data Example
  slug: checkout-three-d-secure-data-example
- key_count: 4
  name: Checkout Three Ds Request Data Example
  slug: checkout-three-ds-request-data-example
- key_count: 3
  name: Checkout Three Ds Requestor Authentication Info Example
  slug: checkout-three-ds-requestor-authentication-info-example
- key_count: 4
  name: Checkout Three Ds Requestor Prior Authentication Info Example
  slug: checkout-three-ds-requestor-prior-authentication-info-example
- key_count: 40
  name: Checkout Three Ds2 Request Data Example
  slug: checkout-three-ds2-request-data-example
- key_count: 37
  name: Checkout Three Ds2 Request Fields Example
  slug: checkout-three-ds2-request-fields-example
- key_count: 19
  name: Checkout Three Ds2 Response Data Example
  slug: checkout-three-ds2-response-data-example
- key_count: 14
  name: Checkout Three Ds2 Result Example
  slug: checkout-three-ds2-result-example
- key_count: 1
  name: Checkout Update Payment Link Request Example
  slug: checkout-update-payment-link-request-example
- key_count: 7
  name: Checkout Upi Collect Details Example
  slug: checkout-upi-collect-details-example
- key_count: 5
  name: Checkout Upi Intent Details Example
  slug: checkout-upi-intent-details-example
- key_count: 1
  name: Checkout Utility Request Example
  slug: checkout-utility-request-example
- key_count: 1
  name: Checkout Utility Response Example
  slug: checkout-utility-response-example
- key_count: 5
  name: Checkout Vipps Details Example
  slug: checkout-vipps-details-example
- key_count: 4
  name: Checkout Visa Checkout Details Example
  slug: checkout-visa-checkout-details-example
- key_count: 2
  name: Checkout We Chat Pay Details Example
  slug: checkout-we-chat-pay-details-example
- key_count: 4
  name: Checkout We Chat Pay Mini Program Details Example
  slug: checkout-we-chat-pay-mini-program-details-example
- key_count: 5
  name: Checkout Zip Details Example
  slug: checkout-zip-details-example
- key_count: 10
  name: Configuration Account Holder Capability Example
  slug: configuration-account-holder-capability-example
- key_count: 13
  name: Configuration Account Holder Example
  slug: configuration-account-holder-example
- key_count: 9
  name: Configuration Account Holder Info Example
  slug: configuration-account-holder-info-example
- key_count: 11
  name: Configuration Account Holder Update Request Example
  slug: configuration-account-holder-update-request-example
- key_count: 7
  name: Configuration Account Supporting Entity Capability Example
  slug: configuration-account-supporting-entity-capability-example
- key_count: 2
  name: Configuration Active Network Tokens Restriction Example
  slug: configuration-active-network-tokens-restriction-example
- key_count: 2
  name: Configuration Additional Bank Identification Example
  slug: configuration-additional-bank-identification-example
- key_count: 6
  name: Configuration Address Example
  slug: configuration-address-example
- key_count: 3
  name: Configuration Address Requirement Example
  slug: configuration-address-requirement-example
- key_count: 2
  name: Configuration Amount Example
  slug: configuration-amount-example
- key_count: 4
  name: Configuration Amount Min Max Requirement Example
  slug: configuration-amount-min-max-requirement-example
- key_count: 3
  name: Configuration Au Local Account Identification Example
  slug: configuration-au-local-account-identification-example
- key_count: 3
  name: Configuration Authentication Example
  slug: configuration-authentication-example
- key_count: 10
  name: Configuration Balance Account Base Example
  slug: configuration-balance-account-base-example
- key_count: 11
  name: Configuration Balance Account Example
  slug: configuration-balance-account-example
- key_count: 8
  name: Configuration Balance Account Info Example
  slug: configuration-balance-account-info-example
- key_count: 7
  name: Configuration Balance Account Update Request Example
  slug: configuration-balance-account-update-request-example
- key_count: 5
  name: Configuration Balance Example
  slug: configuration-balance-example
- key_count: 3
  name: Configuration Balance Platform Example
  slug: configuration-balance-platform-example
- key_count: 3
  name: Configuration Balance Sweep Configurations Response Example
  slug: configuration-balance-sweep-configurations-response-example
- key_count: 1
  name: Configuration Bank Account Example
  slug: configuration-bank-account-example
- key_count: 3
  name: Configuration Bank Account Identification Type Requirement Example
  slug: configuration-bank-account-identification-type-requirement-example
- key_count: 1
  name: Configuration Bank Account Identification Validation Request Example
  slug: configuration-bank-account-identification-validation-request-example
- key_count: 1
  name: Configuration Bank Account Model Example
  slug: configuration-bank-account-model-example
- key_count: 3
  name: Configuration Bank Identification Example
  slug: configuration-bank-identification-example
- key_count: 4
  name: Configuration Br Local Account Identification Example
  slug: configuration-br-local-account-identification-example
- key_count: 2
  name: Configuration Brand Variants Restriction Example
  slug: configuration-brand-variants-restriction-example
- key_count: 9
  name: Configuration Bulk Address Example
  slug: configuration-bulk-address-example
- key_count: 5
  name: Configuration Ca Local Account Identification Example
  slug: configuration-ca-local-account-identification-example
- key_count: 4
  name: Configuration Capability Problem Entity Example
  slug: configuration-capability-problem-entity-example
- key_count: 3
  name: Configuration Capability Problem Entity Recursive Example
  slug: configuration-capability-problem-entity-recursive-example
- key_count: 2
  name: Configuration Capability Problem Example
  slug: configuration-capability-problem-example
- key_count: 5
  name: Configuration Capability Settings Example
  slug: configuration-capability-settings-example
- key_count: 4
  name: Configuration Capital Balance Example
  slug: configuration-capital-balance-example
- key_count: 4
  name: Configuration Capital Grant Account Example
  slug: configuration-capital-grant-account-example
- key_count: 14
  name: Configuration Card Configuration Example
  slug: configuration-card-configuration-example
- key_count: 13
  name: Configuration Card Example
  slug: configuration-card-example
- key_count: 8
  name: Configuration Card Info Example
  slug: configuration-card-info-example
- key_count: 8
  name: Configuration Card Order Example
  slug: configuration-card-order-example
- key_count: 3
  name: Configuration Card Order Item Delivery Status Example
  slug: configuration-card-order-item-delivery-status-example
- key_count: 8
  name: Configuration Card Order Item Example
  slug: configuration-card-order-item-example
- key_count: 4
  name: Configuration Contact Details Example
  slug: configuration-contact-details-example
- key_count: 2
  name: Configuration Counterparty Bank Restriction Example
  slug: configuration-counterparty-bank-restriction-example
- key_count: 2
  name: Configuration Counterparty Example
  slug: configuration-counterparty-example
- key_count: 2
  name: Configuration Countries Restriction Example
  slug: configuration-countries-restriction-example
- key_count: 12
  name: Configuration Create Sweep Configuration V2 Example
  slug: configuration-create-sweep-configuration-v2-example
- key_count: 3
  name: Configuration Cz Local Account Identification Example
  slug: configuration-cz-local-account-identification-example
- key_count: 2
  name: Configuration Day Of Week Restriction Example
  slug: configuration-day-of-week-restriction-example
- key_count: 7
  name: Configuration Delivery Address Example
  slug: configuration-delivery-address-example
- key_count: 6
  name: Configuration Delivery Contact Example
  slug: configuration-delivery-contact-example
- key_count: 11
  name: Configuration Device Info Example
  slug: configuration-device-info-example
- key_count: 2
  name: Configuration Different Currencies Restriction Example
  slug: configuration-different-currencies-restriction-example
- key_count: 3
  name: Configuration Dk Local Account Identification Example
  slug: configuration-dk-local-account-identification-example
- key_count: 2
  name: Configuration Duration Example
  slug: configuration-duration-example
- key_count: 2
  name: Configuration Entry Modes Restriction Example
  slug: configuration-entry-modes-restriction-example
- key_count: 2
  name: Configuration Expiry Example
  slug: configuration-expiry-example
- key_count: 1
  name: Configuration Fee Example
  slug: configuration-fee-example
- key_count: 1
  name: Configuration Get Network Token Response Example
  slug: configuration-get-network-token-response-example
- key_count: 2
  name: Configuration Get Tax Form Response Example
  slug: configuration-get-tax-form-response-example
- key_count: 1
  name: Configuration Grant Limit Example
  slug: configuration-grant-limit-example
- key_count: 8
  name: Configuration Grant Offer Example
  slug: configuration-grant-offer-example
- key_count: 1
  name: Configuration Grant Offers Example
  slug: configuration-grant-offers-example
- key_count: 3
  name: Configuration Hk Local Account Identification Example
  slug: configuration-hk-local-account-identification-example
- key_count: 2
  name: Configuration Hu Local Account Identification Example
  slug: configuration-hu-local-account-identification-example
- key_count: 2
  name: Configuration Iban Account Identification Example
  slug: configuration-iban-account-identification-example
- key_count: 2
  name: Configuration International Transaction Restriction Example
  slug: configuration-international-transaction-restriction-example
- key_count: 3
  name: Configuration Invalid Field Example
  slug: configuration-invalid-field-example
- key_count: 0
  name: Configuration Json Object Example
  slug: configuration-json-object-example
- key_count: 1
  name: Configuration List Network Tokens Response Example
  slug: configuration-list-network-tokens-response-example
- key_count: 2
  name: Configuration Matching Transactions Restriction Example
  slug: configuration-matching-transactions-restriction-example
- key_count: 2
  name: Configuration Mccs Restriction Example
  slug: configuration-mccs-restriction-example
- key_count: 2
  name: Configuration Merchant Acquirer Pair Example
  slug: configuration-merchant-acquirer-pair-example
- key_count: 2
  name: Configuration Merchant Names Restriction Example
  slug: configuration-merchant-names-restriction-example
- key_count: 2
  name: Configuration Merchants Restriction Example
  slug: configuration-merchants-restriction-example
- key_count: 2
  name: Configuration Name Example
  slug: configuration-name-example
- key_count: 8
  name: Configuration Network Token Example
  slug: configuration-network-token-example
- key_count: 2
  name: Configuration No Local Account Identification Example
  slug: configuration-no-local-account-identification-example
- key_count: 4
  name: Configuration Number And Bic Account Identification Example
  slug: configuration-number-and-bic-account-identification-example
- key_count: 2
  name: Configuration Nz Local Account Identification Example
  slug: configuration-nz-local-account-identification-example
- key_count: 3
  name: Configuration Paginated Account Holders Response Example
  slug: configuration-paginated-account-holders-response-example
- key_count: 3
  name: Configuration Paginated Balance Accounts Response Example
  slug: configuration-paginated-balance-accounts-response-example
- key_count: 3
  name: Configuration Paginated Get Card Order Item Response Example
  slug: configuration-paginated-get-card-order-item-response-example
- key_count: 3
  name: Configuration Paginated Get Card Order Response Example
  slug: configuration-paginated-get-card-order-response-example
- key_count: 3
  name: Configuration Paginated Payment Instruments Response Example
  slug: configuration-paginated-payment-instruments-response-example
- key_count: 11
  name: Configuration Payment Instrument Example
  slug: configuration-payment-instrument-example
- key_count: 6
  name: Configuration Payment Instrument Group Example
  slug: configuration-payment-instrument-group-example
- key_count: 5
  name: Configuration Payment Instrument Group Info Example
  slug: configuration-payment-instrument-group-info-example
- key_count: 10
  name: Configuration Payment Instrument Info Example
  slug: configuration-payment-instrument-info-example
- key_count: 5
  name: Configuration Payment Instrument Requirement Example
  slug: configuration-payment-instrument-requirement-example
- key_count: 3
  name: Configuration Payment Instrument Reveal Info Example
  slug: configuration-payment-instrument-reveal-info-example
- key_count: 5
  name: Configuration Payment Instrument Update Request Example
  slug: configuration-payment-instrument-update-request-example
- key_count: 2
  name: Configuration Phone Example
  slug: configuration-phone-example
- key_count: 3
  name: Configuration Phone Number Example
  slug: configuration-phone-number-example
- key_count: 4
  name: Configuration Pin Change Request Example
  slug: configuration-pin-change-request-example
- key_count: 1
  name: Configuration Pin Change Response Example
  slug: configuration-pin-change-response-example
- key_count: 2
  name: Configuration Pl Local Account Identification Example
  slug: configuration-pl-local-account-identification-example
- key_count: 2
  name: Configuration Platform Payment Configuration Example
  slug: configuration-platform-payment-configuration-example
- key_count: 2
  name: Configuration Processing Types Restriction Example
  slug: configuration-processing-types-restriction-example
- key_count: 2
  name: Configuration Public Key Response Example
  slug: configuration-public-key-response-example
- key_count: 2
  name: Configuration Remediating Action Example
  slug: configuration-remediating-action-example
- key_count: 3
  name: Configuration Repayment Example
  slug: configuration-repayment-example
- key_count: 2
  name: Configuration Repayment Term Example
  slug: configuration-repayment-term-example
- key_count: 9
  name: Configuration Rest Service Error Example
  slug: configuration-rest-service-error-example
- key_count: 2
  name: Configuration Reveal Pin Request Example
  slug: configuration-reveal-pin-request-example
- key_count: 2
  name: Configuration Reveal Pin Response Example
  slug: configuration-reveal-pin-response-example
- key_count: 2
  name: Configuration Same Amount Restriction Example
  slug: configuration-same-amount-restriction-example
- key_count: 2
  name: Configuration Same Counterparty Restriction Example
  slug: configuration-same-counterparty-restriction-example
- key_count: 3
  name: Configuration Se Local Account Identification Example
  slug: configuration-se-local-account-identification-example
- key_count: 3
  name: Configuration Sg Local Account Identification Example
  slug: configuration-sg-local-account-identification-example
- key_count: 2
  name: Configuration String Match Example
  slug: configuration-string-match-example
- key_count: 13
  name: Configuration Sweep Configuration V2 Example
  slug: configuration-sweep-configuration-v2-example
- key_count: 3
  name: Configuration Sweep Counterparty Example
  slug: configuration-sweep-counterparty-example
- key_count: 2
  name: Configuration Sweep Schedule Example
  slug: configuration-sweep-schedule-example
- key_count: 1
  name: Configuration Threshold Repayment Example
  slug: configuration-threshold-repayment-example
- key_count: 2
  name: Configuration Time Of Day Example
  slug: configuration-time-of-day-example
- key_count: 2
  name: Configuration Time Of Day Restriction Example
  slug: configuration-time-of-day-restriction-example
- key_count: 2
  name: Configuration Total Amount Restriction Example
  slug: configuration-total-amount-restriction-example
- key_count: 2
  name: Configuration Transaction Rule Entity Key Example
  slug: configuration-transaction-rule-entity-key-example
- key_count: 14
  name: Configuration Transaction Rule Example
  slug: configuration-transaction-rule-example
- key_count: 13
  name: Configuration Transaction Rule Info Example
  slug: configuration-transaction-rule-info-example
- key_count: 6
  name: Configuration Transaction Rule Interval Example
  slug: configuration-transaction-rule-interval-example
- key_count: 1
  name: Configuration Transaction Rule Response Example
  slug: configuration-transaction-rule-response-example
- key_count: 17
  name: Configuration Transaction Rule Restrictions Example
  slug: configuration-transaction-rule-restrictions-example
- key_count: 1
  name: Configuration Transaction Rules Response Example
  slug: configuration-transaction-rules-response-example
- key_count: 5
  name: Configuration Transfer Route Example
  slug: configuration-transfer-route-example
- key_count: 7
  name: Configuration Transfer Route Request Example
  slug: configuration-transfer-route-request-example
- key_count: 1
  name: Configuration Transfer Route Response Example
  slug: configuration-transfer-route-response-example
- key_count: 3
  name: Configuration Uk Local Account Identification Example
  slug: configuration-uk-local-account-identification-example
- key_count: 1
  name: Configuration Update Network Token Request Example
  slug: configuration-update-network-token-request-example
- key_count: 12
  name: Configuration Update Payment Instrument Example
  slug: configuration-update-payment-instrument-example
- key_count: 13
  name: Configuration Update Sweep Configuration V2 Example
  slug: configuration-update-sweep-configuration-v2-example
- key_count: 4
  name: Configuration Us Local Account Identification Example
  slug: configuration-us-local-account-identification-example
- key_count: 3
  name: Configuration Verification Deadline Example
  slug: configuration-verification-deadline-example
- key_count: 6
  name: Configuration Verification Error Example
  slug: configuration-verification-error-example
- key_count: 5
  name: Configuration Verification Error Recursive Example
  slug: configuration-verification-error-recursive-example
- key_count: 10
  name: Configuration Webhooks Account Holder Capability Example
  slug: configuration-webhooks-account-holder-capability-example
- key_count: 13
  name: Configuration Webhooks Account Holder Example
  slug: configuration-webhooks-account-holder-example
- key_count: 2
  name: Configuration Webhooks Account Holder Notification Data Example
  slug: configuration-webhooks-account-holder-notification-data-example
- key_count: 3
  name: Configuration Webhooks Account Holder Notification Request Example
  slug: configuration-webhooks-account-holder-notification-request-example
- key_count: 7
  name: Configuration Webhooks Account Supporting Entity Capability Example
  slug: configuration-webhooks-account-supporting-entity-capability-example
- key_count: 6
  name: Configuration Webhooks Address Example
  slug: configuration-webhooks-address-example
- key_count: 2
  name: Configuration Webhooks Amount Example
  slug: configuration-webhooks-amount-example
- key_count: 3
  name: Configuration Webhooks Authentication Example
  slug: configuration-webhooks-authentication-example
- key_count: 12
  name: Configuration Webhooks Balance Account Example
  slug: configuration-webhooks-balance-account-example
- key_count: 2
  name: Configuration Webhooks Balance Account Notification Data Example
  slug: configuration-webhooks-balance-account-notification-data-example
- key_count: 3
  name: Configuration Webhooks Balance Account Notification Request Example
  slug: configuration-webhooks-balance-account-notification-request-example
- key_count: 5
  name: Configuration Webhooks Balance Example
  slug: configuration-webhooks-balance-example
- key_count: 1
  name: Configuration Webhooks Balance Platform Notification Response Example
  slug: configuration-webhooks-balance-platform-notification-response-example
- key_count: 9
  name: Configuration Webhooks Bulk Address Example
  slug: configuration-webhooks-bulk-address-example
- key_count: 4
  name: Configuration Webhooks Capability Problem Entity Example
  slug: configuration-webhooks-capability-problem-entity-example
- key_count: 3
  name: Configuration Webhooks Capability Problem Entity Recursive Example
  slug: configuration-webhooks-capability-problem-entity-recursive-example
- key_count: 2
  name: Configuration Webhooks Capability Problem Example
  slug: configuration-webhooks-capability-problem-example
- key_count: 5
  name: Configuration Webhooks Capability Settings Example
  slug: configuration-webhooks-capability-settings-example
- key_count: 14
  name: Configuration Webhooks Card Configuration Example
  slug: configuration-webhooks-card-configuration-example
- key_count: 13
  name: Configuration Webhooks Card Example
  slug: configuration-webhooks-card-example
- key_count: 3
  name: Configuration Webhooks Card Order Item Delivery Status Example
  slug: configuration-webhooks-card-order-item-delivery-status-example
- key_count: 8
  name: Configuration Webhooks Card Order Item Example
  slug: configuration-webhooks-card-order-item-example
- key_count: 3
  name: Configuration Webhooks Card Order Notification Request Example
  slug: configuration-webhooks-card-order-notification-request-example
- key_count: 4
  name: Configuration Webhooks Contact Details Example
  slug: configuration-webhooks-contact-details-example
- key_count: 7
  name: Configuration Webhooks Contact Example
  slug: configuration-webhooks-contact-example
- key_count: 2
  name: Configuration Webhooks Expiry Example
  slug: configuration-webhooks-expiry-example
- key_count: 2
  name: Configuration Webhooks Iban Account Identification Example
  slug: configuration-webhooks-iban-account-identification-example
- key_count: 2
  name: Configuration Webhooks Name Example
  slug: configuration-webhooks-name-example
- key_count: 10
  name: Configuration Webhooks Payment Instrument Example
  slug: configuration-webhooks-payment-instrument-example
- key_count: 2
  name: Configuration Webhooks Payment Instrument Notification Data Example
  slug: configuration-webhooks-payment-instrument-notification-data-example
- key_count: 1
  name: Configuration Webhooks Payment Instrument Reference Example
  slug: configuration-webhooks-payment-instrument-reference-example
- key_count: 3
  name: Configuration Webhooks Payment Notification Request Example
  slug: configuration-webhooks-payment-notification-request-example
- key_count: 3
  name: Configuration Webhooks Personal Data Example
  slug: configuration-webhooks-personal-data-example
- key_count: 2
  name: Configuration Webhooks Phone Example
  slug: configuration-webhooks-phone-example
- key_count: 3
  name: Configuration Webhooks Phone Number Example
  slug: configuration-webhooks-phone-number-example
- key_count: 2
  name: Configuration Webhooks Platform Payment Configuration Example
  slug: configuration-webhooks-platform-payment-configuration-example
- key_count: 2
  name: Configuration Webhooks Remediating Action Example
  slug: configuration-webhooks-remediating-action-example
- key_count: 3
  name: Configuration Webhooks Resource Example
  slug: configuration-webhooks-resource-example
- key_count: 3
  name: Configuration Webhooks Sweep Configuration Notification Data Example
  slug: configuration-webhooks-sweep-configuration-notification-data-example
- key_count: 3
  name: Configuration Webhooks Sweep Configuration Notification Request Example
  slug: configuration-webhooks-sweep-configuration-notification-request-example
- key_count: 11
  name: Configuration Webhooks Sweep Configuration V2 Example
  slug: configuration-webhooks-sweep-configuration-v2-example
- key_count: 3
  name: Configuration Webhooks Sweep Counterparty Example
  slug: configuration-webhooks-sweep-counterparty-example
- key_count: 2
  name: Configuration Webhooks Sweep Schedule Example
  slug: configuration-webhooks-sweep-schedule-example
- key_count: 4
  name: Configuration Webhooks Us Local Account Identification Example
  slug: configuration-webhooks-us-local-account-identification-example
- key_count: 3
  name: Configuration Webhooks Verification Deadline Example
  slug: configuration-webhooks-verification-deadline-example
- key_count: 6
  name: Configuration Webhooks Verification Error Example
  slug: configuration-webhooks-verification-error-example
- key_count: 5
  name: Configuration Webhooks Verification Error Recursive Example
  slug: configuration-webhooks-verification-error-recursive-example
- key_count: 3
  name: Data Protection Subject Erasure By Psp Reference Request Example
  slug: data-protection-subject-erasure-by-psp-reference-request-example
- key_count: 1
  name: Data Protection Subject Erasure Response Example
  slug: data-protection-subject-erasure-response-example
- key_count: 2
  name: Disputes Accept Dispute Request Example
  slug: disputes-accept-dispute-request-example
- key_count: 1
  name: Disputes Accept Dispute Response Example
  slug: disputes-accept-dispute-response-example
- key_count: 3
  name: Disputes Defend Dispute Request Example
  slug: disputes-defend-dispute-request-example
- key_count: 1
  name: Disputes Defend Dispute Response Example
  slug: disputes-defend-dispute-response-example
- key_count: 3
  name: Disputes Defense Document Example
  slug: disputes-defense-document-example
- key_count: 3
  name: Disputes Defense Document Type Example
  slug: disputes-defense-document-type-example
- key_count: 3
  name: Disputes Defense Reason Example
  slug: disputes-defense-reason-example
- key_count: 2
  name: Disputes Defense Reasons Request Example
  slug: disputes-defense-reasons-request-example
- key_count: 2
  name: Disputes Defense Reasons Response Example
  slug: disputes-defense-reasons-response-example
- key_count: 3
  name: Disputes Delete Defense Document Request Example
  slug: disputes-delete-defense-document-request-example
- key_count: 1
  name: Disputes Delete Defense Document Response Example
  slug: disputes-delete-defense-document-response-example
- key_count: 2
  name: Disputes Dispute Service Result Example
  slug: disputes-dispute-service-result-example
- key_count: 3
  name: Disputes Supply Defense Document Request Example
  slug: disputes-supply-defense-document-request-example
- key_count: 1
  name: Disputes Supply Defense Document Response Example
  slug: disputes-supply-defense-document-response-example
- key_count: 2
  name: Funds Account Detail Balance Example
  slug: funds-account-detail-balance-example
- key_count: 1
  name: Funds Account Holder Balance Request Example
  slug: funds-account-holder-balance-request-example
- key_count: 5
  name: Funds Account Holder Balance Response Example
  slug: funds-account-holder-balance-response-example
- key_count: 3
  name: Funds Account Holder Transaction List Request Example
  slug: funds-account-holder-transaction-list-request-example
- key_count: 4
  name: Funds Account Holder Transaction List Response Example
  slug: funds-account-holder-transaction-list-response-example
- key_count: 3
  name: Funds Account Transaction List Example
  slug: funds-account-transaction-list-example
- key_count: 2
  name: Funds Amount Example
  slug: funds-amount-example
- key_count: 26
  name: Funds Bank Account Detail Example
  slug: funds-bank-account-detail-example
- key_count: 6
  name: Funds Debit Account Holder Request Example
  slug: funds-debit-account-holder-request-example
- key_count: 6
  name: Funds Debit Account Holder Response Example
  slug: funds-debit-account-holder-response-example
- key_count: 3
  name: Funds Detail Balance Example
  slug: funds-detail-balance-example
- key_count: 3
  name: Funds Error Field Type Example
  slug: funds-error-field-type-example
- key_count: 3
  name: Funds Field Type Example
  slug: funds-field-type-example
- key_count: 8
  name: Funds Payout Account Holder Request Example
  slug: funds-payout-account-holder-request-example
- key_count: 6
  name: Funds Payout Account Holder Response Example
  slug: funds-payout-account-holder-response-example
- key_count: 3
  name: Funds Refund Funds Transfer Request Example
  slug: funds-refund-funds-transfer-request-example
- key_count: 6
  name: Funds Refund Funds Transfer Response Example
  slug: funds-refund-funds-transfer-response-example
- key_count: 2
  name: Funds Refund Not Paid Out Transfers Request Example
  slug: funds-refund-not-paid-out-transfers-request-example
- key_count: 3
  name: Funds Refund Not Paid Out Transfers Response Example
  slug: funds-refund-not-paid-out-transfers-response-example
- key_count: 3
  name: Funds Setup Beneficiary Request Example
  slug: funds-setup-beneficiary-request-example
- key_count: 3
  name: Funds Setup Beneficiary Response Example
  slug: funds-setup-beneficiary-response-example
- key_count: 2
  name: Funds Split Amount Example
  slug: funds-split-amount-example
- key_count: 5
  name: Funds Split Example
  slug: funds-split-example
- key_count: 16
  name: Funds Transaction Example
  slug: funds-transaction-example
- key_count: 2
  name: Funds Transaction List For Account Example
  slug: funds-transaction-list-for-account-example
- key_count: 5
  name: Funds Transfer Funds Request Example
  slug: funds-transfer-funds-request-example
- key_count: 4
  name: Funds Transfer Funds Response Example
  slug: funds-transfer-funds-response-example
- key_count: 6
  name: Hosted Onboarding Collect Information Example
  slug: hosted-onboarding-collect-information-example
- key_count: 3
  name: Hosted Onboarding Error Field Type Example
  slug: hosted-onboarding-error-field-type-example
- key_count: 3
  name: Hosted Onboarding Field Type Example
  slug: hosted-onboarding-field-type-example
- key_count: 8
  name: Hosted Onboarding Get Onboarding Url Request Example
  slug: hosted-onboarding-get-onboarding-url-request-example
- key_count: 4
  name: Hosted Onboarding Get Onboarding Url Response Example
  slug: hosted-onboarding-get-onboarding-url-response-example
- key_count: 2
  name: Hosted Onboarding Get Pci Url Request Example
  slug: hosted-onboarding-get-pci-url-request-example
- key_count: 4
  name: Hosted Onboarding Get Pci Url Response Example
  slug: hosted-onboarding-get-pci-url-response-example
- key_count: 9
  name: Hosted Onboarding Show Pages Example
  slug: hosted-onboarding-show-pages-example
- key_count: 2
  name: Legal Entity Accept Terms Of Service Request Example
  slug: legal-entity-accept-terms-of-service-request-example
- key_count: 6
  name: Legal Entity Accept Terms Of Service Response Example
  slug: legal-entity-accept-terms-of-service-response-example
- key_count: 2
  name: Legal Entity Additional Bank Identification Example
  slug: legal-entity-additional-bank-identification-example
- key_count: 6
  name: Legal Entity Address Example
  slug: legal-entity-address-example
- key_count: 2
  name: Legal Entity Amount Example
  slug: legal-entity-amount-example
- key_count: 5
  name: Legal Entity Attachment Example
  slug: legal-entity-attachment-example
- key_count: 3
  name: Legal Entity Au Local Account Identification Example
  slug: legal-entity-au-local-account-identification-example
- key_count: 5
  name: Legal Entity Bank Account Info Example
  slug: legal-entity-bank-account-info-example
- key_count: 1
  name: Legal Entity Birth Data Example
  slug: legal-entity-birth-data-example
- key_count: 10
  name: Legal Entity Business Line Example
  slug: legal-entity-business-line-example
- key_count: 8
  name: Legal Entity Business Line Info Example
  slug: legal-entity-business-line-info-example
- key_count: 8
  name: Legal Entity Business Line Info Update Example
  slug: legal-entity-business-line-info-update-example
- key_count: 1
  name: Legal Entity Business Lines Example
  slug: legal-entity-business-lines-example
- key_count: 5
  name: Legal Entity Ca Local Account Identification Example
  slug: legal-entity-ca-local-account-identification-example
- key_count: 1
  name: Legal Entity Calculate Terms Of Service Status Response Example
  slug: legal-entity-calculate-terms-of-service-status-response-example
- key_count: 4
  name: Legal Entity Capability Problem Entity Example
  slug: legal-entity-capability-problem-entity-example
- key_count: 3
  name: Legal Entity Capability Problem Entity Recursive Example
  slug: legal-entity-capability-problem-entity-recursive-example
- key_count: 2
  name: Legal Entity Capability Problem Example
  slug: legal-entity-capability-problem-example
- key_count: 5
  name: Legal Entity Capability Settings Example
  slug: legal-entity-capability-settings-example
- key_count: 3
  name: Legal Entity Cz Local Account Identification Example
  slug: legal-entity-cz-local-account-identification-example
- key_count: 1
  name: Legal Entity Data Review Confirmation Response Example
  slug: legal-entity-data-review-confirmation-response-example
- key_count: 3
  name: Legal Entity Dk Local Account Identification Example
  slug: legal-entity-dk-local-account-identification-example
- key_count: 13
  name: Legal Entity Document Example
  slug: legal-entity-document-example
- key_count: 3
  name: Legal Entity Document Page Example
  slug: legal-entity-document-page-example
- key_count: 7
  name: Legal Entity Document Reference Example
  slug: legal-entity-document-reference-example
- key_count: 1
  name: Legal Entity Entity Reference Example
  slug: legal-entity-entity-reference-example
- key_count: 2
  name: Legal Entity Generate Pci Description Request Example
  slug: legal-entity-generate-pci-description-request-example
- key_count: 3
  name: Legal Entity Generate Pci Description Response Example
  slug: legal-entity-generate-pci-description-response-example
- key_count: 1
  name: Legal Entity Get Pci Questionnaire Infos Response Example
  slug: legal-entity-get-pci-questionnaire-infos-response-example
- key_count: 4
  name: Legal Entity Get Pci Questionnaire Response Example
  slug: legal-entity-get-pci-questionnaire-response-example
- key_count: 1
  name: Legal Entity Get Terms Of Service Acceptance Infos Response Example
  slug: legal-entity-get-terms-of-service-acceptance-infos-response-example
- key_count: 2
  name: Legal Entity Get Terms Of Service Document Request Example
  slug: legal-entity-get-terms-of-service-document-request-example
- key_count: 5
  name: Legal Entity Get Terms Of Service Document Response Example
  slug: legal-entity-get-terms-of-service-document-response-example
- key_count: 3
  name: Legal Entity Hk Local Account Identification Example
  slug: legal-entity-hk-local-account-identification-example
- key_count: 2
  name: Legal Entity Hu Local Account Identification Example
  slug: legal-entity-hu-local-account-identification-example
- key_count: 2
  name: Legal Entity Iban Account Identification Example
  slug: legal-entity-iban-account-identification-example
- key_count: 7
  name: Legal Entity Identification Data Example
  slug: legal-entity-identification-data-example
- key_count: 9
  name: Legal Entity Individual Example
  slug: legal-entity-individual-example
- key_count: 7
  name: Legal Entity Legal Entity Association Example
  slug: legal-entity-legal-entity-association-example
- key_count: 8
  name: Legal Entity Legal Entity Capability Example
  slug: legal-entity-legal-entity-capability-example
- key_count: 16
  name: Legal Entity Legal Entity Example
  slug: legal-entity-legal-entity-example
- key_count: 10
  name: Legal Entity Legal Entity Info Example
  slug: legal-entity-legal-entity-info-example
- key_count: 10
  name: Legal Entity Legal Entity Info Required Type Example
  slug: legal-entity-legal-entity-info-required-type-example
- key_count: 3
  name: Legal Entity Name Example
  slug: legal-entity-name-example
- key_count: 2
  name: Legal Entity No Local Account Identification Example
  slug: legal-entity-no-local-account-identification-example
- key_count: 4
  name: Legal Entity Number And Bic Account Identification Example
  slug: legal-entity-number-and-bic-account-identification-example
- key_count: 2
  name: Legal Entity Nz Local Account Identification Example
  slug: legal-entity-nz-local-account-identification-example
- key_count: 1
  name: Legal Entity Onboarding Link Example
  slug: legal-entity-onboarding-link-example
- key_count: 4
  name: Legal Entity Onboarding Link Info Example
  slug: legal-entity-onboarding-link-info-example
- key_count: 5
  name: Legal Entity Onboarding Theme Example
  slug: legal-entity-onboarding-theme-example
- key_count: 3
  name: Legal Entity Onboarding Themes Example
  slug: legal-entity-onboarding-themes-example
- key_count: 16
  name: Legal Entity Organization Example
  slug: legal-entity-organization-example
- key_count: 2
  name: Legal Entity Owner Entity Example
  slug: legal-entity-owner-entity-example
- key_count: 3
  name: Legal Entity Pci Document Info Example
  slug: legal-entity-pci-document-info-example
- key_count: 2
  name: Legal Entity Pci Signing Request Example
  slug: legal-entity-pci-signing-request-example
- key_count: 2
  name: Legal Entity Pci Signing Response Example
  slug: legal-entity-pci-signing-response-example
- key_count: 2
  name: Legal Entity Phone Number Example
  slug: legal-entity-phone-number-example
- key_count: 2
  name: Legal Entity Pl Local Account Identification Example
  slug: legal-entity-pl-local-account-identification-example
- key_count: 2
  name: Legal Entity Remediating Action Example
  slug: legal-entity-remediating-action-example
- key_count: 3
  name: Legal Entity Se Local Account Identification Example
  slug: legal-entity-se-local-account-identification-example
- key_count: 3
  name: Legal Entity Sg Local Account Identification Example
  slug: legal-entity-sg-local-account-identification-example
- key_count: 11
  name: Legal Entity Sole Proprietorship Example
  slug: legal-entity-sole-proprietorship-example
- key_count: 4
  name: Legal Entity Source Of Funds Example
  slug: legal-entity-source-of-funds-example
- key_count: 3
  name: Legal Entity Stock Data Example
  slug: legal-entity-stock-data-example
- key_count: 4
  name: Legal Entity Supporting Entity Capability Example
  slug: legal-entity-supporting-entity-capability-example
- key_count: 3
  name: Legal Entity Tax Information Example
  slug: legal-entity-tax-information-example
- key_count: 4
  name: Legal Entity Tax Reporting Classification Example
  slug: legal-entity-tax-reporting-classification-example
- key_count: 5
  name: Legal Entity Terms Of Service Acceptance Info Example
  slug: legal-entity-terms-of-service-acceptance-info-example
- key_count: 7
  name: Legal Entity Transfer Instrument Example
  slug: legal-entity-transfer-instrument-example
- key_count: 3
  name: Legal Entity Transfer Instrument Info Example
  slug: legal-entity-transfer-instrument-info-example
- key_count: 4
  name: Legal Entity Transfer Instrument Reference Example
  slug: legal-entity-transfer-instrument-reference-example
- key_count: 13
  name: Legal Entity Trust Example
  slug: legal-entity-trust-example
- key_count: 3
  name: Legal Entity Uk Local Account Identification Example
  slug: legal-entity-uk-local-account-identification-example
- key_count: 2
  name: Legal Entity Undefined Beneficiary Example
  slug: legal-entity-undefined-beneficiary-example
- key_count: 12
  name: Legal Entity Unincorporated Partnership Example
  slug: legal-entity-unincorporated-partnership-example
- key_count: 4
  name: Legal Entity Us Local Account Identification Example
  slug: legal-entity-us-local-account-identification-example
- key_count: 3
  name: Legal Entity Verification Deadline Example
  slug: legal-entity-verification-deadline-example
- key_count: 6
  name: Legal Entity Verification Error Example
  slug: legal-entity-verification-error-example
- key_count: 5
  name: Legal Entity Verification Error Recursive Example
  slug: legal-entity-verification-error-recursive-example
- key_count: 1
  name: Legal Entity Verification Errors Example
  slug: legal-entity-verification-errors-example
- key_count: 2
  name: Legal Entity Web Data Example
  slug: legal-entity-web-data-example
- key_count: 1
  name: Legal Entity Web Data Exemption Example
  slug: legal-entity-web-data-exemption-example
- key_count: 3
  name: Management Additional Commission Example
  slug: management-additional-commission-example
- key_count: 2
  name: Management Additional Settings Example
  slug: management-additional-settings-example
- key_count: 3
  name: Management Additional Settings Response Example
  slug: management-additional-settings-response-example
- key_count: 7
  name: Management Address Example
  slug: management-address-example
- key_count: 1
  name: Management Afterpay Touch Info Example
  slug: management-afterpay-touch-info-example
- key_count: 3
  name: Management Allowed Origin Example
  slug: management-allowed-origin-example
- key_count: 1
  name: Management Allowed Origins Response Example
  slug: management-allowed-origins-response-example
- key_count: 2
  name: Management Amount Example
  slug: management-amount-example
- key_count: 8
  name: Management Android App Example
  slug: management-android-app-example
- key_count: 1
  name: Management Android Apps Response Example
  slug: management-android-apps-response-example
- key_count: 7
  name: Management Android Certificate Example
  slug: management-android-certificate-example
- key_count: 1
  name: Management Android Certificates Response Example
  slug: management-android-certificates-response-example
- key_count: 9
  name: Management Api Credential Example
  slug: management-api-credential-example
- key_count: 6
  name: Management Api Credential Links Example
  slug: management-api-credential-links-example
- key_count: 1
  name: Management Apple Pay Info Example
  slug: management-apple-pay-info-example
- key_count: 2
  name: Management Bcmc Info Example
  slug: management-bcmc-info-example
- key_count: 1
  name: Management Billing Entities Response Example
  slug: management-billing-entities-response-example
- key_count: 5
  name: Management Billing Entity Example
  slug: management-billing-entity-example
- key_count: 1
  name: Management Cardholder Receipt Example
  slug: management-cardholder-receipt-example
- key_count: 2
  name: Management Cartes Bancaires Info Example
  slug: management-cartes-bancaires-info-example
- key_count: 1
  name: Management Clearpay Info Example
  slug: management-clearpay-info-example
- key_count: 2
  name: Management Commission Example
  slug: management-commission-example
- key_count: 10
  name: Management Company Api Credential Example
  slug: management-company-api-credential-example
- key_count: 7
  name: Management Company Example
  slug: management-company-example
- key_count: 4
  name: Management Company Links Example
  slug: management-company-links-example
- key_count: 11
  name: Management Company User Example
  slug: management-company-user-example
- key_count: 4
  name: Management Configuration Example
  slug: management-configuration-example
- key_count: 1
  name: Management Connectivity Example
  slug: management-connectivity-example
- key_count: 5
  name: Management Contact Example
  slug: management-contact-example
- key_count: 3
  name: Management Create Allowed Origin Request Example
  slug: management-create-allowed-origin-request-example
- key_count: 11
  name: Management Create Api Credential Response Example
  slug: management-create-api-credential-response-example
- key_count: 4
  name: Management Create Company Api Credential Request Example
  slug: management-create-company-api-credential-request-example
- key_count: 12
  name: Management Create Company Api Credential Response Example
  slug: management-create-company-api-credential-response-example
- key_count: 7
  name: Management Create Company User Request Example
  slug: management-create-company-user-request-example
- key_count: 11
  name: Management Create Company User Response Example
  slug: management-create-company-user-response-example
- key_count: 16
  name: Management Create Company Webhook Request Example
  slug: management-create-company-webhook-request-example
- key_count: 3
  name: Management Create Merchant Api Credential Request Example
  slug: management-create-merchant-api-credential-request-example
- key_count: 7
  name: Management Create Merchant Request Example
  slug: management-create-merchant-request-example
- key_count: 7
  name: Management Create Merchant Response Example
  slug: management-create-merchant-response-example
- key_count: 6
  name: Management Create Merchant User Request Example
  slug: management-create-merchant-user-request-example
- key_count: 14
  name: Management Create Merchant Webhook Request Example
  slug: management-create-merchant-webhook-request-example
- key_count: 10
  name: Management Create User Response Example
  slug: management-create-user-response-example
- key_count: 3
  name: Management Currency Example
  slug: management-currency-example
- key_count: 7
  name: Management Custom Notification Example
  slug: management-custom-notification-example
- key_count: 2
  name: Management Data Center Example
  slug: management-data-center-example
- key_count: 2
  name: Management Event Url Example
  slug: management-event-url-example
- key_count: 8
  name: Management External Terminal Action Example
  slug: management-external-terminal-action-example
- key_count: 2
  name: Management File Example
  slug: management-file-example
- key_count: 1
  name: Management Generate Api Key Response Example
  slug: management-generate-api-key-response-example
- key_count: 1
  name: Management Generate Client Key Response Example
  slug: management-generate-client-key-response-example
- key_count: 1
  name: Management Generate Hmac Key Response Example
  slug: management-generate-hmac-key-response-example
- key_count: 1
  name: Management Generic Pm With Tdi Info Example
  slug: management-generic-pm-with-tdi-info-example
- key_count: 1
  name: Management Giro Pay Info Example
  slug: management-giro-pay-info-example
- key_count: 2
  name: Management Google Pay Info Example
  slug: management-google-pay-info-example
- key_count: 4
  name: Management Gratuity Example
  slug: management-gratuity-example
- key_count: 3
  name: Management Hardware Example
  slug: management-hardware-example
- key_count: 2
  name: Management Id Name Example
  slug: management-id-name-example
- key_count: 2
  name: Management Install Android App Details Example
  slug: management-install-android-app-details-example
- key_count: 2
  name: Management Install Android Certificate Details Example
  slug: management-install-android-certificate-details-example
- key_count: 3
  name: Management Invalid Field Example
  slug: management-invalid-field-example
- key_count: 0
  name: Management Json Object Example
  slug: management-json-object-example
- key_count: 3
  name: Management Key Example
  slug: management-key-example
- key_count: 4
  name: Management Klarna Info Example
  slug: management-klarna-info-example
- key_count: 1
  name: Management Links Element Example
  slug: management-links-element-example
- key_count: 1
  name: Management Links Example
  slug: management-links-example
- key_count: 4
  name: Management List Company Api Credentials Response Example
  slug: management-list-company-api-credentials-response-example
- key_count: 4
  name: Management List Company Response Example
  slug: management-list-company-response-example
- key_count: 4
  name: Management List Company Users Response Example
  slug: management-list-company-users-response-example
- key_count: 1
  name: Management List External Terminal Actions Response Example
  slug: management-list-external-terminal-actions-response-example
- key_count: 4
  name: Management List Merchant Api Credentials Response Example
  slug: management-list-merchant-api-credentials-response-example
- key_count: 4
  name: Management List Merchant Response Example
  slug: management-list-merchant-response-example
- key_count: 4
  name: Management List Merchant Users Response Example
  slug: management-list-merchant-users-response-example
- key_count: 4
  name: Management List Stores Response Example
  slug: management-list-stores-response-example
- key_count: 4
  name: Management List Terminals Response Example
  slug: management-list-terminals-response-example
- key_count: 5
  name: Management List Webhooks Response Example
  slug: management-list-webhooks-response-example
- key_count: 3
  name: Management Localization Example
  slug: management-localization-example
- key_count: 1
  name: Management Logo Example
  slug: management-logo-example
- key_count: 11
  name: Management Me Api Credential Example
  slug: management-me-api-credential-example
- key_count: 3
  name: Management Meal Voucher Fr Info Example
  slug: management-meal-voucher-fr-info-example
- key_count: 14
  name: Management Merchant Example
  slug: management-merchant-example
- key_count: 4
  name: Management Merchant Links Example
  slug: management-merchant-links-example
- key_count: 2
  name: Management Minor Units Monetary Value Example
  slug: management-minor-units-monetary-value-example
- key_count: 2
  name: Management Name Example
  slug: management-name-example
- key_count: 2
  name: Management Name2 Example
  slug: management-name2-example
- key_count: 5
  name: Management Nexo Example
  slug: management-nexo-example
- key_count: 5
  name: Management Notification Example
  slug: management-notification-example
- key_count: 2
  name: Management Notification Url Example
  slug: management-notification-url-example
- key_count: 2
  name: Management Offline Processing Example
  slug: management-offline-processing-example
- key_count: 3
  name: Management Opi Example
  slug: management-opi-example
- key_count: 4
  name: Management Order Item Example
  slug: management-order-item-example
- key_count: 5
  name: Management Pagination Links Example
  slug: management-pagination-links-example
- key_count: 4
  name: Management Passcodes Example
  slug: management-passcodes-example
- key_count: 3
  name: Management Pay At Table Example
  slug: management-pay-at-table-example
- key_count: 3
  name: Management Pay Pal Info Example
  slug: management-pay-pal-info-example
- key_count: 2
  name: Management Payment Example
  slug: management-payment-example
- key_count: 37
  name: Management Payment Method Example
  slug: management-payment-method-example
- key_count: 5
  name: Management Payment Method Response Example
  slug: management-payment-method-response-example
- key_count: 33
  name: Management Payment Method Setup Info Example
  slug: management-payment-method-setup-info-example
- key_count: 7
  name: Management Payout Settings Example
  slug: management-payout-settings-example
- key_count: 3
  name: Management Payout Settings Request Example
  slug: management-payout-settings-request-example
- key_count: 1
  name: Management Payout Settings Response Example
  slug: management-payout-settings-response-example
- key_count: 18
  name: Management Profile Example
  slug: management-profile-example
- key_count: 3
  name: Management Receipt Options Example
  slug: management-receipt-options-example
- key_count: 16
  name: Management Receipt Printing Example
  slug: management-receipt-printing-example
- key_count: 1
  name: Management Referenced Example
  slug: management-referenced-example
- key_count: 1
  name: Management Refunds Example
  slug: management-refunds-example
- key_count: 2
  name: Management Release Update Details Example
  slug: management-release-update-details-example
- key_count: 2
  name: Management Request Activation Response Example
  slug: management-request-activation-response-example
- key_count: 9
  name: Management Rest Service Error Example
  slug: management-rest-service-error-example
- key_count: 4
  name: Management Schedule Terminal Actions Request Example
  slug: management-schedule-terminal-actions-request-example
- key_count: 7
  name: Management Schedule Terminal Actions Response Example
  slug: management-schedule-terminal-actions-response-example
- key_count: 3
  name: Management Settings Example
  slug: management-settings-example
- key_count: 4
  name: Management Shipping Location Example
  slug: management-shipping-location-example
- key_count: 1
  name: Management Shipping Locations Response Example
  slug: management-shipping-locations-response-example
- key_count: 4
  name: Management Signature Example
  slug: management-signature-example
- key_count: 2
  name: Management Sofort Info Example
  slug: management-sofort-info-example
- key_count: 4
  name: Management Split Configuration Example
  slug: management-split-configuration-example
- key_count: 1
  name: Management Split Configuration List Example
  slug: management-split-configuration-list-example
- key_count: 15
  name: Management Split Configuration Logic Example
  slug: management-split-configuration-logic-example
- key_count: 6
  name: Management Split Configuration Rule Example
  slug: management-split-configuration-rule-example
- key_count: 2
  name: Management Standalone Example
  slug: management-standalone-example
- key_count: 8
  name: Management Store Creation Request Example
  slug: management-store-creation-request-example
- key_count: 9
  name: Management Store Creation With Merchant Code Request Example
  slug: management-store-creation-with-merchant-code-request-example
- key_count: 12
  name: Management Store Example
  slug: management-store-example
- key_count: 7
  name: Management Store Location Example
  slug: management-store-location-example
- key_count: 2
  name: Management Store Split Configuration Example
  slug: management-store-split-configuration-example
- key_count: 2
  name: Management Surcharge Example
  slug: management-surcharge-example
- key_count: 1
  name: Management Swish Info Example
  slug: management-swish-info-example
- key_count: 1
  name: Management Tap To Pay Example
  slug: management-tap-to-pay-example
- key_count: 2
  name: Management Terminal Action Schedule Detail Example
  slug: management-terminal-action-schedule-detail-example
- key_count: 5
  name: Management Terminal Assignment Example
  slug: management-terminal-assignment-example
- key_count: 2
  name: Management Terminal Connectivity Bluetooth Example
  slug: management-terminal-connectivity-bluetooth-example
- key_count: 2
  name: Management Terminal Connectivity Cellular Example
  slug: management-terminal-connectivity-cellular-example
- key_count: 3
  name: Management Terminal Connectivity Ethernet Example
  slug: management-terminal-connectivity-ethernet-example
- key_count: 4
  name: Management Terminal Connectivity Example
  slug: management-terminal-connectivity-example
- key_count: 3
  name: Management Terminal Connectivity Wifi Example
  slug: management-terminal-connectivity-wifi-example
- key_count: 8
  name: Management Terminal Example
  slug: management-terminal-example
- key_count: 1
  name: Management Terminal Models Response Example
  slug: management-terminal-models-response-example
- key_count: 8
  name: Management Terminal Order Example
  slug: management-terminal-order-example
- key_count: 6
  name: Management Terminal Order Request Example
  slug: management-terminal-order-request-example
- key_count: 1
  name: Management Terminal Orders Response Example
  slug: management-terminal-orders-response-example
- key_count: 5
  name: Management Terminal Product Example
  slug: management-terminal-product-example
- key_count: 2
  name: Management Terminal Product Price Example
  slug: management-terminal-product-price-example
- key_count: 1
  name: Management Terminal Products Response Example
  slug: management-terminal-products-response-example
- key_count: 4
  name: Management Terminal Reassignment Request Example
  slug: management-terminal-reassignment-request-example
- key_count: 4
  name: Management Terminal Reassignment Target Example
  slug: management-terminal-reassignment-target-example
- key_count: 20
  name: Management Terminal Settings Example
  slug: management-terminal-settings-example
- key_count: 3
  name: Management Test Company Webhook Request Example
  slug: management-test-company-webhook-request-example
- key_count: 6
  name: Management Test Output Example
  slug: management-test-output-example
- key_count: 2
  name: Management Test Webhook Request Example
  slug: management-test-webhook-request-example
- key_count: 1
  name: Management Test Webhook Response Example
  slug: management-test-webhook-response-example
- key_count: 1
  name: Management Timeouts Example
  slug: management-timeouts-example
- key_count: 2
  name: Management Transaction Description Info Example
  slug: management-transaction-description-info-example
- key_count: 1
  name: Management Twint Info Example
  slug: management-twint-info-example
- key_count: 2
  name: Management Uninstall Android App Details Example
  slug: management-uninstall-android-app-details-example
- key_count: 2
  name: Management Uninstall Android Certificate Details Example
  slug: management-uninstall-android-certificate-details-example
- key_count: 6
  name: Management Updatable Address Example
  slug: management-updatable-address-example
- key_count: 5
  name: Management Update Company Api Credential Request Example
  slug: management-update-company-api-credential-request-example
- key_count: 7
  name: Management Update Company User Request Example
  slug: management-update-company-user-request-example
- key_count: 15
  name: Management Update Company Webhook Request Example
  slug: management-update-company-webhook-request-example
- key_count: 4
  name: Management Update Merchant Api Credential Request Example
  slug: management-update-merchant-api-credential-request-example
- key_count: 6
  name: Management Update Merchant User Request Example
  slug: management-update-merchant-user-request-example
- key_count: 13
  name: Management Update Merchant Webhook Request Example
  slug: management-update-merchant-webhook-request-example
- key_count: 18
  name: Management Update Payment Method Info Example
  slug: management-update-payment-method-info-example
- key_count: 1
  name: Management Update Payout Settings Request Example
  slug: management-update-payout-settings-request-example
- key_count: 15
  name: Management Update Split Configuration Logic Request Example
  slug: management-update-split-configuration-logic-request-example
- key_count: 1
  name: Management Update Split Configuration Request Example
  slug: management-update-split-configuration-request-example
- key_count: 4
  name: Management Update Split Configuration Rule Request Example
  slug: management-update-split-configuration-rule-request-example
- key_count: 7
  name: Management Update Store Request Example
  slug: management-update-store-request-example
- key_count: 1
  name: Management Upload Android App Response Example
  slug: management-upload-android-app-response-example
- key_count: 4
  name: Management Url Example
  slug: management-url-example
- key_count: 10
  name: Management User Example
  slug: management-user-example
- key_count: 2
  name: Management Vipps Info Example
  slug: management-vipps-info-example
- key_count: 22
  name: Management Webhook Example
  slug: management-webhook-example
- key_count: 5
  name: Management Webhook Links Example
  slug: management-webhook-links-example
- key_count: 8
  name: Management Webhooks Account Capability Data Example
  slug: management-webhooks-account-capability-data-example
- key_count: 5
  name: Management Webhooks Account Create Notification Data Example
  slug: management-webhooks-account-create-notification-data-example
- key_count: 1
  name: Management Webhooks Account Notification Response Example
  slug: management-webhooks-account-notification-response-example
- key_count: 4
  name: Management Webhooks Account Update Notification Data Example
  slug: management-webhooks-account-update-notification-data-example
- key_count: 4
  name: Management Webhooks Capability Problem Entity Example
  slug: management-webhooks-capability-problem-entity-example
- key_count: 3
  name: Management Webhooks Capability Problem Entity Recursive Example
  slug: management-webhooks-capability-problem-entity-recursive-example
- key_count: 2
  name: Management Webhooks Capability Problem Example
  slug: management-webhooks-capability-problem-example
- key_count: 4
  name: Management Webhooks Merchant Created Notification Request Example
  slug: management-webhooks-merchant-created-notification-request-example
- key_count: 4
  name: Management Webhooks Merchant Updated Notification Request Example
  slug: management-webhooks-merchant-updated-notification-request-example
- key_count: 9
  name: Management Webhooks Mid Service Notification Data Example
  slug: management-webhooks-mid-service-notification-data-example
- key_count: 4
  name: Management Webhooks Payment Method Created Notification Request Example
  slug: management-webhooks-payment-method-created-notification-request-example
- key_count: 1
  name: Management Webhooks Payment Method Notification Response Example
  slug: management-webhooks-payment-method-notification-response-example
- key_count: 4
  name: Management Webhooks Payment Method Request Removed Notification Request Example
  slug: management-webhooks-payment-method-request-removed-notification-request-example
- key_count: 4
  name: Management Webhooks Payment Method Scheduled For Removal Notification Request Example
  slug: management-webhooks-payment-method-scheduled-for-removal-notification-request-example
- key_count: 2
  name: Management Webhooks Remediating Action Example
  slug: management-webhooks-remediating-action-example
- key_count: 5
  name: Management Webhooks Verification Error Example
  slug: management-webhooks-verification-error-example
- key_count: 4
  name: Management Webhooks Verification Error Recursive Example
  slug: management-webhooks-verification-error-recursive-example
- key_count: 2
  name: Management Wifi Profiles Example
  slug: management-wifi-profiles-example
- key_count: 1
  name: Notification Configurations Create Notification Configuration Request Example
  slug: notification-configurations-create-notification-configuration-request-example
- key_count: 1
  name: Notification Configurations Delete Notification Configuration Request Example
  slug: notification-configurations-delete-notification-configuration-request-example
- key_count: 0
  name: Notification Configurations Empty Request Example
  slug: notification-configurations-empty-request-example
- key_count: 3
  name: Notification Configurations Error Field Type Example
  slug: notification-configurations-error-field-type-example
- key_count: 2
  name: Notification Configurations Exchange Message Example
  slug: notification-configurations-exchange-message-example
- key_count: 3
  name: Notification Configurations Field Type Example
  slug: notification-configurations-field-type-example
- key_count: 3
  name: Notification Configurations Generic Response Example
  slug: notification-configurations-generic-response-example
- key_count: 4
  name: Notification Configurations Get Notification Configuration List Response Example
  slug: notification-configurations-get-notification-configuration-list-response-example
- key_count: 1
  name: Notification Configurations Get Notification Configuration Request Example
  slug: notification-configurations-get-notification-configuration-request-example
- key_count: 4
  name: Notification Configurations Get Notification Configuration Response Example
  slug: notification-configurations-get-notification-configuration-response-example
- key_count: 10
  name: Notification Configurations Notification Configuration Details Example
  slug: notification-configurations-notification-configuration-details-example
- key_count: 2
  name: Notification Configurations Notification Event Configuration Example
  slug: notification-configurations-notification-event-configuration-example
- key_count: 2
  name: Notification Configurations Test Notification Configuration Request Example
  slug: notification-configurations-test-notification-configuration-request-example
- key_count: 8
  name: Notification Configurations Test Notification Configuration Response Example
  slug: notification-configurations-test-notification-configuration-response-example
- key_count: 1
  name: Notification Configurations Update Notification Configuration Request Example
  slug: notification-configurations-update-notification-configuration-request-example
- key_count: 9
  name: Notification Webhooks Account Holder Capability Example
  slug: notification-webhooks-account-holder-capability-example
- key_count: 10
  name: Notification Webhooks Account Holder Example
  slug: notification-webhooks-account-holder-example
- key_count: 2
  name: Notification Webhooks Account Holder Notification Data Example
  slug: notification-webhooks-account-holder-notification-data-example
- key_count: 3
  name: Notification Webhooks Account Holder Notification Request Example
  slug: notification-webhooks-account-holder-notification-request-example
- key_count: 6
  name: Notification Webhooks Address Example
  slug: notification-webhooks-address-example
- key_count: 2
  name: Notification Webhooks Amount Example
  slug: notification-webhooks-amount-example
- key_count: 3
  name: Notification Webhooks Authentication Example
  slug: notification-webhooks-authentication-example
- key_count: 10
  name: Notification Webhooks Balance Account Example
  slug: notification-webhooks-balance-account-example
- key_count: 2
  name: Notification Webhooks Balance Account Notification Data Example
  slug: notification-webhooks-balance-account-notification-data-example
- key_count: 3
  name: Notification Webhooks Balance Account Notification Request Example
  slug: notification-webhooks-balance-account-notification-request-example
- key_count: 4
  name: Notification Webhooks Balance Example
  slug: notification-webhooks-balance-example
- key_count: 1
  name: Notification Webhooks Balance Platform Notification Response Example
  slug: notification-webhooks-balance-platform-notification-response-example
- key_count: 1
  name: Notification Webhooks Bank Account Example
  slug: notification-webhooks-bank-account-example
- key_count: 3
  name: Notification Webhooks Bank Account Info Example
  slug: notification-webhooks-bank-account-info-example
- key_count: 9
  name: Notification Webhooks Bulk Address Example
  slug: notification-webhooks-bulk-address-example
- key_count: 3
  name: Notification Webhooks Capability Problem Entity Example
  slug: notification-webhooks-capability-problem-entity-example
- key_count: 2
  name: Notification Webhooks Capability Problem Entity Recursive Example
  slug: notification-webhooks-capability-problem-entity-recursive-example
- key_count: 2
  name: Notification Webhooks Capability Problem Example
  slug: notification-webhooks-capability-problem-example
- key_count: 14
  name: Notification Webhooks Card Configuration Example
  slug: notification-webhooks-card-configuration-example
- key_count: 12
  name: Notification Webhooks Card Example
  slug: notification-webhooks-card-example
- key_count: 4
  name: Notification Webhooks Contact Details Example
  slug: notification-webhooks-contact-details-example
- key_count: 7
  name: Notification Webhooks Contact Example
  slug: notification-webhooks-contact-example
- key_count: 4
  name: Notification Webhooks Counterparty Example
  slug: notification-webhooks-counterparty-example
- key_count: 2
  name: Notification Webhooks Cron Sweep Schedule Example
  slug: notification-webhooks-cron-sweep-schedule-example
- key_count: 2
  name: Notification Webhooks Expiry Example
  slug: notification-webhooks-expiry-example
- key_count: 17
  name: Notification Webhooks Incoming Transfer Notification Data Example
  slug: notification-webhooks-incoming-transfer-notification-data-example
- key_count: 3
  name: Notification Webhooks Incoming Transfer Notification Request Example
  slug: notification-webhooks-incoming-transfer-notification-request-example
- key_count: 2
  name: Notification Webhooks Json Object Example
  slug: notification-webhooks-json-object-example
- key_count: 1
  name: Notification Webhooks Json Path Example
  slug: notification-webhooks-json-path-example
- key_count: 4
  name: Notification Webhooks Merchant Data Example
  slug: notification-webhooks-merchant-data-example
- key_count: 4
  name: Notification Webhooks Name 2 Example
  slug: notification-webhooks-name-2-example
- key_count: 2
  name: Notification Webhooks Name Example
  slug: notification-webhooks-name-example
- key_count: 6
  name: Notification Webhooks Name Location Example
  slug: notification-webhooks-name-location-example
- key_count: 2
  name: Notification Webhooks Notification Modification Data Example
  slug: notification-webhooks-notification-modification-data-example
- key_count: 22
  name: Notification Webhooks Outgoing Transfer Notification Data Example
  slug: notification-webhooks-outgoing-transfer-notification-data-example
- key_count: 3
  name: Notification Webhooks Outgoing Transfer Notification Request Example
  slug: notification-webhooks-outgoing-transfer-notification-request-example
- key_count: 10
  name: Notification Webhooks Payment Instrument Example
  slug: notification-webhooks-payment-instrument-example
- key_count: 2
  name: Notification Webhooks Payment Instrument Notification Data Example
  slug: notification-webhooks-payment-instrument-notification-data-example
- key_count: 1
  name: Notification Webhooks Payment Instrument Reference Example
  slug: notification-webhooks-payment-instrument-reference-example
- key_count: 20
  name: Notification Webhooks Payment Notification Data Example
  slug: notification-webhooks-payment-notification-data-example
- key_count: 3
  name: Notification Webhooks Payment Notification Request 2 Example
  slug: notification-webhooks-payment-notification-request-2-example
- key_count: 3
  name: Notification Webhooks Payment Notification Request Example
  slug: notification-webhooks-payment-notification-request-example
- key_count: 3
  name: Notification Webhooks Personal Data Example
  slug: notification-webhooks-personal-data-example
- key_count: 2
  name: Notification Webhooks Phone Example
  slug: notification-webhooks-phone-example
- key_count: 3
  name: Notification Webhooks Phone Number Example
  slug: notification-webhooks-phone-number-example
- key_count: 8
  name: Notification Webhooks Platform Payment Example
  slug: notification-webhooks-platform-payment-example
- key_count: 3
  name: Notification Webhooks Relayed Authorisation Data Example
  slug: notification-webhooks-relayed-authorisation-data-example
- key_count: 2
  name: Notification Webhooks Remediating Action Example
  slug: notification-webhooks-remediating-action-example
- key_count: 7
  name: Notification Webhooks Report Notification Data Example
  slug: notification-webhooks-report-notification-data-example
- key_count: 3
  name: Notification Webhooks Report Notification Request Example
  slug: notification-webhooks-report-notification-request-example
- key_count: 3
  name: Notification Webhooks Resource Example
  slug: notification-webhooks-resource-example
- key_count: 3
  name: Notification Webhooks Resource Reference Example
  slug: notification-webhooks-resource-reference-example
- key_count: 10
  name: Notification Webhooks Sweep Configuration Example
  slug: notification-webhooks-sweep-configuration-example
- key_count: 3
  name: Notification Webhooks Sweep Configuration Notification Data Example
  slug: notification-webhooks-sweep-configuration-notification-data-example
- key_count: 3
  name: Notification Webhooks Sweep Configuration Notification Request Example
  slug: notification-webhooks-sweep-configuration-notification-request-example
- key_count: 10
  name: Notification Webhooks Sweep Configuration V2 Example
  slug: notification-webhooks-sweep-configuration-v2-example
- key_count: 3
  name: Notification Webhooks Sweep Counterparty Example
  slug: notification-webhooks-sweep-counterparty-example
- key_count: 1
  name: Notification Webhooks Sweep Schedule Example
  slug: notification-webhooks-sweep-schedule-example
- key_count: 3
  name: Notification Webhooks Transaction Event Violation Example
  slug: notification-webhooks-transaction-event-violation-example
- key_count: 24
  name: Notification Webhooks Transaction Notification Data Example
  slug: notification-webhooks-transaction-notification-data-example
- key_count: 2
  name: Notification Webhooks Transaction Rule Source Example
  slug: notification-webhooks-transaction-rule-source-example
- key_count: 2
  name: Notification Webhooks Transaction Rules Result Example
  slug: notification-webhooks-transaction-rules-result-example
- key_count: 2
  name: Notification Webhooks Validation Result Example
  slug: notification-webhooks-validation-result-example
- key_count: 5
  name: Notification Webhooks Verification Error Example
  slug: notification-webhooks-verification-error-example
- key_count: 4
  name: Notification Webhooks Verification Error Recursive Example
  slug: notification-webhooks-verification-error-recursive-example
- key_count: 7
  name: Notifications Account Close Notification Example
  slug: notifications-account-close-notification-example
- key_count: 7
  name: Notifications Account Create Notification Example
  slug: notifications-account-create-notification-example
- key_count: 3
  name: Notifications Account Event Example
  slug: notifications-account-event-example
- key_count: 5
  name: Notifications Account Funds Below Threshold Notification Content Example
  slug: notifications-account-funds-below-threshold-notification-content-example
- key_count: 7
  name: Notifications Account Funds Below Threshold Notification Example
  slug: notifications-account-funds-below-threshold-notification-example
- key_count: 7
  name: Notifications Account Holder Create Notification Example
  slug: notifications-account-holder-create-notification-example
- key_count: 15
  name: Notifications Account Holder Details Example
  slug: notifications-account-holder-details-example
- key_count: 17
  name: Notifications Account Holder Payout Notification Content Example
  slug: notifications-account-holder-payout-notification-content-example
- key_count: 7
  name: Notifications Account Holder Payout Notification Example
  slug: notifications-account-holder-payout-notification-example
- key_count: 5
  name: Notifications Account Holder Status Change Notification Content Example
  slug: notifications-account-holder-status-change-notification-content-example
- key_count: 7
  name: Notifications Account Holder Status Change Notification Example
  slug: notifications-account-holder-status-change-notification-example
- key_count: 5
  name: Notifications Account Holder Status Example
  slug: notifications-account-holder-status-example
- key_count: 7
  name: Notifications Account Holder Store Status Change Notification Content Example
  slug: notifications-account-holder-store-status-change-notification-content-example
- key_count: 7
  name: Notifications Account Holder Store Status Change Notification Example
  slug: notifications-account-holder-store-status-change-notification-example
- key_count: 4
  name: Notifications Account Holder Upcoming Deadline Notification Content Example
  slug: notifications-account-holder-upcoming-deadline-notification-content-example
- key_count: 7
  name: Notifications Account Holder Upcoming Deadline Notification Example
  slug: notifications-account-holder-upcoming-deadline-notification-example
- key_count: 7
  name: Notifications Account Holder Update Notification Example
  slug: notifications-account-holder-update-notification-example
- key_count: 7
  name: Notifications Account Holder Verification Notification Content Example
  slug: notifications-account-holder-verification-notification-content-example
- key_count: 7
  name: Notifications Account Holder Verification Notification Example
  slug: notifications-account-holder-verification-notification-example
- key_count: 6
  name: Notifications Account Payout State Example
  slug: notifications-account-payout-state-example
- key_count: 5
  name: Notifications Account Processing State Example
  slug: notifications-account-processing-state-example
- key_count: 7
  name: Notifications Account Update Notification Example
  slug: notifications-account-update-notification-example
- key_count: 2
  name: Notifications Amount Example
  slug: notifications-amount-example
- key_count: 26
  name: Notifications Bank Account Detail Example
  slug: notifications-bank-account-detail-example
- key_count: 7
  name: Notifications Beneficiary Setup Notification Content Example
  slug: notifications-beneficiary-setup-notification-content-example
- key_count: 7
  name: Notifications Beneficiary Setup Notification Example
  slug: notifications-beneficiary-setup-notification-example
- key_count: 10
  name: Notifications Business Details Example
  slug: notifications-business-details-example
- key_count: 5
  name: Notifications Close Account Response Example
  slug: notifications-close-account-response-example
- key_count: 1
  name: Notifications Compensate Negative Balance Notification Content Example
  slug: notifications-compensate-negative-balance-notification-content-example
- key_count: 7
  name: Notifications Compensate Negative Balance Notification Example
  slug: notifications-compensate-negative-balance-notification-example
- key_count: 3
  name: Notifications Compensate Negative Balance Notification Record Example
  slug: notifications-compensate-negative-balance-notification-record-example
- key_count: 12
  name: Notifications Create Account Holder Response Example
  slug: notifications-create-account-holder-response-example
- key_count: 12
  name: Notifications Create Account Response Example
  slug: notifications-create-account-response-example
- key_count: 7
  name: Notifications Direct Debit Initiated Notification Content Example
  slug: notifications-direct-debit-initiated-notification-content-example
- key_count: 7
  name: Notifications Direct Debit Initiated Notification Example
  slug: notifications-direct-debit-initiated-notification-example
- key_count: 3
  name: Notifications Error Field Type Example
  slug: notifications-error-field-type-example
- key_count: 3
  name: Notifications Field Type Example
  slug: notifications-field-type-example
- key_count: 2
  name: Notifications Individual Details Example
  slug: notifications-individual-details-example
- key_count: 1
  name: Notifications Kyc Check Result Example
  slug: notifications-kyc-check-result-example
- key_count: 4
  name: Notifications Kyc Check Status Data Example
  slug: notifications-kyc-check-status-data-example
- key_count: 2
  name: Notifications Kyc Check Summary Example
  slug: notifications-kyc-check-summary-example
- key_count: 2
  name: Notifications Kyc Legal Arrangement Check Result Example
  slug: notifications-kyc-legal-arrangement-check-result-example
- key_count: 3
  name: Notifications Kyc Legal Arrangement Entity Check Result Example
  slug: notifications-kyc-legal-arrangement-entity-check-result-example
- key_count: 2
  name: Notifications Kyc Payout Method Check Result Example
  slug: notifications-kyc-payout-method-check-result-example
- key_count: 4
  name: Notifications Kyc Shareholder Check Result Example
  slug: notifications-kyc-shareholder-check-result-example
- key_count: 2
  name: Notifications Kyc Signatory Check Result Example
  slug: notifications-kyc-signatory-check-result-example
- key_count: 2
  name: Notifications Kyc Ultimate Parent Company Check Result Example
  slug: notifications-kyc-ultimate-parent-company-check-result-example
- key_count: 7
  name: Notifications Kyc Verification Result Example
  slug: notifications-kyc-verification-result-example
- key_count: 9
  name: Notifications Legal Arrangement Detail Example
  slug: notifications-legal-arrangement-detail-example
- key_count: 11
  name: Notifications Legal Arrangement Entity Detail Example
  slug: notifications-legal-arrangement-entity-detail-example
- key_count: 2
  name: Notifications Local Date Example
  slug: notifications-local-date-example
- key_count: 2
  name: Notifications Message Example
  slug: notifications-message-example
- key_count: 2
  name: Notifications Notification Error Container Example
  slug: notifications-notification-error-container-example
- key_count: 1
  name: Notifications Notification Response Example
  slug: notifications-notification-response-example
- key_count: 2
  name: Notifications Operation Status Example
  slug: notifications-operation-status-example
- key_count: 6
  name: Notifications Payment Failure Notification Content Example
  slug: notifications-payment-failure-notification-content-example
- key_count: 7
  name: Notifications Payment Failure Notification Example
  slug: notifications-payment-failure-notification-example
- key_count: 5
  name: Notifications Payout Method Example
  slug: notifications-payout-method-example
- key_count: 2
  name: Notifications Payout Schedule Response Example
  slug: notifications-payout-schedule-response-example
- key_count: 5
  name: Notifications Personal Document Data Example
  slug: notifications-personal-document-data-example
- key_count: 5
  name: Notifications Refund Funds Transfer Notification Content Example
  slug: notifications-refund-funds-transfer-notification-content-example
- key_count: 7
  name: Notifications Refund Funds Transfer Notification Example
  slug: notifications-refund-funds-transfer-notification-example
- key_count: 3
  name: Notifications Refund Result Example
  slug: notifications-refund-result-example
- key_count: 5
  name: Notifications Report Available Notification Content Example
  slug: notifications-report-available-notification-content-example
- key_count: 7
  name: Notifications Report Available Notification Example
  slug: notifications-report-available-notification-example
- key_count: 5
  name: Notifications Scheduled Refunds Notification Content Example
  slug: notifications-scheduled-refunds-notification-content-example
- key_count: 7
  name: Notifications Scheduled Refunds Notification Example
  slug: notifications-scheduled-refunds-notification-example
- key_count: 11
  name: Notifications Shareholder Contact Example
  slug: notifications-shareholder-contact-example
- key_count: 10
  name: Notifications Signatory Contact Example
  slug: notifications-signatory-contact-example
- key_count: 2
  name: Notifications Split Amount Example
  slug: notifications-split-amount-example
- key_count: 5
  name: Notifications Split Example
  slug: notifications-split-example
- key_count: 15
  name: Notifications Store Detail Example
  slug: notifications-store-detail-example
- key_count: 16
  name: Notifications Transaction Example
  slug: notifications-transaction-example
- key_count: 7
  name: Notifications Transfer Funds Notification Content Example
  slug: notifications-transfer-funds-notification-content-example
- key_count: 7
  name: Notifications Transfer Funds Notification Example
  slug: notifications-transfer-funds-notification-example
- key_count: 5
  name: Notifications Ultimate Parent Company Business Details Example
  slug: notifications-ultimate-parent-company-business-details-example
- key_count: 3
  name: Notifications Ultimate Parent Company Example
  slug: notifications-ultimate-parent-company-example
- key_count: 11
  name: Notifications Update Account Holder Response Example
  slug: notifications-update-account-holder-response-example
- key_count: 10
  name: Notifications Update Account Response Example
  slug: notifications-update-account-response-example
- key_count: 6
  name: Notifications Vias Address Example
  slug: notifications-vias-address-example
- key_count: 4
  name: Notifications Vias Name Example
  slug: notifications-vias-name-example
- key_count: 3
  name: Notifications Vias Personal Data Example
  slug: notifications-vias-personal-data-example
- key_count: 3
  name: Notifications Vias Phone Number Example
  slug: notifications-vias-phone-number-example
- key_count: 19
  name: Payments Account Info Example
  slug: payments-account-info-example
- key_count: 16
  name: Payments Acct Info Example
  slug: payments-acct-info-example
- key_count: 28
  name: Payments Additional Data Airline Example
  slug: payments-additional-data-airline-example
- key_count: 23
  name: Payments Additional Data Car Rental Example
  slug: payments-additional-data-car-rental-example
- key_count: 16
  name: Payments Additional Data Common Example
  slug: payments-additional-data-common-example
- key_count: 17
  name: Payments Additional Data Level23 Example
  slug: payments-additional-data-level23-example
- key_count: 16
  name: Payments Additional Data Lodging Example
  slug: payments-additional-data-lodging-example
- key_count: 1
  name: Payments Additional Data Modifications Example
  slug: payments-additional-data-modifications-example
- key_count: 18
  name: Payments Additional Data Open Invoice Example
  slug: payments-additional-data-open-invoice-example
- key_count: 1
  name: Payments Additional Data Opi Example
  slug: payments-additional-data-opi-example
- key_count: 8
  name: Payments Additional Data Ratepay Example
  slug: payments-additional-data-ratepay-example
- key_count: 3
  name: Payments Additional Data Retry Example
  slug: payments-additional-data-retry-example
- key_count: 21
  name: Payments Additional Data Risk Example
  slug: payments-additional-data-risk-example
- key_count: 15
  name: Payments Additional Data Risk Standalone Example
  slug: payments-additional-data-risk-standalone-example
- key_count: 10
  name: Payments Additional Data Sub Merchant Example
  slug: payments-additional-data-sub-merchant-example
- key_count: 9
  name: Payments Additional Data Temporary Services Example
  slug: payments-additional-data-temporary-services-example
- key_count: 6
  name: Payments Additional Data Wallets Example
  slug: payments-additional-data-wallets-example
- key_count: 6
  name: Payments Additional Data3 D Secure Example
  slug: payments-additional-data3-d-secure-example
- key_count: 6
  name: Payments Address Example
  slug: payments-address-example
- key_count: 11
  name: Payments Adjust Authorisation Request Example
  slug: payments-adjust-authorisation-request-example
- key_count: 2
  name: Payments Amount Example
  slug: payments-amount-example
- key_count: 6
  name: Payments Application Info Example
  slug: payments-application-info-example
- key_count: 2
  name: Payments Authentication Result Request Example
  slug: payments-authentication-result-request-example
- key_count: 2
  name: Payments Authentication Result Response Example
  slug: payments-authentication-result-response-example
- key_count: 9
  name: Payments Bank Account Example
  slug: payments-bank-account-example
- key_count: 9
  name: Payments Browser Info Example
  slug: payments-browser-info-example
- key_count: 9
  name: Payments Cancel Or Refund Request Example
  slug: payments-cancel-or-refund-request-example
- key_count: 10
  name: Payments Cancel Request Example
  slug: payments-cancel-request-example
- key_count: 11
  name: Payments Capture Request Example
  slug: payments-capture-request-example
- key_count: 8
  name: Payments Card Example
  slug: payments-card-example
- key_count: 2
  name: Payments Common Field Example
  slug: payments-common-field-example
- key_count: 2
  name: Payments Device Render Options Example
  slug: payments-device-render-options-example
- key_count: 6
  name: Payments Donation Request Example
  slug: payments-donation-request-example
- key_count: 3
  name: Payments External Platform Example
  slug: payments-external-platform-example
- key_count: 12
  name: Payments Forex Quote Example
  slug: payments-forex-quote-example
- key_count: 3
  name: Payments Fraud Check Result Example
  slug: payments-fraud-check-result-example
- key_count: 1
  name: Payments Fraud Check Result Wrapper Example
  slug: payments-fraud-check-result-wrapper-example
- key_count: 2
  name: Payments Fraud Result Example
  slug: payments-fraud-result-example
- key_count: 9
  name: Payments Fund Destination Example
  slug: payments-fund-destination-example
- key_count: 6
  name: Payments Fund Source Example
  slug: payments-fund-source-example
- key_count: 2
  name: Payments Installments Example
  slug: payments-installments-example
- key_count: 8
  name: Payments Mandate Example
  slug: payments-mandate-example
- key_count: 3
  name: Payments Merchant Device Example
  slug: payments-merchant-device-example
- key_count: 14
  name: Payments Merchant Risk Indicator Example
  slug: payments-merchant-risk-indicator-example
- key_count: 3
  name: Payments Modification Result Example
  slug: payments-modification-result-example
- key_count: 2
  name: Payments Name Example
  slug: payments-name-example
- key_count: 53
  name: Payments Payment Request Example
  slug: payments-payment-request-example
- key_count: 45
  name: Payments Payment Request3D Example
  slug: payments-payment-request3d-example
- key_count: 45
  name: Payments Payment Request3Ds2 Example
  slug: payments-payment-request3ds2-example
- key_count: 11
  name: Payments Payment Result Example
  slug: payments-payment-result-example
- key_count: 2
  name: Payments Phone Example
  slug: payments-phone-example
- key_count: 3
  name: Payments Platform Chargeback Logic Example
  slug: payments-platform-chargeback-logic-example
- key_count: 5
  name: Payments Recurring Example
  slug: payments-recurring-example
- key_count: 11
  name: Payments Refund Request Example
  slug: payments-refund-request-example
- key_count: 6
  name: Payments Response Additional Data Billing Address Example
  slug: payments-response-additional-data-billing-address-example
- key_count: 8
  name: Payments Response Additional Data Card Example
  slug: payments-response-additional-data-card-example
- key_count: 59
  name: Payments Response Additional Data Common Example
  slug: payments-response-additional-data-common-example
- key_count: 2
  name: Payments Response Additional Data Domestic Error Example
  slug: payments-response-additional-data-domestic-error-example
- key_count: 12
  name: Payments Response Additional Data Installments Example
  slug: payments-response-additional-data-installments-example
- key_count: 3
  name: Payments Response Additional Data Network Tokens Example
  slug: payments-response-additional-data-network-tokens-example
- key_count: 1
  name: Payments Response Additional Data Opi Example
  slug: payments-response-additional-data-opi-example
- key_count: 3
  name: Payments Response Additional Data Sepa Example
  slug: payments-response-additional-data-sepa-example
- key_count: 5
  name: Payments Response Additional Data3 D Secure Example
  slug: payments-response-additional-data3-d-secure-example
- key_count: 4
  name: Payments Sdk Ephem Pub Key Example
  slug: payments-sdk-ephem-pub-key-example
- key_count: 3
  name: Payments Shopper Interaction Device Example
  slug: payments-shopper-interaction-device-example
- key_count: 2
  name: Payments Split Amount Example
  slug: payments-split-amount-example
- key_count: 5
  name: Payments Split Example
  slug: payments-split-example
- key_count: 5
  name: Payments Sub Merchant Example
  slug: payments-sub-merchant-example
- key_count: 10
  name: Payments Technical Cancel Request Example
  slug: payments-technical-cancel-request-example
- key_count: 12
  name: Payments Three D Secure Data Example
  slug: payments-three-d-secure-data-example
- key_count: 3
  name: Payments Three Ds Requestor Authentication Info Example
  slug: payments-three-ds-requestor-authentication-info-example
- key_count: 4
  name: Payments Three Ds Requestor Prior Authentication Info Example
  slug: payments-three-ds-requestor-prior-authentication-info-example
- key_count: 6
  name: Payments Three Ds1 Result Example
  slug: payments-three-ds1-result-example
- key_count: 39
  name: Payments Three Ds2 Request Data Example
  slug: payments-three-ds2-request-data-example
- key_count: 14
  name: Payments Three Ds2 Result Example
  slug: payments-three-ds2-result-example
- key_count: 2
  name: Payments Three Ds2 Result Request Example
  slug: payments-three-ds2-result-request-example
- key_count: 1
  name: Payments Three Ds2 Result Response Example
  slug: payments-three-ds2-result-response-example
- key_count: 11
  name: Payments Void Pending Refund Request Example
  slug: payments-void-pending-refund-request-example
- key_count: 6
  name: Payouts Address Example
  slug: payouts-address-example
- key_count: 2
  name: Payouts Amount Example
  slug: payouts-amount-example
- key_count: 9
  name: Payouts Bank Account Example
  slug: payouts-bank-account-example
- key_count: 8
  name: Payouts Card Example
  slug: payouts-card-example
- key_count: 3
  name: Payouts Fraud Check Result Example
  slug: payouts-fraud-check-result-example
- key_count: 1
  name: Payouts Fraud Check Result Wrapper Example
  slug: payouts-fraud-check-result-wrapper-example
- key_count: 2
  name: Payouts Fraud Result Example
  slug: payouts-fraud-result-example
- key_count: 6
  name: Payouts Fund Source Example
  slug: payouts-fund-source-example
- key_count: 3
  name: Payouts Modify Request Example
  slug: payouts-modify-request-example
- key_count: 3
  name: Payouts Modify Response Example
  slug: payouts-modify-response-example
- key_count: 2
  name: Payouts Name Example
  slug: payouts-name-example
- key_count: 14
  name: Payouts Payout Request Example
  slug: payouts-payout-request-example
- key_count: 11
  name: Payouts Payout Response Example
  slug: payouts-payout-response-example
- key_count: 5
  name: Payouts Recurring Example
  slug: payouts-recurring-example
- key_count: 6
  name: Payouts Response Additional Data Billing Address Example
  slug: payouts-response-additional-data-billing-address-example
- key_count: 8
  name: Payouts Response Additional Data Card Example
  slug: payouts-response-additional-data-card-example
- key_count: 59
  name: Payouts Response Additional Data Common Example
  slug: payouts-response-additional-data-common-example
- key_count: 2
  name: Payouts Response Additional Data Domestic Error Example
  slug: payouts-response-additional-data-domestic-error-example
- key_count: 12
  name: Payouts Response Additional Data Installments Example
  slug: payouts-response-additional-data-installments-example
- key_count: 3
  name: Payouts Response Additional Data Network Tokens Example
  slug: payouts-response-additional-data-network-tokens-example
- key_count: 1
  name: Payouts Response Additional Data Opi Example
  slug: payouts-response-additional-data-opi-example
- key_count: 3
  name: Payouts Response Additional Data Sepa Example
  slug: payouts-response-additional-data-sepa-example
- key_count: 5
  name: Payouts Response Additional Data3 D Secure Example
  slug: payouts-response-additional-data3-d-secure-example
- key_count: 19
  name: Payouts Store Detail And Submit Request Example
  slug: payouts-store-detail-and-submit-request-example
- key_count: 4
  name: Payouts Store Detail And Submit Response Example
  slug: payouts-store-detail-and-submit-response-example
- key_count: 16
  name: Payouts Store Detail Request Example
  slug: payouts-store-detail-request-example
- key_count: 4
  name: Payouts Store Detail Response Example
  slug: payouts-store-detail-response-example
- key_count: 15
  name: Payouts Submit Request Example
  slug: payouts-submit-request-example
- key_count: 4
  name: Payouts Submit Response Example
  slug: payouts-submit-response-example
- key_count: 6
  name: Pos Terminal Address Example
  slug: pos-terminal-address-example
- key_count: 5
  name: Pos Terminal Assign Terminals Request Example
  slug: pos-terminal-assign-terminals-request-example
- key_count: 1
  name: Pos Terminal Assign Terminals Response Example
  slug: pos-terminal-assign-terminals-response-example
- key_count: 1
  name: Pos Terminal Find Terminal Request Example
  slug: pos-terminal-find-terminal-request-example
- key_count: 5
  name: Pos Terminal Find Terminal Response Example
  slug: pos-terminal-find-terminal-response-example
- key_count: 2
  name: Pos Terminal Get Stores Under Account Request Example
  slug: pos-terminal-get-stores-under-account-request-example
- key_count: 1
  name: Pos Terminal Get Stores Under Account Response Example
  slug: pos-terminal-get-stores-under-account-response-example
- key_count: 1
  name: Pos Terminal Get Terminal Details Request Example
  slug: pos-terminal-get-terminal-details-request-example
- key_count: 25
  name: Pos Terminal Get Terminal Details Response Example
  slug: pos-terminal-get-terminal-details-response-example
- key_count: 3
  name: Pos Terminal Get Terminals Under Account Request Example
  slug: pos-terminal-get-terminals-under-account-request-example
- key_count: 3
  name: Pos Terminal Get Terminals Under Account Response Example
  slug: pos-terminal-get-terminals-under-account-response-example
- key_count: 4
  name: Pos Terminal Merchant Account Example
  slug: pos-terminal-merchant-account-example
- key_count: 6
  name: Pos Terminal Store Example
  slug: pos-terminal-store-example
- key_count: 6
  name: Recurring Address Example
  slug: recurring-address-example
- key_count: 2
  name: Recurring Amount Example
  slug: recurring-amount-example
- key_count: 9
  name: Recurring Bank Account Example
  slug: recurring-bank-account-example
- key_count: 8
  name: Recurring Card Example
  slug: recurring-card-example
- key_count: 4
  name: Recurring Create Permit Request Example
  slug: recurring-create-permit-request-example
- key_count: 2
  name: Recurring Create Permit Result Example
  slug: recurring-create-permit-result-example
- key_count: 2
  name: Recurring Disable Permit Request Example
  slug: recurring-disable-permit-request-example
- key_count: 2
  name: Recurring Disable Permit Result Example
  slug: recurring-disable-permit-result-example
- key_count: 4
  name: Recurring Disable Request Example
  slug: recurring-disable-request-example
- key_count: 1
  name: Recurring Disable Result Example
  slug: recurring-disable-result-example
- key_count: 2
  name: Recurring Name Example
  slug: recurring-name-example
- key_count: 9
  name: Recurring Notify Shopper Request Example
  slug: recurring-notify-shopper-request-example
- key_count: 7
  name: Recurring Notify Shopper Result Example
  slug: recurring-notify-shopper-result-example
- key_count: 5
  name: Recurring Permit Example
  slug: recurring-permit-example
- key_count: 3
  name: Recurring Permit Restriction Example
  slug: recurring-permit-restriction-example
- key_count: 2
  name: Recurring Permit Result Example
  slug: recurring-permit-result-example
- key_count: 17
  name: Recurring Recurring Detail Example
  slug: recurring-recurring-detail-example
- key_count: 1
  name: Recurring Recurring Detail Wrapper Example
  slug: recurring-recurring-detail-wrapper-example
- key_count: 3
  name: Recurring Recurring Details Request Example
  slug: recurring-recurring-details-request-example
- key_count: 4
  name: Recurring Recurring Details Result Example
  slug: recurring-recurring-details-result-example
- key_count: 5
  name: Recurring Recurring Example
  slug: recurring-recurring-example
- key_count: 6
  name: Recurring Schedule Account Updater Request Example
  slug: recurring-schedule-account-updater-request-example
- key_count: 2
  name: Recurring Schedule Account Updater Result Example
  slug: recurring-schedule-account-updater-result-example
- key_count: 2
  name: Recurring Token Details Example
  slug: recurring-token-details-example
- key_count: 1
  name: Report Webhooks Balance Platform Notification Response Example
  slug: report-webhooks-balance-platform-notification-response-example
- key_count: 7
  name: Report Webhooks Report Notification Data Example
  slug: report-webhooks-report-notification-data-example
- key_count: 3
  name: Report Webhooks Report Notification Request Example
  slug: report-webhooks-report-notification-request-example
- key_count: 3
  name: Report Webhooks Resource Example
  slug: report-webhooks-resource-example
- key_count: 3
  name: Report Webhooks Resource Reference Example
  slug: report-webhooks-resource-reference-example
- key_count: 2
  name: Stored Value Amount Example
  slug: stored-value-amount-example
- key_count: 8
  name: Stored Value Stored Value Balance Check Request Example
  slug: stored-value-stored-value-balance-check-request-example
- key_count: 5
  name: Stored Value Stored Value Balance Check Response Example
  slug: stored-value-stored-value-balance-check-response-example
- key_count: 9
  name: Stored Value Stored Value Balance Merge Request Example
  slug: stored-value-stored-value-balance-merge-request-example
- key_count: 6
  name: Stored Value Stored Value Balance Merge Response Example
  slug: stored-value-stored-value-balance-merge-response-example
- key_count: 8
  name: Stored Value Stored Value Issue Request Example
  slug: stored-value-stored-value-issue-request-example
- key_count: 7
  name: Stored Value Stored Value Issue Response Example
  slug: stored-value-stored-value-issue-response-example
- key_count: 9
  name: Stored Value Stored Value Load Request Example
  slug: stored-value-stored-value-load-request-example
- key_count: 6
  name: Stored Value Stored Value Load Response Example
  slug: stored-value-stored-value-load-response-example
- key_count: 9
  name: Stored Value Stored Value Status Change Request Example
  slug: stored-value-stored-value-status-change-request-example
- key_count: 6
  name: Stored Value Stored Value Status Change Response Example
  slug: stored-value-stored-value-status-change-response-example
- key_count: 6
  name: Stored Value Stored Value Void Request Example
  slug: stored-value-stored-value-void-request-example
- key_count: 5
  name: Stored Value Stored Value Void Response Example
  slug: stored-value-stored-value-void-response-example
- key_count: 3
  name: Terminal Abort Request Example
  slug: terminal-abort-request-example
- key_count: 1
  name: Terminal Admin Request Example
  slug: terminal-admin-request-example
- key_count: 1
  name: Terminal Admin Response Example
  slug: terminal-admin-response-example
- key_count: 4
  name: Terminal Allowed Product Example
  slug: terminal-allowed-product-example
- key_count: 8
  name: Terminal Amounts Req Example
  slug: terminal-amounts-req-example
- key_count: 6
  name: Terminal Amounts Resp Example
  slug: terminal-amounts-resp-example
- key_count: 2
  name: Terminal Area Size Example
  slug: terminal-area-size-example
- key_count: 2
  name: Terminal Balance Inquiry Request Example
  slug: terminal-balance-inquiry-request-example
- key_count: 4
  name: Terminal Balance Inquiry Response Example
  slug: terminal-balance-inquiry-response-example
- key_count: 2
  name: Terminal Captured Signature Example
  slug: terminal-captured-signature-example
- key_count: 2
  name: Terminal Card Acquisition Request Example
  slug: terminal-card-acquisition-request-example
- key_count: 7
  name: Terminal Card Acquisition Response Example
  slug: terminal-card-acquisition-response-example
- key_count: 9
  name: Terminal Card Acquisition Transaction Example
  slug: terminal-card-acquisition-transaction-example
- key_count: 11
  name: Terminal Card Data Example
  slug: terminal-card-data-example
- key_count: 3
  name: Terminal Card Holder Pin Example
  slug: terminal-card-holder-pin-example
- key_count: 6
  name: Terminal Card Reader Apdu Request Example
  slug: terminal-card-reader-apdu-request-example
- key_count: 3
  name: Terminal Card Reader Apdu Response Example
  slug: terminal-card-reader-apdu-response-example
- key_count: 3
  name: Terminal Cash Handling Device Example
  slug: terminal-cash-handling-device-example
- key_count: 7
  name: Terminal Check Data Example
  slug: terminal-check-data-example
- key_count: 2
  name: Terminal Coins Or Bills Example
  slug: terminal-coins-or-bills-example
- key_count: 2
  name: Terminal Converted Amount Example
  slug: terminal-converted-amount-example
- key_count: 6
  name: Terminal Currency Conversion Example
  slug: terminal-currency-conversion-example
- key_count: 10
  name: Terminal Customer Order Example
  slug: terminal-customer-order-example
- key_count: 3
  name: Terminal Diagnosis Request Example
  slug: terminal-diagnosis-request-example
- key_count: 4
  name: Terminal Diagnosis Response Example
  slug: terminal-diagnosis-response-example
- key_count: 7
  name: Terminal Display Output Example
  slug: terminal-display-output-example
- key_count: 1
  name: Terminal Display Request Example
  slug: terminal-display-request-example
- key_count: 1
  name: Terminal Display Response Example
  slug: terminal-display-response-example
- key_count: 3
  name: Terminal Enable Service Request Example
  slug: terminal-enable-service-request-example
- key_count: 1
  name: Terminal Enable Service Response Example
  slug: terminal-enable-service-response-example
- key_count: 7
  name: Terminal Event Notification Example
  slug: terminal-event-notification-example
- key_count: 2
  name: Terminal Geographic Coordinates Example
  slug: terminal-geographic-coordinates-example
- key_count: 2
  name: Terminal Geolocation Example
  slug: terminal-geolocation-example
- key_count: 2
  name: Terminal Get Totals Request Example
  slug: terminal-get-totals-request-example
- key_count: 3
  name: Terminal Get Totals Response Example
  slug: terminal-get-totals-response-example
- key_count: 2
  name: Terminal Host Status Example
  slug: terminal-host-status-example
- key_count: 2
  name: Terminal Icc Reset Data Example
  slug: terminal-icc-reset-data-example
- key_count: 21
  name: Terminal Input Data Example
  slug: terminal-input-data-example
- key_count: 7
  name: Terminal Input Example
  slug: terminal-input-example
- key_count: 2
  name: Terminal Input Request Example
  slug: terminal-input-request-example
- key_count: 2
  name: Terminal Input Response Example
  slug: terminal-input-response-example
- key_count: 4
  name: Terminal Input Result Example
  slug: terminal-input-result-example
- key_count: 7
  name: Terminal Input Update Example
  slug: terminal-input-update-example
- key_count: 10
  name: Terminal Instalment Example
  slug: terminal-instalment-example
- key_count: 10
  name: Terminal Login Request Example
  slug: terminal-login-request-example
- key_count: 4
  name: Terminal Login Response Example
  slug: terminal-login-response-example
- key_count: 1
  name: Terminal Logout Request Example
  slug: terminal-logout-request-example
- key_count: 1
  name: Terminal Logout Response Example
  slug: terminal-logout-response-example
- key_count: 2
  name: Terminal Loyalty Account Example
  slug: terminal-loyalty-account-example
- key_count: 4
  name: Terminal Loyalty Account Id Example
  slug: terminal-loyalty-account-id-example
- key_count: 2
  name: Terminal Loyalty Account Req Example
  slug: terminal-loyalty-account-req-example
- key_count: 4
  name: Terminal Loyalty Account Status Example
  slug: terminal-loyalty-account-status-example
- key_count: 4
  name: Terminal Loyalty Acquirer Data Example
  slug: terminal-loyalty-acquirer-data-example
- key_count: 3
  name: Terminal Loyalty Amount Example
  slug: terminal-loyalty-amount-example
- key_count: 3
  name: Terminal Loyalty Data Example
  slug: terminal-loyalty-data-example
- key_count: 3
  name: Terminal Loyalty Request Example
  slug: terminal-loyalty-request-example
- key_count: 5
  name: Terminal Loyalty Response Example
  slug: terminal-loyalty-response-example
- key_count: 5
  name: Terminal Loyalty Result Example
  slug: terminal-loyalty-result-example
- key_count: 3
  name: Terminal Loyalty Totals Example
  slug: terminal-loyalty-totals-example
- key_count: 6
  name: Terminal Loyalty Transaction Example
  slug: terminal-loyalty-transaction-example
- key_count: 6
  name: Terminal Menu Entry Example
  slug: terminal-menu-entry-example
- key_count: 8
  name: Terminal Message Header Example
  slug: terminal-message-header-example
- key_count: 5
  name: Terminal Message Reference Example
  slug: terminal-message-reference-example
- key_count: 6
  name: Terminal Mobile Data Example
  slug: terminal-mobile-data-example
- key_count: 9
  name: Terminal Original Poi Transaction Example
  slug: terminal-original-poi-transaction-example
- key_count: 2
  name: Terminal Output Barcode Example
  slug: terminal-output-barcode-example
- key_count: 5
  name: Terminal Output Content Example
  slug: terminal-output-content-example
- key_count: 3
  name: Terminal Output Result Example
  slug: terminal-output-result-example
- key_count: 11
  name: Terminal Output Text Example
  slug: terminal-output-text-example
- key_count: 3
  name: Terminal Payment Account Req Example
  slug: terminal-payment-account-req-example
- key_count: 4
  name: Terminal Payment Account Status Example
  slug: terminal-payment-account-status-example
- key_count: 6
  name: Terminal Payment Acquirer Data Example
  slug: terminal-payment-acquirer-data-example
- key_count: 7
  name: Terminal Payment Data Example
  slug: terminal-payment-data-example
- key_count: 6
  name: Terminal Payment Instrument Data Example
  slug: terminal-payment-instrument-data-example
- key_count: 4
  name: Terminal Payment Receipt Example
  slug: terminal-payment-receipt-example
- key_count: 4
  name: Terminal Payment Request Example
  slug: terminal-payment-request-example
- key_count: 7
  name: Terminal Payment Response Example
  slug: terminal-payment-response-example
- key_count: 13
  name: Terminal Payment Result Example
  slug: terminal-payment-result-example
- key_count: 3
  name: Terminal Payment Token Example
  slug: terminal-payment-token-example
- key_count: 3
  name: Terminal Payment Totals Example
  slug: terminal-payment-totals-example
- key_count: 4
  name: Terminal Payment Transaction Example
  slug: terminal-payment-transaction-example
- key_count: 6
  name: Terminal Performed Transaction Example
  slug: terminal-performed-transaction-example
- key_count: 2
  name: Terminal Poi Data Example
  slug: terminal-poi-data-example
- key_count: 2
  name: Terminal Poi Profile Example
  slug: terminal-poi-profile-example
- key_count: 4
  name: Terminal Poi Software Example
  slug: terminal-poi-software-example
- key_count: 8
  name: Terminal Poi Status Example
  slug: terminal-poi-status-example
- key_count: 4
  name: Terminal Poi System Data Example
  slug: terminal-poi-system-data-example
- key_count: 4
  name: Terminal Poi Terminal Data Example
  slug: terminal-poi-terminal-data-example
- key_count: 2
  name: Terminal Point Example
  slug: terminal-point-example
- key_count: 2
  name: Terminal Predefined Content Example
  slug: terminal-predefined-content-example
- key_count: 5
  name: Terminal Print Output Example
  slug: terminal-print-output-example
- key_count: 1
  name: Terminal Print Request Example
  slug: terminal-print-request-example
- key_count: 2
  name: Terminal Print Response Example
  slug: terminal-print-response-example
- key_count: 3
  name: Terminal Rebates Example
  slug: terminal-rebates-example
- key_count: 3
  name: Terminal Reconciliation Request Example
  slug: terminal-reconciliation-request-example
- key_count: 4
  name: Terminal Reconciliation Response Example
  slug: terminal-reconciliation-response-example
- key_count: 2
  name: Terminal Repeated Message Response Example
  slug: terminal-repeated-message-response-example
- key_count: 6
  name: Terminal Repeated Response Message Body Example
  slug: terminal-repeated-response-message-body-example
- key_count: 3
  name: Terminal Response Example
  slug: terminal-response-example
- key_count: 5
  name: Terminal Reversal Request Example
  slug: terminal-reversal-request-example
- key_count: 6
  name: Terminal Reversal Response Example
  slug: terminal-reversal-response-example
- key_count: 12
  name: Terminal Sale Data Example
  slug: terminal-sale-data-example
- key_count: 11
  name: Terminal Sale Item Example
  slug: terminal-sale-item-example
- key_count: 7
  name: Terminal Sale Item Rebate Example
  slug: terminal-sale-item-rebate-example
- key_count: 4
  name: Terminal Sale Software Example
  slug: terminal-sale-software-example
- key_count: 1
  name: Terminal Sale Terminal Data Example
  slug: terminal-sale-terminal-data-example
- key_count: 1
  name: Terminal Sale To Issuer Data Example
  slug: terminal-sale-to-issuer-data-example
- key_count: 5
  name: Terminal Security Trailer Example
  slug: terminal-security-trailer-example
- key_count: 4
  name: Terminal Sensitive Card Data Example
  slug: terminal-sensitive-card-data-example
- key_count: 3
  name: Terminal Sensitive Mobile Data Example
  slug: terminal-sensitive-mobile-data-example
- key_count: 4
  name: Terminal Sound Content Example
  slug: terminal-sound-content-example
- key_count: 7
  name: Terminal Stored Value Account Id Example
  slug: terminal-stored-value-account-id-example
- key_count: 2
  name: Terminal Stored Value Account Status Example
  slug: terminal-stored-value-account-status-example
- key_count: 8
  name: Terminal Stored Value Data Example
  slug: terminal-stored-value-data-example
- key_count: 3
  name: Terminal Stored Value Request Example
  slug: terminal-stored-value-request-example
- key_count: 5
  name: Terminal Stored Value Response Example
  slug: terminal-stored-value-response-example
- key_count: 7
  name: Terminal Stored Value Result Example
  slug: terminal-stored-value-result-example
- key_count: 5
  name: Terminal Total Filter Example
  slug: terminal-total-filter-example
- key_count: 3
  name: Terminal Track Data Example
  slug: terminal-track-data-example
- key_count: 9
  name: Terminal Transaction Conditions Example
  slug: terminal-transaction-conditions-example
- key_count: 2
  name: Terminal Transaction Id Type Example
  slug: terminal-transaction-id-type-example
- key_count: 3
  name: Terminal Transaction Status Request Example
  slug: terminal-transaction-status-request-example
- key_count: 3
  name: Terminal Transaction Status Response Example
  slug: terminal-transaction-status-response-example
- key_count: 14
  name: Terminal Transaction Totals Example
  slug: terminal-transaction-totals-example
- key_count: 3
  name: Terminal Utm Coordinates Example
  slug: terminal-utm-coordinates-example
- key_count: 2
  name: Test Cards Avs Address Example
  slug: test-cards-avs-address-example
- key_count: 3
  name: Test Cards Create Test Card Ranges Request Example
  slug: test-cards-create-test-card-ranges-request-example
- key_count: 1
  name: Test Cards Create Test Card Ranges Result Example
  slug: test-cards-create-test-card-ranges-result-example
- key_count: 4
  name: Test Cards Test Card Range Creation Result Example
  slug: test-cards-test-card-range-creation-result-example
- key_count: 10
  name: Test Cards Test Card Range Example
  slug: test-cards-test-card-range-example
- key_count: 2
  name: Transaction Webhooks Amount Example
  slug: transaction-webhooks-amount-example
- key_count: 1
  name: Transaction Webhooks Balance Platform Notification Response Example
  slug: transaction-webhooks-balance-platform-notification-response-example
- key_count: 3
  name: Transaction Webhooks Resource Example
  slug: transaction-webhooks-resource-example
- key_count: 3
  name: Transaction Webhooks Resource Reference Example
  slug: transaction-webhooks-resource-reference-example
- key_count: 10
  name: Transaction Webhooks Transaction Example
  slug: transaction-webhooks-transaction-example
- key_count: 3
  name: Transaction Webhooks Transaction Notification Request V4 Example
  slug: transaction-webhooks-transaction-notification-request-v4-example
- key_count: 2
  name: Transaction Webhooks Transfer Data Example
  slug: transaction-webhooks-transfer-data-example
- key_count: 2
  name: Transfer Webhooks Additional Bank Identification Example
  slug: transfer-webhooks-additional-bank-identification-example
- key_count: 6
  name: Transfer Webhooks Address Example
  slug: transfer-webhooks-address-example
- key_count: 3
  name: Transfer Webhooks Amount Adjustment Example
  slug: transfer-webhooks-amount-adjustment-example
- key_count: 2
  name: Transfer Webhooks Amount Example
  slug: transfer-webhooks-amount-example
- key_count: 3
  name: Transfer Webhooks Au Local Account Identification Example
  slug: transfer-webhooks-au-local-account-identification-example
- key_count: 4
  name: Transfer Webhooks Balance Mutation Example
  slug: transfer-webhooks-balance-mutation-example
- key_count: 1
  name: Transfer Webhooks Balance Platform Notification Response Example
  slug: transfer-webhooks-balance-platform-notification-response-example
- key_count: 2
  name: Transfer Webhooks Bank Account V3 Example
  slug: transfer-webhooks-bank-account-v3-example
- key_count: 2
  name: Transfer Webhooks Bank Category Data Example
  slug: transfer-webhooks-bank-category-data-example
- key_count: 4
  name: Transfer Webhooks Br Local Account Identification Example
  slug: transfer-webhooks-br-local-account-identification-example
- key_count: 5
  name: Transfer Webhooks Ca Local Account Identification Example
  slug: transfer-webhooks-ca-local-account-identification-example
- key_count: 4
  name: Transfer Webhooks Counterparty V3 Example
  slug: transfer-webhooks-counterparty-v3-example
- key_count: 3
  name: Transfer Webhooks Cz Local Account Identification Example
  slug: transfer-webhooks-cz-local-account-identification-example
- key_count: 3
  name: Transfer Webhooks Dk Local Account Identification Example
  slug: transfer-webhooks-dk-local-account-identification-example
- key_count: 3
  name: Transfer Webhooks Hk Local Account Identification Example
  slug: transfer-webhooks-hk-local-account-identification-example
- key_count: 2
  name: Transfer Webhooks Hu Local Account Identification Example
  slug: transfer-webhooks-hu-local-account-identification-example
- key_count: 2
  name: Transfer Webhooks Iban Account Identification Example
  slug: transfer-webhooks-iban-account-identification-example
- key_count: 3
  name: Transfer Webhooks Internal Category Data Example
  slug: transfer-webhooks-internal-category-data-example
- key_count: 8
  name: Transfer Webhooks Issued Card Example
  slug: transfer-webhooks-issued-card-example
- key_count: 5
  name: Transfer Webhooks Merchant Data Example
  slug: transfer-webhooks-merchant-data-example
- key_count: 5
  name: Transfer Webhooks Modification Example
  slug: transfer-webhooks-modification-example
- key_count: 6
  name: Transfer Webhooks Name Location Example
  slug: transfer-webhooks-name-location-example
- key_count: 2
  name: Transfer Webhooks No Local Account Identification Example
  slug: transfer-webhooks-no-local-account-identification-example
- key_count: 4
  name: Transfer Webhooks Number And Bic Account Identification Example
  slug: transfer-webhooks-number-and-bic-account-identification-example
- key_count: 2
  name: Transfer Webhooks Nz Local Account Identification Example
  slug: transfer-webhooks-nz-local-account-identification-example
- key_count: 7
  name: Transfer Webhooks Party Identification Example
  slug: transfer-webhooks-party-identification-example
- key_count: 4
  name: Transfer Webhooks Payment Instrument Example
  slug: transfer-webhooks-payment-instrument-example
- key_count: 2
  name: Transfer Webhooks Pl Local Account Identification Example
  slug: transfer-webhooks-pl-local-account-identification-example
- key_count: 6
  name: Transfer Webhooks Platform Payment Example
  slug: transfer-webhooks-platform-payment-example
- key_count: 2
  name: Transfer Webhooks Relayed Authorisation Data Example
  slug: transfer-webhooks-relayed-authorisation-data-example
- key_count: 3
  name: Transfer Webhooks Resource Example
  slug: transfer-webhooks-resource-example
- key_count: 3
  name: Transfer Webhooks Resource Reference Example
  slug: transfer-webhooks-resource-reference-example
- key_count: 3
  name: Transfer Webhooks Se Local Account Identification Example
  slug: transfer-webhooks-se-local-account-identification-example
- key_count: 3
  name: Transfer Webhooks Sg Local Account Identification Example
  slug: transfer-webhooks-sg-local-account-identification-example
- key_count: 3
  name: Transfer Webhooks Transaction Event Violation Example
  slug: transfer-webhooks-transaction-event-violation-example
- key_count: 5
  name: Transfer Webhooks Transaction Rule Reference Example
  slug: transfer-webhooks-transaction-rule-reference-example
- key_count: 2
  name: Transfer Webhooks Transaction Rule Source Example
  slug: transfer-webhooks-transaction-rule-source-example
- key_count: 4
  name: Transfer Webhooks Transaction Rules Result Example
  slug: transfer-webhooks-transaction-rules-result-example
- key_count: 22
  name: Transfer Webhooks Transfer Data Example
  slug: transfer-webhooks-transfer-data-example
- key_count: 14
  name: Transfer Webhooks Transfer Event Example
  slug: transfer-webhooks-transfer-event-example
- key_count: 4
  name: Transfer Webhooks Transfer Notification Counter Party Example
  slug: transfer-webhooks-transfer-notification-counter-party-example
- key_count: 7
  name: Transfer Webhooks Transfer Notification Merchant Data Example
  slug: transfer-webhooks-transfer-notification-merchant-data-example
- key_count: 3
  name: Transfer Webhooks Transfer Notification Request Example
  slug: transfer-webhooks-transfer-notification-request-example
- key_count: 2
  name: Transfer Webhooks Transfer Notification Transfer Tracking Example
  slug: transfer-webhooks-transfer-notification-transfer-tracking-example
- key_count: 2
  name: Transfer Webhooks Transfer Notification Validation Fact Example
  slug: transfer-webhooks-transfer-notification-validation-fact-example
- key_count: 3
  name: Transfer Webhooks Uk Local Account Identification Example
  slug: transfer-webhooks-uk-local-account-identification-example
- key_count: 4
  name: Transfer Webhooks Us Local Account Identification Example
  slug: transfer-webhooks-us-local-account-identification-example
- key_count: 2
  name: Transfers Additional Bank Identification Example
  slug: transfers-additional-bank-identification-example
- key_count: 6
  name: Transfers Address Example
  slug: transfers-address-example
- key_count: 2
  name: Transfers Amount Example
  slug: transfers-amount-example
- key_count: 3
  name: Transfers Au Local Account Identification Example
  slug: transfers-au-local-account-identification-example
- key_count: 2
  name: Transfers Bank Account V3 Example
  slug: transfers-bank-account-v3-example
- key_count: 2
  name: Transfers Bank Category Data Example
  slug: transfers-bank-category-data-example
- key_count: 4
  name: Transfers Br Local Account Identification Example
  slug: transfers-br-local-account-identification-example
- key_count: 5
  name: Transfers Ca Local Account Identification Example
  slug: transfers-ca-local-account-identification-example
- key_count: 4
  name: Transfers Capital Balance Example
  slug: transfers-capital-balance-example
- key_count: 9
  name: Transfers Capital Grant Example
  slug: transfers-capital-grant-example
- key_count: 3
  name: Transfers Capital Grant Info Example
  slug: transfers-capital-grant-info-example
- key_count: 1
  name: Transfers Capital Grants Example
  slug: transfers-capital-grants-example
- key_count: 3
  name: Transfers Counterparty Example
  slug: transfers-counterparty-example
- key_count: 3
  name: Transfers Counterparty Info V3 Example
  slug: transfers-counterparty-info-v3-example
- key_count: 4
  name: Transfers Counterparty V3 Example
  slug: transfers-counterparty-v3-example
- key_count: 3
  name: Transfers Cz Local Account Identification Example
  slug: transfers-cz-local-account-identification-example
- key_count: 3
  name: Transfers Dk Local Account Identification Example
  slug: transfers-dk-local-account-identification-example
- key_count: 1
  name: Transfers Fee Example
  slug: transfers-fee-example
- key_count: 3
  name: Transfers Hk Local Account Identification Example
  slug: transfers-hk-local-account-identification-example
- key_count: 2
  name: Transfers Hu Local Account Identification Example
  slug: transfers-hu-local-account-identification-example
- key_count: 2
  name: Transfers Iban Account Identification Example
  slug: transfers-iban-account-identification-example
- key_count: 3
  name: Transfers Internal Category Data Example
  slug: transfers-internal-category-data-example
- key_count: 3
  name: Transfers Invalid Field Example
  slug: transfers-invalid-field-example
- key_count: 8
  name: Transfers Issued Card Example
  slug: transfers-issued-card-example
- key_count: 0
  name: Transfers Json Object Example
  slug: transfers-json-object-example
- key_count: 1
  name: Transfers Link Example
  slug: transfers-link-example
- key_count: 2
  name: Transfers Links Example
  slug: transfers-links-example
- key_count: 5
  name: Transfers Merchant Data Example
  slug: transfers-merchant-data-example
- key_count: 6
  name: Transfers Name Location Example
  slug: transfers-name-location-example
- key_count: 2
  name: Transfers No Local Account Identification Example
  slug: transfers-no-local-account-identification-example
- key_count: 4
  name: Transfers Number And Bic Account Identification Example
  slug: transfers-number-and-bic-account-identification-example
- key_count: 2
  name: Transfers Nz Local Account Identification Example
  slug: transfers-nz-local-account-identification-example
- key_count: 7
  name: Transfers Party Identification Example
  slug: transfers-party-identification-example
- key_count: 4
  name: Transfers Payment Instrument Example
  slug: transfers-payment-instrument-example
- key_count: 2
  name: Transfers Pl Local Account Identification Example
  slug: transfers-pl-local-account-identification-example
- key_count: 6
  name: Transfers Platform Payment Example
  slug: transfers-platform-payment-example
- key_count: 2
  name: Transfers Relayed Authorisation Data Example
  slug: transfers-relayed-authorisation-data-example
- key_count: 3
  name: Transfers Repayment Example
  slug: transfers-repayment-example
- key_count: 2
  name: Transfers Repayment Term Example
  slug: transfers-repayment-term-example
- key_count: 3
  name: Transfers Resource Reference Example
  slug: transfers-resource-reference-example
- key_count: 9
  name: Transfers Rest Service Error Example
  slug: transfers-rest-service-error-example
- key_count: 2
  name: Transfers Return Transfer Request Example
  slug: transfers-return-transfer-request-example
- key_count: 4
  name: Transfers Return Transfer Response Example
  slug: transfers-return-transfer-response-example
- key_count: 3
  name: Transfers Se Local Account Identification Example
  slug: transfers-se-local-account-identification-example
- key_count: 3
  name: Transfers Sg Local Account Identification Example
  slug: transfers-sg-local-account-identification-example
- key_count: 1
  name: Transfers Threshold Repayment Example
  slug: transfers-threshold-repayment-example
- key_count: 10
  name: Transfers Transaction Example
  slug: transfers-transaction-example
- key_count: 2
  name: Transfers Transaction Search Response Example
  slug: transfers-transaction-search-response-example
- key_count: 2
  name: Transfers Transfer Data Example
  slug: transfers-transfer-data-example
- key_count: 15
  name: Transfers Transfer Example
  slug: transfers-transfer-example
- key_count: 10
  name: Transfers Transfer Info Example
  slug: transfers-transfer-info-example
- key_count: 2
  name: Transfers Transfer Notification Validation Fact Example
  slug: transfers-transfer-notification-validation-fact-example
- key_count: 3
  name: Transfers Uk Local Account Identification Example
  slug: transfers-uk-local-account-identification-example
- key_count: 7
  name: Transfers Ultimate Party Identification Example
  slug: transfers-ultimate-party-identification-example
- key_count: 4
  name: Transfers Us Local Account Identification Example
  slug: transfers-us-local-account-identification-example
- key_count: 3
  name: Webhooks Ach Notification Of Change Notification Request Data Example
  slug: webhooks-ach-notification-of-change-notification-request-data-example
- key_count: 4
  name: Webhooks Ach Notification Of Change Notification Request Data Noc Example
  slug: webhooks-ach-notification-of-change-notification-request-data-noc-example
- key_count: 5
  name: Webhooks Ach Notification Of Change Notification Request Example
  slug: webhooks-ach-notification-of-change-notification-request-example
- key_count: 2
  name: Webhooks Amount Example
  slug: webhooks-amount-example
- key_count: 143
  name: Webhooks Authorisation Notification Additional Data Example
  slug: webhooks-authorisation-notification-additional-data-example
- key_count: 2
  name: Webhooks Authorisation Notification Request Example
  slug: webhooks-authorisation-notification-request-example
- key_count: 11
  name: Webhooks Authorisation Notification Request Item Example
  slug: webhooks-authorisation-notification-request-item-example
- key_count: 1
  name: Webhooks Authorisation Notification Request Item Wrapper Example
  slug: webhooks-authorisation-notification-request-item-wrapper-example
- key_count: 2
  name: Webhooks Expire Notification Request Example
  slug: webhooks-expire-notification-request-example
- key_count: 11
  name: Webhooks Expire Notification Request Item Example
  slug: webhooks-expire-notification-request-item-example
- key_count: 1
  name: Webhooks Expire Notification Request Item Wrapper Example
  slug: webhooks-expire-notification-request-item-wrapper-example
- key_count: 121
  name: Webhooks Notification Additional Data Example
  slug: webhooks-notification-additional-data-example
- key_count: 2
  name: Webhooks Notification Request Example
  slug: webhooks-notification-request-example
- key_count: 11
  name: Webhooks Notification Request Item Example
  slug: webhooks-notification-request-item-example
- key_count: 1
  name: Webhooks Notification Request Item Wrapper Example
  slug: webhooks-notification-request-item-wrapper-example
- key_count: 1
  name: Webhooks Notification Response Example
  slug: webhooks-notification-response-example
- key_count: 2
  name: Webhooks Paidout Reversed Notification Request Example
  slug: webhooks-paidout-reversed-notification-request-example
- key_count: 11
  name: Webhooks Paidout Reversed Notification Request Item Example
  slug: webhooks-paidout-reversed-notification-request-item-example
- key_count: 1
  name: Webhooks Paidout Reversed Notification Request Item Wrapper Example
  slug: webhooks-paidout-reversed-notification-request-item-wrapper-example
- key_count: 122
  name: Webhooks Recurring Contract Notification Additional Data Example
  slug: webhooks-recurring-contract-notification-additional-data-example
- key_count: 2
  name: Webhooks Recurring Contract Notification Request Example
  slug: webhooks-recurring-contract-notification-request-example
- key_count: 12
  name: Webhooks Recurring Contract Notification Request Item Example
  slug: webhooks-recurring-contract-notification-request-item-example
- key_count: 1
  name: Webhooks Recurring Contract Notification Request Item Wrapper Example
  slug: webhooks-recurring-contract-notification-request-item-wrapper-example
- key_count: 2
  name: Webhooks Report Available Notification Request Example
  slug: webhooks-report-available-notification-request-example
- key_count: 11
  name: Webhooks Report Available Notification Request Item Example
  slug: webhooks-report-available-notification-request-item-example
- key_count: 1
  name: Webhooks Report Available Notification Request Item Wrapper Example
  slug: webhooks-report-available-notification-request-item-wrapper-example
features:
- $0.13 fixed processing fee per transaction (no setup/monthly fees)
- 'Visa/Mastercard: $0.13 + Interchange++ + 0.60%'
- 'PayPal: $0.13 + direct contract + management fee'
- 'Klarna: $0.13 + 0.99%-4.99% + currency-specific fees'
- 'Affirm: $0.13 + 4.19%-5.19% + $0.30'
- 100 RPS API rate limit per merchant
- Single integration for 100+ payment methods
- Interchange++ transparent pricing
- Flexible payout timing and currency
- REST API for Payments, Recurring, Modifications
- Webhooks for transaction events
- Adyen Drop-In and Components for UI
- Risk and Revenue Accelerate add-ons
- Capital and Issuing for embedded finance
- POS terminals (hardware separate)
- Custom enterprise contracts with volume discounts
finops:
- name: Adyen Finops
  service_category: Payments
  slug: adyen-finops
graphqls:
- description: Adyen is a global enterprise payment platform offering a unified solution for accepting payments worldwide. Adyen's platform supports cards, digital wallets, local payment methods, point-of-sale termi
  name: Adyen GraphQL
  slug: adyen-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adyen.png
integrations:
- description: Pre-built plugin for Adobe Commerce and Magento e-commerce platforms with full payment method support.
  name: Adobe Commerce (Magento)
- description: Integration with Salesforce Commerce Cloud for seamless payment processing in SFCC storefronts.
  name: Salesforce Commerce Cloud
- description: Native plugin for Shopware e-commerce platform supporting all Adyen payment methods.
  name: Shopware
- description: Integration with SAP Commerce Cloud for enterprise e-commerce payment processing.
  name: SAP Commerce Cloud
- description: Partner integration with Shopify for accepting Adyen payments through Shopify stores.
  name: Shopify
- description: Integration with Oracle NetSuite ERP for payment processing and reconciliation.
  name: NetSuite
- description: Plugin for PrestaShop e-commerce platform enabling Adyen payment acceptance.
  name: PrestaShop
- description: Integration with CommerceTools headless commerce platform for flexible payment experiences.
  name: CommerceTools
json_schemas:
- name: AdditionalBankIdentification
  property_count: 2
  slug: accounting-notifications-additional-bank-identification
- name: Address-2
  property_count: 6
  slug: accounting-notifications-address-2
- name: AmountAdjustment
  property_count: 3
  slug: accounting-notifications-amount-adjustment
- name: Amount
  property_count: 2
  slug: accounting-notifications-amount
- name: AULocalAccountIdentification
  property_count: 3
  slug: accounting-notifications-au-local-account-identification
- name: BalanceMutation
  property_count: 4
  slug: accounting-notifications-balance-mutation
- name: BalancePlatformNotificationResponse
  property_count: 1
  slug: accounting-notifications-balance-platform-notification-response
- name: BankAccountV3
  property_count: 2
  slug: accounting-notifications-bank-account-v3
- name: BRLocalAccountIdentification
  property_count: 4
  slug: accounting-notifications-br-local-account-identification
- name: CALocalAccountIdentification
  property_count: 4
  slug: accounting-notifications-ca-local-account-identification
- name: CounterpartyV3
  property_count: 4
  slug: accounting-notifications-counterparty-v3
- name: CZLocalAccountIdentification
  property_count: 3
  slug: accounting-notifications-cz-local-account-identification
- name: DKLocalAccountIdentification
  property_count: 3
  slug: accounting-notifications-dk-local-account-identification
- name: HULocalAccountIdentification
  property_count: 2
  slug: accounting-notifications-hu-local-account-identification
- name: IbanAccountIdentification
  property_count: 2
  slug: accounting-notifications-iban-account-identification
- name: MerchantData
  property_count: 4
  slug: accounting-notifications-merchant-data
- name: NameLocation
  property_count: 6
  slug: accounting-notifications-name-location
- name: NOLocalAccountIdentification
  property_count: 2
  slug: accounting-notifications-no-local-account-identification
- name: NumberAndBicAccountIdentification
  property_count: 4
  slug: accounting-notifications-number-and-bic-account-identification
- name: PartyIdentification-2
  property_count: 5
  slug: accounting-notifications-party-identification-2
- name: PaymentInstrument
  property_count: 4
  slug: accounting-notifications-payment-instrument
- name: PLLocalAccountIdentification
  property_count: 2
  slug: accounting-notifications-pl-local-account-identification
- name: RelayedAuthorisationData-2
  property_count: 2
  slug: accounting-notifications-relayed-authorisation-data-2
- name: ResourceReference
  property_count: 3
  slug: accounting-notifications-resource-reference
- name: Resource
  property_count: 3
  slug: accounting-notifications-resource
- name: SELocalAccountIdentification
  property_count: 3
  slug: accounting-notifications-se-local-account-identification
- name: SGLocalAccountIdentification
  property_count: 3
  slug: accounting-notifications-sg-local-account-identification
- name: TransactionEventViolation
  property_count: 3
  slug: accounting-notifications-transaction-event-violation
- name: TransactionRuleReference
  property_count: 3
  slug: accounting-notifications-transaction-rule-reference
- name: TransactionRuleSource
  property_count: 2
  slug: accounting-notifications-transaction-rule-source
- name: TransactionRulesResult
  property_count: 4
  slug: accounting-notifications-transaction-rules-result
- name: TransferEvent
  property_count: 11
  slug: accounting-notifications-transfer-event
- name: TransferNotificationData
  property_count: 31
  slug: accounting-notifications-transfer-notification-data
- name: TransferNotificationRequest
  property_count: 3
  slug: accounting-notifications-transfer-notification-request
- name: TransferNotificationTransferTracking
  property_count: 1
  slug: accounting-notifications-transfer-notification-transfer-tracking
- name: TransferNotificationValidationFact
  property_count: 2
  slug: accounting-notifications-transfer-notification-validation-fact
- name: UKLocalAccountIdentification
  property_count: 3
  slug: accounting-notifications-uk-local-account-identification
- name: USLocalAccountIdentification
  property_count: 4
  slug: accounting-notifications-us-local-account-identification
- name: AccountEvent
  property_count: 3
  slug: accounts-account-event
- name: AccountHolderDetails
  property_count: 15
  slug: accounts-account-holder-details
- name: AccountHolderStatus
  property_count: 5
  slug: accounts-account-holder-status
- name: AccountPayoutState
  property_count: 6
  slug: accounts-account-payout-state
- name: AccountProcessingState
  property_count: 5
  slug: accounts-account-processing-state
- name: Account
  property_count: 10
  slug: accounts-account
- name: Amount
  property_count: 2
  slug: accounts-amount
- name: BankAccountDetail
  property_count: 26
  slug: accounts-bank-account-detail
- name: BusinessDetails
  property_count: 10
  slug: accounts-business-details
- name: CloseAccountHolderRequest
  property_count: 1
  slug: accounts-close-account-holder-request
- name: CloseAccountHolderResponse
  property_count: 4
  slug: accounts-close-account-holder-response
- name: CloseAccountRequest
  property_count: 1
  slug: accounts-close-account-request
- name: CloseAccountResponse
  property_count: 5
  slug: accounts-close-account-response
- name: CloseStoresRequest
  property_count: 2
  slug: accounts-close-stores-request
- name: CreateAccountHolderRequest
  property_count: 8
  slug: accounts-create-account-holder-request
- name: CreateAccountHolderResponse
  property_count: 12
  slug: accounts-create-account-holder-response
- name: CreateAccountRequest
  property_count: 8
  slug: accounts-create-account-request
- name: CreateAccountResponse
  property_count: 12
  slug: accounts-create-account-response
- name: DeleteBankAccountRequest
  property_count: 2
  slug: accounts-delete-bank-account-request
- name: DeleteLegalArrangementRequest
  property_count: 2
  slug: accounts-delete-legal-arrangement-request
- name: DeletePayoutMethodRequest
  property_count: 2
  slug: accounts-delete-payout-method-request
- name: DeleteShareholderRequest
  property_count: 2
  slug: accounts-delete-shareholder-request
- name: DeleteSignatoriesRequest
  property_count: 2
  slug: accounts-delete-signatories-request
- name: DocumentDetail
  property_count: 9
  slug: accounts-document-detail
- name: ErrorFieldType
  property_count: 3
  slug: accounts-error-field-type
- name: FieldType
  property_count: 3
  slug: accounts-field-type
- name: GenericResponse
  property_count: 3
  slug: accounts-generic-response
- name: GetAccountHolderRequest
  property_count: 3
  slug: accounts-get-account-holder-request
- name: GetAccountHolderResponse
  property_count: 14
  slug: accounts-get-account-holder-response
- name: GetAccountHolderStatusResponse
  property_count: 5
  slug: accounts-get-account-holder-status-response
- name: GetTaxFormRequest
  property_count: 3
  slug: accounts-get-tax-form-request
- name: GetTaxFormResponse
  property_count: 5
  slug: accounts-get-tax-form-response
- name: GetUploadedDocumentsRequest
  property_count: 3
  slug: accounts-get-uploaded-documents-request
- name: GetUploadedDocumentsResponse
  property_count: 4
  slug: accounts-get-uploaded-documents-response
- name: IndividualDetails
  property_count: 2
  slug: accounts-individual-details
- name: KYCCheckResult
  property_count: 1
  slug: accounts-kyc-check-result
- name: KYCCheckStatusData
  property_count: 4
  slug: accounts-kyc-check-status-data
- name: KYCCheckSummary
  property_count: 2
  slug: accounts-kyc-check-summary
- name: KYCLegalArrangementCheckResult
  property_count: 2
  slug: accounts-kyc-legal-arrangement-check-result
- name: KYCLegalArrangementEntityCheckResult
  property_count: 3
  slug: accounts-kyc-legal-arrangement-entity-check-result
- name: KYCPayoutMethodCheckResult
  property_count: 2
  slug: accounts-kyc-payout-method-check-result
- name: KYCShareholderCheckResult
  property_count: 4
  slug: accounts-kyc-shareholder-check-result
- name: KYCSignatoryCheckResult
  property_count: 2
  slug: accounts-kyc-signatory-check-result
- name: KYCUltimateParentCompanyCheckResult
  property_count: 2
  slug: accounts-kyc-ultimate-parent-company-check-result
- name: KYCVerificationResult
  property_count: 7
  slug: accounts-kyc-verification-result
- name: LegalArrangementDetail
  property_count: 9
  slug: accounts-legal-arrangement-detail
- name: LegalArrangementEntityDetail
  property_count: 11
  slug: accounts-legal-arrangement-entity-detail
- name: LegalArrangementRequest
  property_count: 2
  slug: accounts-legal-arrangement-request
- name: MigratedAccounts
  property_count: 2
  slug: accounts-migrated-accounts
- name: MigratedShareholders
  property_count: 2
  slug: accounts-migrated-shareholders
- name: MigratedStores
  property_count: 4
  slug: accounts-migrated-stores
- name: MigrationData
  property_count: 7
  slug: accounts-migration-data
- name: PayoutMethod
  property_count: 5
  slug: accounts-payout-method
- name: PayoutScheduleResponse
  property_count: 2
  slug: accounts-payout-schedule-response
- name: PerformVerificationRequest
  property_count: 3
  slug: accounts-perform-verification-request
- name: PersonalDocumentData
  property_count: 5
  slug: accounts-personal-document-data
- name: ShareholderContact
  property_count: 11
  slug: accounts-shareholder-contact
- name: SignatoryContact
  property_count: 10
  slug: accounts-signatory-contact
- name: StoreDetail
  property_count: 15
  slug: accounts-store-detail
- name: SuspendAccountHolderRequest
  property_count: 1
  slug: accounts-suspend-account-holder-request
- name: SuspendAccountHolderResponse
  property_count: 4
  slug: accounts-suspend-account-holder-response
- name: UltimateParentCompanyBusinessDetails
  property_count: 5
  slug: accounts-ultimate-parent-company-business-details
- name: UltimateParentCompany
  property_count: 3
  slug: accounts-ultimate-parent-company
- name: UnSuspendAccountHolderRequest
  property_count: 1
  slug: accounts-un-suspend-account-holder-request
- name: UnSuspendAccountHolderResponse
  property_count: 4
  slug: accounts-un-suspend-account-holder-response
- name: UpdateAccountHolderRequest
  property_count: 7
  slug: accounts-update-account-holder-request
- name: UpdateAccountHolderResponse
  property_count: 11
  slug: accounts-update-account-holder-response
- name: UpdateAccountHolderStateRequest
  property_count: 4
  slug: accounts-update-account-holder-state-request
- name: UpdateAccountRequest
  property_count: 7
  slug: accounts-update-account-request
- name: UpdateAccountResponse
  property_count: 10
  slug: accounts-update-account-response
- name: UpdatePayoutScheduleRequest
  property_count: 3
  slug: accounts-update-payout-schedule-request
- name: UploadDocumentRequest
  property_count: 2
  slug: accounts-upload-document-request
- name: ViasAddress
  property_count: 6
  slug: accounts-vias-address
- name: ViasName
  property_count: 4
  slug: accounts-vias-name
- name: ViasPersonalData
  property_count: 3
  slug: accounts-vias-personal-data
- name: ViasPhoneNumber
  property_count: 3
  slug: accounts-vias-phone-number
- name: AbortRequest
  property_count: 3
  slug: adyen-abortrequest
- name: AcceptDisputeRequest
  property_count: 2
  slug: adyen-acceptdisputerequest
- name: AcceptDisputeResponse
  property_count: 1
  slug: adyen-acceptdisputeresponse
- name: AcceptTermsOfServiceRequest
  property_count: 2
  slug: adyen-accepttermsofservicerequest
- name: AcceptTermsOfServiceResponse
  property_count: 6
  slug: adyen-accepttermsofserviceresponse
- name: Account
  property_count: 10
  slug: adyen-account
- name: AccountCapabilityData
  property_count: 8
  slug: adyen-accountcapabilitydata
- name: AccountCloseNotification
  property_count: 7
  slug: adyen-accountclosenotification
- name: AccountCreateNotification
  property_count: 7
  slug: adyen-accountcreatenotification
- name: AccountCreateNotificationData
  property_count: 5
  slug: adyen-accountcreatenotificationdata
- name: AccountDetailBalance
  property_count: 2
  slug: adyen-accountdetailbalance
- name: AccountEvent
  property_count: 3
  slug: adyen-accountevent
- name: AccountFundsBelowThresholdNotification
  property_count: 7
  slug: adyen-accountfundsbelowthresholdnotification
- name: AccountFundsBelowThresholdNotificationContent
  property_count: 5
  slug: adyen-accountfundsbelowthresholdnotificationcontent
- name: AccountHolder
  property_count: 13
  slug: adyen-accountholder
- name: AccountHolderBalanceRequest
  property_count: 1
  slug: adyen-accountholderbalancerequest
- name: AccountHolderBalanceResponse
  property_count: 5
  slug: adyen-accountholderbalanceresponse
- name: AccountHolderCapability
  property_count: 10
  slug: adyen-accountholdercapability
- name: AccountHolderCreateNotification
  property_count: 7
  slug: adyen-accountholdercreatenotification
- name: AccountHolderDetails
  property_count: 15
  slug: adyen-accountholderdetails
- name: AccountHolderInfo
  property_count: 9
  slug: adyen-accountholderinfo
- name: AccountHolderNotificationData
  property_count: 2
  slug: adyen-accountholdernotificationdata
- name: AccountHolderNotificationRequest
  property_count: 3
  slug: adyen-accountholdernotificationrequest
- name: AccountHolderPayoutNotification
  property_count: 7
  slug: adyen-accountholderpayoutnotification
- name: AccountHolderPayoutNotificationContent
  property_count: 17
  slug: adyen-accountholderpayoutnotificationcontent
- name: AccountHolderStatus
  property_count: 5
  slug: adyen-accountholderstatus
- name: AccountHolderStatusChangeNotification
  property_count: 7
  slug: adyen-accountholderstatuschangenotification
- name: AccountHolderStatusChangeNotificationContent
  property_count: 5
  slug: adyen-accountholderstatuschangenotificationcontent
- name: AccountHolderStoreStatusChangeNotification
  property_count: 7
  slug: adyen-accountholderstorestatuschangenotification
- name: AccountHolderStoreStatusChangeNotificationContent
  property_count: 7
  slug: adyen-accountholderstorestatuschangenotificationcontent
- name: AccountHolderTransactionListRequest
  property_count: 3
  slug: adyen-accountholdertransactionlistrequest
- name: AccountHolderTransactionListResponse
  property_count: 4
  slug: adyen-accountholdertransactionlistresponse
- name: AccountHolderUpcomingDeadlineNotification
  property_count: 7
  slug: adyen-accountholderupcomingdeadlinenotification
- name: AccountHolderUpcomingDeadlineNotificationContent
  property_count: 4
  slug: adyen-accountholderupcomingdeadlinenotificationcontent
- name: AccountHolderUpdateNotification
  property_count: 7
  slug: adyen-accountholderupdatenotification
- name: AccountHolderUpdateRequest
  property_count: 11
  slug: adyen-accountholderupdaterequest
- name: AccountHolderVerificationNotification
  property_count: 7
  slug: adyen-accountholderverificationnotification
- name: AccountHolderVerificationNotificationContent
  property_count: 7
  slug: adyen-accountholderverificationnotificationcontent
- name: AccountInfo
  property_count: 19
  slug: adyen-accountinfo
- name: AccountNotificationResponse
  property_count: 1
  slug: adyen-accountnotificationresponse
- name: AccountPayoutState
  property_count: 6
  slug: adyen-accountpayoutstate
- name: AccountProcessingState
  property_count: 5
  slug: adyen-accountprocessingstate
- name: AccountSupportingEntityCapability
  property_count: 7
  slug: adyen-accountsupportingentitycapability
- name: AccountTransactionList
  property_count: 3
  slug: adyen-accounttransactionlist
- name: AccountType
  property_count: 0
  slug: adyen-accounttype
- name: AccountUpdateNotification
  property_count: 7
  slug: adyen-accountupdatenotification
- name: AccountUpdateNotificationData
  property_count: 4
  slug: adyen-accountupdatenotificationdata
- name: AcctInfo
  property_count: 16
  slug: adyen-acctinfo
- name: ACH Direct Debit
  property_count: 10
  slug: adyen-achdetails
- name: AchNotificationOfChangeNotificationRequest
  property_count: 5
  slug: adyen-achnotificationofchangenotificationrequest
- name: AchNotificationOfChangeNotificationRequestData
  property_count: 3
  slug: adyen-achnotificationofchangenotificationrequestdata
- name: AchNotificationOfChangeNotificationRequestDataNoc
  property_count: 4
  slug: adyen-achnotificationofchangenotificationrequestdatanoc
- name: ActiveNetworkTokensRestriction
  property_count: 2
  slug: adyen-activenetworktokensrestriction
- name: AdditionalBankIdentification
  property_count: 2
  slug: adyen-additionalbankidentification
- name: AdditionalCommission
  property_count: 3
  slug: adyen-additionalcommission
- name: AdditionalData3DSecure
  property_count: 6
  slug: adyen-additionaldata3dsecure
- name: AdditionalDataAirline
  property_count: 28
  slug: adyen-additionaldataairline
- name: AdditionalDataCarRental
  property_count: 23
  slug: adyen-additionaldatacarrental
- name: AdditionalDataCommon
  property_count: 16
  slug: adyen-additionaldatacommon
- name: AdditionalDataLevel23
  property_count: 17
  slug: adyen-additionaldatalevel23
- name: AdditionalDataLodging
  property_count: 16
  slug: adyen-additionaldatalodging
- name: AdditionalDataModifications
  property_count: 1
  slug: adyen-additionaldatamodifications
- name: AdditionalDataOpenInvoice
  property_count: 18
  slug: adyen-additionaldataopeninvoice
- name: AdditionalDataOpi
  property_count: 1
  slug: adyen-additionaldataopi
- name: AdditionalDataRatepay
  property_count: 8
  slug: adyen-additionaldataratepay
- name: AdditionalDataRetry
  property_count: 3
  slug: adyen-additionaldataretry
- name: AdditionalDataRisk
  property_count: 21
  slug: adyen-additionaldatarisk
- name: AdditionalDataRiskStandalone
  property_count: 15
  slug: adyen-additionaldatariskstandalone
- name: AdditionalDataSubMerchant
  property_count: 10
  slug: adyen-additionaldatasubmerchant
- name: AdditionalDataTemporaryServices
  property_count: 9
  slug: adyen-additionaldatatemporaryservices
- name: AdditionalDataWallets
  property_count: 6
  slug: adyen-additionaldatawallets
- name: AdditionalSettings
  property_count: 2
  slug: adyen-additionalsettings
- name: AdditionalSettingsResponse
  property_count: 3
  slug: adyen-additionalsettingsresponse
- name: Address-2
  property_count: 6
  slug: adyen-address-2
- name: Address
  property_count: 6
  slug: adyen-address
- name: AddressRequirement
  property_count: 3
  slug: adyen-addressrequirement
- name: AdjustAuthorisationRequest
  property_count: 11
  slug: adyen-adjustauthorisationrequest
- name: AdminRequest
  property_count: 1
  slug: adyen-adminrequest
- name: AdminResponse
  property_count: 1
  slug: adyen-adminresponse
- name: Afterpay
  property_count: 7
  slug: adyen-afterpaydetails
- name: AfterpayTouchInfo
  property_count: 1
  slug: adyen-afterpaytouchinfo
- name: Alignment
  property_count: 0
  slug: adyen-alignment
- name: AllowedOrigin
  property_count: 3
  slug: adyen-allowedorigin
- name: AllowedOriginsResponse
  property_count: 1
  slug: adyen-allowedoriginsresponse
- name: AllowedProduct
  property_count: 4
  slug: adyen-allowedproduct
- name: Amazon Pay
  property_count: 4
  slug: adyen-amazonpaydetails
- name: Amount
  property_count: 2
  slug: adyen-amount
- name: AmountAdjustment
  property_count: 3
  slug: adyen-amountadjustment
- name: AmountMinMaxRequirement
  property_count: 4
  slug: adyen-amountminmaxrequirement
- name: AmountsReq
  property_count: 8
  slug: adyen-amountsreq
- name: AmountsResp
  property_count: 6
  slug: adyen-amountsresp
- name: AndroidApp
  property_count: 8
  slug: adyen-androidapp
- name: AndroidAppsResponse
  property_count: 1
  slug: adyen-androidappsresponse
- name: AndroidCertificate
  property_count: 7
  slug: adyen-androidcertificate
- name: AndroidCertificatesResponse
  property_count: 1
  slug: adyen-androidcertificatesresponse
- name: Android Pay
  property_count: 2
  slug: adyen-androidpaydetails
- name: ApiCredential
  property_count: 9
  slug: adyen-apicredential
- name: ApiCredentialLinks
  property_count: 6
  slug: adyen-apicredentiallinks
- name: Apple Pay
  property_count: 6
  slug: adyen-applepaydetails
- name: Apple Pay
  property_count: 6
  slug: adyen-applepaydonations
- name: ApplePayInfo
  property_count: 1
  slug: adyen-applepayinfo
- name: ApplePaySessionRequest
  property_count: 3
  slug: adyen-applepaysessionrequest
- name: ApplePaySessionResponse
  property_count: 1
  slug: adyen-applepaysessionresponse
- name: ApplicationInfo
  property_count: 6
  slug: adyen-applicationinfo
- name: AreaSize
  property_count: 2
  slug: adyen-areasize
- name: AssignTerminalsRequest
  property_count: 5
  slug: adyen-assignterminalsrequest
- name: AssignTerminalsResponse
  property_count: 1
  slug: adyen-assignterminalsresponse
- name: Attachment
  property_count: 5
  slug: adyen-attachment
- name: AULocalAccountIdentification
  property_count: 3
  slug: adyen-aulocalaccountidentification
- name: Authentication
  property_count: 3
  slug: adyen-authentication
- name: AuthenticationData
  property_count: 3
  slug: adyen-authenticationdata
- name: AuthenticationInfo
  property_count: 15
  slug: adyen-authenticationinfo
- name: AuthenticationMethod
  property_count: 0
  slug: adyen-authenticationmethod
- name: AuthenticationNotificationData
  property_count: 6
  slug: adyen-authenticationnotificationdata
- name: AuthenticationNotificationRequest
  property_count: 3
  slug: adyen-authenticationnotificationrequest
- name: AuthenticationResultRequest
  property_count: 2
  slug: adyen-authenticationresultrequest
- name: AuthenticationResultResponse
  property_count: 2
  slug: adyen-authenticationresultresponse
- name: AuthorisationNotificationAdditionalData
  property_count: 143
  slug: adyen-authorisationnotificationadditionaldata
- name: AuthorisationNotificationRequest
  property_count: 2
  slug: adyen-authorisationnotificationrequest
- name: AuthorisationNotificationRequestItem
  property_count: 11
  slug: adyen-authorisationnotificationrequestitem
- name: AuthorisationNotificationRequestItemWrapper
  property_count: 1
  slug: adyen-authorisationnotificationrequestitemwrapper
- name: Avs
  property_count: 2
  slug: adyen-avs
- name: AvsAddress
  property_count: 2
  slug: adyen-avsaddress
- name: BACS Direct Debit
  property_count: 7
  slug: adyen-bacsdirectdebitdetails
- name: Balance
  property_count: 5
  slug: adyen-balance
- name: BalanceAccount
  property_count: 11
  slug: adyen-balanceaccount
- name: BalanceAccountBase
  property_count: 10
  slug: adyen-balanceaccountbase
- name: BalanceAccountInfo
  property_count: 8
  slug: adyen-balanceaccountinfo
- name: BalanceAccountNotificationData
  property_count: 2
  slug: adyen-balanceaccountnotificationdata
- name: BalanceAccountNotificationRequest
  property_count: 3
  slug: adyen-balanceaccountnotificationrequest
- name: BalanceAccountUpdateRequest
  property_count: 7
  slug: adyen-balanceaccountupdaterequest
- name: BalanceCheckRequest
  property_count: 44
  slug: adyen-balancecheckrequest
- name: BalanceCheckResponse
  property_count: 7
  slug: adyen-balancecheckresponse
- name: BalanceInquiryRequest
  property_count: 2
  slug: adyen-balanceinquiryrequest
- name: BalanceInquiryResponse
  property_count: 4
  slug: adyen-balanceinquiryresponse
- name: BalanceMutation
  property_count: 4
  slug: adyen-balancemutation
- name: BalancePlatform
  property_count: 3
  slug: adyen-balanceplatform
- name: BalancePlatformNotificationResponse
  property_count: 1
  slug: adyen-balanceplatformnotificationresponse
- name: BalanceSweepConfigurationsResponse
  property_count: 3
  slug: adyen-balancesweepconfigurationsresponse
- name: BalanceTransferRequest
  property_count: 6
  slug: adyen-balancetransferrequest
- name: BalanceTransferResponse
  property_count: 9
  slug: adyen-balancetransferresponse
- name: BankAccount
  property_count: 9
  slug: adyen-bankaccount
- name: BankAccountDetail
  property_count: 26
  slug: adyen-bankaccountdetail
- name: BankAccountIdentificationTypeRequirement
  property_count: 3
  slug: adyen-bankaccountidentificationtyperequirement
- name: BankAccountIdentificationValidationRequest
  property_count: 1
  slug: adyen-bankaccountidentificationvalidationrequest
- name: BankAccountInfo
  property_count: 5
  slug: adyen-bankaccountinfo
- name: BankAccountModel
  property_count: 1
  slug: adyen-bankaccountmodel
- name: BankAccountV3
  property_count: 2
  slug: adyen-bankaccountv3
- name: BankCategoryData
  property_count: 2
  slug: adyen-bankcategorydata
- name: BankIdentification
  property_count: 3
  slug: adyen-bankidentification
- name: BarcodeType
  property_count: 0
  slug: adyen-barcodetype
- name: BcmcInfo
  property_count: 2
  slug: adyen-bcmcinfo
- name: BeneficiarySetupNotification
  property_count: 7
  slug: adyen-beneficiarysetupnotification
- name: BeneficiarySetupNotificationContent
  property_count: 7
  slug: adyen-beneficiarysetupnotificationcontent
- name: BillDesk
  property_count: 3
  slug: adyen-billdeskdetails
- name: BillingAddress
  property_count: 6
  slug: adyen-billingaddress
- name: BillingEntitiesResponse
  property_count: 1
  slug: adyen-billingentitiesresponse
- name: BillingEntity
  property_count: 5
  slug: adyen-billingentity
- name: BinDetail
  property_count: 1
  slug: adyen-bindetail
- name: BirthData
  property_count: 1
  slug: adyen-birthdata
- name: BLIK
  property_count: 5
  slug: adyen-blikdetails
- name: BrandVariantsRestriction
  property_count: 2
  slug: adyen-brandvariantsrestriction
- name: BRLocalAccountIdentification
  property_count: 4
  slug: adyen-brlocalaccountidentification
- name: BrowserInfo
  property_count: 9
  slug: adyen-browserinfo
- name: BulkAddress
  property_count: 9
  slug: adyen-bulkaddress
- name: BusinessDetails
  property_count: 10
  slug: adyen-businessdetails
- name: BusinessLine
  property_count: 10
  slug: adyen-businessline
- name: BusinessLineInfo
  property_count: 8
  slug: adyen-businesslineinfo
- name: BusinessLineInfoUpdate
  property_count: 8
  slug: adyen-businesslineinfoupdate
- name: BusinessLines
  property_count: 1
  slug: adyen-businesslines
- name: CalculateTermsOfServiceStatusResponse
  property_count: 1
  slug: adyen-calculatetermsofservicestatusresponse
- name: CALocalAccountIdentification
  property_count: 4
  slug: adyen-calocalaccountidentification
- name: CancelOrderRequest
  property_count: 2
  slug: adyen-cancelorderrequest
- name: CancelOrderResponse
  property_count: 2
  slug: adyen-cancelorderresponse
- name: CancelOrRefundRequest
  property_count: 9
  slug: adyen-cancelorrefundrequest
- name: CancelRequest
  property_count: 10
  slug: adyen-cancelrequest
- name: CapabilityProblem
  property_count: 2
  slug: adyen-capabilityproblem
- name: CapabilityProblemEntity-recursive
  property_count: 3
  slug: adyen-capabilityproblementity-recursive
- name: CapabilityProblemEntity
  property_count: 4
  slug: adyen-capabilityproblementity
- name: CapabilitySettings
  property_count: 5
  slug: adyen-capabilitysettings
- name: CapitalBalance
  property_count: 4
  slug: adyen-capitalbalance
- name: CapitalGrant
  property_count: 9
  slug: adyen-capitalgrant
- name: CapitalGrantAccount
  property_count: 4
  slug: adyen-capitalgrantaccount
- name: CapitalGrantInfo
  property_count: 3
  slug: adyen-capitalgrantinfo
- name: CapitalGrants
  property_count: 1
  slug: adyen-capitalgrants
- name: CapturedSignature
  property_count: 2
  slug: adyen-capturedsignature
- name: CaptureRequest
  property_count: 11
  slug: adyen-capturerequest
- name: Card
  property_count: 8
  slug: adyen-card
- name: CardAcquisitionRequest
  property_count: 2
  slug: adyen-cardacquisitionrequest
- name: CardAcquisitionResponse
  property_count: 7
  slug: adyen-cardacquisitionresponse
- name: CardAcquisitionTransaction
  property_count: 9
  slug: adyen-cardacquisitiontransaction
- name: CardBin
  property_count: 11
  slug: adyen-cardbin
- name: CardBrandDetails
  property_count: 2
  slug: adyen-cardbranddetails
- name: CardConfiguration
  property_count: 14
  slug: adyen-cardconfiguration
- name: CardData
  property_count: 11
  slug: adyen-carddata
- name: Card
  property_count: 19
  slug: adyen-carddetails
- name: CardDetailsRequest
  property_count: 5
  slug: adyen-carddetailsrequest
- name: CardDetailsResponse
  property_count: 1
  slug: adyen-carddetailsresponse
- name: Card
  property_count: 19
  slug: adyen-carddonations
- name: CardHolderPIN
  property_count: 3
  slug: adyen-cardholderpin
- name: CardholderReceipt
  property_count: 1
  slug: adyen-cardholderreceipt
- name: CardInfo
  property_count: 8
  slug: adyen-cardinfo
- name: CardOrder
  property_count: 8
  slug: adyen-cardorder
- name: CardOrderItem
  property_count: 8
  slug: adyen-cardorderitem
- name: CardOrderItemDeliveryStatus
  property_count: 3
  slug: adyen-cardorderitemdeliverystatus
- name: CardOrderNotificationRequest
  property_count: 3
  slug: adyen-cardordernotificationrequest
- name: CardReaderAPDURequest
  property_count: 6
  slug: adyen-cardreaderapdurequest
- name: CardReaderAPDUResponse
  property_count: 3
  slug: adyen-cardreaderapduresponse
- name: CartesBancairesInfo
  property_count: 2
  slug: adyen-cartesbancairesinfo
- name: CashHandlingDevice
  property_count: 3
  slug: adyen-cashhandlingdevice
- name: Cellulant
  property_count: 3
  slug: adyen-cellulantdetails
- name: ChallengeInfo
  property_count: 6
  slug: adyen-challengeinfo
- name: CharacterHeight
  property_count: 0
  slug: adyen-characterheight
- name: CharacterStyle
  property_count: 0
  slug: adyen-characterstyle
- name: CharacterWidth
  property_count: 0
  slug: adyen-characterwidth
- name: CheckData
  property_count: 7
  slug: adyen-checkdata
- name: CheckoutAwaitAction
  property_count: 4
  slug: adyen-checkoutawaitaction
- name: CheckoutDelegatedAuthenticationAction
  property_count: 6
  slug: adyen-checkoutdelegatedauthenticationaction
- name: CheckoutNativeRedirectAction
  property_count: 6
  slug: adyen-checkoutnativeredirectaction
- name: CheckoutOrderResponse
  property_count: 6
  slug: adyen-checkoutorderresponse
- name: CheckoutQrCodeAction
  property_count: 6
  slug: adyen-checkoutqrcodeaction
- name: CheckoutRedirectAction
  property_count: 5
  slug: adyen-checkoutredirectaction
- name: CheckoutSDKAction
  property_count: 5
  slug: adyen-checkoutsdkaction
- name: CheckoutSessionInstallmentOption
  property_count: 3
  slug: adyen-checkoutsessioninstallmentoption
- name: CheckoutThreeDS2Action
  property_count: 7
  slug: adyen-checkoutthreeds2action
- name: CheckoutVoucherAction
  property_count: 21
  slug: adyen-checkoutvoucheraction
- name: ClearpayInfo
  property_count: 1
  slug: adyen-clearpayinfo
- name: CloseAccountHolderRequest
  property_count: 1
  slug: adyen-closeaccountholderrequest
- name: CloseAccountHolderResponse
  property_count: 4
  slug: adyen-closeaccountholderresponse
- name: CloseAccountRequest
  property_count: 1
  slug: adyen-closeaccountrequest
- name: CloseAccountResponse
  property_count: 5
  slug: adyen-closeaccountresponse
- name: CloseStoresRequest
  property_count: 2
  slug: adyen-closestoresrequest
- name: CoinsOrBills
  property_count: 2
  slug: adyen-coinsorbills
- name: CollectInformation
  property_count: 6
  slug: adyen-collectinformation
- name: Color
  property_count: 0
  slug: adyen-color
- name: Commission
  property_count: 2
  slug: adyen-commission
- name: CommonField
  property_count: 2
  slug: adyen-commonfield
- name: Company
  property_count: 6
  slug: adyen-company
- name: CompanyApiCredential
  property_count: 10
  slug: adyen-companyapicredential
- name: CompanyLinks
  property_count: 4
  slug: adyen-companylinks
- name: CompanyUser
  property_count: 11
  slug: adyen-companyuser
- name: CompensateNegativeBalanceNotification
  property_count: 7
  slug: adyen-compensatenegativebalancenotification
- name: CompensateNegativeBalanceNotificationContent
  property_count: 1
  slug: adyen-compensatenegativebalancenotificationcontent
- name: CompensateNegativeBalanceNotificationRecord
  property_count: 3
  slug: adyen-compensatenegativebalancenotificationrecord
- name: Configuration
  property_count: 4
  slug: adyen-configuration
- name: Connectivity
  property_count: 1
  slug: adyen-connectivity
- name: Contact
  property_count: 7
  slug: adyen-contact
- name: ContactDetails
  property_count: 4
  slug: adyen-contactdetails
- name: ConvertedAmount
  property_count: 2
  slug: adyen-convertedamount
- name: CostEstimateAssumptions
  property_count: 3
  slug: adyen-costestimateassumptions
- name: CostEstimateRequest
  property_count: 10
  slug: adyen-costestimaterequest
- name: CostEstimateResponse
  property_count: 5
  slug: adyen-costestimateresponse
- name: Counterparty
  property_count: 2
  slug: adyen-counterparty
- name: CounterpartyBankRestriction
  property_count: 2
  slug: adyen-counterpartybankrestriction
- name: CounterpartyInfoV3
  property_count: 3
  slug: adyen-counterpartyinfov3
- name: CounterpartyV3
  property_count: 4
  slug: adyen-counterpartyv3
- name: CountriesRestriction
  property_count: 2
  slug: adyen-countriesrestriction
- name: CreateAccountHolderRequest
  property_count: 8
  slug: adyen-createaccountholderrequest
- name: CreateAccountHolderResponse
  property_count: 12
  slug: adyen-createaccountholderresponse
- name: CreateAccountRequest
  property_count: 8
  slug: adyen-createaccountrequest
- name: CreateAccountResponse
  property_count: 12
  slug: adyen-createaccountresponse
- name: CreateAllowedOriginRequest
  property_count: 3
  slug: adyen-createallowedoriginrequest
- name: CreateApiCredentialResponse
  property_count: 11
  slug: adyen-createapicredentialresponse
- name: CreateCheckoutSessionRequest
  property_count: 59
  slug: adyen-createcheckoutsessionrequest
- name: CreateCheckoutSessionResponse
  property_count: 62
  slug: adyen-createcheckoutsessionresponse
- name: CreateCompanyApiCredentialRequest
  property_count: 4
  slug: adyen-createcompanyapicredentialrequest
- name: CreateCompanyApiCredentialResponse
  property_count: 12
  slug: adyen-createcompanyapicredentialresponse
- name: CreateCompanyUserRequest
  property_count: 7
  slug: adyen-createcompanyuserrequest
- name: CreateCompanyUserResponse
  property_count: 11
  slug: adyen-createcompanyuserresponse
- name: CreateCompanyWebhookRequest
  property_count: 16
  slug: adyen-createcompanywebhookrequest
- name: CreateMerchantApiCredentialRequest
  property_count: 3
  slug: adyen-createmerchantapicredentialrequest
- name: CreateMerchantRequest
  property_count: 7
  slug: adyen-createmerchantrequest
- name: CreateMerchantResponse
  property_count: 7
  slug: adyen-createmerchantresponse
- name: CreateMerchantUserRequest
  property_count: 6
  slug: adyen-createmerchantuserrequest
- name: CreateMerchantWebhookRequest
  property_count: 14
  slug: adyen-createmerchantwebhookrequest
- name: CreateNotificationConfigurationRequest
  property_count: 1
  slug: adyen-createnotificationconfigurationrequest
- name: CreateOrderRequest
  property_count: 4
  slug: adyen-createorderrequest
- name: CreateOrderResponse
  property_count: 10
  slug: adyen-createorderresponse
- name: CreatePermitRequest
  property_count: 4
  slug: adyen-createpermitrequest
- name: CreatePermitResult
  property_count: 2
  slug: adyen-createpermitresult
- name: CreateSweepConfigurationV2
  property_count: 12
  slug: adyen-createsweepconfigurationv2
- name: CreateTestCardRangesRequest
  property_count: 3
  slug: adyen-createtestcardrangesrequest
- name: CreateTestCardRangesResult
  property_count: 1
  slug: adyen-createtestcardrangesresult
- name: CreateUserResponse
  property_count: 10
  slug: adyen-createuserresponse
- name: CronSweepSchedule
  property_count: 2
  slug: adyen-cronsweepschedule
- name: Currency
  property_count: 3
  slug: adyen-currency
- name: CurrencyConversion
  property_count: 6
  slug: adyen-currencyconversion
- name: CustomerOrder
  property_count: 10
  slug: adyen-customerorder
- name: CustomerOrderReq
  property_count: 0
  slug: adyen-customerorderreq
- name: CustomNotification
  property_count: 7
  slug: adyen-customnotification
- name: CZLocalAccountIdentification
  property_count: 3
  slug: adyen-czlocalaccountidentification
- name: DataCenter
  property_count: 2
  slug: adyen-datacenter
- name: DataReviewConfirmationResponse
  property_count: 1
  slug: adyen-datareviewconfirmationresponse
- name: DayOfWeekRestriction
  property_count: 2
  slug: adyen-dayofweekrestriction
- name: DebitAccountHolderRequest
  property_count: 6
  slug: adyen-debitaccountholderrequest
- name: DebitAccountHolderResponse
  property_count: 6
  slug: adyen-debitaccountholderresponse
- name: DefendDisputeRequest
  property_count: 3
  slug: adyen-defenddisputerequest
- name: DefendDisputeResponse
  property_count: 1
  slug: adyen-defenddisputeresponse
- name: DefenseDocument
  property_count: 3
  slug: adyen-defensedocument
- name: DefenseDocumentType
  property_count: 3
  slug: adyen-defensedocumenttype
- name: DefenseReason
  property_count: 3
  slug: adyen-defensereason
- name: DefenseReasonsRequest
  property_count: 2
  slug: adyen-defensereasonsrequest
- name: DefenseReasonsResponse
  property_count: 2
  slug: adyen-defensereasonsresponse
- name: DeleteBankAccountRequest
  property_count: 2
  slug: adyen-deletebankaccountrequest
- name: DeleteDefenseDocumentRequest
  property_count: 3
  slug: adyen-deletedefensedocumentrequest
- name: DeleteDefenseDocumentResponse
  property_count: 1
  slug: adyen-deletedefensedocumentresponse
- name: DeleteLegalArrangementRequest
  property_count: 2
  slug: adyen-deletelegalarrangementrequest
- name: DeleteNotificationConfigurationRequest
  property_count: 1
  slug: adyen-deletenotificationconfigurationrequest
- name: DeletePayoutMethodRequest
  property_count: 2
  slug: adyen-deletepayoutmethodrequest
- name: DeleteShareholderRequest
  property_count: 2
  slug: adyen-deleteshareholderrequest
- name: DeleteSignatoriesRequest
  property_count: 2
  slug: adyen-deletesignatoriesrequest
- name: DeliveryAddress
  property_count: 8
  slug: adyen-deliveryaddress
- name: DeliveryContact
  property_count: 6
  slug: adyen-deliverycontact
- name: DetailBalance
  property_count: 3
  slug: adyen-detailbalance
- name: DetailsRequestAuthenticationData
  property_count: 1
  slug: adyen-detailsrequestauthenticationdata
- name: Device
  property_count: 0
  slug: adyen-device
- name: DeviceInfo
  property_count: 11
  slug: adyen-deviceinfo
- name: DeviceRenderOptions
  property_count: 2
  slug: adyen-devicerenderoptions
- name: DiagnosisRequest
  property_count: 3
  slug: adyen-diagnosisrequest
- name: DiagnosisResponse
  property_count: 4
  slug: adyen-diagnosisresponse
- name: DifferentCurrenciesRestriction
  property_count: 2
  slug: adyen-differentcurrenciesrestriction
- name: DirectDebitInitiatedNotification
  property_count: 7
  slug: adyen-directdebitinitiatednotification
- name: DirectDebitInitiatedNotificationContent
  property_count: 7
  slug: adyen-directdebitinitiatednotificationcontent
- name: DisablePermitRequest
  property_count: 2
  slug: adyen-disablepermitrequest
- name: DisablePermitResult
  property_count: 2
  slug: adyen-disablepermitresult
- name: DisableRequest
  property_count: 4
  slug: adyen-disablerequest
- name: DisableResult
  property_count: 1
  slug: adyen-disableresult
- name: DisplayOutput
  property_count: 7
  slug: adyen-displayoutput
- name: DisplayRequest
  property_count: 1
  slug: adyen-displayrequest
- name: DisplayResponse
  property_count: 1
  slug: adyen-displayresponse
- name: DisputeServiceResult
  property_count: 2
  slug: adyen-disputeserviceresult
- name: DKLocalAccountIdentification
  property_count: 3
  slug: adyen-dklocalaccountidentification
- name: Document
  property_count: 13
  slug: adyen-document
- name: DocumentDetail
  property_count: 9
  slug: adyen-documentdetail
- name: DocumentPage
  property_count: 3
  slug: adyen-documentpage
- name: DocumentQualifier
  property_count: 0
  slug: adyen-documentqualifier
- name: DocumentReference
  property_count: 7
  slug: adyen-documentreference
- name: Doku
  property_count: 5
  slug: adyen-dokudetails
- name: DonationPaymentRequest
  property_count: 41
  slug: adyen-donationpaymentrequest
- name: DonationPaymentResponse
  property_count: 7
  slug: adyen-donationpaymentresponse
- name: DonationRequest
  property_count: 6
  slug: adyen-donationrequest
- name: Dotpay
  property_count: 3
  slug: adyen-dotpaydetails
- name: Dragonpay
  property_count: 4
  slug: adyen-dragonpaydetails
- name: DSPublicKeyDetail
  property_count: 5
  slug: adyen-dspublickeydetail
- name: Duration
  property_count: 2
  slug: adyen-duration
- name: Voucher
  property_count: 6
  slug: adyen-econtextvoucherdetails
- name: EmptyRequest
  property_count: 0
  slug: adyen-emptyrequest
- name: EnableServiceRequest
  property_count: 3
  slug: adyen-enableservicerequest
- name: EnableServiceResponse
  property_count: 1
  slug: adyen-enableserviceresponse
- name: EncryptedOrderData
  property_count: 2
  slug: adyen-encryptedorderdata
- name: EntityReference
  property_count: 1
  slug: adyen-entityreference
- name: EntryMode
  property_count: 0
  slug: adyen-entrymode
- name: EntryModesRestriction
  property_count: 2
  slug: adyen-entrymodesrestriction
- name: ErrorCondition
  property_count: 0
  slug: adyen-errorcondition
- name: ErrorFieldType
  property_count: 3
  slug: adyen-errorfieldtype
- name: EventNotification
  property_count: 7
  slug: adyen-eventnotification
- name: EventToNotify
  property_count: 0
  slug: adyen-eventtonotify
- name: EventUrl
  property_count: 2
  slug: adyen-eventurl
- name: ExchangeMessage
  property_count: 2
  slug: adyen-exchangemessage
- name: ExpireNotificationRequest
  property_count: 2
  slug: adyen-expirenotificationrequest
- name: ExpireNotificationRequestItem
  property_count: 11
  slug: adyen-expirenotificationrequestitem
- name: ExpireNotificationRequestItemWrapper
  property_count: 1
  slug: adyen-expirenotificationrequestitemwrapper
- name: Expiry
  property_count: 2
  slug: adyen-expiry
- name: ExternalPlatform
  property_count: 3
  slug: adyen-externalplatform
- name: ExternalTerminalAction
  property_count: 8
  slug: adyen-externalterminalaction
- name: Fee
  property_count: 1
  slug: adyen-fee
- name: FieldType
  property_count: 3
  slug: adyen-fieldtype
- name: File
  property_count: 2
  slug: adyen-file
- name: FindTerminalRequest
  property_count: 1
  slug: adyen-findterminalrequest
- name: FindTerminalResponse
  property_count: 5
  slug: adyen-findterminalresponse
- name: ForceEntryMode
  property_count: 0
  slug: adyen-forceentrymode
- name: ForexQuote
  property_count: 12
  slug: adyen-forexquote
- name: FraudCheckResult
  property_count: 3
  slug: adyen-fraudcheckresult
- name: FraudCheckResultWrapper
  property_count: 1
  slug: adyen-fraudcheckresultwrapper
- name: FraudResult
  property_count: 2
  slug: adyen-fraudresult
- name: FundDestination
  property_count: 9
  slug: adyen-funddestination
- name: FundOrigin
  property_count: 5
  slug: adyen-fundorigin
- name: FundRecipient
  property_count: 10
  slug: adyen-fundrecipient
- name: FundSource
  property_count: 6
  slug: adyen-fundsource
- name: GenerateApiKeyResponse
  property_count: 1
  slug: adyen-generateapikeyresponse
- name: GenerateClientKeyResponse
  property_count: 1
  slug: adyen-generateclientkeyresponse
- name: GenerateHmacKeyResponse
  property_count: 1
  slug: adyen-generatehmackeyresponse
- name: GeneratePciDescriptionRequest
  property_count: 2
  slug: adyen-generatepcidescriptionrequest
- name: GeneratePciDescriptionResponse
  property_count: 3
  slug: adyen-generatepcidescriptionresponse
- name: Stored Payment Method
  property_count: 5
  slug: adyen-genericissuerpaymentmethoddetails
- name: GenericPmWithTdiInfo
  property_count: 1
  slug: adyen-genericpmwithtdiinfo
- name: GenericProfile
  property_count: 0
  slug: adyen-genericprofile
- name: GenericResponse
  property_count: 3
  slug: adyen-genericresponse
- name: GeographicCoordinates
  property_count: 2
  slug: adyen-geographiccoordinates
- name: Geolocation
  property_count: 2
  slug: adyen-geolocation
- name: GetAccountHolderRequest
  property_count: 3
  slug: adyen-getaccountholderrequest
- name: GetAccountHolderResponse
  property_count: 14
  slug: adyen-getaccountholderresponse
- name: GetAccountHolderStatusResponse
  property_count: 5
  slug: adyen-getaccountholderstatusresponse
- name: GetNetworkTokenResponse
  property_count: 1
  slug: adyen-getnetworktokenresponse
- name: GetNotificationConfigurationListResponse
  property_count: 4
  slug: adyen-getnotificationconfigurationlistresponse
- name: GetNotificationConfigurationRequest
  property_count: 1
  slug: adyen-getnotificationconfigurationrequest
- name: GetNotificationConfigurationResponse
  property_count: 4
  slug: adyen-getnotificationconfigurationresponse
- name: GetOnboardingUrlRequest
  property_count: 8
  slug: adyen-getonboardingurlrequest
- name: GetOnboardingUrlResponse
  property_count: 4
  slug: adyen-getonboardingurlresponse
- name: GetPciQuestionnaireInfosResponse
  property_count: 1
  slug: adyen-getpciquestionnaireinfosresponse
- name: GetPciQuestionnaireResponse
  property_count: 4
  slug: adyen-getpciquestionnaireresponse
- name: GetPciUrlRequest
  property_count: 2
  slug: adyen-getpciurlrequest
- name: GetPciUrlResponse
  property_count: 4
  slug: adyen-getpciurlresponse
- name: GetStoresUnderAccountRequest
  property_count: 2
  slug: adyen-getstoresunderaccountrequest
- name: GetStoresUnderAccountResponse
  property_count: 1
  slug: adyen-getstoresunderaccountresponse
- name: GetTaxFormRequest
  property_count: 3
  slug: adyen-gettaxformrequest
- name: GetTaxFormResponse
  property_count: 5
  slug: adyen-gettaxformresponse
- name: GetTerminalDetailsRequest
  property_count: 1
  slug: adyen-getterminaldetailsrequest
- name: GetTerminalDetailsResponse
  property_count: 25
  slug: adyen-getterminaldetailsresponse
- name: GetTerminalsUnderAccountRequest
  property_count: 3
  slug: adyen-getterminalsunderaccountrequest
- name: GetTerminalsUnderAccountResponse
  property_count: 3
  slug: adyen-getterminalsunderaccountresponse
- name: GetTermsOfServiceAcceptanceInfosResponse
  property_count: 1
  slug: adyen-gettermsofserviceacceptanceinfosresponse
- name: GetTermsOfServiceDocumentRequest
  property_count: 2
  slug: adyen-gettermsofservicedocumentrequest
- name: GetTermsOfServiceDocumentResponse
  property_count: 5
  slug: adyen-gettermsofservicedocumentresponse
- name: GetTotalsRequest
  property_count: 2
  slug: adyen-gettotalsrequest
- name: GetTotalsResponse
  property_count: 3
  slug: adyen-gettotalsresponse
- name: GetUploadedDocumentsRequest
  property_count: 3
  slug: adyen-getuploadeddocumentsrequest
- name: GetUploadedDocumentsResponse
  property_count: 4
  slug: adyen-getuploadeddocumentsresponse
- name: Giropay
  property_count: 4
  slug: adyen-giropaydetails
- name: GiroPayInfo
  property_count: 1
  slug: adyen-giropayinfo
- name: GlobalStatus
  property_count: 0
  slug: adyen-globalstatus
- name: Google Pay
  property_count: 7
  slug: adyen-googlepaydetails
- name: Google Pay
  property_count: 7
  slug: adyen-googlepaydonations
- name: GooglePayInfo
  property_count: 2
  slug: adyen-googlepayinfo
- name: GrantLimit
  property_count: 1
  slug: adyen-grantlimit
- name: GrantOffer
  property_count: 8
  slug: adyen-grantoffer
- name: GrantOffers
  property_count: 1
  slug: adyen-grantoffers
- name: Gratuity
  property_count: 4
  slug: adyen-gratuity
- name: Hardware
  property_count: 3
  slug: adyen-hardware
- name: HKLocalAccountIdentification
  property_count: 3
  slug: adyen-hklocalaccountidentification
- name: HostStatus
  property_count: 2
  slug: adyen-hoststatus
- name: HULocalAccountIdentification
  property_count: 2
  slug: adyen-hulocalaccountidentification
- name: IbanAccountIdentification
  property_count: 2
  slug: adyen-ibanaccountidentification
- name: ICCResetData
  property_count: 2
  slug: adyen-iccresetdata
- name: iDEAL
  property_count: 5
  slug: adyen-idealdetails
- name: iDEAL
  property_count: 5
  slug: adyen-idealdonations
- name: IdentificationData
  property_count: 7
  slug: adyen-identificationdata
- name: IdentificationSupport
  property_count: 0
  slug: adyen-identificationsupport
- name: IdentificationType
  property_count: 0
  slug: adyen-identificationtype
- name: IdName
  property_count: 2
  slug: adyen-idname
- name: IncomingTransferNotificationData
  property_count: 17
  slug: adyen-incomingtransfernotificationdata
- name: IncomingTransferNotificationRequest
  property_count: 3
  slug: adyen-incomingtransfernotificationrequest
- name: Individual
  property_count: 9
  slug: adyen-individual
- name: IndividualDetails
  property_count: 2
  slug: adyen-individualdetails
- name: InfoQualify
  property_count: 0
  slug: adyen-infoqualify
- name: Input
  property_count: 7
  slug: adyen-input
- name: InputCommand
  property_count: 0
  slug: adyen-inputcommand
- name: InputData
  property_count: 21
  slug: adyen-inputdata
- name: InputDetail
  property_count: 9
  slug: adyen-inputdetail
- name: InputRequest
  property_count: 2
  slug: adyen-inputrequest
- name: InputResponse
  property_count: 2
  slug: adyen-inputresponse
- name: InputResult
  property_count: 4
  slug: adyen-inputresult
- name: InputUpdate
  property_count: 7
  slug: adyen-inputupdate
- name: InstallAndroidAppDetails
  property_count: 2
  slug: adyen-installandroidappdetails
- name: InstallAndroidCertificateDetails
  property_count: 2
  slug: adyen-installandroidcertificatedetails
- name: InstallmentOption
  property_count: 4
  slug: adyen-installmentoption
- name: Installments
  property_count: 2
  slug: adyen-installments
- name: InstallmentsNumber
  property_count: 1
  slug: adyen-installmentsnumber
- name: Instalment
  property_count: 10
  slug: adyen-instalment
- name: InstalmentType
  property_count: 0
  slug: adyen-instalmenttype
- name: InternalCategoryData
  property_count: 3
  slug: adyen-internalcategorydata
- name: InternationalTransactionRestriction
  property_count: 2
  slug: adyen-internationaltransactionrestriction
- name: InvalidField
  property_count: 3
  slug: adyen-invalidfield
- name: IssuedCard
  property_count: 8
  slug: adyen-issuedcard
- name: Item
  property_count: 2
  slug: adyen-item
- name: JSONObject
  property_count: 0
  slug: adyen-jsonobject
- name: JSONPath
  property_count: 1
  slug: adyen-jsonpath
- name: Key
  property_count: 3
  slug: adyen-key
- name: Klarna
  property_count: 8
  slug: adyen-klarnadetails
- name: KlarnaInfo
  property_count: 4
  slug: adyen-klarnainfo
- name: KYCCheckResult
  property_count: 1
  slug: adyen-kyccheckresult
- name: KYCCheckStatusData
  property_count: 4
  slug: adyen-kyccheckstatusdata
- name: KYCCheckSummary
  property_count: 2
  slug: adyen-kycchecksummary
- name: KYCLegalArrangementCheckResult
  property_count: 2
  slug: adyen-kyclegalarrangementcheckresult
- name: KYCLegalArrangementEntityCheckResult
  property_count: 3
  slug: adyen-kyclegalarrangemententitycheckresult
- name: KYCPayoutMethodCheckResult
  property_count: 2
  slug: adyen-kycpayoutmethodcheckresult
- name: KYCShareholderCheckResult
  property_count: 4
  slug: adyen-kycshareholdercheckresult
- name: KYCSignatoryCheckResult
  property_count: 2
  slug: adyen-kycsignatorycheckresult
- name: KYCUltimateParentCompanyCheckResult
  property_count: 2
  slug: adyen-kycultimateparentcompanycheckresult
- name: KYCVerificationResult
  property_count: 7
  slug: adyen-kycverificationresult
- name: LegalArrangementDetail
  property_count: 9
  slug: adyen-legalarrangementdetail
- name: LegalArrangementEntityDetail
  property_count: 11
  slug: adyen-legalarrangemententitydetail
- name: LegalArrangementRequest
  property_count: 2
  slug: adyen-legalarrangementrequest
- name: LegalEntity
  property_count: 16
  slug: adyen-legalentity
- name: LegalEntityAssociation
  property_count: 7
  slug: adyen-legalentityassociation
- name: LegalEntityCapability
  property_count: 8
  slug: adyen-legalentitycapability
- name: LegalEntityInfo
  property_count: 10
  slug: adyen-legalentityinfo
- name: LegalEntityInfoRequiredType
  property_count: 10
  slug: adyen-legalentityinforequiredtype
- name: LineItem
  property_count: 17
  slug: adyen-lineitem
- name: Link
  property_count: 1
  slug: adyen-link
- name: Links
  property_count: 1
  slug: adyen-links
- name: LinksElement
  property_count: 1
  slug: adyen-linkselement
- name: ListCompanyApiCredentialsResponse
  property_count: 4
  slug: adyen-listcompanyapicredentialsresponse
- name: ListCompanyResponse
  property_count: 4
  slug: adyen-listcompanyresponse
- name: ListCompanyUsersResponse
  property_count: 4
  slug: adyen-listcompanyusersresponse
- name: ListExternalTerminalActionsResponse
  property_count: 1
  slug: adyen-listexternalterminalactionsresponse
- name: ListMerchantApiCredentialsResponse
  property_count: 4
  slug: adyen-listmerchantapicredentialsresponse
- name: ListMerchantResponse
  property_count: 4
  slug: adyen-listmerchantresponse
- name: ListMerchantUsersResponse
  property_count: 4
  slug: adyen-listmerchantusersresponse
- name: ListNetworkTokensResponse
  property_count: 1
  slug: adyen-listnetworktokensresponse
- name: ListStoredPaymentMethodsResponse
  property_count: 3
  slug: adyen-liststoredpaymentmethodsresponse
- name: ListStoresResponse
  property_count: 4
  slug: adyen-liststoresresponse
- name: ListTerminalsResponse
  property_count: 4
  slug: adyen-listterminalsresponse
- name: ListWebhooksResponse
  property_count: 5
  slug: adyen-listwebhooksresponse
- name: LocalDate
  property_count: 2
  slug: adyen-localdate
- name: Localization
  property_count: 3
  slug: adyen-localization
- name: LoginRequest
  property_count: 10
  slug: adyen-loginrequest
- name: LoginResponse
  property_count: 4
  slug: adyen-loginresponse
- name: Logo
  property_count: 1
  slug: adyen-logo
- name: LogoutRequest
  property_count: 1
  slug: adyen-logoutrequest
- name: LogoutResponse
  property_count: 1
  slug: adyen-logoutresponse
- name: LoyaltyAccount
  property_count: 2
  slug: adyen-loyaltyaccount
- name: LoyaltyAccountID
  property_count: 4
  slug: adyen-loyaltyaccountid
- name: LoyaltyAccountReq
  property_count: 2
  slug: adyen-loyaltyaccountreq
- name: LoyaltyAccountStatus
  property_count: 4
  slug: adyen-loyaltyaccountstatus
- name: LoyaltyAcquirerData
  property_count: 4
  slug: adyen-loyaltyacquirerdata
- name: LoyaltyAmount
  property_count: 3
  slug: adyen-loyaltyamount
- name: LoyaltyData
  property_count: 3
  slug: adyen-loyaltydata
- name: LoyaltyHandling
  property_count: 0
  slug: adyen-loyaltyhandling
- name: LoyaltyRequest
  property_count: 3
  slug: adyen-loyaltyrequest
- name: LoyaltyResponse
  property_count: 5
  slug: adyen-loyaltyresponse
- name: LoyaltyResult
  property_count: 5
  slug: adyen-loyaltyresult
- name: LoyaltyTotals
  property_count: 3
  slug: adyen-loyaltytotals
- name: LoyaltyTransaction
  property_count: 6
  slug: adyen-loyaltytransaction
- name: LoyaltyTransactionType
  property_count: 0
  slug: adyen-loyaltytransactiontype
- name: LoyaltyUnit
  property_count: 0
  slug: adyen-loyaltyunit
- name: Mandate
  property_count: 8
  slug: adyen-mandate
- name: Masterpass
  property_count: 4
  slug: adyen-masterpassdetails
- name: MatchingTransactionsRestriction
  property_count: 2
  slug: adyen-matchingtransactionsrestriction
- name: MBWay
  property_count: 4
  slug: adyen-mbwaydetails
- name: MccsRestriction
  property_count: 2
  slug: adyen-mccsrestriction
- name: MealVoucherFRInfo
  property_count: 3
  slug: adyen-mealvoucherfrinfo
- name: MeApiCredential
  property_count: 11
  slug: adyen-meapicredential
- name: MenuEntry
  property_count: 6
  slug: adyen-menuentry
- name: MenuEntryTag
  property_count: 0
  slug: adyen-menuentrytag
- name: Merchant
  property_count: 14
  slug: adyen-merchant
- name: MerchantAccount
  property_count: 4
  slug: adyen-merchantaccount
- name: MerchantAcquirerPair
  property_count: 2
  slug: adyen-merchantacquirerpair
- name: MerchantCreatedNotificationRequest
  property_count: 4
  slug: adyen-merchantcreatednotificationrequest
- name: MerchantData
  property_count: 4
  slug: adyen-merchantdata
- name: MerchantDetails
  property_count: 3
  slug: adyen-merchantdetails
- name: MerchantDevice
  property_count: 3
  slug: adyen-merchantdevice
- name: MerchantLinks
  property_count: 4
  slug: adyen-merchantlinks
- name: MerchantNamesRestriction
  property_count: 2
  slug: adyen-merchantnamesrestriction
- name: MerchantRiskIndicator
  property_count: 14
  slug: adyen-merchantriskindicator
- name: MerchantsRestriction
  property_count: 2
  slug: adyen-merchantsrestriction
- name: MerchantUpdatedNotificationRequest
  property_count: 4
  slug: adyen-merchantupdatednotificationrequest
- name: Message
  property_count: 2
  slug: adyen-message
- name: MessageCategory
  property_count: 0
  slug: adyen-messagecategory
- name: MessageClass
  property_count: 0
  slug: adyen-messageclass
- name: MessageHeader
  property_count: 8
  slug: adyen-messageheader
- name: MessageReference
  property_count: 5
  slug: adyen-messagereference
- name: MessageType
  property_count: 0
  slug: adyen-messagetype
- name: MidServiceNotificationData
  property_count: 9
  slug: adyen-midservicenotificationdata
- name: MigratedAccounts
  property_count: 2
  slug: adyen-migratedaccounts
- name: MigratedShareholders
  property_count: 2
  slug: adyen-migratedshareholders
- name: MigratedStores
  property_count: 4
  slug: adyen-migratedstores
- name: MigrationData
  property_count: 7
  slug: adyen-migrationdata
- name: MinorUnitsMonetaryValue
  property_count: 2
  slug: adyen-minorunitsmonetaryvalue
- name: MobileData
  property_count: 6
  slug: adyen-mobiledata
- name: MobilePay
  property_count: 2
  slug: adyen-mobilepaydetails
- name: Modification
  property_count: 5
  slug: adyen-modification
- name: ModificationResult
  property_count: 3
  slug: adyen-modificationresult
- name: ModifyRequest
  property_count: 3
  slug: adyen-modifyrequest
- name: ModifyResponse
  property_count: 3
  slug: adyen-modifyresponse
- name: MOLPay
  property_count: 3
  slug: adyen-molpaydetails
- name: Name-2
  property_count: 4
  slug: adyen-name-2
- name: Name
  property_count: 2
  slug: adyen-name
- name: Name2
  property_count: 2
  slug: adyen-name2
- name: NameLocation
  property_count: 6
  slug: adyen-namelocation
- name: NetworkToken
  property_count: 8
  slug: adyen-networktoken
- name: Nexo
  property_count: 5
  slug: adyen-nexo
- name: NOLocalAccountIdentification
  property_count: 2
  slug: adyen-nolocalaccountidentification
- name: Notification
  property_count: 5
  slug: adyen-notification
- name: NotificationAdditionalData
  property_count: 121
  slug: adyen-notificationadditionaldata
- name: NotificationConfigurationDetails
  property_count: 10
  slug: adyen-notificationconfigurationdetails
- name: NotificationErrorContainer
  property_count: 2
  slug: adyen-notificationerrorcontainer
- name: NotificationEventConfiguration
  property_count: 2
  slug: adyen-notificationeventconfiguration
- name: NotificationModificationData
  property_count: 2
  slug: adyen-notificationmodificationdata
- name: NotificationRequest
  property_count: 2
  slug: adyen-notificationrequest
- name: NotificationRequestItem
  property_count: 11
  slug: adyen-notificationrequestitem
- name: NotificationRequestItemWrapper
  property_count: 1
  slug: adyen-notificationrequestitemwrapper
- name: NotificationResponse
  property_count: 1
  slug: adyen-notificationresponse
- name: NotificationUrl
  property_count: 2
  slug: adyen-notificationurl
- name: NotifyShopperRequest
  property_count: 9
  slug: adyen-notifyshopperrequest
- name: NotifyShopperResult
  property_count: 7
  slug: adyen-notifyshopperresult
- name: NumberAndBicAccountIdentification
  property_count: 4
  slug: adyen-numberandbicaccountidentification
- name: NZLocalAccountIdentification
  property_count: 2
  slug: adyen-nzlocalaccountidentification
- name: OfflineProcessing
  property_count: 2
  slug: adyen-offlineprocessing
- name: OnboardingLink
  property_count: 1
  slug: adyen-onboardinglink
- name: OnboardingLinkInfo
  property_count: 4
  slug: adyen-onboardinglinkinfo
- name: OnboardingTheme
  property_count: 5
  slug: adyen-onboardingtheme
- name: OnboardingThemes
  property_count: 3
  slug: adyen-onboardingthemes
- name: Open Invoice
  property_count: 7
  slug: adyen-openinvoicedetails
- name: OperationStatus
  property_count: 2
  slug: adyen-operationstatus
- name: Opi
  property_count: 3
  slug: adyen-opi
- name: OrderItem
  property_count: 4
  slug: adyen-orderitem
- name: Organization
  property_count: 16
  slug: adyen-organization
- name: OriginalPOITransaction
  property_count: 9
  slug: adyen-originalpoitransaction
- name: OutgoingTransferNotificationData
  property_count: 22
  slug: adyen-outgoingtransfernotificationdata
- name: OutgoingTransferNotificationRequest
  property_count: 3
  slug: adyen-outgoingtransfernotificationrequest
- name: OutputBarcode
  property_count: 2
  slug: adyen-outputbarcode
- name: OutputContent
  property_count: 5
  slug: adyen-outputcontent
- name: OutputFormat
  property_count: 0
  slug: adyen-outputformat
- name: OutputResult
  property_count: 3
  slug: adyen-outputresult
- name: OutputText
  property_count: 11
  slug: adyen-outputtext
- name: OwnerEntity
  property_count: 2
  slug: adyen-ownerentity
- name: PaginatedAccountHoldersResponse
  property_count: 3
  slug: adyen-paginatedaccountholdersresponse
- name: PaginatedBalanceAccountsResponse
  property_count: 3
  slug: adyen-paginatedbalanceaccountsresponse
- name: PaginatedGetCardOrderItemResponse
  property_count: 3
  slug: adyen-paginatedgetcardorderitemresponse
- name: PaginatedGetCardOrderResponse
  property_count: 3
  slug: adyen-paginatedgetcardorderresponse
- name: PaginatedPaymentInstrumentsResponse
  property_count: 3
  slug: adyen-paginatedpaymentinstrumentsresponse
- name: PaginationLinks
  property_count: 5
  slug: adyen-paginationlinks
- name: PaidoutReversedNotificationRequest
  property_count: 2
  slug: adyen-paidoutreversednotificationrequest
- name: PaidoutReversedNotificationRequestItem
  property_count: 11
  slug: adyen-paidoutreversednotificationrequestitem
- name: PaidoutReversedNotificationRequestItemWrapper
  property_count: 1
  slug: adyen-paidoutreversednotificationrequestitemwrapper
- name: PartyIdentification-2
  property_count: 5
  slug: adyen-partyidentification-2
- name: PartyIdentification
  property_count: 7
  slug: adyen-partyidentification
- name: Passcodes
  property_count: 4
  slug: adyen-passcodes
- name: PayAtTable
  property_count: 3
  slug: adyen-payattable
- name: Payment
  property_count: 2
  slug: adyen-payment
- name: PaymentAccountReq
  property_count: 3
  slug: adyen-paymentaccountreq
- name: PaymentAccountStatus
  property_count: 4
  slug: adyen-paymentaccountstatus
- name: PaymentAcquirerData
  property_count: 6
  slug: adyen-paymentacquirerdata
- name: PaymentAmountUpdateRequest
  property_count: 7
  slug: adyen-paymentamountupdaterequest
- name: PaymentAmountUpdateResponse
  property_count: 9
  slug: adyen-paymentamountupdateresponse
- name: PaymentCancelRequest
  property_count: 3
  slug: adyen-paymentcancelrequest
- name: PaymentCancelResponse
  property_count: 5
  slug: adyen-paymentcancelresponse
- name: PaymentCaptureRequest
  property_count: 8
  slug: adyen-paymentcapturerequest
- name: PaymentCaptureResponse
  property_count: 10
  slug: adyen-paymentcaptureresponse
- name: PaymentCompletionDetails
  property_count: 18
  slug: adyen-paymentcompletiondetails
- name: PaymentData
  property_count: 7
  slug: adyen-paymentdata
- name: Payment Details
  property_count: 2
  slug: adyen-paymentdetails
- name: PaymentDetailsRequest
  property_count: 4
  slug: adyen-paymentdetailsrequest
- name: PaymentDetailsResponse
  property_count: 15
  slug: adyen-paymentdetailsresponse
- name: PaymentFailureNotification
  property_count: 7
  slug: adyen-paymentfailurenotification
- name: PaymentFailureNotificationContent
  property_count: 6
  slug: adyen-paymentfailurenotificationcontent
- name: PaymentInstrument
  property_count: 4
  slug: adyen-paymentinstrument
- name: PaymentInstrumentData
  property_count: 6
  slug: adyen-paymentinstrumentdata
- name: PaymentInstrumentGroup
  property_count: 6
  slug: adyen-paymentinstrumentgroup
- name: PaymentInstrumentGroupInfo
  property_count: 5
  slug: adyen-paymentinstrumentgroupinfo
- name: PaymentInstrumentInfo
  property_count: 10
  slug: adyen-paymentinstrumentinfo
- name: PaymentInstrumentNotificationData
  property_count: 2
  slug: adyen-paymentinstrumentnotificationdata
- name: PaymentInstrumentReference
  property_count: 1
  slug: adyen-paymentinstrumentreference
- name: PaymentInstrumentRequirement
  property_count: 5
  slug: adyen-paymentinstrumentrequirement
- name: PaymentInstrumentRevealInfo
  property_count: 3
  slug: adyen-paymentinstrumentrevealinfo
- name: PaymentInstrumentType
  property_count: 0
  slug: adyen-paymentinstrumenttype
- name: PaymentInstrumentUpdateRequest
  property_count: 5
  slug: adyen-paymentinstrumentupdaterequest
- name: PaymentLinkRequest
  property_count: 38
  slug: adyen-paymentlinkrequest
- name: PaymentLinkResponse
  property_count: 42
  slug: adyen-paymentlinkresponse
- name: PaymentMethod
  property_count: 9
  slug: adyen-paymentmethod
- name: PaymentMethodCreatedNotificationRequest
  property_count: 4
  slug: adyen-paymentmethodcreatednotificationrequest
- name: PaymentMethodGroup
  property_count: 3
  slug: adyen-paymentmethodgroup
- name: PaymentMethodIssuer
  property_count: 3
  slug: adyen-paymentmethodissuer
- name: PaymentMethodNotificationResponse
  property_count: 1
  slug: adyen-paymentmethodnotificationresponse
- name: PaymentMethodRequestRemovedNotificationRequest
  property_count: 4
  slug: adyen-paymentmethodrequestremovednotificationrequest
- name: PaymentMethodResponse
  property_count: 5
  slug: adyen-paymentmethodresponse
- name: PaymentMethodScheduledForRemovalNotificationRequest
  property_count: 4
  slug: adyen-paymentmethodscheduledforremovalnotificationrequest
- name: PaymentMethodSetupInfo
  property_count: 33
  slug: adyen-paymentmethodsetupinfo
- name: PaymentMethodsRequest
  property_count: 12
  slug: adyen-paymentmethodsrequest
- name: PaymentMethodsResponse
  property_count: 2
  slug: adyen-paymentmethodsresponse
- name: PaymentNotificationData
  property_count: 20
  slug: adyen-paymentnotificationdata
- name: PaymentNotificationRequest-2
  property_count: 3
  slug: adyen-paymentnotificationrequest-2
- name: PaymentNotificationRequest
  property_count: 3
  slug: adyen-paymentnotificationrequest
- name: PaymentReceipt
  property_count: 4
  slug: adyen-paymentreceipt
- name: PaymentRefundRequest
  property_count: 8
  slug: adyen-paymentrefundrequest
- name: PaymentRefundResponse
  property_count: 10
  slug: adyen-paymentrefundresponse
- name: PaymentRequest
  property_count: 67
  slug: adyen-paymentrequest
- name: PaymentRequest3d
  property_count: 45
  slug: adyen-paymentrequest3d
- name: PaymentRequest3ds2
  property_count: 45
  slug: adyen-paymentrequest3ds2
- name: PaymentResponse
  property_count: 15
  slug: adyen-paymentresponse
- name: PaymentResult
  property_count: 11
  slug: adyen-paymentresult
- name: PaymentReversalRequest
  property_count: 3
  slug: adyen-paymentreversalrequest
- name: PaymentReversalResponse
  property_count: 5
  slug: adyen-paymentreversalresponse
- name: PaymentSetupRequest
  property_count: 56
  slug: adyen-paymentsetuprequest
- name: PaymentSetupResponse
  property_count: 2
  slug: adyen-paymentsetupresponse
- name: PaymentToken
  property_count: 3
  slug: adyen-paymenttoken
- name: PaymentTotals
  property_count: 3
  slug: adyen-paymenttotals
- name: PaymentTransaction
  property_count: 4
  slug: adyen-paymenttransaction
- name: PaymentType
  property_count: 0
  slug: adyen-paymenttype
- name: PaymentVerificationRequest
  property_count: 1
  slug: adyen-paymentverificationrequest
- name: PaymentVerificationResponse
  property_count: 10
  slug: adyen-paymentverificationresponse
- name: PayoutAccountHolderRequest
  property_count: 8
  slug: adyen-payoutaccountholderrequest
- name: PayoutAccountHolderResponse
  property_count: 6
  slug: adyen-payoutaccountholderresponse
- name: PayoutMethod
  property_count: 5
  slug: adyen-payoutmethod
- name: PayoutRequest
  property_count: 14
  slug: adyen-payoutrequest
- name: PayoutResponse
  property_count: 11
  slug: adyen-payoutresponse
- name: PayoutScheduleResponse
  property_count: 2
  slug: adyen-payoutscheduleresponse
- name: PayoutSettings
  property_count: 7
  slug: adyen-payoutsettings
- name: PayoutSettingsRequest
  property_count: 3
  slug: adyen-payoutsettingsrequest
- name: PayoutSettingsResponse
  property_count: 1
  slug: adyen-payoutsettingsresponse
- name: PayPal
  property_count: 9
  slug: adyen-paypaldetails
- name: PayPalInfo
  property_count: 3
  slug: adyen-paypalinfo
- name: PayU
  property_count: 6
  slug: adyen-payuupidetails
- name: Google Pay
  property_count: 6
  slug: adyen-paywithgoogledetails
- name: Google Pay
  property_count: 6
  slug: adyen-paywithgoogledonations
- name: PciDocumentInfo
  property_count: 3
  slug: adyen-pcidocumentinfo
- name: PciSigningRequest
  property_count: 2
  slug: adyen-pcisigningrequest
- name: PciSigningResponse
  property_count: 2
  slug: adyen-pcisigningresponse
- name: PerformedTransaction
  property_count: 6
  slug: adyen-performedtransaction
- name: PerformVerificationRequest
  property_count: 3
  slug: adyen-performverificationrequest
- name: PeriodUnit
  property_count: 0
  slug: adyen-periodunit
- name: Permit
  property_count: 5
  slug: adyen-permit
- name: PermitRestriction
  property_count: 3
  slug: adyen-permitrestriction
- name: PermitResult
  property_count: 2
  slug: adyen-permitresult
- name: PersonalData
  property_count: 3
  slug: adyen-personaldata
- name: PersonalDocumentData
  property_count: 5
  slug: adyen-personaldocumentdata
- name: Phone
  property_count: 2
  slug: adyen-phone
- name: PhoneNumber
  property_count: 3
  slug: adyen-phonenumber
- name: PinChangeRequest
  property_count: 4
  slug: adyen-pinchangerequest
- name: PinChangeResponse
  property_count: 1
  slug: adyen-pinchangeresponse
- name: PINFormat
  property_count: 0
  slug: adyen-pinformat
- name: PINRequestType
  property_count: 0
  slug: adyen-pinrequesttype
- name: PlatformChargebackLogic
  property_count: 3
  slug: adyen-platformchargebacklogic
- name: PlatformPayment
  property_count: 8
  slug: adyen-platformpayment
- name: PlatformPaymentConfiguration
  property_count: 2
  slug: adyen-platformpaymentconfiguration
- name: PLLocalAccountIdentification
  property_count: 2
  slug: adyen-pllocalaccountidentification
- name: POICapabilities
  property_count: 0
  slug: adyen-poicapabilities
- name: POIData
  property_count: 2
  slug: adyen-poidata
- name: Point
  property_count: 2
  slug: adyen-point
- name: POIProfile
  property_count: 2
  slug: adyen-poiprofile
- name: POISoftware
  property_count: 4
  slug: adyen-poisoftware
- name: POIStatus
  property_count: 8
  slug: adyen-poistatus
- name: POISystemData
  property_count: 4
  slug: adyen-poisystemdata
- name: POITerminalData
  property_count: 4
  slug: adyen-poiterminaldata
- name: PredefinedContent
  property_count: 2
  slug: adyen-predefinedcontent
- name: PrinterStatus
  property_count: 0
  slug: adyen-printerstatus
- name: PrintOutput
  property_count: 5
  slug: adyen-printoutput
- name: PrintRequest
  property_count: 1
  slug: adyen-printrequest
- name: PrintResponse
  property_count: 2
  slug: adyen-printresponse
- name: ProcessingTypesRestriction
  property_count: 2
  slug: adyen-processingtypesrestriction
- name: Profile
  property_count: 18
  slug: adyen-profile
- name: PublicKeyResponse
  property_count: 2
  slug: adyen-publickeyresponse
- name: PurchaseInfo
  property_count: 3
  slug: adyen-purchaseinfo
- name: Ratepay
  property_count: 7
  slug: adyen-ratepaydetails
- name: Rebates
  property_count: 3
  slug: adyen-rebates
- name: ReceiptOptions
  property_count: 3
  slug: adyen-receiptoptions
- name: ReceiptPrinting
  property_count: 16
  slug: adyen-receiptprinting
- name: ReconciliationRequest
  property_count: 3
  slug: adyen-reconciliationrequest
- name: ReconciliationResponse
  property_count: 4
  slug: adyen-reconciliationresponse
- name: ReconciliationType
  property_count: 0
  slug: adyen-reconciliationtype
- name: Recurring
  property_count: 5
  slug: adyen-recurring
- name: RecurringContractNotificationAdditionalData
  property_count: 122
  slug: adyen-recurringcontractnotificationadditionaldata
- name: RecurringContractNotificationRequest
  property_count: 2
  slug: adyen-recurringcontractnotificationrequest
- name: RecurringContractNotificationRequestItem
  property_count: 12
  slug: adyen-recurringcontractnotificationrequestitem
- name: RecurringContractNotificationRequestItemWrapper
  property_count: 1
  slug: adyen-recurringcontractnotificationrequestitemwrapper
- name: RecurringDetail
  property_count: 11
  slug: adyen-recurringdetail
- name: RecurringDetailsRequest
  property_count: 3
  slug: adyen-recurringdetailsrequest
- name: RecurringDetailsResult
  property_count: 4
  slug: adyen-recurringdetailsresult
- name: RecurringDetailWrapper
  property_count: 1
  slug: adyen-recurringdetailwrapper
- name: Referenced
  property_count: 1
  slug: adyen-referenced
- name: RefundFundsTransferNotification
  property_count: 7
  slug: adyen-refundfundstransfernotification
- name: RefundFundsTransferNotificationContent
  property_count: 5
  slug: adyen-refundfundstransfernotificationcontent
- name: RefundFundsTransferRequest
  property_count: 3
  slug: adyen-refundfundstransferrequest
- name: RefundFundsTransferResponse
  property_count: 6
  slug: adyen-refundfundstransferresponse
- name: RefundNotPaidOutTransfersRequest
  property_count: 2
  slug: adyen-refundnotpaidouttransfersrequest
- name: RefundNotPaidOutTransfersResponse
  property_count: 3
  slug: adyen-refundnotpaidouttransfersresponse
- name: RefundRequest
  property_count: 11
  slug: adyen-refundrequest
- name: RefundResult
  property_count: 3
  slug: adyen-refundresult
- name: Refunds
  property_count: 1
  slug: adyen-refunds
- name: RelayedAuthorisationData-2
  property_count: 2
  slug: adyen-relayedauthorisationdata-2
- name: RelayedAuthorisationData
  property_count: 3
  slug: adyen-relayedauthorisationdata
- name: ReleaseUpdateDetails
  property_count: 2
  slug: adyen-releaseupdatedetails
- name: RemediatingAction
  property_count: 2
  slug: adyen-remediatingaction
- name: Repayment
  property_count: 3
  slug: adyen-repayment
- name: RepaymentTerm
  property_count: 2
  slug: adyen-repaymentterm
- name: RepeatedMessageResponse
  property_count: 2
  slug: adyen-repeatedmessageresponse
- name: RepeatedResponseMessageBody
  property_count: 6
  slug: adyen-repeatedresponsemessagebody
- name: ReportAvailableNotification
  property_count: 7
  slug: adyen-reportavailablenotification
- name: ReportAvailableNotificationContent
  property_count: 5
  slug: adyen-reportavailablenotificationcontent
- name: ReportAvailableNotificationRequest
  property_count: 2
  slug: adyen-reportavailablenotificationrequest
- name: ReportAvailableNotificationRequestItem
  property_count: 11
  slug: adyen-reportavailablenotificationrequestitem
- name: ReportAvailableNotificationRequestItemWrapper
  property_count: 1
  slug: adyen-reportavailablenotificationrequestitemwrapper
- name: ReportNotificationData
  property_count: 7
  slug: adyen-reportnotificationdata
- name: ReportNotificationRequest
  property_count: 3
  slug: adyen-reportnotificationrequest
- name: RequestActivationResponse
  property_count: 2
  slug: adyen-requestactivationresponse
- name: Resource
  property_count: 3
  slug: adyen-resource
- name: ResourceReference
  property_count: 3
  slug: adyen-resourcereference
- name: Response
  property_count: 3
  slug: adyen-response
- name: ResponseAdditionalData3DSecure
  property_count: 5
  slug: adyen-responseadditionaldata3dsecure
- name: ResponseAdditionalDataBillingAddress
  property_count: 6
  slug: adyen-responseadditionaldatabillingaddress
- name: ResponseAdditionalDataCard
  property_count: 8
  slug: adyen-responseadditionaldatacard
- name: ResponseAdditionalDataCommon
  property_count: 59
  slug: adyen-responseadditionaldatacommon
- name: ResponseAdditionalDataDomesticError
  property_count: 2
  slug: adyen-responseadditionaldatadomesticerror
- name: ResponseAdditionalDataInstallments
  property_count: 12
  slug: adyen-responseadditionaldatainstallments
- name: ResponseAdditionalDataNetworkTokens
  property_count: 3
  slug: adyen-responseadditionaldatanetworktokens
- name: ResponseAdditionalDataOpi
  property_count: 1
  slug: adyen-responseadditionaldataopi
- name: ResponseAdditionalDataSepa
  property_count: 3
  slug: adyen-responseadditionaldatasepa
- name: ResponseMode
  property_count: 0
  slug: adyen-responsemode
- name: paymentResponse
  property_count: 2
  slug: adyen-responsepaymentmethod
- name: RestServiceError
  property_count: 9
  slug: adyen-restserviceerror
- name: Result
  property_count: 0
  slug: adyen-result
- name: ReturnTransferRequest
  property_count: 2
  slug: adyen-returntransferrequest
- name: ReturnTransferResponse
  property_count: 4
  slug: adyen-returntransferresponse
- name: RevealPinRequest
  property_count: 2
  slug: adyen-revealpinrequest
- name: RevealPinResponse
  property_count: 2
  slug: adyen-revealpinresponse
- name: ReversalReason
  property_count: 0
  slug: adyen-reversalreason
- name: ReversalRequest
  property_count: 5
  slug: adyen-reversalrequest
- name: ReversalResponse
  property_count: 6
  slug: adyen-reversalresponse
- name: RiskData
  property_count: 4
  slug: adyen-riskdata
- name: SaleCapabilities
  property_count: 0
  slug: adyen-salecapabilities
- name: SaleData
  property_count: 12
  slug: adyen-saledata
- name: SaleItem
  property_count: 11
  slug: adyen-saleitem
- name: SaleItemRebate
  property_count: 7
  slug: adyen-saleitemrebate
- name: SaleSoftware
  property_count: 4
  slug: adyen-salesoftware
- name: SaleTerminalData
  property_count: 1
  slug: adyen-saleterminaldata
- name: SaleToIssuerData
  property_count: 1
  slug: adyen-saletoissuerdata
- name: SameAmountRestriction
  property_count: 2
  slug: adyen-sameamountrestriction
- name: SameCounterpartyRestriction
  property_count: 2
  slug: adyen-samecounterpartyrestriction
- name: Samsung Pay
  property_count: 6
  slug: adyen-samsungpaydetails
- name: ScheduleAccountUpdaterRequest
  property_count: 6
  slug: adyen-scheduleaccountupdaterrequest
- name: ScheduleAccountUpdaterResult
  property_count: 2
  slug: adyen-scheduleaccountupdaterresult
- name: ScheduledRefundsNotification
  property_count: 7
  slug: adyen-scheduledrefundsnotification
- name: ScheduledRefundsNotificationContent
  property_count: 5
  slug: adyen-scheduledrefundsnotificationcontent
- name: ScheduleTerminalActionsRequest
  property_count: 4
  slug: adyen-scheduleterminalactionsrequest
- name: ScheduleTerminalActionsResponse
  property_count: 7
  slug: adyen-scheduleterminalactionsresponse
- name: SDKEphemPubKey
  property_count: 4
  slug: adyen-sdkephempubkey
- name: SecurityTrailer
  property_count: 5
  slug: adyen-securitytrailer
- name: SELocalAccountIdentification
  property_count: 3
  slug: adyen-selocalaccountidentification
- name: SensitiveCardData
  property_count: 4
  slug: adyen-sensitivecarddata
- name: SensitiveMobileData
  property_count: 3
  slug: adyen-sensitivemobiledata
- name: SEPA Direct Debit
  property_count: 6
  slug: adyen-sepadirectdebitdetails
- name: ServiceError
  property_count: 5
  slug: adyen-serviceerror
- name: ServiceErrorDetails
  property_count: 4
  slug: adyen-serviceerrordetails
- name: ServiceProfiles
  property_count: 0
  slug: adyen-serviceprofiles
- name: ServicesEnabled
  property_count: 0
  slug: adyen-servicesenabled
- name: SessionResultResponse
  property_count: 2
  slug: adyen-sessionresultresponse
- name: Settings
  property_count: 3
  slug: adyen-settings
- name: SetupBeneficiaryRequest
  property_count: 3
  slug: adyen-setupbeneficiaryrequest
- name: SetupBeneficiaryResponse
  property_count: 3
  slug: adyen-setupbeneficiaryresponse
- name: SGLocalAccountIdentification
  property_count: 3
  slug: adyen-sglocalaccountidentification
- name: ShareholderContact
  property_count: 11
  slug: adyen-shareholdercontact
- name: ShippingLocation
  property_count: 4
  slug: adyen-shippinglocation
- name: ShippingLocationsResponse
  property_count: 1
  slug: adyen-shippinglocationsresponse
- name: ShopperInput
  property_count: 3
  slug: adyen-shopperinput
- name: ShopperInteractionDevice
  property_count: 3
  slug: adyen-shopperinteractiondevice
- name: ShowPages
  property_count: 9
  slug: adyen-showpages
- name: SignatoryContact
  property_count: 10
  slug: adyen-signatorycontact
- name: Signature
  property_count: 4
  slug: adyen-signature
- name: SofortInfo
  property_count: 2
  slug: adyen-sofortinfo
- name: SoleProprietorship
  property_count: 11
  slug: adyen-soleproprietorship
- name: SoundAction
  property_count: 0
  slug: adyen-soundaction
- name: SoundContent
  property_count: 4
  slug: adyen-soundcontent
- name: SoundFormat
  property_count: 0
  slug: adyen-soundformat
- name: SourceOfFunds
  property_count: 4
  slug: adyen-sourceoffunds
- name: Split
  property_count: 5
  slug: adyen-split
- name: SplitAmount
  property_count: 2
  slug: adyen-splitamount
- name: SplitConfiguration
  property_count: 4
  slug: adyen-splitconfiguration
- name: SplitConfigurationList
  property_count: 1
  slug: adyen-splitconfigurationlist
- name: SplitConfigurationLogic
  property_count: 15
  slug: adyen-splitconfigurationlogic
- name: SplitConfigurationRule
  property_count: 6
  slug: adyen-splitconfigurationrule
- name: Standalone
  property_count: 2
  slug: adyen-standalone
- name: StandalonePaymentCancelRequest
  property_count: 4
  slug: adyen-standalonepaymentcancelrequest
- name: StandalonePaymentCancelResponse
  property_count: 5
  slug: adyen-standalonepaymentcancelresponse
- name: StockData
  property_count: 3
  slug: adyen-stockdata
- name: Store
  property_count: 12
  slug: adyen-store
- name: StoreCreationRequest
  property_count: 8
  slug: adyen-storecreationrequest
- name: StoreCreationWithMerchantCodeRequest
  property_count: 9
  slug: adyen-storecreationwithmerchantcoderequest
- name: StoredDetails
  property_count: 3
  slug: adyen-storeddetails
- name: StoreDetail
  property_count: 15
  slug: adyen-storedetail
- name: StoreDetailAndSubmitRequest
  property_count: 19
  slug: adyen-storedetailandsubmitrequest
- name: StoreDetailAndSubmitResponse
  property_count: 4
  slug: adyen-storedetailandsubmitresponse
- name: StoreDetailRequest
  property_count: 16
  slug: adyen-storedetailrequest
- name: StoreDetailResponse
  property_count: 4
  slug: adyen-storedetailresponse
- name: StoredPaymentMethod
  property_count: 17
  slug: adyen-storedpaymentmethod
- name: Stored Payment Method
  property_count: 4
  slug: adyen-storedpaymentmethoddetails
- name: StoredPaymentMethodResource
  property_count: 17
  slug: adyen-storedpaymentmethodresource
- name: StoredValueAccountID
  property_count: 7
  slug: adyen-storedvalueaccountid
- name: StoredValueAccountStatus
  property_count: 2
  slug: adyen-storedvalueaccountstatus
- name: StoredValueAccountType
  property_count: 0
  slug: adyen-storedvalueaccounttype
- name: StoredValueBalanceCheckRequest
  property_count: 8
  slug: adyen-storedvaluebalancecheckrequest
- name: StoredValueBalanceCheckResponse
  property_count: 5
  slug: adyen-storedvaluebalancecheckresponse
- name: StoredValueBalanceMergeRequest
  property_count: 9
  slug: adyen-storedvaluebalancemergerequest
- name: StoredValueBalanceMergeResponse
  property_count: 6
  slug: adyen-storedvaluebalancemergeresponse
- name: StoredValueData
  property_count: 8
  slug: adyen-storedvaluedata
- name: StoredValueIssueRequest
  property_count: 8
  slug: adyen-storedvalueissuerequest
- name: StoredValueIssueResponse
  property_count: 7
  slug: adyen-storedvalueissueresponse
- name: StoredValueLoadRequest
  property_count: 9
  slug: adyen-storedvalueloadrequest
- name: StoredValueLoadResponse
  property_count: 6
  slug: adyen-storedvalueloadresponse
- name: StoredValueRequest
  property_count: 3
  slug: adyen-storedvaluerequest
- name: StoredValueResponse
  property_count: 5
  slug: adyen-storedvalueresponse
- name: StoredValueResult
  property_count: 7
  slug: adyen-storedvalueresult
- name: StoredValueStatusChangeRequest
  property_count: 9
  slug: adyen-storedvaluestatuschangerequest
- name: StoredValueStatusChangeResponse
  property_count: 6
  slug: adyen-storedvaluestatuschangeresponse
- name: StoredValueTransactionType
  property_count: 0
  slug: adyen-storedvaluetransactiontype
- name: StoredValueVoidRequest
  property_count: 6
  slug: adyen-storedvaluevoidrequest
- name: StoredValueVoidResponse
  property_count: 5
  slug: adyen-storedvaluevoidresponse
- name: StoreLocation
  property_count: 7
  slug: adyen-storelocation
- name: StoreSplitConfiguration
  property_count: 2
  slug: adyen-storesplitconfiguration
- name: StringMatch
  property_count: 2
  slug: adyen-stringmatch
- name: SubInputDetail
  property_count: 6
  slug: adyen-subinputdetail
- name: SubjectErasureByPspReferenceRequest
  property_count: 3
  slug: adyen-subjecterasurebypspreferencerequest
- name: SubjectErasureResponse
  property_count: 1
  slug: adyen-subjecterasureresponse
- name: SubMerchant
  property_count: 5
  slug: adyen-submerchant
- name: SubMerchantInfo
  property_count: 5
  slug: adyen-submerchantinfo
- name: SubmitRequest
  property_count: 15
  slug: adyen-submitrequest
- name: SubmitResponse
  property_count: 4
  slug: adyen-submitresponse
- name: SupplyDefenseDocumentRequest
  property_count: 3
  slug: adyen-supplydefensedocumentrequest
- name: SupplyDefenseDocumentResponse
  property_count: 1
  slug: adyen-supplydefensedocumentresponse
- name: SupportingEntityCapability
  property_count: 4
  slug: adyen-supportingentitycapability
- name: Surcharge
  property_count: 2
  slug: adyen-surcharge
- name: SuspendAccountHolderRequest
  property_count: 1
  slug: adyen-suspendaccountholderrequest
- name: SuspendAccountHolderResponse
  property_count: 4
  slug: adyen-suspendaccountholderresponse
- name: SweepConfiguration
  property_count: 10
  slug: adyen-sweepconfiguration
- name: SweepConfigurationNotificationData
  property_count: 3
  slug: adyen-sweepconfigurationnotificationdata
- name: SweepConfigurationNotificationRequest
  property_count: 3
  slug: adyen-sweepconfigurationnotificationrequest
- name: SweepConfigurationV2
  property_count: 13
  slug: adyen-sweepconfigurationv2
- name: SweepCounterparty
  property_count: 3
  slug: adyen-sweepcounterparty
- name: SweepSchedule
  property_count: 2
  slug: adyen-sweepschedule
- name: SwishInfo
  property_count: 1
  slug: adyen-swishinfo
- name: TapToPay
  property_count: 1
  slug: adyen-taptopay
- name: TaxInformation
  property_count: 3
  slug: adyen-taxinformation
- name: TaxReportingClassification
  property_count: 4
  slug: adyen-taxreportingclassification
- name: TechnicalCancelRequest
  property_count: 10
  slug: adyen-technicalcancelrequest
- name: Terminal
  property_count: 8
  slug: adyen-terminal
- name: TerminalActionScheduleDetail
  property_count: 2
  slug: adyen-terminalactionscheduledetail
- name: TerminalAssignment
  property_count: 5
  slug: adyen-terminalassignment
- name: TerminalConnectivity
  property_count: 4
  slug: adyen-terminalconnectivity
- name: TerminalConnectivityBluetooth
  property_count: 2
  slug: adyen-terminalconnectivitybluetooth
- name: TerminalConnectivityCellular
  property_count: 2
  slug: adyen-terminalconnectivitycellular
- name: TerminalConnectivityEthernet
  property_count: 3
  slug: adyen-terminalconnectivityethernet
- name: TerminalConnectivityWifi
  property_count: 3
  slug: adyen-terminalconnectivitywifi
- name: TerminalEnvironment
  property_count: 0
  slug: adyen-terminalenvironment
- name: TerminalModelsResponse
  property_count: 1
  slug: adyen-terminalmodelsresponse
- name: TerminalOrder
  property_count: 8
  slug: adyen-terminalorder
- name: TerminalOrderRequest
  property_count: 6
  slug: adyen-terminalorderrequest
- name: TerminalOrdersResponse
  property_count: 1
  slug: adyen-terminalordersresponse
- name: TerminalProduct
  property_count: 5
  slug: adyen-terminalproduct
- name: TerminalProductPrice
  property_count: 2
  slug: adyen-terminalproductprice
- name: TerminalProductsResponse
  property_count: 1
  slug: adyen-terminalproductsresponse
- name: TerminalReassignmentRequest
  property_count: 4
  slug: adyen-terminalreassignmentrequest
- name: TerminalReassignmentTarget
  property_count: 4
  slug: adyen-terminalreassignmenttarget
- name: TerminalSettings
  property_count: 20
  slug: adyen-terminalsettings
- name: TermsOfServiceAcceptanceInfo
  property_count: 5
  slug: adyen-termsofserviceacceptanceinfo
- name: TestCardRange
  property_count: 10
  slug: adyen-testcardrange
- name: TestCardRangeCreationResult
  property_count: 4
  slug: adyen-testcardrangecreationresult
- name: TestCompanyWebhookRequest
  property_count: 3
  slug: adyen-testcompanywebhookrequest
- name: TestNotificationConfigurationRequest
  property_count: 2
  slug: adyen-testnotificationconfigurationrequest
- name: TestNotificationConfigurationResponse
  property_count: 8
  slug: adyen-testnotificationconfigurationresponse
- name: TestOutput
  property_count: 6
  slug: adyen-testoutput
- name: TestWebhookRequest
  property_count: 2
  slug: adyen-testwebhookrequest
- name: TestWebhookResponse
  property_count: 1
  slug: adyen-testwebhookresponse
- name: ThreeDS1Result
  property_count: 6
  slug: adyen-threeds1result
- name: ThreeDS2CardRangeDetail
  property_count: 6
  slug: adyen-threeds2cardrangedetail
- name: ThreeDS2RequestData
  property_count: 40
  slug: adyen-threeds2requestdata
- name: ThreeDS2RequestFields
  property_count: 37
  slug: adyen-threeds2requestfields
- name: ThreeDS2ResponseData
  property_count: 19
  slug: adyen-threeds2responsedata
- name: ThreeDS2Result
  property_count: 14
  slug: adyen-threeds2result
- name: ThreeDS2ResultRequest
  property_count: 2
  slug: adyen-threeds2resultrequest
- name: ThreeDS2ResultResponse
  property_count: 1
  slug: adyen-threeds2resultresponse
- name: ThreeDSAvailabilityRequest
  property_count: 6
  slug: adyen-threedsavailabilityrequest
- name: ThreeDSAvailabilityResponse
  property_count: 5
  slug: adyen-threedsavailabilityresponse
- name: ThreeDSecureData
  property_count: 12
  slug: adyen-threedsecuredata
- name: ThreeDSRequestData
  property_count: 4
  slug: adyen-threedsrequestdata
- name: ThreeDSRequestorAuthenticationInfo
  property_count: 3
  slug: adyen-threedsrequestorauthenticationinfo
- name: ThreeDSRequestorPriorAuthenticationInfo
  property_count: 4
  slug: adyen-threedsrequestorpriorauthenticationinfo
- name: ThresholdRepayment
  property_count: 1
  slug: adyen-thresholdrepayment
- name: TimeOfDay
  property_count: 2
  slug: adyen-timeofday
- name: TimeOfDayRestriction
  property_count: 2
  slug: adyen-timeofdayrestriction
- name: Timeouts
  property_count: 1
  slug: adyen-timeouts
- name: TokenDetails
  property_count: 2
  slug: adyen-tokendetails
- name: TokenRequestedType
  property_count: 0
  slug: adyen-tokenrequestedtype
- name: TotalAmountRestriction
  property_count: 2
  slug: adyen-totalamountrestriction
- name: TotalDetails
  property_count: 0
  slug: adyen-totaldetails
- name: TotalFilter
  property_count: 5
  slug: adyen-totalfilter
- name: TrackData
  property_count: 3
  slug: adyen-trackdata
- name: TrackFormat
  property_count: 0
  slug: adyen-trackformat
- name: Transaction
  property_count: 16
  slug: adyen-transaction
- name: TransactionAction
  property_count: 0
  slug: adyen-transactionaction
- name: TransactionConditions
  property_count: 9
  slug: adyen-transactionconditions
- name: TransactionDescriptionInfo
  property_count: 2
  slug: adyen-transactiondescriptioninfo
- name: TransactionEventViolation
  property_count: 3
  slug: adyen-transactioneventviolation
- name: TransactionIDType
  property_count: 2
  slug: adyen-transactionidtype
- name: TransactionListForAccount
  property_count: 2
  slug: adyen-transactionlistforaccount
- name: TransactionNotificationData
  property_count: 24
  slug: adyen-transactionnotificationdata
- name: TransactionNotificationRequestV4
  property_count: 3
  slug: adyen-transactionnotificationrequestv4
- name: TransactionRule
  property_count: 14
  slug: adyen-transactionrule
- name: TransactionRuleEntityKey
  property_count: 2
  slug: adyen-transactionruleentitykey
- name: TransactionRuleInfo
  property_count: 13
  slug: adyen-transactionruleinfo
- name: TransactionRuleInterval
  property_count: 6
  slug: adyen-transactionruleinterval
- name: TransactionRuleReference
  property_count: 3
  slug: adyen-transactionrulereference
- name: TransactionRuleResponse
  property_count: 1
  slug: adyen-transactionruleresponse
- name: TransactionRuleRestrictions
  property_count: 17
  slug: adyen-transactionrulerestrictions
- name: TransactionRuleSource
  property_count: 2
  slug: adyen-transactionrulesource
- name: TransactionRulesResponse
  property_count: 1
  slug: adyen-transactionrulesresponse
- name: TransactionRulesResult
  property_count: 4
  slug: adyen-transactionrulesresult
- name: TransactionSearchResponse
  property_count: 2
  slug: adyen-transactionsearchresponse
- name: TransactionStatusRequest
  property_count: 3
  slug: adyen-transactionstatusrequest
- name: TransactionStatusResponse
  property_count: 3
  slug: adyen-transactionstatusresponse
- name: TransactionTotals
  property_count: 14
  slug: adyen-transactiontotals
- name: TransactionType
  property_count: 0
  slug: adyen-transactiontype
- name: Transfer
  property_count: 15
  slug: adyen-transfer
- name: TransferData
  property_count: 2
  slug: adyen-transferdata
- name: TransferEvent
  property_count: 11
  slug: adyen-transferevent
- name: TransferFundsNotification
  property_count: 7
  slug: adyen-transferfundsnotification
- name: TransferFundsNotificationContent
  property_count: 7
  slug: adyen-transferfundsnotificationcontent
- name: TransferFundsRequest
  property_count: 5
  slug: adyen-transferfundsrequest
- name: TransferFundsResponse
  property_count: 4
  slug: adyen-transferfundsresponse
- name: TransferInfo
  property_count: 10
  slug: adyen-transferinfo
- name: TransferInstrument
  property_count: 7
  slug: adyen-transferinstrument
- name: TransferInstrumentInfo
  property_count: 3
  slug: adyen-transferinstrumentinfo
- name: TransferInstrumentReference
  property_count: 4
  slug: adyen-transferinstrumentreference
- name: TransferNotificationCounterParty
  property_count: 4
  slug: adyen-transfernotificationcounterparty
- name: TransferNotificationData
  property_count: 31
  slug: adyen-transfernotificationdata
- name: TransferNotificationMerchantData
  property_count: 7
  slug: adyen-transfernotificationmerchantdata
- name: TransferNotificationRequest
  property_count: 3
  slug: adyen-transfernotificationrequest
- name: TransferNotificationTransferTracking
  property_count: 1
  slug: adyen-transfernotificationtransfertracking
- name: TransferNotificationValidationFact
  property_count: 2
  slug: adyen-transfernotificationvalidationfact
- name: TransferRoute
  property_count: 5
  slug: adyen-transferroute
- name: TransferRouteRequest
  property_count: 7
  slug: adyen-transferrouterequest
- name: TransferRouteResponse
  property_count: 1
  slug: adyen-transferrouteresponse
- name: Trust
  property_count: 13
  slug: adyen-trust
- name: TwintInfo
  property_count: 1
  slug: adyen-twintinfo
- name: TypeCode
  property_count: 0
  slug: adyen-typecode
- name: UKLocalAccountIdentification
  property_count: 3
  slug: adyen-uklocalaccountidentification
- name: UltimateParentCompany
  property_count: 3
  slug: adyen-ultimateparentcompany
- name: UltimateParentCompanyBusinessDetails
  property_count: 5
  slug: adyen-ultimateparentcompanybusinessdetails
- name: UltimatePartyIdentification
  property_count: 7
  slug: adyen-ultimatepartyidentification
- name: UndefinedBeneficiary
  property_count: 2
  slug: adyen-undefinedbeneficiary
- name: UnincorporatedPartnership
  property_count: 12
  slug: adyen-unincorporatedpartnership
- name: UninstallAndroidAppDetails
  property_count: 2
  slug: adyen-uninstallandroidappdetails
- name: UninstallAndroidCertificateDetails
  property_count: 2
  slug: adyen-uninstallandroidcertificatedetails
- name: UnitOfMeasure
  property_count: 0
  slug: adyen-unitofmeasure
- name: UnSuspendAccountHolderRequest
  property_count: 1
  slug: adyen-unsuspendaccountholderrequest
- name: UnSuspendAccountHolderResponse
  property_count: 4
  slug: adyen-unsuspendaccountholderresponse
- name: UpdatableAddress
  property_count: 6
  slug: adyen-updatableaddress
- name: UpdateAccountHolderRequest
  property_count: 7
  slug: adyen-updateaccountholderrequest
- name: UpdateAccountHolderResponse
  property_count: 11
  slug: adyen-updateaccountholderresponse
- name: UpdateAccountHolderStateRequest
  property_count: 4
  slug: adyen-updateaccountholderstaterequest
- name: UpdateAccountRequest
  property_count: 7
  slug: adyen-updateaccountrequest
- name: UpdateAccountResponse
  property_count: 10
  slug: adyen-updateaccountresponse
- name: UpdateCompanyApiCredentialRequest
  property_count: 5
  slug: adyen-updatecompanyapicredentialrequest
- name: UpdateCompanyUserRequest
  property_count: 7
  slug: adyen-updatecompanyuserrequest
- name: UpdateCompanyWebhookRequest
  property_count: 15
  slug: adyen-updatecompanywebhookrequest
- name: UpdateMerchantApiCredentialRequest
  property_count: 4
  slug: adyen-updatemerchantapicredentialrequest
- name: UpdateMerchantUserRequest
  property_count: 6
  slug: adyen-updatemerchantuserrequest
- name: UpdateMerchantWebhookRequest
  property_count: 13
  slug: adyen-updatemerchantwebhookrequest
- name: UpdateNetworkTokenRequest
  property_count: 1
  slug: adyen-updatenetworktokenrequest
- name: UpdateNotificationConfigurationRequest
  property_count: 1
  slug: adyen-updatenotificationconfigurationrequest
- name: UpdatePaymentInstrument
  property_count: 12
  slug: adyen-updatepaymentinstrument
- name: UpdatePaymentLinkRequest
  property_count: 1
  slug: adyen-updatepaymentlinkrequest
- name: UpdatePaymentMethodInfo
  property_count: 18
  slug: adyen-updatepaymentmethodinfo
- name: UpdatePayoutScheduleRequest
  property_count: 3
  slug: adyen-updatepayoutschedulerequest
- name: UpdatePayoutSettingsRequest
  property_count: 1
  slug: adyen-updatepayoutsettingsrequest
- name: UpdateSplitConfigurationLogicRequest
  property_count: 15
  slug: adyen-updatesplitconfigurationlogicrequest
- name: UpdateSplitConfigurationRequest
  property_count: 1
  slug: adyen-updatesplitconfigurationrequest
- name: UpdateSplitConfigurationRuleRequest
  property_count: 4
  slug: adyen-updatesplitconfigurationrulerequest
- name: UpdateStoreRequest
  property_count: 7
  slug: adyen-updatestorerequest
- name: UpdateSweepConfigurationV2
  property_count: 13
  slug: adyen-updatesweepconfigurationv2
- name: UPI Collect
  property_count: 7
  slug: adyen-upicollectdetails
- name: UPI Intent
  property_count: 5
  slug: adyen-upiintentdetails
- name: UploadAndroidAppResponse
  property_count: 1
  slug: adyen-uploadandroidappresponse
- name: UploadDocumentRequest
  property_count: 2
  slug: adyen-uploaddocumentrequest
- name: Url
  property_count: 4
  slug: adyen-url
- name: User
  property_count: 10
  slug: adyen-user
- name: USLocalAccountIdentification
  property_count: 4
  slug: adyen-uslocalaccountidentification
- name: UtilityRequest
  property_count: 1
  slug: adyen-utilityrequest
- name: UtilityResponse
  property_count: 1
  slug: adyen-utilityresponse
- name: UTMCoordinates
  property_count: 3
  slug: adyen-utmcoordinates
- name: ValidationResult
  property_count: 2
  slug: adyen-validationresult
- name: VerificationDeadline
  property_count: 3
  slug: adyen-verificationdeadline
- name: VerificationError-recursive
  property_count: 5
  slug: adyen-verificationerror-recursive
- name: VerificationError
  property_count: 6
  slug: adyen-verificationerror
- name: VerificationErrors
  property_count: 1
  slug: adyen-verificationerrors
- name: ViasAddress
  property_count: 6
  slug: adyen-viasaddress
- name: ViasName
  property_count: 4
  slug: adyen-viasname
- name: ViasPersonalData
  property_count: 3
  slug: adyen-viaspersonaldata
- name: ViasPhoneNumber
  property_count: 3
  slug: adyen-viasphonenumber
- name: Vipps
  property_count: 5
  slug: adyen-vippsdetails
- name: VippsInfo
  property_count: 2
  slug: adyen-vippsinfo
- name: Visa Checkout
  property_count: 4
  slug: adyen-visacheckoutdetails
- name: VoidPendingRefundRequest
  property_count: 11
  slug: adyen-voidpendingrefundrequest
- name: WebData
  property_count: 2
  slug: adyen-webdata
- name: WebDataExemption
  property_count: 1
  slug: adyen-webdataexemption
- name: Webhook
  property_count: 22
  slug: adyen-webhook
- name: WebhookLinks
  property_count: 5
  slug: adyen-webhooklinks
- name: WeChat Pay
  property_count: 2
  slug: adyen-wechatpaydetails
- name: WeChat Pay - Mini Program
  property_count: 4
  slug: adyen-wechatpayminiprogramdetails
- name: WifiProfiles
  property_count: 2
  slug: adyen-wifiprofiles
- name: Zip
  property_count: 5
  slug: adyen-zipdetails
- name: Amount
  property_count: 2
  slug: authentication-webhooks-amount
- name: AuthenticationInfo
  property_count: 15
  slug: authentication-webhooks-authentication-info
- name: AuthenticationNotificationData
  property_count: 6
  slug: authentication-webhooks-authentication-notification-data
- name: AuthenticationNotificationRequest
  property_count: 3
  slug: authentication-webhooks-authentication-notification-request
- name: BalancePlatformNotificationResponse
  property_count: 1
  slug: authentication-webhooks-balance-platform-notification-response
- name: ChallengeInfo
  property_count: 6
  slug: authentication-webhooks-challenge-info
- name: PurchaseInfo
  property_count: 3
  slug: authentication-webhooks-purchase-info
- name: Resource
  property_count: 3
  slug: authentication-webhooks-resource
- name: Amount
  property_count: 2
  slug: balance-control-amount
- name: BalanceTransferRequest
  property_count: 6
  slug: balance-control-balance-transfer-request
- name: BalanceTransferResponse
  property_count: 9
  slug: balance-control-balance-transfer-response
- name: Amount
  property_count: 2
  slug: binlookup-amount
- name: BinDetail
  property_count: 1
  slug: binlookup-bin-detail
- name: CardBin
  property_count: 11
  slug: binlookup-card-bin
- name: CostEstimateAssumptions
  property_count: 3
  slug: binlookup-cost-estimate-assumptions
- name: CostEstimateRequest
  property_count: 10
  slug: binlookup-cost-estimate-request
- name: CostEstimateResponse
  property_count: 5
  slug: binlookup-cost-estimate-response
- name: DSPublicKeyDetail
  property_count: 5
  slug: binlookup-ds-public-key-detail
- name: MerchantDetails
  property_count: 3
  slug: binlookup-merchant-details
- name: Recurring
  property_count: 5
  slug: binlookup-recurring
- name: ThreeDSAvailabilityRequest
  property_count: 6
  slug: binlookup-three-ds-availability-request
- name: ThreeDSAvailabilityResponse
  property_count: 5
  slug: binlookup-three-ds-availability-response
- name: ThreeDS2CardRangeDetail
  property_count: 6
  slug: binlookup-three-ds2-card-range-detail
- name: AccountInfo
  property_count: 19
  slug: checkout-account-info
- name: AcctInfo
  property_count: 16
  slug: checkout-acct-info
- name: AchDetails
  property_count: 10
  slug: checkout-ach-details
- name: AdditionalDataAirline
  property_count: 28
  slug: checkout-additional-data-airline
- name: AdditionalDataCarRental
  property_count: 23
  slug: checkout-additional-data-car-rental
- name: AdditionalDataCommon
  property_count: 16
  slug: checkout-additional-data-common
- name: AdditionalDataLevel23
  property_count: 17
  slug: checkout-additional-data-level23
- name: AdditionalDataLodging
  property_count: 16
  slug: checkout-additional-data-lodging
- name: AdditionalDataOpenInvoice
  property_count: 18
  slug: checkout-additional-data-open-invoice
- name: AdditionalDataOpi
  property_count: 1
  slug: checkout-additional-data-opi
- name: AdditionalDataRatepay
  property_count: 8
  slug: checkout-additional-data-ratepay
- name: AdditionalDataRetry
  property_count: 3
  slug: checkout-additional-data-retry
- name: AdditionalDataRisk
  property_count: 21
  slug: checkout-additional-data-risk
- name: AdditionalDataRiskStandalone
  property_count: 15
  slug: checkout-additional-data-risk-standalone
- name: AdditionalDataSubMerchant
  property_count: 10
  slug: checkout-additional-data-sub-merchant
- name: AdditionalDataTemporaryServices
  property_count: 9
  slug: checkout-additional-data-temporary-services
- name: AdditionalDataWallets
  property_count: 6
  slug: checkout-additional-data-wallets
- name: AdditionalData3DSecure
  property_count: 6
  slug: checkout-additional-data3-d-secure
- name: Address
  property_count: 6
  slug: checkout-address
- name: AfterpayDetails
  property_count: 7
  slug: checkout-afterpay-details
- name: AmazonPayDetails
  property_count: 4
  slug: checkout-amazon-pay-details
- name: Amount
  property_count: 2
  slug: checkout-amount
- name: AndroidPayDetails
  property_count: 2
  slug: checkout-android-pay-details
- name: ApplePayDetails
  property_count: 6
  slug: checkout-apple-pay-details
- name: ApplePayDonations
  property_count: 6
  slug: checkout-apple-pay-donations
- name: ApplePaySessionRequest
  property_count: 3
  slug: checkout-apple-pay-session-request
- name: ApplePaySessionResponse
  property_count: 1
  slug: checkout-apple-pay-session-response
- name: ApplicationInfo
  property_count: 6
  slug: checkout-application-info
- name: AuthenticationData
  property_count: 3
  slug: checkout-authentication-data
- name: Avs
  property_count: 2
  slug: checkout-avs
- name: BacsDirectDebitDetails
  property_count: 7
  slug: checkout-bacs-direct-debit-details
- name: BalanceCheckRequest
  property_count: 44
  slug: checkout-balance-check-request
- name: BalanceCheckResponse
  property_count: 7
  slug: checkout-balance-check-response
- name: BankAccount
  property_count: 9
  slug: checkout-bank-account
- name: BillDeskDetails
  property_count: 3
  slug: checkout-bill-desk-details
- name: BillingAddress
  property_count: 6
  slug: checkout-billing-address
- name: BlikDetails
  property_count: 5
  slug: checkout-blik-details
- name: BrowserInfo
  property_count: 9
  slug: checkout-browser-info
- name: CancelOrderRequest
  property_count: 2
  slug: checkout-cancel-order-request
- name: CancelOrderResponse
  property_count: 2
  slug: checkout-cancel-order-response
- name: CardBrandDetails
  property_count: 2
  slug: checkout-card-brand-details
- name: CardDetailsRequest
  property_count: 5
  slug: checkout-card-details-request
- name: CardDetailsResponse
  property_count: 1
  slug: checkout-card-details-response
- name: CardDetails
  property_count: 19
  slug: checkout-card-details
- name: CardDonations
  property_count: 19
  slug: checkout-card-donations
- name: Card
  property_count: 8
  slug: checkout-card
- name: CellulantDetails
  property_count: 3
  slug: checkout-cellulant-details
- name: CheckoutAwaitAction
  property_count: 4
  slug: checkout-checkout-await-action
- name: CheckoutDelegatedAuthenticationAction
  property_count: 6
  slug: checkout-checkout-delegated-authentication-action
- name: CheckoutNativeRedirectAction
  property_count: 6
  slug: checkout-checkout-native-redirect-action
- name: CheckoutOrderResponse
  property_count: 6
  slug: checkout-checkout-order-response
- name: CheckoutQrCodeAction
  property_count: 6
  slug: checkout-checkout-qr-code-action
- name: CheckoutRedirectAction
  property_count: 5
  slug: checkout-checkout-redirect-action
- name: CheckoutSDKAction
  property_count: 5
  slug: checkout-checkout-sdk-action
- name: CheckoutSessionInstallmentOption
  property_count: 3
  slug: checkout-checkout-session-installment-option
- name: CheckoutThreeDS2Action
  property_count: 7
  slug: checkout-checkout-three-ds2-action
- name: CheckoutVoucherAction
  property_count: 21
  slug: checkout-checkout-voucher-action
- name: CommonField
  property_count: 2
  slug: checkout-common-field
- name: Company
  property_count: 6
  slug: checkout-company
- name: Configuration
  property_count: 4
  slug: checkout-configuration
- name: CreateCheckoutSessionRequest
  property_count: 59
  slug: checkout-create-checkout-session-request
- name: CreateCheckoutSessionResponse
  property_count: 62
  slug: checkout-create-checkout-session-response
- name: CreateOrderRequest
  property_count: 4
  slug: checkout-create-order-request
- name: CreateOrderResponse
  property_count: 10
  slug: checkout-create-order-response
- name: DeliveryAddress
  property_count: 8
  slug: checkout-delivery-address
- name: DetailsRequestAuthenticationData
  property_count: 1
  slug: checkout-details-request-authentication-data
- name: DeviceRenderOptions
  property_count: 2
  slug: checkout-device-render-options
- name: DokuDetails
  property_count: 5
  slug: checkout-doku-details
- name: DonationPaymentRequest
  property_count: 41
  slug: checkout-donation-payment-request
- name: DonationPaymentResponse
  property_count: 7
  slug: checkout-donation-payment-response
- name: DotpayDetails
  property_count: 3
  slug: checkout-dotpay-details
- name: DragonpayDetails
  property_count: 4
  slug: checkout-dragonpay-details
- name: EcontextVoucherDetails
  property_count: 6
  slug: checkout-econtext-voucher-details
- name: EncryptedOrderData
  property_count: 2
  slug: checkout-encrypted-order-data
- name: ExternalPlatform
  property_count: 3
  slug: checkout-external-platform
- name: ForexQuote
  property_count: 12
  slug: checkout-forex-quote
- name: FraudCheckResult
  property_count: 3
  slug: checkout-fraud-check-result
- name: FraudResult
  property_count: 2
  slug: checkout-fraud-result
- name: FundOrigin
  property_count: 5
  slug: checkout-fund-origin
- name: FundRecipient
  property_count: 10
  slug: checkout-fund-recipient
- name: GenericIssuerPaymentMethodDetails
  property_count: 5
  slug: checkout-generic-issuer-payment-method-details
- name: GiropayDetails
  property_count: 4
  slug: checkout-giropay-details
- name: GooglePayDetails
  property_count: 7
  slug: checkout-google-pay-details
- name: GooglePayDonations
  property_count: 7
  slug: checkout-google-pay-donations
- name: IdealDetails
  property_count: 5
  slug: checkout-ideal-details
- name: IdealDonations
  property_count: 5
  slug: checkout-ideal-donations
- name: InputDetail
  property_count: 9
  slug: checkout-input-detail
- name: InstallmentOption
  property_count: 4
  slug: checkout-installment-option
- name: InstallmentsNumber
  property_count: 1
  slug: checkout-installments-number
- name: Installments
  property_count: 2
  slug: checkout-installments
- name: Item
  property_count: 2
  slug: checkout-item
- name: KlarnaDetails
  property_count: 8
  slug: checkout-klarna-details
- name: LineItem
  property_count: 17
  slug: checkout-line-item
- name: ListStoredPaymentMethodsResponse
  property_count: 3
  slug: checkout-list-stored-payment-methods-response
- name: Mandate
  property_count: 8
  slug: checkout-mandate
- name: MasterpassDetails
  property_count: 4
  slug: checkout-masterpass-details
- name: MbwayDetails
  property_count: 4
  slug: checkout-mbway-details
- name: MerchantDevice
  property_count: 3
  slug: checkout-merchant-device
- name: MerchantRiskIndicator
  property_count: 14
  slug: checkout-merchant-risk-indicator
- name: MobilePayDetails
  property_count: 2
  slug: checkout-mobile-pay-details
- name: MolPayDetails
  property_count: 3
  slug: checkout-mol-pay-details
- name: Name
  property_count: 2
  slug: checkout-name
- name: OpenInvoiceDetails
  property_count: 7
  slug: checkout-open-invoice-details
- name: PayPalDetails
  property_count: 9
  slug: checkout-pay-pal-details
- name: PayUUpiDetails
  property_count: 6
  slug: checkout-pay-u-upi-details
- name: PayWithGoogleDetails
  property_count: 6
  slug: checkout-pay-with-google-details
- name: PayWithGoogleDonations
  property_count: 6
  slug: checkout-pay-with-google-donations
- name: PaymentAmountUpdateRequest
  property_count: 7
  slug: checkout-payment-amount-update-request
- name: PaymentAmountUpdateResponse
  property_count: 9
  slug: checkout-payment-amount-update-response
- name: PaymentCancelRequest
  property_count: 3
  slug: checkout-payment-cancel-request
- name: PaymentCancelResponse
  property_count: 5
  slug: checkout-payment-cancel-response
- name: PaymentCaptureRequest
  property_count: 8
  slug: checkout-payment-capture-request
- name: PaymentCaptureResponse
  property_count: 10
  slug: checkout-payment-capture-response
- name: PaymentCompletionDetails
  property_count: 18
  slug: checkout-payment-completion-details
- name: PaymentDetailsRequest
  property_count: 4
  slug: checkout-payment-details-request
- name: PaymentDetailsResponse
  property_count: 15
  slug: checkout-payment-details-response
- name: PaymentDetails
  property_count: 2
  slug: checkout-payment-details
- name: PaymentLinkRequest
  property_count: 38
  slug: checkout-payment-link-request
- name: PaymentLinkResponse
  property_count: 42
  slug: checkout-payment-link-response
- name: PaymentMethodGroup
  property_count: 3
  slug: checkout-payment-method-group
- name: PaymentMethodIssuer
  property_count: 3
  slug: checkout-payment-method-issuer
- name: PaymentMethod
  property_count: 9
  slug: checkout-payment-method
- name: PaymentMethodsRequest
  property_count: 12
  slug: checkout-payment-methods-request
- name: PaymentMethodsResponse
  property_count: 2
  slug: checkout-payment-methods-response
- name: PaymentRefundRequest
  property_count: 8
  slug: checkout-payment-refund-request
- name: PaymentRefundResponse
  property_count: 10
  slug: checkout-payment-refund-response
- name: PaymentRequest
  property_count: 67
  slug: checkout-payment-request
- name: PaymentResponse
  property_count: 15
  slug: checkout-payment-response
- name: PaymentReversalRequest
  property_count: 3
  slug: checkout-payment-reversal-request
- name: PaymentReversalResponse
  property_count: 5
  slug: checkout-payment-reversal-response
- name: PaymentSetupRequest
  property_count: 56
  slug: checkout-payment-setup-request
- name: PaymentSetupResponse
  property_count: 2
  slug: checkout-payment-setup-response
- name: PaymentVerificationRequest
  property_count: 1
  slug: checkout-payment-verification-request
- name: PaymentVerificationResponse
  property_count: 10
  slug: checkout-payment-verification-response
- name: Phone
  property_count: 2
  slug: checkout-phone
- name: PlatformChargebackLogic
  property_count: 3
  slug: checkout-platform-chargeback-logic
- name: RatepayDetails
  property_count: 7
  slug: checkout-ratepay-details
- name: RecurringDetail
  property_count: 11
  slug: checkout-recurring-detail
- name: Recurring
  property_count: 5
  slug: checkout-recurring
- name: ResponseAdditionalDataBillingAddress
  property_count: 6
  slug: checkout-response-additional-data-billing-address
- name: ResponseAdditionalDataCard
  property_count: 8
  slug: checkout-response-additional-data-card
- name: ResponseAdditionalDataCommon
  property_count: 59
  slug: checkout-response-additional-data-common
- name: ResponseAdditionalDataDomesticError
  property_count: 2
  slug: checkout-response-additional-data-domestic-error
- name: ResponseAdditionalDataInstallments
  property_count: 12
  slug: checkout-response-additional-data-installments
- name: ResponseAdditionalDataNetworkTokens
  property_count: 3
  slug: checkout-response-additional-data-network-tokens
- name: ResponseAdditionalDataOpi
  property_count: 1
  slug: checkout-response-additional-data-opi
- name: ResponseAdditionalDataSepa
  property_count: 3
  slug: checkout-response-additional-data-sepa
- name: ResponseAdditionalData3DSecure
  property_count: 5
  slug: checkout-response-additional-data3-d-secure
- name: ResponsePaymentMethod
  property_count: 2
  slug: checkout-response-payment-method
- name: RiskData
  property_count: 4
  slug: checkout-risk-data
- name: SamsungPayDetails
  property_count: 6
  slug: checkout-samsung-pay-details
- name: SDKEphemPubKey
  property_count: 4
  slug: checkout-sdk-ephem-pub-key
- name: SepaDirectDebitDetails
  property_count: 6
  slug: checkout-sepa-direct-debit-details
- name: ServiceErrorDetails
  property_count: 4
  slug: checkout-service-error-details
- name: SessionResultResponse
  property_count: 2
  slug: checkout-session-result-response
- name: ShopperInput
  property_count: 3
  slug: checkout-shopper-input
- name: ShopperInteractionDevice
  property_count: 3
  slug: checkout-shopper-interaction-device
- name: SplitAmount
  property_count: 2
  slug: checkout-split-amount
- name: Split
  property_count: 5
  slug: checkout-split
- name: StandalonePaymentCancelRequest
  property_count: 4
  slug: checkout-standalone-payment-cancel-request
- name: StandalonePaymentCancelResponse
  property_count: 5
  slug: checkout-standalone-payment-cancel-response
- name: StoredDetails
  property_count: 3
  slug: checkout-stored-details
- name: StoredPaymentMethodDetails
  property_count: 4
  slug: checkout-stored-payment-method-details
- name: StoredPaymentMethodResource
  property_count: 17
  slug: checkout-stored-payment-method-resource
- name: StoredPaymentMethod
  property_count: 17
  slug: checkout-stored-payment-method
- name: SubInputDetail
  property_count: 6
  slug: checkout-sub-input-detail
- name: SubMerchantInfo
  property_count: 5
  slug: checkout-sub-merchant-info
- name: SubMerchant
  property_count: 5
  slug: checkout-sub-merchant
- name: ThreeDSecureData
  property_count: 12
  slug: checkout-three-d-secure-data
- name: ThreeDSRequestData
  property_count: 4
  slug: checkout-three-ds-request-data
- name: ThreeDSRequestorAuthenticationInfo
  property_count: 3
  slug: checkout-three-ds-requestor-authentication-info
- name: ThreeDSRequestorPriorAuthenticationInfo
  property_count: 4
  slug: checkout-three-ds-requestor-prior-authentication-info
- name: ThreeDS2RequestData
  property_count: 40
  slug: checkout-three-ds2-request-data
- name: ThreeDS2RequestFields
  property_count: 37
  slug: checkout-three-ds2-request-fields
- name: ThreeDS2ResponseData
  property_count: 19
  slug: checkout-three-ds2-response-data
- name: ThreeDS2Result
  property_count: 14
  slug: checkout-three-ds2-result
- name: UpdatePaymentLinkRequest
  property_count: 1
  slug: checkout-update-payment-link-request
- name: UpiCollectDetails
  property_count: 7
  slug: checkout-upi-collect-details
- name: UpiIntentDetails
  property_count: 5
  slug: checkout-upi-intent-details
- name: UtilityRequest
  property_count: 1
  slug: checkout-utility-request
- name: UtilityResponse
  property_count: 1
  slug: checkout-utility-response
- name: VippsDetails
  property_count: 5
  slug: checkout-vipps-details
- name: VisaCheckoutDetails
  property_count: 4
  slug: checkout-visa-checkout-details
- name: WeChatPayDetails
  property_count: 2
  slug: checkout-we-chat-pay-details
- name: WeChatPayMiniProgramDetails
  property_count: 4
  slug: checkout-we-chat-pay-mini-program-details
- name: ZipDetails
  property_count: 5
  slug: checkout-zip-details
- name: AccountHolderCapability
  property_count: 10
  slug: configuration-account-holder-capability
- name: AccountHolderInfo
  property_count: 9
  slug: configuration-account-holder-info
- name: AccountHolder
  property_count: 13
  slug: configuration-account-holder
- name: AccountHolderUpdateRequest
  property_count: 11
  slug: configuration-account-holder-update-request
- name: AccountSupportingEntityCapability
  property_count: 7
  slug: configuration-account-supporting-entity-capability
- name: ActiveNetworkTokensRestriction
  property_count: 2
  slug: configuration-active-network-tokens-restriction
- name: AdditionalBankIdentification
  property_count: 2
  slug: configuration-additional-bank-identification
- name: AddressRequirement
  property_count: 3
  slug: configuration-address-requirement
- name: Address
  property_count: 6
  slug: configuration-address
- name: AmountMinMaxRequirement
  property_count: 4
  slug: configuration-amount-min-max-requirement
- name: Amount
  property_count: 2
  slug: configuration-amount
- name: AULocalAccountIdentification
  property_count: 3
  slug: configuration-au-local-account-identification
- name: Authentication
  property_count: 3
  slug: configuration-authentication
- name: BalanceAccountBase
  property_count: 10
  slug: configuration-balance-account-base
- name: BalanceAccountInfo
  property_count: 8
  slug: configuration-balance-account-info
- name: BalanceAccount
  property_count: 11
  slug: configuration-balance-account
- name: BalanceAccountUpdateRequest
  property_count: 7
  slug: configuration-balance-account-update-request
- name: BalancePlatform
  property_count: 3
  slug: configuration-balance-platform
- name: Balance
  property_count: 5
  slug: configuration-balance
- name: BalanceSweepConfigurationsResponse
  property_count: 3
  slug: configuration-balance-sweep-configurations-response
- name: BankAccountIdentificationTypeRequirement
  property_count: 3
  slug: configuration-bank-account-identification-type-requirement
- name: BankAccountIdentificationValidationRequest
  property_count: 1
  slug: configuration-bank-account-identification-validation-request
- name: BankAccountModel
  property_count: 1
  slug: configuration-bank-account-model
- name: BankAccount
  property_count: 1
  slug: configuration-bank-account
- name: BankIdentification
  property_count: 3
  slug: configuration-bank-identification
- name: BRLocalAccountIdentification
  property_count: 4
  slug: configuration-br-local-account-identification
- name: BrandVariantsRestriction
  property_count: 2
  slug: configuration-brand-variants-restriction
- name: BulkAddress
  property_count: 9
  slug: configuration-bulk-address
- name: CALocalAccountIdentification
  property_count: 5
  slug: configuration-ca-local-account-identification
- name: CapabilityProblemEntity-recursive
  property_count: 3
  slug: configuration-capability-problem-entity-recursive
- name: CapabilityProblemEntity
  property_count: 4
  slug: configuration-capability-problem-entity
- name: CapabilityProblem
  property_count: 2
  slug: configuration-capability-problem
- name: CapabilitySettings
  property_count: 5
  slug: configuration-capability-settings
- name: CapitalBalance
  property_count: 4
  slug: configuration-capital-balance
- name: CapitalGrantAccount
  property_count: 4
  slug: configuration-capital-grant-account
- name: CardConfiguration
  property_count: 14
  slug: configuration-card-configuration
- name: CardInfo
  property_count: 8
  slug: configuration-card-info
- name: CardOrderItemDeliveryStatus
  property_count: 3
  slug: configuration-card-order-item-delivery-status
- name: CardOrderItem
  property_count: 8
  slug: configuration-card-order-item
- name: CardOrder
  property_count: 8
  slug: configuration-card-order
- name: Card
  property_count: 13
  slug: configuration-card
- name: ContactDetails
  property_count: 4
  slug: configuration-contact-details
- name: CounterpartyBankRestriction
  property_count: 2
  slug: configuration-counterparty-bank-restriction
- name: Counterparty
  property_count: 2
  slug: configuration-counterparty
- name: CountriesRestriction
  property_count: 2
  slug: configuration-countries-restriction
- name: CreateSweepConfigurationV2
  property_count: 12
  slug: configuration-create-sweep-configuration-v2
- name: CZLocalAccountIdentification
  property_count: 3
  slug: configuration-cz-local-account-identification
- name: DayOfWeekRestriction
  property_count: 2
  slug: configuration-day-of-week-restriction
- name: DeliveryAddress
  property_count: 7
  slug: configuration-delivery-address
- name: DeliveryContact
  property_count: 6
  slug: configuration-delivery-contact
- name: DeviceInfo
  property_count: 11
  slug: configuration-device-info
- name: DifferentCurrenciesRestriction
  property_count: 2
  slug: configuration-different-currencies-restriction
- name: DKLocalAccountIdentification
  property_count: 3
  slug: configuration-dk-local-account-identification
- name: Duration
  property_count: 2
  slug: configuration-duration
- name: EntryModesRestriction
  property_count: 2
  slug: configuration-entry-modes-restriction
- name: Expiry
  property_count: 2
  slug: configuration-expiry
- name: Fee
  property_count: 1
  slug: configuration-fee
- name: GetNetworkTokenResponse
  property_count: 1
  slug: configuration-get-network-token-response
- name: GetTaxFormResponse
  property_count: 2
  slug: configuration-get-tax-form-response
- name: GrantLimit
  property_count: 1
  slug: configuration-grant-limit
- name: GrantOffer
  property_count: 8
  slug: configuration-grant-offer
- name: GrantOffers
  property_count: 1
  slug: configuration-grant-offers
- name: HKLocalAccountIdentification
  property_count: 3
  slug: configuration-hk-local-account-identification
- name: HULocalAccountIdentification
  property_count: 2
  slug: configuration-hu-local-account-identification
- name: IbanAccountIdentification
  property_count: 2
  slug: configuration-iban-account-identification
- name: InternationalTransactionRestriction
  property_count: 2
  slug: configuration-international-transaction-restriction
- name: InvalidField
  property_count: 3
  slug: configuration-invalid-field
- name: JSONObject
  property_count: 0
  slug: configuration-json-object
- name: ListNetworkTokensResponse
  property_count: 1
  slug: configuration-list-network-tokens-response
- name: MatchingTransactionsRestriction
  property_count: 2
  slug: configuration-matching-transactions-restriction
- name: MccsRestriction
  property_count: 2
  slug: configuration-mccs-restriction
- name: MerchantAcquirerPair
  property_count: 2
  slug: configuration-merchant-acquirer-pair
- name: MerchantNamesRestriction
  property_count: 2
  slug: configuration-merchant-names-restriction
- name: MerchantsRestriction
  property_count: 2
  slug: configuration-merchants-restriction
- name: Name
  property_count: 2
  slug: configuration-name
- name: NetworkToken
  property_count: 8
  slug: configuration-network-token
- name: NOLocalAccountIdentification
  property_count: 2
  slug: configuration-no-local-account-identification
- name: NumberAndBicAccountIdentification
  property_count: 4
  slug: configuration-number-and-bic-account-identification
- name: NZLocalAccountIdentification
  property_count: 2
  slug: configuration-nz-local-account-identification
- name: PaginatedAccountHoldersResponse
  property_count: 3
  slug: configuration-paginated-account-holders-response
- name: PaginatedBalanceAccountsResponse
  property_count: 3
  slug: configuration-paginated-balance-accounts-response
- name: PaginatedGetCardOrderItemResponse
  property_count: 3
  slug: configuration-paginated-get-card-order-item-response
- name: PaginatedGetCardOrderResponse
  property_count: 3
  slug: configuration-paginated-get-card-order-response
- name: PaginatedPaymentInstrumentsResponse
  property_count: 3
  slug: configuration-paginated-payment-instruments-response
- name: PaymentInstrumentGroupInfo
  property_count: 5
  slug: configuration-payment-instrument-group-info
- name: PaymentInstrumentGroup
  property_count: 6
  slug: configuration-payment-instrument-group
- name: PaymentInstrumentInfo
  property_count: 10
  slug: configuration-payment-instrument-info
- name: PaymentInstrumentRequirement
  property_count: 5
  slug: configuration-payment-instrument-requirement
- name: PaymentInstrumentRevealInfo
  property_count: 3
  slug: configuration-payment-instrument-reveal-info
- name: PaymentInstrument
  property_count: 11
  slug: configuration-payment-instrument
- name: PaymentInstrumentUpdateRequest
  property_count: 5
  slug: configuration-payment-instrument-update-request
- name: PhoneNumber
  property_count: 3
  slug: configuration-phone-number
- name: Phone
  property_count: 2
  slug: configuration-phone
- name: PinChangeRequest
  property_count: 4
  slug: configuration-pin-change-request
- name: PinChangeResponse
  property_count: 1
  slug: configuration-pin-change-response
- name: PLLocalAccountIdentification
  property_count: 2
  slug: configuration-pl-local-account-identification
- name: PlatformPaymentConfiguration
  property_count: 2
  slug: configuration-platform-payment-configuration
- name: ProcessingTypesRestriction
  property_count: 2
  slug: configuration-processing-types-restriction
- name: PublicKeyResponse
  property_count: 2
  slug: configuration-public-key-response
- name: RemediatingAction
  property_count: 2
  slug: configuration-remediating-action
- name: Repayment
  property_count: 3
  slug: configuration-repayment
- name: RepaymentTerm
  property_count: 2
  slug: configuration-repayment-term
- name: RestServiceError
  property_count: 9
  slug: configuration-rest-service-error
- name: RevealPinRequest
  property_count: 2
  slug: configuration-reveal-pin-request
- name: RevealPinResponse
  property_count: 2
  slug: configuration-reveal-pin-response
- name: SameAmountRestriction
  property_count: 2
  slug: configuration-same-amount-restriction
- name: SameCounterpartyRestriction
  property_count: 2
  slug: configuration-same-counterparty-restriction
- name: SELocalAccountIdentification
  property_count: 3
  slug: configuration-se-local-account-identification
- name: SGLocalAccountIdentification
  property_count: 3
  slug: configuration-sg-local-account-identification
- name: StringMatch
  property_count: 2
  slug: configuration-string-match
- name: SweepConfigurationV2
  property_count: 13
  slug: configuration-sweep-configuration-v2
- name: SweepCounterparty
  property_count: 3
  slug: configuration-sweep-counterparty
- name: SweepSchedule
  property_count: 2
  slug: configuration-sweep-schedule
- name: ThresholdRepayment
  property_count: 1
  slug: configuration-threshold-repayment
- name: TimeOfDayRestriction
  property_count: 2
  slug: configuration-time-of-day-restriction
- name: TimeOfDay
  property_count: 2
  slug: configuration-time-of-day
- name: TotalAmountRestriction
  property_count: 2
  slug: configuration-total-amount-restriction
- name: TransactionRuleEntityKey
  property_count: 2
  slug: configuration-transaction-rule-entity-key
- name: TransactionRuleInfo
  property_count: 13
  slug: configuration-transaction-rule-info
- name: TransactionRuleInterval
  property_count: 6
  slug: configuration-transaction-rule-interval
- name: TransactionRuleResponse
  property_count: 1
  slug: configuration-transaction-rule-response
- name: TransactionRuleRestrictions
  property_count: 17
  slug: configuration-transaction-rule-restrictions
- name: TransactionRule
  property_count: 14
  slug: configuration-transaction-rule
- name: TransactionRulesResponse
  property_count: 1
  slug: configuration-transaction-rules-response
- name: TransferRouteRequest
  property_count: 7
  slug: configuration-transfer-route-request
- name: TransferRouteResponse
  property_count: 1
  slug: configuration-transfer-route-response
- name: TransferRoute
  property_count: 5
  slug: configuration-transfer-route
- name: UKLocalAccountIdentification
  property_count: 3
  slug: configuration-uk-local-account-identification
- name: UpdateNetworkTokenRequest
  property_count: 1
  slug: configuration-update-network-token-request
- name: UpdatePaymentInstrument
  property_count: 12
  slug: configuration-update-payment-instrument
- name: UpdateSweepConfigurationV2
  property_count: 13
  slug: configuration-update-sweep-configuration-v2
- name: USLocalAccountIdentification
  property_count: 4
  slug: configuration-us-local-account-identification
- name: VerificationDeadline
  property_count: 3
  slug: configuration-verification-deadline
- name: VerificationError-recursive
  property_count: 5
  slug: configuration-verification-error-recursive
- name: VerificationError
  property_count: 6
  slug: configuration-verification-error
- name: AccountHolderCapability
  property_count: 10
  slug: configuration-webhooks-account-holder-capability
- name: AccountHolderNotificationData
  property_count: 2
  slug: configuration-webhooks-account-holder-notification-data
- name: AccountHolderNotificationRequest
  property_count: 3
  slug: configuration-webhooks-account-holder-notification-request
- name: AccountHolder
  property_count: 13
  slug: configuration-webhooks-account-holder
- name: AccountSupportingEntityCapability
  property_count: 7
  slug: configuration-webhooks-account-supporting-entity-capability
- name: Address
  property_count: 6
  slug: configuration-webhooks-address
- name: Amount
  property_count: 2
  slug: configuration-webhooks-amount
- name: Authentication
  property_count: 3
  slug: configuration-webhooks-authentication
- name: BalanceAccountNotificationData
  property_count: 2
  slug: configuration-webhooks-balance-account-notification-data
- name: BalanceAccountNotificationRequest
  property_count: 3
  slug: configuration-webhooks-balance-account-notification-request
- name: BalanceAccount
  property_count: 12
  slug: configuration-webhooks-balance-account
- name: BalancePlatformNotificationResponse
  property_count: 1
  slug: configuration-webhooks-balance-platform-notification-response
- name: Balance
  property_count: 5
  slug: configuration-webhooks-balance
- name: BulkAddress
  property_count: 9
  slug: configuration-webhooks-bulk-address
- name: CapabilityProblemEntity-recursive
  property_count: 3
  slug: configuration-webhooks-capability-problem-entity-recursive
- name: CapabilityProblemEntity
  property_count: 4
  slug: configuration-webhooks-capability-problem-entity
- name: CapabilityProblem
  property_count: 2
  slug: configuration-webhooks-capability-problem
- name: CapabilitySettings
  property_count: 5
  slug: configuration-webhooks-capability-settings
- name: CardConfiguration
  property_count: 14
  slug: configuration-webhooks-card-configuration
- name: CardOrderItemDeliveryStatus
  property_count: 3
  slug: configuration-webhooks-card-order-item-delivery-status
- name: CardOrderItem
  property_count: 8
  slug: configuration-webhooks-card-order-item
- name: CardOrderNotificationRequest
  property_count: 3
  slug: configuration-webhooks-card-order-notification-request
- name: Card
  property_count: 13
  slug: configuration-webhooks-card
- name: ContactDetails
  property_count: 4
  slug: configuration-webhooks-contact-details
- name: Contact
  property_count: 7
  slug: configuration-webhooks-contact
- name: Expiry
  property_count: 2
  slug: configuration-webhooks-expiry
- name: IbanAccountIdentification
  property_count: 2
  slug: configuration-webhooks-iban-account-identification
- name: Name
  property_count: 2
  slug: configuration-webhooks-name
- name: PaymentInstrumentNotificationData
  property_count: 2
  slug: configuration-webhooks-payment-instrument-notification-data
- name: PaymentInstrumentReference
  property_count: 1
  slug: configuration-webhooks-payment-instrument-reference
- name: PaymentInstrument
  property_count: 10
  slug: configuration-webhooks-payment-instrument
- name: PaymentNotificationRequest
  property_count: 3
  slug: configuration-webhooks-payment-notification-request
- name: PersonalData
  property_count: 3
  slug: configuration-webhooks-personal-data
- name: PhoneNumber
  property_count: 3
  slug: configuration-webhooks-phone-number
- name: Phone
  property_count: 2
  slug: configuration-webhooks-phone
- name: PlatformPaymentConfiguration
  property_count: 2
  slug: configuration-webhooks-platform-payment-configuration
- name: RemediatingAction
  property_count: 2
  slug: configuration-webhooks-remediating-action
- name: Resource
  property_count: 3
  slug: configuration-webhooks-resource
- name: SweepConfigurationNotificationData
  property_count: 3
  slug: configuration-webhooks-sweep-configuration-notification-data
- name: SweepConfigurationNotificationRequest
  property_count: 3
  slug: configuration-webhooks-sweep-configuration-notification-request
- name: SweepConfigurationV2
  property_count: 11
  slug: configuration-webhooks-sweep-configuration-v2
- name: SweepCounterparty
  property_count: 3
  slug: configuration-webhooks-sweep-counterparty
- name: SweepSchedule
  property_count: 2
  slug: configuration-webhooks-sweep-schedule
- name: USLocalAccountIdentification
  property_count: 4
  slug: configuration-webhooks-us-local-account-identification
- name: VerificationDeadline
  property_count: 3
  slug: configuration-webhooks-verification-deadline
- name: VerificationError-recursive
  property_count: 5
  slug: configuration-webhooks-verification-error-recursive
- name: VerificationError
  property_count: 6
  slug: configuration-webhooks-verification-error
- name: SubjectErasureByPspReferenceRequest
  property_count: 3
  slug: data-protection-subject-erasure-by-psp-reference-request
- name: SubjectErasureResponse
  property_count: 1
  slug: data-protection-subject-erasure-response
- name: AcceptDisputeRequest
  property_count: 2
  slug: disputes-accept-dispute-request
- name: AcceptDisputeResponse
  property_count: 1
  slug: disputes-accept-dispute-response
- name: DefendDisputeRequest
  property_count: 3
  slug: disputes-defend-dispute-request
- name: DefendDisputeResponse
  property_count: 1
  slug: disputes-defend-dispute-response
- name: DefenseDocument
  property_count: 3
  slug: disputes-defense-document
- name: DefenseDocumentType
  property_count: 3
  slug: disputes-defense-document-type
- name: DefenseReason
  property_count: 3
  slug: disputes-defense-reason
- name: DefenseReasonsRequest
  property_count: 2
  slug: disputes-defense-reasons-request
- name: DefenseReasonsResponse
  property_count: 2
  slug: disputes-defense-reasons-response
- name: DeleteDefenseDocumentRequest
  property_count: 3
  slug: disputes-delete-defense-document-request
- name: DeleteDefenseDocumentResponse
  property_count: 1
  slug: disputes-delete-defense-document-response
- name: DisputeServiceResult
  property_count: 2
  slug: disputes-dispute-service-result
- name: SupplyDefenseDocumentRequest
  property_count: 3
  slug: disputes-supply-defense-document-request
- name: SupplyDefenseDocumentResponse
  property_count: 1
  slug: disputes-supply-defense-document-response
- name: AccountDetailBalance
  property_count: 2
  slug: funds-account-detail-balance
- name: AccountHolderBalanceRequest
  property_count: 1
  slug: funds-account-holder-balance-request
- name: AccountHolderBalanceResponse
  property_count: 5
  slug: funds-account-holder-balance-response
- name: AccountHolderTransactionListRequest
  property_count: 3
  slug: funds-account-holder-transaction-list-request
- name: AccountHolderTransactionListResponse
  property_count: 4
  slug: funds-account-holder-transaction-list-response
- name: AccountTransactionList
  property_count: 3
  slug: funds-account-transaction-list
- name: Amount
  property_count: 2
  slug: funds-amount
- name: BankAccountDetail
  property_count: 26
  slug: funds-bank-account-detail
- name: DebitAccountHolderRequest
  property_count: 6
  slug: funds-debit-account-holder-request
- name: DebitAccountHolderResponse
  property_count: 6
  slug: funds-debit-account-holder-response
- name: DetailBalance
  property_count: 3
  slug: funds-detail-balance
- name: ErrorFieldType
  property_count: 3
  slug: funds-error-field-type
- name: FieldType
  property_count: 3
  slug: funds-field-type
- name: PayoutAccountHolderRequest
  property_count: 8
  slug: funds-payout-account-holder-request
- name: PayoutAccountHolderResponse
  property_count: 6
  slug: funds-payout-account-holder-response
- name: RefundFundsTransferRequest
  property_count: 3
  slug: funds-refund-funds-transfer-request
- name: RefundFundsTransferResponse
  property_count: 6
  slug: funds-refund-funds-transfer-response
- name: RefundNotPaidOutTransfersRequest
  property_count: 2
  slug: funds-refund-not-paid-out-transfers-request
- name: RefundNotPaidOutTransfersResponse
  property_count: 3
  slug: funds-refund-not-paid-out-transfers-response
- name: SetupBeneficiaryRequest
  property_count: 3
  slug: funds-setup-beneficiary-request
- name: SetupBeneficiaryResponse
  property_count: 3
  slug: funds-setup-beneficiary-response
- name: SplitAmount
  property_count: 2
  slug: funds-split-amount
- name: Split
  property_count: 5
  slug: funds-split
- name: TransactionListForAccount
  property_count: 2
  slug: funds-transaction-list-for-account
- name: Transaction
  property_count: 16
  slug: funds-transaction
- name: TransferFundsRequest
  property_count: 5
  slug: funds-transfer-funds-request
- name: TransferFundsResponse
  property_count: 4
  slug: funds-transfer-funds-response
- name: CollectInformation
  property_count: 6
  slug: hosted-onboarding-collect-information
- name: ErrorFieldType
  property_count: 3
  slug: hosted-onboarding-error-field-type
- name: FieldType
  property_count: 3
  slug: hosted-onboarding-field-type
- name: GetOnboardingUrlRequest
  property_count: 8
  slug: hosted-onboarding-get-onboarding-url-request
- name: GetOnboardingUrlResponse
  property_count: 4
  slug: hosted-onboarding-get-onboarding-url-response
- name: GetPciUrlRequest
  property_count: 2
  slug: hosted-onboarding-get-pci-url-request
- name: GetPciUrlResponse
  property_count: 4
  slug: hosted-onboarding-get-pci-url-response
- name: ShowPages
  property_count: 9
  slug: hosted-onboarding-show-pages
- name: AcceptTermsOfServiceRequest
  property_count: 2
  slug: legal-entity-accept-terms-of-service-request
- name: AcceptTermsOfServiceResponse
  property_count: 6
  slug: legal-entity-accept-terms-of-service-response
- name: AdditionalBankIdentification
  property_count: 2
  slug: legal-entity-additional-bank-identification
- name: Address
  property_count: 6
  slug: legal-entity-address
- name: Amount
  property_count: 2
  slug: legal-entity-amount
- name: Attachment
  property_count: 5
  slug: legal-entity-attachment
- name: AULocalAccountIdentification
  property_count: 3
  slug: legal-entity-au-local-account-identification
- name: BankAccountInfo
  property_count: 5
  slug: legal-entity-bank-account-info
- name: BirthData
  property_count: 1
  slug: legal-entity-birth-data
- name: BusinessLineInfo
  property_count: 8
  slug: legal-entity-business-line-info
- name: BusinessLineInfoUpdate
  property_count: 8
  slug: legal-entity-business-line-info-update
- name: BusinessLine
  property_count: 10
  slug: legal-entity-business-line
- name: BusinessLines
  property_count: 1
  slug: legal-entity-business-lines
- name: CALocalAccountIdentification
  property_count: 5
  slug: legal-entity-ca-local-account-identification
- name: CalculateTermsOfServiceStatusResponse
  property_count: 1
  slug: legal-entity-calculate-terms-of-service-status-response
- name: CapabilityProblemEntity-recursive
  property_count: 3
  slug: legal-entity-capability-problem-entity-recursive
- name: CapabilityProblemEntity
  property_count: 4
  slug: legal-entity-capability-problem-entity
- name: CapabilityProblem
  property_count: 2
  slug: legal-entity-capability-problem
- name: CapabilitySettings
  property_count: 5
  slug: legal-entity-capability-settings
- name: CZLocalAccountIdentification
  property_count: 3
  slug: legal-entity-cz-local-account-identification
- name: DataReviewConfirmationResponse
  property_count: 1
  slug: legal-entity-data-review-confirmation-response
- name: DKLocalAccountIdentification
  property_count: 3
  slug: legal-entity-dk-local-account-identification
- name: DocumentPage
  property_count: 3
  slug: legal-entity-document-page
- name: DocumentReference
  property_count: 7
  slug: legal-entity-document-reference
- name: Document
  property_count: 13
  slug: legal-entity-document
- name: EntityReference
  property_count: 1
  slug: legal-entity-entity-reference
- name: GeneratePciDescriptionRequest
  property_count: 2
  slug: legal-entity-generate-pci-description-request
- name: GeneratePciDescriptionResponse
  property_count: 3
  slug: legal-entity-generate-pci-description-response
- name: GetPciQuestionnaireInfosResponse
  property_count: 1
  slug: legal-entity-get-pci-questionnaire-infos-response
- name: GetPciQuestionnaireResponse
  property_count: 4
  slug: legal-entity-get-pci-questionnaire-response
- name: GetTermsOfServiceAcceptanceInfosResponse
  property_count: 1
  slug: legal-entity-get-terms-of-service-acceptance-infos-response
- name: GetTermsOfServiceDocumentRequest
  property_count: 2
  slug: legal-entity-get-terms-of-service-document-request
- name: GetTermsOfServiceDocumentResponse
  property_count: 5
  slug: legal-entity-get-terms-of-service-document-response
- name: HKLocalAccountIdentification
  property_count: 3
  slug: legal-entity-hk-local-account-identification
- name: HULocalAccountIdentification
  property_count: 2
  slug: legal-entity-hu-local-account-identification
- name: IbanAccountIdentification
  property_count: 2
  slug: legal-entity-iban-account-identification
- name: IdentificationData
  property_count: 7
  slug: legal-entity-identification-data
- name: Individual
  property_count: 9
  slug: legal-entity-individual
- name: LegalEntityAssociation
  property_count: 7
  slug: legal-entity-legal-entity-association
- name: LegalEntityCapability
  property_count: 8
  slug: legal-entity-legal-entity-capability
- name: LegalEntityInfoRequiredType
  property_count: 10
  slug: legal-entity-legal-entity-info-required-type
- name: LegalEntityInfo
  property_count: 10
  slug: legal-entity-legal-entity-info
- name: LegalEntity
  property_count: 16
  slug: legal-entity-legal-entity
- name: Name
  property_count: 3
  slug: legal-entity-name
- name: NOLocalAccountIdentification
  property_count: 2
  slug: legal-entity-no-local-account-identification
- name: NumberAndBicAccountIdentification
  property_count: 4
  slug: legal-entity-number-and-bic-account-identification
- name: NZLocalAccountIdentification
  property_count: 2
  slug: legal-entity-nz-local-account-identification
- name: OnboardingLinkInfo
  property_count: 4
  slug: legal-entity-onboarding-link-info
- name: OnboardingLink
  property_count: 1
  slug: legal-entity-onboarding-link
- name: OnboardingTheme
  property_count: 5
  slug: legal-entity-onboarding-theme
- name: OnboardingThemes
  property_count: 3
  slug: legal-entity-onboarding-themes
- name: Organization
  property_count: 16
  slug: legal-entity-organization
- name: OwnerEntity
  property_count: 2
  slug: legal-entity-owner-entity
- name: PciDocumentInfo
  property_count: 3
  slug: legal-entity-pci-document-info
- name: PciSigningRequest
  property_count: 2
  slug: legal-entity-pci-signing-request
- name: PciSigningResponse
  property_count: 2
  slug: legal-entity-pci-signing-response
- name: PhoneNumber
  property_count: 2
  slug: legal-entity-phone-number
- name: PLLocalAccountIdentification
  property_count: 2
  slug: legal-entity-pl-local-account-identification
- name: RemediatingAction
  property_count: 2
  slug: legal-entity-remediating-action
- name: SELocalAccountIdentification
  property_count: 3
  slug: legal-entity-se-local-account-identification
- name: SGLocalAccountIdentification
  property_count: 3
  slug: legal-entity-sg-local-account-identification
- name: SoleProprietorship
  property_count: 11
  slug: legal-entity-sole-proprietorship
- name: SourceOfFunds
  property_count: 4
  slug: legal-entity-source-of-funds
- name: StockData
  property_count: 3
  slug: legal-entity-stock-data
- name: SupportingEntityCapability
  property_count: 4
  slug: legal-entity-supporting-entity-capability
- name: TaxInformation
  property_count: 3
  slug: legal-entity-tax-information
- name: TaxReportingClassification
  property_count: 4
  slug: legal-entity-tax-reporting-classification
- name: TermsOfServiceAcceptanceInfo
  property_count: 5
  slug: legal-entity-terms-of-service-acceptance-info
- name: TransferInstrumentInfo
  property_count: 3
  slug: legal-entity-transfer-instrument-info
- name: TransferInstrumentReference
  property_count: 4
  slug: legal-entity-transfer-instrument-reference
- name: TransferInstrument
  property_count: 7
  slug: legal-entity-transfer-instrument
- name: Trust
  property_count: 13
  slug: legal-entity-trust
- name: UKLocalAccountIdentification
  property_count: 3
  slug: legal-entity-uk-local-account-identification
- name: UndefinedBeneficiary
  property_count: 2
  slug: legal-entity-undefined-beneficiary
- name: UnincorporatedPartnership
  property_count: 12
  slug: legal-entity-unincorporated-partnership
- name: USLocalAccountIdentification
  property_count: 4
  slug: legal-entity-us-local-account-identification
- name: VerificationDeadline
  property_count: 3
  slug: legal-entity-verification-deadline
- name: VerificationError-recursive
  property_count: 5
  slug: legal-entity-verification-error-recursive
- name: VerificationError
  property_count: 6
  slug: legal-entity-verification-error
- name: VerificationErrors
  property_count: 1
  slug: legal-entity-verification-errors
- name: WebDataExemption
  property_count: 1
  slug: legal-entity-web-data-exemption
- name: WebData
  property_count: 2
  slug: legal-entity-web-data
- name: AdditionalCommission
  property_count: 3
  slug: management-additional-commission
- name: AdditionalSettingsResponse
  property_count: 3
  slug: management-additional-settings-response
- name: AdditionalSettings
  property_count: 2
  slug: management-additional-settings
- name: Address
  property_count: 7
  slug: management-address
- name: AfterpayTouchInfo
  property_count: 1
  slug: management-afterpay-touch-info
- name: AllowedOrigin
  property_count: 3
  slug: management-allowed-origin
- name: AllowedOriginsResponse
  property_count: 1
  slug: management-allowed-origins-response
- name: Amount
  property_count: 2
  slug: management-amount
- name: AndroidApp
  property_count: 8
  slug: management-android-app
- name: AndroidAppsResponse
  property_count: 1
  slug: management-android-apps-response
- name: AndroidCertificate
  property_count: 7
  slug: management-android-certificate
- name: AndroidCertificatesResponse
  property_count: 1
  slug: management-android-certificates-response
- name: ApiCredentialLinks
  property_count: 6
  slug: management-api-credential-links
- name: ApiCredential
  property_count: 9
  slug: management-api-credential
- name: ApplePayInfo
  property_count: 1
  slug: management-apple-pay-info
- name: BcmcInfo
  property_count: 2
  slug: management-bcmc-info
- name: BillingEntitiesResponse
  property_count: 1
  slug: management-billing-entities-response
- name: BillingEntity
  property_count: 5
  slug: management-billing-entity
- name: CardholderReceipt
  property_count: 1
  slug: management-cardholder-receipt
- name: CartesBancairesInfo
  property_count: 2
  slug: management-cartes-bancaires-info
- name: ClearpayInfo
  property_count: 1
  slug: management-clearpay-info
- name: Commission
  property_count: 2
  slug: management-commission
- name: CompanyApiCredential
  property_count: 10
  slug: management-company-api-credential
- name: CompanyLinks
  property_count: 4
  slug: management-company-links
- name: Company
  property_count: 7
  slug: management-company
- name: CompanyUser
  property_count: 11
  slug: management-company-user
- name: Configuration
  property_count: 4
  slug: management-configuration
- name: Connectivity
  property_count: 1
  slug: management-connectivity
- name: Contact
  property_count: 5
  slug: management-contact
- name: CreateAllowedOriginRequest
  property_count: 3
  slug: management-create-allowed-origin-request
- name: CreateApiCredentialResponse
  property_count: 11
  slug: management-create-api-credential-response
- name: CreateCompanyApiCredentialRequest
  property_count: 4
  slug: management-create-company-api-credential-request
- name: CreateCompanyApiCredentialResponse
  property_count: 12
  slug: management-create-company-api-credential-response
- name: CreateCompanyUserRequest
  property_count: 7
  slug: management-create-company-user-request
- name: CreateCompanyUserResponse
  property_count: 11
  slug: management-create-company-user-response
- name: CreateCompanyWebhookRequest
  property_count: 16
  slug: management-create-company-webhook-request
- name: CreateMerchantApiCredentialRequest
  property_count: 3
  slug: management-create-merchant-api-credential-request
- name: CreateMerchantRequest
  property_count: 7
  slug: management-create-merchant-request
- name: CreateMerchantResponse
  property_count: 7
  slug: management-create-merchant-response
- name: CreateMerchantUserRequest
  property_count: 6
  slug: management-create-merchant-user-request
- name: CreateMerchantWebhookRequest
  property_count: 14
  slug: management-create-merchant-webhook-request
- name: CreateUserResponse
  property_count: 10
  slug: management-create-user-response
- name: Currency
  property_count: 3
  slug: management-currency
- name: CustomNotification
  property_count: 7
  slug: management-custom-notification
- name: DataCenter
  property_count: 2
  slug: management-data-center
- name: EventUrl
  property_count: 2
  slug: management-event-url
- name: ExternalTerminalAction
  property_count: 8
  slug: management-external-terminal-action
- name: File
  property_count: 2
  slug: management-file
- name: GenerateApiKeyResponse
  property_count: 1
  slug: management-generate-api-key-response
- name: GenerateClientKeyResponse
  property_count: 1
  slug: management-generate-client-key-response
- name: GenerateHmacKeyResponse
  property_count: 1
  slug: management-generate-hmac-key-response
- name: GenericPmWithTdiInfo
  property_count: 1
  slug: management-generic-pm-with-tdi-info
- name: GiroPayInfo
  property_count: 1
  slug: management-giro-pay-info
- name: GooglePayInfo
  property_count: 2
  slug: management-google-pay-info
- name: Gratuity
  property_count: 4
  slug: management-gratuity
- name: Hardware
  property_count: 3
  slug: management-hardware
- name: IdName
  property_count: 2
  slug: management-id-name
- name: InstallAndroidAppDetails
  property_count: 2
  slug: management-install-android-app-details
- name: InstallAndroidCertificateDetails
  property_count: 2
  slug: management-install-android-certificate-details
- name: InvalidField
  property_count: 3
  slug: management-invalid-field
- name: JSONObject
  property_count: 0
  slug: management-json-object
- name: Key
  property_count: 3
  slug: management-key
- name: KlarnaInfo
  property_count: 4
  slug: management-klarna-info
- name: LinksElement
  property_count: 1
  slug: management-links-element
- name: Links
  property_count: 1
  slug: management-links
- name: ListCompanyApiCredentialsResponse
  property_count: 4
  slug: management-list-company-api-credentials-response
- name: ListCompanyResponse
  property_count: 4
  slug: management-list-company-response
- name: ListCompanyUsersResponse
  property_count: 4
  slug: management-list-company-users-response
- name: ListExternalTerminalActionsResponse
  property_count: 1
  slug: management-list-external-terminal-actions-response
- name: ListMerchantApiCredentialsResponse
  property_count: 4
  slug: management-list-merchant-api-credentials-response
- name: ListMerchantResponse
  property_count: 4
  slug: management-list-merchant-response
- name: ListMerchantUsersResponse
  property_count: 4
  slug: management-list-merchant-users-response
- name: ListStoresResponse
  property_count: 4
  slug: management-list-stores-response
- name: ListTerminalsResponse
  property_count: 4
  slug: management-list-terminals-response
- name: ListWebhooksResponse
  property_count: 5
  slug: management-list-webhooks-response
- name: Localization
  property_count: 3
  slug: management-localization
- name: Logo
  property_count: 1
  slug: management-logo
- name: MeApiCredential
  property_count: 11
  slug: management-me-api-credential
- name: MealVoucherFRInfo
  property_count: 3
  slug: management-meal-voucher-fr-info
- name: MerchantLinks
  property_count: 4
  slug: management-merchant-links
- name: Merchant
  property_count: 14
  slug: management-merchant
- name: MinorUnitsMonetaryValue
  property_count: 2
  slug: management-minor-units-monetary-value
- name: Name
  property_count: 2
  slug: management-name
- name: Name2
  property_count: 2
  slug: management-name2
- name: Nexo
  property_count: 5
  slug: management-nexo
- name: Notification
  property_count: 5
  slug: management-notification
- name: NotificationUrl
  property_count: 2
  slug: management-notification-url
- name: OfflineProcessing
  property_count: 2
  slug: management-offline-processing
- name: Opi
  property_count: 3
  slug: management-opi
- name: OrderItem
  property_count: 4
  slug: management-order-item
- name: PaginationLinks
  property_count: 5
  slug: management-pagination-links
- name: Passcodes
  property_count: 4
  slug: management-passcodes
- name: PayAtTable
  property_count: 3
  slug: management-pay-at-table
- name: PayPalInfo
  property_count: 3
  slug: management-pay-pal-info
- name: PaymentMethodResponse
  property_count: 5
  slug: management-payment-method-response
- name: PaymentMethod
  property_count: 37
  slug: management-payment-method
- name: PaymentMethodSetupInfo
  property_count: 33
  slug: management-payment-method-setup-info
- name: Payment
  property_count: 2
  slug: management-payment
- name: PayoutSettingsRequest
  property_count: 3
  slug: management-payout-settings-request
- name: PayoutSettingsResponse
  property_count: 1
  slug: management-payout-settings-response
- name: PayoutSettings
  property_count: 7
  slug: management-payout-settings
- name: Profile
  property_count: 18
  slug: management-profile
- name: ReceiptOptions
  property_count: 3
  slug: management-receipt-options
- name: ReceiptPrinting
  property_count: 16
  slug: management-receipt-printing
- name: Referenced
  property_count: 1
  slug: management-referenced
- name: Refunds
  property_count: 1
  slug: management-refunds
- name: ReleaseUpdateDetails
  property_count: 2
  slug: management-release-update-details
- name: RequestActivationResponse
  property_count: 2
  slug: management-request-activation-response
- name: RestServiceError
  property_count: 9
  slug: management-rest-service-error
- name: ScheduleTerminalActionsRequest
  property_count: 4
  slug: management-schedule-terminal-actions-request
- name: ScheduleTerminalActionsResponse
  property_count: 7
  slug: management-schedule-terminal-actions-response
- name: Settings
  property_count: 3
  slug: management-settings
- name: ShippingLocation
  property_count: 4
  slug: management-shipping-location
- name: ShippingLocationsResponse
  property_count: 1
  slug: management-shipping-locations-response
- name: Signature
  property_count: 4
  slug: management-signature
- name: SofortInfo
  property_count: 2
  slug: management-sofort-info
- name: SplitConfigurationList
  property_count: 1
  slug: management-split-configuration-list
- name: SplitConfigurationLogic
  property_count: 15
  slug: management-split-configuration-logic
- name: SplitConfigurationRule
  property_count: 6
  slug: management-split-configuration-rule
- name: SplitConfiguration
  property_count: 4
  slug: management-split-configuration
- name: Standalone
  property_count: 2
  slug: management-standalone
- name: StoreCreationRequest
  property_count: 8
  slug: management-store-creation-request
- name: StoreCreationWithMerchantCodeRequest
  property_count: 9
  slug: management-store-creation-with-merchant-code-request
- name: StoreLocation
  property_count: 7
  slug: management-store-location
- name: Store
  property_count: 12
  slug: management-store
- name: StoreSplitConfiguration
  property_count: 2
  slug: management-store-split-configuration
- name: Surcharge
  property_count: 2
  slug: management-surcharge
- name: SwishInfo
  property_count: 1
  slug: management-swish-info
- name: TapToPay
  property_count: 1
  slug: management-tap-to-pay
- name: TerminalActionScheduleDetail
  property_count: 2
  slug: management-terminal-action-schedule-detail
- name: TerminalAssignment
  property_count: 5
  slug: management-terminal-assignment
- name: TerminalConnectivityBluetooth
  property_count: 2
  slug: management-terminal-connectivity-bluetooth
- name: TerminalConnectivityCellular
  property_count: 2
  slug: management-terminal-connectivity-cellular
- name: TerminalConnectivityEthernet
  property_count: 3
  slug: management-terminal-connectivity-ethernet
- name: TerminalConnectivity
  property_count: 4
  slug: management-terminal-connectivity
- name: TerminalConnectivityWifi
  property_count: 3
  slug: management-terminal-connectivity-wifi
- name: TerminalModelsResponse
  property_count: 1
  slug: management-terminal-models-response
- name: TerminalOrderRequest
  property_count: 6
  slug: management-terminal-order-request
- name: TerminalOrder
  property_count: 8
  slug: management-terminal-order
- name: TerminalOrdersResponse
  property_count: 1
  slug: management-terminal-orders-response
- name: TerminalProductPrice
  property_count: 2
  slug: management-terminal-product-price
- name: TerminalProduct
  property_count: 5
  slug: management-terminal-product
- name: TerminalProductsResponse
  property_count: 1
  slug: management-terminal-products-response
- name: TerminalReassignmentRequest
  property_count: 4
  slug: management-terminal-reassignment-request
- name: TerminalReassignmentTarget
  property_count: 4
  slug: management-terminal-reassignment-target
- name: Terminal
  property_count: 8
  slug: management-terminal
- name: TerminalSettings
  property_count: 20
  slug: management-terminal-settings
- name: TestCompanyWebhookRequest
  property_count: 3
  slug: management-test-company-webhook-request
- name: TestOutput
  property_count: 6
  slug: management-test-output
- name: TestWebhookRequest
  property_count: 2
  slug: management-test-webhook-request
- name: TestWebhookResponse
  property_count: 1
  slug: management-test-webhook-response
- name: Timeouts
  property_count: 1
  slug: management-timeouts
- name: TransactionDescriptionInfo
  property_count: 2
  slug: management-transaction-description-info
- name: TwintInfo
  property_count: 1
  slug: management-twint-info
- name: UninstallAndroidAppDetails
  property_count: 2
  slug: management-uninstall-android-app-details
- name: UninstallAndroidCertificateDetails
  property_count: 2
  slug: management-uninstall-android-certificate-details
- name: UpdatableAddress
  property_count: 6
  slug: management-updatable-address
- name: UpdateCompanyApiCredentialRequest
  property_count: 5
  slug: management-update-company-api-credential-request
- name: UpdateCompanyUserRequest
  property_count: 7
  slug: management-update-company-user-request
- name: UpdateCompanyWebhookRequest
  property_count: 15
  slug: management-update-company-webhook-request
- name: UpdateMerchantApiCredentialRequest
  property_count: 4
  slug: management-update-merchant-api-credential-request
- name: UpdateMerchantUserRequest
  property_count: 6
  slug: management-update-merchant-user-request
- name: UpdateMerchantWebhookRequest
  property_count: 13
  slug: management-update-merchant-webhook-request
- name: UpdatePaymentMethodInfo
  property_count: 18
  slug: management-update-payment-method-info
- name: UpdatePayoutSettingsRequest
  property_count: 1
  slug: management-update-payout-settings-request
- name: UpdateSplitConfigurationLogicRequest
  property_count: 15
  slug: management-update-split-configuration-logic-request
- name: UpdateSplitConfigurationRequest
  property_count: 1
  slug: management-update-split-configuration-request
- name: UpdateSplitConfigurationRuleRequest
  property_count: 4
  slug: management-update-split-configuration-rule-request
- name: UpdateStoreRequest
  property_count: 7
  slug: management-update-store-request
- name: UploadAndroidAppResponse
  property_count: 1
  slug: management-upload-android-app-response
- name: Url
  property_count: 4
  slug: management-url
- name: User
  property_count: 10
  slug: management-user
- name: VippsInfo
  property_count: 2
  slug: management-vipps-info
- name: WebhookLinks
  property_count: 5
  slug: management-webhook-links
- name: Webhook
  property_count: 22
  slug: management-webhook
- name: AccountCapabilityData
  property_count: 8
  slug: management-webhooks-account-capability-data
- name: AccountCreateNotificationData
  property_count: 5
  slug: management-webhooks-account-create-notification-data
- name: AccountNotificationResponse
  property_count: 1
  slug: management-webhooks-account-notification-response
- name: AccountUpdateNotificationData
  property_count: 4
  slug: management-webhooks-account-update-notification-data
- name: CapabilityProblemEntity-recursive
  property_count: 3
  slug: management-webhooks-capability-problem-entity-recursive
- name: CapabilityProblemEntity
  property_count: 4
  slug: management-webhooks-capability-problem-entity
- name: CapabilityProblem
  property_count: 2
  slug: management-webhooks-capability-problem
- name: MerchantCreatedNotificationRequest
  property_count: 4
  slug: management-webhooks-merchant-created-notification-request
- name: MerchantUpdatedNotificationRequest
  property_count: 4
  slug: management-webhooks-merchant-updated-notification-request
- name: MidServiceNotificationData
  property_count: 9
  slug: management-webhooks-mid-service-notification-data
- name: PaymentMethodCreatedNotificationRequest
  property_count: 4
  slug: management-webhooks-payment-method-created-notification-request
- name: PaymentMethodNotificationResponse
  property_count: 1
  slug: management-webhooks-payment-method-notification-response
- name: PaymentMethodRequestRemovedNotificationRequest
  property_count: 4
  slug: management-webhooks-payment-method-request-removed-notification-request
- name: PaymentMethodScheduledForRemovalNotificationRequest
  property_count: 4
  slug: management-webhooks-payment-method-scheduled-for-removal-notification-request
- name: RemediatingAction
  property_count: 2
  slug: management-webhooks-remediating-action
- name: VerificationError-recursive
  property_count: 4
  slug: management-webhooks-verification-error-recursive
- name: VerificationError
  property_count: 5
  slug: management-webhooks-verification-error
- name: WifiProfiles
  property_count: 2
  slug: management-wifi-profiles
- name: CreateNotificationConfigurationRequest
  property_count: 1
  slug: notification-configurations-create-notification-configuration-request
- name: DeleteNotificationConfigurationRequest
  property_count: 1
  slug: notification-configurations-delete-notification-configuration-request
- name: EmptyRequest
  property_count: 0
  slug: notification-configurations-empty-request
- name: ErrorFieldType
  property_count: 3
  slug: notification-configurations-error-field-type
- name: ExchangeMessage
  property_count: 2
  slug: notification-configurations-exchange-message
- name: FieldType
  property_count: 3
  slug: notification-configurations-field-type
- name: GenericResponse
  property_count: 3
  slug: notification-configurations-generic-response
- name: GetNotificationConfigurationListResponse
  property_count: 4
  slug: notification-configurations-get-notification-configuration-list-response
- name: GetNotificationConfigurationRequest
  property_count: 1
  slug: notification-configurations-get-notification-configuration-request
- name: GetNotificationConfigurationResponse
  property_count: 4
  slug: notification-configurations-get-notification-configuration-response
- name: NotificationConfigurationDetails
  property_count: 10
  slug: notification-configurations-notification-configuration-details
- name: NotificationEventConfiguration
  property_count: 2
  slug: notification-configurations-notification-event-configuration
- name: TestNotificationConfigurationRequest
  property_count: 2
  slug: notification-configurations-test-notification-configuration-request
- name: TestNotificationConfigurationResponse
  property_count: 8
  slug: notification-configurations-test-notification-configuration-response
- name: UpdateNotificationConfigurationRequest
  property_count: 1
  slug: notification-configurations-update-notification-configuration-request
- name: AccountHolderCapability
  property_count: 9
  slug: notification-webhooks-account-holder-capability
- name: AccountHolderNotificationData
  property_count: 2
  slug: notification-webhooks-account-holder-notification-data
- name: AccountHolderNotificationRequest
  property_count: 3
  slug: notification-webhooks-account-holder-notification-request
- name: AccountHolder
  property_count: 10
  slug: notification-webhooks-account-holder
- name: Address
  property_count: 6
  slug: notification-webhooks-address
- name: Amount
  property_count: 2
  slug: notification-webhooks-amount
- name: Authentication
  property_count: 3
  slug: notification-webhooks-authentication
- name: BalanceAccountNotificationData
  property_count: 2
  slug: notification-webhooks-balance-account-notification-data
- name: BalanceAccountNotificationRequest
  property_count: 3
  slug: notification-webhooks-balance-account-notification-request
- name: BalanceAccount
  property_count: 10
  slug: notification-webhooks-balance-account
- name: BalancePlatformNotificationResponse
  property_count: 1
  slug: notification-webhooks-balance-platform-notification-response
- name: Balance
  property_count: 4
  slug: notification-webhooks-balance
- name: BankAccountInfo
  property_count: 3
  slug: notification-webhooks-bank-account-info
- name: BankAccount
  property_count: 1
  slug: notification-webhooks-bank-account
- name: BulkAddress
  property_count: 9
  slug: notification-webhooks-bulk-address
- name: CapabilityProblemEntity-recursive
  property_count: 2
  slug: notification-webhooks-capability-problem-entity-recursive
- name: CapabilityProblemEntity
  property_count: 3
  slug: notification-webhooks-capability-problem-entity
- name: CapabilityProblem
  property_count: 2
  slug: notification-webhooks-capability-problem
- name: CardConfiguration
  property_count: 14
  slug: notification-webhooks-card-configuration
- name: Card
  property_count: 12
  slug: notification-webhooks-card
- name: ContactDetails
  property_count: 4
  slug: notification-webhooks-contact-details
- name: Contact
  property_count: 7
  slug: notification-webhooks-contact
- name: Counterparty
  property_count: 4
  slug: notification-webhooks-counterparty
- name: CronSweepSchedule
  property_count: 2
  slug: notification-webhooks-cron-sweep-schedule
- name: Expiry
  property_count: 2
  slug: notification-webhooks-expiry
- name: IncomingTransferNotificationData
  property_count: 17
  slug: notification-webhooks-incoming-transfer-notification-data
- name: IncomingTransferNotificationRequest
  property_count: 3
  slug: notification-webhooks-incoming-transfer-notification-request
- name: JSONObject
  property_count: 2
  slug: notification-webhooks-json-object
- name: JSONPath
  property_count: 1
  slug: notification-webhooks-json-path
- name: MerchantData
  property_count: 4
  slug: notification-webhooks-merchant-data
- name: Name-2
  property_count: 4
  slug: notification-webhooks-name-2
- name: NameLocation
  property_count: 6
  slug: notification-webhooks-name-location
- name: Name
  property_count: 2
  slug: notification-webhooks-name
- name: NotificationModificationData
  property_count: 2
  slug: notification-webhooks-notification-modification-data
- name: OutgoingTransferNotificationData
  property_count: 22
  slug: notification-webhooks-outgoing-transfer-notification-data
- name: OutgoingTransferNotificationRequest
  property_count: 3
  slug: notification-webhooks-outgoing-transfer-notification-request
- name: PaymentInstrumentNotificationData
  property_count: 2
  slug: notification-webhooks-payment-instrument-notification-data
- name: PaymentInstrumentReference
  property_count: 1
  slug: notification-webhooks-payment-instrument-reference
- name: PaymentInstrument
  property_count: 10
  slug: notification-webhooks-payment-instrument
- name: PaymentNotificationData
  property_count: 20
  slug: notification-webhooks-payment-notification-data
- name: PaymentNotificationRequest-2
  property_count: 3
  slug: notification-webhooks-payment-notification-request-2
- name: PaymentNotificationRequest
  property_count: 3
  slug: notification-webhooks-payment-notification-request
- name: PersonalData
  property_count: 3
  slug: notification-webhooks-personal-data
- name: PhoneNumber
  property_count: 3
  slug: notification-webhooks-phone-number
- name: Phone
  property_count: 2
  slug: notification-webhooks-phone
- name: PlatformPayment
  property_count: 8
  slug: notification-webhooks-platform-payment
- name: RelayedAuthorisationData
  property_count: 3
  slug: notification-webhooks-relayed-authorisation-data
- name: RemediatingAction
  property_count: 2
  slug: notification-webhooks-remediating-action
- name: ReportNotificationData
  property_count: 7
  slug: notification-webhooks-report-notification-data
- name: ReportNotificationRequest
  property_count: 3
  slug: notification-webhooks-report-notification-request
- name: ResourceReference
  property_count: 3
  slug: notification-webhooks-resource-reference
- name: Resource
  property_count: 3
  slug: notification-webhooks-resource
- name: SweepConfigurationNotificationData
  property_count: 3
  slug: notification-webhooks-sweep-configuration-notification-data
- name: SweepConfigurationNotificationRequest
  property_count: 3
  slug: notification-webhooks-sweep-configuration-notification-request
- name: SweepConfiguration
  property_count: 10
  slug: notification-webhooks-sweep-configuration
- name: SweepConfigurationV2
  property_count: 10
  slug: notification-webhooks-sweep-configuration-v2
- name: SweepCounterparty
  property_count: 3
  slug: notification-webhooks-sweep-counterparty
- name: SweepSchedule
  property_count: 1
  slug: notification-webhooks-sweep-schedule
- name: TransactionEventViolation
  property_count: 3
  slug: notification-webhooks-transaction-event-violation
- name: TransactionNotificationData
  property_count: 24
  slug: notification-webhooks-transaction-notification-data
- name: TransactionRuleSource
  property_count: 2
  slug: notification-webhooks-transaction-rule-source
- name: TransactionRulesResult
  property_count: 2
  slug: notification-webhooks-transaction-rules-result
- name: ValidationResult
  property_count: 2
  slug: notification-webhooks-validation-result
- name: VerificationError-recursive
  property_count: 4
  slug: notification-webhooks-verification-error-recursive
- name: VerificationError
  property_count: 5
  slug: notification-webhooks-verification-error
- name: AccountCloseNotification
  property_count: 7
  slug: notifications-account-close-notification
- name: AccountCreateNotification
  property_count: 7
  slug: notifications-account-create-notification
- name: AccountEvent
  property_count: 3
  slug: notifications-account-event
- name: AccountFundsBelowThresholdNotificationContent
  property_count: 5
  slug: notifications-account-funds-below-threshold-notification-content
- name: AccountFundsBelowThresholdNotification
  property_count: 7
  slug: notifications-account-funds-below-threshold-notification
- name: AccountHolderCreateNotification
  property_count: 7
  slug: notifications-account-holder-create-notification
- name: AccountHolderDetails
  property_count: 15
  slug: notifications-account-holder-details
- name: AccountHolderPayoutNotificationContent
  property_count: 17
  slug: notifications-account-holder-payout-notification-content
- name: AccountHolderPayoutNotification
  property_count: 7
  slug: notifications-account-holder-payout-notification
- name: AccountHolderStatusChangeNotificationContent
  property_count: 5
  slug: notifications-account-holder-status-change-notification-content
- name: AccountHolderStatusChangeNotification
  property_count: 7
  slug: notifications-account-holder-status-change-notification
- name: AccountHolderStatus
  property_count: 5
  slug: notifications-account-holder-status
- name: AccountHolderStoreStatusChangeNotificationContent
  property_count: 7
  slug: notifications-account-holder-store-status-change-notification-content
- name: AccountHolderStoreStatusChangeNotification
  property_count: 7
  slug: notifications-account-holder-store-status-change-notification
- name: AccountHolderUpcomingDeadlineNotificationContent
  property_count: 4
  slug: notifications-account-holder-upcoming-deadline-notification-content
- name: AccountHolderUpcomingDeadlineNotification
  property_count: 7
  slug: notifications-account-holder-upcoming-deadline-notification
- name: AccountHolderUpdateNotification
  property_count: 7
  slug: notifications-account-holder-update-notification
- name: AccountHolderVerificationNotificationContent
  property_count: 7
  slug: notifications-account-holder-verification-notification-content
- name: AccountHolderVerificationNotification
  property_count: 7
  slug: notifications-account-holder-verification-notification
- name: AccountPayoutState
  property_count: 6
  slug: notifications-account-payout-state
- name: AccountProcessingState
  property_count: 5
  slug: notifications-account-processing-state
- name: AccountUpdateNotification
  property_count: 7
  slug: notifications-account-update-notification
- name: Amount
  property_count: 2
  slug: notifications-amount
- name: BankAccountDetail
  property_count: 26
  slug: notifications-bank-account-detail
- name: BeneficiarySetupNotificationContent
  property_count: 7
  slug: notifications-beneficiary-setup-notification-content
- name: BeneficiarySetupNotification
  property_count: 7
  slug: notifications-beneficiary-setup-notification
- name: BusinessDetails
  property_count: 10
  slug: notifications-business-details
- name: CloseAccountResponse
  property_count: 5
  slug: notifications-close-account-response
- name: CompensateNegativeBalanceNotificationContent
  property_count: 1
  slug: notifications-compensate-negative-balance-notification-content
- name: CompensateNegativeBalanceNotificationRecord
  property_count: 3
  slug: notifications-compensate-negative-balance-notification-record
- name: CompensateNegativeBalanceNotification
  property_count: 7
  slug: notifications-compensate-negative-balance-notification
- name: CreateAccountHolderResponse
  property_count: 12
  slug: notifications-create-account-holder-response
- name: CreateAccountResponse
  property_count: 12
  slug: notifications-create-account-response
- name: DirectDebitInitiatedNotificationContent
  property_count: 7
  slug: notifications-direct-debit-initiated-notification-content
- name: DirectDebitInitiatedNotification
  property_count: 7
  slug: notifications-direct-debit-initiated-notification
- name: ErrorFieldType
  property_count: 3
  slug: notifications-error-field-type
- name: FieldType
  property_count: 3
  slug: notifications-field-type
- name: IndividualDetails
  property_count: 2
  slug: notifications-individual-details
- name: KYCCheckResult
  property_count: 1
  slug: notifications-kyc-check-result
- name: KYCCheckStatusData
  property_count: 4
  slug: notifications-kyc-check-status-data
- name: KYCCheckSummary
  property_count: 2
  slug: notifications-kyc-check-summary
- name: KYCLegalArrangementCheckResult
  property_count: 2
  slug: notifications-kyc-legal-arrangement-check-result
- name: KYCLegalArrangementEntityCheckResult
  property_count: 3
  slug: notifications-kyc-legal-arrangement-entity-check-result
- name: KYCPayoutMethodCheckResult
  property_count: 2
  slug: notifications-kyc-payout-method-check-result
- name: KYCShareholderCheckResult
  property_count: 4
  slug: notifications-kyc-shareholder-check-result
- name: KYCSignatoryCheckResult
  property_count: 2
  slug: notifications-kyc-signatory-check-result
- name: KYCUltimateParentCompanyCheckResult
  property_count: 2
  slug: notifications-kyc-ultimate-parent-company-check-result
- name: KYCVerificationResult
  property_count: 7
  slug: notifications-kyc-verification-result
- name: LegalArrangementDetail
  property_count: 9
  slug: notifications-legal-arrangement-detail
- name: LegalArrangementEntityDetail
  property_count: 11
  slug: notifications-legal-arrangement-entity-detail
- name: LocalDate
  property_count: 2
  slug: notifications-local-date
- name: Message
  property_count: 2
  slug: notifications-message
- name: NotificationErrorContainer
  property_count: 2
  slug: notifications-notification-error-container
- name: NotificationResponse
  property_count: 1
  slug: notifications-notification-response
- name: OperationStatus
  property_count: 2
  slug: notifications-operation-status
- name: PaymentFailureNotificationContent
  property_count: 6
  slug: notifications-payment-failure-notification-content
- name: PaymentFailureNotification
  property_count: 7
  slug: notifications-payment-failure-notification
- name: PayoutMethod
  property_count: 5
  slug: notifications-payout-method
- name: PayoutScheduleResponse
  property_count: 2
  slug: notifications-payout-schedule-response
- name: PersonalDocumentData
  property_count: 5
  slug: notifications-personal-document-data
- name: RefundFundsTransferNotificationContent
  property_count: 5
  slug: notifications-refund-funds-transfer-notification-content
- name: RefundFundsTransferNotification
  property_count: 7
  slug: notifications-refund-funds-transfer-notification
- name: RefundResult
  property_count: 3
  slug: notifications-refund-result
- name: ReportAvailableNotificationContent
  property_count: 5
  slug: notifications-report-available-notification-content
- name: ReportAvailableNotification
  property_count: 7
  slug: notifications-report-available-notification
- name: ScheduledRefundsNotificationContent
  property_count: 5
  slug: notifications-scheduled-refunds-notification-content
- name: ScheduledRefundsNotification
  property_count: 7
  slug: notifications-scheduled-refunds-notification
- name: ShareholderContact
  property_count: 11
  slug: notifications-shareholder-contact
- name: SignatoryContact
  property_count: 10
  slug: notifications-signatory-contact
- name: SplitAmount
  property_count: 2
  slug: notifications-split-amount
- name: Split
  property_count: 5
  slug: notifications-split
- name: StoreDetail
  property_count: 15
  slug: notifications-store-detail
- name: Transaction
  property_count: 16
  slug: notifications-transaction
- name: TransferFundsNotificationContent
  property_count: 7
  slug: notifications-transfer-funds-notification-content
- name: TransferFundsNotification
  property_count: 7
  slug: notifications-transfer-funds-notification
- name: UltimateParentCompanyBusinessDetails
  property_count: 5
  slug: notifications-ultimate-parent-company-business-details
- name: UltimateParentCompany
  property_count: 3
  slug: notifications-ultimate-parent-company
- name: UpdateAccountHolderResponse
  property_count: 11
  slug: notifications-update-account-holder-response
- name: UpdateAccountResponse
  property_count: 10
  slug: notifications-update-account-response
- name: ViasAddress
  property_count: 6
  slug: notifications-vias-address
- name: ViasName
  property_count: 4
  slug: notifications-vias-name
- name: ViasPersonalData
  property_count: 3
  slug: notifications-vias-personal-data
- name: ViasPhoneNumber
  property_count: 3
  slug: notifications-vias-phone-number
- name: AccountInfo
  property_count: 19
  slug: payments-account-info
- name: AcctInfo
  property_count: 16
  slug: payments-acct-info
- name: AdditionalDataAirline
  property_count: 28
  slug: payments-additional-data-airline
- name: AdditionalDataCarRental
  property_count: 23
  slug: payments-additional-data-car-rental
- name: AdditionalDataCommon
  property_count: 16
  slug: payments-additional-data-common
- name: AdditionalDataLevel23
  property_count: 17
  slug: payments-additional-data-level23
- name: AdditionalDataLodging
  property_count: 16
  slug: payments-additional-data-lodging
- name: AdditionalDataModifications
  property_count: 1
  slug: payments-additional-data-modifications
- name: AdditionalDataOpenInvoice
  property_count: 18
  slug: payments-additional-data-open-invoice
- name: AdditionalDataOpi
  property_count: 1
  slug: payments-additional-data-opi
- name: AdditionalDataRatepay
  property_count: 8
  slug: payments-additional-data-ratepay
- name: AdditionalDataRetry
  property_count: 3
  slug: payments-additional-data-retry
- name: AdditionalDataRisk
  property_count: 21
  slug: payments-additional-data-risk
- name: AdditionalDataRiskStandalone
  property_count: 15
  slug: payments-additional-data-risk-standalone
- name: AdditionalDataSubMerchant
  property_count: 10
  slug: payments-additional-data-sub-merchant
- name: AdditionalDataTemporaryServices
  property_count: 9
  slug: payments-additional-data-temporary-services
- name: AdditionalDataWallets
  property_count: 6
  slug: payments-additional-data-wallets
- name: AdditionalData3DSecure
  property_count: 6
  slug: payments-additional-data3-d-secure
- name: Address
  property_count: 6
  slug: payments-address
- name: AdjustAuthorisationRequest
  property_count: 11
  slug: payments-adjust-authorisation-request
- name: Amount
  property_count: 2
  slug: payments-amount
- name: ApplicationInfo
  property_count: 6
  slug: payments-application-info
- name: AuthenticationResultRequest
  property_count: 2
  slug: payments-authentication-result-request
- name: AuthenticationResultResponse
  property_count: 2
  slug: payments-authentication-result-response
- name: BankAccount
  property_count: 9
  slug: payments-bank-account
- name: BrowserInfo
  property_count: 9
  slug: payments-browser-info
- name: CancelOrRefundRequest
  property_count: 9
  slug: payments-cancel-or-refund-request
- name: CancelRequest
  property_count: 10
  slug: payments-cancel-request
- name: CaptureRequest
  property_count: 11
  slug: payments-capture-request
- name: Card
  property_count: 8
  slug: payments-card
- name: CommonField
  property_count: 2
  slug: payments-common-field
- name: DeviceRenderOptions
  property_count: 2
  slug: payments-device-render-options
- name: DonationRequest
  property_count: 6
  slug: payments-donation-request
- name: ExternalPlatform
  property_count: 3
  slug: payments-external-platform
- name: ForexQuote
  property_count: 12
  slug: payments-forex-quote
- name: FraudCheckResult
  property_count: 3
  slug: payments-fraud-check-result
- name: FraudCheckResultWrapper
  property_count: 1
  slug: payments-fraud-check-result-wrapper
- name: FraudResult
  property_count: 2
  slug: payments-fraud-result
- name: FundDestination
  property_count: 9
  slug: payments-fund-destination
- name: FundSource
  property_count: 6
  slug: payments-fund-source
- name: Installments
  property_count: 2
  slug: payments-installments
- name: Mandate
  property_count: 8
  slug: payments-mandate
- name: MerchantDevice
  property_count: 3
  slug: payments-merchant-device
- name: MerchantRiskIndicator
  property_count: 14
  slug: payments-merchant-risk-indicator
- name: ModificationResult
  property_count: 3
  slug: payments-modification-result
- name: Name
  property_count: 2
  slug: payments-name
- name: PaymentRequest
  property_count: 53
  slug: payments-payment-request
- name: PaymentRequest3d
  property_count: 45
  slug: payments-payment-request3d
- name: PaymentRequest3ds2
  property_count: 45
  slug: payments-payment-request3ds2
- name: PaymentResult
  property_count: 11
  slug: payments-payment-result
- name: Phone
  property_count: 2
  slug: payments-phone
- name: PlatformChargebackLogic
  property_count: 3
  slug: payments-platform-chargeback-logic
- name: Recurring
  property_count: 5
  slug: payments-recurring
- name: RefundRequest
  property_count: 11
  slug: payments-refund-request
- name: ResponseAdditionalDataBillingAddress
  property_count: 6
  slug: payments-response-additional-data-billing-address
- name: ResponseAdditionalDataCard
  property_count: 8
  slug: payments-response-additional-data-card
- name: ResponseAdditionalDataCommon
  property_count: 59
  slug: payments-response-additional-data-common
- name: ResponseAdditionalDataDomesticError
  property_count: 2
  slug: payments-response-additional-data-domestic-error
- name: ResponseAdditionalDataInstallments
  property_count: 12
  slug: payments-response-additional-data-installments
- name: ResponseAdditionalDataNetworkTokens
  property_count: 3
  slug: payments-response-additional-data-network-tokens
- name: ResponseAdditionalDataOpi
  property_count: 1
  slug: payments-response-additional-data-opi
- name: ResponseAdditionalDataSepa
  property_count: 3
  slug: payments-response-additional-data-sepa
- name: ResponseAdditionalData3DSecure
  property_count: 5
  slug: payments-response-additional-data3-d-secure
- name: SDKEphemPubKey
  property_count: 4
  slug: payments-sdk-ephem-pub-key
- name: ShopperInteractionDevice
  property_count: 3
  slug: payments-shopper-interaction-device
- name: SplitAmount
  property_count: 2
  slug: payments-split-amount
- name: Split
  property_count: 5
  slug: payments-split
- name: SubMerchant
  property_count: 5
  slug: payments-sub-merchant
- name: TechnicalCancelRequest
  property_count: 10
  slug: payments-technical-cancel-request
- name: ThreeDSecureData
  property_count: 12
  slug: payments-three-d-secure-data
- name: ThreeDSRequestorAuthenticationInfo
  property_count: 3
  slug: payments-three-ds-requestor-authentication-info
- name: ThreeDSRequestorPriorAuthenticationInfo
  property_count: 4
  slug: payments-three-ds-requestor-prior-authentication-info
- name: ThreeDS1Result
  property_count: 6
  slug: payments-three-ds1-result
- name: ThreeDS2RequestData
  property_count: 39
  slug: payments-three-ds2-request-data
- name: ThreeDS2ResultRequest
  property_count: 2
  slug: payments-three-ds2-result-request
- name: ThreeDS2ResultResponse
  property_count: 1
  slug: payments-three-ds2-result-response
- name: ThreeDS2Result
  property_count: 14
  slug: payments-three-ds2-result
- name: VoidPendingRefundRequest
  property_count: 11
  slug: payments-void-pending-refund-request
- name: Address
  property_count: 6
  slug: payouts-address
- name: Amount
  property_count: 2
  slug: payouts-amount
- name: BankAccount
  property_count: 9
  slug: payouts-bank-account
- name: Card
  property_count: 8
  slug: payouts-card
- name: FraudCheckResult
  property_count: 3
  slug: payouts-fraud-check-result
- name: FraudCheckResultWrapper
  property_count: 1
  slug: payouts-fraud-check-result-wrapper
- name: FraudResult
  property_count: 2
  slug: payouts-fraud-result
- name: FundSource
  property_count: 6
  slug: payouts-fund-source
- name: ModifyRequest
  property_count: 3
  slug: payouts-modify-request
- name: ModifyResponse
  property_count: 3
  slug: payouts-modify-response
- name: Name
  property_count: 2
  slug: payouts-name
- name: PayoutRequest
  property_count: 14
  slug: payouts-payout-request
- name: PayoutResponse
  property_count: 11
  slug: payouts-payout-response
- name: Recurring
  property_count: 5
  slug: payouts-recurring
- name: ResponseAdditionalDataBillingAddress
  property_count: 6
  slug: payouts-response-additional-data-billing-address
- name: ResponseAdditionalDataCard
  property_count: 8
  slug: payouts-response-additional-data-card
- name: ResponseAdditionalDataCommon
  property_count: 59
  slug: payouts-response-additional-data-common
- name: ResponseAdditionalDataDomesticError
  property_count: 2
  slug: payouts-response-additional-data-domestic-error
- name: ResponseAdditionalDataInstallments
  property_count: 12
  slug: payouts-response-additional-data-installments
- name: ResponseAdditionalDataNetworkTokens
  property_count: 3
  slug: payouts-response-additional-data-network-tokens
- name: ResponseAdditionalDataOpi
  property_count: 1
  slug: payouts-response-additional-data-opi
- name: ResponseAdditionalDataSepa
  property_count: 3
  slug: payouts-response-additional-data-sepa
- name: ResponseAdditionalData3DSecure
  property_count: 5
  slug: payouts-response-additional-data3-d-secure
- name: StoreDetailAndSubmitRequest
  property_count: 19
  slug: payouts-store-detail-and-submit-request
- name: StoreDetailAndSubmitResponse
  property_count: 4
  slug: payouts-store-detail-and-submit-response
- name: StoreDetailRequest
  property_count: 16
  slug: payouts-store-detail-request
- name: StoreDetailResponse
  property_count: 4
  slug: payouts-store-detail-response
- name: SubmitRequest
  property_count: 15
  slug: payouts-submit-request
- name: SubmitResponse
  property_count: 4
  slug: payouts-submit-response
- name: Address
  property_count: 6
  slug: pos-terminal-address
- name: AssignTerminalsRequest
  property_count: 5
  slug: pos-terminal-assign-terminals-request
- name: AssignTerminalsResponse
  property_count: 1
  slug: pos-terminal-assign-terminals-response
- name: FindTerminalRequest
  property_count: 1
  slug: pos-terminal-find-terminal-request
- name: FindTerminalResponse
  property_count: 5
  slug: pos-terminal-find-terminal-response
- name: GetStoresUnderAccountRequest
  property_count: 2
  slug: pos-terminal-get-stores-under-account-request
- name: GetStoresUnderAccountResponse
  property_count: 1
  slug: pos-terminal-get-stores-under-account-response
- name: GetTerminalDetailsRequest
  property_count: 1
  slug: pos-terminal-get-terminal-details-request
- name: GetTerminalDetailsResponse
  property_count: 25
  slug: pos-terminal-get-terminal-details-response
- name: GetTerminalsUnderAccountRequest
  property_count: 3
  slug: pos-terminal-get-terminals-under-account-request
- name: GetTerminalsUnderAccountResponse
  property_count: 3
  slug: pos-terminal-get-terminals-under-account-response
- name: MerchantAccount
  property_count: 4
  slug: pos-terminal-merchant-account
- name: Store
  property_count: 6
  slug: pos-terminal-store
- name: Address
  property_count: 6
  slug: recurring-address
- name: Amount
  property_count: 2
  slug: recurring-amount
- name: BankAccount
  property_count: 9
  slug: recurring-bank-account
- name: Card
  property_count: 8
  slug: recurring-card
- name: CreatePermitRequest
  property_count: 4
  slug: recurring-create-permit-request
- name: CreatePermitResult
  property_count: 2
  slug: recurring-create-permit-result
- name: DisablePermitRequest
  property_count: 2
  slug: recurring-disable-permit-request
- name: DisablePermitResult
  property_count: 2
  slug: recurring-disable-permit-result
- name: DisableRequest
  property_count: 4
  slug: recurring-disable-request
- name: DisableResult
  property_count: 1
  slug: recurring-disable-result
- name: Name
  property_count: 2
  slug: recurring-name
- name: NotifyShopperRequest
  property_count: 9
  slug: recurring-notify-shopper-request
- name: NotifyShopperResult
  property_count: 7
  slug: recurring-notify-shopper-result
- name: PermitRestriction
  property_count: 3
  slug: recurring-permit-restriction
- name: PermitResult
  property_count: 2
  slug: recurring-permit-result
- name: Permit
  property_count: 5
  slug: recurring-permit
- name: RecurringDetail
  property_count: 17
  slug: recurring-recurring-detail
- name: RecurringDetailWrapper
  property_count: 1
  slug: recurring-recurring-detail-wrapper
- name: RecurringDetailsRequest
  property_count: 3
  slug: recurring-recurring-details-request
- name: RecurringDetailsResult
  property_count: 4
  slug: recurring-recurring-details-result
- name: Recurring
  property_count: 5
  slug: recurring-recurring
- name: ScheduleAccountUpdaterRequest
  property_count: 6
  slug: recurring-schedule-account-updater-request
- name: ScheduleAccountUpdaterResult
  property_count: 2
  slug: recurring-schedule-account-updater-result
- name: TokenDetails
  property_count: 2
  slug: recurring-token-details
- name: BalancePlatformNotificationResponse
  property_count: 1
  slug: report-webhooks-balance-platform-notification-response
- name: ReportNotificationData
  property_count: 7
  slug: report-webhooks-report-notification-data
- name: ReportNotificationRequest
  property_count: 3
  slug: report-webhooks-report-notification-request
- name: ResourceReference
  property_count: 3
  slug: report-webhooks-resource-reference
- name: Resource
  property_count: 3
  slug: report-webhooks-resource
- name: Amount
  property_count: 2
  slug: stored-value-amount
- name: StoredValueBalanceCheckRequest
  property_count: 8
  slug: stored-value-stored-value-balance-check-request
- name: StoredValueBalanceCheckResponse
  property_count: 5
  slug: stored-value-stored-value-balance-check-response
- name: StoredValueBalanceMergeRequest
  property_count: 9
  slug: stored-value-stored-value-balance-merge-request
- name: StoredValueBalanceMergeResponse
  property_count: 6
  slug: stored-value-stored-value-balance-merge-response
- name: StoredValueIssueRequest
  property_count: 8
  slug: stored-value-stored-value-issue-request
- name: StoredValueIssueResponse
  property_count: 7
  slug: stored-value-stored-value-issue-response
- name: StoredValueLoadRequest
  property_count: 9
  slug: stored-value-stored-value-load-request
- name: StoredValueLoadResponse
  property_count: 6
  slug: stored-value-stored-value-load-response
- name: StoredValueStatusChangeRequest
  property_count: 9
  slug: stored-value-stored-value-status-change-request
- name: StoredValueStatusChangeResponse
  property_count: 6
  slug: stored-value-stored-value-status-change-response
- name: StoredValueVoidRequest
  property_count: 6
  slug: stored-value-stored-value-void-request
- name: StoredValueVoidResponse
  property_count: 5
  slug: stored-value-stored-value-void-response
- name: AbortRequest
  property_count: 3
  slug: terminal-abort-request
- name: AccountType
  property_count: 0
  slug: terminal-account-type
- name: AdminRequest
  property_count: 1
  slug: terminal-admin-request
- name: AdminResponse
  property_count: 1
  slug: terminal-admin-response
- name: Alignment
  property_count: 0
  slug: terminal-alignment
- name: AllowedProduct
  property_count: 4
  slug: terminal-allowed-product
- name: AmountsReq
  property_count: 8
  slug: terminal-amounts-req
- name: AmountsResp
  property_count: 6
  slug: terminal-amounts-resp
- name: AreaSize
  property_count: 2
  slug: terminal-area-size
- name: AuthenticationMethod
  property_count: 0
  slug: terminal-authentication-method
- name: BalanceInquiryRequest
  property_count: 2
  slug: terminal-balance-inquiry-request
- name: BalanceInquiryResponse
  property_count: 4
  slug: terminal-balance-inquiry-response
- name: BarcodeType
  property_count: 0
  slug: terminal-barcode-type
- name: CapturedSignature
  property_count: 2
  slug: terminal-captured-signature
- name: CardAcquisitionRequest
  property_count: 2
  slug: terminal-card-acquisition-request
- name: CardAcquisitionResponse
  property_count: 7
  slug: terminal-card-acquisition-response
- name: CardAcquisitionTransaction
  property_count: 9
  slug: terminal-card-acquisition-transaction
- name: CardData
  property_count: 11
  slug: terminal-card-data
- name: CardHolderPIN
  property_count: 3
  slug: terminal-card-holder-pin
- name: CardReaderAPDURequest
  property_count: 6
  slug: terminal-card-reader-apdu-request
- name: CardReaderAPDUResponse
  property_count: 3
  slug: terminal-card-reader-apdu-response
- name: CashHandlingDevice
  property_count: 3
  slug: terminal-cash-handling-device
- name: CharacterHeight
  property_count: 0
  slug: terminal-character-height
- name: CharacterStyle
  property_count: 0
  slug: terminal-character-style
- name: CharacterWidth
  property_count: 0
  slug: terminal-character-width
- name: CheckData
  property_count: 7
  slug: terminal-check-data
- name: CoinsOrBills
  property_count: 2
  slug: terminal-coins-or-bills
- name: Color
  property_count: 0
  slug: terminal-color
- name: ConvertedAmount
  property_count: 2
  slug: terminal-converted-amount
- name: CurrencyConversion
  property_count: 6
  slug: terminal-currency-conversion
- name: CustomerOrderReq
  property_count: 0
  slug: terminal-customer-order-req
- name: CustomerOrder
  property_count: 10
  slug: terminal-customer-order
- name: Device
  property_count: 0
  slug: terminal-device
- name: DiagnosisRequest
  property_count: 3
  slug: terminal-diagnosis-request
- name: DiagnosisResponse
  property_count: 4
  slug: terminal-diagnosis-response
- name: DisplayOutput
  property_count: 7
  slug: terminal-display-output
- name: DisplayRequest
  property_count: 1
  slug: terminal-display-request
- name: DisplayResponse
  property_count: 1
  slug: terminal-display-response
- name: DocumentQualifier
  property_count: 0
  slug: terminal-document-qualifier
- name: EnableServiceRequest
  property_count: 3
  slug: terminal-enable-service-request
- name: EnableServiceResponse
  property_count: 1
  slug: terminal-enable-service-response
- name: EntryMode
  property_count: 0
  slug: terminal-entry-mode
- name: ErrorCondition
  property_count: 0
  slug: terminal-error-condition
- name: EventNotification
  property_count: 7
  slug: terminal-event-notification
- name: EventToNotify
  property_count: 0
  slug: terminal-event-to-notify
- name: ForceEntryMode
  property_count: 0
  slug: terminal-force-entry-mode
- name: GenericProfile
  property_count: 0
  slug: terminal-generic-profile
- name: GeographicCoordinates
  property_count: 2
  slug: terminal-geographic-coordinates
- name: Geolocation
  property_count: 2
  slug: terminal-geolocation
- name: GetTotalsRequest
  property_count: 2
  slug: terminal-get-totals-request
- name: GetTotalsResponse
  property_count: 3
  slug: terminal-get-totals-response
- name: GlobalStatus
  property_count: 0
  slug: terminal-global-status
- name: HostStatus
  property_count: 2
  slug: terminal-host-status
- name: ICCResetData
  property_count: 2
  slug: terminal-icc-reset-data
- name: IdentificationSupport
  property_count: 0
  slug: terminal-identification-support
- name: IdentificationType
  property_count: 0
  slug: terminal-identification-type
- name: InfoQualify
  property_count: 0
  slug: terminal-info-qualify
- name: InputCommand
  property_count: 0
  slug: terminal-input-command
- name: InputData
  property_count: 21
  slug: terminal-input-data
- name: InputRequest
  property_count: 2
  slug: terminal-input-request
- name: InputResponse
  property_count: 2
  slug: terminal-input-response
- name: InputResult
  property_count: 4
  slug: terminal-input-result
- name: Input
  property_count: 7
  slug: terminal-input
- name: InputUpdate
  property_count: 7
  slug: terminal-input-update
- name: Instalment
  property_count: 10
  slug: terminal-instalment
- name: InstalmentType
  property_count: 0
  slug: terminal-instalment-type
- name: LoginRequest
  property_count: 10
  slug: terminal-login-request
- name: LoginResponse
  property_count: 4
  slug: terminal-login-response
- name: LogoutRequest
  property_count: 1
  slug: terminal-logout-request
- name: LogoutResponse
  property_count: 1
  slug: terminal-logout-response
- name: LoyaltyAccountID
  property_count: 4
  slug: terminal-loyalty-account-id
- name: LoyaltyAccountReq
  property_count: 2
  slug: terminal-loyalty-account-req
- name: LoyaltyAccount
  property_count: 2
  slug: terminal-loyalty-account
- name: LoyaltyAccountStatus
  property_count: 4
  slug: terminal-loyalty-account-status
- name: LoyaltyAcquirerData
  property_count: 4
  slug: terminal-loyalty-acquirer-data
- name: LoyaltyAmount
  property_count: 3
  slug: terminal-loyalty-amount
- name: LoyaltyData
  property_count: 3
  slug: terminal-loyalty-data
- name: LoyaltyHandling
  property_count: 0
  slug: terminal-loyalty-handling
- name: LoyaltyRequest
  property_count: 3
  slug: terminal-loyalty-request
- name: LoyaltyResponse
  property_count: 5
  slug: terminal-loyalty-response
- name: LoyaltyResult
  property_count: 5
  slug: terminal-loyalty-result
- name: LoyaltyTotals
  property_count: 3
  slug: terminal-loyalty-totals
- name: LoyaltyTransaction
  property_count: 6
  slug: terminal-loyalty-transaction
- name: LoyaltyTransactionType
  property_count: 0
  slug: terminal-loyalty-transaction-type
- name: LoyaltyUnit
  property_count: 0
  slug: terminal-loyalty-unit
- name: MenuEntry
  property_count: 6
  slug: terminal-menu-entry
- name: MenuEntryTag
  property_count: 0
  slug: terminal-menu-entry-tag
- name: MessageCategory
  property_count: 0
  slug: terminal-message-category
- name: MessageClass
  property_count: 0
  slug: terminal-message-class
- name: MessageHeader
  property_count: 8
  slug: terminal-message-header
- name: MessageReference
  property_count: 5
  slug: terminal-message-reference
- name: MessageType
  property_count: 0
  slug: terminal-message-type
- name: MobileData
  property_count: 6
  slug: terminal-mobile-data
- name: OriginalPOITransaction
  property_count: 9
  slug: terminal-original-poi-transaction
- name: OutputBarcode
  property_count: 2
  slug: terminal-output-barcode
- name: OutputContent
  property_count: 5
  slug: terminal-output-content
- name: OutputFormat
  property_count: 0
  slug: terminal-output-format
- name: OutputResult
  property_count: 3
  slug: terminal-output-result
- name: OutputText
  property_count: 11
  slug: terminal-output-text
- name: PaymentAccountReq
  property_count: 3
  slug: terminal-payment-account-req
- name: PaymentAccountStatus
  property_count: 4
  slug: terminal-payment-account-status
- name: PaymentAcquirerData
  property_count: 6
  slug: terminal-payment-acquirer-data
- name: PaymentData
  property_count: 7
  slug: terminal-payment-data
- name: PaymentInstrumentData
  property_count: 6
  slug: terminal-payment-instrument-data
- name: PaymentInstrumentType
  property_count: 0
  slug: terminal-payment-instrument-type
- name: PaymentReceipt
  property_count: 4
  slug: terminal-payment-receipt
- name: PaymentRequest
  property_count: 4
  slug: terminal-payment-request
- name: PaymentResponse
  property_count: 7
  slug: terminal-payment-response
- name: PaymentResult
  property_count: 13
  slug: terminal-payment-result
- name: PaymentToken
  property_count: 3
  slug: terminal-payment-token
- name: PaymentTotals
  property_count: 3
  slug: terminal-payment-totals
- name: PaymentTransaction
  property_count: 4
  slug: terminal-payment-transaction
- name: PaymentType
  property_count: 0
  slug: terminal-payment-type
- name: PerformedTransaction
  property_count: 6
  slug: terminal-performed-transaction
- name: PeriodUnit
  property_count: 0
  slug: terminal-period-unit
- name: PINFormat
  property_count: 0
  slug: terminal-pin-format
- name: PINRequestType
  property_count: 0
  slug: terminal-pin-request-type
- name: POICapabilities
  property_count: 0
  slug: terminal-poi-capabilities
- name: POIData
  property_count: 2
  slug: terminal-poi-data
- name: POIProfile
  property_count: 2
  slug: terminal-poi-profile
- name: POISoftware
  property_count: 4
  slug: terminal-poi-software
- name: POIStatus
  property_count: 8
  slug: terminal-poi-status
- name: POISystemData
  property_count: 4
  slug: terminal-poi-system-data
- name: POITerminalData
  property_count: 4
  slug: terminal-poi-terminal-data
- name: Point
  property_count: 2
  slug: terminal-point
- name: PredefinedContent
  property_count: 2
  slug: terminal-predefined-content
- name: PrintOutput
  property_count: 5
  slug: terminal-print-output
- name: PrintRequest
  property_count: 1
  slug: terminal-print-request
- name: PrintResponse
  property_count: 2
  slug: terminal-print-response
- name: PrinterStatus
  property_count: 0
  slug: terminal-printer-status
- name: Rebates
  property_count: 3
  slug: terminal-rebates
- name: ReconciliationRequest
  property_count: 3
  slug: terminal-reconciliation-request
- name: ReconciliationResponse
  property_count: 4
  slug: terminal-reconciliation-response
- name: ReconciliationType
  property_count: 0
  slug: terminal-reconciliation-type
- name: RepeatedMessageResponse
  property_count: 2
  slug: terminal-repeated-message-response
- name: RepeatedResponseMessageBody
  property_count: 6
  slug: terminal-repeated-response-message-body
- name: ResponseMode
  property_count: 0
  slug: terminal-response-mode
- name: Response
  property_count: 3
  slug: terminal-response
- name: Result
  property_count: 0
  slug: terminal-result
- name: ReversalReason
  property_count: 0
  slug: terminal-reversal-reason
- name: ReversalRequest
  property_count: 5
  slug: terminal-reversal-request
- name: ReversalResponse
  property_count: 6
  slug: terminal-reversal-response
- name: SaleCapabilities
  property_count: 0
  slug: terminal-sale-capabilities
- name: SaleData
  property_count: 12
  slug: terminal-sale-data
- name: SaleItemRebate
  property_count: 7
  slug: terminal-sale-item-rebate
- name: SaleItem
  property_count: 11
  slug: terminal-sale-item
- name: SaleSoftware
  property_count: 4
  slug: terminal-sale-software
- name: SaleTerminalData
  property_count: 1
  slug: terminal-sale-terminal-data
- name: SaleToIssuerData
  property_count: 1
  slug: terminal-sale-to-issuer-data
- name: SecurityTrailer
  property_count: 5
  slug: terminal-security-trailer
- name: SensitiveCardData
  property_count: 4
  slug: terminal-sensitive-card-data
- name: SensitiveMobileData
  property_count: 3
  slug: terminal-sensitive-mobile-data
- name: ServiceProfiles
  property_count: 0
  slug: terminal-service-profiles
- name: ServicesEnabled
  property_count: 0
  slug: terminal-services-enabled
- name: SoundAction
  property_count: 0
  slug: terminal-sound-action
- name: SoundContent
  property_count: 4
  slug: terminal-sound-content
- name: SoundFormat
  property_count: 0
  slug: terminal-sound-format
- name: StoredValueAccountID
  property_count: 7
  slug: terminal-stored-value-account-id
- name: StoredValueAccountStatus
  property_count: 2
  slug: terminal-stored-value-account-status
- name: StoredValueAccountType
  property_count: 0
  slug: terminal-stored-value-account-type
- name: StoredValueData
  property_count: 8
  slug: terminal-stored-value-data
- name: StoredValueRequest
  property_count: 3
  slug: terminal-stored-value-request
- name: StoredValueResponse
  property_count: 5
  slug: terminal-stored-value-response
- name: StoredValueResult
  property_count: 7
  slug: terminal-stored-value-result
- name: StoredValueTransactionType
  property_count: 0
  slug: terminal-stored-value-transaction-type
- name: TerminalEnvironment
  property_count: 0
  slug: terminal-terminal-environment
- name: TokenRequestedType
  property_count: 0
  slug: terminal-token-requested-type
- name: TotalDetails
  property_count: 0
  slug: terminal-total-details
- name: TotalFilter
  property_count: 5
  slug: terminal-total-filter
- name: TrackData
  property_count: 3
  slug: terminal-track-data
- name: TrackFormat
  property_count: 0
  slug: terminal-track-format
- name: TransactionAction
  property_count: 0
  slug: terminal-transaction-action
- name: TransactionConditions
  property_count: 9
  slug: terminal-transaction-conditions
- name: TransactionIDType
  property_count: 2
  slug: terminal-transaction-id-type
- name: TransactionStatusRequest
  property_count: 3
  slug: terminal-transaction-status-request
- name: TransactionStatusResponse
  property_count: 3
  slug: terminal-transaction-status-response
- name: TransactionTotals
  property_count: 14
  slug: terminal-transaction-totals
- name: TransactionType
  property_count: 0
  slug: terminal-transaction-type
- name: TypeCode
  property_count: 0
  slug: terminal-type-code
- name: UnitOfMeasure
  property_count: 0
  slug: terminal-unit-of-measure
- name: UTMCoordinates
  property_count: 3
  slug: terminal-utm-coordinates
- name: AvsAddress
  property_count: 2
  slug: test-cards-avs-address
- name: CreateTestCardRangesRequest
  property_count: 3
  slug: test-cards-create-test-card-ranges-request
- name: CreateTestCardRangesResult
  property_count: 1
  slug: test-cards-create-test-card-ranges-result
- name: TestCardRangeCreationResult
  property_count: 4
  slug: test-cards-test-card-range-creation-result
- name: TestCardRange
  property_count: 10
  slug: test-cards-test-card-range
- name: Amount
  property_count: 2
  slug: transaction-webhooks-amount
- name: BalancePlatformNotificationResponse
  property_count: 1
  slug: transaction-webhooks-balance-platform-notification-response
- name: ResourceReference
  property_count: 3
  slug: transaction-webhooks-resource-reference
- name: Resource
  property_count: 3
  slug: transaction-webhooks-resource
- name: TransactionNotificationRequestV4
  property_count: 3
  slug: transaction-webhooks-transaction-notification-request-v4
- name: Transaction
  property_count: 10
  slug: transaction-webhooks-transaction
- name: TransferData
  property_count: 2
  slug: transaction-webhooks-transfer-data
- name: AdditionalBankIdentification
  property_count: 2
  slug: transfer-webhooks-additional-bank-identification
- name: Address
  property_count: 6
  slug: transfer-webhooks-address
- name: AmountAdjustment
  property_count: 3
  slug: transfer-webhooks-amount-adjustment
- name: Amount
  property_count: 2
  slug: transfer-webhooks-amount
- name: AULocalAccountIdentification
  property_count: 3
  slug: transfer-webhooks-au-local-account-identification
- name: BalanceMutation
  property_count: 4
  slug: transfer-webhooks-balance-mutation
- name: BalancePlatformNotificationResponse
  property_count: 1
  slug: transfer-webhooks-balance-platform-notification-response
- name: BankAccountV3
  property_count: 2
  slug: transfer-webhooks-bank-account-v3
- name: BankCategoryData
  property_count: 2
  slug: transfer-webhooks-bank-category-data
- name: BRLocalAccountIdentification
  property_count: 4
  slug: transfer-webhooks-br-local-account-identification
- name: CALocalAccountIdentification
  property_count: 5
  slug: transfer-webhooks-ca-local-account-identification
- name: CounterpartyV3
  property_count: 4
  slug: transfer-webhooks-counterparty-v3
- name: CZLocalAccountIdentification
  property_count: 3
  slug: transfer-webhooks-cz-local-account-identification
- name: DKLocalAccountIdentification
  property_count: 3
  slug: transfer-webhooks-dk-local-account-identification
- name: HKLocalAccountIdentification
  property_count: 3
  slug: transfer-webhooks-hk-local-account-identification
- name: HULocalAccountIdentification
  property_count: 2
  slug: transfer-webhooks-hu-local-account-identification
- name: IbanAccountIdentification
  property_count: 2
  slug: transfer-webhooks-iban-account-identification
- name: InternalCategoryData
  property_count: 3
  slug: transfer-webhooks-internal-category-data
- name: IssuedCard
  property_count: 8
  slug: transfer-webhooks-issued-card
- name: MerchantData
  property_count: 5
  slug: transfer-webhooks-merchant-data
- name: Modification
  property_count: 5
  slug: transfer-webhooks-modification
- name: NameLocation
  property_count: 6
  slug: transfer-webhooks-name-location
- name: NOLocalAccountIdentification
  property_count: 2
  slug: transfer-webhooks-no-local-account-identification
- name: NumberAndBicAccountIdentification
  property_count: 4
  slug: transfer-webhooks-number-and-bic-account-identification
- name: NZLocalAccountIdentification
  property_count: 2
  slug: transfer-webhooks-nz-local-account-identification
- name: PartyIdentification
  property_count: 7
  slug: transfer-webhooks-party-identification
- name: PaymentInstrument
  property_count: 4
  slug: transfer-webhooks-payment-instrument
- name: PLLocalAccountIdentification
  property_count: 2
  slug: transfer-webhooks-pl-local-account-identification
- name: PlatformPayment
  property_count: 6
  slug: transfer-webhooks-platform-payment
- name: RelayedAuthorisationData
  property_count: 2
  slug: transfer-webhooks-relayed-authorisation-data
- name: ResourceReference
  property_count: 3
  slug: transfer-webhooks-resource-reference
- name: Resource
  property_count: 3
  slug: transfer-webhooks-resource
- name: SELocalAccountIdentification
  property_count: 3
  slug: transfer-webhooks-se-local-account-identification
- name: SGLocalAccountIdentification
  property_count: 3
  slug: transfer-webhooks-sg-local-account-identification
- name: TransactionEventViolation
  property_count: 3
  slug: transfer-webhooks-transaction-event-violation
- name: TransactionRuleReference
  property_count: 5
  slug: transfer-webhooks-transaction-rule-reference
- name: TransactionRuleSource
  property_count: 2
  slug: transfer-webhooks-transaction-rule-source
- name: TransactionRulesResult
  property_count: 4
  slug: transfer-webhooks-transaction-rules-result
- name: TransferData
  property_count: 22
  slug: transfer-webhooks-transfer-data
- name: TransferEvent
  property_count: 14
  slug: transfer-webhooks-transfer-event
- name: TransferNotificationCounterParty
  property_count: 4
  slug: transfer-webhooks-transfer-notification-counter-party
- name: TransferNotificationMerchantData
  property_count: 7
  slug: transfer-webhooks-transfer-notification-merchant-data
- name: TransferNotificationRequest
  property_count: 3
  slug: transfer-webhooks-transfer-notification-request
- name: TransferNotificationTransferTracking
  property_count: 2
  slug: transfer-webhooks-transfer-notification-transfer-tracking
- name: TransferNotificationValidationFact
  property_count: 2
  slug: transfer-webhooks-transfer-notification-validation-fact
- name: UKLocalAccountIdentification
  property_count: 3
  slug: transfer-webhooks-uk-local-account-identification
- name: USLocalAccountIdentification
  property_count: 4
  slug: transfer-webhooks-us-local-account-identification
- name: AdditionalBankIdentification
  property_count: 2
  slug: transfers-additional-bank-identification
- name: Address
  property_count: 6
  slug: transfers-address
- name: Amount
  property_count: 2
  slug: transfers-amount
- name: AULocalAccountIdentification
  property_count: 3
  slug: transfers-au-local-account-identification
- name: BankAccountV3
  property_count: 2
  slug: transfers-bank-account-v3
- name: BankCategoryData
  property_count: 2
  slug: transfers-bank-category-data
- name: BRLocalAccountIdentification
  property_count: 4
  slug: transfers-br-local-account-identification
- name: CALocalAccountIdentification
  property_count: 5
  slug: transfers-ca-local-account-identification
- name: CapitalBalance
  property_count: 4
  slug: transfers-capital-balance
- name: CapitalGrantInfo
  property_count: 3
  slug: transfers-capital-grant-info
- name: CapitalGrant
  property_count: 9
  slug: transfers-capital-grant
- name: CapitalGrants
  property_count: 1
  slug: transfers-capital-grants
- name: CounterpartyInfoV3
  property_count: 3
  slug: transfers-counterparty-info-v3
- name: Counterparty
  property_count: 3
  slug: transfers-counterparty
- name: CounterpartyV3
  property_count: 4
  slug: transfers-counterparty-v3
- name: CZLocalAccountIdentification
  property_count: 3
  slug: transfers-cz-local-account-identification
- name: DKLocalAccountIdentification
  property_count: 3
  slug: transfers-dk-local-account-identification
- name: Fee
  property_count: 1
  slug: transfers-fee
- name: HKLocalAccountIdentification
  property_count: 3
  slug: transfers-hk-local-account-identification
- name: HULocalAccountIdentification
  property_count: 2
  slug: transfers-hu-local-account-identification
- name: IbanAccountIdentification
  property_count: 2
  slug: transfers-iban-account-identification
- name: InternalCategoryData
  property_count: 3
  slug: transfers-internal-category-data
- name: InvalidField
  property_count: 3
  slug: transfers-invalid-field
- name: IssuedCard
  property_count: 8
  slug: transfers-issued-card
- name: JSONObject
  property_count: 0
  slug: transfers-json-object
- name: Link
  property_count: 1
  slug: transfers-link
- name: Links
  property_count: 2
  slug: transfers-links
- name: MerchantData
  property_count: 5
  slug: transfers-merchant-data
- name: NameLocation
  property_count: 6
  slug: transfers-name-location
- name: NOLocalAccountIdentification
  property_count: 2
  slug: transfers-no-local-account-identification
- name: NumberAndBicAccountIdentification
  property_count: 4
  slug: transfers-number-and-bic-account-identification
- name: NZLocalAccountIdentification
  property_count: 2
  slug: transfers-nz-local-account-identification
- name: PartyIdentification
  property_count: 7
  slug: transfers-party-identification
- name: PaymentInstrument
  property_count: 4
  slug: transfers-payment-instrument
- name: PLLocalAccountIdentification
  property_count: 2
  slug: transfers-pl-local-account-identification
- name: PlatformPayment
  property_count: 6
  slug: transfers-platform-payment
- name: RelayedAuthorisationData
  property_count: 2
  slug: transfers-relayed-authorisation-data
- name: Repayment
  property_count: 3
  slug: transfers-repayment
- name: RepaymentTerm
  property_count: 2
  slug: transfers-repayment-term
- name: ResourceReference
  property_count: 3
  slug: transfers-resource-reference
- name: RestServiceError
  property_count: 9
  slug: transfers-rest-service-error
- name: ReturnTransferRequest
  property_count: 2
  slug: transfers-return-transfer-request
- name: ReturnTransferResponse
  property_count: 4
  slug: transfers-return-transfer-response
- name: SELocalAccountIdentification
  property_count: 3
  slug: transfers-se-local-account-identification
- name: SGLocalAccountIdentification
  property_count: 3
  slug: transfers-sg-local-account-identification
- name: ThresholdRepayment
  property_count: 1
  slug: transfers-threshold-repayment
- name: Transaction
  property_count: 10
  slug: transfers-transaction
- name: TransactionSearchResponse
  property_count: 2
  slug: transfers-transaction-search-response
- name: TransferData
  property_count: 2
  slug: transfers-transfer-data
- name: TransferInfo
  property_count: 10
  slug: transfers-transfer-info
- name: TransferNotificationValidationFact
  property_count: 2
  slug: transfers-transfer-notification-validation-fact
- name: Transfer
  property_count: 15
  slug: transfers-transfer
- name: UKLocalAccountIdentification
  property_count: 3
  slug: transfers-uk-local-account-identification
- name: UltimatePartyIdentification
  property_count: 7
  slug: transfers-ultimate-party-identification
- name: USLocalAccountIdentification
  property_count: 4
  slug: transfers-us-local-account-identification
- name: AchNotificationOfChangeNotificationRequestDataNoc
  property_count: 4
  slug: webhooks-ach-notification-of-change-notification-request-data-noc
- name: AchNotificationOfChangeNotificationRequestData
  property_count: 3
  slug: webhooks-ach-notification-of-change-notification-request-data
- name: AchNotificationOfChangeNotificationRequest
  property_count: 5
  slug: webhooks-ach-notification-of-change-notification-request
- name: Amount
  property_count: 2
  slug: webhooks-amount
- name: AuthorisationNotificationAdditionalData
  property_count: 143
  slug: webhooks-authorisation-notification-additional-data
- name: AuthorisationNotificationRequestItem
  property_count: 11
  slug: webhooks-authorisation-notification-request-item
- name: AuthorisationNotificationRequestItemWrapper
  property_count: 1
  slug: webhooks-authorisation-notification-request-item-wrapper
- name: AuthorisationNotificationRequest
  property_count: 2
  slug: webhooks-authorisation-notification-request
- name: ExpireNotificationRequestItem
  property_count: 11
  slug: webhooks-expire-notification-request-item
- name: ExpireNotificationRequestItemWrapper
  property_count: 1
  slug: webhooks-expire-notification-request-item-wrapper
- name: ExpireNotificationRequest
  property_count: 2
  slug: webhooks-expire-notification-request
- name: NotificationAdditionalData
  property_count: 121
  slug: webhooks-notification-additional-data
- name: NotificationRequestItem
  property_count: 11
  slug: webhooks-notification-request-item
- name: NotificationRequestItemWrapper
  property_count: 1
  slug: webhooks-notification-request-item-wrapper
- name: NotificationRequest
  property_count: 2
  slug: webhooks-notification-request
- name: NotificationResponse
  property_count: 1
  slug: webhooks-notification-response
- name: PaidoutReversedNotificationRequestItem
  property_count: 11
  slug: webhooks-paidout-reversed-notification-request-item
- name: PaidoutReversedNotificationRequestItemWrapper
  property_count: 1
  slug: webhooks-paidout-reversed-notification-request-item-wrapper
- name: PaidoutReversedNotificationRequest
  property_count: 2
  slug: webhooks-paidout-reversed-notification-request
- name: RecurringContractNotificationAdditionalData
  property_count: 122
  slug: webhooks-recurring-contract-notification-additional-data
- name: RecurringContractNotificationRequestItem
  property_count: 12
  slug: webhooks-recurring-contract-notification-request-item
- name: RecurringContractNotificationRequestItemWrapper
  property_count: 1
  slug: webhooks-recurring-contract-notification-request-item-wrapper
- name: RecurringContractNotificationRequest
  property_count: 2
  slug: webhooks-recurring-contract-notification-request
- name: ReportAvailableNotificationRequestItem
  property_count: 11
  slug: webhooks-report-available-notification-request-item
- name: ReportAvailableNotificationRequestItemWrapper
  property_count: 1
  slug: webhooks-report-available-notification-request-item-wrapper
- name: ReportAvailableNotificationRequest
  property_count: 2
  slug: webhooks-report-available-notification-request
json_structures:
- name: Accounting Notifications Additional Bank Identification Structure
  property_count: 2
  slug: accounting-notifications-additional-bank-identification-structure
- name: Accounting Notifications Address 2 Structure
  property_count: 6
  slug: accounting-notifications-address-2-structure
- name: Accounting Notifications Amount Adjustment Structure
  property_count: 3
  slug: accounting-notifications-amount-adjustment-structure
- name: Accounting Notifications Amount Structure
  property_count: 2
  slug: accounting-notifications-amount-structure
- name: Accounting Notifications Au Local Account Identification Structure
  property_count: 3
  slug: accounting-notifications-au-local-account-identification-structure
- name: Accounting Notifications Balance Mutation Structure
  property_count: 4
  slug: accounting-notifications-balance-mutation-structure
- name: Accounting Notifications Balance Platform Notification Response Structure
  property_count: 1
  slug: accounting-notifications-balance-platform-notification-response-structure
- name: Accounting Notifications Bank Account V3 Structure
  property_count: 2
  slug: accounting-notifications-bank-account-v3-structure
- name: Accounting Notifications Br Local Account Identification Structure
  property_count: 4
  slug: accounting-notifications-br-local-account-identification-structure
- name: Accounting Notifications Ca Local Account Identification Structure
  property_count: 4
  slug: accounting-notifications-ca-local-account-identification-structure
- name: Accounting Notifications Counterparty V3 Structure
  property_count: 4
  slug: accounting-notifications-counterparty-v3-structure
- name: Accounting Notifications Cz Local Account Identification Structure
  property_count: 3
  slug: accounting-notifications-cz-local-account-identification-structure
- name: Accounting Notifications Dk Local Account Identification Structure
  property_count: 3
  slug: accounting-notifications-dk-local-account-identification-structure
- name: Accounting Notifications Hu Local Account Identification Structure
  property_count: 2
  slug: accounting-notifications-hu-local-account-identification-structure
- name: Accounting Notifications Iban Account Identification Structure
  property_count: 2
  slug: accounting-notifications-iban-account-identification-structure
- name: Accounting Notifications Merchant Data Structure
  property_count: 4
  slug: accounting-notifications-merchant-data-structure
- name: Accounting Notifications Name Location Structure
  property_count: 6
  slug: accounting-notifications-name-location-structure
- name: Accounting Notifications No Local Account Identification Structure
  property_count: 2
  slug: accounting-notifications-no-local-account-identification-structure
- name: Accounting Notifications Number And Bic Account Identification Structure
  property_count: 4
  slug: accounting-notifications-number-and-bic-account-identification-structure
- name: Accounting Notifications Party Identification 2 Structure
  property_count: 5
  slug: accounting-notifications-party-identification-2-structure
- name: Accounting Notifications Payment Instrument Structure
  property_count: 4
  slug: accounting-notifications-payment-instrument-structure
- name: Accounting Notifications Pl Local Account Identification Structure
  property_count: 2
  slug: accounting-notifications-pl-local-account-identification-structure
- name: Accounting Notifications Relayed Authorisation Data 2 Structure
  property_count: 2
  slug: accounting-notifications-relayed-authorisation-data-2-structure
- name: Accounting Notifications Resource Reference Structure
  property_count: 3
  slug: accounting-notifications-resource-reference-structure
- name: Accounting Notifications Resource Structure
  property_count: 3
  slug: accounting-notifications-resource-structure
- name: Accounting Notifications Se Local Account Identification Structure
  property_count: 3
  slug: accounting-notifications-se-local-account-identification-structure
- name: Accounting Notifications Sg Local Account Identification Structure
  property_count: 3
  slug: accounting-notifications-sg-local-account-identification-structure
- name: Accounting Notifications Transaction Event Violation Structure
  property_count: 3
  slug: accounting-notifications-transaction-event-violation-structure
- name: Accounting Notifications Transaction Rule Reference Structure
  property_count: 3
  slug: accounting-notifications-transaction-rule-reference-structure
- name: Accounting Notifications Transaction Rule Source Structure
  property_count: 2
  slug: accounting-notifications-transaction-rule-source-structure
- name: Accounting Notifications Transaction Rules Result Structure
  property_count: 4
  slug: accounting-notifications-transaction-rules-result-structure
- name: Accounting Notifications Transfer Event Structure
  property_count: 11
  slug: accounting-notifications-transfer-event-structure
- name: Accounting Notifications Transfer Notification Data Structure
  property_count: 31
  slug: accounting-notifications-transfer-notification-data-structure
- name: Accounting Notifications Transfer Notification Request Structure
  property_count: 3
  slug: accounting-notifications-transfer-notification-request-structure
- name: Accounting Notifications Transfer Notification Transfer Tracking Structure
  property_count: 1
  slug: accounting-notifications-transfer-notification-transfer-tracking-structure
- name: Accounting Notifications Transfer Notification Validation Fact Structure
  property_count: 2
  slug: accounting-notifications-transfer-notification-validation-fact-structure
- name: Accounting Notifications Uk Local Account Identification Structure
  property_count: 3
  slug: accounting-notifications-uk-local-account-identification-structure
- name: Accounting Notifications Us Local Account Identification Structure
  property_count: 4
  slug: accounting-notifications-us-local-account-identification-structure
- name: Accounts Account Event Structure
  property_count: 3
  slug: accounts-account-event-structure
- name: Accounts Account Holder Details Structure
  property_count: 15
  slug: accounts-account-holder-details-structure
- name: Accounts Account Holder Status Structure
  property_count: 5
  slug: accounts-account-holder-status-structure
- name: Accounts Account Payout State Structure
  property_count: 6
  slug: accounts-account-payout-state-structure
- name: Accounts Account Processing State Structure
  property_count: 5
  slug: accounts-account-processing-state-structure
- name: Accounts Account Structure
  property_count: 10
  slug: accounts-account-structure
- name: Accounts Amount Structure
  property_count: 2
  slug: accounts-amount-structure
- name: Accounts Bank Account Detail Structure
  property_count: 26
  slug: accounts-bank-account-detail-structure
- name: Accounts Business Details Structure
  property_count: 10
  slug: accounts-business-details-structure
- name: Accounts Close Account Holder Request Structure
  property_count: 1
  slug: accounts-close-account-holder-request-structure
- name: Accounts Close Account Holder Response Structure
  property_count: 4
  slug: accounts-close-account-holder-response-structure
- name: Accounts Close Account Request Structure
  property_count: 1
  slug: accounts-close-account-request-structure
- name: Accounts Close Account Response Structure
  property_count: 5
  slug: accounts-close-account-response-structure
- name: Accounts Close Stores Request Structure
  property_count: 2
  slug: accounts-close-stores-request-structure
- name: Accounts Create Account Holder Request Structure
  property_count: 8
  slug: accounts-create-account-holder-request-structure
- name: Accounts Create Account Holder Response Structure
  property_count: 12
  slug: accounts-create-account-holder-response-structure
- name: Accounts Create Account Request Structure
  property_count: 8
  slug: accounts-create-account-request-structure
- name: Accounts Create Account Response Structure
  property_count: 12
  slug: accounts-create-account-response-structure
- name: Accounts Delete Bank Account Request Structure
  property_count: 2
  slug: accounts-delete-bank-account-request-structure
- name: Accounts Delete Legal Arrangement Request Structure
  property_count: 2
  slug: accounts-delete-legal-arrangement-request-structure
- name: Accounts Delete Payout Method Request Structure
  property_count: 2
  slug: accounts-delete-payout-method-request-structure
- name: Accounts Delete Shareholder Request Structure
  property_count: 2
  slug: accounts-delete-shareholder-request-structure
- name: Accounts Delete Signatories Request Structure
  property_count: 2
  slug: accounts-delete-signatories-request-structure
- name: Accounts Document Detail Structure
  property_count: 9
  slug: accounts-document-detail-structure
- name: Accounts Error Field Type Structure
  property_count: 3
  slug: accounts-error-field-type-structure
- name: Accounts Field Type Structure
  property_count: 3
  slug: accounts-field-type-structure
- name: Accounts Generic Response Structure
  property_count: 3
  slug: accounts-generic-response-structure
- name: Accounts Get Account Holder Request Structure
  property_count: 3
  slug: accounts-get-account-holder-request-structure
- name: Accounts Get Account Holder Response Structure
  property_count: 14
  slug: accounts-get-account-holder-response-structure
- name: Accounts Get Account Holder Status Response Structure
  property_count: 5
  slug: accounts-get-account-holder-status-response-structure
- name: Accounts Get Tax Form Request Structure
  property_count: 3
  slug: accounts-get-tax-form-request-structure
- name: Accounts Get Tax Form Response Structure
  property_count: 5
  slug: accounts-get-tax-form-response-structure
- name: Accounts Get Uploaded Documents Request Structure
  property_count: 3
  slug: accounts-get-uploaded-documents-request-structure
- name: Accounts Get Uploaded Documents Response Structure
  property_count: 4
  slug: accounts-get-uploaded-documents-response-structure
- name: Accounts Individual Details Structure
  property_count: 2
  slug: accounts-individual-details-structure
- name: Accounts Kyc Check Result Structure
  property_count: 1
  slug: accounts-kyc-check-result-structure
- name: Accounts Kyc Check Status Data Structure
  property_count: 4
  slug: accounts-kyc-check-status-data-structure
- name: Accounts Kyc Check Summary Structure
  property_count: 2
  slug: accounts-kyc-check-summary-structure
- name: Accounts Kyc Legal Arrangement Check Result Structure
  property_count: 2
  slug: accounts-kyc-legal-arrangement-check-result-structure
- name: Accounts Kyc Legal Arrangement Entity Check Result Structure
  property_count: 3
  slug: accounts-kyc-legal-arrangement-entity-check-result-structure
- name: Accounts Kyc Payout Method Check Result Structure
  property_count: 2
  slug: accounts-kyc-payout-method-check-result-structure
- name: Accounts Kyc Shareholder Check Result Structure
  property_count: 4
  slug: accounts-kyc-shareholder-check-result-structure
- name: Accounts Kyc Signatory Check Result Structure
  property_count: 2
  slug: accounts-kyc-signatory-check-result-structure
- name: Accounts Kyc Ultimate Parent Company Check Result Structure
  property_count: 2
  slug: accounts-kyc-ultimate-parent-company-check-result-structure
- name: Accounts Kyc Verification Result Structure
  property_count: 7
  slug: accounts-kyc-verification-result-structure
- name: Accounts Legal Arrangement Detail Structure
  property_count: 9
  slug: accounts-legal-arrangement-detail-structure
- name: Accounts Legal Arrangement Entity Detail Structure
  property_count: 11
  slug: accounts-legal-arrangement-entity-detail-structure
- name: Accounts Legal Arrangement Request Structure
  property_count: 2
  slug: accounts-legal-arrangement-request-structure
- name: Accounts Migrated Accounts Structure
  property_count: 2
  slug: accounts-migrated-accounts-structure
- name: Accounts Migrated Shareholders Structure
  property_count: 2
  slug: accounts-migrated-shareholders-structure
- name: Accounts Migrated Stores Structure
  property_count: 4
  slug: accounts-migrated-stores-structure
- name: Accounts Migration Data Structure
  property_count: 7
  slug: accounts-migration-data-structure
- name: Accounts Payout Method Structure
  property_count: 5
  slug: accounts-payout-method-structure
- name: Accounts Payout Schedule Response Structure
  property_count: 2
  slug: accounts-payout-schedule-response-structure
- name: Accounts Perform Verification Request Structure
  property_count: 3
  slug: accounts-perform-verification-request-structure
- name: Accounts Personal Document Data Structure
  property_count: 5
  slug: accounts-personal-document-data-structure
- name: Accounts Shareholder Contact Structure
  property_count: 11
  slug: accounts-shareholder-contact-structure
- name: Accounts Signatory Contact Structure
  property_count: 10
  slug: accounts-signatory-contact-structure
- name: Accounts Store Detail Structure
  property_count: 15
  slug: accounts-store-detail-structure
- name: Accounts Suspend Account Holder Request Structure
  property_count: 1
  slug: accounts-suspend-account-holder-request-structure
- name: Accounts Suspend Account Holder Response Structure
  property_count: 4
  slug: accounts-suspend-account-holder-response-structure
- name: Accounts Ultimate Parent Company Business Details Structure
  property_count: 5
  slug: accounts-ultimate-parent-company-business-details-structure
- name: Accounts Ultimate Parent Company Structure
  property_count: 3
  slug: accounts-ultimate-parent-company-structure
- name: Accounts Un Suspend Account Holder Request Structure
  property_count: 1
  slug: accounts-un-suspend-account-holder-request-structure
- name: Accounts Un Suspend Account Holder Response Structure
  property_count: 4
  slug: accounts-un-suspend-account-holder-response-structure
- name: Accounts Update Account Holder Request Structure
  property_count: 7
  slug: accounts-update-account-holder-request-structure
- name: Accounts Update Account Holder Response Structure
  property_count: 11
  slug: accounts-update-account-holder-response-structure
- name: Accounts Update Account Holder State Request Structure
  property_count: 4
  slug: accounts-update-account-holder-state-request-structure
- name: Accounts Update Account Request Structure
  property_count: 7
  slug: accounts-update-account-request-structure
- name: Accounts Update Account Response Structure
  property_count: 10
  slug: accounts-update-account-response-structure
- name: Accounts Update Payout Schedule Request Structure
  property_count: 3
  slug: accounts-update-payout-schedule-request-structure
- name: Accounts Upload Document Request Structure
  property_count: 2
  slug: accounts-upload-document-request-structure
- name: Accounts Vias Address Structure
  property_count: 6
  slug: accounts-vias-address-structure
- name: Accounts Vias Name Structure
  property_count: 4
  slug: accounts-vias-name-structure
- name: Accounts Vias Personal Data Structure
  property_count: 3
  slug: accounts-vias-personal-data-structure
- name: Accounts Vias Phone Number Structure
  property_count: 3
  slug: accounts-vias-phone-number-structure
- name: Adyen Structure
  property_count: 0
  slug: adyen-structure
- name: Authentication Webhooks Amount Structure
  property_count: 2
  slug: authentication-webhooks-amount-structure
- name: Authentication Webhooks Authentication Info Structure
  property_count: 15
  slug: authentication-webhooks-authentication-info-structure
- name: Authentication Webhooks Authentication Notification Data Structure
  property_count: 6
  slug: authentication-webhooks-authentication-notification-data-structure
- name: Authentication Webhooks Authentication Notification Request Structure
  property_count: 3
  slug: authentication-webhooks-authentication-notification-request-structure
- name: Authentication Webhooks Balance Platform Notification Response Structure
  property_count: 1
  slug: authentication-webhooks-balance-platform-notification-response-structure
- name: Authentication Webhooks Challenge Info Structure
  property_count: 6
  slug: authentication-webhooks-challenge-info-structure
- name: Authentication Webhooks Purchase Info Structure
  property_count: 3
  slug: authentication-webhooks-purchase-info-structure
- name: Authentication Webhooks Resource Structure
  property_count: 3
  slug: authentication-webhooks-resource-structure
- name: Balance Control Amount Structure
  property_count: 2
  slug: balance-control-amount-structure
- name: Balance Control Balance Transfer Request Structure
  property_count: 6
  slug: balance-control-balance-transfer-request-structure
- name: Balance Control Balance Transfer Response Structure
  property_count: 9
  slug: balance-control-balance-transfer-response-structure
- name: Binlookup Amount Structure
  property_count: 2
  slug: binlookup-amount-structure
- name: Binlookup Bin Detail Structure
  property_count: 1
  slug: binlookup-bin-detail-structure
- name: Binlookup Card Bin Structure
  property_count: 11
  slug: binlookup-card-bin-structure
- name: Binlookup Cost Estimate Assumptions Structure
  property_count: 3
  slug: binlookup-cost-estimate-assumptions-structure
- name: Binlookup Cost Estimate Request Structure
  property_count: 10
  slug: binlookup-cost-estimate-request-structure
- name: Binlookup Cost Estimate Response Structure
  property_count: 5
  slug: binlookup-cost-estimate-response-structure
- name: Binlookup Ds Public Key Detail Structure
  property_count: 5
  slug: binlookup-ds-public-key-detail-structure
- name: Binlookup Merchant Details Structure
  property_count: 3
  slug: binlookup-merchant-details-structure
- name: Binlookup Recurring Structure
  property_count: 5
  slug: binlookup-recurring-structure
- name: Binlookup Three Ds Availability Request Structure
  property_count: 6
  slug: binlookup-three-ds-availability-request-structure
- name: Binlookup Three Ds Availability Response Structure
  property_count: 5
  slug: binlookup-three-ds-availability-response-structure
- name: Binlookup Three Ds2 Card Range Detail Structure
  property_count: 6
  slug: binlookup-three-ds2-card-range-detail-structure
- name: Checkout Account Info Structure
  property_count: 19
  slug: checkout-account-info-structure
- name: Checkout Acct Info Structure
  property_count: 16
  slug: checkout-acct-info-structure
- name: Checkout Ach Details Structure
  property_count: 10
  slug: checkout-ach-details-structure
- name: Checkout Additional Data Airline Structure
  property_count: 28
  slug: checkout-additional-data-airline-structure
- name: Checkout Additional Data Car Rental Structure
  property_count: 23
  slug: checkout-additional-data-car-rental-structure
- name: Checkout Additional Data Common Structure
  property_count: 16
  slug: checkout-additional-data-common-structure
- name: Checkout Additional Data Level23 Structure
  property_count: 17
  slug: checkout-additional-data-level23-structure
- name: Checkout Additional Data Lodging Structure
  property_count: 16
  slug: checkout-additional-data-lodging-structure
- name: Checkout Additional Data Open Invoice Structure
  property_count: 18
  slug: checkout-additional-data-open-invoice-structure
- name: Checkout Additional Data Opi Structure
  property_count: 1
  slug: checkout-additional-data-opi-structure
- name: Checkout Additional Data Ratepay Structure
  property_count: 8
  slug: checkout-additional-data-ratepay-structure
- name: Checkout Additional Data Retry Structure
  property_count: 3
  slug: checkout-additional-data-retry-structure
- name: Checkout Additional Data Risk Standalone Structure
  property_count: 15
  slug: checkout-additional-data-risk-standalone-structure
- name: Checkout Additional Data Risk Structure
  property_count: 21
  slug: checkout-additional-data-risk-structure
- name: Checkout Additional Data Sub Merchant Structure
  property_count: 10
  slug: checkout-additional-data-sub-merchant-structure
- name: Checkout Additional Data Temporary Services Structure
  property_count: 9
  slug: checkout-additional-data-temporary-services-structure
- name: Checkout Additional Data Wallets Structure
  property_count: 6
  slug: checkout-additional-data-wallets-structure
- name: Checkout Additional Data3 D Secure Structure
  property_count: 6
  slug: checkout-additional-data3-d-secure-structure
- name: Checkout Address Structure
  property_count: 6
  slug: checkout-address-structure
- name: Checkout Afterpay Details Structure
  property_count: 7
  slug: checkout-afterpay-details-structure
- name: Checkout Amazon Pay Details Structure
  property_count: 4
  slug: checkout-amazon-pay-details-structure
- name: Checkout Amount Structure
  property_count: 2
  slug: checkout-amount-structure
- name: Checkout Android Pay Details Structure
  property_count: 2
  slug: checkout-android-pay-details-structure
- name: Checkout Apple Pay Details Structure
  property_count: 6
  slug: checkout-apple-pay-details-structure
- name: Checkout Apple Pay Donations Structure
  property_count: 6
  slug: checkout-apple-pay-donations-structure
- name: Checkout Apple Pay Session Request Structure
  property_count: 3
  slug: checkout-apple-pay-session-request-structure
- name: Checkout Apple Pay Session Response Structure
  property_count: 1
  slug: checkout-apple-pay-session-response-structure
- name: Checkout Application Info Structure
  property_count: 6
  slug: checkout-application-info-structure
- name: Checkout Authentication Data Structure
  property_count: 3
  slug: checkout-authentication-data-structure
- name: Checkout Avs Structure
  property_count: 2
  slug: checkout-avs-structure
- name: Checkout Bacs Direct Debit Details Structure
  property_count: 7
  slug: checkout-bacs-direct-debit-details-structure
- name: Checkout Balance Check Request Structure
  property_count: 44
  slug: checkout-balance-check-request-structure
- name: Checkout Balance Check Response Structure
  property_count: 7
  slug: checkout-balance-check-response-structure
- name: Checkout Bank Account Structure
  property_count: 9
  slug: checkout-bank-account-structure
- name: Checkout Bill Desk Details Structure
  property_count: 3
  slug: checkout-bill-desk-details-structure
- name: Checkout Billing Address Structure
  property_count: 6
  slug: checkout-billing-address-structure
- name: Checkout Blik Details Structure
  property_count: 5
  slug: checkout-blik-details-structure
- name: Checkout Browser Info Structure
  property_count: 9
  slug: checkout-browser-info-structure
- name: Checkout Cancel Order Request Structure
  property_count: 2
  slug: checkout-cancel-order-request-structure
- name: Checkout Cancel Order Response Structure
  property_count: 2
  slug: checkout-cancel-order-response-structure
- name: Checkout Card Brand Details Structure
  property_count: 2
  slug: checkout-card-brand-details-structure
- name: Checkout Card Details Request Structure
  property_count: 5
  slug: checkout-card-details-request-structure
- name: Checkout Card Details Response Structure
  property_count: 1
  slug: checkout-card-details-response-structure
- name: Checkout Card Details Structure
  property_count: 19
  slug: checkout-card-details-structure
- name: Checkout Card Donations Structure
  property_count: 19
  slug: checkout-card-donations-structure
- name: Checkout Card Structure
  property_count: 8
  slug: checkout-card-structure
- name: Checkout Cellulant Details Structure
  property_count: 3
  slug: checkout-cellulant-details-structure
- name: Checkout Checkout Await Action Structure
  property_count: 4
  slug: checkout-checkout-await-action-structure
- name: Checkout Checkout Delegated Authentication Action Structure
  property_count: 6
  slug: checkout-checkout-delegated-authentication-action-structure
- name: Checkout Checkout Native Redirect Action Structure
  property_count: 6
  slug: checkout-checkout-native-redirect-action-structure
- name: Checkout Checkout Order Response Structure
  property_count: 6
  slug: checkout-checkout-order-response-structure
- name: Checkout Checkout Qr Code Action Structure
  property_count: 6
  slug: checkout-checkout-qr-code-action-structure
- name: Checkout Checkout Redirect Action Structure
  property_count: 5
  slug: checkout-checkout-redirect-action-structure
- name: Checkout Checkout Sdk Action Structure
  property_count: 5
  slug: checkout-checkout-sdk-action-structure
- name: Checkout Checkout Session Installment Option Structure
  property_count: 3
  slug: checkout-checkout-session-installment-option-structure
- name: Checkout Checkout Three Ds2 Action Structure
  property_count: 7
  slug: checkout-checkout-three-ds2-action-structure
- name: Checkout Checkout Voucher Action Structure
  property_count: 21
  slug: checkout-checkout-voucher-action-structure
- name: Checkout Common Field Structure
  property_count: 2
  slug: checkout-common-field-structure
- name: Checkout Company Structure
  property_count: 6
  slug: checkout-company-structure
- name: Checkout Configuration Structure
  property_count: 4
  slug: checkout-configuration-structure
- name: Checkout Create Checkout Session Request Structure
  property_count: 59
  slug: checkout-create-checkout-session-request-structure
- name: Checkout Create Checkout Session Response Structure
  property_count: 62
  slug: checkout-create-checkout-session-response-structure
- name: Checkout Create Order Request Structure
  property_count: 4
  slug: checkout-create-order-request-structure
- name: Checkout Create Order Response Structure
  property_count: 10
  slug: checkout-create-order-response-structure
- name: Checkout Delivery Address Structure
  property_count: 8
  slug: checkout-delivery-address-structure
- name: Checkout Details Request Authentication Data Structure
  property_count: 1
  slug: checkout-details-request-authentication-data-structure
- name: Checkout Device Render Options Structure
  property_count: 2
  slug: checkout-device-render-options-structure
- name: Checkout Doku Details Structure
  property_count: 5
  slug: checkout-doku-details-structure
- name: Checkout Donation Payment Request Structure
  property_count: 41
  slug: checkout-donation-payment-request-structure
- name: Checkout Donation Payment Response Structure
  property_count: 7
  slug: checkout-donation-payment-response-structure
- name: Checkout Dotpay Details Structure
  property_count: 3
  slug: checkout-dotpay-details-structure
- name: Checkout Dragonpay Details Structure
  property_count: 4
  slug: checkout-dragonpay-details-structure
- name: Checkout Econtext Voucher Details Structure
  property_count: 6
  slug: checkout-econtext-voucher-details-structure
- name: Checkout Encrypted Order Data Structure
  property_count: 2
  slug: checkout-encrypted-order-data-structure
- name: Checkout External Platform Structure
  property_count: 3
  slug: checkout-external-platform-structure
- name: Checkout Forex Quote Structure
  property_count: 12
  slug: checkout-forex-quote-structure
- name: Checkout Fraud Check Result Structure
  property_count: 3
  slug: checkout-fraud-check-result-structure
- name: Checkout Fraud Result Structure
  property_count: 2
  slug: checkout-fraud-result-structure
- name: Checkout Fund Origin Structure
  property_count: 5
  slug: checkout-fund-origin-structure
- name: Checkout Fund Recipient Structure
  property_count: 10
  slug: checkout-fund-recipient-structure
- name: Checkout Generic Issuer Payment Method Details Structure
  property_count: 5
  slug: checkout-generic-issuer-payment-method-details-structure
- name: Checkout Giropay Details Structure
  property_count: 4
  slug: checkout-giropay-details-structure
- name: Checkout Google Pay Details Structure
  property_count: 7
  slug: checkout-google-pay-details-structure
- name: Checkout Google Pay Donations Structure
  property_count: 7
  slug: checkout-google-pay-donations-structure
- name: Checkout Ideal Details Structure
  property_count: 5
  slug: checkout-ideal-details-structure
- name: Checkout Ideal Donations Structure
  property_count: 5
  slug: checkout-ideal-donations-structure
- name: Checkout Input Detail Structure
  property_count: 9
  slug: checkout-input-detail-structure
- name: Checkout Installment Option Structure
  property_count: 4
  slug: checkout-installment-option-structure
- name: Checkout Installments Number Structure
  property_count: 1
  slug: checkout-installments-number-structure
- name: Checkout Installments Structure
  property_count: 2
  slug: checkout-installments-structure
- name: Checkout Item Structure
  property_count: 2
  slug: checkout-item-structure
- name: Checkout Klarna Details Structure
  property_count: 8
  slug: checkout-klarna-details-structure
- name: Checkout Line Item Structure
  property_count: 17
  slug: checkout-line-item-structure
- name: Checkout List Stored Payment Methods Response Structure
  property_count: 3
  slug: checkout-list-stored-payment-methods-response-structure
- name: Checkout Mandate Structure
  property_count: 8
  slug: checkout-mandate-structure
- name: Checkout Masterpass Details Structure
  property_count: 4
  slug: checkout-masterpass-details-structure
- name: Checkout Mbway Details Structure
  property_count: 4
  slug: checkout-mbway-details-structure
- name: Checkout Merchant Device Structure
  property_count: 3
  slug: checkout-merchant-device-structure
- name: Checkout Merchant Risk Indicator Structure
  property_count: 14
  slug: checkout-merchant-risk-indicator-structure
- name: Checkout Mobile Pay Details Structure
  property_count: 2
  slug: checkout-mobile-pay-details-structure
- name: Checkout Mol Pay Details Structure
  property_count: 3
  slug: checkout-mol-pay-details-structure
- name: Checkout Name Structure
  property_count: 2
  slug: checkout-name-structure
- name: Checkout Open Invoice Details Structure
  property_count: 7
  slug: checkout-open-invoice-details-structure
- name: Checkout Pay Pal Details Structure
  property_count: 9
  slug: checkout-pay-pal-details-structure
- name: Checkout Pay U Upi Details Structure
  property_count: 6
  slug: checkout-pay-u-upi-details-structure
- name: Checkout Pay With Google Details Structure
  property_count: 6
  slug: checkout-pay-with-google-details-structure
- name: Checkout Pay With Google Donations Structure
  property_count: 6
  slug: checkout-pay-with-google-donations-structure
- name: Checkout Payment Amount Update Request Structure
  property_count: 7
  slug: checkout-payment-amount-update-request-structure
- name: Checkout Payment Amount Update Response Structure
  property_count: 9
  slug: checkout-payment-amount-update-response-structure
- name: Checkout Payment Cancel Request Structure
  property_count: 3
  slug: checkout-payment-cancel-request-structure
- name: Checkout Payment Cancel Response Structure
  property_count: 5
  slug: checkout-payment-cancel-response-structure
- name: Checkout Payment Capture Request Structure
  property_count: 8
  slug: checkout-payment-capture-request-structure
- name: Checkout Payment Capture Response Structure
  property_count: 10
  slug: checkout-payment-capture-response-structure
- name: Checkout Payment Completion Details Structure
  property_count: 18
  slug: checkout-payment-completion-details-structure
- name: Checkout Payment Details Request Structure
  property_count: 4
  slug: checkout-payment-details-request-structure
- name: Checkout Payment Details Response Structure
  property_count: 15
  slug: checkout-payment-details-response-structure
- name: Checkout Payment Details Structure
  property_count: 2
  slug: checkout-payment-details-structure
- name: Checkout Payment Link Request Structure
  property_count: 38
  slug: checkout-payment-link-request-structure
- name: Checkout Payment Link Response Structure
  property_count: 42
  slug: checkout-payment-link-response-structure
- name: Checkout Payment Method Group Structure
  property_count: 3
  slug: checkout-payment-method-group-structure
- name: Checkout Payment Method Issuer Structure
  property_count: 3
  slug: checkout-payment-method-issuer-structure
- name: Checkout Payment Method Structure
  property_count: 9
  slug: checkout-payment-method-structure
- name: Checkout Payment Methods Request Structure
  property_count: 12
  slug: checkout-payment-methods-request-structure
- name: Checkout Payment Methods Response Structure
  property_count: 2
  slug: checkout-payment-methods-response-structure
- name: Checkout Payment Refund Request Structure
  property_count: 8
  slug: checkout-payment-refund-request-structure
- name: Checkout Payment Refund Response Structure
  property_count: 10
  slug: checkout-payment-refund-response-structure
- name: Checkout Payment Request Structure
  property_count: 67
  slug: checkout-payment-request-structure
- name: Checkout Payment Response Structure
  property_count: 15
  slug: checkout-payment-response-structure
- name: Checkout Payment Reversal Request Structure
  property_count: 3
  slug: checkout-payment-reversal-request-structure
- name: Checkout Payment Reversal Response Structure
  property_count: 5
  slug: checkout-payment-reversal-response-structure
- name: Checkout Payment Setup Request Structure
  property_count: 56
  slug: checkout-payment-setup-request-structure
- name: Checkout Payment Setup Response Structure
  property_count: 2
  slug: checkout-payment-setup-response-structure
- name: Checkout Payment Verification Request Structure
  property_count: 1
  slug: checkout-payment-verification-request-structure
- name: Checkout Payment Verification Response Structure
  property_count: 10
  slug: checkout-payment-verification-response-structure
- name: Checkout Phone Structure
  property_count: 2
  slug: checkout-phone-structure
- name: Checkout Platform Chargeback Logic Structure
  property_count: 3
  slug: checkout-platform-chargeback-logic-structure
- name: Checkout Ratepay Details Structure
  property_count: 7
  slug: checkout-ratepay-details-structure
- name: Checkout Recurring Detail Structure
  property_count: 11
  slug: checkout-recurring-detail-structure
- name: Checkout Recurring Structure
  property_count: 5
  slug: checkout-recurring-structure
- name: Checkout Response Additional Data Billing Address Structure
  property_count: 6
  slug: checkout-response-additional-data-billing-address-structure
- name: Checkout Response Additional Data Card Structure
  property_count: 8
  slug: checkout-response-additional-data-card-structure
- name: Checkout Response Additional Data Common Structure
  property_count: 59
  slug: checkout-response-additional-data-common-structure
- name: Checkout Response Additional Data Domestic Error Structure
  property_count: 2
  slug: checkout-response-additional-data-domestic-error-structure
- name: Checkout Response Additional Data Installments Structure
  property_count: 12
  slug: checkout-response-additional-data-installments-structure
- name: Checkout Response Additional Data Network Tokens Structure
  property_count: 3
  slug: checkout-response-additional-data-network-tokens-structure
- name: Checkout Response Additional Data Opi Structure
  property_count: 1
  slug: checkout-response-additional-data-opi-structure
- name: Checkout Response Additional Data Sepa Structure
  property_count: 3
  slug: checkout-response-additional-data-sepa-structure
- name: Checkout Response Additional Data3 D Secure Structure
  property_count: 5
  slug: checkout-response-additional-data3-d-secure-structure
- name: Checkout Response Payment Method Structure
  property_count: 2
  slug: checkout-response-payment-method-structure
- name: Checkout Risk Data Structure
  property_count: 4
  slug: checkout-risk-data-structure
- name: Checkout Samsung Pay Details Structure
  property_count: 6
  slug: checkout-samsung-pay-details-structure
- name: Checkout Sdk Ephem Pub Key Structure
  property_count: 4
  slug: checkout-sdk-ephem-pub-key-structure
- name: Checkout Sepa Direct Debit Details Structure
  property_count: 6
  slug: checkout-sepa-direct-debit-details-structure
- name: Checkout Service Error Details Structure
  property_count: 4
  slug: checkout-service-error-details-structure
- name: Checkout Session Result Response Structure
  property_count: 2
  slug: checkout-session-result-response-structure
- name: Checkout Shopper Input Structure
  property_count: 3
  slug: checkout-shopper-input-structure
- name: Checkout Shopper Interaction Device Structure
  property_count: 3
  slug: checkout-shopper-interaction-device-structure
- name: Checkout Split Amount Structure
  property_count: 2
  slug: checkout-split-amount-structure
- name: Checkout Split Structure
  property_count: 5
  slug: checkout-split-structure
- name: Checkout Standalone Payment Cancel Request Structure
  property_count: 4
  slug: checkout-standalone-payment-cancel-request-structure
- name: Checkout Standalone Payment Cancel Response Structure
  property_count: 5
  slug: checkout-standalone-payment-cancel-response-structure
- name: Checkout Stored Details Structure
  property_count: 3
  slug: checkout-stored-details-structure
- name: Checkout Stored Payment Method Details Structure
  property_count: 4
  slug: checkout-stored-payment-method-details-structure
- name: Checkout Stored Payment Method Resource Structure
  property_count: 17
  slug: checkout-stored-payment-method-resource-structure
- name: Checkout Stored Payment Method Structure
  property_count: 17
  slug: checkout-stored-payment-method-structure
- name: Checkout Sub Input Detail Structure
  property_count: 6
  slug: checkout-sub-input-detail-structure
- name: Checkout Sub Merchant Info Structure
  property_count: 5
  slug: checkout-sub-merchant-info-structure
- name: Checkout Sub Merchant Structure
  property_count: 5
  slug: checkout-sub-merchant-structure
- name: Checkout Three D Secure Data Structure
  property_count: 12
  slug: checkout-three-d-secure-data-structure
- name: Checkout Three Ds Request Data Structure
  property_count: 4
  slug: checkout-three-ds-request-data-structure
- name: Checkout Three Ds Requestor Authentication Info Structure
  property_count: 3
  slug: checkout-three-ds-requestor-authentication-info-structure
- name: Checkout Three Ds Requestor Prior Authentication Info Structure
  property_count: 4
  slug: checkout-three-ds-requestor-prior-authentication-info-structure
- name: Checkout Three Ds2 Request Data Structure
  property_count: 40
  slug: checkout-three-ds2-request-data-structure
- name: Checkout Three Ds2 Request Fields Structure
  property_count: 37
  slug: checkout-three-ds2-request-fields-structure
- name: Checkout Three Ds2 Response Data Structure
  property_count: 19
  slug: checkout-three-ds2-response-data-structure
- name: Checkout Three Ds2 Result Structure
  property_count: 14
  slug: checkout-three-ds2-result-structure
- name: Checkout Update Payment Link Request Structure
  property_count: 1
  slug: checkout-update-payment-link-request-structure
- name: Checkout Upi Collect Details Structure
  property_count: 7
  slug: checkout-upi-collect-details-structure
- name: Checkout Upi Intent Details Structure
  property_count: 5
  slug: checkout-upi-intent-details-structure
- name: Checkout Utility Request Structure
  property_count: 1
  slug: checkout-utility-request-structure
- name: Checkout Utility Response Structure
  property_count: 1
  slug: checkout-utility-response-structure
- name: Checkout Vipps Details Structure
  property_count: 5
  slug: checkout-vipps-details-structure
- name: Checkout Visa Checkout Details Structure
  property_count: 4
  slug: checkout-visa-checkout-details-structure
- name: Checkout We Chat Pay Details Structure
  property_count: 2
  slug: checkout-we-chat-pay-details-structure
- name: Checkout We Chat Pay Mini Program Details Structure
  property_count: 4
  slug: checkout-we-chat-pay-mini-program-details-structure
- name: Checkout Zip Details Structure
  property_count: 5
  slug: checkout-zip-details-structure
- name: Configuration Account Holder Capability Structure
  property_count: 10
  slug: configuration-account-holder-capability-structure
- name: Configuration Account Holder Info Structure
  property_count: 9
  slug: configuration-account-holder-info-structure
- name: Configuration Account Holder Structure
  property_count: 13
  slug: configuration-account-holder-structure
- name: Configuration Account Holder Update Request Structure
  property_count: 11
  slug: configuration-account-holder-update-request-structure
- name: Configuration Account Supporting Entity Capability Structure
  property_count: 7
  slug: configuration-account-supporting-entity-capability-structure
- name: Configuration Active Network Tokens Restriction Structure
  property_count: 2
  slug: configuration-active-network-tokens-restriction-structure
- name: Configuration Additional Bank Identification Structure
  property_count: 2
  slug: configuration-additional-bank-identification-structure
- name: Configuration Address Requirement Structure
  property_count: 3
  slug: configuration-address-requirement-structure
- name: Configuration Address Structure
  property_count: 6
  slug: configuration-address-structure
- name: Configuration Amount Min Max Requirement Structure
  property_count: 4
  slug: configuration-amount-min-max-requirement-structure
- name: Configuration Amount Structure
  property_count: 2
  slug: configuration-amount-structure
- name: Configuration Au Local Account Identification Structure
  property_count: 3
  slug: configuration-au-local-account-identification-structure
- name: Configuration Authentication Structure
  property_count: 3
  slug: configuration-authentication-structure
- name: Configuration Balance Account Base Structure
  property_count: 10
  slug: configuration-balance-account-base-structure
- name: Configuration Balance Account Info Structure
  property_count: 8
  slug: configuration-balance-account-info-structure
- name: Configuration Balance Account Structure
  property_count: 11
  slug: configuration-balance-account-structure
- name: Configuration Balance Account Update Request Structure
  property_count: 7
  slug: configuration-balance-account-update-request-structure
- name: Configuration Balance Platform Structure
  property_count: 3
  slug: configuration-balance-platform-structure
- name: Configuration Balance Structure
  property_count: 5
  slug: configuration-balance-structure
- name: Configuration Balance Sweep Configurations Response Structure
  property_count: 3
  slug: configuration-balance-sweep-configurations-response-structure
- name: Configuration Bank Account Identification Type Requirement Structure
  property_count: 3
  slug: configuration-bank-account-identification-type-requirement-structure
- name: Configuration Bank Account Identification Validation Request Structure
  property_count: 1
  slug: configuration-bank-account-identification-validation-request-structure
- name: Configuration Bank Account Model Structure
  property_count: 1
  slug: configuration-bank-account-model-structure
- name: Configuration Bank Account Structure
  property_count: 1
  slug: configuration-bank-account-structure
- name: Configuration Bank Identification Structure
  property_count: 3
  slug: configuration-bank-identification-structure
- name: Configuration Br Local Account Identification Structure
  property_count: 4
  slug: configuration-br-local-account-identification-structure
- name: Configuration Brand Variants Restriction Structure
  property_count: 2
  slug: configuration-brand-variants-restriction-structure
- name: Configuration Bulk Address Structure
  property_count: 9
  slug: configuration-bulk-address-structure
- name: Configuration Ca Local Account Identification Structure
  property_count: 5
  slug: configuration-ca-local-account-identification-structure
- name: Configuration Capability Problem Entity Recursive Structure
  property_count: 3
  slug: configuration-capability-problem-entity-recursive-structure
- name: Configuration Capability Problem Entity Structure
  property_count: 4
  slug: configuration-capability-problem-entity-structure
- name: Configuration Capability Problem Structure
  property_count: 2
  slug: configuration-capability-problem-structure
- name: Configuration Capability Settings Structure
  property_count: 5
  slug: configuration-capability-settings-structure
- name: Configuration Capital Balance Structure
  property_count: 4
  slug: configuration-capital-balance-structure
- name: Configuration Capital Grant Account Structure
  property_count: 4
  slug: configuration-capital-grant-account-structure
- name: Configuration Card Configuration Structure
  property_count: 14
  slug: configuration-card-configuration-structure
- name: Configuration Card Info Structure
  property_count: 8
  slug: configuration-card-info-structure
- name: Configuration Card Order Item Delivery Status Structure
  property_count: 3
  slug: configuration-card-order-item-delivery-status-structure
- name: Configuration Card Order Item Structure
  property_count: 8
  slug: configuration-card-order-item-structure
- name: Configuration Card Order Structure
  property_count: 8
  slug: configuration-card-order-structure
- name: Configuration Card Structure
  property_count: 13
  slug: configuration-card-structure
- name: Configuration Contact Details Structure
  property_count: 4
  slug: configuration-contact-details-structure
- name: Configuration Counterparty Bank Restriction Structure
  property_count: 2
  slug: configuration-counterparty-bank-restriction-structure
- name: Configuration Counterparty Structure
  property_count: 2
  slug: configuration-counterparty-structure
- name: Configuration Countries Restriction Structure
  property_count: 2
  slug: configuration-countries-restriction-structure
- name: Configuration Create Sweep Configuration V2 Structure
  property_count: 12
  slug: configuration-create-sweep-configuration-v2-structure
- name: Configuration Cz Local Account Identification Structure
  property_count: 3
  slug: configuration-cz-local-account-identification-structure
- name: Configuration Day Of Week Restriction Structure
  property_count: 2
  slug: configuration-day-of-week-restriction-structure
- name: Configuration Delivery Address Structure
  property_count: 7
  slug: configuration-delivery-address-structure
- name: Configuration Delivery Contact Structure
  property_count: 6
  slug: configuration-delivery-contact-structure
- name: Configuration Device Info Structure
  property_count: 11
  slug: configuration-device-info-structure
- name: Configuration Different Currencies Restriction Structure
  property_count: 2
  slug: configuration-different-currencies-restriction-structure
- name: Configuration Dk Local Account Identification Structure
  property_count: 3
  slug: configuration-dk-local-account-identification-structure
- name: Configuration Duration Structure
  property_count: 2
  slug: configuration-duration-structure
- name: Configuration Entry Modes Restriction Structure
  property_count: 2
  slug: configuration-entry-modes-restriction-structure
- name: Configuration Expiry Structure
  property_count: 2
  slug: configuration-expiry-structure
- name: Configuration Fee Structure
  property_count: 1
  slug: configuration-fee-structure
- name: Configuration Get Network Token Response Structure
  property_count: 1
  slug: configuration-get-network-token-response-structure
- name: Configuration Get Tax Form Response Structure
  property_count: 2
  slug: configuration-get-tax-form-response-structure
- name: Configuration Grant Limit Structure
  property_count: 1
  slug: configuration-grant-limit-structure
- name: Configuration Grant Offer Structure
  property_count: 8
  slug: configuration-grant-offer-structure
- name: Configuration Grant Offers Structure
  property_count: 1
  slug: configuration-grant-offers-structure
- name: Configuration Hk Local Account Identification Structure
  property_count: 3
  slug: configuration-hk-local-account-identification-structure
- name: Configuration Hu Local Account Identification Structure
  property_count: 2
  slug: configuration-hu-local-account-identification-structure
- name: Configuration Iban Account Identification Structure
  property_count: 2
  slug: configuration-iban-account-identification-structure
- name: Configuration International Transaction Restriction Structure
  property_count: 2
  slug: configuration-international-transaction-restriction-structure
- name: Configuration Invalid Field Structure
  property_count: 3
  slug: configuration-invalid-field-structure
- name: Configuration Json Object Structure
  property_count: 0
  slug: configuration-json-object-structure
- name: Configuration List Network Tokens Response Structure
  property_count: 1
  slug: configuration-list-network-tokens-response-structure
- name: Configuration Matching Transactions Restriction Structure
  property_count: 2
  slug: configuration-matching-transactions-restriction-structure
- name: Configuration Mccs Restriction Structure
  property_count: 2
  slug: configuration-mccs-restriction-structure
- name: Configuration Merchant Acquirer Pair Structure
  property_count: 2
  slug: configuration-merchant-acquirer-pair-structure
- name: Configuration Merchant Names Restriction Structure
  property_count: 2
  slug: configuration-merchant-names-restriction-structure
- name: Configuration Merchants Restriction Structure
  property_count: 2
  slug: configuration-merchants-restriction-structure
- name: Configuration Name Structure
  property_count: 2
  slug: configuration-name-structure
- name: Configuration Network Token Structure
  property_count: 8
  slug: configuration-network-token-structure
- name: Configuration No Local Account Identification Structure
  property_count: 2
  slug: configuration-no-local-account-identification-structure
- name: Configuration Number And Bic Account Identification Structure
  property_count: 4
  slug: configuration-number-and-bic-account-identification-structure
- name: Configuration Nz Local Account Identification Structure
  property_count: 2
  slug: configuration-nz-local-account-identification-structure
- name: Configuration Paginated Account Holders Response Structure
  property_count: 3
  slug: configuration-paginated-account-holders-response-structure
- name: Configuration Paginated Balance Accounts Response Structure
  property_count: 3
  slug: configuration-paginated-balance-accounts-response-structure
- name: Configuration Paginated Get Card Order Item Response Structure
  property_count: 3
  slug: configuration-paginated-get-card-order-item-response-structure
- name: Configuration Paginated Get Card Order Response Structure
  property_count: 3
  slug: configuration-paginated-get-card-order-response-structure
- name: Configuration Paginated Payment Instruments Response Structure
  property_count: 3
  slug: configuration-paginated-payment-instruments-response-structure
- name: Configuration Payment Instrument Group Info Structure
  property_count: 5
  slug: configuration-payment-instrument-group-info-structure
- name: Configuration Payment Instrument Group Structure
  property_count: 6
  slug: configuration-payment-instrument-group-structure
- name: Configuration Payment Instrument Info Structure
  property_count: 10
  slug: configuration-payment-instrument-info-structure
- name: Configuration Payment Instrument Requirement Structure
  property_count: 5
  slug: configuration-payment-instrument-requirement-structure
- name: Configuration Payment Instrument Reveal Info Structure
  property_count: 3
  slug: configuration-payment-instrument-reveal-info-structure
- name: Configuration Payment Instrument Structure
  property_count: 11
  slug: configuration-payment-instrument-structure
- name: Configuration Payment Instrument Update Request Structure
  property_count: 5
  slug: configuration-payment-instrument-update-request-structure
- name: Configuration Phone Number Structure
  property_count: 3
  slug: configuration-phone-number-structure
- name: Configuration Phone Structure
  property_count: 2
  slug: configuration-phone-structure
- name: Configuration Pin Change Request Structure
  property_count: 4
  slug: configuration-pin-change-request-structure
- name: Configuration Pin Change Response Structure
  property_count: 1
  slug: configuration-pin-change-response-structure
- name: Configuration Pl Local Account Identification Structure
  property_count: 2
  slug: configuration-pl-local-account-identification-structure
- name: Configuration Platform Payment Configuration Structure
  property_count: 2
  slug: configuration-platform-payment-configuration-structure
- name: Configuration Processing Types Restriction Structure
  property_count: 2
  slug: configuration-processing-types-restriction-structure
- name: Configuration Public Key Response Structure
  property_count: 2
  slug: configuration-public-key-response-structure
- name: Configuration Remediating Action Structure
  property_count: 2
  slug: configuration-remediating-action-structure
- name: Configuration Repayment Structure
  property_count: 3
  slug: configuration-repayment-structure
- name: Configuration Repayment Term Structure
  property_count: 2
  slug: configuration-repayment-term-structure
- name: Configuration Rest Service Error Structure
  property_count: 9
  slug: configuration-rest-service-error-structure
- name: Configuration Reveal Pin Request Structure
  property_count: 2
  slug: configuration-reveal-pin-request-structure
- name: Configuration Reveal Pin Response Structure
  property_count: 2
  slug: configuration-reveal-pin-response-structure
- name: Configuration Same Amount Restriction Structure
  property_count: 2
  slug: configuration-same-amount-restriction-structure
- name: Configuration Same Counterparty Restriction Structure
  property_count: 2
  slug: configuration-same-counterparty-restriction-structure
- name: Configuration Se Local Account Identification Structure
  property_count: 3
  slug: configuration-se-local-account-identification-structure
- name: Configuration Sg Local Account Identification Structure
  property_count: 3
  slug: configuration-sg-local-account-identification-structure
- name: Configuration String Match Structure
  property_count: 2
  slug: configuration-string-match-structure
- name: Configuration Sweep Configuration V2 Structure
  property_count: 13
  slug: configuration-sweep-configuration-v2-structure
- name: Configuration Sweep Counterparty Structure
  property_count: 3
  slug: configuration-sweep-counterparty-structure
- name: Configuration Sweep Schedule Structure
  property_count: 2
  slug: configuration-sweep-schedule-structure
- name: Configuration Threshold Repayment Structure
  property_count: 1
  slug: configuration-threshold-repayment-structure
- name: Configuration Time Of Day Restriction Structure
  property_count: 2
  slug: configuration-time-of-day-restriction-structure
- name: Configuration Time Of Day Structure
  property_count: 2
  slug: configuration-time-of-day-structure
- name: Configuration Total Amount Restriction Structure
  property_count: 2
  slug: configuration-total-amount-restriction-structure
- name: Configuration Transaction Rule Entity Key Structure
  property_count: 2
  slug: configuration-transaction-rule-entity-key-structure
- name: Configuration Transaction Rule Info Structure
  property_count: 13
  slug: configuration-transaction-rule-info-structure
- name: Configuration Transaction Rule Interval Structure
  property_count: 6
  slug: configuration-transaction-rule-interval-structure
- name: Configuration Transaction Rule Response Structure
  property_count: 1
  slug: configuration-transaction-rule-response-structure
- name: Configuration Transaction Rule Restrictions Structure
  property_count: 17
  slug: configuration-transaction-rule-restrictions-structure
- name: Configuration Transaction Rule Structure
  property_count: 14
  slug: configuration-transaction-rule-structure
- name: Configuration Transaction Rules Response Structure
  property_count: 1
  slug: configuration-transaction-rules-response-structure
- name: Configuration Transfer Route Request Structure
  property_count: 7
  slug: configuration-transfer-route-request-structure
- name: Configuration Transfer Route Response Structure
  property_count: 1
  slug: configuration-transfer-route-response-structure
- name: Configuration Transfer Route Structure
  property_count: 5
  slug: configuration-transfer-route-structure
- name: Configuration Uk Local Account Identification Structure
  property_count: 3
  slug: configuration-uk-local-account-identification-structure
- name: Configuration Update Network Token Request Structure
  property_count: 1
  slug: configuration-update-network-token-request-structure
- name: Configuration Update Payment Instrument Structure
  property_count: 12
  slug: configuration-update-payment-instrument-structure
- name: Configuration Update Sweep Configuration V2 Structure
  property_count: 13
  slug: configuration-update-sweep-configuration-v2-structure
- name: Configuration Us Local Account Identification Structure
  property_count: 4
  slug: configuration-us-local-account-identification-structure
- name: Configuration Verification Deadline Structure
  property_count: 3
  slug: configuration-verification-deadline-structure
- name: Configuration Verification Error Recursive Structure
  property_count: 5
  slug: configuration-verification-error-recursive-structure
- name: Configuration Verification Error Structure
  property_count: 6
  slug: configuration-verification-error-structure
- name: Configuration Webhooks Account Holder Capability Structure
  property_count: 10
  slug: configuration-webhooks-account-holder-capability-structure
- name: Configuration Webhooks Account Holder Notification Data Structure
  property_count: 2
  slug: configuration-webhooks-account-holder-notification-data-structure
- name: Configuration Webhooks Account Holder Notification Request Structure
  property_count: 3
  slug: configuration-webhooks-account-holder-notification-request-structure
- name: Configuration Webhooks Account Holder Structure
  property_count: 13
  slug: configuration-webhooks-account-holder-structure
- name: Configuration Webhooks Account Supporting Entity Capability Structure
  property_count: 7
  slug: configuration-webhooks-account-supporting-entity-capability-structure
- name: Configuration Webhooks Address Structure
  property_count: 6
  slug: configuration-webhooks-address-structure
- name: Configuration Webhooks Amount Structure
  property_count: 2
  slug: configuration-webhooks-amount-structure
- name: Configuration Webhooks Authentication Structure
  property_count: 3
  slug: configuration-webhooks-authentication-structure
- name: Configuration Webhooks Balance Account Notification Data Structure
  property_count: 2
  slug: configuration-webhooks-balance-account-notification-data-structure
- name: Configuration Webhooks Balance Account Notification Request Structure
  property_count: 3
  slug: configuration-webhooks-balance-account-notification-request-structure
- name: Configuration Webhooks Balance Account Structure
  property_count: 12
  slug: configuration-webhooks-balance-account-structure
- name: Configuration Webhooks Balance Platform Notification Response Structure
  property_count: 1
  slug: configuration-webhooks-balance-platform-notification-response-structure
- name: Configuration Webhooks Balance Structure
  property_count: 5
  slug: configuration-webhooks-balance-structure
- name: Configuration Webhooks Bulk Address Structure
  property_count: 9
  slug: configuration-webhooks-bulk-address-structure
- name: Configuration Webhooks Capability Problem Entity Recursive Structure
  property_count: 3
  slug: configuration-webhooks-capability-problem-entity-recursive-structure
- name: Configuration Webhooks Capability Problem Entity Structure
  property_count: 4
  slug: configuration-webhooks-capability-problem-entity-structure
- name: Configuration Webhooks Capability Problem Structure
  property_count: 2
  slug: configuration-webhooks-capability-problem-structure
- name: Configuration Webhooks Capability Settings Structure
  property_count: 5
  slug: configuration-webhooks-capability-settings-structure
- name: Configuration Webhooks Card Configuration Structure
  property_count: 14
  slug: configuration-webhooks-card-configuration-structure
- name: Configuration Webhooks Card Order Item Delivery Status Structure
  property_count: 3
  slug: configuration-webhooks-card-order-item-delivery-status-structure
- name: Configuration Webhooks Card Order Item Structure
  property_count: 8
  slug: configuration-webhooks-card-order-item-structure
- name: Configuration Webhooks Card Order Notification Request Structure
  property_count: 3
  slug: configuration-webhooks-card-order-notification-request-structure
- name: Configuration Webhooks Card Structure
  property_count: 13
  slug: configuration-webhooks-card-structure
- name: Configuration Webhooks Contact Details Structure
  property_count: 4
  slug: configuration-webhooks-contact-details-structure
- name: Configuration Webhooks Contact Structure
  property_count: 7
  slug: configuration-webhooks-contact-structure
- name: Configuration Webhooks Expiry Structure
  property_count: 2
  slug: configuration-webhooks-expiry-structure
- name: Configuration Webhooks Iban Account Identification Structure
  property_count: 2
  slug: configuration-webhooks-iban-account-identification-structure
- name: Configuration Webhooks Name Structure
  property_count: 2
  slug: configuration-webhooks-name-structure
- name: Configuration Webhooks Payment Instrument Notification Data Structure
  property_count: 2
  slug: configuration-webhooks-payment-instrument-notification-data-structure
- name: Configuration Webhooks Payment Instrument Reference Structure
  property_count: 1
  slug: configuration-webhooks-payment-instrument-reference-structure
- name: Configuration Webhooks Payment Instrument Structure
  property_count: 10
  slug: configuration-webhooks-payment-instrument-structure
- name: Configuration Webhooks Payment Notification Request Structure
  property_count: 3
  slug: configuration-webhooks-payment-notification-request-structure
- name: Configuration Webhooks Personal Data Structure
  property_count: 3
  slug: configuration-webhooks-personal-data-structure
- name: Configuration Webhooks Phone Number Structure
  property_count: 3
  slug: configuration-webhooks-phone-number-structure
- name: Configuration Webhooks Phone Structure
  property_count: 2
  slug: configuration-webhooks-phone-structure
- name: Configuration Webhooks Platform Payment Configuration Structure
  property_count: 2
  slug: configuration-webhooks-platform-payment-configuration-structure
- name: Configuration Webhooks Remediating Action Structure
  property_count: 2
  slug: configuration-webhooks-remediating-action-structure
- name: Configuration Webhooks Resource Structure
  property_count: 3
  slug: configuration-webhooks-resource-structure
- name: Configuration Webhooks Sweep Configuration Notification Data Structure
  property_count: 3
  slug: configuration-webhooks-sweep-configuration-notification-data-structure
- name: Configuration Webhooks Sweep Configuration Notification Request Structure
  property_count: 3
  slug: configuration-webhooks-sweep-configuration-notification-request-structure
- name: Configuration Webhooks Sweep Configuration V2 Structure
  property_count: 11
  slug: configuration-webhooks-sweep-configuration-v2-structure
- name: Configuration Webhooks Sweep Counterparty Structure
  property_count: 3
  slug: configuration-webhooks-sweep-counterparty-structure
- name: Configuration Webhooks Sweep Schedule Structure
  property_count: 2
  slug: configuration-webhooks-sweep-schedule-structure
- name: Configuration Webhooks Us Local Account Identification Structure
  property_count: 4
  slug: configuration-webhooks-us-local-account-identification-structure
- name: Configuration Webhooks Verification Deadline Structure
  property_count: 3
  slug: configuration-webhooks-verification-deadline-structure
- name: Configuration Webhooks Verification Error Recursive Structure
  property_count: 5
  slug: configuration-webhooks-verification-error-recursive-structure
- name: Configuration Webhooks Verification Error Structure
  property_count: 6
  slug: configuration-webhooks-verification-error-structure
- name: Data Protection Subject Erasure By Psp Reference Request Structure
  property_count: 3
  slug: data-protection-subject-erasure-by-psp-reference-request-structure
- name: Data Protection Subject Erasure Response Structure
  property_count: 1
  slug: data-protection-subject-erasure-response-structure
- name: Disputes Accept Dispute Request Structure
  property_count: 2
  slug: disputes-accept-dispute-request-structure
- name: Disputes Accept Dispute Response Structure
  property_count: 1
  slug: disputes-accept-dispute-response-structure
- name: Disputes Defend Dispute Request Structure
  property_count: 3
  slug: disputes-defend-dispute-request-structure
- name: Disputes Defend Dispute Response Structure
  property_count: 1
  slug: disputes-defend-dispute-response-structure
- name: Disputes Defense Document Structure
  property_count: 3
  slug: disputes-defense-document-structure
- name: Disputes Defense Document Type Structure
  property_count: 3
  slug: disputes-defense-document-type-structure
- name: Disputes Defense Reason Structure
  property_count: 3
  slug: disputes-defense-reason-structure
- name: Disputes Defense Reasons Request Structure
  property_count: 2
  slug: disputes-defense-reasons-request-structure
- name: Disputes Defense Reasons Response Structure
  property_count: 2
  slug: disputes-defense-reasons-response-structure
- name: Disputes Delete Defense Document Request Structure
  property_count: 3
  slug: disputes-delete-defense-document-request-structure
- name: Disputes Delete Defense Document Response Structure
  property_count: 1
  slug: disputes-delete-defense-document-response-structure
- name: Disputes Dispute Service Result Structure
  property_count: 2
  slug: disputes-dispute-service-result-structure
- name: Disputes Supply Defense Document Request Structure
  property_count: 3
  slug: disputes-supply-defense-document-request-structure
- name: Disputes Supply Defense Document Response Structure
  property_count: 1
  slug: disputes-supply-defense-document-response-structure
- name: Funds Account Detail Balance Structure
  property_count: 2
  slug: funds-account-detail-balance-structure
- name: Funds Account Holder Balance Request Structure
  property_count: 1
  slug: funds-account-holder-balance-request-structure
- name: Funds Account Holder Balance Response Structure
  property_count: 5
  slug: funds-account-holder-balance-response-structure
- name: Funds Account Holder Transaction List Request Structure
  property_count: 3
  slug: funds-account-holder-transaction-list-request-structure
- name: Funds Account Holder Transaction List Response Structure
  property_count: 4
  slug: funds-account-holder-transaction-list-response-structure
- name: Funds Account Transaction List Structure
  property_count: 3
  slug: funds-account-transaction-list-structure
- name: Funds Amount Structure
  property_count: 2
  slug: funds-amount-structure
- name: Funds Bank Account Detail Structure
  property_count: 26
  slug: funds-bank-account-detail-structure
- name: Funds Debit Account Holder Request Structure
  property_count: 6
  slug: funds-debit-account-holder-request-structure
- name: Funds Debit Account Holder Response Structure
  property_count: 6
  slug: funds-debit-account-holder-response-structure
- name: Funds Detail Balance Structure
  property_count: 3
  slug: funds-detail-balance-structure
- name: Funds Error Field Type Structure
  property_count: 3
  slug: funds-error-field-type-structure
- name: Funds Field Type Structure
  property_count: 3
  slug: funds-field-type-structure
- name: Funds Payout Account Holder Request Structure
  property_count: 8
  slug: funds-payout-account-holder-request-structure
- name: Funds Payout Account Holder Response Structure
  property_count: 6
  slug: funds-payout-account-holder-response-structure
- name: Funds Refund Funds Transfer Request Structure
  property_count: 3
  slug: funds-refund-funds-transfer-request-structure
- name: Funds Refund Funds Transfer Response Structure
  property_count: 6
  slug: funds-refund-funds-transfer-response-structure
- name: Funds Refund Not Paid Out Transfers Request Structure
  property_count: 2
  slug: funds-refund-not-paid-out-transfers-request-structure
- name: Funds Refund Not Paid Out Transfers Response Structure
  property_count: 3
  slug: funds-refund-not-paid-out-transfers-response-structure
- name: Funds Setup Beneficiary Request Structure
  property_count: 3
  slug: funds-setup-beneficiary-request-structure
- name: Funds Setup Beneficiary Response Structure
  property_count: 3
  slug: funds-setup-beneficiary-response-structure
- name: Funds Split Amount Structure
  property_count: 2
  slug: funds-split-amount-structure
- name: Funds Split Structure
  property_count: 5
  slug: funds-split-structure
- name: Funds Transaction List For Account Structure
  property_count: 2
  slug: funds-transaction-list-for-account-structure
- name: Funds Transaction Structure
  property_count: 16
  slug: funds-transaction-structure
- name: Funds Transfer Funds Request Structure
  property_count: 5
  slug: funds-transfer-funds-request-structure
- name: Funds Transfer Funds Response Structure
  property_count: 4
  slug: funds-transfer-funds-response-structure
- name: Hosted Onboarding Collect Information Structure
  property_count: 6
  slug: hosted-onboarding-collect-information-structure
- name: Hosted Onboarding Error Field Type Structure
  property_count: 3
  slug: hosted-onboarding-error-field-type-structure
- name: Hosted Onboarding Field Type Structure
  property_count: 3
  slug: hosted-onboarding-field-type-structure
- name: Hosted Onboarding Get Onboarding Url Request Structure
  property_count: 8
  slug: hosted-onboarding-get-onboarding-url-request-structure
- name: Hosted Onboarding Get Onboarding Url Response Structure
  property_count: 4
  slug: hosted-onboarding-get-onboarding-url-response-structure
- name: Hosted Onboarding Get Pci Url Request Structure
  property_count: 2
  slug: hosted-onboarding-get-pci-url-request-structure
- name: Hosted Onboarding Get Pci Url Response Structure
  property_count: 4
  slug: hosted-onboarding-get-pci-url-response-structure
- name: Hosted Onboarding Show Pages Structure
  property_count: 9
  slug: hosted-onboarding-show-pages-structure
- name: Legal Entity Accept Terms Of Service Request Structure
  property_count: 2
  slug: legal-entity-accept-terms-of-service-request-structure
- name: Legal Entity Accept Terms Of Service Response Structure
  property_count: 6
  slug: legal-entity-accept-terms-of-service-response-structure
- name: Legal Entity Additional Bank Identification Structure
  property_count: 2
  slug: legal-entity-additional-bank-identification-structure
- name: Legal Entity Address Structure
  property_count: 6
  slug: legal-entity-address-structure
- name: Legal Entity Amount Structure
  property_count: 2
  slug: legal-entity-amount-structure
- name: Legal Entity Attachment Structure
  property_count: 5
  slug: legal-entity-attachment-structure
- name: Legal Entity Au Local Account Identification Structure
  property_count: 3
  slug: legal-entity-au-local-account-identification-structure
- name: Legal Entity Bank Account Info Structure
  property_count: 5
  slug: legal-entity-bank-account-info-structure
- name: Legal Entity Birth Data Structure
  property_count: 1
  slug: legal-entity-birth-data-structure
- name: Legal Entity Business Line Info Structure
  property_count: 8
  slug: legal-entity-business-line-info-structure
- name: Legal Entity Business Line Info Update Structure
  property_count: 8
  slug: legal-entity-business-line-info-update-structure
- name: Legal Entity Business Line Structure
  property_count: 10
  slug: legal-entity-business-line-structure
- name: Legal Entity Business Lines Structure
  property_count: 1
  slug: legal-entity-business-lines-structure
- name: Legal Entity Ca Local Account Identification Structure
  property_count: 5
  slug: legal-entity-ca-local-account-identification-structure
- name: Legal Entity Calculate Terms Of Service Status Response Structure
  property_count: 1
  slug: legal-entity-calculate-terms-of-service-status-response-structure
- name: Legal Entity Capability Problem Entity Recursive Structure
  property_count: 3
  slug: legal-entity-capability-problem-entity-recursive-structure
- name: Legal Entity Capability Problem Entity Structure
  property_count: 4
  slug: legal-entity-capability-problem-entity-structure
- name: Legal Entity Capability Problem Structure
  property_count: 2
  slug: legal-entity-capability-problem-structure
- name: Legal Entity Capability Settings Structure
  property_count: 5
  slug: legal-entity-capability-settings-structure
- name: Legal Entity Cz Local Account Identification Structure
  property_count: 3
  slug: legal-entity-cz-local-account-identification-structure
- name: Legal Entity Data Review Confirmation Response Structure
  property_count: 1
  slug: legal-entity-data-review-confirmation-response-structure
- name: Legal Entity Dk Local Account Identification Structure
  property_count: 3
  slug: legal-entity-dk-local-account-identification-structure
- name: Legal Entity Document Page Structure
  property_count: 3
  slug: legal-entity-document-page-structure
- name: Legal Entity Document Reference Structure
  property_count: 7
  slug: legal-entity-document-reference-structure
- name: Legal Entity Document Structure
  property_count: 13
  slug: legal-entity-document-structure
- name: Legal Entity Entity Reference Structure
  property_count: 1
  slug: legal-entity-entity-reference-structure
- name: Legal Entity Generate Pci Description Request Structure
  property_count: 2
  slug: legal-entity-generate-pci-description-request-structure
- name: Legal Entity Generate Pci Description Response Structure
  property_count: 3
  slug: legal-entity-generate-pci-description-response-structure
- name: Legal Entity Get Pci Questionnaire Infos Response Structure
  property_count: 1
  slug: legal-entity-get-pci-questionnaire-infos-response-structure
- name: Legal Entity Get Pci Questionnaire Response Structure
  property_count: 4
  slug: legal-entity-get-pci-questionnaire-response-structure
- name: Legal Entity Get Terms Of Service Acceptance Infos Response Structure
  property_count: 1
  slug: legal-entity-get-terms-of-service-acceptance-infos-response-structure
- name: Legal Entity Get Terms Of Service Document Request Structure
  property_count: 2
  slug: legal-entity-get-terms-of-service-document-request-structure
- name: Legal Entity Get Terms Of Service Document Response Structure
  property_count: 5
  slug: legal-entity-get-terms-of-service-document-response-structure
- name: Legal Entity Hk Local Account Identification Structure
  property_count: 3
  slug: legal-entity-hk-local-account-identification-structure
- name: Legal Entity Hu Local Account Identification Structure
  property_count: 2
  slug: legal-entity-hu-local-account-identification-structure
- name: Legal Entity Iban Account Identification Structure
  property_count: 2
  slug: legal-entity-iban-account-identification-structure
- name: Legal Entity Identification Data Structure
  property_count: 7
  slug: legal-entity-identification-data-structure
- name: Legal Entity Individual Structure
  property_count: 9
  slug: legal-entity-individual-structure
- name: Legal Entity Legal Entity Association Structure
  property_count: 7
  slug: legal-entity-legal-entity-association-structure
- name: Legal Entity Legal Entity Capability Structure
  property_count: 8
  slug: legal-entity-legal-entity-capability-structure
- name: Legal Entity Legal Entity Info Required Type Structure
  property_count: 10
  slug: legal-entity-legal-entity-info-required-type-structure
- name: Legal Entity Legal Entity Info Structure
  property_count: 10
  slug: legal-entity-legal-entity-info-structure
- name: Legal Entity Legal Entity Structure
  property_count: 16
  slug: legal-entity-legal-entity-structure
- name: Legal Entity Name Structure
  property_count: 3
  slug: legal-entity-name-structure
- name: Legal Entity No Local Account Identification Structure
  property_count: 2
  slug: legal-entity-no-local-account-identification-structure
- name: Legal Entity Number And Bic Account Identification Structure
  property_count: 4
  slug: legal-entity-number-and-bic-account-identification-structure
- name: Legal Entity Nz Local Account Identification Structure
  property_count: 2
  slug: legal-entity-nz-local-account-identification-structure
- name: Legal Entity Onboarding Link Info Structure
  property_count: 4
  slug: legal-entity-onboarding-link-info-structure
- name: Legal Entity Onboarding Link Structure
  property_count: 1
  slug: legal-entity-onboarding-link-structure
- name: Legal Entity Onboarding Theme Structure
  property_count: 5
  slug: legal-entity-onboarding-theme-structure
- name: Legal Entity Onboarding Themes Structure
  property_count: 3
  slug: legal-entity-onboarding-themes-structure
- name: Legal Entity Organization Structure
  property_count: 16
  slug: legal-entity-organization-structure
- name: Legal Entity Owner Entity Structure
  property_count: 2
  slug: legal-entity-owner-entity-structure
- name: Legal Entity Pci Document Info Structure
  property_count: 3
  slug: legal-entity-pci-document-info-structure
- name: Legal Entity Pci Signing Request Structure
  property_count: 2
  slug: legal-entity-pci-signing-request-structure
- name: Legal Entity Pci Signing Response Structure
  property_count: 2
  slug: legal-entity-pci-signing-response-structure
- name: Legal Entity Phone Number Structure
  property_count: 2
  slug: legal-entity-phone-number-structure
- name: Legal Entity Pl Local Account Identification Structure
  property_count: 2
  slug: legal-entity-pl-local-account-identification-structure
- name: Legal Entity Remediating Action Structure
  property_count: 2
  slug: legal-entity-remediating-action-structure
- name: Legal Entity Se Local Account Identification Structure
  property_count: 3
  slug: legal-entity-se-local-account-identification-structure
- name: Legal Entity Sg Local Account Identification Structure
  property_count: 3
  slug: legal-entity-sg-local-account-identification-structure
- name: Legal Entity Sole Proprietorship Structure
  property_count: 11
  slug: legal-entity-sole-proprietorship-structure
- name: Legal Entity Source Of Funds Structure
  property_count: 4
  slug: legal-entity-source-of-funds-structure
- name: Legal Entity Stock Data Structure
  property_count: 3
  slug: legal-entity-stock-data-structure
- name: Legal Entity Supporting Entity Capability Structure
  property_count: 4
  slug: legal-entity-supporting-entity-capability-structure
- name: Legal Entity Tax Information Structure
  property_count: 3
  slug: legal-entity-tax-information-structure
- name: Legal Entity Tax Reporting Classification Structure
  property_count: 4
  slug: legal-entity-tax-reporting-classification-structure
- name: Legal Entity Terms Of Service Acceptance Info Structure
  property_count: 5
  slug: legal-entity-terms-of-service-acceptance-info-structure
- name: Legal Entity Transfer Instrument Info Structure
  property_count: 3
  slug: legal-entity-transfer-instrument-info-structure
- name: Legal Entity Transfer Instrument Reference Structure
  property_count: 4
  slug: legal-entity-transfer-instrument-reference-structure
- name: Legal Entity Transfer Instrument Structure
  property_count: 7
  slug: legal-entity-transfer-instrument-structure
- name: Legal Entity Trust Structure
  property_count: 13
  slug: legal-entity-trust-structure
- name: Legal Entity Uk Local Account Identification Structure
  property_count: 3
  slug: legal-entity-uk-local-account-identification-structure
- name: Legal Entity Undefined Beneficiary Structure
  property_count: 2
  slug: legal-entity-undefined-beneficiary-structure
- name: Legal Entity Unincorporated Partnership Structure
  property_count: 12
  slug: legal-entity-unincorporated-partnership-structure
- name: Legal Entity Us Local Account Identification Structure
  property_count: 4
  slug: legal-entity-us-local-account-identification-structure
- name: Legal Entity Verification Deadline Structure
  property_count: 3
  slug: legal-entity-verification-deadline-structure
- name: Legal Entity Verification Error Recursive Structure
  property_count: 5
  slug: legal-entity-verification-error-recursive-structure
- name: Legal Entity Verification Error Structure
  property_count: 6
  slug: legal-entity-verification-error-structure
- name: Legal Entity Verification Errors Structure
  property_count: 1
  slug: legal-entity-verification-errors-structure
- name: Legal Entity Web Data Exemption Structure
  property_count: 1
  slug: legal-entity-web-data-exemption-structure
- name: Legal Entity Web Data Structure
  property_count: 2
  slug: legal-entity-web-data-structure
- name: Management Additional Commission Structure
  property_count: 3
  slug: management-additional-commission-structure
- name: Management Additional Settings Response Structure
  property_count: 3
  slug: management-additional-settings-response-structure
- name: Management Additional Settings Structure
  property_count: 2
  slug: management-additional-settings-structure
- name: Management Address Structure
  property_count: 7
  slug: management-address-structure
- name: Management Afterpay Touch Info Structure
  property_count: 1
  slug: management-afterpay-touch-info-structure
- name: Management Allowed Origin Structure
  property_count: 3
  slug: management-allowed-origin-structure
- name: Management Allowed Origins Response Structure
  property_count: 1
  slug: management-allowed-origins-response-structure
- name: Management Amount Structure
  property_count: 2
  slug: management-amount-structure
- name: Management Android App Structure
  property_count: 8
  slug: management-android-app-structure
- name: Management Android Apps Response Structure
  property_count: 1
  slug: management-android-apps-response-structure
- name: Management Android Certificate Structure
  property_count: 7
  slug: management-android-certificate-structure
- name: Management Android Certificates Response Structure
  property_count: 1
  slug: management-android-certificates-response-structure
- name: Management Api Credential Links Structure
  property_count: 6
  slug: management-api-credential-links-structure
- name: Management Api Credential Structure
  property_count: 9
  slug: management-api-credential-structure
- name: Management Apple Pay Info Structure
  property_count: 1
  slug: management-apple-pay-info-structure
- name: Management Bcmc Info Structure
  property_count: 2
  slug: management-bcmc-info-structure
- name: Management Billing Entities Response Structure
  property_count: 1
  slug: management-billing-entities-response-structure
- name: Management Billing Entity Structure
  property_count: 5
  slug: management-billing-entity-structure
- name: Management Cardholder Receipt Structure
  property_count: 1
  slug: management-cardholder-receipt-structure
- name: Management Cartes Bancaires Info Structure
  property_count: 2
  slug: management-cartes-bancaires-info-structure
- name: Management Clearpay Info Structure
  property_count: 1
  slug: management-clearpay-info-structure
- name: Management Commission Structure
  property_count: 2
  slug: management-commission-structure
- name: Management Company Api Credential Structure
  property_count: 10
  slug: management-company-api-credential-structure
- name: Management Company Links Structure
  property_count: 4
  slug: management-company-links-structure
- name: Management Company Structure
  property_count: 7
  slug: management-company-structure
- name: Management Company User Structure
  property_count: 11
  slug: management-company-user-structure
- name: Management Configuration Structure
  property_count: 4
  slug: management-configuration-structure
- name: Management Connectivity Structure
  property_count: 1
  slug: management-connectivity-structure
- name: Management Contact Structure
  property_count: 5
  slug: management-contact-structure
- name: Management Create Allowed Origin Request Structure
  property_count: 3
  slug: management-create-allowed-origin-request-structure
- name: Management Create Api Credential Response Structure
  property_count: 11
  slug: management-create-api-credential-response-structure
- name: Management Create Company Api Credential Request Structure
  property_count: 4
  slug: management-create-company-api-credential-request-structure
- name: Management Create Company Api Credential Response Structure
  property_count: 12
  slug: management-create-company-api-credential-response-structure
- name: Management Create Company User Request Structure
  property_count: 7
  slug: management-create-company-user-request-structure
- name: Management Create Company User Response Structure
  property_count: 11
  slug: management-create-company-user-response-structure
- name: Management Create Company Webhook Request Structure
  property_count: 16
  slug: management-create-company-webhook-request-structure
- name: Management Create Merchant Api Credential Request Structure
  property_count: 3
  slug: management-create-merchant-api-credential-request-structure
- name: Management Create Merchant Request Structure
  property_count: 7
  slug: management-create-merchant-request-structure
- name: Management Create Merchant Response Structure
  property_count: 7
  slug: management-create-merchant-response-structure
- name: Management Create Merchant User Request Structure
  property_count: 6
  slug: management-create-merchant-user-request-structure
- name: Management Create Merchant Webhook Request Structure
  property_count: 14
  slug: management-create-merchant-webhook-request-structure
- name: Management Create User Response Structure
  property_count: 10
  slug: management-create-user-response-structure
- name: Management Currency Structure
  property_count: 3
  slug: management-currency-structure
- name: Management Custom Notification Structure
  property_count: 7
  slug: management-custom-notification-structure
- name: Management Data Center Structure
  property_count: 2
  slug: management-data-center-structure
- name: Management Event Url Structure
  property_count: 2
  slug: management-event-url-structure
- name: Management External Terminal Action Structure
  property_count: 8
  slug: management-external-terminal-action-structure
- name: Management File Structure
  property_count: 2
  slug: management-file-structure
- name: Management Generate Api Key Response Structure
  property_count: 1
  slug: management-generate-api-key-response-structure
- name: Management Generate Client Key Response Structure
  property_count: 1
  slug: management-generate-client-key-response-structure
- name: Management Generate Hmac Key Response Structure
  property_count: 1
  slug: management-generate-hmac-key-response-structure
- name: Management Generic Pm With Tdi Info Structure
  property_count: 1
  slug: management-generic-pm-with-tdi-info-structure
- name: Management Giro Pay Info Structure
  property_count: 1
  slug: management-giro-pay-info-structure
- name: Management Google Pay Info Structure
  property_count: 2
  slug: management-google-pay-info-structure
- name: Management Gratuity Structure
  property_count: 4
  slug: management-gratuity-structure
- name: Management Hardware Structure
  property_count: 3
  slug: management-hardware-structure
- name: Management Id Name Structure
  property_count: 2
  slug: management-id-name-structure
- name: Management Install Android App Details Structure
  property_count: 2
  slug: management-install-android-app-details-structure
- name: Management Install Android Certificate Details Structure
  property_count: 2
  slug: management-install-android-certificate-details-structure
- name: Management Invalid Field Structure
  property_count: 3
  slug: management-invalid-field-structure
- name: Management Json Object Structure
  property_count: 0
  slug: management-json-object-structure
- name: Management Key Structure
  property_count: 3
  slug: management-key-structure
- name: Management Klarna Info Structure
  property_count: 4
  slug: management-klarna-info-structure
- name: Management Links Element Structure
  property_count: 1
  slug: management-links-element-structure
- name: Management Links Structure
  property_count: 1
  slug: management-links-structure
- name: Management List Company Api Credentials Response Structure
  property_count: 4
  slug: management-list-company-api-credentials-response-structure
- name: Management List Company Response Structure
  property_count: 4
  slug: management-list-company-response-structure
- name: Management List Company Users Response Structure
  property_count: 4
  slug: management-list-company-users-response-structure
- name: Management List External Terminal Actions Response Structure
  property_count: 1
  slug: management-list-external-terminal-actions-response-structure
- name: Management List Merchant Api Credentials Response Structure
  property_count: 4
  slug: management-list-merchant-api-credentials-response-structure
- name: Management List Merchant Response Structure
  property_count: 4
  slug: management-list-merchant-response-structure
- name: Management List Merchant Users Response Structure
  property_count: 4
  slug: management-list-merchant-users-response-structure
- name: Management List Stores Response Structure
  property_count: 4
  slug: management-list-stores-response-structure
- name: Management List Terminals Response Structure
  property_count: 4
  slug: management-list-terminals-response-structure
- name: Management List Webhooks Response Structure
  property_count: 5
  slug: management-list-webhooks-response-structure
- name: Management Localization Structure
  property_count: 3
  slug: management-localization-structure
- name: Management Logo Structure
  property_count: 1
  slug: management-logo-structure
- name: Management Me Api Credential Structure
  property_count: 11
  slug: management-me-api-credential-structure
- name: Management Meal Voucher Fr Info Structure
  property_count: 3
  slug: management-meal-voucher-fr-info-structure
- name: Management Merchant Links Structure
  property_count: 4
  slug: management-merchant-links-structure
- name: Management Merchant Structure
  property_count: 14
  slug: management-merchant-structure
- name: Management Minor Units Monetary Value Structure
  property_count: 2
  slug: management-minor-units-monetary-value-structure
- name: Management Name Structure
  property_count: 2
  slug: management-name-structure
- name: Management Name2 Structure
  property_count: 2
  slug: management-name2-structure
- name: Management Nexo Structure
  property_count: 5
  slug: management-nexo-structure
- name: Management Notification Structure
  property_count: 5
  slug: management-notification-structure
- name: Management Notification Url Structure
  property_count: 2
  slug: management-notification-url-structure
- name: Management Offline Processing Structure
  property_count: 2
  slug: management-offline-processing-structure
- name: Management Opi Structure
  property_count: 3
  slug: management-opi-structure
- name: Management Order Item Structure
  property_count: 4
  slug: management-order-item-structure
- name: Management Pagination Links Structure
  property_count: 5
  slug: management-pagination-links-structure
- name: Management Passcodes Structure
  property_count: 4
  slug: management-passcodes-structure
- name: Management Pay At Table Structure
  property_count: 3
  slug: management-pay-at-table-structure
- name: Management Pay Pal Info Structure
  property_count: 3
  slug: management-pay-pal-info-structure
- name: Management Payment Method Response Structure
  property_count: 5
  slug: management-payment-method-response-structure
- name: Management Payment Method Setup Info Structure
  property_count: 33
  slug: management-payment-method-setup-info-structure
- name: Management Payment Method Structure
  property_count: 37
  slug: management-payment-method-structure
- name: Management Payment Structure
  property_count: 2
  slug: management-payment-structure
- name: Management Payout Settings Request Structure
  property_count: 3
  slug: management-payout-settings-request-structure
- name: Management Payout Settings Response Structure
  property_count: 1
  slug: management-payout-settings-response-structure
- name: Management Payout Settings Structure
  property_count: 7
  slug: management-payout-settings-structure
- name: Management Profile Structure
  property_count: 18
  slug: management-profile-structure
- name: Management Receipt Options Structure
  property_count: 3
  slug: management-receipt-options-structure
- name: Management Receipt Printing Structure
  property_count: 16
  slug: management-receipt-printing-structure
- name: Management Referenced Structure
  property_count: 1
  slug: management-referenced-structure
- name: Management Refunds Structure
  property_count: 1
  slug: management-refunds-structure
- name: Management Release Update Details Structure
  property_count: 2
  slug: management-release-update-details-structure
- name: Management Request Activation Response Structure
  property_count: 2
  slug: management-request-activation-response-structure
- name: Management Rest Service Error Structure
  property_count: 9
  slug: management-rest-service-error-structure
- name: Management Schedule Terminal Actions Request Structure
  property_count: 4
  slug: management-schedule-terminal-actions-request-structure
- name: Management Schedule Terminal Actions Response Structure
  property_count: 7
  slug: management-schedule-terminal-actions-response-structure
- name: Management Settings Structure
  property_count: 3
  slug: management-settings-structure
- name: Management Shipping Location Structure
  property_count: 4
  slug: management-shipping-location-structure
- name: Management Shipping Locations Response Structure
  property_count: 1
  slug: management-shipping-locations-response-structure
- name: Management Signature Structure
  property_count: 4
  slug: management-signature-structure
- name: Management Sofort Info Structure
  property_count: 2
  slug: management-sofort-info-structure
- name: Management Split Configuration List Structure
  property_count: 1
  slug: management-split-configuration-list-structure
- name: Management Split Configuration Logic Structure
  property_count: 15
  slug: management-split-configuration-logic-structure
- name: Management Split Configuration Rule Structure
  property_count: 6
  slug: management-split-configuration-rule-structure
- name: Management Split Configuration Structure
  property_count: 4
  slug: management-split-configuration-structure
- name: Management Standalone Structure
  property_count: 2
  slug: management-standalone-structure
- name: Management Store Creation Request Structure
  property_count: 8
  slug: management-store-creation-request-structure
- name: Management Store Creation With Merchant Code Request Structure
  property_count: 9
  slug: management-store-creation-with-merchant-code-request-structure
- name: Management Store Location Structure
  property_count: 7
  slug: management-store-location-structure
- name: Management Store Split Configuration Structure
  property_count: 2
  slug: management-store-split-configuration-structure
- name: Management Store Structure
  property_count: 12
  slug: management-store-structure
- name: Management Surcharge Structure
  property_count: 2
  slug: management-surcharge-structure
- name: Management Swish Info Structure
  property_count: 1
  slug: management-swish-info-structure
- name: Management Tap To Pay Structure
  property_count: 1
  slug: management-tap-to-pay-structure
- name: Management Terminal Action Schedule Detail Structure
  property_count: 2
  slug: management-terminal-action-schedule-detail-structure
- name: Management Terminal Assignment Structure
  property_count: 5
  slug: management-terminal-assignment-structure
- name: Management Terminal Connectivity Bluetooth Structure
  property_count: 2
  slug: management-terminal-connectivity-bluetooth-structure
- name: Management Terminal Connectivity Cellular Structure
  property_count: 2
  slug: management-terminal-connectivity-cellular-structure
- name: Management Terminal Connectivity Ethernet Structure
  property_count: 3
  slug: management-terminal-connectivity-ethernet-structure
- name: Management Terminal Connectivity Structure
  property_count: 4
  slug: management-terminal-connectivity-structure
- name: Management Terminal Connectivity Wifi Structure
  property_count: 3
  slug: management-terminal-connectivity-wifi-structure
- name: Management Terminal Models Response Structure
  property_count: 1
  slug: management-terminal-models-response-structure
- name: Management Terminal Order Request Structure
  property_count: 6
  slug: management-terminal-order-request-structure
- name: Management Terminal Order Structure
  property_count: 8
  slug: management-terminal-order-structure
- name: Management Terminal Orders Response Structure
  property_count: 1
  slug: management-terminal-orders-response-structure
- name: Management Terminal Product Price Structure
  property_count: 2
  slug: management-terminal-product-price-structure
- name: Management Terminal Product Structure
  property_count: 5
  slug: management-terminal-product-structure
- name: Management Terminal Products Response Structure
  property_count: 1
  slug: management-terminal-products-response-structure
- name: Management Terminal Reassignment Request Structure
  property_count: 4
  slug: management-terminal-reassignment-request-structure
- name: Management Terminal Reassignment Target Structure
  property_count: 4
  slug: management-terminal-reassignment-target-structure
- name: Management Terminal Settings Structure
  property_count: 20
  slug: management-terminal-settings-structure
- name: Management Terminal Structure
  property_count: 8
  slug: management-terminal-structure
- name: Management Test Company Webhook Request Structure
  property_count: 3
  slug: management-test-company-webhook-request-structure
- name: Management Test Output Structure
  property_count: 6
  slug: management-test-output-structure
- name: Management Test Webhook Request Structure
  property_count: 2
  slug: management-test-webhook-request-structure
- name: Management Test Webhook Response Structure
  property_count: 1
  slug: management-test-webhook-response-structure
- name: Management Timeouts Structure
  property_count: 1
  slug: management-timeouts-structure
- name: Management Transaction Description Info Structure
  property_count: 2
  slug: management-transaction-description-info-structure
- name: Management Twint Info Structure
  property_count: 1
  slug: management-twint-info-structure
- name: Management Uninstall Android App Details Structure
  property_count: 2
  slug: management-uninstall-android-app-details-structure
- name: Management Uninstall Android Certificate Details Structure
  property_count: 2
  slug: management-uninstall-android-certificate-details-structure
- name: Management Updatable Address Structure
  property_count: 6
  slug: management-updatable-address-structure
- name: Management Update Company Api Credential Request Structure
  property_count: 5
  slug: management-update-company-api-credential-request-structure
- name: Management Update Company User Request Structure
  property_count: 7
  slug: management-update-company-user-request-structure
- name: Management Update Company Webhook Request Structure
  property_count: 15
  slug: management-update-company-webhook-request-structure
- name: Management Update Merchant Api Credential Request Structure
  property_count: 4
  slug: management-update-merchant-api-credential-request-structure
- name: Management Update Merchant User Request Structure
  property_count: 6
  slug: management-update-merchant-user-request-structure
- name: Management Update Merchant Webhook Request Structure
  property_count: 13
  slug: management-update-merchant-webhook-request-structure
- name: Management Update Payment Method Info Structure
  property_count: 18
  slug: management-update-payment-method-info-structure
- name: Management Update Payout Settings Request Structure
  property_count: 1
  slug: management-update-payout-settings-request-structure
- name: Management Update Split Configuration Logic Request Structure
  property_count: 15
  slug: management-update-split-configuration-logic-request-structure
- name: Management Update Split Configuration Request Structure
  property_count: 1
  slug: management-update-split-configuration-request-structure
- name: Management Update Split Configuration Rule Request Structure
  property_count: 4
  slug: management-update-split-configuration-rule-request-structure
- name: Management Update Store Request Structure
  property_count: 7
  slug: management-update-store-request-structure
- name: Management Upload Android App Response Structure
  property_count: 1
  slug: management-upload-android-app-response-structure
- name: Management Url Structure
  property_count: 4
  slug: management-url-structure
- name: Management User Structure
  property_count: 10
  slug: management-user-structure
- name: Management Vipps Info Structure
  property_count: 2
  slug: management-vipps-info-structure
- name: Management Webhook Links Structure
  property_count: 5
  slug: management-webhook-links-structure
- name: Management Webhook Structure
  property_count: 22
  slug: management-webhook-structure
- name: Management Webhooks Account Capability Data Structure
  property_count: 8
  slug: management-webhooks-account-capability-data-structure
- name: Management Webhooks Account Create Notification Data Structure
  property_count: 5
  slug: management-webhooks-account-create-notification-data-structure
- name: Management Webhooks Account Notification Response Structure
  property_count: 1
  slug: management-webhooks-account-notification-response-structure
- name: Management Webhooks Account Update Notification Data Structure
  property_count: 4
  slug: management-webhooks-account-update-notification-data-structure
- name: Management Webhooks Capability Problem Entity Recursive Structure
  property_count: 3
  slug: management-webhooks-capability-problem-entity-recursive-structure
- name: Management Webhooks Capability Problem Entity Structure
  property_count: 4
  slug: management-webhooks-capability-problem-entity-structure
- name: Management Webhooks Capability Problem Structure
  property_count: 2
  slug: management-webhooks-capability-problem-structure
- name: Management Webhooks Merchant Created Notification Request Structure
  property_count: 4
  slug: management-webhooks-merchant-created-notification-request-structure
- name: Management Webhooks Merchant Updated Notification Request Structure
  property_count: 4
  slug: management-webhooks-merchant-updated-notification-request-structure
- name: Management Webhooks Mid Service Notification Data Structure
  property_count: 9
  slug: management-webhooks-mid-service-notification-data-structure
- name: Management Webhooks Payment Method Created Notification Request Structure
  property_count: 4
  slug: management-webhooks-payment-method-created-notification-request-structure
- name: Management Webhooks Payment Method Notification Response Structure
  property_count: 1
  slug: management-webhooks-payment-method-notification-response-structure
- name: Management Webhooks Payment Method Request Removed Notification Request Structure
  property_count: 4
  slug: management-webhooks-payment-method-request-removed-notification-request-structure
- name: Management Webhooks Payment Method Scheduled For Removal Notification Request Structure
  property_count: 4
  slug: management-webhooks-payment-method-scheduled-for-removal-notification-request-structure
- name: Management Webhooks Remediating Action Structure
  property_count: 2
  slug: management-webhooks-remediating-action-structure
- name: Management Webhooks Verification Error Recursive Structure
  property_count: 4
  slug: management-webhooks-verification-error-recursive-structure
- name: Management Webhooks Verification Error Structure
  property_count: 5
  slug: management-webhooks-verification-error-structure
- name: Management Wifi Profiles Structure
  property_count: 2
  slug: management-wifi-profiles-structure
- name: Notification Configurations Create Notification Configuration Request Structure
  property_count: 1
  slug: notification-configurations-create-notification-configuration-request-structure
- name: Notification Configurations Delete Notification Configuration Request Structure
  property_count: 1
  slug: notification-configurations-delete-notification-configuration-request-structure
- name: Notification Configurations Empty Request Structure
  property_count: 0
  slug: notification-configurations-empty-request-structure
- name: Notification Configurations Error Field Type Structure
  property_count: 3
  slug: notification-configurations-error-field-type-structure
- name: Notification Configurations Exchange Message Structure
  property_count: 2
  slug: notification-configurations-exchange-message-structure
- name: Notification Configurations Field Type Structure
  property_count: 3
  slug: notification-configurations-field-type-structure
- name: Notification Configurations Generic Response Structure
  property_count: 3
  slug: notification-configurations-generic-response-structure
- name: Notification Configurations Get Notification Configuration List Response Structure
  property_count: 4
  slug: notification-configurations-get-notification-configuration-list-response-structure
- name: Notification Configurations Get Notification Configuration Request Structure
  property_count: 1
  slug: notification-configurations-get-notification-configuration-request-structure
- name: Notification Configurations Get Notification Configuration Response Structure
  property_count: 4
  slug: notification-configurations-get-notification-configuration-response-structure
- name: Notification Configurations Notification Configuration Details Structure
  property_count: 10
  slug: notification-configurations-notification-configuration-details-structure
- name: Notification Configurations Notification Event Configuration Structure
  property_count: 2
  slug: notification-configurations-notification-event-configuration-structure
- name: Notification Configurations Test Notification Configuration Request Structure
  property_count: 2
  slug: notification-configurations-test-notification-configuration-request-structure
- name: Notification Configurations Test Notification Configuration Response Structure
  property_count: 8
  slug: notification-configurations-test-notification-configuration-response-structure
- name: Notification Configurations Update Notification Configuration Request Structure
  property_count: 1
  slug: notification-configurations-update-notification-configuration-request-structure
- name: Notification Webhooks Account Holder Capability Structure
  property_count: 9
  slug: notification-webhooks-account-holder-capability-structure
- name: Notification Webhooks Account Holder Notification Data Structure
  property_count: 2
  slug: notification-webhooks-account-holder-notification-data-structure
- name: Notification Webhooks Account Holder Notification Request Structure
  property_count: 3
  slug: notification-webhooks-account-holder-notification-request-structure
- name: Notification Webhooks Account Holder Structure
  property_count: 10
  slug: notification-webhooks-account-holder-structure
- name: Notification Webhooks Address Structure
  property_count: 6
  slug: notification-webhooks-address-structure
- name: Notification Webhooks Amount Structure
  property_count: 2
  slug: notification-webhooks-amount-structure
- name: Notification Webhooks Authentication Structure
  property_count: 3
  slug: notification-webhooks-authentication-structure
- name: Notification Webhooks Balance Account Notification Data Structure
  property_count: 2
  slug: notification-webhooks-balance-account-notification-data-structure
- name: Notification Webhooks Balance Account Notification Request Structure
  property_count: 3
  slug: notification-webhooks-balance-account-notification-request-structure
- name: Notification Webhooks Balance Account Structure
  property_count: 10
  slug: notification-webhooks-balance-account-structure
- name: Notification Webhooks Balance Platform Notification Response Structure
  property_count: 1
  slug: notification-webhooks-balance-platform-notification-response-structure
- name: Notification Webhooks Balance Structure
  property_count: 4
  slug: notification-webhooks-balance-structure
- name: Notification Webhooks Bank Account Info Structure
  property_count: 3
  slug: notification-webhooks-bank-account-info-structure
- name: Notification Webhooks Bank Account Structure
  property_count: 1
  slug: notification-webhooks-bank-account-structure
- name: Notification Webhooks Bulk Address Structure
  property_count: 9
  slug: notification-webhooks-bulk-address-structure
- name: Notification Webhooks Capability Problem Entity Recursive Structure
  property_count: 2
  slug: notification-webhooks-capability-problem-entity-recursive-structure
- name: Notification Webhooks Capability Problem Entity Structure
  property_count: 3
  slug: notification-webhooks-capability-problem-entity-structure
- name: Notification Webhooks Capability Problem Structure
  property_count: 2
  slug: notification-webhooks-capability-problem-structure
- name: Notification Webhooks Card Configuration Structure
  property_count: 14
  slug: notification-webhooks-card-configuration-structure
- name: Notification Webhooks Card Structure
  property_count: 12
  slug: notification-webhooks-card-structure
- name: Notification Webhooks Contact Details Structure
  property_count: 4
  slug: notification-webhooks-contact-details-structure
- name: Notification Webhooks Contact Structure
  property_count: 7
  slug: notification-webhooks-contact-structure
- name: Notification Webhooks Counterparty Structure
  property_count: 4
  slug: notification-webhooks-counterparty-structure
- name: Notification Webhooks Cron Sweep Schedule Structure
  property_count: 2
  slug: notification-webhooks-cron-sweep-schedule-structure
- name: Notification Webhooks Expiry Structure
  property_count: 2
  slug: notification-webhooks-expiry-structure
- name: Notification Webhooks Incoming Transfer Notification Data Structure
  property_count: 17
  slug: notification-webhooks-incoming-transfer-notification-data-structure
- name: Notification Webhooks Incoming Transfer Notification Request Structure
  property_count: 3
  slug: notification-webhooks-incoming-transfer-notification-request-structure
- name: Notification Webhooks Json Object Structure
  property_count: 2
  slug: notification-webhooks-json-object-structure
- name: Notification Webhooks Json Path Structure
  property_count: 1
  slug: notification-webhooks-json-path-structure
- name: Notification Webhooks Merchant Data Structure
  property_count: 4
  slug: notification-webhooks-merchant-data-structure
- name: Notification Webhooks Name 2 Structure
  property_count: 4
  slug: notification-webhooks-name-2-structure
- name: Notification Webhooks Name Location Structure
  property_count: 6
  slug: notification-webhooks-name-location-structure
- name: Notification Webhooks Name Structure
  property_count: 2
  slug: notification-webhooks-name-structure
- name: Notification Webhooks Notification Modification Data Structure
  property_count: 2
  slug: notification-webhooks-notification-modification-data-structure
- name: Notification Webhooks Outgoing Transfer Notification Data Structure
  property_count: 22
  slug: notification-webhooks-outgoing-transfer-notification-data-structure
- name: Notification Webhooks Outgoing Transfer Notification Request Structure
  property_count: 3
  slug: notification-webhooks-outgoing-transfer-notification-request-structure
- name: Notification Webhooks Payment Instrument Notification Data Structure
  property_count: 2
  slug: notification-webhooks-payment-instrument-notification-data-structure
- name: Notification Webhooks Payment Instrument Reference Structure
  property_count: 1
  slug: notification-webhooks-payment-instrument-reference-structure
- name: Notification Webhooks Payment Instrument Structure
  property_count: 10
  slug: notification-webhooks-payment-instrument-structure
- name: Notification Webhooks Payment Notification Data Structure
  property_count: 20
  slug: notification-webhooks-payment-notification-data-structure
- name: Notification Webhooks Payment Notification Request 2 Structure
  property_count: 3
  slug: notification-webhooks-payment-notification-request-2-structure
- name: Notification Webhooks Payment Notification Request Structure
  property_count: 3
  slug: notification-webhooks-payment-notification-request-structure
- name: Notification Webhooks Personal Data Structure
  property_count: 3
  slug: notification-webhooks-personal-data-structure
- name: Notification Webhooks Phone Number Structure
  property_count: 3
  slug: notification-webhooks-phone-number-structure
- name: Notification Webhooks Phone Structure
  property_count: 2
  slug: notification-webhooks-phone-structure
- name: Notification Webhooks Platform Payment Structure
  property_count: 8
  slug: notification-webhooks-platform-payment-structure
- name: Notification Webhooks Relayed Authorisation Data Structure
  property_count: 3
  slug: notification-webhooks-relayed-authorisation-data-structure
- name: Notification Webhooks Remediating Action Structure
  property_count: 2
  slug: notification-webhooks-remediating-action-structure
- name: Notification Webhooks Report Notification Data Structure
  property_count: 7
  slug: notification-webhooks-report-notification-data-structure
- name: Notification Webhooks Report Notification Request Structure
  property_count: 3
  slug: notification-webhooks-report-notification-request-structure
- name: Notification Webhooks Resource Reference Structure
  property_count: 3
  slug: notification-webhooks-resource-reference-structure
- name: Notification Webhooks Resource Structure
  property_count: 3
  slug: notification-webhooks-resource-structure
- name: Notification Webhooks Sweep Configuration Notification Data Structure
  property_count: 3
  slug: notification-webhooks-sweep-configuration-notification-data-structure
- name: Notification Webhooks Sweep Configuration Notification Request Structure
  property_count: 3
  slug: notification-webhooks-sweep-configuration-notification-request-structure
- name: Notification Webhooks Sweep Configuration Structure
  property_count: 10
  slug: notification-webhooks-sweep-configuration-structure
- name: Notification Webhooks Sweep Configuration V2 Structure
  property_count: 10
  slug: notification-webhooks-sweep-configuration-v2-structure
- name: Notification Webhooks Sweep Counterparty Structure
  property_count: 3
  slug: notification-webhooks-sweep-counterparty-structure
- name: Notification Webhooks Sweep Schedule Structure
  property_count: 1
  slug: notification-webhooks-sweep-schedule-structure
- name: Notification Webhooks Transaction Event Violation Structure
  property_count: 3
  slug: notification-webhooks-transaction-event-violation-structure
- name: Notification Webhooks Transaction Notification Data Structure
  property_count: 24
  slug: notification-webhooks-transaction-notification-data-structure
- name: Notification Webhooks Transaction Rule Source Structure
  property_count: 2
  slug: notification-webhooks-transaction-rule-source-structure
- name: Notification Webhooks Transaction Rules Result Structure
  property_count: 2
  slug: notification-webhooks-transaction-rules-result-structure
- name: Notification Webhooks Validation Result Structure
  property_count: 2
  slug: notification-webhooks-validation-result-structure
- name: Notification Webhooks Verification Error Recursive Structure
  property_count: 4
  slug: notification-webhooks-verification-error-recursive-structure
- name: Notification Webhooks Verification Error Structure
  property_count: 5
  slug: notification-webhooks-verification-error-structure
- name: Notifications Account Close Notification Structure
  property_count: 7
  slug: notifications-account-close-notification-structure
- name: Notifications Account Create Notification Structure
  property_count: 7
  slug: notifications-account-create-notification-structure
- name: Notifications Account Event Structure
  property_count: 3
  slug: notifications-account-event-structure
- name: Notifications Account Funds Below Threshold Notification Content Structure
  property_count: 5
  slug: notifications-account-funds-below-threshold-notification-content-structure
- name: Notifications Account Funds Below Threshold Notification Structure
  property_count: 7
  slug: notifications-account-funds-below-threshold-notification-structure
- name: Notifications Account Holder Create Notification Structure
  property_count: 7
  slug: notifications-account-holder-create-notification-structure
- name: Notifications Account Holder Details Structure
  property_count: 15
  slug: notifications-account-holder-details-structure
- name: Notifications Account Holder Payout Notification Content Structure
  property_count: 17
  slug: notifications-account-holder-payout-notification-content-structure
- name: Notifications Account Holder Payout Notification Structure
  property_count: 7
  slug: notifications-account-holder-payout-notification-structure
- name: Notifications Account Holder Status Change Notification Content Structure
  property_count: 5
  slug: notifications-account-holder-status-change-notification-content-structure
- name: Notifications Account Holder Status Change Notification Structure
  property_count: 7
  slug: notifications-account-holder-status-change-notification-structure
- name: Notifications Account Holder Status Structure
  property_count: 5
  slug: notifications-account-holder-status-structure
- name: Notifications Account Holder Store Status Change Notification Content Structure
  property_count: 7
  slug: notifications-account-holder-store-status-change-notification-content-structure
- name: Notifications Account Holder Store Status Change Notification Structure
  property_count: 7
  slug: notifications-account-holder-store-status-change-notification-structure
- name: Notifications Account Holder Upcoming Deadline Notification Content Structure
  property_count: 4
  slug: notifications-account-holder-upcoming-deadline-notification-content-structure
- name: Notifications Account Holder Upcoming Deadline Notification Structure
  property_count: 7
  slug: notifications-account-holder-upcoming-deadline-notification-structure
- name: Notifications Account Holder Update Notification Structure
  property_count: 7
  slug: notifications-account-holder-update-notification-structure
- name: Notifications Account Holder Verification Notification Content Structure
  property_count: 7
  slug: notifications-account-holder-verification-notification-content-structure
- name: Notifications Account Holder Verification Notification Structure
  property_count: 7
  slug: notifications-account-holder-verification-notification-structure
- name: Notifications Account Payout State Structure
  property_count: 6
  slug: notifications-account-payout-state-structure
- name: Notifications Account Processing State Structure
  property_count: 5
  slug: notifications-account-processing-state-structure
- name: Notifications Account Update Notification Structure
  property_count: 7
  slug: notifications-account-update-notification-structure
- name: Notifications Amount Structure
  property_count: 2
  slug: notifications-amount-structure
- name: Notifications Bank Account Detail Structure
  property_count: 26
  slug: notifications-bank-account-detail-structure
- name: Notifications Beneficiary Setup Notification Content Structure
  property_count: 7
  slug: notifications-beneficiary-setup-notification-content-structure
- name: Notifications Beneficiary Setup Notification Structure
  property_count: 7
  slug: notifications-beneficiary-setup-notification-structure
- name: Notifications Business Details Structure
  property_count: 10
  slug: notifications-business-details-structure
- name: Notifications Close Account Response Structure
  property_count: 5
  slug: notifications-close-account-response-structure
- name: Notifications Compensate Negative Balance Notification Content Structure
  property_count: 1
  slug: notifications-compensate-negative-balance-notification-content-structure
- name: Notifications Compensate Negative Balance Notification Record Structure
  property_count: 3
  slug: notifications-compensate-negative-balance-notification-record-structure
- name: Notifications Compensate Negative Balance Notification Structure
  property_count: 7
  slug: notifications-compensate-negative-balance-notification-structure
- name: Notifications Create Account Holder Response Structure
  property_count: 12
  slug: notifications-create-account-holder-response-structure
- name: Notifications Create Account Response Structure
  property_count: 12
  slug: notifications-create-account-response-structure
- name: Notifications Direct Debit Initiated Notification Content Structure
  property_count: 7
  slug: notifications-direct-debit-initiated-notification-content-structure
- name: Notifications Direct Debit Initiated Notification Structure
  property_count: 7
  slug: notifications-direct-debit-initiated-notification-structure
- name: Notifications Error Field Type Structure
  property_count: 3
  slug: notifications-error-field-type-structure
- name: Notifications Field Type Structure
  property_count: 3
  slug: notifications-field-type-structure
- name: Notifications Individual Details Structure
  property_count: 2
  slug: notifications-individual-details-structure
- name: Notifications Kyc Check Result Structure
  property_count: 1
  slug: notifications-kyc-check-result-structure
- name: Notifications Kyc Check Status Data Structure
  property_count: 4
  slug: notifications-kyc-check-status-data-structure
- name: Notifications Kyc Check Summary Structure
  property_count: 2
  slug: notifications-kyc-check-summary-structure
- name: Notifications Kyc Legal Arrangement Check Result Structure
  property_count: 2
  slug: notifications-kyc-legal-arrangement-check-result-structure
- name: Notifications Kyc Legal Arrangement Entity Check Result Structure
  property_count: 3
  slug: notifications-kyc-legal-arrangement-entity-check-result-structure
- name: Notifications Kyc Payout Method Check Result Structure
  property_count: 2
  slug: notifications-kyc-payout-method-check-result-structure
- name: Notifications Kyc Shareholder Check Result Structure
  property_count: 4
  slug: notifications-kyc-shareholder-check-result-structure
- name: Notifications Kyc Signatory Check Result Structure
  property_count: 2
  slug: notifications-kyc-signatory-check-result-structure
- name: Notifications Kyc Ultimate Parent Company Check Result Structure
  property_count: 2
  slug: notifications-kyc-ultimate-parent-company-check-result-structure
- name: Notifications Kyc Verification Result Structure
  property_count: 7
  slug: notifications-kyc-verification-result-structure
- name: Notifications Legal Arrangement Detail Structure
  property_count: 9
  slug: notifications-legal-arrangement-detail-structure
- name: Notifications Legal Arrangement Entity Detail Structure
  property_count: 11
  slug: notifications-legal-arrangement-entity-detail-structure
- name: Notifications Local Date Structure
  property_count: 2
  slug: notifications-local-date-structure
- name: Notifications Message Structure
  property_count: 2
  slug: notifications-message-structure
- name: Notifications Notification Error Container Structure
  property_count: 2
  slug: notifications-notification-error-container-structure
- name: Notifications Notification Response Structure
  property_count: 1
  slug: notifications-notification-response-structure
- name: Notifications Operation Status Structure
  property_count: 2
  slug: notifications-operation-status-structure
- name: Notifications Payment Failure Notification Content Structure
  property_count: 6
  slug: notifications-payment-failure-notification-content-structure
- name: Notifications Payment Failure Notification Structure
  property_count: 7
  slug: notifications-payment-failure-notification-structure
- name: Notifications Payout Method Structure
  property_count: 5
  slug: notifications-payout-method-structure
- name: Notifications Payout Schedule Response Structure
  property_count: 2
  slug: notifications-payout-schedule-response-structure
- name: Notifications Personal Document Data Structure
  property_count: 5
  slug: notifications-personal-document-data-structure
- name: Notifications Refund Funds Transfer Notification Content Structure
  property_count: 5
  slug: notifications-refund-funds-transfer-notification-content-structure
- name: Notifications Refund Funds Transfer Notification Structure
  property_count: 7
  slug: notifications-refund-funds-transfer-notification-structure
- name: Notifications Refund Result Structure
  property_count: 3
  slug: notifications-refund-result-structure
- name: Notifications Report Available Notification Content Structure
  property_count: 5
  slug: notifications-report-available-notification-content-structure
- name: Notifications Report Available Notification Structure
  property_count: 7
  slug: notifications-report-available-notification-structure
- name: Notifications Scheduled Refunds Notification Content Structure
  property_count: 5
  slug: notifications-scheduled-refunds-notification-content-structure
- name: Notifications Scheduled Refunds Notification Structure
  property_count: 7
  slug: notifications-scheduled-refunds-notification-structure
- name: Notifications Shareholder Contact Structure
  property_count: 11
  slug: notifications-shareholder-contact-structure
- name: Notifications Signatory Contact Structure
  property_count: 10
  slug: notifications-signatory-contact-structure
- name: Notifications Split Amount Structure
  property_count: 2
  slug: notifications-split-amount-structure
- name: Notifications Split Structure
  property_count: 5
  slug: notifications-split-structure
- name: Notifications Store Detail Structure
  property_count: 15
  slug: notifications-store-detail-structure
- name: Notifications Transaction Structure
  property_count: 16
  slug: notifications-transaction-structure
- name: Notifications Transfer Funds Notification Content Structure
  property_count: 7
  slug: notifications-transfer-funds-notification-content-structure
- name: Notifications Transfer Funds Notification Structure
  property_count: 7
  slug: notifications-transfer-funds-notification-structure
- name: Notifications Ultimate Parent Company Business Details Structure
  property_count: 5
  slug: notifications-ultimate-parent-company-business-details-structure
- name: Notifications Ultimate Parent Company Structure
  property_count: 3
  slug: notifications-ultimate-parent-company-structure
- name: Notifications Update Account Holder Response Structure
  property_count: 11
  slug: notifications-update-account-holder-response-structure
- name: Notifications Update Account Response Structure
  property_count: 10
  slug: notifications-update-account-response-structure
- name: Notifications Vias Address Structure
  property_count: 6
  slug: notifications-vias-address-structure
- name: Notifications Vias Name Structure
  property_count: 4
  slug: notifications-vias-name-structure
- name: Notifications Vias Personal Data Structure
  property_count: 3
  slug: notifications-vias-personal-data-structure
- name: Notifications Vias Phone Number Structure
  property_count: 3
  slug: notifications-vias-phone-number-structure
- name: Payments Account Info Structure
  property_count: 19
  slug: payments-account-info-structure
- name: Payments Acct Info Structure
  property_count: 16
  slug: payments-acct-info-structure
- name: Payments Additional Data Airline Structure
  property_count: 28
  slug: payments-additional-data-airline-structure
- name: Payments Additional Data Car Rental Structure
  property_count: 23
  slug: payments-additional-data-car-rental-structure
- name: Payments Additional Data Common Structure
  property_count: 16
  slug: payments-additional-data-common-structure
- name: Payments Additional Data Level23 Structure
  property_count: 17
  slug: payments-additional-data-level23-structure
- name: Payments Additional Data Lodging Structure
  property_count: 16
  slug: payments-additional-data-lodging-structure
- name: Payments Additional Data Modifications Structure
  property_count: 1
  slug: payments-additional-data-modifications-structure
- name: Payments Additional Data Open Invoice Structure
  property_count: 18
  slug: payments-additional-data-open-invoice-structure
- name: Payments Additional Data Opi Structure
  property_count: 1
  slug: payments-additional-data-opi-structure
- name: Payments Additional Data Ratepay Structure
  property_count: 8
  slug: payments-additional-data-ratepay-structure
- name: Payments Additional Data Retry Structure
  property_count: 3
  slug: payments-additional-data-retry-structure
- name: Payments Additional Data Risk Standalone Structure
  property_count: 15
  slug: payments-additional-data-risk-standalone-structure
- name: Payments Additional Data Risk Structure
  property_count: 21
  slug: payments-additional-data-risk-structure
- name: Payments Additional Data Sub Merchant Structure
  property_count: 10
  slug: payments-additional-data-sub-merchant-structure
- name: Payments Additional Data Temporary Services Structure
  property_count: 9
  slug: payments-additional-data-temporary-services-structure
- name: Payments Additional Data Wallets Structure
  property_count: 6
  slug: payments-additional-data-wallets-structure
- name: Payments Additional Data3 D Secure Structure
  property_count: 6
  slug: payments-additional-data3-d-secure-structure
- name: Payments Address Structure
  property_count: 6
  slug: payments-address-structure
- name: Payments Adjust Authorisation Request Structure
  property_count: 11
  slug: payments-adjust-authorisation-request-structure
- name: Payments Amount Structure
  property_count: 2
  slug: payments-amount-structure
- name: Payments Application Info Structure
  property_count: 6
  slug: payments-application-info-structure
- name: Payments Authentication Result Request Structure
  property_count: 2
  slug: payments-authentication-result-request-structure
- name: Payments Authentication Result Response Structure
  property_count: 2
  slug: payments-authentication-result-response-structure
- name: Payments Bank Account Structure
  property_count: 9
  slug: payments-bank-account-structure
- name: Payments Browser Info Structure
  property_count: 9
  slug: payments-browser-info-structure
- name: Payments Cancel Or Refund Request Structure
  property_count: 9
  slug: payments-cancel-or-refund-request-structure
- name: Payments Cancel Request Structure
  property_count: 10
  slug: payments-cancel-request-structure
- name: Payments Capture Request Structure
  property_count: 11
  slug: payments-capture-request-structure
- name: Payments Card Structure
  property_count: 8
  slug: payments-card-structure
- name: Payments Common Field Structure
  property_count: 2
  slug: payments-common-field-structure
- name: Payments Device Render Options Structure
  property_count: 2
  slug: payments-device-render-options-structure
- name: Payments Donation Request Structure
  property_count: 6
  slug: payments-donation-request-structure
- name: Payments External Platform Structure
  property_count: 3
  slug: payments-external-platform-structure
- name: Payments Forex Quote Structure
  property_count: 12
  slug: payments-forex-quote-structure
- name: Payments Fraud Check Result Structure
  property_count: 3
  slug: payments-fraud-check-result-structure
- name: Payments Fraud Check Result Wrapper Structure
  property_count: 1
  slug: payments-fraud-check-result-wrapper-structure
- name: Payments Fraud Result Structure
  property_count: 2
  slug: payments-fraud-result-structure
- name: Payments Fund Destination Structure
  property_count: 9
  slug: payments-fund-destination-structure
- name: Payments Fund Source Structure
  property_count: 6
  slug: payments-fund-source-structure
- name: Payments Installments Structure
  property_count: 2
  slug: payments-installments-structure
- name: Payments Mandate Structure
  property_count: 8
  slug: payments-mandate-structure
- name: Payments Merchant Device Structure
  property_count: 3
  slug: payments-merchant-device-structure
- name: Payments Merchant Risk Indicator Structure
  property_count: 14
  slug: payments-merchant-risk-indicator-structure
- name: Payments Modification Result Structure
  property_count: 3
  slug: payments-modification-result-structure
- name: Payments Name Structure
  property_count: 2
  slug: payments-name-structure
- name: Payments Payment Request Structure
  property_count: 53
  slug: payments-payment-request-structure
- name: Payments Payment Request3D Structure
  property_count: 45
  slug: payments-payment-request3d-structure
- name: Payments Payment Request3Ds2 Structure
  property_count: 45
  slug: payments-payment-request3ds2-structure
- name: Payments Payment Result Structure
  property_count: 11
  slug: payments-payment-result-structure
- name: Payments Phone Structure
  property_count: 2
  slug: payments-phone-structure
- name: Payments Platform Chargeback Logic Structure
  property_count: 3
  slug: payments-platform-chargeback-logic-structure
- name: Payments Recurring Structure
  property_count: 5
  slug: payments-recurring-structure
- name: Payments Refund Request Structure
  property_count: 11
  slug: payments-refund-request-structure
- name: Payments Response Additional Data Billing Address Structure
  property_count: 6
  slug: payments-response-additional-data-billing-address-structure
- name: Payments Response Additional Data Card Structure
  property_count: 8
  slug: payments-response-additional-data-card-structure
- name: Payments Response Additional Data Common Structure
  property_count: 59
  slug: payments-response-additional-data-common-structure
- name: Payments Response Additional Data Domestic Error Structure
  property_count: 2
  slug: payments-response-additional-data-domestic-error-structure
- name: Payments Response Additional Data Installments Structure
  property_count: 12
  slug: payments-response-additional-data-installments-structure
- name: Payments Response Additional Data Network Tokens Structure
  property_count: 3
  slug: payments-response-additional-data-network-tokens-structure
- name: Payments Response Additional Data Opi Structure
  property_count: 1
  slug: payments-response-additional-data-opi-structure
- name: Payments Response Additional Data Sepa Structure
  property_count: 3
  slug: payments-response-additional-data-sepa-structure
- name: Payments Response Additional Data3 D Secure Structure
  property_count: 5
  slug: payments-response-additional-data3-d-secure-structure
- name: Payments Sdk Ephem Pub Key Structure
  property_count: 4
  slug: payments-sdk-ephem-pub-key-structure
- name: Payments Shopper Interaction Device Structure
  property_count: 3
  slug: payments-shopper-interaction-device-structure
- name: Payments Split Amount Structure
  property_count: 2
  slug: payments-split-amount-structure
- name: Payments Split Structure
  property_count: 5
  slug: payments-split-structure
- name: Payments Sub Merchant Structure
  property_count: 5
  slug: payments-sub-merchant-structure
- name: Payments Technical Cancel Request Structure
  property_count: 10
  slug: payments-technical-cancel-request-structure
- name: Payments Three D Secure Data Structure
  property_count: 12
  slug: payments-three-d-secure-data-structure
- name: Payments Three Ds Requestor Authentication Info Structure
  property_count: 3
  slug: payments-three-ds-requestor-authentication-info-structure
- name: Payments Three Ds Requestor Prior Authentication Info Structure
  property_count: 4
  slug: payments-three-ds-requestor-prior-authentication-info-structure
- name: Payments Three Ds1 Result Structure
  property_count: 6
  slug: payments-three-ds1-result-structure
- name: Payments Three Ds2 Request Data Structure
  property_count: 39
  slug: payments-three-ds2-request-data-structure
- name: Payments Three Ds2 Result Request Structure
  property_count: 2
  slug: payments-three-ds2-result-request-structure
- name: Payments Three Ds2 Result Response Structure
  property_count: 1
  slug: payments-three-ds2-result-response-structure
- name: Payments Three Ds2 Result Structure
  property_count: 14
  slug: payments-three-ds2-result-structure
- name: Payments Void Pending Refund Request Structure
  property_count: 11
  slug: payments-void-pending-refund-request-structure
- name: Payouts Address Structure
  property_count: 6
  slug: payouts-address-structure
- name: Payouts Amount Structure
  property_count: 2
  slug: payouts-amount-structure
- name: Payouts Bank Account Structure
  property_count: 9
  slug: payouts-bank-account-structure
- name: Payouts Card Structure
  property_count: 8
  slug: payouts-card-structure
- name: Payouts Fraud Check Result Structure
  property_count: 3
  slug: payouts-fraud-check-result-structure
- name: Payouts Fraud Check Result Wrapper Structure
  property_count: 1
  slug: payouts-fraud-check-result-wrapper-structure
- name: Payouts Fraud Result Structure
  property_count: 2
  slug: payouts-fraud-result-structure
- name: Payouts Fund Source Structure
  property_count: 6
  slug: payouts-fund-source-structure
- name: Payouts Modify Request Structure
  property_count: 3
  slug: payouts-modify-request-structure
- name: Payouts Modify Response Structure
  property_count: 3
  slug: payouts-modify-response-structure
- name: Payouts Name Structure
  property_count: 2
  slug: payouts-name-structure
- name: Payouts Payout Request Structure
  property_count: 14
  slug: payouts-payout-request-structure
- name: Payouts Payout Response Structure
  property_count: 11
  slug: payouts-payout-response-structure
- name: Payouts Recurring Structure
  property_count: 5
  slug: payouts-recurring-structure
- name: Payouts Response Additional Data Billing Address Structure
  property_count: 6
  slug: payouts-response-additional-data-billing-address-structure
- name: Payouts Response Additional Data Card Structure
  property_count: 8
  slug: payouts-response-additional-data-card-structure
- name: Payouts Response Additional Data Common Structure
  property_count: 59
  slug: payouts-response-additional-data-common-structure
- name: Payouts Response Additional Data Domestic Error Structure
  property_count: 2
  slug: payouts-response-additional-data-domestic-error-structure
- name: Payouts Response Additional Data Installments Structure
  property_count: 12
  slug: payouts-response-additional-data-installments-structure
- name: Payouts Response Additional Data Network Tokens Structure
  property_count: 3
  slug: payouts-response-additional-data-network-tokens-structure
- name: Payouts Response Additional Data Opi Structure
  property_count: 1
  slug: payouts-response-additional-data-opi-structure
- name: Payouts Response Additional Data Sepa Structure
  property_count: 3
  slug: payouts-response-additional-data-sepa-structure
- name: Payouts Response Additional Data3 D Secure Structure
  property_count: 5
  slug: payouts-response-additional-data3-d-secure-structure
- name: Payouts Store Detail And Submit Request Structure
  property_count: 19
  slug: payouts-store-detail-and-submit-request-structure
- name: Payouts Store Detail And Submit Response Structure
  property_count: 4
  slug: payouts-store-detail-and-submit-response-structure
- name: Payouts Store Detail Request Structure
  property_count: 16
  slug: payouts-store-detail-request-structure
- name: Payouts Store Detail Response Structure
  property_count: 4
  slug: payouts-store-detail-response-structure
- name: Payouts Submit Request Structure
  property_count: 15
  slug: payouts-submit-request-structure
- name: Payouts Submit Response Structure
  property_count: 4
  slug: payouts-submit-response-structure
- name: Pos Terminal Address Structure
  property_count: 6
  slug: pos-terminal-address-structure
- name: Pos Terminal Assign Terminals Request Structure
  property_count: 5
  slug: pos-terminal-assign-terminals-request-structure
- name: Pos Terminal Assign Terminals Response Structure
  property_count: 1
  slug: pos-terminal-assign-terminals-response-structure
- name: Pos Terminal Find Terminal Request Structure
  property_count: 1
  slug: pos-terminal-find-terminal-request-structure
- name: Pos Terminal Find Terminal Response Structure
  property_count: 5
  slug: pos-terminal-find-terminal-response-structure
- name: Pos Terminal Get Stores Under Account Request Structure
  property_count: 2
  slug: pos-terminal-get-stores-under-account-request-structure
- name: Pos Terminal Get Stores Under Account Response Structure
  property_count: 1
  slug: pos-terminal-get-stores-under-account-response-structure
- name: Pos Terminal Get Terminal Details Request Structure
  property_count: 1
  slug: pos-terminal-get-terminal-details-request-structure
- name: Pos Terminal Get Terminal Details Response Structure
  property_count: 25
  slug: pos-terminal-get-terminal-details-response-structure
- name: Pos Terminal Get Terminals Under Account Request Structure
  property_count: 3
  slug: pos-terminal-get-terminals-under-account-request-structure
- name: Pos Terminal Get Terminals Under Account Response Structure
  property_count: 3
  slug: pos-terminal-get-terminals-under-account-response-structure
- name: Pos Terminal Merchant Account Structure
  property_count: 4
  slug: pos-terminal-merchant-account-structure
- name: Pos Terminal Store Structure
  property_count: 6
  slug: pos-terminal-store-structure
- name: Recurring Address Structure
  property_count: 6
  slug: recurring-address-structure
- name: Recurring Amount Structure
  property_count: 2
  slug: recurring-amount-structure
- name: Recurring Bank Account Structure
  property_count: 9
  slug: recurring-bank-account-structure
- name: Recurring Card Structure
  property_count: 8
  slug: recurring-card-structure
- name: Recurring Create Permit Request Structure
  property_count: 4
  slug: recurring-create-permit-request-structure
- name: Recurring Create Permit Result Structure
  property_count: 2
  slug: recurring-create-permit-result-structure
- name: Recurring Disable Permit Request Structure
  property_count: 2
  slug: recurring-disable-permit-request-structure
- name: Recurring Disable Permit Result Structure
  property_count: 2
  slug: recurring-disable-permit-result-structure
- name: Recurring Disable Request Structure
  property_count: 4
  slug: recurring-disable-request-structure
- name: Recurring Disable Result Structure
  property_count: 1
  slug: recurring-disable-result-structure
- name: Recurring Name Structure
  property_count: 2
  slug: recurring-name-structure
- name: Recurring Notify Shopper Request Structure
  property_count: 9
  slug: recurring-notify-shopper-request-structure
- name: Recurring Notify Shopper Result Structure
  property_count: 7
  slug: recurring-notify-shopper-result-structure
- name: Recurring Permit Restriction Structure
  property_count: 3
  slug: recurring-permit-restriction-structure
- name: Recurring Permit Result Structure
  property_count: 2
  slug: recurring-permit-result-structure
- name: Recurring Permit Structure
  property_count: 5
  slug: recurring-permit-structure
- name: Recurring Recurring Detail Structure
  property_count: 17
  slug: recurring-recurring-detail-structure
- name: Recurring Recurring Detail Wrapper Structure
  property_count: 1
  slug: recurring-recurring-detail-wrapper-structure
- name: Recurring Recurring Details Request Structure
  property_count: 3
  slug: recurring-recurring-details-request-structure
- name: Recurring Recurring Details Result Structure
  property_count: 4
  slug: recurring-recurring-details-result-structure
- name: Recurring Recurring Structure
  property_count: 5
  slug: recurring-recurring-structure
- name: Recurring Schedule Account Updater Request Structure
  property_count: 6
  slug: recurring-schedule-account-updater-request-structure
- name: Recurring Schedule Account Updater Result Structure
  property_count: 2
  slug: recurring-schedule-account-updater-result-structure
- name: Recurring Token Details Structure
  property_count: 2
  slug: recurring-token-details-structure
- name: Report Webhooks Balance Platform Notification Response Structure
  property_count: 1
  slug: report-webhooks-balance-platform-notification-response-structure
- name: Report Webhooks Report Notification Data Structure
  property_count: 7
  slug: report-webhooks-report-notification-data-structure
- name: Report Webhooks Report Notification Request Structure
  property_count: 3
  slug: report-webhooks-report-notification-request-structure
- name: Report Webhooks Resource Reference Structure
  property_count: 3
  slug: report-webhooks-resource-reference-structure
- name: Report Webhooks Resource Structure
  property_count: 3
  slug: report-webhooks-resource-structure
- name: Stored Value Amount Structure
  property_count: 2
  slug: stored-value-amount-structure
- name: Stored Value Stored Value Balance Check Request Structure
  property_count: 8
  slug: stored-value-stored-value-balance-check-request-structure
- name: Stored Value Stored Value Balance Check Response Structure
  property_count: 5
  slug: stored-value-stored-value-balance-check-response-structure
- name: Stored Value Stored Value Balance Merge Request Structure
  property_count: 9
  slug: stored-value-stored-value-balance-merge-request-structure
- name: Stored Value Stored Value Balance Merge Response Structure
  property_count: 6
  slug: stored-value-stored-value-balance-merge-response-structure
- name: Stored Value Stored Value Issue Request Structure
  property_count: 8
  slug: stored-value-stored-value-issue-request-structure
- name: Stored Value Stored Value Issue Response Structure
  property_count: 7
  slug: stored-value-stored-value-issue-response-structure
- name: Stored Value Stored Value Load Request Structure
  property_count: 9
  slug: stored-value-stored-value-load-request-structure
- name: Stored Value Stored Value Load Response Structure
  property_count: 6
  slug: stored-value-stored-value-load-response-structure
- name: Stored Value Stored Value Status Change Request Structure
  property_count: 9
  slug: stored-value-stored-value-status-change-request-structure
- name: Stored Value Stored Value Status Change Response Structure
  property_count: 6
  slug: stored-value-stored-value-status-change-response-structure
- name: Stored Value Stored Value Void Request Structure
  property_count: 6
  slug: stored-value-stored-value-void-request-structure
- name: Stored Value Stored Value Void Response Structure
  property_count: 5
  slug: stored-value-stored-value-void-response-structure
- name: Terminal Abort Request Structure
  property_count: 3
  slug: terminal-abort-request-structure
- name: Terminal Account Type Structure
  property_count: 0
  slug: terminal-account-type-structure
- name: Terminal Admin Request Structure
  property_count: 1
  slug: terminal-admin-request-structure
- name: Terminal Admin Response Structure
  property_count: 1
  slug: terminal-admin-response-structure
- name: Terminal Alignment Structure
  property_count: 0
  slug: terminal-alignment-structure
- name: Terminal Allowed Product Structure
  property_count: 4
  slug: terminal-allowed-product-structure
- name: Terminal Amounts Req Structure
  property_count: 8
  slug: terminal-amounts-req-structure
- name: Terminal Amounts Resp Structure
  property_count: 6
  slug: terminal-amounts-resp-structure
- name: Terminal Area Size Structure
  property_count: 2
  slug: terminal-area-size-structure
- name: Terminal Authentication Method Structure
  property_count: 0
  slug: terminal-authentication-method-structure
- name: Terminal Balance Inquiry Request Structure
  property_count: 2
  slug: terminal-balance-inquiry-request-structure
- name: Terminal Balance Inquiry Response Structure
  property_count: 4
  slug: terminal-balance-inquiry-response-structure
- name: Terminal Barcode Type Structure
  property_count: 0
  slug: terminal-barcode-type-structure
- name: Terminal Captured Signature Structure
  property_count: 2
  slug: terminal-captured-signature-structure
- name: Terminal Card Acquisition Request Structure
  property_count: 2
  slug: terminal-card-acquisition-request-structure
- name: Terminal Card Acquisition Response Structure
  property_count: 7
  slug: terminal-card-acquisition-response-structure
- name: Terminal Card Acquisition Transaction Structure
  property_count: 9
  slug: terminal-card-acquisition-transaction-structure
- name: Terminal Card Data Structure
  property_count: 11
  slug: terminal-card-data-structure
- name: Terminal Card Holder Pin Structure
  property_count: 3
  slug: terminal-card-holder-pin-structure
- name: Terminal Card Reader Apdu Request Structure
  property_count: 6
  slug: terminal-card-reader-apdu-request-structure
- name: Terminal Card Reader Apdu Response Structure
  property_count: 3
  slug: terminal-card-reader-apdu-response-structure
- name: Terminal Cash Handling Device Structure
  property_count: 3
  slug: terminal-cash-handling-device-structure
- name: Terminal Character Height Structure
  property_count: 0
  slug: terminal-character-height-structure
- name: Terminal Character Style Structure
  property_count: 0
  slug: terminal-character-style-structure
- name: Terminal Character Width Structure
  property_count: 0
  slug: terminal-character-width-structure
- name: Terminal Check Data Structure
  property_count: 7
  slug: terminal-check-data-structure
- name: Terminal Coins Or Bills Structure
  property_count: 2
  slug: terminal-coins-or-bills-structure
- name: Terminal Color Structure
  property_count: 0
  slug: terminal-color-structure
- name: Terminal Converted Amount Structure
  property_count: 2
  slug: terminal-converted-amount-structure
- name: Terminal Currency Conversion Structure
  property_count: 6
  slug: terminal-currency-conversion-structure
- name: Terminal Customer Order Req Structure
  property_count: 0
  slug: terminal-customer-order-req-structure
- name: Terminal Customer Order Structure
  property_count: 10
  slug: terminal-customer-order-structure
- name: Terminal Device Structure
  property_count: 0
  slug: terminal-device-structure
- name: Terminal Diagnosis Request Structure
  property_count: 3
  slug: terminal-diagnosis-request-structure
- name: Terminal Diagnosis Response Structure
  property_count: 4
  slug: terminal-diagnosis-response-structure
- name: Terminal Display Output Structure
  property_count: 7
  slug: terminal-display-output-structure
- name: Terminal Display Request Structure
  property_count: 1
  slug: terminal-display-request-structure
- name: Terminal Display Response Structure
  property_count: 1
  slug: terminal-display-response-structure
- name: Terminal Document Qualifier Structure
  property_count: 0
  slug: terminal-document-qualifier-structure
- name: Terminal Enable Service Request Structure
  property_count: 3
  slug: terminal-enable-service-request-structure
- name: Terminal Enable Service Response Structure
  property_count: 1
  slug: terminal-enable-service-response-structure
- name: Terminal Entry Mode Structure
  property_count: 0
  slug: terminal-entry-mode-structure
- name: Terminal Error Condition Structure
  property_count: 0
  slug: terminal-error-condition-structure
- name: Terminal Event Notification Structure
  property_count: 7
  slug: terminal-event-notification-structure
- name: Terminal Event To Notify Structure
  property_count: 0
  slug: terminal-event-to-notify-structure
- name: Terminal Force Entry Mode Structure
  property_count: 0
  slug: terminal-force-entry-mode-structure
- name: Terminal Generic Profile Structure
  property_count: 0
  slug: terminal-generic-profile-structure
- name: Terminal Geographic Coordinates Structure
  property_count: 2
  slug: terminal-geographic-coordinates-structure
- name: Terminal Geolocation Structure
  property_count: 2
  slug: terminal-geolocation-structure
- name: Terminal Get Totals Request Structure
  property_count: 2
  slug: terminal-get-totals-request-structure
- name: Terminal Get Totals Response Structure
  property_count: 3
  slug: terminal-get-totals-response-structure
- name: Terminal Global Status Structure
  property_count: 0
  slug: terminal-global-status-structure
- name: Terminal Host Status Structure
  property_count: 2
  slug: terminal-host-status-structure
- name: Terminal Icc Reset Data Structure
  property_count: 2
  slug: terminal-icc-reset-data-structure
- name: Terminal Identification Support Structure
  property_count: 0
  slug: terminal-identification-support-structure
- name: Terminal Identification Type Structure
  property_count: 0
  slug: terminal-identification-type-structure
- name: Terminal Info Qualify Structure
  property_count: 0
  slug: terminal-info-qualify-structure
- name: Terminal Input Command Structure
  property_count: 0
  slug: terminal-input-command-structure
- name: Terminal Input Data Structure
  property_count: 21
  slug: terminal-input-data-structure
- name: Terminal Input Request Structure
  property_count: 2
  slug: terminal-input-request-structure
- name: Terminal Input Response Structure
  property_count: 2
  slug: terminal-input-response-structure
- name: Terminal Input Result Structure
  property_count: 4
  slug: terminal-input-result-structure
- name: Terminal Input Structure
  property_count: 7
  slug: terminal-input-structure
- name: Terminal Input Update Structure
  property_count: 7
  slug: terminal-input-update-structure
- name: Terminal Instalment Structure
  property_count: 10
  slug: terminal-instalment-structure
- name: Terminal Instalment Type Structure
  property_count: 0
  slug: terminal-instalment-type-structure
- name: Terminal Login Request Structure
  property_count: 10
  slug: terminal-login-request-structure
- name: Terminal Login Response Structure
  property_count: 4
  slug: terminal-login-response-structure
- name: Terminal Logout Request Structure
  property_count: 1
  slug: terminal-logout-request-structure
- name: Terminal Logout Response Structure
  property_count: 1
  slug: terminal-logout-response-structure
- name: Terminal Loyalty Account Id Structure
  property_count: 4
  slug: terminal-loyalty-account-id-structure
- name: Terminal Loyalty Account Req Structure
  property_count: 2
  slug: terminal-loyalty-account-req-structure
- name: Terminal Loyalty Account Status Structure
  property_count: 4
  slug: terminal-loyalty-account-status-structure
- name: Terminal Loyalty Account Structure
  property_count: 2
  slug: terminal-loyalty-account-structure
- name: Terminal Loyalty Acquirer Data Structure
  property_count: 4
  slug: terminal-loyalty-acquirer-data-structure
- name: Terminal Loyalty Amount Structure
  property_count: 3
  slug: terminal-loyalty-amount-structure
- name: Terminal Loyalty Data Structure
  property_count: 3
  slug: terminal-loyalty-data-structure
- name: Terminal Loyalty Handling Structure
  property_count: 0
  slug: terminal-loyalty-handling-structure
- name: Terminal Loyalty Request Structure
  property_count: 3
  slug: terminal-loyalty-request-structure
- name: Terminal Loyalty Response Structure
  property_count: 5
  slug: terminal-loyalty-response-structure
- name: Terminal Loyalty Result Structure
  property_count: 5
  slug: terminal-loyalty-result-structure
- name: Terminal Loyalty Totals Structure
  property_count: 3
  slug: terminal-loyalty-totals-structure
- name: Terminal Loyalty Transaction Structure
  property_count: 6
  slug: terminal-loyalty-transaction-structure
- name: Terminal Loyalty Transaction Type Structure
  property_count: 0
  slug: terminal-loyalty-transaction-type-structure
- name: Terminal Loyalty Unit Structure
  property_count: 0
  slug: terminal-loyalty-unit-structure
- name: Terminal Menu Entry Structure
  property_count: 6
  slug: terminal-menu-entry-structure
- name: Terminal Menu Entry Tag Structure
  property_count: 0
  slug: terminal-menu-entry-tag-structure
- name: Terminal Message Category Structure
  property_count: 0
  slug: terminal-message-category-structure
- name: Terminal Message Class Structure
  property_count: 0
  slug: terminal-message-class-structure
- name: Terminal Message Header Structure
  property_count: 8
  slug: terminal-message-header-structure
- name: Terminal Message Reference Structure
  property_count: 5
  slug: terminal-message-reference-structure
- name: Terminal Message Type Structure
  property_count: 0
  slug: terminal-message-type-structure
- name: Terminal Mobile Data Structure
  property_count: 6
  slug: terminal-mobile-data-structure
- name: Terminal Original Poi Transaction Structure
  property_count: 9
  slug: terminal-original-poi-transaction-structure
- name: Terminal Output Barcode Structure
  property_count: 2
  slug: terminal-output-barcode-structure
- name: Terminal Output Content Structure
  property_count: 5
  slug: terminal-output-content-structure
- name: Terminal Output Format Structure
  property_count: 0
  slug: terminal-output-format-structure
- name: Terminal Output Result Structure
  property_count: 3
  slug: terminal-output-result-structure
- name: Terminal Output Text Structure
  property_count: 11
  slug: terminal-output-text-structure
- name: Terminal Payment Account Req Structure
  property_count: 3
  slug: terminal-payment-account-req-structure
- name: Terminal Payment Account Status Structure
  property_count: 4
  slug: terminal-payment-account-status-structure
- name: Terminal Payment Acquirer Data Structure
  property_count: 6
  slug: terminal-payment-acquirer-data-structure
- name: Terminal Payment Data Structure
  property_count: 7
  slug: terminal-payment-data-structure
- name: Terminal Payment Instrument Data Structure
  property_count: 6
  slug: terminal-payment-instrument-data-structure
- name: Terminal Payment Instrument Type Structure
  property_count: 0
  slug: terminal-payment-instrument-type-structure
- name: Terminal Payment Receipt Structure
  property_count: 4
  slug: terminal-payment-receipt-structure
- name: Terminal Payment Request Structure
  property_count: 4
  slug: terminal-payment-request-structure
- name: Terminal Payment Response Structure
  property_count: 7
  slug: terminal-payment-response-structure
- name: Terminal Payment Result Structure
  property_count: 13
  slug: terminal-payment-result-structure
- name: Terminal Payment Token Structure
  property_count: 3
  slug: terminal-payment-token-structure
- name: Terminal Payment Totals Structure
  property_count: 3
  slug: terminal-payment-totals-structure
- name: Terminal Payment Transaction Structure
  property_count: 4
  slug: terminal-payment-transaction-structure
- name: Terminal Payment Type Structure
  property_count: 0
  slug: terminal-payment-type-structure
- name: Terminal Performed Transaction Structure
  property_count: 6
  slug: terminal-performed-transaction-structure
- name: Terminal Period Unit Structure
  property_count: 0
  slug: terminal-period-unit-structure
- name: Terminal Pin Format Structure
  property_count: 0
  slug: terminal-pin-format-structure
- name: Terminal Pin Request Type Structure
  property_count: 0
  slug: terminal-pin-request-type-structure
- name: Terminal Poi Capabilities Structure
  property_count: 0
  slug: terminal-poi-capabilities-structure
- name: Terminal Poi Data Structure
  property_count: 2
  slug: terminal-poi-data-structure
- name: Terminal Poi Profile Structure
  property_count: 2
  slug: terminal-poi-profile-structure
- name: Terminal Poi Software Structure
  property_count: 4
  slug: terminal-poi-software-structure
- name: Terminal Poi Status Structure
  property_count: 8
  slug: terminal-poi-status-structure
- name: Terminal Poi System Data Structure
  property_count: 4
  slug: terminal-poi-system-data-structure
- name: Terminal Poi Terminal Data Structure
  property_count: 4
  slug: terminal-poi-terminal-data-structure
- name: Terminal Point Structure
  property_count: 2
  slug: terminal-point-structure
- name: Terminal Predefined Content Structure
  property_count: 2
  slug: terminal-predefined-content-structure
- name: Terminal Print Output Structure
  property_count: 5
  slug: terminal-print-output-structure
- name: Terminal Print Request Structure
  property_count: 1
  slug: terminal-print-request-structure
- name: Terminal Print Response Structure
  property_count: 2
  slug: terminal-print-response-structure
- name: Terminal Printer Status Structure
  property_count: 0
  slug: terminal-printer-status-structure
- name: Terminal Rebates Structure
  property_count: 3
  slug: terminal-rebates-structure
- name: Terminal Reconciliation Request Structure
  property_count: 3
  slug: terminal-reconciliation-request-structure
- name: Terminal Reconciliation Response Structure
  property_count: 4
  slug: terminal-reconciliation-response-structure
- name: Terminal Reconciliation Type Structure
  property_count: 0
  slug: terminal-reconciliation-type-structure
- name: Terminal Repeated Message Response Structure
  property_count: 2
  slug: terminal-repeated-message-response-structure
- name: Terminal Repeated Response Message Body Structure
  property_count: 6
  slug: terminal-repeated-response-message-body-structure
- name: Terminal Response Mode Structure
  property_count: 0
  slug: terminal-response-mode-structure
- name: Terminal Response Structure
  property_count: 3
  slug: terminal-response-structure
- name: Terminal Result Structure
  property_count: 0
  slug: terminal-result-structure
- name: Terminal Reversal Reason Structure
  property_count: 0
  slug: terminal-reversal-reason-structure
- name: Terminal Reversal Request Structure
  property_count: 5
  slug: terminal-reversal-request-structure
- name: Terminal Reversal Response Structure
  property_count: 6
  slug: terminal-reversal-response-structure
- name: Terminal Sale Capabilities Structure
  property_count: 0
  slug: terminal-sale-capabilities-structure
- name: Terminal Sale Data Structure
  property_count: 12
  slug: terminal-sale-data-structure
- name: Terminal Sale Item Rebate Structure
  property_count: 7
  slug: terminal-sale-item-rebate-structure
- name: Terminal Sale Item Structure
  property_count: 11
  slug: terminal-sale-item-structure
- name: Terminal Sale Software Structure
  property_count: 4
  slug: terminal-sale-software-structure
- name: Terminal Sale Terminal Data Structure
  property_count: 1
  slug: terminal-sale-terminal-data-structure
- name: Terminal Sale To Issuer Data Structure
  property_count: 1
  slug: terminal-sale-to-issuer-data-structure
- name: Terminal Security Trailer Structure
  property_count: 5
  slug: terminal-security-trailer-structure
- name: Terminal Sensitive Card Data Structure
  property_count: 4
  slug: terminal-sensitive-card-data-structure
- name: Terminal Sensitive Mobile Data Structure
  property_count: 3
  slug: terminal-sensitive-mobile-data-structure
- name: Terminal Service Profiles Structure
  property_count: 0
  slug: terminal-service-profiles-structure
- name: Terminal Services Enabled Structure
  property_count: 0
  slug: terminal-services-enabled-structure
- name: Terminal Sound Action Structure
  property_count: 0
  slug: terminal-sound-action-structure
- name: Terminal Sound Content Structure
  property_count: 4
  slug: terminal-sound-content-structure
- name: Terminal Sound Format Structure
  property_count: 0
  slug: terminal-sound-format-structure
- name: Terminal Stored Value Account Id Structure
  property_count: 7
  slug: terminal-stored-value-account-id-structure
- name: Terminal Stored Value Account Status Structure
  property_count: 2
  slug: terminal-stored-value-account-status-structure
- name: Terminal Stored Value Account Type Structure
  property_count: 0
  slug: terminal-stored-value-account-type-structure
- name: Terminal Stored Value Data Structure
  property_count: 8
  slug: terminal-stored-value-data-structure
- name: Terminal Stored Value Request Structure
  property_count: 3
  slug: terminal-stored-value-request-structure
- name: Terminal Stored Value Response Structure
  property_count: 5
  slug: terminal-stored-value-response-structure
- name: Terminal Stored Value Result Structure
  property_count: 7
  slug: terminal-stored-value-result-structure
- name: Terminal Stored Value Transaction Type Structure
  property_count: 0
  slug: terminal-stored-value-transaction-type-structure
- name: Terminal Terminal Environment Structure
  property_count: 0
  slug: terminal-terminal-environment-structure
- name: Terminal Token Requested Type Structure
  property_count: 0
  slug: terminal-token-requested-type-structure
- name: Terminal Total Details Structure
  property_count: 0
  slug: terminal-total-details-structure
- name: Terminal Total Filter Structure
  property_count: 5
  slug: terminal-total-filter-structure
- name: Terminal Track Data Structure
  property_count: 3
  slug: terminal-track-data-structure
- name: Terminal Track Format Structure
  property_count: 0
  slug: terminal-track-format-structure
- name: Terminal Transaction Action Structure
  property_count: 0
  slug: terminal-transaction-action-structure
- name: Terminal Transaction Conditions Structure
  property_count: 9
  slug: terminal-transaction-conditions-structure
- name: Terminal Transaction Id Type Structure
  property_count: 2
  slug: terminal-transaction-id-type-structure
- name: Terminal Transaction Status Request Structure
  property_count: 3
  slug: terminal-transaction-status-request-structure
- name: Terminal Transaction Status Response Structure
  property_count: 3
  slug: terminal-transaction-status-response-structure
- name: Terminal Transaction Totals Structure
  property_count: 14
  slug: terminal-transaction-totals-structure
- name: Terminal Transaction Type Structure
  property_count: 0
  slug: terminal-transaction-type-structure
- name: Terminal Type Code Structure
  property_count: 0
  slug: terminal-type-code-structure
- name: Terminal Unit Of Measure Structure
  property_count: 0
  slug: terminal-unit-of-measure-structure
- name: Terminal Utm Coordinates Structure
  property_count: 3
  slug: terminal-utm-coordinates-structure
- name: Test Cards Avs Address Structure
  property_count: 2
  slug: test-cards-avs-address-structure
- name: Test Cards Create Test Card Ranges Request Structure
  property_count: 3
  slug: test-cards-create-test-card-ranges-request-structure
- name: Test Cards Create Test Card Ranges Result Structure
  property_count: 1
  slug: test-cards-create-test-card-ranges-result-structure
- name: Test Cards Test Card Range Creation Result Structure
  property_count: 4
  slug: test-cards-test-card-range-creation-result-structure
- name: Test Cards Test Card Range Structure
  property_count: 10
  slug: test-cards-test-card-range-structure
- name: Transaction Webhooks Amount Structure
  property_count: 2
  slug: transaction-webhooks-amount-structure
- name: Transaction Webhooks Balance Platform Notification Response Structure
  property_count: 1
  slug: transaction-webhooks-balance-platform-notification-response-structure
- name: Transaction Webhooks Resource Reference Structure
  property_count: 3
  slug: transaction-webhooks-resource-reference-structure
- name: Transaction Webhooks Resource Structure
  property_count: 3
  slug: transaction-webhooks-resource-structure
- name: Transaction Webhooks Transaction Notification Request V4 Structure
  property_count: 3
  slug: transaction-webhooks-transaction-notification-request-v4-structure
- name: Transaction Webhooks Transaction Structure
  property_count: 10
  slug: transaction-webhooks-transaction-structure
- name: Transaction Webhooks Transfer Data Structure
  property_count: 2
  slug: transaction-webhooks-transfer-data-structure
- name: Transfer Webhooks Additional Bank Identification Structure
  property_count: 2
  slug: transfer-webhooks-additional-bank-identification-structure
- name: Transfer Webhooks Address Structure
  property_count: 6
  slug: transfer-webhooks-address-structure
- name: Transfer Webhooks Amount Adjustment Structure
  property_count: 3
  slug: transfer-webhooks-amount-adjustment-structure
- name: Transfer Webhooks Amount Structure
  property_count: 2
  slug: transfer-webhooks-amount-structure
- name: Transfer Webhooks Au Local Account Identification Structure
  property_count: 3
  slug: transfer-webhooks-au-local-account-identification-structure
- name: Transfer Webhooks Balance Mutation Structure
  property_count: 4
  slug: transfer-webhooks-balance-mutation-structure
- name: Transfer Webhooks Balance Platform Notification Response Structure
  property_count: 1
  slug: transfer-webhooks-balance-platform-notification-response-structure
- name: Transfer Webhooks Bank Account V3 Structure
  property_count: 2
  slug: transfer-webhooks-bank-account-v3-structure
- name: Transfer Webhooks Bank Category Data Structure
  property_count: 2
  slug: transfer-webhooks-bank-category-data-structure
- name: Transfer Webhooks Br Local Account Identification Structure
  property_count: 4
  slug: transfer-webhooks-br-local-account-identification-structure
- name: Transfer Webhooks Ca Local Account Identification Structure
  property_count: 5
  slug: transfer-webhooks-ca-local-account-identification-structure
- name: Transfer Webhooks Counterparty V3 Structure
  property_count: 4
  slug: transfer-webhooks-counterparty-v3-structure
- name: Transfer Webhooks Cz Local Account Identification Structure
  property_count: 3
  slug: transfer-webhooks-cz-local-account-identification-structure
- name: Transfer Webhooks Dk Local Account Identification Structure
  property_count: 3
  slug: transfer-webhooks-dk-local-account-identification-structure
- name: Transfer Webhooks Hk Local Account Identification Structure
  property_count: 3
  slug: transfer-webhooks-hk-local-account-identification-structure
- name: Transfer Webhooks Hu Local Account Identification Structure
  property_count: 2
  slug: transfer-webhooks-hu-local-account-identification-structure
- name: Transfer Webhooks Iban Account Identification Structure
  property_count: 2
  slug: transfer-webhooks-iban-account-identification-structure
- name: Transfer Webhooks Internal Category Data Structure
  property_count: 3
  slug: transfer-webhooks-internal-category-data-structure
- name: Transfer Webhooks Issued Card Structure
  property_count: 8
  slug: transfer-webhooks-issued-card-structure
- name: Transfer Webhooks Merchant Data Structure
  property_count: 5
  slug: transfer-webhooks-merchant-data-structure
- name: Transfer Webhooks Modification Structure
  property_count: 5
  slug: transfer-webhooks-modification-structure
- name: Transfer Webhooks Name Location Structure
  property_count: 6
  slug: transfer-webhooks-name-location-structure
- name: Transfer Webhooks No Local Account Identification Structure
  property_count: 2
  slug: transfer-webhooks-no-local-account-identification-structure
- name: Transfer Webhooks Number And Bic Account Identification Structure
  property_count: 4
  slug: transfer-webhooks-number-and-bic-account-identification-structure
- name: Transfer Webhooks Nz Local Account Identification Structure
  property_count: 2
  slug: transfer-webhooks-nz-local-account-identification-structure
- name: Transfer Webhooks Party Identification Structure
  property_count: 7
  slug: transfer-webhooks-party-identification-structure
- name: Transfer Webhooks Payment Instrument Structure
  property_count: 4
  slug: transfer-webhooks-payment-instrument-structure
- name: Transfer Webhooks Pl Local Account Identification Structure
  property_count: 2
  slug: transfer-webhooks-pl-local-account-identification-structure
- name: Transfer Webhooks Platform Payment Structure
  property_count: 6
  slug: transfer-webhooks-platform-payment-structure
- name: Transfer Webhooks Relayed Authorisation Data Structure
  property_count: 2
  slug: transfer-webhooks-relayed-authorisation-data-structure
- name: Transfer Webhooks Resource Reference Structure
  property_count: 3
  slug: transfer-webhooks-resource-reference-structure
- name: Transfer Webhooks Resource Structure
  property_count: 3
  slug: transfer-webhooks-resource-structure
- name: Transfer Webhooks Se Local Account Identification Structure
  property_count: 3
  slug: transfer-webhooks-se-local-account-identification-structure
- name: Transfer Webhooks Sg Local Account Identification Structure
  property_count: 3
  slug: transfer-webhooks-sg-local-account-identification-structure
- name: Transfer Webhooks Transaction Event Violation Structure
  property_count: 3
  slug: transfer-webhooks-transaction-event-violation-structure
- name: Transfer Webhooks Transaction Rule Reference Structure
  property_count: 5
  slug: transfer-webhooks-transaction-rule-reference-structure
- name: Transfer Webhooks Transaction Rule Source Structure
  property_count: 2
  slug: transfer-webhooks-transaction-rule-source-structure
- name: Transfer Webhooks Transaction Rules Result Structure
  property_count: 4
  slug: transfer-webhooks-transaction-rules-result-structure
- name: Transfer Webhooks Transfer Data Structure
  property_count: 22
  slug: transfer-webhooks-transfer-data-structure
- name: Transfer Webhooks Transfer Event Structure
  property_count: 14
  slug: transfer-webhooks-transfer-event-structure
- name: Transfer Webhooks Transfer Notification Counter Party Structure
  property_count: 4
  slug: transfer-webhooks-transfer-notification-counter-party-structure
- name: Transfer Webhooks Transfer Notification Merchant Data Structure
  property_count: 7
  slug: transfer-webhooks-transfer-notification-merchant-data-structure
- name: Transfer Webhooks Transfer Notification Request Structure
  property_count: 3
  slug: transfer-webhooks-transfer-notification-request-structure
- name: Transfer Webhooks Transfer Notification Transfer Tracking Structure
  property_count: 2
  slug: transfer-webhooks-transfer-notification-transfer-tracking-structure
- name: Transfer Webhooks Transfer Notification Validation Fact Structure
  property_count: 2
  slug: transfer-webhooks-transfer-notification-validation-fact-structure
- name: Transfer Webhooks Uk Local Account Identification Structure
  property_count: 3
  slug: transfer-webhooks-uk-local-account-identification-structure
- name: Transfer Webhooks Us Local Account Identification Structure
  property_count: 4
  slug: transfer-webhooks-us-local-account-identification-structure
- name: Transfers Additional Bank Identification Structure
  property_count: 2
  slug: transfers-additional-bank-identification-structure
- name: Transfers Address Structure
  property_count: 6
  slug: transfers-address-structure
- name: Transfers Amount Structure
  property_count: 2
  slug: transfers-amount-structure
- name: Transfers Au Local Account Identification Structure
  property_count: 3
  slug: transfers-au-local-account-identification-structure
- name: Transfers Bank Account V3 Structure
  property_count: 2
  slug: transfers-bank-account-v3-structure
- name: Transfers Bank Category Data Structure
  property_count: 2
  slug: transfers-bank-category-data-structure
- name: Transfers Br Local Account Identification Structure
  property_count: 4
  slug: transfers-br-local-account-identification-structure
- name: Transfers Ca Local Account Identification Structure
  property_count: 5
  slug: transfers-ca-local-account-identification-structure
- name: Transfers Capital Balance Structure
  property_count: 4
  slug: transfers-capital-balance-structure
- name: Transfers Capital Grant Info Structure
  property_count: 3
  slug: transfers-capital-grant-info-structure
- name: Transfers Capital Grant Structure
  property_count: 9
  slug: transfers-capital-grant-structure
- name: Transfers Capital Grants Structure
  property_count: 1
  slug: transfers-capital-grants-structure
- name: Transfers Counterparty Info V3 Structure
  property_count: 3
  slug: transfers-counterparty-info-v3-structure
- name: Transfers Counterparty Structure
  property_count: 3
  slug: transfers-counterparty-structure
- name: Transfers Counterparty V3 Structure
  property_count: 4
  slug: transfers-counterparty-v3-structure
- name: Transfers Cz Local Account Identification Structure
  property_count: 3
  slug: transfers-cz-local-account-identification-structure
- name: Transfers Dk Local Account Identification Structure
  property_count: 3
  slug: transfers-dk-local-account-identification-structure
- name: Transfers Fee Structure
  property_count: 1
  slug: transfers-fee-structure
- name: Transfers Hk Local Account Identification Structure
  property_count: 3
  slug: transfers-hk-local-account-identification-structure
- name: Transfers Hu Local Account Identification Structure
  property_count: 2
  slug: transfers-hu-local-account-identification-structure
- name: Transfers Iban Account Identification Structure
  property_count: 2
  slug: transfers-iban-account-identification-structure
- name: Transfers Internal Category Data Structure
  property_count: 3
  slug: transfers-internal-category-data-structure
- name: Transfers Invalid Field Structure
  property_count: 3
  slug: transfers-invalid-field-structure
- name: Transfers Issued Card Structure
  property_count: 8
  slug: transfers-issued-card-structure
- name: Transfers Json Object Structure
  property_count: 0
  slug: transfers-json-object-structure
- name: Transfers Link Structure
  property_count: 1
  slug: transfers-link-structure
- name: Transfers Links Structure
  property_count: 2
  slug: transfers-links-structure
- name: Transfers Merchant Data Structure
  property_count: 5
  slug: transfers-merchant-data-structure
- name: Transfers Name Location Structure
  property_count: 6
  slug: transfers-name-location-structure
- name: Transfers No Local Account Identification Structure
  property_count: 2
  slug: transfers-no-local-account-identification-structure
- name: Transfers Number And Bic Account Identification Structure
  property_count: 4
  slug: transfers-number-and-bic-account-identification-structure
- name: Transfers Nz Local Account Identification Structure
  property_count: 2
  slug: transfers-nz-local-account-identification-structure
- name: Transfers Party Identification Structure
  property_count: 7
  slug: transfers-party-identification-structure
- name: Transfers Payment Instrument Structure
  property_count: 4
  slug: transfers-payment-instrument-structure
- name: Transfers Pl Local Account Identification Structure
  property_count: 2
  slug: transfers-pl-local-account-identification-structure
- name: Transfers Platform Payment Structure
  property_count: 6
  slug: transfers-platform-payment-structure
- name: Transfers Relayed Authorisation Data Structure
  property_count: 2
  slug: transfers-relayed-authorisation-data-structure
- name: Transfers Repayment Structure
  property_count: 3
  slug: transfers-repayment-structure
- name: Transfers Repayment Term Structure
  property_count: 2
  slug: transfers-repayment-term-structure
- name: Transfers Resource Reference Structure
  property_count: 3
  slug: transfers-resource-reference-structure
- name: Transfers Rest Service Error Structure
  property_count: 9
  slug: transfers-rest-service-error-structure
- name: Transfers Return Transfer Request Structure
  property_count: 2
  slug: transfers-return-transfer-request-structure
- name: Transfers Return Transfer Response Structure
  property_count: 4
  slug: transfers-return-transfer-response-structure
- name: Transfers Se Local Account Identification Structure
  property_count: 3
  slug: transfers-se-local-account-identification-structure
- name: Transfers Sg Local Account Identification Structure
  property_count: 3
  slug: transfers-sg-local-account-identification-structure
- name: Transfers Threshold Repayment Structure
  property_count: 1
  slug: transfers-threshold-repayment-structure
- name: Transfers Transaction Search Response Structure
  property_count: 2
  slug: transfers-transaction-search-response-structure
- name: Transfers Transaction Structure
  property_count: 10
  slug: transfers-transaction-structure
- name: Transfers Transfer Data Structure
  property_count: 2
  slug: transfers-transfer-data-structure
- name: Transfers Transfer Info Structure
  property_count: 10
  slug: transfers-transfer-info-structure
- name: Transfers Transfer Notification Validation Fact Structure
  property_count: 2
  slug: transfers-transfer-notification-validation-fact-structure
- name: Transfers Transfer Structure
  property_count: 15
  slug: transfers-transfer-structure
- name: Transfers Uk Local Account Identification Structure
  property_count: 3
  slug: transfers-uk-local-account-identification-structure
- name: Transfers Ultimate Party Identification Structure
  property_count: 7
  slug: transfers-ultimate-party-identification-structure
- name: Transfers Us Local Account Identification Structure
  property_count: 4
  slug: transfers-us-local-account-identification-structure
- name: Webhooks Ach Notification Of Change Notification Request Data Noc Structure
  property_count: 4
  slug: webhooks-ach-notification-of-change-notification-request-data-noc-structure
- name: Webhooks Ach Notification Of Change Notification Request Data Structure
  property_count: 3
  slug: webhooks-ach-notification-of-change-notification-request-data-structure
- name: Webhooks Ach Notification Of Change Notification Request Structure
  property_count: 5
  slug: webhooks-ach-notification-of-change-notification-request-structure
- name: Webhooks Amount Structure
  property_count: 2
  slug: webhooks-amount-structure
- name: Webhooks Authorisation Notification Additional Data Structure
  property_count: 143
  slug: webhooks-authorisation-notification-additional-data-structure
- name: Webhooks Authorisation Notification Request Item Structure
  property_count: 11
  slug: webhooks-authorisation-notification-request-item-structure
- name: Webhooks Authorisation Notification Request Item Wrapper Structure
  property_count: 1
  slug: webhooks-authorisation-notification-request-item-wrapper-structure
- name: Webhooks Authorisation Notification Request Structure
  property_count: 2
  slug: webhooks-authorisation-notification-request-structure
- name: Webhooks Expire Notification Request Item Structure
  property_count: 11
  slug: webhooks-expire-notification-request-item-structure
- name: Webhooks Expire Notification Request Item Wrapper Structure
  property_count: 1
  slug: webhooks-expire-notification-request-item-wrapper-structure
- name: Webhooks Expire Notification Request Structure
  property_count: 2
  slug: webhooks-expire-notification-request-structure
- name: Webhooks Notification Additional Data Structure
  property_count: 121
  slug: webhooks-notification-additional-data-structure
- name: Webhooks Notification Request Item Structure
  property_count: 11
  slug: webhooks-notification-request-item-structure
- name: Webhooks Notification Request Item Wrapper Structure
  property_count: 1
  slug: webhooks-notification-request-item-wrapper-structure
- name: Webhooks Notification Request Structure
  property_count: 2
  slug: webhooks-notification-request-structure
- name: Webhooks Notification Response Structure
  property_count: 1
  slug: webhooks-notification-response-structure
- name: Webhooks Paidout Reversed Notification Request Item Structure
  property_count: 11
  slug: webhooks-paidout-reversed-notification-request-item-structure
- name: Webhooks Paidout Reversed Notification Request Item Wrapper Structure
  property_count: 1
  slug: webhooks-paidout-reversed-notification-request-item-wrapper-structure
- name: Webhooks Paidout Reversed Notification Request Structure
  property_count: 2
  slug: webhooks-paidout-reversed-notification-request-structure
- name: Webhooks Recurring Contract Notification Additional Data Structure
  property_count: 122
  slug: webhooks-recurring-contract-notification-additional-data-structure
- name: Webhooks Recurring Contract Notification Request Item Structure
  property_count: 12
  slug: webhooks-recurring-contract-notification-request-item-structure
- name: Webhooks Recurring Contract Notification Request Item Wrapper Structure
  property_count: 1
  slug: webhooks-recurring-contract-notification-request-item-wrapper-structure
- name: Webhooks Recurring Contract Notification Request Structure
  property_count: 2
  slug: webhooks-recurring-contract-notification-request-structure
- name: Webhooks Report Available Notification Request Item Structure
  property_count: 11
  slug: webhooks-report-available-notification-request-item-structure
- name: Webhooks Report Available Notification Request Item Wrapper Structure
  property_count: 1
  slug: webhooks-report-available-notification-request-item-wrapper-structure
- name: Webhooks Report Available Notification Request Structure
  property_count: 2
  slug: webhooks-report-available-notification-request-structure
jsonld:
- class_count: 40
  name: Adyen Accounting Notifications Context
  property_count: 91
  slug: adyen-accounting-notifications-context
- class_count: 2
  name: Adyen Accounts Account Context
  property_count: 9
  slug: adyen-accounts-account-context
- class_count: 1
  name: Adyen Accounts Account Event Context
  property_count: 3
  slug: adyen-accounts-account-event-context
- class_count: 3
  name: Adyen Accounts Account Holder Context
  property_count: 19
  slug: adyen-accounts-account-holder-context
- class_count: 1
  name: Adyen Accounts Account Payout Context
  property_count: 6
  slug: adyen-accounts-account-payout-context
- class_count: 1
  name: Adyen Accounts Account Processing Context
  property_count: 5
  slug: adyen-accounts-account-processing-context
- class_count: 1
  name: Adyen Accounts Amount Context
  property_count: 2
  slug: adyen-accounts-amount-context
- class_count: 1
  name: Adyen Accounts Bank Account Context
  property_count: 26
  slug: adyen-accounts-bank-account-context
- class_count: 1
  name: Adyen Accounts Business Details Context
  property_count: 10
  slug: adyen-accounts-business-details-context
- class_count: 4
  name: Adyen Accounts Close Account Context
  property_count: 7
  slug: adyen-accounts-close-account-context
- class_count: 1
  name: Adyen Accounts Close Stores Context
  property_count: 2
  slug: adyen-accounts-close-stores-context
- class_count: 5
  name: Adyen Accounts Create Account Context
  property_count: 20
  slug: adyen-accounts-create-account-context
- class_count: 1
  name: Adyen Accounts Delete Bank Context
  property_count: 2
  slug: adyen-accounts-delete-bank-context
- class_count: 1
  name: Adyen Accounts Delete Legal Context
  property_count: 2
  slug: adyen-accounts-delete-legal-context
- class_count: 1
  name: Adyen Accounts Delete Payout Context
  property_count: 2
  slug: adyen-accounts-delete-payout-context
- class_count: 1
  name: Adyen Accounts Delete Shareholder Context
  property_count: 2
  slug: adyen-accounts-delete-shareholder-context
- class_count: 1
  name: Adyen Accounts Delete Signatories Context
  property_count: 2
  slug: adyen-accounts-delete-signatories-context
- class_count: 2
  name: Adyen Accounts Document Detail Context
  property_count: 8
  slug: adyen-accounts-document-detail-context
- class_count: 1
  name: Adyen Accounts Error Field Context
  property_count: 3
  slug: adyen-accounts-error-field-context
- class_count: 1
  name: Adyen Accounts Field Type Context
  property_count: 3
  slug: adyen-accounts-field-type-context
- class_count: 1
  name: Adyen Accounts Generic Response Context
  property_count: 3
  slug: adyen-accounts-generic-response-context
- class_count: 4
  name: Adyen Accounts Get Account Context
  property_count: 15
  slug: adyen-accounts-get-account-context
- class_count: 2
  name: Adyen Accounts Get Tax Context
  property_count: 8
  slug: adyen-accounts-get-tax-context
- class_count: 2
  name: Adyen Accounts Get Uploaded Context
  property_count: 7
  slug: adyen-accounts-get-uploaded-context
- class_count: 2
  name: Adyen Accounts Individual Details Context
  property_count: 1
  slug: adyen-accounts-individual-details-context
- class_count: 3
  name: Adyen Accounts Kyc Check Context
  property_count: 7
  slug: adyen-accounts-kyc-check-context
- class_count: 2
  name: Adyen Accounts Kyc Legal Context
  property_count: 3
  slug: adyen-accounts-kyc-legal-context
- class_count: 1
  name: Adyen Accounts Kyc Payout Context
  property_count: 2
  slug: adyen-accounts-kyc-payout-context
- class_count: 1
  name: Adyen Accounts Kyc Shareholder Context
  property_count: 4
  slug: adyen-accounts-kyc-shareholder-context
- class_count: 1
  name: Adyen Accounts Kyc Signatory Context
  property_count: 2
  slug: adyen-accounts-kyc-signatory-context
- class_count: 1
  name: Adyen Accounts Kyc Ultimate Context
  property_count: 2
  slug: adyen-accounts-kyc-ultimate-context
- class_count: 1
  name: Adyen Accounts Kyc Verification Context
  property_count: 7
  slug: adyen-accounts-kyc-verification-context
- class_count: 5
  name: Adyen Accounts Legal Arrangement Context
  property_count: 18
  slug: adyen-accounts-legal-arrangement-context
- class_count: 1
  name: Adyen Accounts Migrated Accounts Context
  property_count: 2
  slug: adyen-accounts-migrated-accounts-context
- class_count: 1
  name: Adyen Accounts Migrated Shareholders Context
  property_count: 2
  slug: adyen-accounts-migrated-shareholders-context
- class_count: 1
  name: Adyen Accounts Migrated Stores Context
  property_count: 4
  slug: adyen-accounts-migrated-stores-context
- class_count: 1
  name: Adyen Accounts Migration Data Context
  property_count: 7
  slug: adyen-accounts-migration-data-context
- class_count: 1
  name: Adyen Accounts Payout Method Context
  property_count: 5
  slug: adyen-accounts-payout-method-context
- class_count: 1
  name: Adyen Accounts Payout Schedule Context
  property_count: 2
  slug: adyen-accounts-payout-schedule-context
- class_count: 1
  name: Adyen Accounts Perform Verification Context
  property_count: 3
  slug: adyen-accounts-perform-verification-context
- class_count: 1
  name: Adyen Accounts Personal Document Context
  property_count: 5
  slug: adyen-accounts-personal-document-context
- class_count: 3
  name: Adyen Accounts Shareholder Contact Context
  property_count: 9
  slug: adyen-accounts-shareholder-contact-context
- class_count: 3
  name: Adyen Accounts Signatory Contact Context
  property_count: 8
  slug: adyen-accounts-signatory-contact-context
- class_count: 1
  name: Adyen Accounts Store Detail Context
  property_count: 15
  slug: adyen-accounts-store-detail-context
- class_count: 2
  name: Adyen Accounts Suspend Account Context
  property_count: 5
  slug: adyen-accounts-suspend-account-context
- class_count: 2
  name: Adyen Accounts Ultimate Parent Context
  property_count: 8
  slug: adyen-accounts-ultimate-parent-context
- class_count: 2
  name: Adyen Accounts Un Suspend Context
  property_count: 5
  slug: adyen-accounts-un-suspend-context
- class_count: 6
  name: Adyen Accounts Update Account Context
  property_count: 20
  slug: adyen-accounts-update-account-context
- class_count: 1
  name: Adyen Accounts Update Payout Context
  property_count: 3
  slug: adyen-accounts-update-payout-context
- class_count: 1
  name: Adyen Accounts Upload Document Context
  property_count: 2
  slug: adyen-accounts-upload-document-context
- class_count: 1
  name: Adyen Accounts Vias Address Context
  property_count: 6
  slug: adyen-accounts-vias-address-context
- class_count: 1
  name: Adyen Accounts Vias Name Context
  property_count: 4
  slug: adyen-accounts-vias-name-context
- class_count: 1
  name: Adyen Accounts Vias Personal Context
  property_count: 3
  slug: adyen-accounts-vias-personal-context
- class_count: 1
  name: Adyen Accounts Vias Phone Context
  property_count: 3
  slug: adyen-accounts-vias-phone-context
- class_count: 8
  name: Adyen Authentication Webhooks Context
  property_count: 36
  slug: adyen-authentication-webhooks-context
- class_count: 1
  name: Adyen Balance Control Amount Context
  property_count: 2
  slug: adyen-balance-control-amount-context
- class_count: 3
  name: Adyen Balance Control Balance Context
  property_count: 8
  slug: adyen-balance-control-balance-context
- class_count: 1
  name: Adyen Binlookup Amount Context
  property_count: 2
  slug: adyen-binlookup-amount-context
- class_count: 1
  name: Adyen Binlookup Bin Detail Context
  property_count: 1
  slug: adyen-binlookup-bin-detail-context
- class_count: 1
  name: Adyen Binlookup Card Bin Context
  property_count: 11
  slug: adyen-binlookup-card-bin-context
- class_count: 3
  name: Adyen Binlookup Cost Estimate Context
  property_count: 18
  slug: adyen-binlookup-cost-estimate-context
- class_count: 1
  name: Adyen Binlookup Ds Public Context
  property_count: 5
  slug: adyen-binlookup-ds-public-context
- class_count: 1
  name: Adyen Binlookup Merchant Details Context
  property_count: 3
  slug: adyen-binlookup-merchant-details-context
- class_count: 1
  name: Adyen Binlookup Recurring Context
  property_count: 5
  slug: adyen-binlookup-recurring-context
- class_count: 2
  name: Adyen Binlookup Three Ds Context
  property_count: 11
  slug: adyen-binlookup-three-ds-context
- class_count: 1
  name: Adyen Binlookup Three Ds2 Context
  property_count: 6
  slug: adyen-binlookup-three-ds2-context
- class_count: 1
  name: Adyen Checkout Account Info Context
  property_count: 19
  slug: adyen-checkout-account-info-context
- class_count: 1
  name: Adyen Checkout Acct Info Context
  property_count: 16
  slug: adyen-checkout-acct-info-context
- class_count: 1
  name: Adyen Checkout Ach Details Context
  property_count: 10
  slug: adyen-checkout-ach-details-context
- class_count: 14
  name: Adyen Checkout Additional Data Context
  property_count: 187
  slug: adyen-checkout-additional-data-context
- class_count: 1
  name: Adyen Checkout Additional Data3 Context
  property_count: 6
  slug: adyen-checkout-additional-data3-context
- class_count: 1
  name: Adyen Checkout Address Context
  property_count: 6
  slug: adyen-checkout-address-context
- class_count: 1
  name: Adyen Checkout Afterpay Details Context
  property_count: 7
  slug: adyen-checkout-afterpay-details-context
- class_count: 1
  name: Adyen Checkout Amazon Pay Context
  property_count: 4
  slug: adyen-checkout-amazon-pay-context
- class_count: 1
  name: Adyen Checkout Amount Context
  property_count: 2
  slug: adyen-checkout-amount-context
- class_count: 1
  name: Adyen Checkout Android Pay Context
  property_count: 2
  slug: adyen-checkout-android-pay-context
- class_count: 4
  name: Adyen Checkout Apple Pay Context
  property_count: 10
  slug: adyen-checkout-apple-pay-context
- class_count: 1
  name: Adyen Checkout Application Info Context
  property_count: 6
  slug: adyen-checkout-application-info-context
- class_count: 1
  name: Adyen Checkout Authentication Data Context
  property_count: 3
  slug: adyen-checkout-authentication-data-context
- class_count: 1
  name: Adyen Checkout Avs Context
  property_count: 2
  slug: adyen-checkout-avs-context
- class_count: 1
  name: Adyen Checkout Bacs Direct Context
  property_count: 7
  slug: adyen-checkout-bacs-direct-context
- class_count: 2
  name: Adyen Checkout Balance Check Context
  property_count: 50
  slug: adyen-checkout-balance-check-context
- class_count: 1
  name: Adyen Checkout Bank Account Context
  property_count: 9
  slug: adyen-checkout-bank-account-context
- class_count: 1
  name: Adyen Checkout Bill Desk Context
  property_count: 3
  slug: adyen-checkout-bill-desk-context
- class_count: 1
  name: Adyen Checkout Billing Address Context
  property_count: 6
  slug: adyen-checkout-billing-address-context
- class_count: 1
  name: Adyen Checkout Blik Details Context
  property_count: 5
  slug: adyen-checkout-blik-details-context
- class_count: 1
  name: Adyen Checkout Browser Info Context
  property_count: 9
  slug: adyen-checkout-browser-info-context
- class_count: 2
  name: Adyen Checkout Cancel Order Context
  property_count: 4
  slug: adyen-checkout-cancel-order-context
- class_count: 1
  name: Adyen Checkout Card Brand Context
  property_count: 2
  slug: adyen-checkout-card-brand-context
- class_count: 1
  name: Adyen Checkout Card Context
  property_count: 8
  slug: adyen-checkout-card-context
- class_count: 3
  name: Adyen Checkout Card Details Context
  property_count: 24
  slug: adyen-checkout-card-details-context
- class_count: 1
  name: Adyen Checkout Card Donations Context
  property_count: 19
  slug: adyen-checkout-card-donations-context
- class_count: 1
  name: Adyen Checkout Cellulant Details Context
  property_count: 3
  slug: adyen-checkout-cellulant-details-context
- class_count: 2
  name: Adyen Checkout Checkout Await Context
  property_count: 3
  slug: adyen-checkout-checkout-await-context
- class_count: 2
  name: Adyen Checkout Checkout Delegated Context
  property_count: 5
  slug: adyen-checkout-checkout-delegated-context
- class_count: 2
  name: Adyen Checkout Checkout Native Context
  property_count: 5
  slug: adyen-checkout-checkout-native-context
- class_count: 1
  name: Adyen Checkout Checkout Order Context
  property_count: 6
  slug: adyen-checkout-checkout-order-context
- class_count: 2
  name: Adyen Checkout Checkout Qr Context
  property_count: 5
  slug: adyen-checkout-checkout-qr-context
- class_count: 2
  name: Adyen Checkout Checkout Redirect Context
  property_count: 4
  slug: adyen-checkout-checkout-redirect-context
- class_count: 2
  name: Adyen Checkout Checkout Sdk Context
  property_count: 4
  slug: adyen-checkout-checkout-sdk-context
- class_count: 1
  name: Adyen Checkout Checkout Session Context
  property_count: 3
  slug: adyen-checkout-checkout-session-context
- class_count: 2
  name: Adyen Checkout Checkout Three Context
  property_count: 6
  slug: adyen-checkout-checkout-three-context
- class_count: 2
  name: Adyen Checkout Checkout Voucher Context
  property_count: 20
  slug: adyen-checkout-checkout-voucher-context
- class_count: 3
  name: Adyen Checkout Common Field Context
  property_count: 0
  slug: adyen-checkout-common-field-context
- class_count: 2
  name: Adyen Checkout Company Context
  property_count: 5
  slug: adyen-checkout-company-context
- class_count: 1
  name: Adyen Checkout Configuration Context
  property_count: 4
  slug: adyen-checkout-configuration-context
- class_count: 3
  name: Adyen Checkout Create Checkout Context
  property_count: 61
  slug: adyen-checkout-create-checkout-context
- class_count: 2
  name: Adyen Checkout Create Order Context
  property_count: 11
  slug: adyen-checkout-create-order-context
- class_count: 1
  name: Adyen Checkout Delivery Address Context
  property_count: 8
  slug: adyen-checkout-delivery-address-context
- class_count: 1
  name: Adyen Checkout Details Request Context
  property_count: 1
  slug: adyen-checkout-details-request-context
- class_count: 1
  name: Adyen Checkout Device Render Context
  property_count: 2
  slug: adyen-checkout-device-render-context
- class_count: 1
  name: Adyen Checkout Doku Details Context
  property_count: 5
  slug: adyen-checkout-doku-details-context
- class_count: 2
  name: Adyen Checkout Donation Payment Context
  property_count: 44
  slug: adyen-checkout-donation-payment-context
- class_count: 1
  name: Adyen Checkout Dotpay Details Context
  property_count: 3
  slug: adyen-checkout-dotpay-details-context
- class_count: 1
  name: Adyen Checkout Dragonpay Details Context
  property_count: 4
  slug: adyen-checkout-dragonpay-details-context
- class_count: 1
  name: Adyen Checkout Econtext Voucher Context
  property_count: 6
  slug: adyen-checkout-econtext-voucher-context
- class_count: 1
  name: Adyen Checkout Encrypted Order Context
  property_count: 2
  slug: adyen-checkout-encrypted-order-context
- class_count: 3
  name: Adyen Checkout External Platform Context
  property_count: 1
  slug: adyen-checkout-external-platform-context
- class_count: 1
  name: Adyen Checkout Forex Quote Context
  property_count: 12
  slug: adyen-checkout-forex-quote-context
- class_count: 2
  name: Adyen Checkout Fraud Check Context
  property_count: 2
  slug: adyen-checkout-fraud-check-context
- class_count: 1
  name: Adyen Checkout Fraud Result Context
  property_count: 2
  slug: adyen-checkout-fraud-result-context
- class_count: 1
  name: Adyen Checkout Fund Origin Context
  property_count: 5
  slug: adyen-checkout-fund-origin-context
- class_count: 1
  name: Adyen Checkout Fund Recipient Context
  property_count: 10
  slug: adyen-checkout-fund-recipient-context
- class_count: 1
  name: Adyen Checkout Generic Issuer Context
  property_count: 5
  slug: adyen-checkout-generic-issuer-context
- class_count: 1
  name: Adyen Checkout Giropay Details Context
  property_count: 4
  slug: adyen-checkout-giropay-details-context
- class_count: 2
  name: Adyen Checkout Google Pay Context
  property_count: 7
  slug: adyen-checkout-google-pay-context
- class_count: 1
  name: Adyen Checkout Ideal Details Context
  property_count: 5
  slug: adyen-checkout-ideal-details-context
- class_count: 1
  name: Adyen Checkout Ideal Donations Context
  property_count: 5
  slug: adyen-checkout-ideal-donations-context
- class_count: 1
  name: Adyen Checkout Input Detail Context
  property_count: 9
  slug: adyen-checkout-input-detail-context
- class_count: 1
  name: Adyen Checkout Installment Option Context
  property_count: 4
  slug: adyen-checkout-installment-option-context
- class_count: 1
  name: Adyen Checkout Installments Context
  property_count: 2
  slug: adyen-checkout-installments-context
- class_count: 1
  name: Adyen Checkout Installments Number Context
  property_count: 1
  slug: adyen-checkout-installments-number-context
- class_count: 2
  name: Adyen Checkout Item Context
  property_count: 1
  slug: adyen-checkout-item-context
- class_count: 1
  name: Adyen Checkout Klarna Details Context
  property_count: 8
  slug: adyen-checkout-klarna-details-context
- class_count: 2
  name: Adyen Checkout Line Item Context
  property_count: 16
  slug: adyen-checkout-line-item-context
- class_count: 1
  name: Adyen Checkout List Stored Context
  property_count: 3
  slug: adyen-checkout-list-stored-context
- class_count: 1
  name: Adyen Checkout Mandate Context
  property_count: 8
  slug: adyen-checkout-mandate-context
- class_count: 1
  name: Adyen Checkout Masterpass Details Context
  property_count: 4
  slug: adyen-checkout-masterpass-details-context
- class_count: 1
  name: Adyen Checkout Mbway Details Context
  property_count: 4
  slug: adyen-checkout-mbway-details-context
- class_count: 1
  name: Adyen Checkout Merchant Device Context
  property_count: 3
  slug: adyen-checkout-merchant-device-context
- class_count: 1
  name: Adyen Checkout Merchant Risk Context
  property_count: 14
  slug: adyen-checkout-merchant-risk-context
- class_count: 1
  name: Adyen Checkout Mobile Pay Context
  property_count: 2
  slug: adyen-checkout-mobile-pay-context
- class_count: 1
  name: Adyen Checkout Mol Pay Context
  property_count: 3
  slug: adyen-checkout-mol-pay-context
- class_count: 1
  name: Adyen Checkout Name Context
  property_count: 2
  slug: adyen-checkout-name-context
- class_count: 1
  name: Adyen Checkout Open Invoice Context
  property_count: 7
  slug: adyen-checkout-open-invoice-context
- class_count: 1
  name: Adyen Checkout Pay Pal Context
  property_count: 9
  slug: adyen-checkout-pay-pal-context
- class_count: 1
  name: Adyen Checkout Pay U Context
  property_count: 6
  slug: adyen-checkout-pay-u-context
- class_count: 2
  name: Adyen Checkout Pay With Context
  property_count: 6
  slug: adyen-checkout-pay-with-context
- class_count: 2
  name: Adyen Checkout Payment Amount Context
  property_count: 10
  slug: adyen-checkout-payment-amount-context
- class_count: 2
  name: Adyen Checkout Payment Cancel Context
  property_count: 6
  slug: adyen-checkout-payment-cancel-context
- class_count: 2
  name: Adyen Checkout Payment Capture Context
  property_count: 11
  slug: adyen-checkout-payment-capture-context
- class_count: 1
  name: Adyen Checkout Payment Completion Context
  property_count: 18
  slug: adyen-checkout-payment-completion-context
- class_count: 3
  name: Adyen Checkout Payment Details Context
  property_count: 21
  slug: adyen-checkout-payment-details-context
- class_count: 4
  name: Adyen Checkout Payment Link Context
  property_count: 40
  slug: adyen-checkout-payment-link-context
- class_count: 4
  name: Adyen Checkout Payment Method Context
  property_count: 11
  slug: adyen-checkout-payment-method-context
- class_count: 2
  name: Adyen Checkout Payment Methods Context
  property_count: 14
  slug: adyen-checkout-payment-methods-context
- class_count: 2
  name: Adyen Checkout Payment Refund Context
  property_count: 11
  slug: adyen-checkout-payment-refund-context
- class_count: 1
  name: Adyen Checkout Payment Request Context
  property_count: 67
  slug: adyen-checkout-payment-request-context
- class_count: 1
  name: Adyen Checkout Payment Response Context
  property_count: 15
  slug: adyen-checkout-payment-response-context
- class_count: 2
  name: Adyen Checkout Payment Reversal Context
  property_count: 6
  slug: adyen-checkout-payment-reversal-context
- class_count: 2
  name: Adyen Checkout Payment Setup Context
  property_count: 58
  slug: adyen-checkout-payment-setup-context
- class_count: 2
  name: Adyen Checkout Payment Verification Context
  property_count: 11
  slug: adyen-checkout-payment-verification-context
- class_count: 1
  name: Adyen Checkout Phone Context
  property_count: 2
  slug: adyen-checkout-phone-context
- class_count: 1
  name: Adyen Checkout Platform Chargeback Context
  property_count: 3
  slug: adyen-checkout-platform-chargeback-context
- class_count: 1
  name: Adyen Checkout Ratepay Details Context
  property_count: 7
  slug: adyen-checkout-ratepay-details-context
- class_count: 1
  name: Adyen Checkout Recurring Context
  property_count: 5
  slug: adyen-checkout-recurring-context
- class_count: 2
  name: Adyen Checkout Recurring Detail Context
  property_count: 10
  slug: adyen-checkout-recurring-detail-context
- class_count: 9
  name: Adyen Checkout Response Additional Context
  property_count: 99
  slug: adyen-checkout-response-additional-context
- class_count: 1
  name: Adyen Checkout Response Payment Context
  property_count: 2
  slug: adyen-checkout-response-payment-context
- class_count: 1
  name: Adyen Checkout Risk Data Context
  property_count: 4
  slug: adyen-checkout-risk-data-context
- class_count: 1
  name: Adyen Checkout Samsung Pay Context
  property_count: 6
  slug: adyen-checkout-samsung-pay-context
- class_count: 1
  name: Adyen Checkout Sdk Ephem Context
  property_count: 4
  slug: adyen-checkout-sdk-ephem-context
- class_count: 1
  name: Adyen Checkout Sepa Direct Context
  property_count: 6
  slug: adyen-checkout-sepa-direct-context
- class_count: 1
  name: Adyen Checkout Service Context
  property_count: 4
  slug: adyen-checkout-service-context
- class_count: 1
  name: Adyen Checkout Session Result Context
  property_count: 2
  slug: adyen-checkout-session-result-context
- class_count: 1
  name: Adyen Checkout Shopper Input Context
  property_count: 3
  slug: adyen-checkout-shopper-input-context
- class_count: 1
  name: Adyen Checkout Shopper Interaction Context
  property_count: 3
  slug: adyen-checkout-shopper-interaction-context
- class_count: 1
  name: Adyen Checkout Split Amount Context
  property_count: 2
  slug: adyen-checkout-split-amount-context
- class_count: 2
  name: Adyen Checkout Split Context
  property_count: 4
  slug: adyen-checkout-split-context
- class_count: 2
  name: Adyen Checkout Standalone Payment Context
  property_count: 6
  slug: adyen-checkout-standalone-payment-context
- class_count: 1
  name: Adyen Checkout Stored Details Context
  property_count: 3
  slug: adyen-checkout-stored-details-context
- class_count: 4
  name: Adyen Checkout Stored Payment Context
  property_count: 23
  slug: adyen-checkout-stored-payment-context
- class_count: 1
  name: Adyen Checkout Sub Input Context
  property_count: 6
  slug: adyen-checkout-sub-input-context
- class_count: 3
  name: Adyen Checkout Sub Merchant Context
  property_count: 6
  slug: adyen-checkout-sub-merchant-context
- class_count: 1
  name: Adyen Checkout Three D Context
  property_count: 12
  slug: adyen-checkout-three-d-context
- class_count: 3
  name: Adyen Checkout Three Ds Context
  property_count: 11
  slug: adyen-checkout-three-ds-context
- class_count: 4
  name: Adyen Checkout Three Ds2 Context
  property_count: 60
  slug: adyen-checkout-three-ds2-context
- class_count: 1
  name: Adyen Checkout Update Payment Context
  property_count: 1
  slug: adyen-checkout-update-payment-context
- class_count: 1
  name: Adyen Checkout Upi Collect Context
  property_count: 7
  slug: adyen-checkout-upi-collect-context
- class_count: 1
  name: Adyen Checkout Upi Intent Context
  property_count: 5
  slug: adyen-checkout-upi-intent-context
- class_count: 1
  name: Adyen Checkout Utility Request Context
  property_count: 1
  slug: adyen-checkout-utility-request-context
- class_count: 1
  name: Adyen Checkout Utility Response Context
  property_count: 1
  slug: adyen-checkout-utility-response-context
- class_count: 1
  name: Adyen Checkout Vipps Details Context
  property_count: 5
  slug: adyen-checkout-vipps-details-context
- class_count: 1
  name: Adyen Checkout Visa Checkout Context
  property_count: 4
  slug: adyen-checkout-visa-checkout-context
- class_count: 2
  name: Adyen Checkout We Chat Context
  property_count: 4
  slug: adyen-checkout-we-chat-context
- class_count: 1
  name: Adyen Checkout Zip Details Context
  property_count: 5
  slug: adyen-checkout-zip-details-context
- class_count: 5
  name: Adyen Configuration Account Holder Context
  property_count: 22
  slug: adyen-configuration-account-holder-context
- class_count: 1
  name: Adyen Configuration Account Supporting Context
  property_count: 7
  slug: adyen-configuration-account-supporting-context
- class_count: 1
  name: Adyen Configuration Active Network Context
  property_count: 2
  slug: adyen-configuration-active-network-context
- class_count: 1
  name: Adyen Configuration Additional Bank Context
  property_count: 2
  slug: adyen-configuration-additional-bank-context
- class_count: 1
  name: Adyen Configuration Address Context
  property_count: 6
  slug: adyen-configuration-address-context
- class_count: 2
  name: Adyen Configuration Address Requirement Context
  property_count: 2
  slug: adyen-configuration-address-requirement-context
- class_count: 1
  name: Adyen Configuration Amount Context
  property_count: 2
  slug: adyen-configuration-amount-context
- class_count: 2
  name: Adyen Configuration Amount Min Context
  property_count: 3
  slug: adyen-configuration-amount-min-context
- class_count: 1
  name: Adyen Configuration Au Local Context
  property_count: 3
  slug: adyen-configuration-au-local-context
- class_count: 2
  name: Adyen Configuration Authentication Context
  property_count: 2
  slug: adyen-configuration-authentication-context
- class_count: 5
  name: Adyen Configuration Balance Account Context
  property_count: 10
  slug: adyen-configuration-balance-account-context
- class_count: 1
  name: Adyen Configuration Balance Context
  property_count: 5
  slug: adyen-configuration-balance-context
- class_count: 2
  name: Adyen Configuration Balance Platform Context
  property_count: 2
  slug: adyen-configuration-balance-platform-context
- class_count: 1
  name: Adyen Configuration Balance Sweep Context
  property_count: 3
  slug: adyen-configuration-balance-sweep-context
- class_count: 5
  name: Adyen Configuration Bank Account Context
  property_count: 4
  slug: adyen-configuration-bank-account-context
- class_count: 1
  name: Adyen Configuration Bank Identification Context
  property_count: 3
  slug: adyen-configuration-bank-identification-context
- class_count: 1
  name: Adyen Configuration Br Local Context
  property_count: 4
  slug: adyen-configuration-br-local-context
- class_count: 1
  name: Adyen Configuration Brand Variants Context
  property_count: 2
  slug: adyen-configuration-brand-variants-context
- class_count: 2
  name: Adyen Configuration Bulk Address Context
  property_count: 8
  slug: adyen-configuration-bulk-address-context
- class_count: 1
  name: Adyen Configuration Ca Local Context
  property_count: 5
  slug: adyen-configuration-ca-local-context
- class_count: 3
  name: Adyen Configuration Capability Problem Context
  property_count: 6
  slug: adyen-configuration-capability-problem-context
- class_count: 1
  name: Adyen Configuration Capability Settings Context
  property_count: 5
  slug: adyen-configuration-capability-settings-context
- class_count: 1
  name: Adyen Configuration Capital Balance Context
  property_count: 4
  slug: adyen-configuration-capital-balance-context
- class_count: 1
  name: Adyen Configuration Capital Grant Context
  property_count: 4
  slug: adyen-configuration-capital-grant-context
- class_count: 1
  name: Adyen Configuration Card Configuration Context
  property_count: 14
  slug: adyen-configuration-card-configuration-context
- class_count: 1
  name: Adyen Configuration Card Context
  property_count: 13
  slug: adyen-configuration-card-context
- class_count: 1
  name: Adyen Configuration Card Info Context
  property_count: 8
  slug: adyen-configuration-card-info-context
- class_count: 3
  name: Adyen Configuration Card Order Context
  property_count: 17
  slug: adyen-configuration-card-order-context
- class_count: 2
  name: Adyen Configuration Contact Details Context
  property_count: 3
  slug: adyen-configuration-contact-details-context
- class_count: 1
  name: Adyen Configuration Counterparty Bank Context
  property_count: 2
  slug: adyen-configuration-counterparty-bank-context
- class_count: 1
  name: Adyen Configuration Counterparty Context
  property_count: 2
  slug: adyen-configuration-counterparty-context
- class_count: 1
  name: Adyen Configuration Countries Restriction Context
  property_count: 2
  slug: adyen-configuration-countries-restriction-context
- class_count: 2
  name: Adyen Configuration Create Sweep Context
  property_count: 11
  slug: adyen-configuration-create-sweep-context
- class_count: 1
  name: Adyen Configuration Cz Local Context
  property_count: 3
  slug: adyen-configuration-cz-local-context
- class_count: 1
  name: Adyen Configuration Day Of Context
  property_count: 2
  slug: adyen-configuration-day-of-context
- class_count: 1
  name: Adyen Configuration Delivery Address Context
  property_count: 7
  slug: adyen-configuration-delivery-address-context
- class_count: 3
  name: Adyen Configuration Delivery Contact Context
  property_count: 4
  slug: adyen-configuration-delivery-contact-context
- class_count: 1
  name: Adyen Configuration Device Info Context
  property_count: 11
  slug: adyen-configuration-device-info-context
- class_count: 1
  name: Adyen Configuration Different Currencies Context
  property_count: 2
  slug: adyen-configuration-different-currencies-context
- class_count: 1
  name: Adyen Configuration Dk Local Context
  property_count: 3
  slug: adyen-configuration-dk-local-context
- class_count: 1
  name: Adyen Configuration Duration Context
  property_count: 2
  slug: adyen-configuration-duration-context
- class_count: 1
  name: Adyen Configuration Entry Modes Context
  property_count: 2
  slug: adyen-configuration-entry-modes-context
- class_count: 1
  name: Adyen Configuration Expiry Context
  property_count: 2
  slug: adyen-configuration-expiry-context
- class_count: 1
  name: Adyen Configuration Fee Context
  property_count: 1
  slug: adyen-configuration-fee-context
- class_count: 1
  name: Adyen Configuration Get Network Context
  property_count: 1
  slug: adyen-configuration-get-network-context
- class_count: 1
  name: Adyen Configuration Get Tax Context
  property_count: 2
  slug: adyen-configuration-get-tax-context
- class_count: 1
  name: Adyen Configuration Grant Limit Context
  property_count: 1
  slug: adyen-configuration-grant-limit-context
- class_count: 1
  name: Adyen Configuration Grant Offer Context
  property_count: 8
  slug: adyen-configuration-grant-offer-context
- class_count: 1
  name: Adyen Configuration Grant Offers Context
  property_count: 1
  slug: adyen-configuration-grant-offers-context
- class_count: 1
  name: Adyen Configuration Hk Local Context
  property_count: 3
  slug: adyen-configuration-hk-local-context
- class_count: 1
  name: Adyen Configuration Hu Local Context
  property_count: 2
  slug: adyen-configuration-hu-local-context
- class_count: 1
  name: Adyen Configuration Iban Account Context
  property_count: 2
  slug: adyen-configuration-iban-account-context
- class_count: 1
  name: Adyen Configuration International Transaction Context
  property_count: 2
  slug: adyen-configuration-international-transaction-context
- class_count: 2
  name: Adyen Configuration Invalid Field Context
  property_count: 2
  slug: adyen-configuration-invalid-field-context
- class_count: 1
  name: Adyen Configuration Json Object Context
  property_count: 0
  slug: adyen-configuration-json-object-context
- class_count: 1
  name: Adyen Configuration List Network Context
  property_count: 1
  slug: adyen-configuration-list-network-context
- class_count: 1
  name: Adyen Configuration Matching Transactions Context
  property_count: 2
  slug: adyen-configuration-matching-transactions-context
- class_count: 1
  name: Adyen Configuration Mccs Restriction Context
  property_count: 2
  slug: adyen-configuration-mccs-restriction-context
- class_count: 1
  name: Adyen Configuration Merchant Acquirer Context
  property_count: 2
  slug: adyen-configuration-merchant-acquirer-context
- class_count: 1
  name: Adyen Configuration Merchant Names Context
  property_count: 2
  slug: adyen-configuration-merchant-names-context
- class_count: 1
  name: Adyen Configuration Merchants Restriction Context
  property_count: 2
  slug: adyen-configuration-merchants-restriction-context
- class_count: 1
  name: Adyen Configuration Name Context
  property_count: 2
  slug: adyen-configuration-name-context
- class_count: 1
  name: Adyen Configuration Network Token Context
  property_count: 8
  slug: adyen-configuration-network-token-context
- class_count: 1
  name: Adyen Configuration No Local Context
  property_count: 2
  slug: adyen-configuration-no-local-context
- class_count: 1
  name: Adyen Configuration Number And Context
  property_count: 4
  slug: adyen-configuration-number-and-context
- class_count: 1
  name: Adyen Configuration Nz Local Context
  property_count: 2
  slug: adyen-configuration-nz-local-context
- class_count: 1
  name: Adyen Configuration Paginated Account Context
  property_count: 3
  slug: adyen-configuration-paginated-account-context
- class_count: 1
  name: Adyen Configuration Paginated Balance Context
  property_count: 3
  slug: adyen-configuration-paginated-balance-context
- class_count: 2
  name: Adyen Configuration Paginated Get Context
  property_count: 4
  slug: adyen-configuration-paginated-get-context
- class_count: 1
  name: Adyen Configuration Paginated Payment Context
  property_count: 3
  slug: adyen-configuration-paginated-payment-context
- class_count: 8
  name: Adyen Configuration Payment Instrument Context
  property_count: 19
  slug: adyen-configuration-payment-instrument-context
- class_count: 1
  name: Adyen Configuration Phone Context
  property_count: 2
  slug: adyen-configuration-phone-context
- class_count: 1
  name: Adyen Configuration Phone Number Context
  property_count: 3
  slug: adyen-configuration-phone-number-context
- class_count: 2
  name: Adyen Configuration Pin Change Context
  property_count: 5
  slug: adyen-configuration-pin-change-context
- class_count: 1
  name: Adyen Configuration Pl Local Context
  property_count: 2
  slug: adyen-configuration-pl-local-context
- class_count: 1
  name: Adyen Configuration Platform Payment Context
  property_count: 2
  slug: adyen-configuration-platform-payment-context
- class_count: 1
  name: Adyen Configuration Processing Types Context
  property_count: 2
  slug: adyen-configuration-processing-types-context
- class_count: 1
  name: Adyen Configuration Public Key Context
  property_count: 2
  slug: adyen-configuration-public-key-context
- class_count: 1
  name: Adyen Configuration Remediating Action Context
  property_count: 2
  slug: adyen-configuration-remediating-action-context
- class_count: 1
  name: Adyen Configuration Repayment Context
  property_count: 3
  slug: adyen-configuration-repayment-context
- class_count: 1
  name: Adyen Configuration Repayment Term Context
  property_count: 2
  slug: adyen-configuration-repayment-term-context
- class_count: 1
  name: Adyen Configuration Rest Service Context
  property_count: 9
  slug: adyen-configuration-rest-service-context
- class_count: 2
  name: Adyen Configuration Reveal Pin Context
  property_count: 4
  slug: adyen-configuration-reveal-pin-context
- class_count: 1
  name: Adyen Configuration Same Amount Context
  property_count: 2
  slug: adyen-configuration-same-amount-context
- class_count: 1
  name: Adyen Configuration Same Counterparty Context
  property_count: 2
  slug: adyen-configuration-same-counterparty-context
- class_count: 1
  name: Adyen Configuration Se Local Context
  property_count: 3
  slug: adyen-configuration-se-local-context
- class_count: 1
  name: Adyen Configuration Sg Local Context
  property_count: 3
  slug: adyen-configuration-sg-local-context
- class_count: 1
  name: Adyen Configuration String Match Context
  property_count: 2
  slug: adyen-configuration-string-match-context
- class_count: 2
  name: Adyen Configuration Sweep Configuration Context
  property_count: 12
  slug: adyen-configuration-sweep-configuration-context
- class_count: 1
  name: Adyen Configuration Sweep Counterparty Context
  property_count: 3
  slug: adyen-configuration-sweep-counterparty-context
- class_count: 1
  name: Adyen Configuration Sweep Schedule Context
  property_count: 2
  slug: adyen-configuration-sweep-schedule-context
- class_count: 1
  name: Adyen Configuration Threshold Repayment Context
  property_count: 1
  slug: adyen-configuration-threshold-repayment-context
- class_count: 2
  name: Adyen Configuration Time Of Context
  property_count: 4
  slug: adyen-configuration-time-of-context
- class_count: 1
  name: Adyen Configuration Total Amount Context
  property_count: 2
  slug: adyen-configuration-total-amount-context
- class_count: 7
  name: Adyen Configuration Transaction Rule Context
  property_count: 36
  slug: adyen-configuration-transaction-rule-context
- class_count: 1
  name: Adyen Configuration Transaction Rules Context
  property_count: 1
  slug: adyen-configuration-transaction-rules-context
- class_count: 3
  name: Adyen Configuration Transfer Route Context
  property_count: 10
  slug: adyen-configuration-transfer-route-context
- class_count: 1
  name: Adyen Configuration Uk Local Context
  property_count: 3
  slug: adyen-configuration-uk-local-context
- class_count: 1
  name: Adyen Configuration Update Network Context
  property_count: 1
  slug: adyen-configuration-update-network-context
- class_count: 2
  name: Adyen Configuration Update Payment Context
  property_count: 11
  slug: adyen-configuration-update-payment-context
- class_count: 2
  name: Adyen Configuration Update Sweep Context
  property_count: 12
  slug: adyen-configuration-update-sweep-context
- class_count: 1
  name: Adyen Configuration Us Local Context
  property_count: 4
  slug: adyen-configuration-us-local-context
- class_count: 1
  name: Adyen Configuration Verification Deadline Context
  property_count: 3
  slug: adyen-configuration-verification-deadline-context
- class_count: 2
  name: Adyen Configuration Verification Error Context
  property_count: 6
  slug: adyen-configuration-verification-error-context
- class_count: 50
  name: Adyen Configuration Webhooks Context
  property_count: 135
  slug: adyen-configuration-webhooks-context
- class_count: 2
  name: Adyen Data Protection Subject Context
  property_count: 4
  slug: adyen-data-protection-subject-context
- class_count: 2
  name: Adyen Disputes Accept Dispute Context
  property_count: 3
  slug: adyen-disputes-accept-dispute-context
- class_count: 2
  name: Adyen Disputes Defend Dispute Context
  property_count: 4
  slug: adyen-disputes-defend-dispute-context
- class_count: 2
  name: Adyen Disputes Defense Document Context
  property_count: 5
  slug: adyen-disputes-defense-document-context
- class_count: 1
  name: Adyen Disputes Defense Reason Context
  property_count: 3
  slug: adyen-disputes-defense-reason-context
- class_count: 2
  name: Adyen Disputes Defense Reasons Context
  property_count: 4
  slug: adyen-disputes-defense-reasons-context
- class_count: 2
  name: Adyen Disputes Delete Defense Context
  property_count: 4
  slug: adyen-disputes-delete-defense-context
- class_count: 1
  name: Adyen Disputes Dispute Service Context
  property_count: 2
  slug: adyen-disputes-dispute-service-context
- class_count: 2
  name: Adyen Disputes Supply Defense Context
  property_count: 4
  slug: adyen-disputes-supply-defense-context
- class_count: 1
  name: Adyen Funds Account Detail Context
  property_count: 2
  slug: adyen-funds-account-detail-context
- class_count: 4
  name: Adyen Funds Account Holder Context
  property_count: 9
  slug: adyen-funds-account-holder-context
- class_count: 1
  name: Adyen Funds Account Transaction Context
  property_count: 3
  slug: adyen-funds-account-transaction-context
- class_count: 1
  name: Adyen Funds Amount Context
  property_count: 2
  slug: adyen-funds-amount-context
- class_count: 1
  name: Adyen Funds Bank Account Context
  property_count: 26
  slug: adyen-funds-bank-account-context
- class_count: 3
  name: Adyen Funds Debit Account Context
  property_count: 9
  slug: adyen-funds-debit-account-context
- class_count: 1
  name: Adyen Funds Detail Balance Context
  property_count: 3
  slug: adyen-funds-detail-balance-context
- class_count: 1
  name: Adyen Funds Error Field Context
  property_count: 3
  slug: adyen-funds-error-field-context
- class_count: 1
  name: Adyen Funds Field Type Context
  property_count: 3
  slug: adyen-funds-field-type-context
- class_count: 3
  name: Adyen Funds Payout Account Context
  property_count: 10
  slug: adyen-funds-payout-account-context
- class_count: 2
  name: Adyen Funds Refund Funds Context
  property_count: 7
  slug: adyen-funds-refund-funds-context
- class_count: 2
  name: Adyen Funds Refund Not Context
  property_count: 5
  slug: adyen-funds-refund-not-context
- class_count: 2
  name: Adyen Funds Setup Beneficiary Context
  property_count: 6
  slug: adyen-funds-setup-beneficiary-context
- class_count: 1
  name: Adyen Funds Split Amount Context
  property_count: 2
  slug: adyen-funds-split-amount-context
- class_count: 2
  name: Adyen Funds Split Context
  property_count: 4
  slug: adyen-funds-split-context
- class_count: 2
  name: Adyen Funds Transaction Context
  property_count: 15
  slug: adyen-funds-transaction-context
- class_count: 1
  name: Adyen Funds Transaction List Context
  property_count: 2
  slug: adyen-funds-transaction-list-context
- class_count: 2
  name: Adyen Funds Transfer Funds Context
  property_count: 8
  slug: adyen-funds-transfer-funds-context
- class_count: 1
  name: Adyen Hosted Onboarding Collect Context
  property_count: 6
  slug: adyen-hosted-onboarding-collect-context
- class_count: 1
  name: Adyen Hosted Onboarding Error Context
  property_count: 3
  slug: adyen-hosted-onboarding-error-context
- class_count: 1
  name: Adyen Hosted Onboarding Field Context
  property_count: 3
  slug: adyen-hosted-onboarding-field-context
- class_count: 4
  name: Adyen Hosted Onboarding Get Context
  property_count: 12
  slug: adyen-hosted-onboarding-get-context
- class_count: 1
  name: Adyen Hosted Onboarding Show Context
  property_count: 9
  slug: adyen-hosted-onboarding-show-context
- class_count: 2
  name: Adyen Legal Entity Accept Terms Of Service Context
  property_count: 6
  slug: adyen-legal-entity-accept-terms-of-service-context
- class_count: 1
  name: Adyen Legal Entity Additional Context
  property_count: 2
  slug: adyen-legal-entity-additional-context
- class_count: 1
  name: Adyen Legal Entity Address Context
  property_count: 6
  slug: adyen-legal-entity-address-context
- class_count: 1
  name: Adyen Legal Entity Amount Context
  property_count: 2
  slug: adyen-legal-entity-amount-context
- class_count: 1
  name: Adyen Legal Entity Attachment Context
  property_count: 5
  slug: adyen-legal-entity-attachment-context
- class_count: 1
  name: Adyen Legal Entity Au Context
  property_count: 3
  slug: adyen-legal-entity-au-context
- class_count: 1
  name: Adyen Legal Entity Bank Context
  property_count: 5
  slug: adyen-legal-entity-bank-context
- class_count: 1
  name: Adyen Legal Entity Birth Context
  property_count: 1
  slug: adyen-legal-entity-birth-context
- class_count: 4
  name: Adyen Legal Entity Business Context
  property_count: 11
  slug: adyen-legal-entity-business-context
- class_count: 1
  name: Adyen Legal Entity Ca Context
  property_count: 5
  slug: adyen-legal-entity-ca-context
- class_count: 1
  name: Adyen Legal Entity Calculate Terms Of Service Context
  property_count: 1
  slug: adyen-legal-entity-calculate-terms-of-service-context
- class_count: 4
  name: Adyen Legal Entity Capability Context
  property_count: 11
  slug: adyen-legal-entity-capability-context
- class_count: 1
  name: Adyen Legal Entity Cz Context
  property_count: 3
  slug: adyen-legal-entity-cz-context
- class_count: 1
  name: Adyen Legal Entity Data Context
  property_count: 1
  slug: adyen-legal-entity-data-context
- class_count: 1
  name: Adyen Legal Entity Dk Context
  property_count: 3
  slug: adyen-legal-entity-dk-context
- class_count: 4
  name: Adyen Legal Entity Document Context
  property_count: 16
  slug: adyen-legal-entity-document-context
- class_count: 1
  name: Adyen Legal Entity Entity Context
  property_count: 1
  slug: adyen-legal-entity-entity-context
- class_count: 2
  name: Adyen Legal Entity Generate Context
  property_count: 4
  slug: adyen-legal-entity-generate-context
- class_count: 2
  name: Adyen Legal Entity Get Context
  property_count: 5
  slug: adyen-legal-entity-get-context
- class_count: 3
  name: Adyen Legal Entity Get Terms Of Service Context
  property_count: 6
  slug: adyen-legal-entity-get-terms-of-service-context
- class_count: 1
  name: Adyen Legal Entity Hk Context
  property_count: 3
  slug: adyen-legal-entity-hk-context
- class_count: 1
  name: Adyen Legal Entity Hu Context
  property_count: 2
  slug: adyen-legal-entity-hu-context
- class_count: 1
  name: Adyen Legal Entity Iban Context
  property_count: 2
  slug: adyen-legal-entity-iban-context
- class_count: 1
  name: Adyen Legal Entity Identification Context
  property_count: 7
  slug: adyen-legal-entity-identification-context
- class_count: 3
  name: Adyen Legal Entity Individual Context
  property_count: 7
  slug: adyen-legal-entity-individual-context
- class_count: 6
  name: Adyen Legal Entity Legal Context
  property_count: 28
  slug: adyen-legal-entity-legal-context
- class_count: 1
  name: Adyen Legal Entity Name Context
  property_count: 3
  slug: adyen-legal-entity-name-context
- class_count: 1
  name: Adyen Legal Entity No Context
  property_count: 2
  slug: adyen-legal-entity-no-context
- class_count: 1
  name: Adyen Legal Entity Number Context
  property_count: 4
  slug: adyen-legal-entity-number-context
- class_count: 1
  name: Adyen Legal Entity Nz Context
  property_count: 2
  slug: adyen-legal-entity-nz-context
- class_count: 6
  name: Adyen Legal Entity Onboarding Context
  property_count: 11
  slug: adyen-legal-entity-onboarding-context
- class_count: 3
  name: Adyen Legal Entity Organization Context
  property_count: 14
  slug: adyen-legal-entity-organization-context
- class_count: 1
  name: Adyen Legal Entity Owner Context
  property_count: 2
  slug: adyen-legal-entity-owner-context
- class_count: 3
  name: Adyen Legal Entity Pci Context
  property_count: 6
  slug: adyen-legal-entity-pci-context
- class_count: 1
  name: Adyen Legal Entity Phone Context
  property_count: 2
  slug: adyen-legal-entity-phone-context
- class_count: 1
  name: Adyen Legal Entity Pl Context
  property_count: 2
  slug: adyen-legal-entity-pl-context
- class_count: 1
  name: Adyen Legal Entity Remediating Context
  property_count: 2
  slug: adyen-legal-entity-remediating-context
- class_count: 1
  name: Adyen Legal Entity Se Context
  property_count: 3
  slug: adyen-legal-entity-se-context
- class_count: 1
  name: Adyen Legal Entity Sg Context
  property_count: 3
  slug: adyen-legal-entity-sg-context
- class_count: 3
  name: Adyen Legal Entity Sole Context
  property_count: 9
  slug: adyen-legal-entity-sole-context
- class_count: 2
  name: Adyen Legal Entity Source Context
  property_count: 3
  slug: adyen-legal-entity-source-context
- class_count: 1
  name: Adyen Legal Entity Stock Context
  property_count: 3
  slug: adyen-legal-entity-stock-context
- class_count: 1
  name: Adyen Legal Entity Supporting Context
  property_count: 4
  slug: adyen-legal-entity-supporting-context
- class_count: 2
  name: Adyen Legal Entity Tax Context
  property_count: 6
  slug: adyen-legal-entity-tax-context
- class_count: 1
  name: Adyen Legal Entity Terms Of Service Context
  property_count: 5
  slug: adyen-legal-entity-terms-of-service-context
- class_count: 3
  name: Adyen Legal Entity Transfer Context
  property_count: 10
  slug: adyen-legal-entity-transfer-context
- class_count: 3
  name: Adyen Legal Entity Trust Context
  property_count: 11
  slug: adyen-legal-entity-trust-context
- class_count: 1
  name: Adyen Legal Entity Uk Context
  property_count: 3
  slug: adyen-legal-entity-uk-context
- class_count: 2
  name: Adyen Legal Entity Undefined Context
  property_count: 1
  slug: adyen-legal-entity-undefined-context
- class_count: 3
  name: Adyen Legal Entity Unincorporated Context
  property_count: 10
  slug: adyen-legal-entity-unincorporated-context
- class_count: 1
  name: Adyen Legal Entity Us Context
  property_count: 4
  slug: adyen-legal-entity-us-context
- class_count: 4
  name: Adyen Legal Entity Verification Context
  property_count: 9
  slug: adyen-legal-entity-verification-context
- class_count: 2
  name: Adyen Legal Entity Web Context
  property_count: 3
  slug: adyen-legal-entity-web-context
- class_count: 1
  name: Adyen Management Additional Commission Context
  property_count: 3
  slug: adyen-management-additional-commission-context
- class_count: 2
  name: Adyen Management Additional Settings Context
  property_count: 3
  slug: adyen-management-additional-settings-context
- class_count: 1
  name: Adyen Management Address Context
  property_count: 7
  slug: adyen-management-address-context
- class_count: 1
  name: Adyen Management Afterpay Touch Context
  property_count: 1
  slug: adyen-management-afterpay-touch-context
- class_count: 1
  name: Adyen Management Allowed Origin Context
  property_count: 3
  slug: adyen-management-allowed-origin-context
- class_count: 1
  name: Adyen Management Allowed Origins Context
  property_count: 1
  slug: adyen-management-allowed-origins-context
- class_count: 1
  name: Adyen Management Amount Context
  property_count: 2
  slug: adyen-management-amount-context
- class_count: 2
  name: Adyen Management Android App Context
  property_count: 7
  slug: adyen-management-android-app-context
- class_count: 1
  name: Adyen Management Android Apps Context
  property_count: 1
  slug: adyen-management-android-apps-context
- class_count: 3
  name: Adyen Management Android Certificate Context
  property_count: 5
  slug: adyen-management-android-certificate-context
- class_count: 1
  name: Adyen Management Android Certificates Context
  property_count: 1
  slug: adyen-management-android-certificates-context
- class_count: 3
  name: Adyen Management Api Context
  property_count: 13
  slug: adyen-management-api-context
- class_count: 1
  name: Adyen Management Apple Pay Context
  property_count: 1
  slug: adyen-management-apple-pay-context
- class_count: 1
  name: Adyen Management Bcmc Info Context
  property_count: 2
  slug: adyen-management-bcmc-info-context
- class_count: 1
  name: Adyen Management Billing Entities Context
  property_count: 1
  slug: adyen-management-billing-entities-context
- class_count: 3
  name: Adyen Management Billing Entity Context
  property_count: 3
  slug: adyen-management-billing-entity-context
- class_count: 1
  name: Adyen Management Cardholder Receipt Context
  property_count: 1
  slug: adyen-management-cardholder-receipt-context
- class_count: 1
  name: Adyen Management Cartes Bancaires Context
  property_count: 2
  slug: adyen-management-cartes-bancaires-context
- class_count: 1
  name: Adyen Management Clearpay Info Context
  property_count: 1
  slug: adyen-management-clearpay-info-context
- class_count: 1
  name: Adyen Management Commission Context
  property_count: 2
  slug: adyen-management-commission-context
- class_count: 2
  name: Adyen Management Company Api Context
  property_count: 9
  slug: adyen-management-company-api-context
- class_count: 3
  name: Adyen Management Company Context
  property_count: 5
  slug: adyen-management-company-context
- class_count: 1
  name: Adyen Management Company Links Context
  property_count: 4
  slug: adyen-management-company-links-context
- class_count: 3
  name: Adyen Management Company User Context
  property_count: 9
  slug: adyen-management-company-user-context
- class_count: 1
  name: Adyen Management Configuration Context
  property_count: 4
  slug: adyen-management-configuration-context
- class_count: 1
  name: Adyen Management Connectivity Context
  property_count: 1
  slug: adyen-management-connectivity-context
- class_count: 2
  name: Adyen Management Contact Context
  property_count: 4
  slug: adyen-management-contact-context
- class_count: 1
  name: Adyen Management Create Allowed Context
  property_count: 3
  slug: adyen-management-create-allowed-context
- class_count: 2
  name: Adyen Management Create Api Context
  property_count: 10
  slug: adyen-management-create-api-context
- class_count: 3
  name: Adyen Management Create Company Api Context
  property_count: 11
  slug: adyen-management-create-company-api-context
- class_count: 7
  name: Adyen Management Create Company Context
  property_count: 21
  slug: adyen-management-create-company-context
- class_count: 2
  name: Adyen Management Create Merchant Api Context
  property_count: 2
  slug: adyen-management-create-merchant-api-context
- class_count: 8
  name: Adyen Management Create Merchant Context
  property_count: 22
  slug: adyen-management-create-merchant-context
- class_count: 3
  name: Adyen Management Create User Context
  property_count: 8
  slug: adyen-management-create-user-context
- class_count: 1
  name: Adyen Management Currency Context
  property_count: 3
  slug: adyen-management-currency-context
- class_count: 1
  name: Adyen Management Custom Notification Context
  property_count: 7
  slug: adyen-management-custom-notification-context
- class_count: 2
  name: Adyen Management Data Center Context
  property_count: 1
  slug: adyen-management-data-center-context
- class_count: 1
  name: Adyen Management Event Url Context
  property_count: 2
  slug: adyen-management-event-url-context
- class_count: 1
  name: Adyen Management External Terminal Context
  property_count: 8
  slug: adyen-management-external-terminal-context
- class_count: 2
  name: Adyen Management File Context
  property_count: 1
  slug: adyen-management-file-context
- class_count: 1
  name: Adyen Management Generate Api Context
  property_count: 1
  slug: adyen-management-generate-api-context
- class_count: 1
  name: Adyen Management Generate Client Context
  property_count: 1
  slug: adyen-management-generate-client-context
- class_count: 1
  name: Adyen Management Generate Hmac Context
  property_count: 1
  slug: adyen-management-generate-hmac-context
- class_count: 1
  name: Adyen Management Generic Pm Context
  property_count: 1
  slug: adyen-management-generic-pm-context
- class_count: 1
  name: Adyen Management Giro Pay Context
  property_count: 1
  slug: adyen-management-giro-pay-context
- class_count: 1
  name: Adyen Management Google Pay Context
  property_count: 2
  slug: adyen-management-google-pay-context
- class_count: 1
  name: Adyen Management Gratuity Context
  property_count: 4
  slug: adyen-management-gratuity-context
- class_count: 1
  name: Adyen Management Hardware Context
  property_count: 3
  slug: adyen-management-hardware-context
- class_count: 2
  name: Adyen Management Id Name Context
  property_count: 1
  slug: adyen-management-id-name-context
- class_count: 2
  name: Adyen Management Install Android Context
  property_count: 3
  slug: adyen-management-install-android-context
- class_count: 2
  name: Adyen Management Invalid Field Context
  property_count: 2
  slug: adyen-management-invalid-field-context
- class_count: 1
  name: Adyen Management Json Object Context
  property_count: 0
  slug: adyen-management-json-object-context
- class_count: 3
  name: Adyen Management Key Context
  property_count: 1
  slug: adyen-management-key-context
- class_count: 1
  name: Adyen Management Klarna Info Context
  property_count: 4
  slug: adyen-management-klarna-info-context
- class_count: 1
  name: Adyen Management Links Context
  property_count: 1
  slug: adyen-management-links-context
- class_count: 1
  name: Adyen Management Links Element Context
  property_count: 1
  slug: adyen-management-links-element-context
- class_count: 1
  name: Adyen Management List Company Api Context
  property_count: 4
  slug: adyen-management-list-company-api-context
- class_count: 2
  name: Adyen Management List Company Context
  property_count: 4
  slug: adyen-management-list-company-context
- class_count: 1
  name: Adyen Management List External Context
  property_count: 1
  slug: adyen-management-list-external-context
- class_count: 1
  name: Adyen Management List Merchant Api Context
  property_count: 4
  slug: adyen-management-list-merchant-api-context
- class_count: 2
  name: Adyen Management List Merchant Context
  property_count: 4
  slug: adyen-management-list-merchant-context
- class_count: 1
  name: Adyen Management List Stores Context
  property_count: 4
  slug: adyen-management-list-stores-context
- class_count: 1
  name: Adyen Management List Terminals Context
  property_count: 4
  slug: adyen-management-list-terminals-context
- class_count: 1
  name: Adyen Management List Webhooks Context
  property_count: 5
  slug: adyen-management-list-webhooks-context
- class_count: 1
  name: Adyen Management Localization Context
  property_count: 3
  slug: adyen-management-localization-context
- class_count: 1
  name: Adyen Management Logo Context
  property_count: 1
  slug: adyen-management-logo-context
- class_count: 2
  name: Adyen Management Me Api Context
  property_count: 10
  slug: adyen-management-me-api-context
- class_count: 1
  name: Adyen Management Meal Voucher Context
  property_count: 3
  slug: adyen-management-meal-voucher-context
- class_count: 3
  name: Adyen Management Merchant Context
  property_count: 12
  slug: adyen-management-merchant-context
- class_count: 1
  name: Adyen Management Merchant Links Context
  property_count: 4
  slug: adyen-management-merchant-links-context
- class_count: 1
  name: Adyen Management Minor Units Context
  property_count: 2
  slug: adyen-management-minor-units-context
- class_count: 1
  name: Adyen Management Name Context
  property_count: 2
  slug: adyen-management-name-context
- class_count: 1
  name: Adyen Management Name2 Context
  property_count: 2
  slug: adyen-management-name2-context
- class_count: 1
  name: Adyen Management Nexo Context
  property_count: 5
  slug: adyen-management-nexo-context
- class_count: 1
  name: Adyen Management Notification Context
  property_count: 5
  slug: adyen-management-notification-context
- class_count: 1
  name: Adyen Management Notification Url Context
  property_count: 2
  slug: adyen-management-notification-url-context
- class_count: 1
  name: Adyen Management Offline Processing Context
  property_count: 2
  slug: adyen-management-offline-processing-context
- class_count: 1
  name: Adyen Management Opi Context
  property_count: 3
  slug: adyen-management-opi-context
- class_count: 2
  name: Adyen Management Order Item Context
  property_count: 3
  slug: adyen-management-order-item-context
- class_count: 1
  name: Adyen Management Pagination Links Context
  property_count: 5
  slug: adyen-management-pagination-links-context
- class_count: 1
  name: Adyen Management Passcodes Context
  property_count: 4
  slug: adyen-management-passcodes-context
- class_count: 1
  name: Adyen Management Pay At Context
  property_count: 3
  slug: adyen-management-pay-at-context
- class_count: 1
  name: Adyen Management Pay Pal Context
  property_count: 3
  slug: adyen-management-pay-pal-context
- class_count: 1
  name: Adyen Management Payment Context
  property_count: 2
  slug: adyen-management-payment-context
- class_count: 3
  name: Adyen Management Payment Method Context
  property_count: 42
  slug: adyen-management-payment-method-context
- class_count: 3
  name: Adyen Management Payout Settings Context
  property_count: 8
  slug: adyen-management-payout-settings-context
- class_count: 2
  name: Adyen Management Profile Context
  property_count: 17
  slug: adyen-management-profile-context
- class_count: 1
  name: Adyen Management Receipt Options Context
  property_count: 3
  slug: adyen-management-receipt-options-context
- class_count: 1
  name: Adyen Management Receipt Printing Context
  property_count: 16
  slug: adyen-management-receipt-printing-context
- class_count: 1
  name: Adyen Management Referenced Context
  property_count: 1
  slug: adyen-management-referenced-context
- class_count: 1
  name: Adyen Management Refunds Context
  property_count: 1
  slug: adyen-management-refunds-context
- class_count: 1
  name: Adyen Management Release Update Context
  property_count: 2
  slug: adyen-management-release-update-context
- class_count: 1
  name: Adyen Management Request Activation Context
  property_count: 2
  slug: adyen-management-request-activation-context
- class_count: 1
  name: Adyen Management Rest Service Context
  property_count: 9
  slug: adyen-management-rest-service-context
- class_count: 2
  name: Adyen Management Schedule Terminal Context
  property_count: 8
  slug: adyen-management-schedule-terminal-context
- class_count: 1
  name: Adyen Management Settings Context
  property_count: 3
  slug: adyen-management-settings-context
- class_count: 2
  name: Adyen Management Shipping Location Context
  property_count: 3
  slug: adyen-management-shipping-location-context
- class_count: 1
  name: Adyen Management Shipping Locations Context
  property_count: 1
  slug: adyen-management-shipping-locations-context
- class_count: 1
  name: Adyen Management Signature Context
  property_count: 4
  slug: adyen-management-signature-context
- class_count: 1
  name: Adyen Management Sofort Info Context
  property_count: 2
  slug: adyen-management-sofort-info-context
- class_count: 5
  name: Adyen Management Split Configuration Context
  property_count: 25
  slug: adyen-management-split-configuration-context
- class_count: 1
  name: Adyen Management Standalone Context
  property_count: 2
  slug: adyen-management-standalone-context
- class_count: 2
  name: Adyen Management Store Context
  property_count: 11
  slug: adyen-management-store-context
- class_count: 3
  name: Adyen Management Store Creation Context
  property_count: 8
  slug: adyen-management-store-creation-context
- class_count: 1
  name: Adyen Management Store Location Context
  property_count: 7
  slug: adyen-management-store-location-context
- class_count: 1
  name: Adyen Management Store Split Context
  property_count: 2
  slug: adyen-management-store-split-context
- class_count: 1
  name: Adyen Management Surcharge Context
  property_count: 2
  slug: adyen-management-surcharge-context
- class_count: 1
  name: Adyen Management Swish Info Context
  property_count: 1
  slug: adyen-management-swish-info-context
- class_count: 1
  name: Adyen Management Tap To Context
  property_count: 1
  slug: adyen-management-tap-to-context
- class_count: 1
  name: Adyen Management Terminal Action Context
  property_count: 2
  slug: adyen-management-terminal-action-context
- class_count: 1
  name: Adyen Management Terminal Assignment Context
  property_count: 5
  slug: adyen-management-terminal-assignment-context
- class_count: 5
  name: Adyen Management Terminal Connectivity Context
  property_count: 10
  slug: adyen-management-terminal-connectivity-context
- class_count: 1
  name: Adyen Management Terminal Context
  property_count: 8
  slug: adyen-management-terminal-context
- class_count: 1
  name: Adyen Management Terminal Models Context
  property_count: 1
  slug: adyen-management-terminal-models-context
- class_count: 2
  name: Adyen Management Terminal Order Context
  property_count: 12
  slug: adyen-management-terminal-order-context
- class_count: 1
  name: Adyen Management Terminal Orders Context
  property_count: 1
  slug: adyen-management-terminal-orders-context
- class_count: 4
  name: Adyen Management Terminal Product Context
  property_count: 5
  slug: adyen-management-terminal-product-context
- class_count: 1
  name: Adyen Management Terminal Products Context
  property_count: 1
  slug: adyen-management-terminal-products-context
- class_count: 2
  name: Adyen Management Terminal Reassignment Context
  property_count: 4
  slug: adyen-management-terminal-reassignment-context
- class_count: 1
  name: Adyen Management Terminal Settings Context
  property_count: 20
  slug: adyen-management-terminal-settings-context
- class_count: 1
  name: Adyen Management Test Company Context
  property_count: 3
  slug: adyen-management-test-company-context
- class_count: 1
  name: Adyen Management Test Output Context
  property_count: 6
  slug: adyen-management-test-output-context
- class_count: 2
  name: Adyen Management Test Webhook Context
  property_count: 3
  slug: adyen-management-test-webhook-context
- class_count: 1
  name: Adyen Management Timeouts Context
  property_count: 1
  slug: adyen-management-timeouts-context
- class_count: 1
  name: Adyen Management Transaction Description Context
  property_count: 2
  slug: adyen-management-transaction-description-context
- class_count: 1
  name: Adyen Management Twint Info Context
  property_count: 1
  slug: adyen-management-twint-info-context
- class_count: 2
  name: Adyen Management Uninstall Android Context
  property_count: 3
  slug: adyen-management-uninstall-android-context
- class_count: 1
  name: Adyen Management Updatable Address Context
  property_count: 6
  slug: adyen-management-updatable-address-context
- class_count: 2
  name: Adyen Management Update Company Api Context
  property_count: 4
  slug: adyen-management-update-company-api-context
- class_count: 6
  name: Adyen Management Update Company Context
  property_count: 17
  slug: adyen-management-update-company-context
- class_count: 2
  name: Adyen Management Update Merchant Api Context
  property_count: 3
  slug: adyen-management-update-merchant-api-context
- class_count: 6
  name: Adyen Management Update Merchant Context
  property_count: 14
  slug: adyen-management-update-merchant-context
- class_count: 1
  name: Adyen Management Update Payment Context
  property_count: 18
  slug: adyen-management-update-payment-context
- class_count: 1
  name: Adyen Management Update Payout Context
  property_count: 1
  slug: adyen-management-update-payout-context
- class_count: 4
  name: Adyen Management Update Split Context
  property_count: 19
  slug: adyen-management-update-split-context
- class_count: 2
  name: Adyen Management Update Store Context
  property_count: 6
  slug: adyen-management-update-store-context
- class_count: 1
  name: Adyen Management Upload Android Context
  property_count: 1
  slug: adyen-management-upload-android-context
- class_count: 2
  name: Adyen Management Url Context
  property_count: 3
  slug: adyen-management-url-context
- class_count: 3
  name: Adyen Management User Context
  property_count: 8
  slug: adyen-management-user-context
- class_count: 1
  name: Adyen Management Vipps Info Context
  property_count: 2
  slug: adyen-management-vipps-info-context
- class_count: 3
  name: Adyen Management Webhook Context
  property_count: 20
  slug: adyen-management-webhook-context
- class_count: 1
  name: Adyen Management Webhook Links Context
  property_count: 5
  slug: adyen-management-webhook-links-context
- class_count: 17
  name: Adyen Management Webhooks Context
  property_count: 30
  slug: adyen-management-webhooks-context
- class_count: 1
  name: Adyen Management Wifi Profiles Context
  property_count: 2
  slug: adyen-management-wifi-profiles-context
- class_count: 1
  name: Adyen Notification Configurations Create Context
  property_count: 1
  slug: adyen-notification-configurations-create-context
- class_count: 1
  name: Adyen Notification Configurations Delete Context
  property_count: 1
  slug: adyen-notification-configurations-delete-context
- class_count: 1
  name: Adyen Notification Configurations Empty Context
  property_count: 0
  slug: adyen-notification-configurations-empty-context
- class_count: 1
  name: Adyen Notification Configurations Error Context
  property_count: 3
  slug: adyen-notification-configurations-error-context
- class_count: 1
  name: Adyen Notification Configurations Exchange Context
  property_count: 2
  slug: adyen-notification-configurations-exchange-context
- class_count: 1
  name: Adyen Notification Configurations Field Context
  property_count: 3
  slug: adyen-notification-configurations-field-context
- class_count: 1
  name: Adyen Notification Configurations Generic Context
  property_count: 3
  slug: adyen-notification-configurations-generic-context
- class_count: 3
  name: Adyen Notification Configurations Get Context
  property_count: 6
  slug: adyen-notification-configurations-get-context
- class_count: 3
  name: Adyen Notification Configurations Notification Context
  property_count: 11
  slug: adyen-notification-configurations-notification-context
- class_count: 2
  name: Adyen Notification Configurations Test Context
  property_count: 8
  slug: adyen-notification-configurations-test-context
- class_count: 1
  name: Adyen Notification Configurations Update Context
  property_count: 1
  slug: adyen-notification-configurations-update-context
- class_count: 68
  name: Adyen Notification Webhooks Context
  property_count: 150
  slug: adyen-notification-webhooks-context
- class_count: 86
  name: Adyen Notifications Context
  property_count: 209
  slug: adyen-notifications-context
- class_count: 1
  name: Adyen Payments Account Info Context
  property_count: 19
  slug: adyen-payments-account-info-context
- class_count: 1
  name: Adyen Payments Acct Info Context
  property_count: 16
  slug: adyen-payments-acct-info-context
- class_count: 15
  name: Adyen Payments Additional Data Context
  property_count: 188
  slug: adyen-payments-additional-data-context
- class_count: 1
  name: Adyen Payments Additional Data3 Context
  property_count: 6
  slug: adyen-payments-additional-data3-context
- class_count: 1
  name: Adyen Payments Address Context
  property_count: 6
  slug: adyen-payments-address-context
- class_count: 1
  name: Adyen Payments Adjust Authorisation Context
  property_count: 11
  slug: adyen-payments-adjust-authorisation-context
- class_count: 1
  name: Adyen Payments Amount Context
  property_count: 2
  slug: adyen-payments-amount-context
- class_count: 1
  name: Adyen Payments Application Info Context
  property_count: 6
  slug: adyen-payments-application-info-context
- class_count: 2
  name: Adyen Payments Authentication Result Context
  property_count: 4
  slug: adyen-payments-authentication-result-context
- class_count: 1
  name: Adyen Payments Bank Account Context
  property_count: 9
  slug: adyen-payments-bank-account-context
- class_count: 1
  name: Adyen Payments Browser Info Context
  property_count: 9
  slug: adyen-payments-browser-info-context
- class_count: 1
  name: Adyen Payments Cancel Or Context
  property_count: 9
  slug: adyen-payments-cancel-or-context
- class_count: 1
  name: Adyen Payments Cancel Request Context
  property_count: 10
  slug: adyen-payments-cancel-request-context
- class_count: 1
  name: Adyen Payments Capture Request Context
  property_count: 11
  slug: adyen-payments-capture-request-context
- class_count: 1
  name: Adyen Payments Card Context
  property_count: 8
  slug: adyen-payments-card-context
- class_count: 3
  name: Adyen Payments Common Field Context
  property_count: 0
  slug: adyen-payments-common-field-context
- class_count: 1
  name: Adyen Payments Device Render Context
  property_count: 2
  slug: adyen-payments-device-render-context
- class_count: 1
  name: Adyen Payments Donation Request Context
  property_count: 6
  slug: adyen-payments-donation-request-context
- class_count: 3
  name: Adyen Payments External Platform Context
  property_count: 1
  slug: adyen-payments-external-platform-context
- class_count: 1
  name: Adyen Payments Forex Quote Context
  property_count: 12
  slug: adyen-payments-forex-quote-context
- class_count: 3
  name: Adyen Payments Fraud Check Context
  property_count: 2
  slug: adyen-payments-fraud-check-context
- class_count: 1
  name: Adyen Payments Fraud Result Context
  property_count: 2
  slug: adyen-payments-fraud-result-context
- class_count: 1
  name: Adyen Payments Fund Destination Context
  property_count: 9
  slug: adyen-payments-fund-destination-context
- class_count: 1
  name: Adyen Payments Fund Source Context
  property_count: 6
  slug: adyen-payments-fund-source-context
- class_count: 1
  name: Adyen Payments Installments Context
  property_count: 2
  slug: adyen-payments-installments-context
- class_count: 1
  name: Adyen Payments Mandate Context
  property_count: 8
  slug: adyen-payments-mandate-context
- class_count: 1
  name: Adyen Payments Merchant Device Context
  property_count: 3
  slug: adyen-payments-merchant-device-context
- class_count: 1
  name: Adyen Payments Merchant Risk Context
  property_count: 14
  slug: adyen-payments-merchant-risk-context
- class_count: 1
  name: Adyen Payments Modification Result Context
  property_count: 3
  slug: adyen-payments-modification-result-context
- class_count: 1
  name: Adyen Payments Name Context
  property_count: 2
  slug: adyen-payments-name-context
- class_count: 1
  name: Adyen Payments Payment Request Context
  property_count: 53
  slug: adyen-payments-payment-request-context
- class_count: 1
  name: Adyen Payments Payment Request3D Context
  property_count: 45
  slug: adyen-payments-payment-request3d-context
- class_count: 1
  name: Adyen Payments Payment Request3Ds2 Context
  property_count: 45
  slug: adyen-payments-payment-request3ds2-context
- class_count: 1
  name: Adyen Payments Payment Result Context
  property_count: 11
  slug: adyen-payments-payment-result-context
- class_count: 1
  name: Adyen Payments Phone Context
  property_count: 2
  slug: adyen-payments-phone-context
- class_count: 1
  name: Adyen Payments Platform Chargeback Context
  property_count: 3
  slug: adyen-payments-platform-chargeback-context
- class_count: 1
  name: Adyen Payments Recurring Context
  property_count: 5
  slug: adyen-payments-recurring-context
- class_count: 1
  name: Adyen Payments Refund Request Context
  property_count: 11
  slug: adyen-payments-refund-request-context
- class_count: 9
  name: Adyen Payments Response Additional Context
  property_count: 99
  slug: adyen-payments-response-additional-context
- class_count: 1
  name: Adyen Payments Sdk Ephem Context
  property_count: 4
  slug: adyen-payments-sdk-ephem-context
- class_count: 1
  name: Adyen Payments Shopper Interaction Context
  property_count: 3
  slug: adyen-payments-shopper-interaction-context
- class_count: 1
  name: Adyen Payments Split Amount Context
  property_count: 2
  slug: adyen-payments-split-amount-context
- class_count: 2
  name: Adyen Payments Split Context
  property_count: 4
  slug: adyen-payments-split-context
- class_count: 2
  name: Adyen Payments Sub Merchant Context
  property_count: 4
  slug: adyen-payments-sub-merchant-context
- class_count: 1
  name: Adyen Payments Technical Cancel Context
  property_count: 10
  slug: adyen-payments-technical-cancel-context
- class_count: 1
  name: Adyen Payments Three D Context
  property_count: 12
  slug: adyen-payments-three-d-context
- class_count: 2
  name: Adyen Payments Three Ds Context
  property_count: 7
  slug: adyen-payments-three-ds-context
- class_count: 1
  name: Adyen Payments Three Ds1 Context
  property_count: 6
  slug: adyen-payments-three-ds1-context
- class_count: 4
  name: Adyen Payments Three Ds2 Context
  property_count: 53
  slug: adyen-payments-three-ds2-context
- class_count: 1
  name: Adyen Payments Void Pending Context
  property_count: 11
  slug: adyen-payments-void-pending-context
- class_count: 1
  name: Adyen Payouts Address Context
  property_count: 6
  slug: adyen-payouts-address-context
- class_count: 1
  name: Adyen Payouts Amount Context
  property_count: 2
  slug: adyen-payouts-amount-context
- class_count: 1
  name: Adyen Payouts Bank Account Context
  property_count: 9
  slug: adyen-payouts-bank-account-context
- class_count: 1
  name: Adyen Payouts Card Context
  property_count: 8
  slug: adyen-payouts-card-context
- class_count: 3
  name: Adyen Payouts Fraud Check Context
  property_count: 2
  slug: adyen-payouts-fraud-check-context
- class_count: 1
  name: Adyen Payouts Fraud Result Context
  property_count: 2
  slug: adyen-payouts-fraud-result-context
- class_count: 1
  name: Adyen Payouts Fund Source Context
  property_count: 6
  slug: adyen-payouts-fund-source-context
- class_count: 1
  name: Adyen Payouts Modify Request Context
  property_count: 3
  slug: adyen-payouts-modify-request-context
- class_count: 1
  name: Adyen Payouts Modify Response Context
  property_count: 3
  slug: adyen-payouts-modify-response-context
- class_count: 1
  name: Adyen Payouts Name Context
  property_count: 2
  slug: adyen-payouts-name-context
- class_count: 1
  name: Adyen Payouts Payout Request Context
  property_count: 14
  slug: adyen-payouts-payout-request-context
- class_count: 1
  name: Adyen Payouts Payout Response Context
  property_count: 11
  slug: adyen-payouts-payout-response-context
- class_count: 1
  name: Adyen Payouts Recurring Context
  property_count: 5
  slug: adyen-payouts-recurring-context
- class_count: 9
  name: Adyen Payouts Response Additional Context
  property_count: 99
  slug: adyen-payouts-response-additional-context
- class_count: 4
  name: Adyen Payouts Store Detail Context
  property_count: 23
  slug: adyen-payouts-store-detail-context
- class_count: 1
  name: Adyen Payouts Submit Request Context
  property_count: 15
  slug: adyen-payouts-submit-request-context
- class_count: 1
  name: Adyen Payouts Submit Response Context
  property_count: 4
  slug: adyen-payouts-submit-response-context
- class_count: 1
  name: Adyen Pos Terminal Address Context
  property_count: 6
  slug: adyen-pos-terminal-address-context
- class_count: 2
  name: Adyen Pos Terminal Assign Context
  property_count: 6
  slug: adyen-pos-terminal-assign-context
- class_count: 2
  name: Adyen Pos Terminal Find Context
  property_count: 5
  slug: adyen-pos-terminal-find-context
- class_count: 6
  name: Adyen Pos Terminal Get Context
  property_count: 28
  slug: adyen-pos-terminal-get-context
- class_count: 1
  name: Adyen Pos Terminal Merchant Context
  property_count: 4
  slug: adyen-pos-terminal-merchant-context
- class_count: 2
  name: Adyen Pos Terminal Store Context
  property_count: 5
  slug: adyen-pos-terminal-store-context
- class_count: 1
  name: Adyen Recurring Address Context
  property_count: 6
  slug: adyen-recurring-address-context
- class_count: 1
  name: Adyen Recurring Amount Context
  property_count: 2
  slug: adyen-recurring-amount-context
- class_count: 1
  name: Adyen Recurring Bank Account Context
  property_count: 9
  slug: adyen-recurring-bank-account-context
- class_count: 1
  name: Adyen Recurring Card Context
  property_count: 8
  slug: adyen-recurring-card-context
- class_count: 2
  name: Adyen Recurring Create Permit Context
  property_count: 6
  slug: adyen-recurring-create-permit-context
- class_count: 2
  name: Adyen Recurring Disable Permit Context
  property_count: 4
  slug: adyen-recurring-disable-permit-context
- class_count: 1
  name: Adyen Recurring Disable Request Context
  property_count: 4
  slug: adyen-recurring-disable-request-context
- class_count: 1
  name: Adyen Recurring Disable Result Context
  property_count: 1
  slug: adyen-recurring-disable-result-context
- class_count: 1
  name: Adyen Recurring Name Context
  property_count: 2
  slug: adyen-recurring-name-context
- class_count: 2
  name: Adyen Recurring Notify Shopper Context
  property_count: 13
  slug: adyen-recurring-notify-shopper-context
- class_count: 1
  name: Adyen Recurring Permit Context
  property_count: 5
  slug: adyen-recurring-permit-context
- class_count: 1
  name: Adyen Recurring Permit Restriction Context
  property_count: 3
  slug: adyen-recurring-permit-restriction-context
- class_count: 1
  name: Adyen Recurring Permit Result Context
  property_count: 2
  slug: adyen-recurring-permit-result-context
- class_count: 1
  name: Adyen Recurring Recurring Context
  property_count: 5
  slug: adyen-recurring-recurring-context
- class_count: 3
  name: Adyen Recurring Recurring Detail Context
  property_count: 16
  slug: adyen-recurring-recurring-detail-context
- class_count: 2
  name: Adyen Recurring Recurring Details Context
  property_count: 6
  slug: adyen-recurring-recurring-details-context
- class_count: 2
  name: Adyen Recurring Schedule Account Context
  property_count: 8
  slug: adyen-recurring-schedule-account-context
- class_count: 1
  name: Adyen Recurring Token Details Context
  property_count: 2
  slug: adyen-recurring-token-details-context
- class_count: 6
  name: Adyen Report Webhooks Context
  property_count: 13
  slug: adyen-report-webhooks-context
- class_count: 1
  name: Adyen Stored Value Amount Context
  property_count: 2
  slug: adyen-stored-value-amount-context
- class_count: 12
  name: Adyen Stored Value Stored Context
  property_count: 20
  slug: adyen-stored-value-stored-context
- class_count: 1
  name: Adyen Terminal Abort Request Context
  property_count: 3
  slug: adyen-terminal-abort-request-context
- class_count: 1
  name: Adyen Terminal Account Type Context
  property_count: 0
  slug: adyen-terminal-account-type-context
- class_count: 1
  name: Adyen Terminal Admin Request Context
  property_count: 1
  slug: adyen-terminal-admin-request-context
- class_count: 1
  name: Adyen Terminal Admin Response Context
  property_count: 1
  slug: adyen-terminal-admin-response-context
- class_count: 1
  name: Adyen Terminal Alignment Context
  property_count: 0
  slug: adyen-terminal-alignment-context
- class_count: 1
  name: Adyen Terminal Allowed Product Context
  property_count: 4
  slug: adyen-terminal-allowed-product-context
- class_count: 1
  name: Adyen Terminal Amounts Req Context
  property_count: 8
  slug: adyen-terminal-amounts-req-context
- class_count: 1
  name: Adyen Terminal Amounts Resp Context
  property_count: 6
  slug: adyen-terminal-amounts-resp-context
- class_count: 1
  name: Adyen Terminal Area Size Context
  property_count: 2
  slug: adyen-terminal-area-size-context
- class_count: 1
  name: Adyen Terminal Authentication Method Context
  property_count: 0
  slug: adyen-terminal-authentication-method-context
- class_count: 2
  name: Adyen Terminal Balance Inquiry Context
  property_count: 6
  slug: adyen-terminal-balance-inquiry-context
- class_count: 1
  name: Adyen Terminal Barcode Type Context
  property_count: 0
  slug: adyen-terminal-barcode-type-context
- class_count: 1
  name: Adyen Terminal Captured Signature Context
  property_count: 2
  slug: adyen-terminal-captured-signature-context
- class_count: 3
  name: Adyen Terminal Card Acquisition Context
  property_count: 15
  slug: adyen-terminal-card-acquisition-context
- class_count: 1
  name: Adyen Terminal Card Data Context
  property_count: 11
  slug: adyen-terminal-card-data-context
- class_count: 1
  name: Adyen Terminal Card Holder Context
  property_count: 3
  slug: adyen-terminal-card-holder-context
- class_count: 2
  name: Adyen Terminal Card Reader Context
  property_count: 8
  slug: adyen-terminal-card-reader-context
- class_count: 1
  name: Adyen Terminal Cash Handling Context
  property_count: 3
  slug: adyen-terminal-cash-handling-context
- class_count: 1
  name: Adyen Terminal Character Height Context
  property_count: 0
  slug: adyen-terminal-character-height-context
- class_count: 1
  name: Adyen Terminal Character Style Context
  property_count: 0
  slug: adyen-terminal-character-style-context
- class_count: 1
  name: Adyen Terminal Character Width Context
  property_count: 0
  slug: adyen-terminal-character-width-context
- class_count: 1
  name: Adyen Terminal Check Data Context
  property_count: 7
  slug: adyen-terminal-check-data-context
- class_count: 1
  name: Adyen Terminal Coins Or Context
  property_count: 2
  slug: adyen-terminal-coins-or-context
- class_count: 1
  name: Adyen Terminal Color Context
  property_count: 0
  slug: adyen-terminal-color-context
- class_count: 1
  name: Adyen Terminal Converted Amount Context
  property_count: 2
  slug: adyen-terminal-converted-amount-context
- class_count: 1
  name: Adyen Terminal Currency Conversion Context
  property_count: 6
  slug: adyen-terminal-currency-conversion-context
- class_count: 2
  name: Adyen Terminal Customer Order Context
  property_count: 10
  slug: adyen-terminal-customer-order-context
- class_count: 1
  name: Adyen Terminal Device Context
  property_count: 0
  slug: adyen-terminal-device-context
- class_count: 1
  name: Adyen Terminal Diagnosis Request Context
  property_count: 3
  slug: adyen-terminal-diagnosis-request-context
- class_count: 1
  name: Adyen Terminal Diagnosis Response Context
  property_count: 4
  slug: adyen-terminal-diagnosis-response-context
- class_count: 1
  name: Adyen Terminal Display Output Context
  property_count: 7
  slug: adyen-terminal-display-output-context
- class_count: 1
  name: Adyen Terminal Display Request Context
  property_count: 1
  slug: adyen-terminal-display-request-context
- class_count: 1
  name: Adyen Terminal Display Response Context
  property_count: 1
  slug: adyen-terminal-display-response-context
- class_count: 1
  name: Adyen Terminal Document Qualifier Context
  property_count: 0
  slug: adyen-terminal-document-qualifier-context
- class_count: 2
  name: Adyen Terminal Enable Service Context
  property_count: 4
  slug: adyen-terminal-enable-service-context
- class_count: 1
  name: Adyen Terminal Entry Mode Context
  property_count: 0
  slug: adyen-terminal-entry-mode-context
- class_count: 1
  name: Adyen Terminal Error Condition Context
  property_count: 0
  slug: adyen-terminal-error-condition-context
- class_count: 1
  name: Adyen Terminal Event Notification Context
  property_count: 7
  slug: adyen-terminal-event-notification-context
- class_count: 1
  name: Adyen Terminal Event To Context
  property_count: 0
  slug: adyen-terminal-event-to-context
- class_count: 1
  name: Adyen Terminal Force Entry Context
  property_count: 0
  slug: adyen-terminal-force-entry-context
- class_count: 1
  name: Adyen Terminal Generic Profile Context
  property_count: 0
  slug: adyen-terminal-generic-profile-context
- class_count: 1
  name: Adyen Terminal Geographic Coordinates Context
  property_count: 2
  slug: adyen-terminal-geographic-coordinates-context
- class_count: 1
  name: Adyen Terminal Geolocation Context
  property_count: 2
  slug: adyen-terminal-geolocation-context
- class_count: 2
  name: Adyen Terminal Get Totals Context
  property_count: 5
  slug: adyen-terminal-get-totals-context
- class_count: 1
  name: Adyen Terminal Global Status Context
  property_count: 0
  slug: adyen-terminal-global-status-context
- class_count: 1
  name: Adyen Terminal Host Status Context
  property_count: 2
  slug: adyen-terminal-host-status-context
- class_count: 1
  name: Adyen Terminal Icc Reset Context
  property_count: 2
  slug: adyen-terminal-icc-reset-context
- class_count: 1
  name: Adyen Terminal Identification Support Context
  property_count: 0
  slug: adyen-terminal-identification-support-context
- class_count: 1
  name: Adyen Terminal Identification Type Context
  property_count: 0
  slug: adyen-terminal-identification-type-context
- class_count: 1
  name: Adyen Terminal Info Qualify Context
  property_count: 0
  slug: adyen-terminal-info-qualify-context
- class_count: 1
  name: Adyen Terminal Input Command Context
  property_count: 0
  slug: adyen-terminal-input-command-context
- class_count: 1
  name: Adyen Terminal Input Context
  property_count: 7
  slug: adyen-terminal-input-context
- class_count: 1
  name: Adyen Terminal Input Data Context
  property_count: 21
  slug: adyen-terminal-input-data-context
- class_count: 1
  name: Adyen Terminal Input Request Context
  property_count: 2
  slug: adyen-terminal-input-request-context
- class_count: 1
  name: Adyen Terminal Input Response Context
  property_count: 2
  slug: adyen-terminal-input-response-context
- class_count: 1
  name: Adyen Terminal Input Result Context
  property_count: 4
  slug: adyen-terminal-input-result-context
- class_count: 1
  name: Adyen Terminal Input Update Context
  property_count: 7
  slug: adyen-terminal-input-update-context
- class_count: 1
  name: Adyen Terminal Instalment Context
  property_count: 10
  slug: adyen-terminal-instalment-context
- class_count: 1
  name: Adyen Terminal Instalment Type Context
  property_count: 0
  slug: adyen-terminal-instalment-type-context
- class_count: 1
  name: Adyen Terminal Login Request Context
  property_count: 10
  slug: adyen-terminal-login-request-context
- class_count: 1
  name: Adyen Terminal Login Response Context
  property_count: 4
  slug: adyen-terminal-login-response-context
- class_count: 1
  name: Adyen Terminal Logout Request Context
  property_count: 1
  slug: adyen-terminal-logout-request-context
- class_count: 1
  name: Adyen Terminal Logout Response Context
  property_count: 1
  slug: adyen-terminal-logout-response-context
- class_count: 4
  name: Adyen Terminal Loyalty Account Context
  property_count: 9
  slug: adyen-terminal-loyalty-account-context
- class_count: 1
  name: Adyen Terminal Loyalty Acquirer Context
  property_count: 4
  slug: adyen-terminal-loyalty-acquirer-context
- class_count: 1
  name: Adyen Terminal Loyalty Amount Context
  property_count: 3
  slug: adyen-terminal-loyalty-amount-context
- class_count: 1
  name: Adyen Terminal Loyalty Data Context
  property_count: 3
  slug: adyen-terminal-loyalty-data-context
- class_count: 1
  name: Adyen Terminal Loyalty Handling Context
  property_count: 0
  slug: adyen-terminal-loyalty-handling-context
- class_count: 1
  name: Adyen Terminal Loyalty Request Context
  property_count: 3
  slug: adyen-terminal-loyalty-request-context
- class_count: 1
  name: Adyen Terminal Loyalty Response Context
  property_count: 5
  slug: adyen-terminal-loyalty-response-context
- class_count: 1
  name: Adyen Terminal Loyalty Result Context
  property_count: 5
  slug: adyen-terminal-loyalty-result-context
- class_count: 1
  name: Adyen Terminal Loyalty Totals Context
  property_count: 3
  slug: adyen-terminal-loyalty-totals-context
- class_count: 2
  name: Adyen Terminal Loyalty Transaction Context
  property_count: 5
  slug: adyen-terminal-loyalty-transaction-context
- class_count: 1
  name: Adyen Terminal Loyalty Unit Context
  property_count: 0
  slug: adyen-terminal-loyalty-unit-context
- class_count: 2
  name: Adyen Terminal Menu Entry Context
  property_count: 5
  slug: adyen-terminal-menu-entry-context
- class_count: 1
  name: Adyen Terminal Message Category Context
  property_count: 0
  slug: adyen-terminal-message-category-context
- class_count: 1
  name: Adyen Terminal Message Class Context
  property_count: 0
  slug: adyen-terminal-message-class-context
- class_count: 1
  name: Adyen Terminal Message Header Context
  property_count: 8
  slug: adyen-terminal-message-header-context
- class_count: 1
  name: Adyen Terminal Message Reference Context
  property_count: 5
  slug: adyen-terminal-message-reference-context
- class_count: 1
  name: Adyen Terminal Message Type Context
  property_count: 0
  slug: adyen-terminal-message-type-context
- class_count: 1
  name: Adyen Terminal Mobile Data Context
  property_count: 6
  slug: adyen-terminal-mobile-data-context
- class_count: 1
  name: Adyen Terminal Original Poi Context
  property_count: 9
  slug: adyen-terminal-original-poi-context
- class_count: 1
  name: Adyen Terminal Output Barcode Context
  property_count: 2
  slug: adyen-terminal-output-barcode-context
- class_count: 1
  name: Adyen Terminal Output Content Context
  property_count: 5
  slug: adyen-terminal-output-content-context
- class_count: 1
  name: Adyen Terminal Output Format Context
  property_count: 0
  slug: adyen-terminal-output-format-context
- class_count: 1
  name: Adyen Terminal Output Result Context
  property_count: 3
  slug: adyen-terminal-output-result-context
- class_count: 1
  name: Adyen Terminal Output Text Context
  property_count: 11
  slug: adyen-terminal-output-text-context
- class_count: 2
  name: Adyen Terminal Payment Account Context
  property_count: 6
  slug: adyen-terminal-payment-account-context
- class_count: 1
  name: Adyen Terminal Payment Acquirer Context
  property_count: 6
  slug: adyen-terminal-payment-acquirer-context
- class_count: 1
  name: Adyen Terminal Payment Data Context
  property_count: 7
  slug: adyen-terminal-payment-data-context
- class_count: 2
  name: Adyen Terminal Payment Instrument Context
  property_count: 5
  slug: adyen-terminal-payment-instrument-context
- class_count: 1
  name: Adyen Terminal Payment Receipt Context
  property_count: 4
  slug: adyen-terminal-payment-receipt-context
- class_count: 1
  name: Adyen Terminal Payment Request Context
  property_count: 4
  slug: adyen-terminal-payment-request-context
- class_count: 1
  name: Adyen Terminal Payment Response Context
  property_count: 7
  slug: adyen-terminal-payment-response-context
- class_count: 1
  name: Adyen Terminal Payment Result Context
  property_count: 13
  slug: adyen-terminal-payment-result-context
- class_count: 1
  name: Adyen Terminal Payment Token Context
  property_count: 3
  slug: adyen-terminal-payment-token-context
- class_count: 1
  name: Adyen Terminal Payment Totals Context
  property_count: 3
  slug: adyen-terminal-payment-totals-context
- class_count: 1
  name: Adyen Terminal Payment Transaction Context
  property_count: 4
  slug: adyen-terminal-payment-transaction-context
- class_count: 1
  name: Adyen Terminal Payment Type Context
  property_count: 0
  slug: adyen-terminal-payment-type-context
- class_count: 1
  name: Adyen Terminal Performed Transaction Context
  property_count: 6
  slug: adyen-terminal-performed-transaction-context
- class_count: 1
  name: Adyen Terminal Period Unit Context
  property_count: 0
  slug: adyen-terminal-period-unit-context
- class_count: 1
  name: Adyen Terminal Pin Format Context
  property_count: 0
  slug: adyen-terminal-pin-format-context
- class_count: 1
  name: Adyen Terminal Pin Request Context
  property_count: 0
  slug: adyen-terminal-pin-request-context
- class_count: 1
  name: Adyen Terminal Poi Capabilities Context
  property_count: 0
  slug: adyen-terminal-poi-capabilities-context
- class_count: 1
  name: Adyen Terminal Poi Data Context
  property_count: 2
  slug: adyen-terminal-poi-data-context
- class_count: 1
  name: Adyen Terminal Poi Profile Context
  property_count: 2
  slug: adyen-terminal-poi-profile-context
- class_count: 1
  name: Adyen Terminal Poi Software Context
  property_count: 4
  slug: adyen-terminal-poi-software-context
- class_count: 1
  name: Adyen Terminal Poi Status Context
  property_count: 8
  slug: adyen-terminal-poi-status-context
- class_count: 1
  name: Adyen Terminal Poi System Context
  property_count: 4
  slug: adyen-terminal-poi-system-context
- class_count: 1
  name: Adyen Terminal Poi Terminal Context
  property_count: 4
  slug: adyen-terminal-poi-terminal-context
- class_count: 1
  name: Adyen Terminal Point Context
  property_count: 2
  slug: adyen-terminal-point-context
- class_count: 1
  name: Adyen Terminal Predefined Content Context
  property_count: 2
  slug: adyen-terminal-predefined-content-context
- class_count: 1
  name: Adyen Terminal Print Output Context
  property_count: 5
  slug: adyen-terminal-print-output-context
- class_count: 1
  name: Adyen Terminal Print Request Context
  property_count: 1
  slug: adyen-terminal-print-request-context
- class_count: 1
  name: Adyen Terminal Print Response Context
  property_count: 2
  slug: adyen-terminal-print-response-context
- class_count: 1
  name: Adyen Terminal Printer Status Context
  property_count: 0
  slug: adyen-terminal-printer-status-context
- class_count: 1
  name: Adyen Terminal Rebates Context
  property_count: 3
  slug: adyen-terminal-rebates-context
- class_count: 1
  name: Adyen Terminal Reconciliation Request Context
  property_count: 3
  slug: adyen-terminal-reconciliation-request-context
- class_count: 1
  name: Adyen Terminal Reconciliation Response Context
  property_count: 4
  slug: adyen-terminal-reconciliation-response-context
- class_count: 1
  name: Adyen Terminal Reconciliation Type Context
  property_count: 0
  slug: adyen-terminal-reconciliation-type-context
- class_count: 1
  name: Adyen Terminal Repeated Message Context
  property_count: 2
  slug: adyen-terminal-repeated-message-context
- class_count: 1
  name: Adyen Terminal Repeated Response Context
  property_count: 6
  slug: adyen-terminal-repeated-response-context
- class_count: 1
  name: Adyen Terminal Response Context
  property_count: 3
  slug: adyen-terminal-response-context
- class_count: 1
  name: Adyen Terminal Response Mode Context
  property_count: 0
  slug: adyen-terminal-response-mode-context
- class_count: 1
  name: Adyen Terminal Result Context
  property_count: 0
  slug: adyen-terminal-result-context
- class_count: 1
  name: Adyen Terminal Reversal Reason Context
  property_count: 0
  slug: adyen-terminal-reversal-reason-context
- class_count: 1
  name: Adyen Terminal Reversal Request Context
  property_count: 5
  slug: adyen-terminal-reversal-request-context
- class_count: 1
  name: Adyen Terminal Reversal Response Context
  property_count: 6
  slug: adyen-terminal-reversal-response-context
- class_count: 1
  name: Adyen Terminal Sale Capabilities Context
  property_count: 0
  slug: adyen-terminal-sale-capabilities-context
- class_count: 1
  name: Adyen Terminal Sale Data Context
  property_count: 12
  slug: adyen-terminal-sale-data-context
- class_count: 2
  name: Adyen Terminal Sale Item Context
  property_count: 12
  slug: adyen-terminal-sale-item-context
- class_count: 1
  name: Adyen Terminal Sale Software Context
  property_count: 4
  slug: adyen-terminal-sale-software-context
- class_count: 1
  name: Adyen Terminal Sale Terminal Context
  property_count: 1
  slug: adyen-terminal-sale-terminal-context
- class_count: 1
  name: Adyen Terminal Sale To Context
  property_count: 1
  slug: adyen-terminal-sale-to-context
- class_count: 1
  name: Adyen Terminal Security Trailer Context
  property_count: 5
  slug: adyen-terminal-security-trailer-context
- class_count: 1
  name: Adyen Terminal Sensitive Card Context
  property_count: 4
  slug: adyen-terminal-sensitive-card-context
- class_count: 1
  name: Adyen Terminal Sensitive Mobile Context
  property_count: 3
  slug: adyen-terminal-sensitive-mobile-context
- class_count: 1
  name: Adyen Terminal Service Context
  property_count: 0
  slug: adyen-terminal-service-context
- class_count: 1
  name: Adyen Terminal Services Enabled Context
  property_count: 0
  slug: adyen-terminal-services-enabled-context
- class_count: 1
  name: Adyen Terminal Sound Action Context
  property_count: 0
  slug: adyen-terminal-sound-action-context
- class_count: 1
  name: Adyen Terminal Sound Content Context
  property_count: 4
  slug: adyen-terminal-sound-content-context
- class_count: 1
  name: Adyen Terminal Sound Format Context
  property_count: 0
  slug: adyen-terminal-sound-format-context
- class_count: 8
  name: Adyen Terminal Stored Value Context
  property_count: 18
  slug: adyen-terminal-stored-value-context
- class_count: 1
  name: Adyen Terminal Terminal Environment Context
  property_count: 0
  slug: adyen-terminal-terminal-environment-context
- class_count: 1
  name: Adyen Terminal Token Requested Context
  property_count: 0
  slug: adyen-terminal-token-requested-context
- class_count: 1
  name: Adyen Terminal Total Details Context
  property_count: 0
  slug: adyen-terminal-total-details-context
- class_count: 1
  name: Adyen Terminal Total Filter Context
  property_count: 5
  slug: adyen-terminal-total-filter-context
- class_count: 1
  name: Adyen Terminal Track Data Context
  property_count: 3
  slug: adyen-terminal-track-data-context
- class_count: 1
  name: Adyen Terminal Track Format Context
  property_count: 0
  slug: adyen-terminal-track-format-context
- class_count: 1
  name: Adyen Terminal Transaction Action Context
  property_count: 0
  slug: adyen-terminal-transaction-action-context
- class_count: 1
  name: Adyen Terminal Transaction Conditions Context
  property_count: 9
  slug: adyen-terminal-transaction-conditions-context
- class_count: 1
  name: Adyen Terminal Transaction Id Context
  property_count: 2
  slug: adyen-terminal-transaction-id-context
- class_count: 2
  name: Adyen Terminal Transaction Status Context
  property_count: 5
  slug: adyen-terminal-transaction-status-context
- class_count: 1
  name: Adyen Terminal Transaction Totals Context
  property_count: 14
  slug: adyen-terminal-transaction-totals-context
- class_count: 1
  name: Adyen Terminal Transaction Type Context
  property_count: 0
  slug: adyen-terminal-transaction-type-context
- class_count: 1
  name: Adyen Terminal Type Code Context
  property_count: 0
  slug: adyen-terminal-type-code-context
- class_count: 1
  name: Adyen Terminal Unit Of Context
  property_count: 0
  slug: adyen-terminal-unit-of-context
- class_count: 1
  name: Adyen Terminal Utm Coordinates Context
  property_count: 3
  slug: adyen-terminal-utm-coordinates-context
- class_count: 1
  name: Adyen Test Cards Avs Context
  property_count: 2
  slug: adyen-test-cards-avs-context
- class_count: 2
  name: Adyen Test Cards Create Context
  property_count: 4
  slug: adyen-test-cards-create-context
- class_count: 2
  name: Adyen Test Cards Test Context
  property_count: 14
  slug: adyen-test-cards-test-context
- class_count: 8
  name: Adyen Transaction Webhooks Context
  property_count: 17
  slug: adyen-transaction-webhooks-context
- class_count: 49
  name: Adyen Transfer Webhooks Context
  property_count: 101
  slug: adyen-transfer-webhooks-context
- class_count: 1
  name: Adyen Transfers Additional Bank Context
  property_count: 2
  slug: adyen-transfers-additional-bank-context
- class_count: 1
  name: Adyen Transfers Address Context
  property_count: 6
  slug: adyen-transfers-address-context
- class_count: 1
  name: Adyen Transfers Amount Context
  property_count: 2
  slug: adyen-transfers-amount-context
- class_count: 1
  name: Adyen Transfers Au Local Context
  property_count: 3
  slug: adyen-transfers-au-local-context
- class_count: 1
  name: Adyen Transfers Bank Account Context
  property_count: 2
  slug: adyen-transfers-bank-account-context
- class_count: 1
  name: Adyen Transfers Bank Category Context
  property_count: 2
  slug: adyen-transfers-bank-category-context
- class_count: 1
  name: Adyen Transfers Br Local Context
  property_count: 4
  slug: adyen-transfers-br-local-context
- class_count: 1
  name: Adyen Transfers Ca Local Context
  property_count: 5
  slug: adyen-transfers-ca-local-context
- class_count: 1
  name: Adyen Transfers Capital Balance Context
  property_count: 4
  slug: adyen-transfers-capital-balance-context
- class_count: 2
  name: Adyen Transfers Capital Grant Context
  property_count: 9
  slug: adyen-transfers-capital-grant-context
- class_count: 1
  name: Adyen Transfers Capital Grants Context
  property_count: 1
  slug: adyen-transfers-capital-grants-context
- class_count: 1
  name: Adyen Transfers Counterparty Context
  property_count: 3
  slug: adyen-transfers-counterparty-context
- class_count: 1
  name: Adyen Transfers Counterparty Info Context
  property_count: 3
  slug: adyen-transfers-counterparty-info-context
- class_count: 1
  name: Adyen Transfers Counterparty V3 Context
  property_count: 4
  slug: adyen-transfers-counterparty-v3-context
- class_count: 1
  name: Adyen Transfers Cz Local Context
  property_count: 3
  slug: adyen-transfers-cz-local-context
- class_count: 1
  name: Adyen Transfers Dk Local Context
  property_count: 3
  slug: adyen-transfers-dk-local-context
- class_count: 1
  name: Adyen Transfers Fee Context
  property_count: 1
  slug: adyen-transfers-fee-context
- class_count: 1
  name: Adyen Transfers Hk Local Context
  property_count: 3
  slug: adyen-transfers-hk-local-context
- class_count: 1
  name: Adyen Transfers Hu Local Context
  property_count: 2
  slug: adyen-transfers-hu-local-context
- class_count: 1
  name: Adyen Transfers Iban Account Context
  property_count: 2
  slug: adyen-transfers-iban-account-context
- class_count: 1
  name: Adyen Transfers Internal Category Context
  property_count: 3
  slug: adyen-transfers-internal-category-context
- class_count: 2
  name: Adyen Transfers Invalid Field Context
  property_count: 2
  slug: adyen-transfers-invalid-field-context
- class_count: 1
  name: Adyen Transfers Issued Card Context
  property_count: 8
  slug: adyen-transfers-issued-card-context
- class_count: 1
  name: Adyen Transfers Json Object Context
  property_count: 0
  slug: adyen-transfers-json-object-context
- class_count: 1
  name: Adyen Transfers Link Context
  property_count: 1
  slug: adyen-transfers-link-context
- class_count: 1
  name: Adyen Transfers Links Context
  property_count: 2
  slug: adyen-transfers-links-context
- class_count: 1
  name: Adyen Transfers Merchant Data Context
  property_count: 5
  slug: adyen-transfers-merchant-data-context
- class_count: 2
  name: Adyen Transfers Name Location Context
  property_count: 5
  slug: adyen-transfers-name-location-context
- class_count: 1
  name: Adyen Transfers No Local Context
  property_count: 2
  slug: adyen-transfers-no-local-context
- class_count: 1
  name: Adyen Transfers Number And Context
  property_count: 4
  slug: adyen-transfers-number-and-context
- class_count: 1
  name: Adyen Transfers Nz Local Context
  property_count: 2
  slug: adyen-transfers-nz-local-context
- class_count: 1
  name: Adyen Transfers Party Identification Context
  property_count: 7
  slug: adyen-transfers-party-identification-context
- class_count: 2
  name: Adyen Transfers Payment Instrument Context
  property_count: 3
  slug: adyen-transfers-payment-instrument-context
- class_count: 1
  name: Adyen Transfers Pl Local Context
  property_count: 2
  slug: adyen-transfers-pl-local-context
- class_count: 1
  name: Adyen Transfers Platform Payment Context
  property_count: 6
  slug: adyen-transfers-platform-payment-context
- class_count: 1
  name: Adyen Transfers Relayed Authorisation Context
  property_count: 2
  slug: adyen-transfers-relayed-authorisation-context
- class_count: 1
  name: Adyen Transfers Repayment Context
  property_count: 3
  slug: adyen-transfers-repayment-context
- class_count: 1
  name: Adyen Transfers Repayment Term Context
  property_count: 2
  slug: adyen-transfers-repayment-term-context
- class_count: 2
  name: Adyen Transfers Resource Reference Context
  property_count: 2
  slug: adyen-transfers-resource-reference-context
- class_count: 1
  name: Adyen Transfers Rest Service Context
  property_count: 9
  slug: adyen-transfers-rest-service-context
- class_count: 2
  name: Adyen Transfers Return Transfer Context
  property_count: 5
  slug: adyen-transfers-return-transfer-context
- class_count: 1
  name: Adyen Transfers Se Local Context
  property_count: 3
  slug: adyen-transfers-se-local-context
- class_count: 1
  name: Adyen Transfers Sg Local Context
  property_count: 3
  slug: adyen-transfers-sg-local-context
- class_count: 1
  name: Adyen Transfers Threshold Repayment Context
  property_count: 1
  slug: adyen-transfers-threshold-repayment-context
- class_count: 1
  name: Adyen Transfers Transaction Context
  property_count: 10
  slug: adyen-transfers-transaction-context
- class_count: 1
  name: Adyen Transfers Transaction Search Context
  property_count: 2
  slug: adyen-transfers-transaction-search-context
- class_count: 2
  name: Adyen Transfers Transfer Context
  property_count: 14
  slug: adyen-transfers-transfer-context
- class_count: 1
  name: Adyen Transfers Transfer Data Context
  property_count: 2
  slug: adyen-transfers-transfer-data-context
- class_count: 2
  name: Adyen Transfers Transfer Info Context
  property_count: 9
  slug: adyen-transfers-transfer-info-context
- class_count: 1
  name: Adyen Transfers Transfer Notification Context
  property_count: 2
  slug: adyen-transfers-transfer-notification-context
- class_count: 1
  name: Adyen Transfers Uk Local Context
  property_count: 3
  slug: adyen-transfers-uk-local-context
- class_count: 1
  name: Adyen Transfers Ultimate Party Context
  property_count: 7
  slug: adyen-transfers-ultimate-party-context
- class_count: 1
  name: Adyen Transfers Us Local Context
  property_count: 4
  slug: adyen-transfers-us-local-context
- class_count: 27
  name: Adyen Webhooks Context
  property_count: 171
  slug: adyen-webhooks-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Adyen
nav: Providers
network: true
overview: 'Adyen publishes 138 APIs on the [APIs.io](https://apis.io/) network, including acceptDispute API, Account API, accountHolderBalance API, and 135 more. Tagged areas include Payments, Financial-Services, and Fintech.


  The Adyen catalog on APIs.io includes 1 event-driven AsyncAPI specification, 854 JSON-LD contexts, and 3 Spectral governance rulesets.


  Adyen''s developer surface includes authentication, sandbox, changelog, pricing, documentation, getting-started guide, engineering blog, and 61 more developer resources.'
plans:
- name: Adyen Plans Pricing
  plan_count: 2
  slug: adyen-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Adyen Rate Limits
  slug: adyen-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Adyen API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: adyen-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Adyen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adyen-jsonschema-spectral-rules
- effective_rule_count: 32
  extends: []
  name: Adyen API Rules
  rule_count: 32
  severity_counts:
    error: 12
    hint: 0
    info: 6
    warn: 14
  slug: adyen-spectral-rules
score:
  band: exemplar
  composite: 66.9
  coverage:
    artifact_dirs: 28
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 28.8
    contract_quality: 76.0
    developer_ergonomics: 69.0
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 44.7
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 93.9
      derived: 0
      marker_coverage: 0.0
      total: 212
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/screenshots/adyen-2026-06-20T165409.png
security:
- kind: authentication
  name: Adyen Authentication
  slug: adyen-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Adyen Domain Security
  slug: adyen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adyen Vulnerability Disclosure
  slug: adyen-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Adyen Trust Center
  slug: adyen-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: adyen
tags:
- Payments
- Financial-Services
- Fintech
use_cases:
- description: Accept payments on web and mobile with Drop-in or Components, supporting all major payment methods and currencies.
  name: Online Checkout
- description: Process in-person payments using Adyen's Terminal API and supported payment terminals with tap, dip, and swipe capabilities.
  name: Point-of-Sale Payments
- description: Manage recurring payments and subscriptions using stored payment methods and tokenization.
  name: Subscription and Recurring Billing
- description: Onboard sub-merchants, split payments, and manage payouts to sellers and service providers on marketplace platforms.
  name: Marketplace and Platform Payouts
- description: Offer BNPL options including Affirm, Afterpay, and Klarna to shoppers at checkout to increase conversion.
  name: Buy Now Pay Later
- description: Issue and manage gift cards and stored value products with balance inquiry, load, and redemption capabilities.
  name: Gift Cards and Stored Value
- description: Automate dispute handling processes to respond to chargebacks with defense documents and evidence.
  name: Dispute and Chargeback Management
- description: Process subject erasure requests to comply with GDPR right-to-be-forgotten requirements for shopper data.
  name: GDPR Data Erasure
---
