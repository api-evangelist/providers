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
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 388
  human_in_the_loop: 4
  name: Payrix Agentic Access
  operation_count: 851
  slug: payrix-agentic-access
  summary_line: 851 operations · 388 acting · 4 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Accounts deals with payment account details for merchant boarding and entity funding. Ultimately, all the business performed within Payrix Pro (be it merchant transactions, vendor income, or facilitat
  name: Payrix Accounts API
  slug: payrix-accounts-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Accounts Verification represents an attempt to verify the ownership of a particular bank account by verifying a known deposit amount or credential.
  name: Payrix Accounts Verifications API
  slug: payrix-accounts-verifications-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A way to make monetary adjustments to an entity's funds.
  name: Payrix Adjustments API
  slug: payrix-adjustments-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Aggregation Result Groups Holds data regarding a processed aggregation.
  name: Payrix Aggregation Result Groups API
  slug: payrix-aggregation-result-groups-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Aggregation Results Holds a field totals calculated when processing an aggregation.
  name: Payrix Aggregation Results API
  slug: payrix-aggregation-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Aggregations acts as a scheduler that contains the needed parameters to properly generate results containing the calculated totals and keep such records in the aggregation results resource.
  name: Payrix Aggregations API
  slug: payrix-aggregations-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Alert Actions deals with specific action that occurs following a triggered web alert.
  name: Payrix Alert Actions API
  slug: payrix-alert-actions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Alert Trigger deals with triggers associated with web alerts
  name: Payrix Alert Triggers API
  slug: payrix-alert-triggers-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Web alerts, also known as webhooks, are automated notifications sent from the API server when triggered by a specific action that occurs in your portfolio. You can configure the actions that trigger t
  name: Payrix Alerts API
  slug: payrix-alerts-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Interaction with the API requires authentication. For application integration and persistent authentication, an API key is required.
  name: Payrix API Keys API
  slug: payrix-api-keys-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: An Apple Domains resource represents the status of Apple Pay registration for a specific merchant and domain.
  name: Payrix Apple Domains API
  slug: payrix-apple-domains-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: An Apple Domains Mass Enablement resource represents the bulk registration of multiple merchants, each associated with a respective domain, to enable the Apple Pay service.
  name: Payrix Apple Domains Mass Enablement API
  slug: payrix-apple-domains-mass-enablement-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Assessments represents a record of fees charged by processors or other third-parties to Entities or Orgs. These can represent either charges that are levied on a one-off, regularly scheduled, or event
  name: Payrix Assessments API
  slug: payrix-assessments-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Tokens provide the means through which to safely and securely store payment methods (e.g. credit cards or bank accounts) for later use. A transaction may be initiated for a customer by providing the t
  name: Payrix Authentication Tokens API
  slug: payrix-authentication-tokens-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Batches are a container for transactions that enables batch processing to the processor for a merchant (to settle customer sales). Processing transactions for settlement to the processor is done in ba
  name: Payrix Batches (Settlements) API
  slug: payrix-batches-settlements-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: The billing deals with billing configuration for an entity, org, division or partition. A billing configuration determines how an entity is billed for their payables within Payrix Pro.
  name: Payrix Billing API
  slug: payrix-billing-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A conditional logic that determines the events that will be billed and the configuration for each event.
  name: Payrix Billing Events API
  slug: payrix-billing-events-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Billing Modifiers means to change the total amount of the billing or whoever will pay it.
  name: Payrix Billing Modifiers API
  slug: payrix-billing-modifiers-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Bins Holds information about the issuer of a card. (Bank Issuer Number).
  name: Payrix Bins API
  slug: payrix-bins-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Change Requests Accounts Verification deals with payment account details for merchant boarding and entity funding. Ultimately, all the business performed within Payrix Pro (be it merchant transactions
  name: Payrix Change Requests API
  slug: payrix-change-requests-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Represents a file related to the Chargeback.
  name: Payrix Chargeback Documents API
  slug: payrix-chargeback-documents-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Chargeback Message Results represents a message that is received from the processor in relation to a Chargeback message.
  name: Payrix Chargeback Message Results API
  slug: payrix-chargeback-message-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resources that deal with chargebacks. A chargeback is a dispute of a purchase that has already been charged to an account that can result in a return of funds.
  name: Payrix Chargeback Messages API
  slug: payrix-chargeback-messages-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: The logged status changes of a Chargeback.
  name: Payrix Chargeback Statuses API
  slug: payrix-chargeback-statuses-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resources that deal with chargebacks. A chargeback is a dispute of a purchase that has already been charged to an account that can result in a return of funds.
  name: Payrix Chargebacks API
  slug: payrix-chargebacks-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: 'Represents a unique confirmation code issued to an email address, either when a user indicates that they have forgotten their password, or when the system needs to verify the email address associated '
  name: Payrix Confirmation Codes API
  slug: payrix-confirmation-codes-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A contact reflects a known, valid individual registered as a contact for the entity. It is purely informational and not a required record.
  name: Payrix Contacts API
  slug: payrix-contacts-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Represents an authorization that a given Entity has to connect to an integration to perform a particular action, such as send Transactions to the processor, or board a Merchant with the processor.
  name: Payrix Credentials API
  slug: payrix-credentials-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Customers deals with merchant customer information. Customers may be associated with tokens to create a stored method of payment or with invoices for billing.
  name: Payrix Customers API
  slug: payrix-customers-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A piece of conditional logic that makes a Verification Result change the application and the decision action in certain circumstance.
  name: Payrix Decision Actions API
  slug: payrix-decision-actions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A piece of conditional logic that makes a Decision apply only in certain circumstances.
  name: Payrix Decision Rules API
  slug: payrix-decision-rules-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Decisions deal with the schedule and rules for a check done on Transactions.
  name: Payrix Decisions API
  slug: payrix-decisions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A record of disbursement amount come from.
  name: Payrix Disbursement Entries API
  slug: payrix-disbursement-entries-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Disbursement Reference Represents a reference code issued by the Payout facilitator when a Disbursement is paid.
  name: Payrix Disbursement Reference API
  slug: payrix-disbursement-reference-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Disbursement Results Represents the results of a Disbursement and and any follow-ups actions (confirmations, returns, etc.).
  name: Payrix Disbursement Results API
  slug: payrix-disbursement-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A disbursement represents a movement of funds in an entity's payment account. Records of an occasion where money is either paid to a bank account or received from a bank account.
  name: Payrix Disbursements API
  slug: payrix-disbursements-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Divisions contains a list of user divisions associated with an account. It allows for an additional and optional layer of separation within a partition.
  name: Payrix Divisions API
  slug: payrix-divisions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Embedded Finance stores information related to the activation of the resource for an entity. EmbeddedFinance's Valued Added Service provides access to new products and services related to Embedded Fin
  name: Payrix Embedded Finance API
  slug: payrix-embedded-finance-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Entities are portion of a single facilitator, vendor or merchant. Common business-related details for each type of entity are stored here (like name and address) as well as management details (like wh
  name: Payrix Entities API
  slug: payrix-entities-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: the Entity Custom Fields feature, designed to empower partners to send identifiers and Risk-requested items using unlimited custom fields. By leveraging this feature, partners can ensure that their so
  name: Payrix Entities Custom Fields API
  slug: payrix-entitiescustomfields-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Entity Debts represents a record of a debt between entities or an entity and the System.
  name: Payrix Entity Debts API
  slug: payrix-entity-debts-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Entity Reserves Represents funds held by an Entity in reserve. The funds are held separately from amounts in any entity Funds.
  name: Payrix Entity Reserves API
  slug: payrix-entity-reserves-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Represents an ACH transaction or disbursement that has been rejected. The Entity Return will block ACH creations or send out related to its entity and payment.
  name: Payrix Entity Returns API
  slug: payrix-entity-returns-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: EntityTerms resource represent the different agreed terms and condition agreed to by merchants during the signup.
  name: Payrix Entity Terms API
  slug: payrix-entity-terms-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: An entityData record is used to store a signature image for an entity's acceptance of terms and conditions. This is stored in a separate table so as not to bloat the entities table with signature imag
  name: Payrix Entity Data API
  slug: payrix-entitydata-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: An entityRef may be used to store referential IDs for merchants, facilitators and even vendors. For a merchant, at least a mid and funding entityRef is required for proper transacting and funding. For
  name: Payrix Entity Refs API
  slug: payrix-entityrefs-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: An entry record represents a credit or debit of funds for an entity, possibly part of a transfer of funds between two entities. Any monetary change for an entity in Payrix Pro is recorded in an entry.
  name: Payrix Entries API
  slug: payrix-entries-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Entry Origin represents a record of sources for funded activity.
  name: Payrix Entry Origin API
  slug: payrix-entry-origin-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Fee Modifiers means to change the total amount of the fee or whoever will pay it.
  name: Payrix Fee Modifiers API
  slug: payrix-fee-modifiers-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Fee Refund is a way to reverse a fee that has been charged to another entity incorrectly.
  name: Payrix Fee Refunds API
  slug: payrix-fee-refunds-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A piece of conditional logic that makes a Fee apply only in certain circumstances.
  name: Payrix Fee Rules API
  slug: payrix-fee-rules-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: 'Fees are costs for specific timeframes elapsing, such as weekly, or monthly; or as actions taking place, such as a transaction authorization, Merchant onboarding, or chargeback management. These fees '
  name: Payrix Fees API
  slug: payrix-fees-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Monitor and control entity-level access to the FraudSight service, a comprehensive fraud prevention solution for card-present and card-not-present transactions. Track when entities are enabled or disa
  name: Payrix FraudSight Enablements API
  slug: payrix-fraudsight-enablements-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Query fraudSightResults to retrieve information about fraud detection results from the FraudSight service.
  name: Payrix FraudSight Results API
  slug: payrix-fraudsight-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: 'Each fundOrigin represents the sourced amounts of available funds, which are always traceable to a processor and merchant. This ensures accurate recording and compliance with funding rules. The table '
  name: Payrix Fund Origins API
  slug: payrix-fund-origins-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Funds deal with aggregate funding amount records. A funds record is a snapshot for funding activity, per entity and currency, and is used to determine available funds for an entity.
  name: Payrix Funds API
  slug: payrix-funds-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A host themes retrieves the active theme color associated with a specific host.
  name: Payrix Host Themes API
  slug: payrix-host-themes-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: 'Provides visibility into how a transaction''s interchange classification changes after settlement. Use this endpoint to track **post-settlement reclassifications**, including updates that may occur up '
  name: Payrix Interchange Histories API
  slug: payrix-interchange-histories-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A resource that stores line item details for an invoice.
  name: Payrix Invoice Items API
  slug: payrix-invoice-items-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A resource that relates an invoice item with an invoice. It holds information such as quantity, and price each item.
  name: Payrix Invoice Line Items API
  slug: payrix-invoice-line-items-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Invoice Parameters holds a certain configuration used for creating an invoice such as dba, address, API Key.
  name: Payrix Invoice Parameters API
  slug: payrix-invoice-parameters-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Invoice Results represents the result of an invoice processing. In other words, when the customer pays for an invoice it will then generate an invoice result.
  name: Payrix Invoice Results API
  slug: payrix-invoice-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Invoices deals with customer invoice details allowing for presenting charges to a customer and for payments to be made related to certain products or services.
  name: Payrix Invoices API
  slug: payrix-invoices-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: 'An iplist represents a whitelisted or blacklisted IP address or range. As an additional security measure, it may be useful for users to set specific, known IP addresses to be the only allowed IPs for '
  name: Payrix IP Address Lists API
  slug: payrix-ip-address-lists-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Logins resources deal with individual user details like name and email as well as management details like which partition and division the user belongs to.
  name: Payrix Logins API
  slug: payrix-logins-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: To view and manage utilities that assist with login-related actions such as password resets.
  name: Payrix Logins Helpers API
  slug: payrix-logins-helpers-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: 'Mappings enable the re-mapping of fields in the API for either in or out, using a set of JSON field mappings. For example, if your system uses a different format for out data that it will send to the '
  name: Payrix Mappings API
  slug: payrix-mappings-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A member represents a control or beneficiary member of the entity. At least one primary member record is required for merchant boarding.
  name: Payrix Members API
  slug: payrix-members-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Merchant Platform Statuses provides access to view the status of a merchant's onboarding process to Payrix Pro, including the activation of individual value-added services.
  name: Payrix Merchant Platform Statuses API
  slug: payrix-merchant-platform-statuses-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Result created after an oboarding attempt, it will contain important information related to the boarding and attempt.
  name: Payrix Merchant Results API
  slug: payrix-merchant-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Merchant details for transaction processing entities. Together with the entities table, this table defines a merchant. A merchant is primarily an entity that accepts payments and transacts with custom
  name: Payrix Merchants API
  slug: payrix-merchants-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Represents the sender, receiver, and subject of the Messages resources.
  name: Payrix Message Threads API
  slug: payrix-message-threads-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Represents a message within a Message Thread.
  name: Payrix Messages API
  slug: payrix-messages-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Note Documents represents a file that is related to a specific note record.
  name: Payrix Note Documents API
  slug: payrix-note-documents-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Notes handles risk management notes, reviews and releases for a Hold, Transaction and Entity specific data.
  name: Payrix Notes API
  slug: payrix-notes-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: OmniTokens stores information related to the activation of the resource for an entity. OmniToken's Valued Added Service helps protect transactions and reduce transaction risk.
  name: Payrix Omni Tokens API
  slug: payrix-omnitokens-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Opt Outs provides the ability to disable merchants or entities from participating in specific Value Added Services, such as FraudSight.
  name: Payrix Opt Outs API
  slug: payrix-opt-outs-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A record of an association between a particular Org and a particular Entity. You can associate Entities with an Org by creating Org Entity resources. One Org can contain and be associated with many En
  name: Payrix Org Entities API
  slug: payrix-org-entities-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Org Flow Actions means to add an Entity defined in the associated Org Flow to an Org, or remove an Entity identified in the same way from an Org.
  name: Payrix Org Flow Actions API
  slug: payrix-org-flow-actions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Org Flow Rules Provides access to manage workflows that add or remove merchants from a group based on specific criteria.
  name: Payrix Org Flow Rules API
  slug: payrix-org-flow-rules-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Org Flows represents a way to trigger the addition or removal of the Merchants associated with a Login to a particular Org.
  name: Payrix Org Flows API
  slug: payrix-org-flows-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resource that deals with records of all orgs. An org is an arbitrary grouping of entity records that can be attached to other resources as a unit for shared functionality.
  name: Payrix Orgs API
  slug: payrix-orgs-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: OrgsVASEfeProducts is a way to automatically enable an entity with the default parameters to embeddedFinance.
  name: Payrix Orgs VAS EfeProducts API
  slug: payrix-orgs-vas-efeproducts-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Orgs VAS fraudSightEnablements provides access to manage automatic enrollments for merchants within the specified group for the FraudSight fraud prevention Value Added Service.
  name: Payrix Orgs VAS fraudSightEnablements API
  slug: payrix-orgs-vas-fraudsightenablements-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Orgs VAS OmniTokens provides access to manage automatic enrollments for merchants within the specified group for the Omnitoken Value Added Service.
  name: Payrix Orgs VAS OmniTokens API
  slug: payrix-orgs-vas-omnitokens-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: 'Orgs VAS Pinless Debit Conversion is a new Value-Added Service (VAS) in the Payrix system. This feature is designed to generate additional revenue and will follow the same merchant enablement process '
  name: Payrix Orgs VAS PinlessDebitConversions API
  slug: payrix-orgs-vas-pinlessdebitconversions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: OrgsVasNetworkPaymentManager is a way to automatically enroll an entity associated with a specific org in the networkPaymentManager service.
  name: Payrix Orgs VAS RevenueBoosts API
  slug: payrix-orgs-vas-revenueboosts-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Orgs VAS SaferPayments provides access to manage automatic enrollments for merchants within the specified group for the Safer Payments Value Added Service.
  name: Payrix Orgs VAS SaferPayments API
  slug: payrix-orgs-vas-saferpayments-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Orgs VAS SaferPayments Non-compliance provides access to manage automatic enrollments for fees billing on non-compliant merchants within the specified group for the Safer Payments Value Added Service.
  name: Payrix Orgs VAS SaferPayments Non-compliance API
  slug: payrix-orgs-vas-saferpayments-non-compliance-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A collection of Payment Updates owned by the merchant's entity.
  name: Payrix Payment Update Groups API
  slug: payrix-payment-update-groups-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Payment Updates Holds information about the payment update - updating a payment method or account. The Payment Update will be related to a Payment, Subscription Token or Account, and owned by a Paymen
  name: Payrix Payment Updates API
  slug: payrix-payment-updates-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Payout Flows means to set up a Payouts resource automatically for an Entity or Org when it is boarded, or when a bank account is associated.
  name: Payrix Payout Flows API
  slug: payrix-payout-flows-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resource that tracks details that allow a Disbursement to be paid or debited.
  name: Payrix Payouts API
  slug: payrix-payouts-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Pending Entry represents a record of amounts moving in or out of the funds held by an Entity.
  name: Payrix Pending Entry API
  slug: payrix-pending-entry-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Pinless Debit Conversion is a new Value-Added Service (VAS) in the Payrix system. This feature is designed to generate additional revenue and will follow the same merchant enablement process as value-
  name: Payrix Pinless Debit Conversions API
  slug: payrix-pinless-debit-conversions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resource that represents a recurring type of payment that charges a certain amount on a weekly, monthly, quarterly, or annual basis.
  name: Payrix Plans API
  slug: payrix-plans-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Profit Share Results Holds a message regarding a failed Profit Share process.
  name: Payrix Profit Share Results API
  slug: payrix-profit-share-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A piece of conditional logic that makes a Profit Share apply only in certain circumstances.
  name: Payrix Profit Share Rules API
  slug: payrix-profit-share-rules-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Profit Shares means for an entity to have its earnings expenses shared with another entity.
  name: Payrix Profit Shares API
  slug: payrix-profit-shares-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Reserve Entry represents a record of funds moving in or out of reserve. It can be associated with either a Transaction, a Reserve, an Entity Reserve, or another Reserve Entry resource.
  name: Payrix Reserve Entry API
  slug: payrix-reserve-entry-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resources that deals with reserve activity. Reserving means to withhold funds from an entity by removing the ability to extract the funds from the control of the financial institution.
  name: Payrix Reserves API
  slug: payrix-reserves-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Rev Share Schedules table records the rules for income sharing, detailing who receives and who pays, along with the start and end dates of these rules. It also identifies the partners involved in reve
  name: Payrix Rev Share Schedules API
  slug: payrix-rev-share-schedules-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Rev Share Statements table stores the final calculated revenue share entries that are billed to partners. It applies the revenue sharing schedule to a month's worth of transactions, resulting in the a
  name: Payrix Rev Share Statements API
  slug: payrix-rev-share-statements-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: It captures the entities when they are enabled/disabled/re-enabled with networkPaymentManager
  name: Payrix Revenue Boosts API
  slug: payrix-revenue-boosts-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Safer Payments provides access to create, view, and update SaferPayments Value Added Service records.
  name: Payrix Safer Payments API
  slug: payrix-safer-payments-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Keys used to decrypt data or an indicator of which key to be used to decrypt data
  name: Payrix Secrets API
  slug: payrix-secrets-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resources that deals with secret (private) and public (publishable) user session keys for authentication in API interactions.
  name: Payrix Sessions API
  slug: payrix-sessions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Statement Entry represents a record of funds owed for a billing schedule.
  name: Payrix Statement Entry API
  slug: payrix-statement-entry-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resources for dealing with billing statements for entities. Statements are generated from billing configurations and represent the amount billed for a given period of time.
  name: Payrix Statements API
  slug: payrix-statements-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Represents an association between a Subscription and a means of payment (Token) for that Subscription.
  name: Payrix Subscription Tokens API
  slug: payrix-subscription-tokens-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resources that deal with customer subscriptions to a plan. Customers are subscribed to plans to allow for recurring payments to be made from that customer.
  name: Payrix Subscriptions API
  slug: payrix-subscriptions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Tax Form Requests provides access to create and view requests for tax documents, returning the PDF of the requested tax document.
  name: Payrix Tax Form Requests API
  slug: payrix-tax-form-requests-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Represents the link between a Login and a Team as well as the Login's rights on the Team. The Login resource identified in its login field is considered part of the Team.
  name: Payrix Team Logins API
  slug: payrix-team-logins-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A team is an arbitrary grouping of user records that may have access provisioned on each other and can be attached to other resources as a unit for shared functionality.
  name: Payrix Teams API
  slug: payrix-teams-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Terminal Transaction Reference represents a reference code issued by the Processor in relation to a particular Transaction.
  name: Payrix Terminal Transaction Reference API
  slug: payrix-terminal-transaction-reference-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Represents the result of a Transaction from a processor, which can be approved, declined, or raise an error.
  name: Payrix Terminal Transaction Results API
  slug: payrix-terminal-transaction-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Holds all of the information to a related final transaction and is used to reconcile with the actual, final transaction.
  name: Payrix Terminal Transactions API
  slug: payrix-terminal-transactions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: The terminal_txn_datas database table stores signature data for a terminal activation request. A terminalTxnData represents a signature image for a customer’s acceptance of terms and conditions for th
  name: Payrix Terminal Transactions Datas API
  slug: payrix-terminal-transactions-datas-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Terminal Transactions Metadatas Represents data from an EMV Transaction and/or returned by the credit card network associated with a Transaction.
  name: Payrix Terminal Transactions Metadatas API
  slug: payrix-terminal-transactions-metadatas-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resources for dealing with transaction that occur on physical terminals, such as a table or register.
  name: Payrix Terminals API
  slug: payrix-terminals-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Token Results represent events that occur during the transaction process, specifically related to the usage or creation of tokens. These events are derived from the processor's response and are crucia
  name: Payrix Token Results API
  slug: payrix-token-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Tokens provide the means through which to safely and securely store payment methods (e.g. credit cards or bank accounts) for later use.
  name: Payrix Tokens API
  slug: payrix-tokens-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Transactions Datas represents data associated with a Transaction - in particular, a Base64 encoded image of a signature captured at the time of entering the Transaction.
  name: Payrix Transaction Datas API
  slug: payrix-transaction-datas-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: A holds resource represents a reviewable action taken on a Transaction.
  name: Payrix Transaction Holds API
  slug: payrix-transaction-holds-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: An Item is a line item that is associated with a particular Transaction. It allows you to describe the cost, quantity and other details of each line in the Transaction.
  name: Payrix Transaction Items API
  slug: payrix-transaction-items-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Transaction Metadatas represents data from an EMV Transaction and/or returned by the credit card network associated with a Transaction.
  name: Payrix Transaction Metadatas API
  slug: payrix-transaction-metadatas-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Transactions Results represents the result of a Transaction from a processor. For example, the Transaction may be approved, declined, or raise an error.
  name: Payrix Transactions Results API
  slug: payrix-transactions-results-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Resources for dealing with information relating to a particular credit card transaction, including the merchant, token, subscription, customer and card information.
  name: Payrix Transactions (Txns) API
  slug: payrix-transactions-txns-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: The txnSessionKey is designed to securely handle transactions within Payrix Pro PayFields/PayFrame integrations. This key aims to prevent misuse by third parties, as it is hosted on the front-end side
  name: Payrix Txn Sessions API
  slug: payrix-txn-sessions-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: Value Added Services is a collection of additional services and features beyond the core payment processing functionality that provide additional value to the user.
  name: Payrix Value Added Services API
  slug: payrix-value-added-services-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: VAS EfeOffer Updates provides Access to view Embedded Finance offer updates for Referrers. It holds historic data on an offer through the offer life cycle.
  name: Payrix VAS EfeOffer Updates API
  slug: payrix-vas-efeoffer-updates-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: VAS EfeOffers provides Access to view Embedded Finance offers for Referrers and Merchants, including terms, eligibility and application details.
  name: Payrix VAS EfeOffers API
  slug: payrix-vas-efeoffers-api
- baseURL: https://api.payrix.com
  baseurl_source: declared
  description: 'Resources that deal with third-party entities (non-facilitators and non-merchants) that are involved with the merchant processing and provide a service (or set of services) to the merchant, for which '
  name: Payrix Vendors API
  slug: payrix-vendors-api
artifact_total: 201
asyncapis:
- description: ''
  name: Payrix Webhooks
  slug: payrix-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/rules/payrix-rules.yml
  title: ''
  type: Spectral
  url: rules/payrix-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/json-ld/payrix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/payrix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/vocabulary/payrix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/payrix-vocabulary.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/well-known/payrix-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payrix-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/well-known/payrix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/payrix-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/agentic-access/payrix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/payrix-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/rate-limits/payrix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/payrix-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/asyncapi/payrix-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/payrix-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/data-model/payrix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/payrix-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/components/payrix-components.yml
  title: ''
  type: Components
  url: components/payrix-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/changelog/payrix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/payrix-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/conventions/payrix-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/payrix-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/conventions/payrix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/payrix-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/sandbox/payrix-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/payrix-sandbox.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payrix.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/lifecycle/payrix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/payrix-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/errors/payrix-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/payrix-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/errors/payrix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/payrix-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/conformance/payrix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/payrix-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/overlays/payrix-merchant-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/payrix-merchant-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/llms/payrix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/payrix-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/packages/payrix-packages.yml
  title: ''
  type: SDKs
  url: packages/payrix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/packages/payrix-packages.yml
  title: ''
  type: Packages
  url: packages/payrix-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/authentication/payrix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/payrix-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/payrix/refs/heads/main/security/payrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payrix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.worldpay.com/apis/payrix
- group: docs
  title: ''
  type: Documentation
  url: https://resource.payrix.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.worldpay.com/api-specification/payrix/partner
- group: start
  title: ''
  type: GettingStarted
  url: https://resource.payrix.com/docs/get-started-with-payrix-pro
- group: operate
  title: ''
  type: Support
  url: https://resource.payrix.com/docs/partner-support-guide
- group: company
  title: ''
  type: Blog
  url: https://platforms.worldpay.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payrix
- group: operate
  title: ''
  type: ChangeLog
  url: https://resource.payrix.com/docs/release-notes
- group: start
  title: ''
  type: SignUp
  url: https://test-portal.payrix.com/signup/payrixsandbox
- group: start
  title: ''
  type: Login
  url: https://portal.payrix.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.worldpay.com/en/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.worldpay.com/policies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/worldpay-for-platforms/
created: '2026-09-20'
description: 'Payrix, now operating as Worldpay for Platforms, is an embedded payments provider for vertical SaaS platforms. Its Payrix Pro product is a white-label payment facilitation platform: a REST API and portal for merchant boarding and underwriting, card and eCheck transaction processing, tokenization, recurring billing, fees, disbursements and payouts, chargebacks, risk decisions, embedded finance and reporting, plus hosted PayFields and PayFrame checkout components and mobile/terminal SDKs. Payrix was acquired by FIS/Worldpay, and its API reference and OpenAPI specifications are now published on the Worldpay Developer Hub while api.payrix.com remains the production API host.'
image: https://platforms.worldpay.com/wp-content/uploads/2025/03/Website-Hero-Image-Option-2.png
json_schemas:
- name: accountVerificationsResponseResult
  property_count: 1
  slug: payrix-account-verifications-response-result
- name: accountsPostRequest
  property_count: 14
  slug: payrix-accounts-post-request
- name: accountsPutRequest
  property_count: 10
  slug: payrix-accounts-put-request
- name: accountsResponseResult
  property_count: 1
  slug: payrix-accounts-response-result
- name: adjustmentsResponseResult
  property_count: 1
  slug: payrix-adjustments-response-result
- name: aggregationResultsGroupsResponseResult
  property_count: 1
  slug: payrix-aggregation-results-groups-response-result
- name: aggregationResultsResponseResult
  property_count: 1
  slug: payrix-aggregation-results-response-result
- name: aggregationsPostRequest
  property_count: 22
  slug: payrix-aggregations-post-request
- name: aggregationsPutRequest
  property_count: 22
  slug: payrix-aggregations-put-request
- name: aggregationsResponseResult
  property_count: 1
  slug: payrix-aggregations-response-result
- name: alertActionsPostRequest
  property_count: 10
  slug: payrix-alert-actions-post-request
- name: alertActionsPutRequest
  property_count: 9
  slug: payrix-alert-actions-put-request
- name: alertActionsResponseResult
  property_count: 1
  slug: payrix-alert-actions-response-result
- name: alertTriggersPostRequest
  property_count: 7
  slug: payrix-alert-triggers-post-request
- name: alertTriggersPutRequest
  property_count: 7
  slug: payrix-alert-triggers-put-request
- name: alertTriggersResponseResult
  property_count: 1
  slug: payrix-alert-triggers-response-result
- name: alertsPostRequest
  property_count: 11
  slug: payrix-alerts-post-request
- name: alertsPutRequest
  property_count: 9
  slug: payrix-alerts-put-request
- name: alertsResponseResult
  property_count: 1
  slug: payrix-alerts-response-result
- name: apiKeysPostRequest
  property_count: 7
  slug: payrix-api-keys-post-request
- name: apiKeysPutRequest
  property_count: 5
  slug: payrix-api-keys-put-request
- name: apikeysResponseResult
  property_count: 1
  slug: payrix-apikeys-response-result
- name: appleDomainsMassEnablementCsvResponseResult
  property_count: 1
  slug: payrix-apple-domains-mass-enablement-csv-response-result
- name: appleDomainsMassEnablementForMerchantList
  property_count: 1
  slug: payrix-apple-domains-mass-enablement-for-merchant-list
- name: appleDomainsResponseResult
  property_count: 1
  slug: payrix-apple-domains-response-result
- name: applePayForMerchantListPostRequest
  property_count: 1
  slug: payrix-apple-pay-for-merchant-list-post-request
- name: assessmentsResponseResult
  property_count: 1
  slug: payrix-assessments-response-result
- name: authTokensPostRequest
  property_count: 5
  slug: payrix-auth-tokens-post-request
- name: authTokensPutRequest
  property_count: 3
  slug: payrix-auth-tokens-put-request
- name: authTokensResponseResult
  property_count: 1
  slug: payrix-auth-tokens-response-result
- name: batchesPostRequest
  property_count: 8
  slug: payrix-batches-post-request
- name: batchesPutRequest
  property_count: 6
  slug: payrix-batches-put-request
- name: batchesResponseResult
  property_count: 1
  slug: payrix-batches-response-result
- name: billingEventsPostRequest
  property_count: 6
  slug: payrix-billing-events-post-request
- name: billingEventsPutRequest
  property_count: 6
  slug: payrix-billing-events-put-request
- name: billingEventsResponseResult
  property_count: 1
  slug: payrix-billing-events-response-result
- name: billingModifiersPostRequest
  property_count: 8
  slug: payrix-billing-modifiers-post-request
- name: billingModifiersPutRequest
  property_count: 8
  slug: payrix-billing-modifiers-put-request
- name: billingModifiersResponseResult
  property_count: 1
  slug: payrix-billing-modifiers-response-result
- name: billingsPostRequest
  property_count: 20
  slug: payrix-billings-post-request
- name: billingsPutRequest
  property_count: 18
  slug: payrix-billings-put-request
- name: billingsResponseResult
  property_count: 1
  slug: payrix-billings-response-result
- name: binsResponseResult
  property_count: 1
  slug: payrix-bins-response-result
- name: changeRequestsResponseResult
  property_count: 1
  slug: payrix-change-requests-response-result
- name: chargebackDocumentsPostRequest
  property_count: 8
  slug: payrix-chargeback-documents-post-request
- name: chargebackDocumentsResponseResult
  property_count: 1
  slug: payrix-chargeback-documents-response-result
- name: chargebackMessagePostRequest
  property_count: 13
  slug: payrix-chargeback-message-post-request
- name: chargebackMessageResultsResponseResult
  property_count: 1
  slug: payrix-chargeback-message-results-response-result
- name: chargebackMessagesResponseResult
  property_count: 1
  slug: payrix-chargeback-messages-response-result
- name: chargebackStatusesResponseResult
  property_count: 1
  slug: payrix-chargeback-statuses-response-result
- name: chargebacksDocumentsPutRequest
  property_count: 7
  slug: payrix-chargebacks-documents-put-request
- name: chargebacksResponseResult
  property_count: 1
  slug: payrix-chargebacks-response-result
- name: confirmCodesPostRequest
  property_count: 6
  slug: payrix-confirm-codes-post-request
- name: confirmCodesResponseResult
  property_count: 1
  slug: payrix-confirm-codes-response-result
- name: contactsPostRequest
  property_count: 16
  slug: payrix-contacts-post-request
- name: contactsPutRequest
  property_count: 16
  slug: payrix-contacts-put-request
- name: contactsResponseResult
  property_count: 1
  slug: payrix-contacts-response-result
- name: credentialsPostRequest
  property_count: 12
  slug: payrix-credentials-post-request
- name: updateApplePayDomainPostRequest
  property_count: 1
  slug: payrix-update-apple-pay-domain-post-request
- name: updateApplePayDomainResponseResult
  property_count: 1
  slug: payrix-update-apple-pay-domain-response-result
jsonld:
- class_count: 120
  name: Payrix Context
  property_count: 362
  slug: payrix-context
layout: provider
modified: '2026-09-20'
name: Payrix
nav: Providers
network: true
overview: 'Payrix publishes 133 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Accounts Verifications API, Adjustments API, and 130 more. Tagged areas include Company, Payments, Embedded Payments, Payment Facilitation, and Merchant Onboarding.


  The Payrix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Payrix''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 33 more developer resources.'
plans:
- name: Payrix Plans Pricing
  plan_count: 0
  slug: payrix-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Payrix Rate Limits
  slug: payrix-rate-limits
rules:
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Payrix API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: payrix-rules
score:
  band: strong
  composite: 64.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 8.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 86.6
    developer_ergonomics: 73.2
    discoverability: 81.5
    operational_transparency: 65.8
  previous_composite: 64.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 133
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Payrix Authentication
  slug: payrix-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Payrix Domain Security
  slug: payrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payrix
tags:
- Company
- Payments
- Embedded Payments
- Payment Facilitation
- Merchant Onboarding
- Fintech
- Payouts
- Chargebacks
- Subscription
website: https://payrix.com/
---
