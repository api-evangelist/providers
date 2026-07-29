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
- acting_count: 10
  human_in_the_loop: 0
  name: Red Hat 3Scale Agentic Access
  operation_count: 32
  slug: red-hat-3scale-agentic-access
  summary_line: 32 operations · 10 acting
api_count: 15
apis:
- description: 3scale Webhooks allow API providers to receive real-time HTTP callbacks about account, application, user, and plan events within the 3scale platform. Webhooks can be configured to trigger external sys
  name: Red Hat 3scale Webhooks
  slug: webhooks-api
- description: The 3scale Toolbox is a command-line interface for automating 3scale configuration tasks. It wraps the 3scale Admin REST API to support copying APIs between tenants, promoting configurations between s
  name: Red Hat 3scale Toolbox CLI
  slug: toolbox-cli
- description: Manage developer accounts in the 3scale developer portal
  name: Red Hat 3scale Accounts API
  slug: red-hat-3scale-accounts-api
- description: Manage applications and their API keys and credentials
  name: Red Hat 3scale Applications API
  slug: red-hat-3scale-applications-api
- description: Authorize API calls and check access permissions
  name: Red Hat 3scale Authorization API
  slug: red-hat-3scale-authorization-api
- description: Retrieve and update APIcast gateway configuration
  name: Red Hat 3scale Configuration API
  slug: red-hat-3scale-configuration-api
- description: Inspect and manage DNS cache state
  name: Red Hat 3scale DNS API
  slug: red-hat-3scale-dns-api
- description: Health check and liveness/readiness probes
  name: Red Hat 3scale Health API
  slug: red-hat-3scale-health-api
- description: Bootstrap and initialization endpoints
  name: Red Hat 3scale Initialization API
  slug: red-hat-3scale-initialization-api
- description: Manage billing invoices for developer accounts
  name: Red Hat 3scale Invoices API
  slug: red-hat-3scale-invoices-api
- description: OAuth 2.0 token authorization endpoints
  name: Red Hat 3scale OAuth API
  slug: red-hat-3scale-oauth-api
- description: View payment transactions associated with invoices
  name: Red Hat 3scale Payment Transactions API
  slug: red-hat-3scale-payment-transactions-api
- description: Manage application plans and their features and limits
  name: Red Hat 3scale Plans API
  slug: red-hat-3scale-plans-api
- description: Report API usage back to 3scale for analytics and rate limiting
  name: Red Hat 3scale Reporting API
  slug: red-hat-3scale-reporting-api
- description: Manage API services and their settings
  name: Red Hat 3scale Services API
  slug: red-hat-3scale-services-api
artifact_total: 80
collections:
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts API
  slug: postman-red-hat-3scale-accounts-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Applications API
  slug: postman-red-hat-3scale-applications-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Authorization API
  slug: postman-red-hat-3scale-authorization-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Configuration API
  slug: postman-red-hat-3scale-configuration-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts DNS API
  slug: postman-red-hat-3scale-dns-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Health API
  slug: postman-red-hat-3scale-health-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Initialization API
  slug: postman-red-hat-3scale-initialization-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Invoices API
  slug: postman-red-hat-3scale-invoices-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts OAuth API
  slug: postman-red-hat-3scale-oauth-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Payment Transactions API
  slug: postman-red-hat-3scale-payment-transactions-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Plans API
  slug: postman-red-hat-3scale-plans-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Reporting API
  slug: postman-red-hat-3scale-reporting-api
- collection_type: postman
  name: Red Hat 3scale Account Management Accounts Services API
  slug: postman-red-hat-3scale-services-api
- collection_type: open
  name: Red Hat 3scale Account Management API
  slug: open-red-hat-3scale-account-management
- collection_type: open
  name: Red Hat 3scale Analytics API
  slug: open-red-hat-3scale-analytics
- collection_type: open
  name: Red Hat 3scale APIcast Management API
  slug: open-red-hat-3scale-apicast-management
- collection_type: open
  name: Red Hat 3scale Billing API
  slug: open-red-hat-3scale-billing
- collection_type: open
  name: Red Hat 3scale Service Management API
  slug: open-red-hat-3scale-service-management
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/red-hat-3scale/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/red-hat-3scale-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-hat-3scale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red-hat-3scale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/red-hat-3scale-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/3scale
- group: company
  title: ''
  type: Website
  url: https://www.redhat.com/en/technologies/jboss-middleware/3scale
- group: docs
  title: ''
  type: Documentation
  url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management
- group: start
  title: ''
  type: GettingStarted
  url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/getting_started/index
- group: start
  title: ''
  type: Portal
  url: https://access.redhat.com/products/red-hat-3scale-api-management
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/3scale
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/3scale/APIcast
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/3scale/porta
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/3scale/3scale_toolbox
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/blog/channel/red-hat-middleware
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redhat.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/release_notes/index
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red-hat-3scale-service-management-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red-hat-3scale-account-management-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red-hat-3scale-analytics-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red-hat-3scale-billing-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red-hat-3scale-apicast-management-openapi.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/red-hat-3scale-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-3scale-account-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-3scale-application-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/red-hat-3scale-account-structure.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/red-hat-3scale-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/red-hat-3scale-vocabulary.yml
created: '2026-03-16'
description: Red Hat 3scale API Management is an enterprise-grade API management platform that enables organizations to share, secure, distribute, control, and monetize APIs across internal and external teams. It provides a developer portal, analytics, access control, policy enforcement, and billing for REST, SOAP, GraphQL, and other API types. 3scale runs on-premises via OpenShift or as a hosted managed service, and is fully Kubernetes-native.
examples:
- key_count: 2
  name: Red Hat 3Scale Authorize Transaction Example
  slug: red-hat-3scale-authorize-transaction-example
- key_count: 2
  name: Red Hat 3Scale Create Account Example
  slug: red-hat-3scale-create-account-example
- key_count: 2
  name: Red Hat 3Scale List Applications Example
  slug: red-hat-3scale-list-applications-example
finops:
- name: Red Hat 3Scale Finops
  service_category: API Management
  slug: red-hat-3scale-finops
graphqls:
- description: ''
  name: Red Hat 3scale GraphQL API
  slug: red-hat-3scale-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/red-hat-3scale.png
json_schemas:
- name: Red Hat 3scale Account
  property_count: 6
  slug: red-hat-3scale-account
- name: AccountList
  property_count: 1
  slug: red-hat-3scale-accountlist
- name: Red Hat 3scale Application
  property_count: 9
  slug: red-hat-3scale-application
- name: ApplicationList
  property_count: 1
  slug: red-hat-3scale-applicationlist
- name: ApplicationPlan
  property_count: 7
  slug: red-hat-3scale-applicationplan
- name: ApplicationPlanList
  property_count: 1
  slug: red-hat-3scale-applicationplanlist
- name: AuthorizeErrorResponse
  property_count: 3
  slug: red-hat-3scale-authorizeerrorresponse
- name: AuthorizeResponse
  property_count: 3
  slug: red-hat-3scale-authorizeresponse
- name: BootResponse
  property_count: 2
  slug: red-hat-3scale-bootresponse
- name: CreateAccountRequest
  property_count: 4
  slug: red-hat-3scale-createaccountrequest
- name: CreateApplicationRequest
  property_count: 3
  slug: red-hat-3scale-createapplicationrequest
- name: DnsCacheResponse
  property_count: 1
  slug: red-hat-3scale-dnscacheresponse
- name: GatewayConfig
  property_count: 1
  slug: red-hat-3scale-gatewayconfig
- name: Invoice
  property_count: 11
  slug: red-hat-3scale-invoice
- name: InvoiceLineItem
  property_count: 5
  slug: red-hat-3scale-invoicelineitem
- name: InvoiceList
  property_count: 1
  slug: red-hat-3scale-invoicelist
- name: LivenessStatus
  property_count: 1
  slug: red-hat-3scale-livenessstatus
- name: OAuthAuthorizeResponse
  property_count: 2
  slug: red-hat-3scale-oauthauthorizeresponse
- name: PaymentTransaction
  property_count: 8
  slug: red-hat-3scale-paymenttransaction
- name: PaymentTransactionList
  property_count: 1
  slug: red-hat-3scale-paymenttransactionlist
- name: ReadinessStatus
  property_count: 2
  slug: red-hat-3scale-readinessstatus
- name: ReportRequest
  property_count: 3
  slug: red-hat-3scale-reportrequest
- name: Service
  property_count: 6
  slug: red-hat-3scale-service
- name: ServiceList
  property_count: 1
  slug: red-hat-3scale-servicelist
- name: StatusInfo
  property_count: 2
  slug: red-hat-3scale-statusinfo
- name: TopApplication
  property_count: 2
  slug: red-hat-3scale-topapplication
- name: TopApplicationsList
  property_count: 1
  slug: red-hat-3scale-topapplicationslist
- name: UpdateAccountRequest
  property_count: 2
  slug: red-hat-3scale-updateaccountrequest
- name: UpdateApplicationRequest
  property_count: 3
  slug: red-hat-3scale-updateapplicationrequest
- name: UsageReport
  property_count: 6
  slug: red-hat-3scale-usagereport
- name: UsageStats
  property_count: 6
  slug: red-hat-3scale-usagestats
json_structures:
- name: Red Hat 3Scale Account Structure
  property_count: 0
  slug: red-hat-3scale-account-structure
- name: Red Hat 3Scale Structure
  property_count: 0
  slug: red-hat-3scale-structure
jsonld:
- class_count: 3
  name: Red Hat 3Scale Context
  property_count: 20
  slug: red-hat-3scale-context
layout: provider
modified: '2026-05-19'
name: Red Hat 3scale
nav: Providers
network: true
overview: 'Red Hat 3scale publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Applications API, Authorization API, and 10 more. Tagged areas include API Gateway, API Management, Developer Portal, Enterprise, and Red Hat.


  The Red Hat 3scale catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Red Hat 3scale''s developer surface includes authentication, documentation, getting-started guide, developer portal, engineering blog, support, changelog, and 24 more developer resources.'
plans:
- name: Red Hat 3Scale Plans Pricing
  plan_count: 2
  slug: red-hat-3scale-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 2
  name: Red Hat 3Scale Rate Limits
  slug: red-hat-3scale-rate-limits
rules:
- name: Red Hat 3scale API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: red-hat-3scale-jsonschema-spectral-rules
- name: Red Hat 3scale API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 7
  slug: red-hat-3scale-rules
score:
  band: strong
  composite: 59.1
  delta: -3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.3
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red-hat-3scale/refs/heads/main/screenshots/red-hat-3scale-2026-06-20T192716.png
security:
- kind: authentication
  name: Red Hat 3Scale Authentication
  slug: red-hat-3scale-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Red Hat 3Scale Domain Security
  slug: red-hat-3scale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Hat 3Scale Vulnerability Disclosure
  slug: red-hat-3scale-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: red-hat-3scale
tags:
- API Gateway
- API Management
- Developer Portal
- Enterprise
- Red Hat
website: https://www.redhat.com/en/technologies/jboss-middleware/3scale
---
