---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Navision Agentic Access
  operation_count: 109
  slug: navision-agentic-access
  summary_line: 109 operations · 50 acting
api_count: 40
apis:
- description: SOAP-based web services for legacy integrations and business logic operations in Dynamics NAV. Exposes pages and codeunits with built-in CRUD operations and supports extension codeunits for custom ope
  name: Dynamics NAV SOAP Web Services
  slug: dynamics-nav-soap-web-services
- description: RESTful web services layer for Business Central that provides the preferred integration method. Includes built-in APIs, custom API pages and queries, and supports both on-premises and cloud deployment
  name: Business Central REST API Web Services
  slug: business-central-rest-api-web-services
- description: Manage general ledger accounts
  name: Microsoft Dynamics NAV Accounts API
  slug: navision-accounts-api
- description: Manage installed applications
  name: Microsoft Dynamics NAV App Management API
  slug: navision-app-management-api
- description: Query available application versions and countries
  name: Microsoft Dynamics NAV Available Applications API
  slug: navision-available-applications-api
- description: Manage automation companies
  name: Microsoft Dynamics NAV Companies API
  slug: navision-companies-api
- description: Manage RapidStart configuration packages
  name: Microsoft Dynamics NAV Configuration Packages API
  slug: navision-configuration-packages-api
- description: Manage country and region codes
  name: Microsoft Dynamics NAV Countries/Regions API
  slug: navision-countries-regions-api
- description: Manage currencies and exchange rates
  name: Microsoft Dynamics NAV Currency API
  slug: navision-currency-api
- description: Manage customer payment journals
  name: Microsoft Dynamics NAV Customer Payments API
  slug: navision-customer-payments-api
- description: Manage customer records
  name: Microsoft Dynamics NAV Customers API
  slug: navision-customers-api
- description: Manage dimensions and dimension values
  name: Microsoft Dynamics NAV Dimensions API
  slug: navision-dimensions-api
- description: Manage employee records
  name: Microsoft Dynamics NAV Employees API
  slug: navision-employees-api
- description: View and track environment operations
  name: Microsoft Dynamics NAV Environment Operations API
  slug: navision-environment-operations-api
- description: Manage environment settings and configuration
  name: Microsoft Dynamics NAV Environment Settings API
  slug: navision-environment-settings-api
- description: Manage Business Central environments
  name: Microsoft Dynamics NAV Environments API
  slug: navision-environments-api
- description: Monitor extension installation progress
  name: Microsoft Dynamics NAV Extension Deployment Status API
  slug: navision-extension-deployment-status-api
- description: Upload and install per-tenant extensions
  name: Microsoft Dynamics NAV Extension Upload API
  slug: navision-extension-upload-api
- description: Manage installed extensions
  name: Microsoft Dynamics NAV Extensions API
  slug: navision-extensions-api
- description: Manage feature flags
  name: Microsoft Dynamics NAV Features API
  slug: navision-features-api
- description: Manage item categories
  name: Microsoft Dynamics NAV Item Categories API
  slug: navision-item-categories-api
- description: Manage inventory items
  name: Microsoft Dynamics NAV Items API
  slug: navision-items-api
- description: Manage general journals and journal lines
  name: Microsoft Dynamics NAV Journals API
  slug: navision-journals-api
- description: Manage administrative notifications
  name: Microsoft Dynamics NAV Notifications API
  slug: navision-notifications-api
- description: Manage payment methods
  name: Microsoft Dynamics NAV Payment Methods API
  slug: navision-payment-methods-api
- description: Manage payment terms
  name: Microsoft Dynamics NAV Payment Terms API
  slug: navision-payment-terms-api
- description: Manage permission sets and user permissions
  name: Microsoft Dynamics NAV Permission Sets API
  slug: navision-permission-sets-api
- description: Manage user profiles
  name: Microsoft Dynamics NAV Profiles API
  slug: navision-profiles-api
- description: Manage purchase invoices and lines
  name: Microsoft Dynamics NAV Purchase Invoices API
  slug: navision-purchase-invoices-api
- description: Manage purchase orders and lines
  name: Microsoft Dynamics NAV Purchase Orders API
  slug: navision-purchase-orders-api
- description: Manage sales invoices and lines
  name: Microsoft Dynamics NAV Sales Invoices API
  slug: navision-sales-invoices-api
- description: Manage sales orders and lines
  name: Microsoft Dynamics NAV Sales Orders API
  slug: navision-sales-orders-api
- description: View scheduled background jobs
  name: Microsoft Dynamics NAV Scheduled Jobs API
  slug: navision-scheduled-jobs-api
- description: Manage security groups
  name: Microsoft Dynamics NAV Security Groups API
  slug: navision-security-groups-api
- description: View storage usage and quotas
  name: Microsoft Dynamics NAV Storage API
  slug: navision-storage-api
- description: Manage support settings
  name: Microsoft Dynamics NAV Support Settings API
  slug: navision-support-settings-api
- description: Manage environment updates
  name: Microsoft Dynamics NAV Update Management API
  slug: navision-update-management-api
- description: Manage Business Central users
  name: Microsoft Dynamics NAV Users API
  slug: navision-users-api
- description: Manage vendor payment journals
  name: Microsoft Dynamics NAV Vendor Payments API
  slug: navision-vendor-payments-api
- description: Manage vendor records
  name: Microsoft Dynamics NAV Vendors API
  slug: navision-vendors-api
arazzos:
- description: Create a general journal in a company and read back its line collection.
  name: Business Central Create a Journal and Read Its Lines
  slug: navision-create-journal-and-read-lines-workflow
- description: Resolve a vendor by number, draft a purchase invoice, and confirm it landed.
  name: Business Central Create a Purchase Invoice for a Vendor
  slug: navision-create-purchase-invoice-for-vendor-workflow
- description: Resolve a vendor by number, open a purchase order for them, and read its lines.
  name: Business Central Create a Purchase Order for a Vendor
  slug: navision-create-purchase-order-for-vendor-workflow
- description: Resolve a customer by number, draft a sales invoice, and verify it by id.
  name: Business Central Create a Sales Invoice for a Customer
  slug: navision-create-sales-invoice-for-customer-workflow
- description: Resolve a customer by number, open a sales order for them, and read its lines.
  name: Business Central Create a Sales Order for a Customer
  slug: navision-create-sales-order-for-customer-workflow
- description: Resolve the working company, create a customer, and confirm it persisted.
  name: Business Central Onboard a Customer
  slug: navision-onboard-customer-workflow
- description: Resolve the working company, create a vendor, and confirm it persisted.
  name: Business Central Onboard a Vendor
  slug: navision-onboard-vendor-workflow
- description: Find an item by number and update it if it exists, otherwise create it.
  name: Business Central Upsert an Item
  slug: navision-upsert-item-workflow
artifact_total: 502
collections:
- collection_type: postman
  name: Business Central Administration Center API
  slug: postman-admin-center-api
- collection_type: postman
  name: Business Central Automation API v2.0
  slug: postman-automation-api
- collection_type: postman
  name: Dynamics 365 Business Central API v2.0
  slug: postman-business-central-api-v2
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Business Central Administration Center API
  slug: open-admin-center-api
- collection_type: open
  name: Business Central Automation API v2.0
  slug: open-automation-api
- collection_type: open
  name: Dynamics 365 Business Central API v2.0
  slug: open-business-central-api-v2
- collection_type: open
  name: Business Central Administration Center Accounts API
  slug: open-navision-accounts-api
- collection_type: open
  name: Business Central Administration Center Accounts App Management API
  slug: open-navision-app-management-api
- collection_type: open
  name: Business Central Administration Center Accounts Available Applications API
  slug: open-navision-available-applications-api
- collection_type: open
  name: Business Central Administration Center Accounts Companies API
  slug: open-navision-companies-api
- collection_type: open
  name: Business Central Administration Center Accounts Configuration Packages API
  slug: open-navision-configuration-packages-api
- collection_type: open
  name: Business Central Administration Center Accounts Countries/Regions API
  slug: open-navision-countries-regions-api
- collection_type: open
  name: Business Central Administration Center Accounts Currency API
  slug: open-navision-currency-api
- collection_type: open
  name: Business Central Administration Center Accounts Customer Payments API
  slug: open-navision-customer-payments-api
- collection_type: open
  name: Business Central Administration Center Accounts Customers API
  slug: open-navision-customers-api
- collection_type: open
  name: Business Central Administration Center Accounts Dimensions API
  slug: open-navision-dimensions-api
- collection_type: open
  name: Business Central Administration Center Accounts Employees API
  slug: open-navision-employees-api
- collection_type: open
  name: Business Central Administration Center Accounts Environment Operations API
  slug: open-navision-environment-operations-api
- collection_type: open
  name: Business Central Administration Center Accounts Environment Settings API
  slug: open-navision-environment-settings-api
- collection_type: open
  name: Business Central Administration Center Accounts Environments API
  slug: open-navision-environments-api
- collection_type: open
  name: Business Central Administration Center Accounts Extension Deployment Status API
  slug: open-navision-extension-deployment-status-api
- collection_type: open
  name: Business Central Administration Center Accounts Extension Upload API
  slug: open-navision-extension-upload-api
- collection_type: open
  name: Business Central Administration Center Accounts Extensions API
  slug: open-navision-extensions-api
- collection_type: open
  name: Business Central Administration Center Accounts Features API
  slug: open-navision-features-api
- collection_type: open
  name: Business Central Administration Center Accounts Item Categories API
  slug: open-navision-item-categories-api
- collection_type: open
  name: Business Central Administration Center Accounts Items API
  slug: open-navision-items-api
- collection_type: open
  name: Business Central Administration Center Accounts Journals API
  slug: open-navision-journals-api
- collection_type: open
  name: Business Central Administration Center Accounts Notifications API
  slug: open-navision-notifications-api
- collection_type: open
  name: Business Central Administration Center Accounts Payment Methods API
  slug: open-navision-payment-methods-api
- collection_type: open
  name: Business Central Administration Center Accounts Payment Terms API
  slug: open-navision-payment-terms-api
- collection_type: open
  name: Business Central Administration Center Accounts Permission Sets API
  slug: open-navision-permission-sets-api
- collection_type: open
  name: Business Central Administration Center Accounts Profiles API
  slug: open-navision-profiles-api
- collection_type: open
  name: Business Central Administration Center Accounts Purchase Invoices API
  slug: open-navision-purchase-invoices-api
- collection_type: open
  name: Business Central Administration Center Accounts Purchase Orders API
  slug: open-navision-purchase-orders-api
- collection_type: open
  name: Business Central Administration Center Accounts Sales Invoices API
  slug: open-navision-sales-invoices-api
- collection_type: open
  name: Business Central Administration Center Accounts Sales Orders API
  slug: open-navision-sales-orders-api
- collection_type: open
  name: Business Central Administration Center Accounts Scheduled Jobs API
  slug: open-navision-scheduled-jobs-api
- collection_type: open
  name: Business Central Administration Center Accounts Security Groups API
  slug: open-navision-security-groups-api
- collection_type: open
  name: Business Central Administration Center Accounts Storage API
  slug: open-navision-storage-api
- collection_type: open
  name: Business Central Administration Center Accounts Support Settings API
  slug: open-navision-support-settings-api
- collection_type: open
  name: Business Central Administration Center Accounts Update Management API
  slug: open-navision-update-management-api
- collection_type: open
  name: Business Central Administration Center Accounts Users API
  slug: open-navision-users-api
- collection_type: open
  name: Business Central Administration Center Accounts Vendor Payments API
  slug: open-navision-vendor-payments-api
- collection_type: open
  name: Business Central Administration Center Accounts Vendors API
  slug: open-navision-vendors-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/christianbraeunlich/d365bc-api-postman/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/christianbraeunlich/d365bc-api-postman/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/navision-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/navision-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navision-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/navision-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/navision-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-dynamics-nav/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navision-create-journal-and-read-lines-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navision-create-purchase-invoice-for-vendor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navision-create-purchase-order-for-vendor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navision-create-sales-invoice-for-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navision-create-sales-order-for-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navision-onboard-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navision-onboard-vendor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navision-upsert-item-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-dynamics-navision
- group: start
  title: ''
  type: Portal
  url: https://dynamics.microsoft.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-get-started
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/users-credential-types
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/dynamics-365/blog/product/dynamics-365-business-central/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/overview
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/dynamics
- group: start
  title: ''
  type: Signup
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/trial-signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/dynamics-365/products/business-central/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en/dynamics-365/business-applications/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/BCApps
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/christianbraeunlich/d365bc-api-postman
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/dynamics-rate-limits
- group: build
  title: Laravel SDK
  type: SDKs
  url: https://github.com/niclas-timm/laravel-dynamics-365-business-central
- group: build
  title: Go REST Client
  type: SDKs
  url: https://github.com/AgoraIO/agora-rest-client-go
- group: build
  title: AL Language CLI
  type: CLI
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-command-line-tools
- group: docs
  title: Customer Schema
  type: JSONSchema
  url: json-schema/customer.json
- group: docs
  title: Vendor Schema
  type: JSONSchema
  url: json-schema/vendor.json
- group: docs
  title: Item Schema
  type: JSONSchema
  url: json-schema/item.json
- group: docs
  title: Sales Order Schema
  type: JSONSchema
  url: json-schema/sales-order.json
- group: docs
  title: Purchase Order Schema
  type: JSONSchema
  url: json-schema/purchase-order.json
- group: docs
  title: BC v2 Customer Schema
  type: JSONSchema
  url: json-schema/business-central-v2-customer-schema.json
- group: docs
  title: BC v2 Vendor Schema
  type: JSONSchema
  url: json-schema/business-central-v2-vendor-schema.json
- group: docs
  title: BC v2 Item Schema
  type: JSONSchema
  url: json-schema/business-central-v2-item-schema.json
- group: docs
  title: BC v2 Sales Order Schema
  type: JSONSchema
  url: json-schema/business-central-v2-sales-order-schema.json
- group: docs
  title: BC v2 Purchase Order Schema
  type: JSONSchema
  url: json-schema/business-central-v2-purchase-order-schema.json
- group: docs
  title: Admin Center Environment Schema
  type: JSONSchema
  url: json-schema/admin-center-environment-schema.json
- group: docs
  title: Admin Center Environment Operation Schema
  type: JSONSchema
  url: json-schema/admin-center-environment-operation-schema.json
- group: docs
  title: Automation Extension Schema
  type: JSONSchema
  url: json-schema/automation-extension-schema.json
- group: docs
  title: Automation User Schema
  type: JSONSchema
  url: json-schema/automation-user-schema.json
- group: docs
  title: Automation Company Schema
  type: JSONSchema
  url: json-schema/automation-automation-company-schema.json
- group: design
  title: JSON-LD Context
  type: JSONLD
  url: json-ld/context.jsonld
- group: design
  title: Business Central v2 JSON-LD Context
  type: JSONLD
  url: json-ld/business-central-v2-context.jsonld
- group: design
  title: Admin Center JSON-LD Context
  type: JSONLD
  url: json-ld/admin-center-context.jsonld
- group: design
  title: Automation JSON-LD Context
  type: JSONLD
  url: json-ld/automation-context.jsonld
- group: design
  title: Navision Vocabulary
  type: Vocabulary
  url: vocabulary/navision-vocabulary.yaml
- group: design
  title: Spectral Rules
  type: Rules
  url: rules/navision-spectral-rules.yml
created: '2024-01-20'
description: API collection for Microsoft Dynamics NAV (formerly Navision), an enterprise resource planning (ERP) solution for small and medium-sized businesses. Dynamics NAV has evolved into Dynamics 365 Business Central, which provides modern REST, OData, and SOAP web services for business data integration.
examples:
- key_count: 7
  name: Admin Center App Info Example
  slug: admin-center-app-info-example
- key_count: 4
  name: Admin Center App Install Request Example
  slug: admin-center-app-install-request-example
- key_count: 4
  name: Admin Center App Update Request Example
  slug: admin-center-app-update-request-example
- key_count: 2
  name: Admin Center Copy Environment Request Example
  slug: admin-center-copy-environment-request-example
- key_count: 4
  name: Admin Center Create Environment Request Example
  slug: admin-center-create-environment-request-example
- key_count: 18
  name: Admin Center Environment Example
  slug: admin-center-environment-example
- key_count: 13
  name: Admin Center Environment Operation Example
  slug: admin-center-environment-operation-example
- key_count: 3
  name: Admin Center Environment Settings Example
  slug: admin-center-environment-settings-example
- key_count: 5
  name: Admin Center Error Response Example
  slug: admin-center-error-response-example
- key_count: 3
  name: Admin Center Notification Recipient Example
  slug: admin-center-notification-recipient-example
- key_count: 2
  name: Admin Center Quotas Example
  slug: admin-center-quotas-example
- key_count: 6
  name: Admin Center Restore Environment Request Example
  slug: admin-center-restore-environment-request-example
- key_count: 3
  name: Admin Center Restore Period Example
  slug: admin-center-restore-period-example
- key_count: 7
  name: Admin Center Scheduled Upgrade Example
  slug: admin-center-scheduled-upgrade-example
- key_count: 4
  name: Admin Center Support Settings Example
  slug: admin-center-support-settings-example
- key_count: 2
  name: Admin Center Update Settings Example
  slug: admin-center-update-settings-example
- key_count: 4
  name: Admin Center Used Storage Example
  slug: admin-center-used-storage-example
- key_count: 3
  name: Automation Automation Company Create Example
  slug: automation-automation-company-create-example
- key_count: 5
  name: Automation Automation Company Example
  slug: automation-automation-company-example
- key_count: 2
  name: Automation Automation Company Update Example
  slug: automation-automation-company-update-example
- key_count: 4
  name: Automation Company Example
  slug: automation-company-example
- key_count: 12
  name: Automation Configuration Package Example
  slug: automation-configuration-package-example
- key_count: 1
  name: Automation Error Response Example
  slug: automation-error-response-example
- key_count: 7
  name: Automation Extension Deployment Status Example
  slug: automation-extension-deployment-status-example
- key_count: 10
  name: Automation Extension Example
  slug: automation-extension-example
- key_count: 2
  name: Automation Extension Upload Create Example
  slug: automation-extension-upload-create-example
- key_count: 4
  name: Automation Extension Upload Example
  slug: automation-extension-upload-example
- key_count: 5
  name: Automation Feature Example
  slug: automation-feature-example
- key_count: 6
  name: Automation Permission Set Example
  slug: automation-permission-set-example
- key_count: 6
  name: Automation Profile Example
  slug: automation-profile-example
- key_count: 7
  name: Automation Scheduled Job Example
  slug: automation-scheduled-job-example
- key_count: 4
  name: Automation Security Group Example
  slug: automation-security-group-example
- key_count: 5
  name: Automation User Example
  slug: automation-user-example
- key_count: 6
  name: Automation User Permission Example
  slug: automation-user-permission-example
- key_count: 2
  name: Automation User Update Example
  slug: automation-user-update-example
- key_count: 13
  name: Business Central V2 Account Example
  slug: business-central-v2-account-example
- key_count: 5
  name: Business Central V2 Company Example
  slug: business-central-v2-company-example
- key_count: 5
  name: Business Central V2 Country Region Example
  slug: business-central-v2-country-region-example
- key_count: 7
  name: Business Central V2 Currency Example
  slug: business-central-v2-currency-example
- key_count: 16
  name: Business Central V2 Customer Create Example
  slug: business-central-v2-customer-create-example
- key_count: 28
  name: Business Central V2 Customer Example
  slug: business-central-v2-customer-example
- key_count: 6
  name: Business Central V2 Customer Payment Journal Example
  slug: business-central-v2-customer-payment-journal-example
- key_count: 14
  name: Business Central V2 Customer Update Example
  slug: business-central-v2-customer-update-example
- key_count: 4
  name: Business Central V2 Dimension Example
  slug: business-central-v2-dimension-example
- key_count: 23
  name: Business Central V2 Employee Example
  slug: business-central-v2-employee-example
- key_count: 1
  name: Business Central V2 Error Response Example
  slug: business-central-v2-error-response-example
- key_count: 11
  name: Business Central V2 General Ledger Entry Example
  slug: business-central-v2-general-ledger-entry-example
- key_count: 4
  name: Business Central V2 Item Category Example
  slug: business-central-v2-item-category-example
- key_count: 10
  name: Business Central V2 Item Create Example
  slug: business-central-v2-item-create-example
- key_count: 23
  name: Business Central V2 Item Example
  slug: business-central-v2-item-example
- key_count: 9
  name: Business Central V2 Item Update Example
  slug: business-central-v2-item-update-example
- key_count: 3
  name: Business Central V2 Journal Create Example
  slug: business-central-v2-journal-create-example
- key_count: 7
  name: Business Central V2 Journal Example
  slug: business-central-v2-journal-example
- key_count: 17
  name: Business Central V2 Journal Line Example
  slug: business-central-v2-journal-line-example
- key_count: 4
  name: Business Central V2 Payment Method Example
  slug: business-central-v2-payment-method-example
- key_count: 8
  name: Business Central V2 Payment Term Example
  slug: business-central-v2-payment-term-example
- key_count: 5
  name: Business Central V2 Purchase Invoice Create Example
  slug: business-central-v2-purchase-invoice-create-example
- key_count: 15
  name: Business Central V2 Purchase Invoice Example
  slug: business-central-v2-purchase-invoice-example
- key_count: 6
  name: Business Central V2 Purchase Order Create Example
  slug: business-central-v2-purchase-order-create-example
- key_count: 35
  name: Business Central V2 Purchase Order Example
  slug: business-central-v2-purchase-order-example
- key_count: 27
  name: Business Central V2 Purchase Order Line Example
  slug: business-central-v2-purchase-order-line-example
- key_count: 6
  name: Business Central V2 Purchase Order Update Example
  slug: business-central-v2-purchase-order-update-example
- key_count: 6
  name: Business Central V2 Sales Invoice Create Example
  slug: business-central-v2-sales-invoice-create-example
- key_count: 16
  name: Business Central V2 Sales Invoice Example
  slug: business-central-v2-sales-invoice-example
- key_count: 7
  name: Business Central V2 Sales Order Create Example
  slug: business-central-v2-sales-order-create-example
- key_count: 38
  name: Business Central V2 Sales Order Example
  slug: business-central-v2-sales-order-example
- key_count: 30
  name: Business Central V2 Sales Order Line Example
  slug: business-central-v2-sales-order-line-example
- key_count: 7
  name: Business Central V2 Sales Order Update Example
  slug: business-central-v2-sales-order-update-example
- key_count: 15
  name: Business Central V2 Vendor Create Example
  slug: business-central-v2-vendor-create-example
- key_count: 22
  name: Business Central V2 Vendor Example
  slug: business-central-v2-vendor-example
- key_count: 6
  name: Business Central V2 Vendor Payment Journal Example
  slug: business-central-v2-vendor-payment-journal-example
- key_count: 12
  name: Business Central V2 Vendor Update Example
  slug: business-central-v2-vendor-update-example
- key_count: 6
  name: Navision Activatefeature Example
  slug: navision-activatefeature-example
- key_count: 6
  name: Navision Addnotificationrecipient Example
  slug: navision-addnotificationrecipient-example
- key_count: 6
  name: Navision Copyenvironment Example
  slug: navision-copyenvironment-example
- key_count: 6
  name: Navision Createautomationcompany Example
  slug: navision-createautomationcompany-example
- key_count: 6
  name: Navision Createconfigurationpackage Example
  slug: navision-createconfigurationpackage-example
- key_count: 6
  name: Navision Createcustomer Example
  slug: navision-createcustomer-example
- key_count: 6
  name: Navision Createenvironment Example
  slug: navision-createenvironment-example
- key_count: 6
  name: Navision Createextensionupload Example
  slug: navision-createextensionupload-example
- key_count: 6
  name: Navision Createitem Example
  slug: navision-createitem-example
- key_count: 6
  name: Navision Createjournal Example
  slug: navision-createjournal-example
- key_count: 6
  name: Navision Createpurchaseinvoice Example
  slug: navision-createpurchaseinvoice-example
- key_count: 6
  name: Navision Createpurchaseorder Example
  slug: navision-createpurchaseorder-example
- key_count: 6
  name: Navision Createsalesinvoice Example
  slug: navision-createsalesinvoice-example
- key_count: 6
  name: Navision Createsalesorder Example
  slug: navision-createsalesorder-example
- key_count: 6
  name: Navision Createuserpermission Example
  slug: navision-createuserpermission-example
- key_count: 6
  name: Navision Createvendor Example
  slug: navision-createvendor-example
- key_count: 6
  name: Navision Deleteenvironment Example
  slug: navision-deleteenvironment-example
- key_count: 6
  name: Navision Getaccount Example
  slug: navision-getaccount-example
- key_count: 6
  name: Navision Getallenvironmentsstorage Example
  slug: navision-getallenvironmentsstorage-example
- key_count: 6
  name: Navision Getautomationcompany Example
  slug: navision-getautomationcompany-example
- key_count: 6
  name: Navision Getavailablerestoreperiods Example
  slug: navision-getavailablerestoreperiods-example
- key_count: 6
  name: Navision Getcustomer Example
  slug: navision-getcustomer-example
- key_count: 6
  name: Navision Getenvironment Example
  slug: navision-getenvironment-example
- key_count: 6
  name: Navision Getenvironmentsettings Example
  slug: navision-getenvironmentsettings-example
- key_count: 6
  name: Navision Getenvironmentstorage Example
  slug: navision-getenvironmentstorage-example
- key_count: 6
  name: Navision Getitem Example
  slug: navision-getitem-example
- key_count: 6
  name: Navision Getpurchaseorder Example
  slug: navision-getpurchaseorder-example
- key_count: 6
  name: Navision Getquotas Example
  slug: navision-getquotas-example
- key_count: 6
  name: Navision Getsalesorder Example
  slug: navision-getsalesorder-example
- key_count: 6
  name: Navision Getscheduledupgrade Example
  slug: navision-getscheduledupgrade-example
- key_count: 6
  name: Navision Getsupportsettings Example
  slug: navision-getsupportsettings-example
- key_count: 6
  name: Navision Getuser Example
  slug: navision-getuser-example
- key_count: 6
  name: Navision Getvendor Example
  slug: navision-getvendor-example
- key_count: 6
  name: Navision Installapp Example
  slug: navision-installapp-example
- key_count: 6
  name: Navision Listaccounts Example
  slug: navision-listaccounts-example
- key_count: 6
  name: Navision Listallenvironmentoperations Example
  slug: navision-listallenvironmentoperations-example
- key_count: 6
  name: Navision Listallenvironments Example
  slug: navision-listallenvironments-example
- key_count: 6
  name: Navision Listautomationcompanies Example
  slug: navision-listautomationcompanies-example
- key_count: 6
  name: Navision Listavailablecountries Example
  slug: navision-listavailablecountries-example
- key_count: 6
  name: Navision Listavailableversions Example
  slug: navision-listavailableversions-example
- key_count: 6
  name: Navision Listcompanies Example
  slug: navision-listcompanies-example
- key_count: 6
  name: Navision Listconfigurationpackages Example
  slug: navision-listconfigurationpackages-example
- key_count: 6
  name: Navision Listcountriesregions Example
  slug: navision-listcountriesregions-example
- key_count: 6
  name: Navision Listcurrencies Example
  slug: navision-listcurrencies-example
- key_count: 6
  name: Navision Listcustomerpaymentjournals Example
  slug: navision-listcustomerpaymentjournals-example
- key_count: 6
  name: Navision Listcustomers Example
  slug: navision-listcustomers-example
- key_count: 6
  name: Navision Listdimensions Example
  slug: navision-listdimensions-example
- key_count: 6
  name: Navision Listemployees Example
  slug: navision-listemployees-example
- key_count: 6
  name: Navision Listenvironmentoperations Example
  slug: navision-listenvironmentoperations-example
- key_count: 6
  name: Navision Listenvironments Example
  slug: navision-listenvironments-example
- key_count: 6
  name: Navision Listextensiondeploymentstatuses Example
  slug: navision-listextensiondeploymentstatuses-example
- key_count: 6
  name: Navision Listextensions Example
  slug: navision-listextensions-example
- key_count: 6
  name: Navision Listfeatures Example
  slug: navision-listfeatures-example
- key_count: 6
  name: Navision Listgeneralledgerentries Example
  slug: navision-listgeneralledgerentries-example
- key_count: 6
  name: Navision Listinstalledapps Example
  slug: navision-listinstalledapps-example
- key_count: 6
  name: Navision Listitemcategories Example
  slug: navision-listitemcategories-example
- key_count: 6
  name: Navision Listitems Example
  slug: navision-listitems-example
- key_count: 6
  name: Navision Listjournallines Example
  slug: navision-listjournallines-example
- key_count: 6
  name: Navision Listjournals Example
  slug: navision-listjournals-example
- key_count: 6
  name: Navision Listnotificationrecipients Example
  slug: navision-listnotificationrecipients-example
- key_count: 6
  name: Navision Listpaymentmethods Example
  slug: navision-listpaymentmethods-example
- key_count: 6
  name: Navision Listpaymentterms Example
  slug: navision-listpaymentterms-example
- key_count: 6
  name: Navision Listpermissionsets Example
  slug: navision-listpermissionsets-example
- key_count: 6
  name: Navision Listprofiles Example
  slug: navision-listprofiles-example
- key_count: 6
  name: Navision Listpurchaseinvoices Example
  slug: navision-listpurchaseinvoices-example
- key_count: 6
  name: Navision Listpurchaseorderlines Example
  slug: navision-listpurchaseorderlines-example
- key_count: 6
  name: Navision Listpurchaseorders Example
  slug: navision-listpurchaseorders-example
- key_count: 6
  name: Navision Listsalesinvoices Example
  slug: navision-listsalesinvoices-example
- key_count: 6
  name: Navision Listsalesorderlines Example
  slug: navision-listsalesorderlines-example
- key_count: 6
  name: Navision Listsalesorders Example
  slug: navision-listsalesorders-example
- key_count: 6
  name: Navision Listscheduledjobs Example
  slug: navision-listscheduledjobs-example
- key_count: 6
  name: Navision Listsecuritygroups Example
  slug: navision-listsecuritygroups-example
- key_count: 6
  name: Navision Listuserpermissions Example
  slug: navision-listuserpermissions-example
- key_count: 6
  name: Navision Listusers Example
  slug: navision-listusers-example
- key_count: 6
  name: Navision Listvendorpaymentjournals Example
  slug: navision-listvendorpaymentjournals-example
- key_count: 6
  name: Navision Listvendors Example
  slug: navision-listvendors-example
- key_count: 6
  name: Navision Recoverenvironment Example
  slug: navision-recoverenvironment-example
- key_count: 6
  name: Navision Renameenvironment Example
  slug: navision-renameenvironment-example
- key_count: 6
  name: Navision Restoreenvironment Example
  slug: navision-restoreenvironment-example
- key_count: 6
  name: Navision Setappinsightskey Example
  slug: navision-setappinsightskey-example
- key_count: 6
  name: Navision Setupdatesettings Example
  slug: navision-setupdatesettings-example
- key_count: 6
  name: Navision Uninstallapp Example
  slug: navision-uninstallapp-example
- key_count: 6
  name: Navision Updateapp Example
  slug: navision-updateapp-example
- key_count: 6
  name: Navision Updateautomationcompany Example
  slug: navision-updateautomationcompany-example
- key_count: 6
  name: Navision Updatecustomer Example
  slug: navision-updatecustomer-example
- key_count: 6
  name: Navision Updateitem Example
  slug: navision-updateitem-example
- key_count: 6
  name: Navision Updatepurchaseorder Example
  slug: navision-updatepurchaseorder-example
- key_count: 6
  name: Navision Updatesalesorder Example
  slug: navision-updatesalesorder-example
- key_count: 6
  name: Navision Updateuser Example
  slug: navision-updateuser-example
- key_count: 6
  name: Navision Updatevendor Example
  slug: navision-updatevendor-example
- key_count: 6
  name: Navision Uploadconfigurationpackagefile Example
  slug: navision-uploadconfigurationpackagefile-example
- key_count: 6
  name: Navision Uploadextensionfile Example
  slug: navision-uploadextensionfile-example
features:
- description: General ledger, accounts payable/receivable, bank reconciliation, and financial reporting
  name: Financial Management
- description: Create and manage sales orders, invoices, credit memos, and quotes
  name: Sales Order Management
- description: Manage purchase orders, invoices, and vendor relationships
  name: Purchase Order Management
- description: Track items, stock levels, and inventory valuations
  name: Inventory Management
- description: Programmatic management of production and sandbox environments
  name: Environment Administration
- description: Automate company setup, extension management, and user provisioning
  name: Tenant Automation
finops:
- name: Navision Finops
  service_category: ERP
  slug: navision-finops
image: /assets/icons/navision.png
integrations:
- description: Deep integration with Excel, Outlook, and Teams for business workflows
  name: Microsoft 365
- description: Connect to Power BI, Power Automate, and Power Apps
  name: Power Platform
- description: Sync orders, customers, and inventory with Shopify stores
  name: Shopify
json_schemas:
- name: AppInfo
  property_count: 7
  slug: admin-center-app-info
- name: AppInstallRequest
  property_count: 4
  slug: admin-center-app-install-request
- name: AppUpdateRequest
  property_count: 4
  slug: admin-center-app-update-request
- name: CopyEnvironmentRequest
  property_count: 2
  slug: admin-center-copy-environment-request
- name: CreateEnvironmentRequest
  property_count: 4
  slug: admin-center-create-environment-request
- name: EnvironmentOperation
  property_count: 13
  slug: admin-center-environment-operation
- name: Environment
  property_count: 18
  slug: admin-center-environment
- name: EnvironmentSettings
  property_count: 3
  slug: admin-center-environment-settings
- name: ErrorResponse
  property_count: 5
  slug: admin-center-error-response
- name: NotificationRecipient
  property_count: 3
  slug: admin-center-notification-recipient
- name: Quotas
  property_count: 2
  slug: admin-center-quotas
- name: RestoreEnvironmentRequest
  property_count: 6
  slug: admin-center-restore-environment-request
- name: RestorePeriod
  property_count: 3
  slug: admin-center-restore-period
- name: ScheduledUpgrade
  property_count: 7
  slug: admin-center-scheduled-upgrade
- name: SupportSettings
  property_count: 4
  slug: admin-center-support-settings
- name: UpdateSettings
  property_count: 2
  slug: admin-center-update-settings
- name: UsedStorage
  property_count: 4
  slug: admin-center-used-storage
- name: AutomationCompanyCreate
  property_count: 3
  slug: automation-automation-company-create
- name: AutomationCompany
  property_count: 5
  slug: automation-automation-company
- name: AutomationCompanyUpdate
  property_count: 2
  slug: automation-automation-company-update
- name: Company
  property_count: 4
  slug: automation-company
- name: ConfigurationPackage
  property_count: 12
  slug: automation-configuration-package
- name: ErrorResponse
  property_count: 1
  slug: automation-error-response
- name: ExtensionDeploymentStatus
  property_count: 7
  slug: automation-extension-deployment-status
- name: Extension
  property_count: 10
  slug: automation-extension
- name: ExtensionUploadCreate
  property_count: 2
  slug: automation-extension-upload-create
- name: ExtensionUpload
  property_count: 4
  slug: automation-extension-upload
- name: Feature
  property_count: 5
  slug: automation-feature
- name: PermissionSet
  property_count: 6
  slug: automation-permission-set
- name: Profile
  property_count: 6
  slug: automation-profile
- name: ScheduledJob
  property_count: 7
  slug: automation-scheduled-job
- name: SecurityGroup
  property_count: 4
  slug: automation-security-group
- name: UserPermission
  property_count: 6
  slug: automation-user-permission
- name: User
  property_count: 5
  slug: automation-user
- name: UserUpdate
  property_count: 2
  slug: automation-user-update
- name: Account
  property_count: 13
  slug: business-central-v2-account
- name: Company
  property_count: 5
  slug: business-central-v2-company
- name: CountryRegion
  property_count: 5
  slug: business-central-v2-country-region
- name: Currency
  property_count: 7
  slug: business-central-v2-currency
- name: CustomerCreate
  property_count: 16
  slug: business-central-v2-customer-create
- name: CustomerPaymentJournal
  property_count: 6
  slug: business-central-v2-customer-payment-journal
- name: Customer
  property_count: 28
  slug: business-central-v2-customer
- name: CustomerUpdate
  property_count: 14
  slug: business-central-v2-customer-update
- name: Dimension
  property_count: 4
  slug: business-central-v2-dimension
- name: Employee
  property_count: 23
  slug: business-central-v2-employee
- name: ErrorResponse
  property_count: 1
  slug: business-central-v2-error-response
- name: GeneralLedgerEntry
  property_count: 11
  slug: business-central-v2-general-ledger-entry
- name: ItemCategory
  property_count: 4
  slug: business-central-v2-item-category
- name: ItemCreate
  property_count: 10
  slug: business-central-v2-item-create
- name: Item
  property_count: 23
  slug: business-central-v2-item
- name: ItemUpdate
  property_count: 9
  slug: business-central-v2-item-update
- name: JournalCreate
  property_count: 3
  slug: business-central-v2-journal-create
- name: JournalLine
  property_count: 17
  slug: business-central-v2-journal-line
- name: Journal
  property_count: 7
  slug: business-central-v2-journal
- name: PaymentMethod
  property_count: 4
  slug: business-central-v2-payment-method
- name: PaymentTerm
  property_count: 8
  slug: business-central-v2-payment-term
- name: PurchaseInvoiceCreate
  property_count: 5
  slug: business-central-v2-purchase-invoice-create
- name: PurchaseInvoice
  property_count: 15
  slug: business-central-v2-purchase-invoice
- name: PurchaseOrderCreate
  property_count: 6
  slug: business-central-v2-purchase-order-create
- name: PurchaseOrderLine
  property_count: 27
  slug: business-central-v2-purchase-order-line
- name: PurchaseOrder
  property_count: 35
  slug: business-central-v2-purchase-order
- name: PurchaseOrderUpdate
  property_count: 6
  slug: business-central-v2-purchase-order-update
- name: SalesInvoiceCreate
  property_count: 6
  slug: business-central-v2-sales-invoice-create
- name: SalesInvoice
  property_count: 16
  slug: business-central-v2-sales-invoice
- name: SalesOrderCreate
  property_count: 7
  slug: business-central-v2-sales-order-create
- name: SalesOrderLine
  property_count: 30
  slug: business-central-v2-sales-order-line
- name: SalesOrder
  property_count: 38
  slug: business-central-v2-sales-order
- name: SalesOrderUpdate
  property_count: 7
  slug: business-central-v2-sales-order-update
- name: VendorCreate
  property_count: 15
  slug: business-central-v2-vendor-create
- name: VendorPaymentJournal
  property_count: 6
  slug: business-central-v2-vendor-payment-journal
- name: Vendor
  property_count: 22
  slug: business-central-v2-vendor
- name: VendorUpdate
  property_count: 12
  slug: business-central-v2-vendor-update
- name: Customer
  property_count: 28
  slug: customer
- name: Item
  property_count: 23
  slug: item
- name: Account
  property_count: 13
  slug: navision-account
- name: AppInfo
  property_count: 7
  slug: navision-appinfo
- name: AppInstallRequest
  property_count: 4
  slug: navision-appinstallrequest
- name: AppUpdateRequest
  property_count: 4
  slug: navision-appupdaterequest
- name: AutomationCompany
  property_count: 5
  slug: navision-automationcompany
- name: AutomationCompanyCreate
  property_count: 3
  slug: navision-automationcompanycreate
- name: AutomationCompanyUpdate
  property_count: 2
  slug: navision-automationcompanyupdate
- name: Company
  property_count: 4
  slug: navision-company
- name: ConfigurationPackage
  property_count: 12
  slug: navision-configurationpackage
- name: CopyEnvironmentRequest
  property_count: 2
  slug: navision-copyenvironmentrequest
- name: CountryRegion
  property_count: 5
  slug: navision-countryregion
- name: CreateEnvironmentRequest
  property_count: 4
  slug: navision-createenvironmentrequest
- name: Currency
  property_count: 7
  slug: navision-currency
- name: Customer
  property_count: 28
  slug: navision-customer
- name: CustomerCreate
  property_count: 16
  slug: navision-customercreate
- name: CustomerPaymentJournal
  property_count: 6
  slug: navision-customerpaymentjournal
- name: CustomerUpdate
  property_count: 14
  slug: navision-customerupdate
- name: Dimension
  property_count: 4
  slug: navision-dimension
- name: Employee
  property_count: 23
  slug: navision-employee
- name: Environment
  property_count: 18
  slug: navision-environment
- name: EnvironmentOperation
  property_count: 13
  slug: navision-environmentoperation
- name: EnvironmentSettings
  property_count: 3
  slug: navision-environmentsettings
- name: ErrorResponse
  property_count: 5
  slug: navision-errorresponse
- name: Extension
  property_count: 10
  slug: navision-extension
- name: ExtensionDeploymentStatus
  property_count: 7
  slug: navision-extensiondeploymentstatus
- name: ExtensionUpload
  property_count: 4
  slug: navision-extensionupload
- name: ExtensionUploadCreate
  property_count: 2
  slug: navision-extensionuploadcreate
- name: Feature
  property_count: 5
  slug: navision-feature
- name: GeneralLedgerEntry
  property_count: 11
  slug: navision-generalledgerentry
- name: Item
  property_count: 23
  slug: navision-item
- name: ItemCategory
  property_count: 4
  slug: navision-itemcategory
- name: ItemCreate
  property_count: 10
  slug: navision-itemcreate
- name: ItemUpdate
  property_count: 9
  slug: navision-itemupdate
- name: Journal
  property_count: 7
  slug: navision-journal
- name: JournalCreate
  property_count: 3
  slug: navision-journalcreate
- name: JournalLine
  property_count: 17
  slug: navision-journalline
- name: NotificationRecipient
  property_count: 3
  slug: navision-notificationrecipient
- name: PaymentMethod
  property_count: 4
  slug: navision-paymentmethod
- name: PaymentTerm
  property_count: 8
  slug: navision-paymentterm
- name: PermissionSet
  property_count: 6
  slug: navision-permissionset
- name: Profile
  property_count: 6
  slug: navision-profile
- name: PurchaseInvoice
  property_count: 15
  slug: navision-purchaseinvoice
- name: PurchaseInvoiceCreate
  property_count: 5
  slug: navision-purchaseinvoicecreate
- name: PurchaseOrder
  property_count: 35
  slug: navision-purchaseorder
- name: PurchaseOrderCreate
  property_count: 6
  slug: navision-purchaseordercreate
- name: PurchaseOrderLine
  property_count: 27
  slug: navision-purchaseorderline
- name: PurchaseOrderUpdate
  property_count: 6
  slug: navision-purchaseorderupdate
- name: Quotas
  property_count: 2
  slug: navision-quotas
- name: RestoreEnvironmentRequest
  property_count: 6
  slug: navision-restoreenvironmentrequest
- name: RestorePeriod
  property_count: 3
  slug: navision-restoreperiod
- name: SalesInvoice
  property_count: 16
  slug: navision-salesinvoice
- name: SalesInvoiceCreate
  property_count: 6
  slug: navision-salesinvoicecreate
- name: SalesOrder
  property_count: 38
  slug: navision-salesorder
- name: SalesOrderCreate
  property_count: 7
  slug: navision-salesordercreate
- name: SalesOrderLine
  property_count: 30
  slug: navision-salesorderline
- name: SalesOrderUpdate
  property_count: 7
  slug: navision-salesorderupdate
- name: ScheduledJob
  property_count: 7
  slug: navision-scheduledjob
- name: ScheduledUpgrade
  property_count: 7
  slug: navision-scheduledupgrade
- name: SecurityGroup
  property_count: 4
  slug: navision-securitygroup
- name: SupportSettings
  property_count: 4
  slug: navision-supportsettings
- name: UpdateSettings
  property_count: 2
  slug: navision-updatesettings
- name: UsedStorage
  property_count: 4
  slug: navision-usedstorage
- name: User
  property_count: 5
  slug: navision-user
- name: UserPermission
  property_count: 6
  slug: navision-userpermission
- name: UserUpdate
  property_count: 2
  slug: navision-userupdate
- name: Vendor
  property_count: 22
  slug: navision-vendor
- name: VendorCreate
  property_count: 15
  slug: navision-vendorcreate
- name: VendorPaymentJournal
  property_count: 6
  slug: navision-vendorpaymentjournal
- name: VendorUpdate
  property_count: 12
  slug: navision-vendorupdate
- name: Purchase Order
  property_count: 35
  slug: purchase-order
- name: Sales Order
  property_count: 38
  slug: sales-order
- name: Vendor
  property_count: 22
  slug: vendor
json_structures:
- name: Admin Center App Info Structure
  property_count: 7
  slug: admin-center-app-info-structure
- name: Admin Center App Install Request Structure
  property_count: 4
  slug: admin-center-app-install-request-structure
- name: Admin Center App Update Request Structure
  property_count: 4
  slug: admin-center-app-update-request-structure
- name: Admin Center Copy Environment Request Structure
  property_count: 2
  slug: admin-center-copy-environment-request-structure
- name: Admin Center Create Environment Request Structure
  property_count: 4
  slug: admin-center-create-environment-request-structure
- name: Admin Center Environment Operation Structure
  property_count: 13
  slug: admin-center-environment-operation-structure
- name: Admin Center Environment Settings Structure
  property_count: 3
  slug: admin-center-environment-settings-structure
- name: Admin Center Environment Structure
  property_count: 18
  slug: admin-center-environment-structure
- name: Admin Center Error Response Structure
  property_count: 5
  slug: admin-center-error-response-structure
- name: Admin Center Notification Recipient Structure
  property_count: 3
  slug: admin-center-notification-recipient-structure
- name: Admin Center Quotas Structure
  property_count: 2
  slug: admin-center-quotas-structure
- name: Admin Center Restore Environment Request Structure
  property_count: 6
  slug: admin-center-restore-environment-request-structure
- name: Admin Center Restore Period Structure
  property_count: 3
  slug: admin-center-restore-period-structure
- name: Admin Center Scheduled Upgrade Structure
  property_count: 7
  slug: admin-center-scheduled-upgrade-structure
- name: Admin Center Support Settings Structure
  property_count: 4
  slug: admin-center-support-settings-structure
- name: Admin Center Update Settings Structure
  property_count: 2
  slug: admin-center-update-settings-structure
- name: Admin Center Used Storage Structure
  property_count: 4
  slug: admin-center-used-storage-structure
- name: Automation Automation Company Create Structure
  property_count: 3
  slug: automation-automation-company-create-structure
- name: Automation Automation Company Structure
  property_count: 5
  slug: automation-automation-company-structure
- name: Automation Automation Company Update Structure
  property_count: 2
  slug: automation-automation-company-update-structure
- name: Automation Company Structure
  property_count: 4
  slug: automation-company-structure
- name: Automation Configuration Package Structure
  property_count: 12
  slug: automation-configuration-package-structure
- name: Automation Error Response Structure
  property_count: 1
  slug: automation-error-response-structure
- name: Automation Extension Deployment Status Structure
  property_count: 7
  slug: automation-extension-deployment-status-structure
- name: Automation Extension Structure
  property_count: 10
  slug: automation-extension-structure
- name: Automation Extension Upload Create Structure
  property_count: 2
  slug: automation-extension-upload-create-structure
- name: Automation Extension Upload Structure
  property_count: 4
  slug: automation-extension-upload-structure
- name: Automation Feature Structure
  property_count: 5
  slug: automation-feature-structure
- name: Automation Permission Set Structure
  property_count: 6
  slug: automation-permission-set-structure
- name: Automation Profile Structure
  property_count: 6
  slug: automation-profile-structure
- name: Automation Scheduled Job Structure
  property_count: 7
  slug: automation-scheduled-job-structure
- name: Automation Security Group Structure
  property_count: 4
  slug: automation-security-group-structure
- name: Automation User Permission Structure
  property_count: 6
  slug: automation-user-permission-structure
- name: Automation User Structure
  property_count: 5
  slug: automation-user-structure
- name: Automation User Update Structure
  property_count: 2
  slug: automation-user-update-structure
- name: Business Central V2 Account Structure
  property_count: 13
  slug: business-central-v2-account-structure
- name: Business Central V2 Company Structure
  property_count: 5
  slug: business-central-v2-company-structure
- name: Business Central V2 Country Region Structure
  property_count: 5
  slug: business-central-v2-country-region-structure
- name: Business Central V2 Currency Structure
  property_count: 7
  slug: business-central-v2-currency-structure
- name: Business Central V2 Customer Create Structure
  property_count: 16
  slug: business-central-v2-customer-create-structure
- name: Business Central V2 Customer Payment Journal Structure
  property_count: 6
  slug: business-central-v2-customer-payment-journal-structure
- name: Business Central V2 Customer Structure
  property_count: 28
  slug: business-central-v2-customer-structure
- name: Business Central V2 Customer Update Structure
  property_count: 14
  slug: business-central-v2-customer-update-structure
- name: Business Central V2 Dimension Structure
  property_count: 4
  slug: business-central-v2-dimension-structure
- name: Business Central V2 Employee Structure
  property_count: 23
  slug: business-central-v2-employee-structure
- name: Business Central V2 Error Response Structure
  property_count: 1
  slug: business-central-v2-error-response-structure
- name: Business Central V2 General Ledger Entry Structure
  property_count: 11
  slug: business-central-v2-general-ledger-entry-structure
- name: Business Central V2 Item Category Structure
  property_count: 4
  slug: business-central-v2-item-category-structure
- name: Business Central V2 Item Create Structure
  property_count: 10
  slug: business-central-v2-item-create-structure
- name: Business Central V2 Item Structure
  property_count: 23
  slug: business-central-v2-item-structure
- name: Business Central V2 Item Update Structure
  property_count: 9
  slug: business-central-v2-item-update-structure
- name: Business Central V2 Journal Create Structure
  property_count: 3
  slug: business-central-v2-journal-create-structure
- name: Business Central V2 Journal Line Structure
  property_count: 17
  slug: business-central-v2-journal-line-structure
- name: Business Central V2 Journal Structure
  property_count: 7
  slug: business-central-v2-journal-structure
- name: Business Central V2 Payment Method Structure
  property_count: 4
  slug: business-central-v2-payment-method-structure
- name: Business Central V2 Payment Term Structure
  property_count: 8
  slug: business-central-v2-payment-term-structure
- name: Business Central V2 Purchase Invoice Create Structure
  property_count: 5
  slug: business-central-v2-purchase-invoice-create-structure
- name: Business Central V2 Purchase Invoice Structure
  property_count: 15
  slug: business-central-v2-purchase-invoice-structure
- name: Business Central V2 Purchase Order Create Structure
  property_count: 6
  slug: business-central-v2-purchase-order-create-structure
- name: Business Central V2 Purchase Order Line Structure
  property_count: 27
  slug: business-central-v2-purchase-order-line-structure
- name: Business Central V2 Purchase Order Structure
  property_count: 35
  slug: business-central-v2-purchase-order-structure
- name: Business Central V2 Purchase Order Update Structure
  property_count: 6
  slug: business-central-v2-purchase-order-update-structure
- name: Business Central V2 Sales Invoice Create Structure
  property_count: 6
  slug: business-central-v2-sales-invoice-create-structure
- name: Business Central V2 Sales Invoice Structure
  property_count: 16
  slug: business-central-v2-sales-invoice-structure
- name: Business Central V2 Sales Order Create Structure
  property_count: 7
  slug: business-central-v2-sales-order-create-structure
- name: Business Central V2 Sales Order Line Structure
  property_count: 30
  slug: business-central-v2-sales-order-line-structure
- name: Business Central V2 Sales Order Structure
  property_count: 38
  slug: business-central-v2-sales-order-structure
- name: Business Central V2 Sales Order Update Structure
  property_count: 7
  slug: business-central-v2-sales-order-update-structure
- name: Business Central V2 Vendor Create Structure
  property_count: 15
  slug: business-central-v2-vendor-create-structure
- name: Business Central V2 Vendor Payment Journal Structure
  property_count: 6
  slug: business-central-v2-vendor-payment-journal-structure
- name: Business Central V2 Vendor Structure
  property_count: 22
  slug: business-central-v2-vendor-structure
- name: Business Central V2 Vendor Update Structure
  property_count: 12
  slug: business-central-v2-vendor-update-structure
- name: Navision Structure
  property_count: 0
  slug: navision-structure
jsonld:
- class_count: 0
  name: Admin Center Context
  property_count: 0
  slug: admin-center-context
- class_count: 0
  name: Automation Context
  property_count: 0
  slug: automation-context
- class_count: 0
  name: Business Central V2 Context
  property_count: 0
  slug: business-central-v2-context
- class_count: 0
  name: context Context
  property_count: 9
  slug: context
layout: provider
modified: '2026-05-19'
name: Microsoft Dynamics NAV
nav: Providers
network: true
overview: 'Microsoft Dynamics NAV publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, App Management API, Available Applications API, and 35 more. Tagged areas include Business Management, Dynamics NAV, ERP, Finance, and Inventory.


  The Microsoft Dynamics NAV catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Microsoft Dynamics NAV''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, support, and 49 more developer resources.'
plans:
- name: Navision Plans Pricing
  plan_count: 5
  slug: navision-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 20
  name: Navision Rate Limits
  slug: navision-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Dynamics NAV API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: navision-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Microsoft Dynamics NAV API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 7
  slug: navision-spectral-rules
scopes:
- name: Navision Scopes
  scope_count: 1
  slug: navision-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: strong
  composite: 54.5
  delta: -9.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 25.0
    contract_quality: 68.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 38
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/navision/refs/heads/main/screenshots/navision-2026-06-20T190101.png
security:
- kind: authentication
  name: Navision Authentication
  slug: navision-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Navision Domain Security
  slug: navision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Navision Vulnerability Disclosure
  slug: navision-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: navision
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
use_cases:
- description: Connect external systems to Business Central for real-time business data sync
  name: ERP Integration
- description: Automate company creation and configuration across Business Central tenants
  name: Multi-Company Management
- description: Extract general ledger entries and account data for custom reporting
  name: Financial Reporting
website: https://dynamics.microsoft.com
---
