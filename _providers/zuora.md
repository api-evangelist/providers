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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 279
  human_in_the_loop: 1
  name: Zuora Agentic Access
  operation_count: 446
  slug: zuora-agentic-access
  summary_line: 446 operations · 279 acting · 1 human-in-the-loop
api_count: 80
apis:
- description: The Zuora v1 REST API provides complete coverage of Zuora Billing, Payments, and Platform features. It enables developers to automate billing operations, manage subscriptions, process payments, and in
  name: Zuora V1 API
  slug: v1-api
- description: Accounting Codes are commonly referred to as General Ledger Accounts or General Ledger Account Codes. In Zuora, the use of accounting codes are optional but recommended. This section contains the oper
  name: Zuora Accounting Codes API
  slug: zuora-accounting-codes-api
- description: A key step in configuring Finance is to create accounting periods in Zuora to match your company's financial calendar. This allows Zuora to produce reports and data exports organized by accounting per
  name: Zuora Accounting Periods API
  slug: zuora-accounting-periods-api
- description: Some operations in this section are similar to each other, but are provided for different use scenarios. You should choose the one that best suits your needs. For example, the [Create account](/v1-api
  name: Zuora Accounts API
  slug: zuora-accounts-api
- description: Actions are operations that are batch in nature. For example, the "create", "update", "delete", and other operations allow changes to up-to 50 objects at a time. The "query" operation will return up-t
  name: Zuora Actions API
  slug: zuora-actions-api
- description: The Aggregate Query API (AQuA) is a REST API that executes multiple <a href="https://knowledgecenter.zuora.com/Zuora_Central_Platform/Query/Export_ZOQL" target="_blank">Export ZOQL</a> or <a href="htt
  name: Zuora Aggregate Queries API
  slug: zuora-aggregate-queries-api
- description: 'Zuora System Health dashboard for API (API dashboard) collects and displays data about API usage, failure, performance, and concurrency limit in near real time. It enables you to view all the APIs in '
  name: Zuora API Health API
  slug: zuora-api-health-api
- description: Use attachments in Zuora to upload documents of various formats to associate additional information with accounts, subscriptions, invoices, credit memos, or debit memos. Example attachments could be p
  name: Zuora Attachments API
  slug: zuora-attachments-api
- description: Use the Bill Run call to create ad hoc bill runs and Post, Cancel, Query, and Delete bill runs. For more information about bill runs, see <a href="https://knowledgecenter.zuora.com/Billing/Billing_and
  name: Zuora Bill Run API
  slug: zuora-bill-run-api
- description: Zuora System Health dashboard for Bill Run (Bill Run dashboard) collects and displays data about bill run usage, failure, and performance in near real time. Through the Bill Run dashboard, you can vie
  name: Zuora Bill Run Health API
  slug: zuora-bill-run-health-api
- description: 'Billing documents include invoices, credit memos, and debit memos. **Note**: Credit memos and debit memos are only available if you have the <a href="https://knowledgecenter.zuora.com/Billing/Billing_'
  name: Zuora Billing Documents API
  slug: zuora-billing-documents-api
- description: 'A billing preview run asynchronously generates a downloadable CSV file containing a preview of future invoice item data and credit memo item data for a batch of customer accounts. **Note**: Credit mem'
  name: Zuora Billing Preview Run API
  slug: zuora-billing-preview-run-api
- description: The Zuora Billing product catalog is where you define your products and pricing. The product catalog's ability to handle sophisticated pricing models gives you the power to easily adapt your pricing t
  name: Zuora Catalog API
  slug: zuora-catalog-api
- description: A catalog group is used to group a list of product rate plans with a specific grade.
  name: Zuora Catalog Groups API
  slug: zuora-catalog-groups-api
- description: Configuration Templates in Zuora Deployment Manager enable you to configure your tenants in minutes by importing a templated metadata configuration file. This feature eliminates the need for long manu
  name: Zuora Configuration Templates API
  slug: zuora-configuration-templates-api
- description: Every time a contact is updated a snapshot is taken.
  name: Zuora Contact Snapshots API
  slug: zuora-contact-snapshots-api
- description: 'A contact defines the customer who holds an account or who is otherwise a person to contact about an account. An account requires a contact for the `BillToId` and `SoldToId` fields before the account '
  name: Zuora Contacts API
  slug: zuora-contacts-api
- description: Credit memos reduce invoice and account balances. By applying one or more credit memos to invoices with positive balances, you can reduce the invoice balances in the same way that applying a payment t
  name: Zuora Credit Memos API
  slug: zuora-credit-memos-api
- description: The Event Trigger service manages the business events and trigger conditions that are defined on [Zuora Business Object Model](http://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Busine
  name: Zuora Custom Event Triggers API
  slug: zuora-custom-event-triggers-api
- description: If you use a custom exchange rate provider and upload rates with the Import Foreign Exchange Rates mass action, you can query custom foreign exchange rates from Zuora through API. This feature is in *
  name: Zuora Custom Exchange Rates API
  slug: zuora-custom-exchange-rates-api
- description: 'With Custom Objects service, you can define custom objects, extending the Zuora data model to accommodate your specific use cases. If you use Postman, you can import the custom objects endpoints as a '
  name: Zuora Custom Object Definitions API
  slug: zuora-custom-object-definitions-api
- description: With Custom Objects service, you can submit a bulk job request to create, update, or delete custom object records in a batch. If you use Postman, you can import the custom objects endpoints as a colle
  name: Zuora Custom Object Jobs API
  slug: zuora-custom-object-jobs-api
- description: With Custom Objects service, you can create, update, delete and find custom object records. If you use Postman, you can import the custom objects endpoints as a collection into your Postman app and tr
  name: Zuora Custom Object Records API
  slug: zuora-custom-object-records-api
- description: Open Payment Method (OPM) service is a framework developed by Zuora, which allows you to integrate your custom payment method to Zuora subscription, billing, and revenue management in a dynamic and fl
  name: Zuora Custom Payment Method Types API
  slug: zuora-custom-payment-method-types-api
- description: A custom scheduled event notification is evaluated at the scheduled time of the related scheduled event on a daily basis. If the date meets the combination of the base field and the notification param
  name: Zuora Custom Scheduled Events API
  slug: zuora-custom-scheduled-events-api
- description: The Data Labeling APIs help you to label your existing data with organization(s) in Zuora. Once you turned on Multi Org feature, if you don't label your existing data, they are simply unlabeled, and u
  name: Zuora Data Labeling API
  slug: zuora-data-labeling-api
- description: The Data Query feature enables you to perform SQL queries in your Zuora tenant. To learn how to get started with Data Query, see [Overview of Data Query](https://knowledgecenter.zuora.com/DC_Developer
  name: Zuora Data Queries API
  slug: zuora-data-queries-api
- description: Debit memos increase the amount a customer owes. It is a separate document from the invoice. Debit memos can be used to correct undercharging on an invoice or to levy ad hoc charges outside the contex
  name: Zuora Debit Memos API
  slug: zuora-debit-memos-api
- description: Delivery Adjustments are used to handle end customer delivery complaints for the Delivery Pricing charge model. For more information, see <a href="https://knowledgecenter.zuora.com/Zuora_Billing/Bill_
  name: Zuora Delivery Adjustments API
  slug: zuora-delivery-adjustments-api
- description: 'You can use the [Describe an object](https://www.zuora.com/redocly-test/api-references/api/operation/GET_Describe/) operation to get a reference listing of each object that is available in your Zuora '
  name: Zuora Describe API
  slug: zuora-describe-api
- description: With the <a href="https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/E-Invoicing" target="_blank">E-Invoicing</a> feature, Zuora supports electronic invoices through an integration wi
  name: Zuora E-Invoicing API
  slug: zuora-e-invoicing-api
- description: 'Zuora System Health dashboard for Electronic Payments (Electronic Payment dashboard) collects and displays usage, failure, and performance data about electronic payments in near real time. It enables '
  name: Zuora Electronic Payments Health API
  slug: zuora-electronic-payments-health-api
- description: You can use the operations contained in this section to retrieve files such as export results, invoices, accounting period reports, and so on.
  name: Zuora Files API
  slug: zuora-files-api
- description: Fulfillments are subordinate objects attached to their related order line item. Fulfillment items are subordinate objects attached to their related fulfillment. For more information, see <a href="http
  name: Zuora Fulfillments API
  slug: zuora-fulfillments-api
- description: Hosted payment pages allow your customers to set up a payment method, such as providing a credit card. Since it only handles the payment method, it is suitable for a simple workflow or a complex multi
  name: Zuora Hosted Pages API
  slug: zuora-hosted-pages-api
- description: An import uploads content, especially when you have a large amount of content. The Import object contains all of the information you need to upload content, such as a large number of usage records.
  name: Zuora Imports API
  slug: zuora-imports-api
- description: Use invoice schedules to trigger invoice generation processes. For more information about invoice schedules, see <a href="https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Billing_Schedul
  name: Zuora Invoice Schedules API
  slug: zuora-invoice-schedules-api
- description: Invoices provides information about customers' accounts for invoices, for examples, dates, status, and amounts. For more information about invoices, see <a href="https://knowledgecenter.zuora.com/Bill
  name: Zuora Invoices API
  slug: zuora-invoices-api
- description: Use journal runs to automatically create summary journal entities that are suitable for importing into your general ledger system. For more information about journal runs, see <a href="https://knowled
  name: Zuora Journal Runs API
  slug: zuora-journal-runs-api
- description: Use mass updater to perform mass actions more easily. For more information about mass updater, see <a href="https://knowledgecenter.zuora.com/Billing/Finance/Mass_Updater" target="_blank">Mass Updater
  name: Zuora Mass Updater API
  slug: zuora-mass-updater-api
- description: Notifications are the actions taken to inform users or call third-party endpoints when a certain event happens. Typical actions include emails and callouts. Callouts typically refer to HTTP invocation
  name: Zuora Notifications API
  slug: zuora-notifications-api
- description: Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. You must first create an OAuth client in the Zuora UI before using the [Create an OAuth token](/api-references/api/opera
  name: Zuora OAuth API
  slug: zuora-oauth-api
- description: Use offers to define different product packages with multiple prices for all charge types across different geographic regions, sales areas, customers, or billing frequencies, for example. The Offer ob
  name: Zuora Offers API
  slug: zuora-offers-api
- description: Use operations to generate invoices and credit memos, collect payments for posted invoices, and generate previews of future invoice items for customer accounts.
  name: Zuora Operations API
  slug: zuora-operations-api
- description: You need to have the [Orders](https://knowledgecenter.zuora.com/Zuora_Billing/Subscriptions/Orders) or [Orders Harmonization](https://knowledgecenter.zuora.com/Zuora_Billing/Subscriptions/Orders/Order
  name: Zuora Order Actions API
  slug: zuora-order-actions-api
- description: Use order line item to launch non-subscription and unified monetization business models in Zuora, in addition to subscription business models. For more information about order line items, see <a href=
  name: Zuora Order Line Items API
  slug: zuora-order-line-items-api
- description: Orders are contractual agreements between merchants and customers. For more information about Orders, see <a href="https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders" target="_blank">Order
  name: Zuora Orders API
  slug: zuora-orders-api
- description: The Delayed Capture feature allows you to authorize the availability of funds for a transaction but delay the capture of funds until a later time. You can use the [Create authorization](/api-reference
  name: Zuora Payment Authorization API
  slug: zuora-payment-authorization-api
- description: Gateway reconciliation is the process of verifying that the electronic payment and refund transactions processed in Zuora match the transactions reported by the gateway. For example, if Zuora processe
  name: Zuora Payment Gateway Reconciliation API
  slug: zuora-payment-gateway-reconciliation-api
- description: Use payment gateways to pass authorization, payments, and settlement data securely to and from the merchant's website to the merchant's processor. For more information about payment gateways, see <a h
  name: Zuora Payment Gateways API
  slug: zuora-payment-gateways-api
- description: A Payment Method Snapshot is a copy of the particular Payment Method used in a transaction. If the Payment Method is deleted, the Snapshot continues to retain the data used in each of the past transac
  name: Zuora Payment Method Snapshots API
  slug: zuora-payment-method-snapshots-api
- description: 'The PaymentMethodTransactionLog object contains payment method transaction log data. You can use the [CRUD: Retrieve a payment method transaction log](https://www.zuora.com/redocly-test/api-references'
  name: Zuora Payment Method Transaction Logs API
  slug: zuora-payment-method-transaction-logs-api
- description: Zuora Payment Method Updater (PMU) enables merchants to automatically incorporate changes made to a customer's credit cards. For more information about Zuora PMU, see <a href="https://knowledgecenter.
  name: Zuora Payment Method Updater API
  slug: zuora-payment-method-updater-api
- description: Payment methods represents payment method details associated with a customer account.
  name: Zuora Payment Methods API
  slug: zuora-payment-methods-api
- description: Use payment runs to collect payments using electronic payment methods, for example, credit cards and ACH. For more information about payment runs, see <a href="https://knowledgecenter.zuora.com/Billin
  name: Zuora Payment Runs API
  slug: zuora-payment-runs-api
- description: Use payment schedules to split invoice or account balances into several installments and automatically process payments for the installments. For more information about payment schedules, see <a href=
  name: Zuora Payment Schedules API
  slug: zuora-payment-schedules-api
- description: Use payment transaction logs to export logs of all transactions from Zuora to the Gateway for Payments.
  name: Zuora Payment Transaction Logs API
  slug: zuora-payment-transaction-logs-api
- description: Use payments to process payments, for example, automate recurring payments, manage overpayments, and create refunds. For more information about payments, see <a href="https://knowledgecenter.zuora.com
  name: Zuora Payments API
  slug: zuora-payments-api
- description: The Prepaid with Drawdown feature is a pricing model for consumption-based services, such as data storage. Under this model, customers pay upfront to receive a number of units, usually for a period of
  name: Zuora Prepaid with Drawdown API
  slug: zuora-prepaid-with-drawdown-api
- description: Use price book items to define as many price points as needed for an individual product rate plan charge without the need of duplicating the product rate plan and rate plan charges in your catalog. Th
  name: Zuora Price Book Items API
  slug: zuora-price-book-items-api
- description: Use product charge definitions to define the attributes that can determine the charge behavior, such as billing attributes, pricing attributes, taxation attributes, or accounting attributes. The Produ
  name: Zuora Product Charge Definitions API
  slug: zuora-product-charge-definitions-api
- description: To manage product rate plan charge tiers, use the [Product Rate Plan Charges](/v1-api-reference/api/product-rate-plan-charges) operations instead to update the corresponding product rate plan charge w
  name: Zuora Product Rate Plan Charge Tiers API
  slug: zuora-product-rate-plan-charge-tiers-api
- description: A product rate plan charge represents a charge model or a set of fees associated with a product rate plan, which is the part of a product that your customers subscribe to. Each product rate plan can h
  name: Zuora Product Rate Plan Charges API
  slug: zuora-product-rate-plan-charges-api
- description: 'Use product rate plan definitions to reuse charges in different product rate plans. The Product Rate Plan Definition object is in the **Early Adopter** phase. We are actively soliciting feedback from '
  name: Zuora Product Rate Plan Definitions API
  slug: zuora-product-rate-plan-definitions-api
- description: A product rate plan is the part of a product that your customers subscribe to. Each product can have multiple product rate plans, and each product rate plan can have multiple product rate plan charges
  name: Zuora Product Rate Plans API
  slug: zuora-product-rate-plans-api
- description: A product is an item or service that your company sells. In the subscription economy, a product is generally a service that your customers subscribe to rather than a physical item that they purchase o
  name: Zuora Products API
  slug: zuora-products-api
- description: 'A Ramp is a time container to associate with rate plan charges in your subscription. Inside the Ramp, you can further define a set of Ramp Intervals (time-based periods) where products or pricing can '
  name: Zuora Ramps API
  slug: zuora-ramps-api
- description: A rate plan is part of a subscription or an amendment to a subscription, and it comes from a product rate plan. Like a product and its product rate plans, a subscription can have one or more rate plan
  name: Zuora Rate Plans API
  slug: zuora-rate-plans-api
- description: Zuora allows you to issue and track refunds on payments. Similar to external payments, users can enter external refunds to track refunds that have been performed outside of Zuora Payments (for example
  name: Zuora Refunds API
  slug: zuora-refunds-api
- description: If you are an <a href="https://knowledgecenter.zuora.com/Zuora_Billing/Enable_Order_to_Revenue" target="_blank">Order to Revenue</a> user, you can use the Regenerate operations to regenerate transacti
  name: Zuora Regenerate API
  slug: zuora-regenerate-api
- description: The REST API used in Payment Pages 2.0 are CORS (Cross-Origin Resource Sharing) enabled and therefore requires a digital signature. You can use the [Generate an RSA signature](https://www.zuora.com/re
  name: Zuora RSA Signatures API
  slug: zuora-rsa-signatures-api
- description: You can create billing document sequence sets through the REST API or the Zuora UI, allowing distinct numbering sequences for billing documents, payments, and refunds. To create a billing document seq
  name: Zuora Sequence Sets API
  slug: zuora-sequence-sets-api
- description: The Setting API provides a central API for managing settings in your Zuora tenant. If you use Postman, you can import the Settings API endpoints as a collection into your Postman app and try out diffe
  name: Zuora Settings API
  slug: zuora-settings-api
- description: A light-weight API to sign up customers and subscribe. You need to have the [Orders](https://knowledgecenter.zuora.com/Zuora_Billing/Subscriptions/Orders) or [Orders Harmonization](https://knowledgece
  name: Zuora Sign Up API
  slug: zuora-sign-up-api
- description: A subscription is a product or service that has recurring charges, such as a monthly flat fee or charges based on usage. Subscriptions can also include one-time charges, such as activation fees. Every
  name: Zuora Subscriptions API
  slug: zuora-subscriptions-api
- description: 'A summary journal entry is a summary of Zuora transaction amounts organized by accounting code and general ledger segments. A segment adds more reporting granularity through business dimensions, such '
  name: Zuora Summary Journal Entries API
  slug: zuora-summary-journal-entries-api
- description: The TaxationItem object is used to add a tax amount to an invoice item. In the typical use case, the tax amount that you specify in the object is calculated by <a href="https://knowledgecenter.zuora.c
  name: Zuora Taxation Items API
  slug: zuora-taxation-items-api
- description: Consumption of a billable service or resource (such as database storage space or bundles of emails sent) provides the basis for some charge models - simple usage, tiered pricing, or volume pricing. To
  name: Zuora Usage API
  slug: zuora-usage-api
- description: A workflow is a sequence of tasks that are performed based on predefined logic. A workflow improves efficiency and reduces errors by automating a series of complex tasks that otherwise need to be perf
  name: Zuora Workflows API
  slug: zuora-workflows-api
- description: '**Note:** You can only use the operations in this section if you have the Billing - Revenue Integration feature enabled. See <a href="https://knowledgecenter.zuora.com/Zuora_Revenue/Billing_-_Revenue_'
  name: Zuora Zuora Revenue Integration API
  slug: zuora-zuora-revenue-integration-api
artifact_total: 86
collections:
- collection_type: open
  name: API Reference
  slug: open-zuora-v1
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zuora-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zuora-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zuora
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zuora
- group: start
  title: ''
  type: Portal
  url: https://developer.zuora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zuora.com/
- group: company
  title: ''
  type: Website
  url: https://www.zuora.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.zuora.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.zuora.com/resources/blog/
created: '2025-02-17'
description: Zuora provides a subscription management and billing platform with REST APIs for automating billing, managing subscriptions, processing payments, and extending Zuora's capabilities. The platform offers v1 and Quickstart APIs with comprehensive coverage of billing, payments, and platform features.
finops:
- name: Zuora Finops
  service_category: API
  slug: zuora-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zuora.png
layout: provider
modified: '2026-05-19'
name: Zuora
nav: Providers
network: true
overview: 'Zuora publishes 79 APIs on the [APIs.io](https://apis.io/) network, including Accounting Codes API, Accounting Periods API, Accounts API, and 76 more. Tagged areas include Billing, Finance, Payments, and Subscriptions.


  Zuora''s developer surface includes developer portal, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Zuora Plans Pricing
  plan_count: 3
  slug: zuora-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Zuora Rate Limits
  slug: zuora-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 19.6
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 79
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zuora/refs/heads/main/screenshots/zuora-2026-06-20T202000.png
security:
- kind: domain-security
  name: Zuora Domain Security
  slug: zuora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zuora
tags:
- Billing
- Finance
- Payments
- Subscriptions
website: https://www.zuora.com/
---
