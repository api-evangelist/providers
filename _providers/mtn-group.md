---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 246
  human_in_the_loop: 14
  name: Mtn Group Agentic Access
  operation_count: 475
  slug: mtn-group-agentic-access
  summary_line: 475 operations · 246 acting · 14 human-in-the-loop
api_count: 115
apis:
- description: Enable remote collection of bills, fees or taxes from consumer and business MoMo wallets. Operations include RequestToPay, invoices, pre-approvals, delivery notification, account balance and account h
  name: MTN MoMo Collection API
  slug: momo-collection
- description: Disburse payments from a business MoMo wallet to consumers or other businesses — salary payments, benefits disbursement and supplier payouts — with deposit, refund, transfer and transaction-status ope
  name: MTN MoMo Disbursements API
  slug: momo-disbursement
- description: Transfer funds into MTN MoMo wallets from remittance originators, including cash transfer, transfer, account balance and account holder validation operations.
  name: MTN MoMo Remittance API
  slug: momo-remittance
- description: Provision sandbox API users and API keys for the MTN MoMo Open API test environment, the self-serve step that lets a developer obtain credentials before calling Collection, Disbursements or Remittance
  name: MTN MoMo Sandbox User Provisioning API
  slug: momo-sandbox-user-provisioning
- description: Accessible to Client APP (3PP) - ApiKeyAuth, to subscribe (MO/MT), unsubscribe and push/send message.
  name: MTN Group Accessible to 3PP API
  slug: mtn-group-accessible-to-3pp-api
- description: Used by USSDGW - using ApiKeyAuth, to send MO generated messages to 3PP through MADAPI.
  name: MTN Group Accessible to USSD Gateway API
  slug: mtn-group-accessible-to-ussd-gateway-api
- description: The Activation API from MTN Group — 1 operation(s) for activation.
  name: MTN Group Activation API
  slug: mtn-group-activation-api
- description: The Add User API from MTN Group — 1 operation(s) for add user.
  name: MTN Group Add User API
  slug: mtn-group-add-user-api
- description: The Admin Suspend API from MTN Group — 1 operation(s) for admin suspend.
  name: MTN Group Admin Suspend API
  slug: mtn-group-admin-suspend-api
- description: The Adverts API from MTN Group — 3 operation(s) for adverts.
  name: MTN Group Adverts API
  slug: mtn-group-adverts-api
- description: The Advice Reconcile API from MTN Group — 1 operation(s) for advice reconcile.
  name: MTN Group Advice Reconcile API
  slug: mtn-group-advice-reconcile-api
- description: The agents API from MTN Group — 4 operation(s) for agents.
  name: MTN Group Agents API
  slug: mtn-group-agents-api
- description: The appliedCustomerBillingRate API from MTN Group — 2 operation(s) for appliedcustomerbillingrate.
  name: MTN Group Applied Customer Billing Rate API
  slug: mtn-group-appliedcustomerbillingrate-api
- description: The auth API from MTN Group — 1 operation(s) for auth.
  name: MTN Group Auth API
  slug: mtn-group-auth-api
- description: The Balance Buckets Methods API from MTN Group — 1 operation(s) for balance buckets methods.
  name: MTN Group Balance Buckets Methods API
  slug: mtn-group-balance-buckets-methods-api
- description: The Balance Management API from MTN Group — 1 operation(s) for balance management.
  name: MTN Group Balance Management API
  slug: mtn-group-balance-management-api
- description: The BalanceTransfer API from MTN Group — 1 operation(s) for balancetransfer.
  name: MTN Group Balance Transfer API
  slug: mtn-group-balancetransfer-api
- description: The banktech API from MTN Group — 1 operation(s) for banktech.
  name: MTN Group Banktech API
  slug: mtn-group-banktech-api
- description: The Callback API from MTN Group — 2 operation(s) for callback.
  name: MTN Group Callback API
  slug: mtn-group-callback-api
- description: The Callmeback API from MTN Group — 1 operation(s) for callmeback.
  name: MTN Group Callmeback API
  slug: mtn-group-callmeback-api
- description: The callmeback with geographicLocation API from MTN Group — 1 operation(s) for callmeback with geographiclocation.
  name: MTN Group callmeback with geographicLocation API
  slug: mtn-group-callmeback-with-geographiclocation-api
- description: The Cancel Customer PreApproval API from MTN Group — 1 operation(s) for cancel customer preapproval.
  name: MTN Group Cancel Customer PreApproval API
  slug: mtn-group-cancel-customer-preapproval-api
- description: The capabilityCheck API from MTN Group — 1 operation(s) for capabilitycheck.
  name: MTN Group Capability Check API
  slug: mtn-group-capabilitycheck-api
- description: The catalog API from MTN Group — 2 operation(s) for catalog.
  name: MTN Group Catalog API
  slug: mtn-group-catalog-api
- description: The category API from MTN Group — 1 operation(s) for category.
  name: MTN Group Category API
  slug: mtn-group-category-api
- description: Channel VAS Controller
  name: MTN Group Channel Vas Controller API
  slug: mtn-group-channel-vas-controller-api
- description: The channelService API from MTN Group — 1 operation(s) for channelservice.
  name: MTN Group Channel Service API
  slug: mtn-group-channelservice-api
- description: The Communication API from MTN Group — 4 operation(s) for communication.
  name: MTN Group Communication API
  slug: mtn-group-communication-api
- description: The communicationMessage API from MTN Group — 4 operation(s) for communicationmessage.
  name: MTN Group Communication Message API
  slug: mtn-group-communicationmessage-api
- description: The Consent API from MTN Group — 2 operation(s) for consent.
  name: MTN Group Consent API
  slug: mtn-group-consent-api
- description: Consent Validation Implementation to confirm user consent
  name: MTN Group Consent Validation API
  slug: mtn-group-consent-validation-api
- description: The Content Push API from MTN Group — 2 operation(s) for content push.
  name: MTN Group Content Push API
  slug: mtn-group-content-push-api
- description: The Create Customer API from MTN Group — 1 operation(s) for create customer.
  name: MTN Group Create Customer API
  slug: mtn-group-create-customer-api
- description: The Create Customer PreApproval API from MTN Group — 1 operation(s) for create customer preapproval.
  name: MTN Group Create Customer PreApproval API
  slug: mtn-group-create-customer-preapproval-api
- description: The Customer API from MTN Group — 10 operation(s) for customer.
  name: MTN Group Customer API
  slug: mtn-group-customer-api
- description: The Customer Attribute API from MTN Group — 1 operation(s) for customer attribute.
  name: MTN Group Customer Attribute API
  slug: mtn-group-customer-attribute-api
- description: The Customer Characteristics API from MTN Group — 1 operation(s) for customer characteristics.
  name: MTN Group Customer Characteristics API
  slug: mtn-group-customer-characteristics-api
- description: The Customer Information API from MTN Group — 1 operation(s) for customer information.
  name: MTN Group Customer Information API
  slug: mtn-group-customer-information-api
- description: The Customer KYC API from MTN Group — 7 operation(s) for customer kyc.
  name: MTN Group Customer KYC API
  slug: mtn-group-customer-kyc-api
- description: The Customer Mobile Carrier Data API from MTN Group — 2 operation(s) for customer mobile carrier data.
  name: MTN Group Customer Mobile Carrier Data API
  slug: mtn-group-customer-mobile-carrier-data-api
- description: The Customer Promotion API from MTN Group — 3 operation(s) for customer promotion.
  name: MTN Group Customer Promotion API
  slug: mtn-group-customer-promotion-api
- description: The customerBill API from MTN Group — 2 operation(s) for customerbill.
  name: MTN Group Customer Bill API
  slug: mtn-group-customerbill-api
- description: The customerBillOnDemand API from MTN Group — 2 operation(s) for customerbillondemand.
  name: MTN Group Customer Bill On Demand API
  slug: mtn-group-customerbillondemand-api
- description: The Customers API from MTN Group — 21 operation(s) for customers.
  name: MTN Group Customers API
  slug: mtn-group-customers-api
- description: The CustomerTransferService API from MTN Group — 3 operation(s) for customertransferservice.
  name: MTN Group Customer Transfer Service API
  slug: mtn-group-customertransferservice-api
- description: The Deactivation API from MTN Group — 1 operation(s) for deactivation.
  name: MTN Group Deactivation API
  slug: mtn-group-deactivation-api
- description: The Debit API from MTN Group — 1 operation(s) for debit.
  name: MTN Group Debit API
  slug: mtn-group-debit-api
- description: The Device Information API from MTN Group — 1 operation(s) for device information.
  name: MTN Group Device Information API
  slug: mtn-group-device-information-api
- description: The Device Swap API API from MTN Group — 2 operation(s) for device swap api.
  name: MTN Group Device Swap API
  slug: mtn-group-device-swap-api-api
- description: The document API from MTN Group — 2 operation(s) for document.
  name: MTN Group Document API
  slug: mtn-group-document-api
- description: The Employee Leaves API from MTN Group — 1 operation(s) for employee leaves.
  name: MTN Group Employee Leaves API
  slug: mtn-group-employee-leaves-api
- description: The event API from MTN Group — 2 operation(s) for event.
  name: MTN Group Event API
  slug: mtn-group-event-api
- description: The events subscription API from MTN Group — 2 operation(s) for events subscription.
  name: MTN Group events subscription API
  slug: mtn-group-events-subscription-api
- description: The FinancialAccount API from MTN Group — 4 operation(s) for financialaccount.
  name: MTN Group Financial Account API
  slug: mtn-group-financialaccount-api
- description: The fraudManagement API from MTN Group — 2 operation(s) for fraudmanagement.
  name: MTN Group Fraud Management API
  slug: mtn-group-fraudmanagement-api
- description: The GENEYSIS-EEC-TOKENS API from MTN Group — 1 operation(s) for geneysis-eec-tokens.
  name: MTN Group GENEYSIS EEC TOKENS API
  slug: mtn-group-geneysis-eec-tokens-api
- description: The Get access token API from MTN Group — 1 operation(s) for get access token.
  name: MTN Group Get access token API
  slug: mtn-group-get-access-token-api
- description: The getInfo API from MTN Group — 1 operation(s) for getinfo.
  name: MTN Group Get Info API
  slug: mtn-group-getinfo-api
- description: The hub API from MTN Group — 2 operation(s) for hub.
  name: MTN Group Hub API
  slug: mtn-group-hub-api
- description: The Incident ticket API from MTN Group — 1 operation(s) for incident ticket.
  name: MTN Group Incident ticket API
  slug: mtn-group-incident-ticket-api
- description: The individual API from MTN Group — 2 operation(s) for individual.
  name: MTN Group Individual API
  slug: mtn-group-individual-api
- description: The Kyc API from MTN Group — 2 operation(s) for kyc.
  name: MTN Group Kyc API
  slug: mtn-group-kyc-api
- description: The license-aggregator-controller API from MTN Group — 2 operation(s) for license-aggregator-controller.
  name: MTN Group License Aggregator Controller API
  slug: mtn-group-license-aggregator-controller-api
- description: The Link Accounts API from MTN Group — 1 operation(s) for link accounts.
  name: MTN Group Link Accounts API
  slug: mtn-group-link-accounts-api
- description: The Loyalty Balance API from MTN Group — 1 operation(s) for loyalty balance.
  name: MTN Group Loyalty Balance API
  slug: mtn-group-loyalty-balance-api
- description: The Loyalty Burn API from MTN Group — 1 operation(s) for loyalty burn.
  name: MTN Group Loyalty Burn API
  slug: mtn-group-loyalty-burn-api
- description: The Loyalty Member API from MTN Group — 2 operation(s) for loyalty member.
  name: MTN Group Loyalty Member API
  slug: mtn-group-loyalty-member-api
- description: The Loyalty Program Product API from MTN Group — 2 operation(s) for loyalty program product.
  name: MTN Group Loyalty Program Product API
  slug: mtn-group-loyalty-program-product-api
- description: The Member Summary API from MTN Group — 1 operation(s) for member summary.
  name: MTN Group Member Summary API
  slug: mtn-group-member-summary-api
- description: The Mobile Ads Service API from MTN Group — 1 operation(s) for mobile ads service.
  name: MTN Group Mobile Ads Service API
  slug: mtn-group-mobile-ads-service-api
- description: The MoMo API from MTN Group — 1 operation(s) for momo.
  name: MTN Group Mo Mo API
  slug: mtn-group-momo-api
- description: The monitor API from MTN Group — 2 operation(s) for monitor.
  name: MTN Group Monitor API
  slug: mtn-group-monitor-api
- description: The netflix-integration-controller API from MTN Group — 4 operation(s) for netflix-integration-controller.
  name: MTN Group Netflix Integration Controller API
  slug: mtn-group-netflix-integration-controller-api
- description: The notification listeners (client side) API from MTN Group — 15 operation(s) for notification listeners (client side).
  name: MTN Group notification listeners (client side) API
  slug: mtn-group-notification-listeners-client-side-api
- description: Send Notifications
  name: MTN Group Notifications API
  slug: mtn-group-notifications-api
- description: The NumberRecycleService API from MTN Group — 1 operation(s) for numberrecycleservice.
  name: MTN Group Number Recycle Service API
  slug: mtn-group-numberrecycleservice-api
- description: The OrderFulfillment API from MTN Group — 1 operation(s) for orderfulfillment.
  name: MTN Group Order Fulfillment API
  slug: mtn-group-orderfulfillment-api
- description: The organization API from MTN Group — 2 operation(s) for organization.
  name: MTN Group Organization API
  slug: mtn-group-organization-api
- description: The Organizations API from MTN Group — 3 operation(s) for organizations.
  name: MTN Group Organizations API
  slug: mtn-group-organizations-api
- description: The OTP API from MTN Group — 2 operation(s) for otp.
  name: MTN Group OTP API
  slug: mtn-group-otp-api
- description: The partners API from MTN Group — 2 operation(s) for partners.
  name: MTN Group Partners API
  slug: mtn-group-partners-api
- description: The partyAccount API from MTN Group — 1 operation(s) for partyaccount.
  name: MTN Group Party Account API
  slug: mtn-group-partyaccount-api
- description: The partyInteraction API from MTN Group — 1 operation(s) for partyinteraction.
  name: MTN Group Party Interaction API
  slug: mtn-group-partyinteraction-api
- description: The partyRoleRiskAssessment API from MTN Group — 8 operation(s) for partyroleriskassessment.
  name: MTN Group Party Role Risk Assessment API
  slug: mtn-group-partyroleriskassessment-api
- description: The Payment API from MTN Group — 13 operation(s) for payment.
  name: MTN Group Payment API
  slug: mtn-group-payment-api
- description: The payment methods API from MTN Group — 2 operation(s) for payment methods.
  name: MTN Group payment methods API
  slug: mtn-group-payment-methods-api
- description: The PIN API from MTN Group — 2 operation(s) for pin.
  name: MTN Group PIN API
  slug: mtn-group-pin-api
- description: The Policy API from MTN Group — 1 operation(s) for policy.
  name: MTN Group Policy API
  slug: mtn-group-policy-api
- description: The Premiums API from MTN Group — 1 operation(s) for premiums.
  name: MTN Group Premiums API
  slug: mtn-group-premiums-api
- description: The Process Operations API from MTN Group — 6 operation(s) for process operations.
  name: MTN Group Process Operations API
  slug: mtn-group-process-operations-api
- description: The product API from MTN Group — 2 operation(s) for product.
  name: MTN Group Product API
  slug: mtn-group-product-api
- description: The Productivity Report API from MTN Group — 1 operation(s) for productivity report.
  name: MTN Group Productivity Report API
  slug: mtn-group-productivity-report-api
- description: The productOffering API from MTN Group — 1 operation(s) for productoffering.
  name: MTN Group Product Offering API
  slug: mtn-group-productoffering-api
- description: The productOrder API from MTN Group — 2 operation(s) for productorder.
  name: MTN Group Product Order API
  slug: mtn-group-productorder-api
- description: The products API from MTN Group — 13 operation(s) for products.
  name: MTN Group Products API
  slug: mtn-group-products-api
- description: The Provider API from MTN Group — 3 operation(s) for provider.
  name: MTN Group Provider API
  slug: mtn-group-provider-api
- description: The Purchase API from MTN Group — 1 operation(s) for purchase.
  name: MTN Group Purchase API
  slug: mtn-group-purchase-api
- description: The Query By Data API from MTN Group — 1 operation(s) for query by data.
  name: MTN Group Query By Data API
  slug: mtn-group-query-by-data-api
- description: The Query By Transaction ID API from MTN Group — 1 operation(s) for query by transaction id.
  name: MTN Group Query By Transaction ID API
  slug: mtn-group-query-by-transaction-id-api
- description: The Query logback by targetURL and country code API from MTN Group — 1 operation(s) for query logback by targeturl and country code.
  name: MTN Group Query logback by targetURL and country code API
  slug: mtn-group-query-logback-by-targeturl-and-country-code-api
- description: The Quotation API from MTN Group — 1 operation(s) for quotation.
  name: MTN Group Quotation API
  slug: mtn-group-quotation-api
- description: The Receiving SMS API from MTN Group — 1 operation(s) for receiving sms.
  name: MTN Group Receiving SMS API
  slug: mtn-group-receiving-sms-api
- description: The Reference Data Operations API from MTN Group — 3 operation(s) for reference data operations.
  name: MTN Group Reference Data Operations API
  slug: mtn-group-reference-data-operations-api
- description: The Refund API from MTN Group — 1 operation(s) for refund.
  name: MTN Group Refund API
  slug: mtn-group-refund-api
- description: The Registration API from MTN Group — 7 operation(s) for registration.
  name: MTN Group Registration API
  slug: mtn-group-registration-api
- description: The Reporting API from MTN Group — 1 operation(s) for reporting.
  name: MTN Group Reporting API
  slug: mtn-group-reporting-api
- description: The resource API from MTN Group — 2 operation(s) for resource.
  name: MTN Group Resource API
  slug: mtn-group-resource-api
- description: The ResourceFunction API from MTN Group — 1 operation(s) for resourcefunction.
  name: MTN Group Resource Function API
  slug: mtn-group-resourcefunction-api
- description: The resourceOrder API from MTN Group — 2 operation(s) for resourceorder.
  name: MTN Group Resource Order API
  slug: mtn-group-resourceorder-api
- description: The salesLead API from MTN Group — 1 operation(s) for saleslead.
  name: MTN Group Sales Lead API
  slug: mtn-group-saleslead-api
- description: The Sending SMS API from MTN Group — 4 operation(s) for sending sms.
  name: MTN Group Sending SMS API
  slug: mtn-group-sending-sms-api
- description: The service-activation-controller API from MTN Group — 1 operation(s) for service-activation-controller.
  name: MTN Group Service Activation Controller API
  slug: mtn-group-service-activation-controller-api
- description: The service API from MTN Group — 2 operation(s) for service.
  name: MTN Group Service API
  slug: mtn-group-service-api
- description: The serviceOrder API from MTN Group — 2 operation(s) for serviceorder.
  name: MTN Group Service Order API
  slug: mtn-group-serviceorder-api
- description: The shoppingCart API from MTN Group — 6 operation(s) for shoppingcart.
  name: MTN Group Shopping Cart API
  slug: mtn-group-shoppingcart-api
- description: The siebel API from MTN Group — 3 operation(s) for siebel.
  name: MTN Group Siebel API
  slug: mtn-group-siebel-api
- description: The Sim Activation API from MTN Group — 2 operation(s) for sim activation.
  name: MTN Group Sim Activation API
  slug: mtn-group-sim-activation-api
- description: The SIM & MSISDN Availability APIs API from MTN Group — 3 operation(s) for sim & msisdn availability apis.
  name: MTN Group SIM & MSISDN Availability APIs API
  slug: mtn-group-sim-msisdn-availability-apis-api
- description: The Sim Recycle API from MTN Group — 1 operation(s) for sim recycle.
  name: MTN Group Sim Recycle API
  slug: mtn-group-sim-recycle-api
- description: The SIM Swap API API from MTN Group — 1 operation(s) for sim swap api.
  name: MTN Group SIM Swap API
  slug: mtn-group-sim-swap-api-api
- description: The Sim Swap API from MTN Group — 2 operation(s) for sim swap.
  name: MTN Group Sim Swap API
  slug: mtn-group-sim-swap-api
- description: The SimManagementService API from MTN Group — 11 operation(s) for simmanagementservice.
  name: MTN Group Sim Management Service API
  slug: mtn-group-simmanagementservice-api
- description: The status API from MTN Group — 3 operation(s) for status.
  name: MTN Group Status API
  slug: mtn-group-status-api
- description: The Submit Withdrawal Request API from MTN Group — 1 operation(s) for submit withdrawal request.
  name: MTN Group Submit Withdrawal Request API
  slug: mtn-group-submit-withdrawal-request-api
- description: Subscriber Attributes Controller
  name: MTN Group Subscriber Attributes Controller API
  slug: mtn-group-subscriber-attributes-controller-api
- description: The Subscriber Type API from MTN Group — 1 operation(s) for subscriber type.
  name: MTN Group Subscriber Type API
  slug: mtn-group-subscriber-type-api
- description: The subscriberinfo API from MTN Group — 2 operation(s) for subscriberinfo.
  name: MTN Group Subscriberinfo API
  slug: mtn-group-subscriberinfo-api
- description: The Subscribing for Mobile Originating and Delivery Receipts API from MTN Group — 2 operation(s) for subscribing for mobile originating and delivery receipts.
  name: MTN Group Subscribing for Mobile Originating and Delivery Receipts API
  slug: mtn-group-subscribing-for-mobile-originating-and-delivery-receipts-api
- description: The Taxation API from MTN Group — 1 operation(s) for taxation.
  name: MTN Group Taxation API
  slug: mtn-group-taxation-api
- description: The TMF632 Party Management API from MTN Group — 5 operation(s) for tmf632 party management.
  name: MTN Group TMF632 Party Management API
  slug: mtn-group-tmf632-party-management-api
- description: The TMF676 Payment Management Aggregator API from MTN Group — 2 operation(s) for tmf676 payment management aggregator.
  name: MTN Group TMF676 Payment Management Aggregator API
  slug: mtn-group-tmf676-payment-management-aggregator-api
- description: The TMF908 IoT Device Management API from MTN Group — 3 operation(s) for tmf908 iot device management.
  name: MTN Group TMF908 IoT Device Management API
  slug: mtn-group-tmf908-iot-device-management-api
- description: The topic API from MTN Group — 2 operation(s) for topic.
  name: MTN Group Topic API
  slug: mtn-group-topic-api
- description: The Track ticket API from MTN Group — 2 operation(s) for track ticket.
  name: MTN Group Track ticket API
  slug: mtn-group-track-ticket-api
- description: The trouble-ticket-aggregator-controller API from MTN Group — 5 operation(s) for trouble-ticket-aggregator-controller.
  name: MTN Group Trouble Ticket Aggregator Controller API
  slug: mtn-group-trouble-ticket-aggregator-controller-api
- description: The Unified Balance Enquiry API from MTN Group — 1 operation(s) for unified balance enquiry.
  name: MTN Group Unified Balance Enquiry API
  slug: mtn-group-unified-balance-enquiry-api
- description: The urlCreate API from MTN Group — 1 operation(s) for urlcreate.
  name: MTN Group URL Create API
  slug: mtn-group-urlcreate-api
- description: The Usage Historical Information API from MTN Group — 1 operation(s) for usage historical information.
  name: MTN Group Usage Historical Information API
  slug: mtn-group-usage-historical-information-api
- description: The Usage Limit Adjust API from MTN Group — 1 operation(s) for usage limit adjust.
  name: MTN Group Usage Limit Adjust API
  slug: mtn-group-usage-limit-adjust-api
- description: The usageConsumptionReport API from MTN Group — 2 operation(s) for usageconsumptionreport.
  name: MTN Group Usage Consumption Report API
  slug: mtn-group-usageconsumptionreport-api
- description: The UsageManagement API from MTN Group — 12 operation(s) for usagemanagement.
  name: MTN Group Usage Management API
  slug: mtn-group-usagemanagement-api
- description: The UsageManagementsSSd API from MTN Group — 3 operation(s) for usagemanagementsssd.
  name: MTN Group Usage Managements S Sd API
  slug: mtn-group-usagemanagementsssd-api
- description: The Users API from MTN Group — 3 operation(s) for users.
  name: MTN Group Users API
  slug: mtn-group-users-api
- description: The Validate an Individual's Account Status API from MTN Group — 1 operation(s) for validate an individual's account status.
  name: MTN Group Validate an Individual's Account Status API
  slug: mtn-group-validate-an-individual-s-account-status-api
- description: The Validate Customer API from MTN Group — 1 operation(s) for validate customer.
  name: MTN Group Validate Customer API
  slug: mtn-group-validate-customer-api
- description: The Validate using QnA API from MTN Group — 2 operation(s) for validate using qna.
  name: MTN Group Validate using QnA API
  slug: mtn-group-validate-using-qna-api
- description: The VAS Services API from MTN Group — 5 operation(s) for vas services.
  name: MTN Group VAS Services API
  slug: mtn-group-vas-services-api
- description: The Verify a Partner's FInancial Resources API from MTN Group — 1 operation(s) for verify a partner's financial resources.
  name: MTN Group Verify a Partner's FInancial Resources API
  slug: mtn-group-verify-a-partner-s-financial-resources-api
artifact_total: 261
asyncapis:
- description: ''
  name: Mtn Group Webhooks
  slug: mtn-group-webhooks
collections:
- collection_type: open
  name: Account Decisioning API
  slug: open-mtn-group-account-decisioning
- collection_type: open
  name: TMF666 Account Management API
  slug: open-mtn-group-account-management-coe
- collection_type: open
  name: Mobile Advertisement
  slug: open-mtn-group-advertising-v2
- collection_type: open
  name: MTN Agent Profile API
  slug: open-mtn-group-agent-profile
- collection_type: open
  name: Consent Validation API
  slug: open-mtn-group-ayo-preapproval
- collection_type: open
  name: MTN Accountholders API
  slug: open-mtn-group-ayoaccountholderinfo
- collection_type: open
  name: Balance Management V1
  slug: open-mtn-group-balance-management-v1
- collection_type: open
  name: Authentication APIs
  slug: open-mtn-group-bss-tt-oauth-v1
- collection_type: open
  name: Callmeback V1
  slug: open-mtn-group-callmeback-v1
- collection_type: open
  name: Callmeback V2
  slug: open-mtn-group-callmeback-v2
- collection_type: open
  name: Communication Management API
  slug: open-mtn-group-communication-management-v1
- collection_type: open
  name: Content Push API
  slug: open-mtn-group-content-push
- collection_type: open
  name: MTN Customer Account Management API
  slug: open-mtn-group-customer-account-management-v1
- collection_type: open
  name: Customer Billing Token API
  slug: open-mtn-group-customer-billing-token-v1
- collection_type: open
  name: Customer Transfer
  slug: open-mtn-group-customer-data-transfer-ng-prod
- collection_type: open
  name: Customer Delivery Booking API
  slug: open-mtn-group-customer-delivery-booking
- collection_type: open
  name: Customer Identification API
  slug: open-mtn-group-customer-identification-v1
- collection_type: open
  name: MTN Customer KYC Verification API
  slug: open-mtn-group-customer-kyc-verification
- collection_type: open
  name: Customer Loyalty Management API
  slug: open-mtn-group-customer-loyalty-management
- collection_type: open
  name: Customer Management - COE
  slug: open-mtn-group-customer-management-coe-za-preprod
- collection_type: open
  name: MTN Customer Management API
  slug: open-mtn-group-customer-management
- collection_type: open
  name: Customer PIN Management API
  slug: open-mtn-group-customer-pin-management-v2
- collection_type: open
  name: Customer Promotion Placeholder
  slug: open-mtn-group-customer-promotion
- collection_type: open
  name: Device Swap API
  slug: open-mtn-group-device-swap-v1
- collection_type: open
  name: Digital Partners Management API
  slug: open-mtn-group-digital-partner-management
- collection_type: open
  name: Document
  slug: open-mtn-group-document-managment
- collection_type: open
  name: GENEYSIS - EEC TOKENS MANAGEMENT API-mtn
  slug: open-mtn-group-eec-token-management
- collection_type: open
  name: MTN G2M Product Offering API
  slug: open-mtn-group-g2m
- collection_type: open
  name: Leave Balance
  slug: open-mtn-group-hcm-v1
- collection_type: open
  name: Insurance API
  slug: open-mtn-group-insurance
- collection_type: open
  name: IoT Device Management
  slug: open-mtn-group-iot-device-management
- collection_type: open
  name: ServiceNow - Remedy Incident synchronisation
  slug: open-mtn-group-job-card-management
- collection_type: open
  name: Customer Kyc Consent
  slug: open-mtn-group-kyc-consent
- collection_type: open
  name: MTN Customer Loan API
  slug: open-mtn-group-loans-v2
- collection_type: open
  name: Logback Failure Service
  slug: open-mtn-group-logback-v1
- collection_type: open
  name: Medallia SMS Experience API
  slug: open-mtn-group-medallia-sms-v2
- collection_type: open
  name: MTN Merchant Provisioning API
  slug: open-mtn-group-merchant-provisioning-v1
- collection_type: open
  name: Mobile Customer Information API
  slug: open-mtn-group-mobile-customer-information
- collection_type: open
  name: MoMo Verification API
  slug: open-mtn-group-momo-verification
- collection_type: open
  name: Mobile Advertisement API
  slug: open-mtn-group-mtn-advertising-api-v1
- collection_type: open
  name: Customer Bill Management API
  slug: open-mtn-group-mtn-customer-bill-management
- collection_type: open
  name: Customer Transfer
  slug: open-mtn-group-mtn-customer-datatransfer
- collection_type: open
  name: Api Documentation
  slug: open-mtn-group-mtn-customer-loans-api-v1
- collection_type: open
  name: MTN Customer Plans API
  slug: open-mtn-group-mtn-customer-plans-api-v2
- collection_type: open
  name: MTN Customer Score API
  slug: open-mtn-group-mtn-customer-score
- collection_type: open
  name: Customer Data Share API
  slug: open-mtn-group-mtn-nigeria-customer-datashare
- collection_type: open
  name: Customer Data Gifting API
  slug: open-mtn-group-mtn-nigeria-data-gifting-v1
- collection_type: open
  name: Party Management API
  slug: open-mtn-group-mtn-party-management
- collection_type: open
  name: MTN Product API
  slug: open-mtn-group-mtn-product-offering-api-v2
- collection_type: open
  name: MTN Product API
  slug: open-mtn-group-mtn-product-offering-api-v3
- collection_type: open
  name: MTN Messaging API
  slug: open-mtn-group-mtn-sms-api-v1
- collection_type: open
  name: MTNID-getInfo
  slug: open-mtn-group-mtnid-getinfo
- collection_type: open
  name: Notifications API
  slug: open-mtn-group-notification-production
- collection_type: open
  name: Notifications API
  slug: open-mtn-group-notification-v2
- collection_type: open
  name: MTN MADAPI OAuth2
  slug: open-mtn-group-oauth-v1
- collection_type: open
  name: Order Fulfillment API
  slug: open-mtn-group-order-fulfillment
- collection_type: open
  name: Payment Methods Management
  slug: open-mtn-group-payment-methods-management-sa
- collection_type: open
  name: Payments v1
  slug: open-mtn-group-payments-v1
- collection_type: open
  name: Product Catalog Management
  slug: open-mtn-group-product-catalog-coe
- collection_type: open
  name: Product Catalog Management
  slug: open-mtn-group-product-catalog-management-v1
- collection_type: open
  name: Product Catalog Management
  slug: open-mtn-group-product-catalogue-management
- collection_type: open
  name: Product Ordering
  slug: open-mtn-group-product-ordering-coe
- collection_type: open
  name: Api Documentation Unified Balance
  slug: open-mtn-group-provisioning
- collection_type: open
  name: Madapi-MTN-RCS API
  slug: open-mtn-group-rcs-capability
- collection_type: open
  name: Communication Management
  slug: open-mtn-group-rcs-communication
- collection_type: open
  name: Resource Configuration API
  slug: open-mtn-group-resource-config-v1
- collection_type: open
  name: TMF685 - Resource Pool Management - BSS
  slug: open-mtn-group-resource-pool-management
- collection_type: open
  name: MTN Customer Risk Management API
  slug: open-mtn-group-risk-management
- collection_type: open
  name: Party Management API
  slug: open-mtn-group-rwanda-party-management
- collection_type: open
  name: API Sales
  slug: open-mtn-group-sales-management
- collection_type: open
  name: API Service Activation and Configuration
  slug: open-mtn-group-service-activation-and-configuration
- collection_type: open
  name: API ServiceOrdering
  slug: open-mtn-group-service-ordering
- collection_type: open
  name: MTN Siebel API
  slug: open-mtn-group-siebel
- collection_type: open
  name: Sim Management
  slug: open-mtn-group-sim-management-staging
- collection_type: open
  name: SIM Swap Verification API
  slug: open-mtn-group-sim-swap-verification-v1
- collection_type: open
  name: MTN Customer SIM Verification API
  slug: open-mtn-group-simverification
- collection_type: open
  name: Short Message Service (SMS) API
  slug: open-mtn-group-sms-v3-api
- collection_type: open
  name: Api Documentation
  slug: open-mtn-group-subscriber-details
- collection_type: open
  name: Subscriber Management API
  slug: open-mtn-group-subscriber-management
- collection_type: open
  name: Api Documentation
  slug: open-mtn-group-subscriber-type
- collection_type: open
  name: Taxation
  slug: open-mtn-group-taxation-v1
- collection_type: open
  name: ServiceNow - Remedy Incident synchronisation
  slug: open-mtn-group-ticket
- collection_type: open
  name: Digital Identity Management
  slug: open-mtn-group-tmf-720-digital-identity-management
- collection_type: open
  name: API CustomerBill
  slug: open-mtn-group-tmf-customer-bill-management
- collection_type: open
  name: Document Management
  slug: open-mtn-group-tmf-document-management-tmf667
- collection_type: open
  name: LoyaltySwagger
  slug: open-mtn-group-tmf-loyalty-management-tmf658
- collection_type: open
  name: Party Interaction
  slug: open-mtn-group-tmf-party-interaction-tmf683
- collection_type: open
  name: MTN TMF632 Party Management Aggregator Service
  slug: open-mtn-group-tmf-party-management
- collection_type: open
  name: TMF676 Payment Management
  slug: open-mtn-group-tmf-payment-management-tmf676
- collection_type: open
  name: Prepay Balance Management
  slug: open-mtn-group-tmf-prepay-balance-management-tmf654
- collection_type: open
  name: Product Catalog Management
  slug: open-mtn-group-tmf-product-catalog-tmf620
- collection_type: open
  name: Product Ordering
  slug: open-mtn-group-tmf-product-ordering-tmf622
- collection_type: open
  name: Resource Ordering Management
  slug: open-mtn-group-tmf-resource-ordering-tmf652
- collection_type: open
  name: API Resource Inventory Management
  slug: open-mtn-group-tmf-resourceinventorymanagement-tmf639
- collection_type: open
  name: service-activation-aggregator
  slug: open-mtn-group-tmf-service-activation-tmf678
- collection_type: open
  name: TMF621 Trouble Ticket Management  Aggregator
  slug: open-mtn-group-tmf-trouble-ticket-tmf621
- collection_type: open
  name: Usage Consumption API
  slug: open-mtn-group-tmf-usage-consumption-tmf677
- collection_type: open
  name: MTN Usage Management
  slug: open-mtn-group-tmf-usage-management-tmf635
- collection_type: open
  name: TMF629- Customer Management
  slug: open-mtn-group-tmf629-customer-management
- collection_type: open
  name: MTN Shopping Cart Management API
  slug: open-mtn-group-tmf633-shopping-cart-management
- collection_type: open
  name: Communication Management API TMF-681
  slug: open-mtn-group-tmf681-communication-management
- collection_type: open
  name: Event Streaming API
  slug: open-mtn-group-tmf688-event-management
- collection_type: open
  name: Api Documentation Unified Balance
  slug: open-mtn-group-unified-balance-v1
- collection_type: open
  name: Usage Consumption API
  slug: open-mtn-group-usage-consumption
- collection_type: open
  name: MTN Usage Management
  slug: open-mtn-group-usage-management
- collection_type: open
  name: MTN Messaging USSD API
  slug: open-mtn-group-ussd
- collection_type: open
  name: Mobile Money Withdrawals v1
  slug: open-mtn-group-withdrawals-v1
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/mtn-group-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-account-decisioning-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-customer-bill-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-customer-loans-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-subscriber-details-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-subscriber-type-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-provisioning-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-unified-balance-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-resourceinventorymanagement-tmf639-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-sales-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-service-activation-and-configuration-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-service-ordering-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-bss-tt-oauth-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-balance-management-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-callmeback-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-callmeback-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-rcs-communication-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-communication-management-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf681-communication-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-ayo-preapproval-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-content-push-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-customer-bill-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-billing-token-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-nigeria-data-gifting-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-nigeria-customer-datashare-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-delivery-booking-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-identification-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-kyc-consent-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-loyalty-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-management-coe-za-preprod-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-pin-management-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-promotion-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-survey-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-data-transfer-ng-prod-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-customer-datatransfer-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-device-swap-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-720-digital-identity-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-digital-partner-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-document-managment-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-document-management-tmf667-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf688-event-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-eec-token-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-insurance-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-iot-device-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-hcm-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-logback-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-loyalty-management-tmf658-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-rcs-capability-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-medallia-sms-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-advertising-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-advertising-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mobile-customer-information-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-withdrawals-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-momo-verification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-ayoaccountholderinfo-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-agent-profile-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-account-management-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-customer-kyc-api-v1-product-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-kyc-verification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-loans-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-customer-locations-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-customer-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-customer-plans-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-customer-profiles-api-v2-product-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-risk-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-customer-score-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-simverification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-subscription-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-g2m-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-oauth-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-merchant-provisioning-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-sms-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-ussd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-product-offering-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-product-offering-api-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-ng-retailer-productivity-tracking-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf633-shopping-cart-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-siebel-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-party-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-usage-management-tmf635-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-usage-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtnid-getinfo-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-notification-production-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-notification-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-order-fulfillment-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-party-interaction-tmf683-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-party-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-rwanda-party-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-payment-methods-management-sa-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-payments-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-prepay-balance-management-tmf654-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-product-catalog-coe-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-product-catalog-management-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-product-catalogue-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-product-catalog-tmf620-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-product-ordering-coe-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-product-ordering-tmf622-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-resource-config-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-resource-ordering-tmf652-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-service-activation-tmf678-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-job-card-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-ticket-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-mtn-sms-interface-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-sms-v3-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-sim-management-staging-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-sim-swap-verification-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-subscriber-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-taxation-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-trouble-ticket-tmf621-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf629-customer-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf637-product-inventory-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-account-management-coe-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-payment-management-tmf676-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-resource-pool-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-tmf-usage-consumption-tmf677-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mtn-group-usage-consumption-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mtn-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mtn-group-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mtn-group-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mtn-group-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mtn.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mtn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.mtn.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.mtn.com/products
- group: start
  title: ''
  type: DeveloperPortal
  url: https://momodeveloper.mtn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://momodeveloper.mtn.com/api-documentation
- group: start
  title: ''
  type: SignUp
  url: https://developers.mtn.com/register
- group: start
  title: ''
  type: SignUp
  url: https://momodeveloper.mtn.com/signup
- group: auth
  title: ''
  type: Authentication
  url: https://developers.mtn.com/getting-started
- group: operate
  title: ''
  type: FAQ
  url: https://developers.mtn.com/faq
- group: operate
  title: ''
  type: Support
  url: https://developers.mtn.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.mtn.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.mtn.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MTN-Group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mtn/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MTNGroup
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/TheMTNGroup
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.mtn.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.mtn.com/news/
- group: operate
  title: ''
  type: Community
  url: https://momodevelopercommunity.mtn.com/
- group: operate
  title: ''
  type: Support
  url: https://momodeveloper.mtn.com/contact-support
- group: start
  title: ''
  type: Login
  url: https://developers.mtn.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://momodeveloper.mtn.com/API-collections
- group: other
  title: ''
  type: BestPractices
  url: https://momodeveloper.mtn.com/best-practices
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.mtn.com/getting-started/response-and-error-codes
- group: build
  title: ''
  type: Packages
  url: packages/mtn-group-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mtn-group-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mtn-group-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mtn-group-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/mtn-group-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mtn-group-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/mtn-group-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mtn-group-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.mtn.com/getting-started/things-every-developer-should-know
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mtn-group-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mtn-group-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mtn-group-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/mtn-group-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mtn-group-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mtn-group-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/mtn-group-send-sms.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/mtn-group-collect-a-payment.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/mtn-group-momo-request-to-pay.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/mtn-group-place-a-product-order.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/mtn-group-manage-subscriptions.md
created: '2026-07-25'
description: 'MTN Group is Africa''s largest mobile network operator, headquartered in Johannesburg, South Africa, serving roughly 290 million subscribers across around 16 markets in Africa. Beyond mobile voice, data and enterprise connectivity it runs MoMo, one of the continent''s largest mobile-money platforms. Unusually for a carrier, MTN publishes a genuinely open developer surface: the MTN Developer Platform (MADAPI) at developers.mtn.com lists 221 API products across 15 African markets and lets anyone download the OpenAPI/Swagger definition for a product without an account, and momodeveloper.mtn.com is a self-serve Azure API Management portal with a sandbox for the MoMo Collection, Disbursements and Remittance APIs. Its catalogue is heavily TM Forum Open API shaped (TMF620, TMF621, TMF622, TMF629, TMF632, TMF633, TMF635, TMF637, TMF639, TMF652, TMF654, TMF658, TMF666, TMF667, TMF676, TMF677, TMF678, TMF681, TMF683, TMF685, TMF688, TMF720). MTN South Africa is a GSMA Open Gateway participant
  — it announced Number Verification and SIM Swap with Cell C and Telkom in February 2024 — but nothing in its published catalogue is CAMARA-shaped: its SIM Swap and Device Swap APIs are MTN-proprietary designs secured with OAuth2 client-credentials rather than the CAMARA OIDC/CIBA profile, and no CAMARA API is callable from either portal. MTN is not an Aduna shareholder. Sandbox access is self-serve; production access is vetted and commercially negotiated.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: MTN Group MCP Server
  slug: mtn-group-mcp-server
modified: '2026-07-25'
name: MTN Group
nav: Providers
network: true
overview: 'MTN Group publishes 144 APIs on the [APIs.io](https://apis.io/) network, including Accessible to 3PP API, Accessible to USSD Gateway API, Activation API, and 141 more. Tagged areas include Telecommunications, South Africa, Africa, Mobile Network Operator, and Network APIs.


  The MTN Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MTN Group''s developer surface includes authentication, documentation, API reference, signup flow, FAQ, support, YouTube channel, and 159 more developer resources.'
random_paper: 13
scopes:
- name: Mtn Group Scopes
  scope_count: 2
  slug: mtn-group-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 58.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 91.0
      derived: 0
      marker_coverage: 0.0
      total: 144
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 66.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mtn-group/refs/heads/main/screenshots/mtn-group-2026-08-07T184423.png
security:
- kind: authentication
  name: Mtn Group Authentication
  slug: mtn-group-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Mtn Group Domain Security
  slug: mtn-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mtn-group
tags:
- Telecommunications
- South Africa
- Africa
- Mobile Network Operator
- Network APIs
- Open Gateway
- TM Forum
- BSS
- Mobile Money
- Messaging
- SMS
- USSD
- IoT
- SIM Swap
- Identity Verification
- Payments
website: https://www.mtn.com/
---
