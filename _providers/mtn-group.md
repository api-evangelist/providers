---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 246
  human_in_the_loop: 14
  name: Mtn Group Agentic Access
  operation_count: 475
  slug: mtn-group-agentic-access
  summary_line: 475 operations · 246 acting · 14 human-in-the-loop
api_count: 119
apis:
- description: 'API to consume and process account management actions to perform account status changes to customers with a MoMo Advance account. ChangeLog: 03-March-23 - First version.'
  name: MTN Account Decisioning
  slug: account-decisioning
- description: 'TMF API Reference: TMF 678 - Customer bill Management Release: 19.5 - December 2019 The Customer Bill Management API allows to find and retrieve one or several customer bills (also called invoices) pr'
  name: MTN TMF Customer Bill Management - TMF678
  slug: tmf-customer-bill-management
- description: Api Documentation.
  name: MTN Loans
  slug: mtn-customer-loans-api-v1
- description: Api Documentation.
  name: MTN Subscriber Details
  slug: subscriber-details
- description: Api Documentation.
  name: MTN Subscriber Type
  slug: subscriber-type
- description: Api Documentation.
  name: MTN Provisioning
  slug: provisioning
- description: Api Documentation.
  name: MTN Unified Balance V1
  slug: unified-balance-v1
- description: 'TMF API Reference: TMF639 - Resource Inventory Release : 19.5 - December 2019 Resource Inventory API goal is to provide the ability to manage Resources. Operations Resource Inventory API performs the '
  name: MTN TMF Resource Inventory Management - TMF639
  slug: tmf-resourceinventorymanagement-tmf639
- description: 'TMF API Reference : TMF 699 - Sales This API provides interfaces for Sales Lead, Sales Opportunity, Sales Quote and the other management capabilities to support the sales activities to build relations'
  name: MTN Sales Lead
  slug: sales-management
- description: 'TMF API Reference: TMF640 - Service Activation and Configuration Version 4.0 Service Activation and Configuration API goal is to provide the ability to activate and configure Service. This API feature'
  name: MTN Service Activation and Configuration
  slug: service-activation-and-configuration
- description: 'TMF API Reference : TMF 641 - Service Ordering Management Version 4.1 TMF641 performs the following operations on service order resource : - Retrieval of a service order or a collection of service ord'
  name: MTN Service Ordering
  slug: service-ordering
- description: Authentication API.
  name: MTN BSS TT OAuth V1
  slug: bss-tt-oauth-v1
- description: The Balance Management API facilitates the management of Customer Account capabilitites. It provides a generic API any client or back-end can call to request a Topup function that allows a reseller to
  name: MTN Balance Management V1
  slug: balance-management-v1
- description: callmeback API will be used to post a request in AYO, when initiated by Users via different Applications like "portal", "IVR" etc.
  name: MTN Callmeback V1
  slug: callmeback-v1
- description: callmeback API will be used to post a request to Backend systems when initiated by Users via different Applications like "portal", "IVR" etc.
  name: MTN Callmeback V2
  slug: callmeback-v2
- description: This API Provides a capability to create and send communications, notifications, and instructions to Parties, Individuals, Organizations or Users.
  name: MTN RCS Communication
  slug: rcs-communication
- description: This is Swagger UI environment generated for the TMF Communication Management specification.
  name: MTN Communication Management V1
  slug: communication-management-v1
- description: This is Swagger UI environment generated for the TMF Communication Management specification.
  name: MTN TMF681 Communication Management
  slug: tmf681-communication-management
- description: A suite of apis for customer consent validation.
  name: MTN Consent Validation V1
  slug: ayo-preapproval
- description: The API provides a target system with data content to be pushed via a channel to a customer. Supported Actions 1. SendSms. **Supported OpCo's:** MTN Uganda, MTN Ghana, MTN SA.
  name: MTN Content Push
  slug: content-push
- description: To facilitate the capability for consumers to retrieve bill information at service level , account level or invoice level etc.
  name: MTN Customer Bill Management
  slug: mtn-customer-bill-management
- description: To register services and activate services content tokens.
  name: MTN Customer Billing Token V1
  slug: customer-billing-token-v1
- description: 'The Data Gifting API facilitates purchase of data product for Beneficiary subscriber(Customer) and charging shall be done from Charging system using Requesting subscriber(Sponsor) msisdn and SMS will '
  name: MTN Data Gifting
  slug: mtn-nigeria-data-gifting-v1
- description: The Data Share API facilitates data share between Data Share Agent(Data Sender) and Customer(Data Receiver) also provides a data analytics. It also provides functionality to manage provider and consum
  name: MTN Customer Datashare
  slug: mtn-nigeria-customer-datashare
- description: To retrieve and schedule delivery information for MTN Customers.
  name: MTN Customer Delivery Booking
  slug: customer-delivery-booking
- description: The Customer Identification API provides information about a customer and their historical usage events on voice, data, SMS, Roaming etc. Information can be retrieved by stating the date range for the
  name: MTN Customer Identification V1
  slug: customer-identification-v1
- description: The Customer KYC Consent API facilitates the consent from the customer while capturing and retrieval of Customer Information. This aggregator service provides comprehensive Know Your Customer (KYC) co
  name: MTN KYC Consent
  slug: kyc-consent
- description: 'An API to manage customer loyalty operations. Can also be used by 3rd-party partners (3PP) to get a customer''s loyalty products and rewards **04-Oct-21 ChangeID: 0000000000235** -Branched off from the'
  name: MTN Customer Loyalty Management
  slug: customer-loyalty-management
- description: An API to Create customers,create admin users,activate/deactivate,disable Sims.
  name: MTN Customer Management - COE
  slug: customer-management-coe-za-preprod
- description: To facilitate the capability for customer to create/validate/change Pin Information.
  name: MTN Customer Pin Management v2
  slug: customer-pin-management-v2
- description: API Documentation.
  name: MTN Customer Promotion
  slug: customer-promotion
- description: The API facilitates product survey with a MTN Customer.
  name: MTN Customer Survey
  slug: customer-survey
- description: API will enable MTN customers to transfer part of their active airtime or data to another MTN customer. This service excludes special data plans.
  name: MTN Customer Data Transfer(ng prod)
  slug: customer-data-transfer-ng-prod
- description: API will enable MTN customers to transfer part of their active airtime or data to another MTN customer. This service excludes special data plans.
  name: MTN Customer Data Transfer
  slug: mtn-customer-datatransfer
- description: The Device Swap API is designed to detect changes in the International Mobile Equipment Identity (IMEI) associated with a mobile subscriber's number (MSISDN) within a specific period, typically the la
  name: MTN Device Swap V1
  slug: device-swap-v1
- description: 'TMF API Reference: TMF720 - Digital Identity Management Digital Identity Management API goal is to provide the ability to manage a digital identity. This digital identity allows to identify an individ'
  name: MTN TMF 720 - Digital Identity Management
  slug: tmf-720-digital-identity-management
- description: TM Forum Open APIs (Apache 2.0) Party Management API Provides standardized mechanism for digital partner management such as creation, update, retrieval, deletion and notification of events. Partner is
  name: MTN Digital Partner Management
  slug: digital-partner-management
- description: TMF667 Document API describes the meta-data of a Document, such as the name, creationDate and lifecycle status. The (typically binary) body of this document (such as a Word.doc, PDF, Video clip, or Im
  name: MTN Document Management
  slug: document-managment
- description: This is Swagger UI environment generated for the TMF Document Management specification.
  name: MTN TMF Document Management - TMF667
  slug: tmf-document-management-tmf667
- description: The Event Management API provides a standardized client interface to the enterprise event management system.
  name: MTN TMF688 - Event Management
  slug: tmf688-event-management
- description: This API provides EEC Token Management.
  name: MTN EEC Token Management
  slug: eec-token-management
- description: List of services to integrate with insurance service provider to manage insurance policies and policy related information. It provides the ability for channel applications to request for quote, submit
  name: MTN Insurance
  slug: insurance
- description: This service provides comprehensive IoT device management capabilities for TMF908 operations including device information retrieval, device management operations, and lifecycle management. The service
  name: MTN IoT Device Management
  slug: iot-device-management
- description: Api Documentation.
  name: MTN HCM V1
  slug: hcm-v1
- description: Facility to query failed transactions.
  name: MTN LogBack V1
  slug: logback-v1
- description: The TMForum Loyalty API Specification as developed by Globetom.
  name: MTN TMF Loyalty Management - TMF658
  slug: tmf-loyalty-management-tmf658
- description: This API provides ability to check the capability of an MSISDN to receive RCS mesages.
  name: MTN RCS Capability
  slug: rcs-capability
- description: Provides a RESTful API to expose SMS capability.
  name: MTN Medallia SMS V2
  slug: medallia-sms-v2
- description: This service provides comprehensive mobile advertisement management capabilities for MTN operations including ad targeting, content delivery, campaign management, and performance analytics. The servic
  name: MTN Advertising V2
  slug: advertising-v2
- description: A brief description of the API. It can be multiple lines.
  name: MTN Advertising
  slug: mtn-advertising-api-v1
- description: The mobile info API provides network related data. Supported Operations 1. Get last SIM Swap date of an MSISDN. 2. Get last SIM Swap date indicator of a MSISDN **Supported OpCo's:** MTN Uganda, MTN Gh
  name: MTN Mobile Customer Information
  slug: mobile-customer-information
- description: To facilitate the capability for consumers to realize withdrawals via MADAPI. The callback (i.. Completed) will be handled via MADAPI's callback API.
  name: MTN MoMo Withdrawals V1
  slug: withdrawals-v1
- description: A suite of apis for customer validation.
  name: MTN MoMo Verification V1-ToBeDeleted
  slug: momo-verification
- description: The Accountholders API returns basic information of the Accountholder including MTN Mobile Money account status. i.e. ACTIVE, SUSPENDED, BLOCKED etc. It also support validation of a MoMo accountholder
  name: MTN AccountHolders V1
  slug: ayoaccountholderinfo
- description: An API to retrieve the profile of an MTN field agent. Please refer to the reference guides https://developers.mtn.com/getting-started and Response and Error Codes documents https://developers.mtn.com/
  name: MTN Agent Profile
  slug: agent-profile
- description: This API manages tasks for an MTN customer.
  name: MTN Customer Account Management V1
  slug: customer-account-management-v1
- description: MTN Customer KYC API allows clients to view the KYC (Know Your Customer) details of an MTN customer. The KYC API is a subset of the Customer Profile API.
  name: MTN KYC v1
  slug: mtn-customer-kyc-api-v1-product
- description: The Customer KYC(Know Your Client) Verification API will validate the 3PP Customer KYC information with MTN Customer KYC information.
  name: MTN Customer KYC Verification
  slug: customer-kyc-verification
- description: This API facilitate loan in advance for an MTN customer.
  name: MTN Loans v2
  slug: loans-v2
- description: An API to retrieve the Location details of an MTN customer. Please refer to the Response and Error Codes documents https://developers.mtn.com/insights/response-codes.
  name: MTN Locations
  slug: mtn-customer-locations-api-v1
- description: An API to register MoMo on Tier 0 for BSS. Please refer to the reference guides https://developers.mtn.com/API-Reference-Guides and Response and Error Codes documents https://developers.mtn.com/Respon
  name: MTN Customer Management
  slug: customer-management
- description: 'An API to retrieve the Plan details of an MTN customer and calculate aYo premiums. Can also be used by 3rd-party partners (3PP) for airtime recharge of a prepaid subscriber **24-June-21: ChangeID: c83'
  name: MTN Plans v2
  slug: mtn-customer-plans-api-v2
- description: An API to retrieve the profile of an MTN customer. Please refer to the reference guides https://developers.mtn.com/API-Reference-Guides and Response and Error Codes documents https://developers.mtn.co
  name: MTN Profiles V2
  slug: mtn-customer-profiles-api-v2-product
- description: This API assesses risks for an MTN customer as well as creates applications.
  name: MTN Risk Management
  slug: risk-management
- description: This API is used to determine the customer's score through an activities performed within a period of time.
  name: MTN Customer Score V1
  slug: mtn-customer-score
- description: 'This API is used to verify/validate SIM Swap status, SIM Activation status and SIM Recycle status of a customer''s msisdn. - **''/simSwap/verifyStatus''** capability is used to verify sim swap status as '
  name: MTN SIM Verification
  slug: simverification
- description: MTN Customer Subscription Management API — an MTN Group API product published on the MTN Developer Platform (MADAPI) with a downloadable machine-readable definition covering 6 path(s).
  name: MTN Subscriptions v2
  slug: mtn-subscription-api-v2
- description: API to provide capability to manage Offering specification of products.
  name: MTN G2M
  slug: g2m
- description: Generates an access token based on username and password.
  name: MTN OAuth V1
  slug: oauth-v1
- description: To enable merchants to manage purchases of subscribers.
  name: MTN Merchant Provisioning V1
  slug: merchant-provisioning-v1
- description: MTN SMS Messaging API allowing developers to include SMS messaging in their applications.
  name: MTN SMS
  slug: mtn-sms-api-v1
- description: Provides a RESTful API to expose USSD capability.
  name: MTN USSD interface
  slug: ussd
- description: A MTN API that controls the display of the catalog of Products available for a customer to purchase.
  name: MTN Product Offering v2
  slug: mtn-product-offering-api-v2
- description: A MTN API that controls the display of the catalog of Products available for a customer to purchase.
  name: MTN Product Offering v3
  slug: mtn-product-offering-api-v3
- description: An API to enable MTN retailers track their productivity KPI's over a period of time. Please refer to the reference guides https://developers.mtn.com/API-Reference-Guides and Response and Error Codes d
  name: MTN Retailer Productivity Tracking v1
  slug: mtn-ng-retailer-productivity-tracking-v1
- description: The Shopping Cart API provides a standardized mechanism for the management of shopping carts. Including creation, update, retrieval.
  name: MTN TMF633 - Shopping Cart Management
  slug: tmf633-shopping-cart-management
- description: This API assesses risks for an MTN customer as well as creates applications.
  name: MTN Siebel
  slug: siebel
- description: This service provides comprehensive party management capabilities for MTN customers including individual and organization management, credit information, and partner services. It serves as the aggrega
  name: MTN TMF Party Management - TMF632
  slug: tmf-party-management
- description: This service provides comprehensive usage management capabilities for MTN operations including data usage tracking, subscription management, balance inquiries, and usage analytics. The service integra
  name: MTN TMF Usage Management - TMF635
  slug: tmf-usage-management-tmf635
- description: This service provides comprehensive usage management capabilities for MTN operations including data usage tracking, subscription management, balance inquiries, and usage analytics. The service integra
  name: MTN Usage Management
  slug: usage-management
- description: Interface to the Apigee Cloud MTN-ID userinfo function.
  name: MTN MTNID-getInfo
  slug: mtnid-getinfo
- description: To facilitate notifications. Allows 3PPs to register and have notifications processed to them from the applicable backends.
  name: MTN Notification V1
  slug: notification-production
- description: To facilitate notifications. Allows 3PPs to register and have notifications processed to them from the applicable backends.
  name: MTN Notification v2
  slug: notification-v2
- description: This API provides ability to digital channel to purchase different offers and make payment through Netbanking or Card Payments.
  name: MTN Order Fulfillment
  slug: order-fulfillment
- description: '**TMF API Reference : TMF - 683 Party Interaction** **Release : 19.5 - Oct 2019** The Party Interaction Management API provides a mechanism to manage party interactions. Creation, update and retrieval'
  name: MTN TMF Party Interaction - TMF683
  slug: tmf-party-interaction-tmf683
- description: This API provides standardized mechanism for party management such as creation, update, retrieval and deletion of a party. Party can be an individual or an organization that has any kind of relation w
  name: MTN Party Management
  slug: mtn-party-management
- description: This API provides standardized mechanism for party management such as creation, update, retrieval and deletion of a party. Party can be an individual or an organization that has any kind of relation w
  name: MTN Rwanda Party Management
  slug: rwanda-party-management
- description: 'A suite of apis for customer payment method details and its data type. **07-July-21: ChangeID: 00000** - Updated the response body for the /paymentMethod endpoint **06-December-21:** - Added a new met'
  name: MTN Payment Methods V1
  slug: payment-methods-management-sa
- description: This is the Payment API for MADAPI. Handles payment use cases such as spTransfer, Debit request, Payment request, and related financial transactions. Provides comprehensive payment processing capabili
  name: MTN Payments V1
  slug: payments-v1
- description: This is a sample representation of the Prepay Balance Management TMForum API. It is important to bear in mind that swagger 2.0 does not properly support polymorphism, so the link between the payment m
  name: MTN TMF Prepay Balance Management - TMF654
  slug: tmf-prepay-balance-management-tmf654
- description: API to provide capability to manage catalog, category, Offerings, Offering price and specification of products.
  name: MTN Product Catalog - COE
  slug: product-catalog-coe
- description: API to provide capability to manage catalog, category, Offerings, Offering price and specification of products.
  name: MTN Product Catalog Management V1
  slug: product-catalog-management-v1
- description: API to provide capability to manage catalog, category, Offerings, Offering price and specification of products.
  name: MTN Product Catalogue Management
  slug: product-catalogue-management
- description: API to provide capability to manage catalog, category, Offerings, Offering price and specification of products.
  name: MTN TMF Product Catalog - TMF620
  slug: tmf-product-catalog-tmf620
- description: A Product Order is a type of order which can be used to place an order between a customer and a service provider or between a service provider and a partner and vice versa. Main Product Order attribut
  name: MTN Product Ordering - COE
  slug: product-ordering-coe
- description: A Product Order is a type of order which can be used to place an order between a customer and a service provider or between a service provider and a partner and vice versa. Main Product Order attribut
  name: MTN TMF Product Ordering - TMF622
  slug: tmf-product-ordering-tmf622
- description: API to provision,configure and activate Resource Functions.
  name: MTN Resource Configuration V1
  slug: resource-config-v1
- description: This is Swagger UI environment generated for the TMF Resource Ordering Management specification.
  name: MTN TMF Resource Ordering - TMF652
  slug: tmf-resource-ordering-tmf652
- description: Service Activation and Configuration API goal is to provide the ability to activate and configure Service. This API features Monitor pattern allowing to manage service configuration/activation asynchr
  name: MTN TMF Service Activation - TMF640
  slug: tmf-service-activation-tmf678
- description: An API to share an incident tickets between Remedy and ServiceNow.
  name: MTN Job Card Management
  slug: job-card-management
- description: An API to share an incident tickets between Remedy and ServiceNow.
  name: MTN Incident API
  slug: ticket
- description: Provides a RESTful API to expose SMS capability.
  name: MTN SMS V2
  slug: mtn-sms-interface
- description: Provides a Restful API to expose SMS capability for sending of messages , Mobile originating messages and Delivery Receipts.
  name: MTN SMS v3 API
  slug: sms-v3-api
- description: 'This API provides a comprehensive suite of services for managing SIM-related operations, including SIM swap initiation, status tracking, eligibility checks, and resource management. It ensures secure '
  name: MTN SIM Management V1
  slug: sim-management-staging
- description: The SIM Swap Verification API provides information about an MSISDN's sim-swap details. Supported Operations 1. Get last SIM Swap date of a phone Number.
  name: MTN SIM Swap Verification V1
  slug: sim-swap-verification-v1
- description: This API to be used to manage a Subscriber information.
  name: MTN Subscriber Management
  slug: subscriber-management
- description: This service provides comprehensive taxation management capabilities for MTN operations including tax calculation, validation, reporting, and compliance. It handles various taxation scenarios includin
  name: MTN Taxation V1
  slug: taxation-v1
- description: TMF621 Trouble Ticket Management Aggregator This service provides endpoint to fetch the ticket details with ticket id, create ticket, fetch list of tickets by customer id and update the existing ticke
  name: MTN TMF Trouble Ticket - TMF621
  slug: tmf-trouble-ticket-tmf621
- description: This is Swagger UI environment generated for the TMF Customer Management specification.
  name: MTN TMF629 - Customer Management
  slug: tmf629-customer-management
- description: '**TMF API Reference : TMF 637 - Product Inventory Management**.'
  name: MTN TMF637 Product Inventory
  slug: tmf637-product-inventory
- description: TMF666 Account Management API with MTN extensions to retrieve financial account transactions, transaction details, outstanding balances, account balances.
  name: MTN Account Management - COE
  slug: account-management-coe
- description: TMF676 Payment Management Aggregator API provides comprehensive payment management capabilities following TM Forum TMF676 standards. This service enables payment processing, payment method management,
  name: MTN TMF Payment Management - TMF676
  slug: tmf-payment-management-tmf676
- description: This API provides the option to reserver MSISDN for registration and also validate starter pack pairing.
  name: MTN TMF Resource Pool Management - TMF685
  slug: resource-pool-management
- description: API to fetch Airtime, Currency, Voice, Data and SMS balance details for a subscriber.
  name: MTN TMF Usage Consumption - TMF677
  slug: tmf-usage-consumption-tmf677
- description: API to fetch Airtime, Currency, Voice, Data and SMS balance details for a subscriber.
  name: MTN Usage Consumption V1
  slug: usage-consumption
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
artifact_total: 125
asyncapis:
- description: ''
  name: Mtn Group Webhooks
  slug: mtn-group-webhooks
common:
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
  name: mtn-group-mcp.yml
  slug: mtn-group-mcpyml
modified: '2026-07-25'
name: MTN Group
nav: Providers
network: true
overview: 'MTN Group publishes 115 APIs on the [APIs.io](https://apis.io/) network, including MTN Account Decisioning, MTN TMF Customer Bill Management - TMF678, MTN Loans, and 112 more. Tagged areas include Telecommunications, South Africa, Africa, Mobile Network Operator, and Network APIs.


  The MTN Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MTN Group''s developer surface includes authentication, documentation, API reference, signup flow, FAQ, support, YouTube channel, and 43 more developer resources.'
random_paper: 35
scopes:
- name: Mtn Group Scopes
  scope_count: 2
  slug: mtn-group-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 49.5
  delta: -1.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.0
    developer_ergonomics: 62.5
    discoverability: 68.5
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 13.0
      derived: 0
      marker_coverage: 0.0
      total: 115
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 66.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
