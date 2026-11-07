---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 214
  human_in_the_loop: 0
  name: Xero Agentic Access
  operation_count: 466
  slug: xero-agentic-access
  summary_line: 466 operations · 214 acting
api_count: 15
apis:
- baseURL: https://api.xero.com/api.xro/2.0
  baseurl_source: declared
  description: The Accounting API from Xero — 140 operation(s) for accounting.
  name: Xero Accounting API
  slug: xero-accounting-api
- baseURL: https://api.xero.com/assets.xro/1.0
  baseurl_source: declared
  description: The Asset API from Xero — 4 operation(s) for asset.
  name: Xero Asset API
  slug: xero-asset-api
- baseURL: https://api.xero.com/files.xro/1.0
  baseurl_source: declared
  description: Operations available to regular developers
  name: Xero Files API
  slug: xero-files-api
- baseURL: https://api.xero.com/finance.xro/1.0
  baseurl_source: declared
  description: The Finance API from Xero — 8 operation(s) for finance.
  name: Xero Finance API
  slug: xero-finance-api
- baseURL: https://api.xero.com
  baseurl_source: declared
  description: The Identity API from Xero — 2 operation(s) for identity.
  name: Xero Identity API
  slug: xero-identity-api
- baseURL: https://api.xero.com/payroll.xro/1.0
  baseurl_source: declared
  description: Operations available to regular developers
  name: Xero PayrollAu API
  slug: xero-payrollau-api
- baseURL: https://api.xero.com/payroll.xro/2.0
  baseurl_source: declared
  description: The PayrollNz API from Xero — 46 operation(s) for payrollnz.
  name: Xero PayrollNz API
  slug: xero-payrollnz-api
- baseURL: https://api.xero.com/payroll.xro/2.0
  baseurl_source: declared
  description: The PayrollUk API from Xero — 47 operation(s) for payrolluk.
  name: Xero PayrollUk API
  slug: xero-payrolluk-api
- baseURL: https://api.xero.com/projects.xro/2.0
  baseurl_source: declared
  description: The Project API from Xero — 7 operation(s) for project.
  name: Xero Project API
  slug: xero-project-api
- description: OAuth 2.0 connections endpoint for listing the Xero tenants authorized under an access token.
  name: Xero Connections API
  slug: connections
- baseURL: https://api.xero.com/api.xro/2.0
  baseurl_source: declared
  description: The AccountData API from Xero — 3 operation(s) for accountdata.
  name: Xero Account Data API
  slug: xero-accountdata-api
- baseURL: https://api.xero.com/api.xro/2.0
  baseurl_source: declared
  description: The FeedConnections API from Xero — 5 operation(s) for feedconnections.
  name: Xero Feed Connections API
  slug: xero-feedconnections-api
- baseURL: https://api.xero.com/api.xro/2.0
  baseurl_source: declared
  description: The App Store API from Xero — 4 operation(s) for app store.
  name: Xero App Store API
  slug: xero-app-store-api
- baseURL: https://api.xero.com/api.xro/2.0
  baseurl_source: declared
  description: The Bank Feeds API from Xero — 5 operation(s) for bank feeds.
  name: Xero Bank Feeds API
  slug: xero-bank-feeds-api
artifact_total: 839
asyncapis:
- description: AsyncAPI 2.6 description of Xero's outbound webhook surface for the INVOICE and CONTACT event categories. Xero delivers event notifications by issuing HTTP POST requests with a JSON body to a single s
  name: Xero Webhooks
  slug: xero-webhooks-asyncapi
collections:
- collection_type: postman
  name: Xero Accounting API
  slug: postman-xero-accounting-api
- collection_type: postman
  name: Xero Accounting Asset API
  slug: postman-xero-asset-api
- collection_type: postman
  name: Xero Accounting BankFeeds API
  slug: postman-xero-bankfeeds-api
- collection_type: postman
  name: Xero Accounting Files API
  slug: postman-xero-files-api
- collection_type: postman
  name: Xero Accounting Finance API
  slug: postman-xero-finance-api
- collection_type: postman
  name: Xero Accounting Identity API
  slug: postman-xero-identity-api
- collection_type: postman
  name: Xero Accounting PayrollAu API
  slug: postman-xero-payrollau-api
- collection_type: postman
  name: Xero Accounting PayrollNz API
  slug: postman-xero-payrollnz-api
- collection_type: postman
  name: Xero Accounting PayrollUk API
  slug: postman-xero-payrolluk-api
- collection_type: postman
  name: Xero Accounting Project API
  slug: postman-xero-project-api
- collection_type: open
  name: Xero Accounting API
  slug: open-xero-accounting-api
- collection_type: open
  name: Xero Accounting API
  slug: open-xero-accounting
- collection_type: open
  name: Xero Accounting Asset API
  slug: open-xero-asset-api
- collection_type: open
  name: Xero Assets API
  slug: open-xero-assets
- collection_type: open
  name: Xero Accounting BankFeeds API
  slug: open-xero-bankfeeds-api
- collection_type: open
  name: Xero Bank Feeds API
  slug: open-xero-bankfeeds
- collection_type: open
  name: Xero Accounting Files API
  slug: open-xero-files-api
- collection_type: open
  name: Xero Files API
  slug: open-xero-files
- collection_type: open
  name: Xero Accounting Finance API
  slug: open-xero-finance-api
- collection_type: open
  name: Xero Finance API
  slug: open-xero-finance
- collection_type: open
  name: Xero Accounting Identity API
  slug: open-xero-identity-api
- collection_type: open
  name: Xero OAuth 2 Identity Service API
  slug: open-xero-identity
- collection_type: open
  name: Xero Payroll AU API
  slug: open-xero-payroll-au
- collection_type: open
  name: Xero Payroll NZ
  slug: open-xero-payroll-nz
- collection_type: open
  name: Xero Payroll UK
  slug: open-xero-payroll-uk
- collection_type: open
  name: Xero Accounting PayrollAu API
  slug: open-xero-payrollau-api
- collection_type: open
  name: Xero Accounting PayrollNz API
  slug: open-xero-payrollnz-api
- collection_type: open
  name: Xero Accounting PayrollUk API
  slug: open-xero-payrolluk-api
- collection_type: open
  name: Xero Accounting Project API
  slug: open-xero-project-api
- collection_type: open
  name: Xero Projects API
  slug: open-xero-projects
common:
- group: design
  href: https://artifacts.apis.io/xero/rules/xero-xero-openapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/xero-xero-openapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/xero/rules/xero-rules.yml
  title: ''
  type: Spectral
  url: rules/xero-rules.yml
- group: design
  href: https://artifacts.apis.io/xero/rules/xero-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/xero-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/xero/rules/xero-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/xero-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/xero/json-ld/xero-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/xero-context.jsonld
- group: design
  href: https://artifacts.apis.io/xero/vocabulary/xero-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xero-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/xero/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/xero/asyncapi/xero-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/xero-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/xero/data-model/xero-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xero-data-model.yml
- group: build
  href: https://artifacts.apis.io/xero/cli/xero-cli.yml
  title: ''
  type: CLI
  url: cli/xero-cli.yml
- group: operate
  href: https://artifacts.apis.io/xero/changelog/xero-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/xero-changelog.yml
- group: design
  href: https://artifacts.apis.io/xero/conventions/xero-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/xero-conventions.yml
- group: design
  href: https://artifacts.apis.io/xero/conventions/xero-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xero-conventions.yml
- group: start
  href: https://artifacts.apis.io/xero/sandbox/xero-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/xero-sandbox.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.xero.com/documentation/guides/oauth2/scopes/
- group: design
  href: https://artifacts.apis.io/xero/lifecycle/xero-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xero-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/xero/errors/xero-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xero-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xero/conformance/xero-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xero-conformance.yml
- group: other
  href: https://artifacts.apis.io/xero/overlays/xero-account-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xero-account-data-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/xero/llms/xero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xero-llms.txt
- group: build
  href: https://artifacts.apis.io/xero/mcp/xero-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/xero-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/xero/well-known/xero-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xero-status-security.txt
- group: agent
  href: https://artifacts.apis.io/xero/well-known/xero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xero-well-known.yml
- group: other
  href: https://artifacts.apis.io/xero/hosts/xero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xero-hosts.yml
- group: build
  href: https://artifacts.apis.io/xero/integrations/xero-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/xero-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/xero/vendors/xero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xero-vendors.yml
- group: build
  href: https://artifacts.apis.io/xero/packages/xero-packages.yml
  title: ''
  type: Packages
  url: packages/xero-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.xero.com/signup/
- group: commercial
  href: https://artifacts.apis.io/xero/plans/xero-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xero-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/xero/rate-limits/xero-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xero-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/xero/finops/xero-finops.yml
  title: ''
  type: FinOps
  url: finops/xero-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.xero.com/
- group: other
  href: https://artifacts.apis.io/xero/capabilities/xero-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/xero-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/xero/overview
- group: agent
  href: https://artifacts.apis.io/xero/agentic-access/xero-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xero-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/xero/security/xero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xero-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/xero/authentication/xero-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xero-authentication.yml
- group: auth
  href: https://artifacts.apis.io/xero/scopes/xero-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/xero-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xero
- group: start
  title: ''
  type: Portal
  url: https://developer.xero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.xero.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.xero.com/documentation/getting-started-guide/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.xero.com/documentation/guides/oauth2/overview/
- group: build
  title: ''
  type: SDKs
  url: https://developer.xero.com/documentation/sdks-and-tools/libraries/overview/
- group: design
  title: ''
  type: Webhooks
  url: https://developer.xero.com/documentation/guides/webhooks/overview/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.xero.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://devblog.xero.com/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.xero.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.xero.com/xero-developer-platform-terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xero.com/us/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xero.com/
- group: start
  title: ''
  type: Signup
  url: https://www.xero.com/us/signup/developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XeroAPI
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/XeroAPI/xero-mcp-server
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/XeroAPI/Xero-OpenAPI/blob/fd9d44b04bf4934a7509b8e7ece51a9e0e462e4f/.spectral.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.xero.com/documentation/api/accounting/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.xero.com/pricing
- group: commercial
  title: ''
  type: ProductPricing
  url: https://www.xero.com/us/pricing-plans/
- group: operate
  title: ''
  type: Support
  url: https://central.xero.com/
- group: auth
  title: ''
  type: Security
  url: https://www.xero.com/security/
- group: company
  title: ''
  type: CompanyBlog
  url: https://blog.xero.com/
- group: other
  title: ''
  type: FeatureRequests
  url: https://productideas.xero.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.xero.com/media/
- group: other
  title: ''
  type: Leadership
  url: https://www.xero.com/about/team/
created: '2024-11-07'
description: Xero is a cloud-based accounting software platform that helps small and medium-sized businesses manage their finances. Xero provides a comprehensive developer platform with OAuth 2.0 APIs for accounting, payroll, assets, projects, files, bank feeds, and identity management. The Xero API enables third-party integrations to build custom accounting apps, automations, and business tools. Xero supports SDKs for .NET, Java, Node.js, PHP, Ruby, Python, and provides an MCP server for AI-assisted accounting workflows.
examples:
- key_count: 6
  name: Xero Approveleaveapplication Example
  slug: xero-approveleaveapplication-example
- key_count: 6
  name: Xero Approvetimesheet Example
  slug: xero-approvetimesheet-example
- key_count: 6
  name: Xero Createaccount Example
  slug: xero-createaccount-example
- key_count: 6
  name: Xero Createaccountattachmentbyfilename Example
  slug: xero-createaccountattachmentbyfilename-example
- key_count: 6
  name: Xero Createasset Example
  slug: xero-createasset-example
- key_count: 6
  name: Xero Createassettype Example
  slug: xero-createassettype-example
- key_count: 6
  name: Xero Createbanktransactionattachmentbyfilename Example
  slug: xero-createbanktransactionattachmentbyfilename-example
- key_count: 6
  name: Xero Createbanktransactions Example
  slug: xero-createbanktransactions-example
- key_count: 6
  name: Xero Createbanktransfer Example
  slug: xero-createbanktransfer-example
- key_count: 6
  name: Xero Createbanktransferattachmentbyfilename Example
  slug: xero-createbanktransferattachmentbyfilename-example
- key_count: 6
  name: Xero Createbatchpayment Example
  slug: xero-createbatchpayment-example
- key_count: 6
  name: Xero Createbatchpaymenthistoryrecord Example
  slug: xero-createbatchpaymenthistoryrecord-example
- key_count: 6
  name: Xero Createbenefit Example
  slug: xero-createbenefit-example
- key_count: 6
  name: Xero Createbrandingthemepaymentservices Example
  slug: xero-createbrandingthemepaymentservices-example
- key_count: 6
  name: Xero Createcontactattachmentbyfilename Example
  slug: xero-createcontactattachmentbyfilename-example
- key_count: 6
  name: Xero Createcontactgroup Example
  slug: xero-createcontactgroup-example
- key_count: 6
  name: Xero Createcontactgroupcontacts Example
  slug: xero-createcontactgroupcontacts-example
- key_count: 6
  name: Xero Createcontacts Example
  slug: xero-createcontacts-example
- key_count: 6
  name: Xero Createcreditnoteallocation Example
  slug: xero-createcreditnoteallocation-example
- key_count: 6
  name: Xero Createcreditnoteattachmentbyfilename Example
  slug: xero-createcreditnoteattachmentbyfilename-example
- key_count: 6
  name: Xero Createcreditnotes Example
  slug: xero-createcreditnotes-example
- key_count: 6
  name: Xero Createcurrency Example
  slug: xero-createcurrency-example
- key_count: 6
  name: Xero Creatededuction Example
  slug: xero-creatededuction-example
- key_count: 6
  name: Xero Createearningsrate Example
  slug: xero-createearningsrate-example
- key_count: 6
  name: Xero Createemployee Example
  slug: xero-createemployee-example
- key_count: 6
  name: Xero Createemployeeearningstemplate Example
  slug: xero-createemployeeearningstemplate-example
- key_count: 6
  name: Xero Createemployeeleave Example
  slug: xero-createemployeeleave-example
- key_count: 6
  name: Xero Createemployeeleavesetup Example
  slug: xero-createemployeeleavesetup-example
- key_count: 6
  name: Xero Createemployeeleavetype Example
  slug: xero-createemployeeleavetype-example
- key_count: 6
  name: Xero Createemployeeopeningbalances Example
  slug: xero-createemployeeopeningbalances-example
- key_count: 6
  name: Xero Createemployeepaymentmethod Example
  slug: xero-createemployeepaymentmethod-example
- key_count: 6
  name: Xero Createemployees Example
  slug: xero-createemployees-example
- key_count: 6
  name: Xero Createemployeesalaryandwage Example
  slug: xero-createemployeesalaryandwage-example
- key_count: 6
  name: Xero Createemployeestatutorysickleave Example
  slug: xero-createemployeestatutorysickleave-example
- key_count: 6
  name: Xero Createemployeeworkingpattern Example
  slug: xero-createemployeeworkingpattern-example
- key_count: 6
  name: Xero Createemployment Example
  slug: xero-createemployment-example
- key_count: 6
  name: Xero Createexpenseclaims Example
  slug: xero-createexpenseclaims-example
- key_count: 6
  name: Xero Createfeedconnections Example
  slug: xero-createfeedconnections-example
- key_count: 6
  name: Xero Createfileassociation Example
  slug: xero-createfileassociation-example
- key_count: 6
  name: Xero Createfolder Example
  slug: xero-createfolder-example
- key_count: 6
  name: Xero Createinvoiceattachmentbyfilename Example
  slug: xero-createinvoiceattachmentbyfilename-example
- key_count: 6
  name: Xero Createinvoices Example
  slug: xero-createinvoices-example
- key_count: 6
  name: Xero Createitems Example
  slug: xero-createitems-example
- key_count: 6
  name: Xero Createleaveapplication Example
  slug: xero-createleaveapplication-example
- key_count: 6
  name: Xero Createleavetype Example
  slug: xero-createleavetype-example
- key_count: 6
  name: Xero Createlinkedtransaction Example
  slug: xero-createlinkedtransaction-example
- key_count: 6
  name: Xero Createmanualjournalattachmentbyfilename Example
  slug: xero-createmanualjournalattachmentbyfilename-example
- key_count: 6
  name: Xero Createmanualjournals Example
  slug: xero-createmanualjournals-example
- key_count: 6
  name: Xero Createmultipleemployeeearningstemplate Example
  slug: xero-createmultipleemployeeearningstemplate-example
- key_count: 6
  name: Xero Createoverpaymentallocations Example
  slug: xero-createoverpaymentallocations-example
- key_count: 6
  name: Xero Createoverpaymenthistory Example
  slug: xero-createoverpaymenthistory-example
- key_count: 6
  name: Xero Createpayitem Example
  slug: xero-createpayitem-example
- key_count: 6
  name: Xero Createpayment Example
  slug: xero-createpayment-example
- key_count: 6
  name: Xero Createpaymenthistory Example
  slug: xero-createpaymenthistory-example
- key_count: 6
  name: Xero Createpayments Example
  slug: xero-createpayments-example
- key_count: 6
  name: Xero Createpaymentservice Example
  slug: xero-createpaymentservice-example
- key_count: 6
  name: Xero Createpayrollcalendar Example
  slug: xero-createpayrollcalendar-example
- key_count: 6
  name: Xero Createpayrun Example
  slug: xero-createpayrun-example
- key_count: 6
  name: Xero Createpayruncalendar Example
  slug: xero-createpayruncalendar-example
- key_count: 6
  name: Xero Createprepaymentallocations Example
  slug: xero-createprepaymentallocations-example
- key_count: 6
  name: Xero Createprepaymenthistory Example
  slug: xero-createprepaymenthistory-example
- key_count: 6
  name: Xero Createproject Example
  slug: xero-createproject-example
- key_count: 6
  name: Xero Createpurchaseorderattachmentbyfilename Example
  slug: xero-createpurchaseorderattachmentbyfilename-example
- key_count: 6
  name: Xero Createpurchaseorders Example
  slug: xero-createpurchaseorders-example
- key_count: 6
  name: Xero Createquoteattachmentbyfilename Example
  slug: xero-createquoteattachmentbyfilename-example
- key_count: 6
  name: Xero Createquotes Example
  slug: xero-createquotes-example
- key_count: 6
  name: Xero Createreceipt Example
  slug: xero-createreceipt-example
- key_count: 6
  name: Xero Createreceiptattachmentbyfilename Example
  slug: xero-createreceiptattachmentbyfilename-example
- key_count: 6
  name: Xero Createreceipthistory Example
  slug: xero-createreceipthistory-example
- key_count: 6
  name: Xero Createreimbursement Example
  slug: xero-createreimbursement-example
- key_count: 6
  name: Xero Createrepeatinginvoiceattachmentbyfilename Example
  slug: xero-createrepeatinginvoiceattachmentbyfilename-example
- key_count: 6
  name: Xero Createrepeatinginvoices Example
  slug: xero-createrepeatinginvoices-example
- key_count: 6
  name: Xero Createstatements Example
  slug: xero-createstatements-example
- key_count: 6
  name: Xero Createsuperannuation Example
  slug: xero-createsuperannuation-example
- key_count: 6
  name: Xero Createsuperfund Example
  slug: xero-createsuperfund-example
- key_count: 6
  name: Xero Createtask Example
  slug: xero-createtask-example
- key_count: 6
  name: Xero Createtaxrates Example
  slug: xero-createtaxrates-example
- key_count: 6
  name: Xero Createtimeentry Example
  slug: xero-createtimeentry-example
- key_count: 6
  name: Xero Createtimesheet Example
  slug: xero-createtimesheet-example
- key_count: 6
  name: Xero Createtimesheetline Example
  slug: xero-createtimesheetline-example
- key_count: 6
  name: Xero Createtrackingcategory Example
  slug: xero-createtrackingcategory-example
- key_count: 6
  name: Xero Createtrackingoptions Example
  slug: xero-createtrackingoptions-example
- key_count: 6
  name: Xero Deleteaccount Example
  slug: xero-deleteaccount-example
- key_count: 6
  name: Xero Deletebatchpayment Example
  slug: xero-deletebatchpayment-example
- key_count: 6
  name: Xero Deletebatchpaymentbyurlparam Example
  slug: xero-deletebatchpaymentbyurlparam-example
- key_count: 6
  name: Xero Deletecreditnoteallocations Example
  slug: xero-deletecreditnoteallocations-example
- key_count: 6
  name: Xero Deleteemployeeearningstemplate Example
  slug: xero-deleteemployeeearningstemplate-example
- key_count: 6
  name: Xero Deleteemployeeleave Example
  slug: xero-deleteemployeeleave-example
- key_count: 6
  name: Xero Deleteemployeesalaryandwage Example
  slug: xero-deleteemployeesalaryandwage-example
- key_count: 6
  name: Xero Deleteemployeeworkingpattern Example
  slug: xero-deleteemployeeworkingpattern-example
- key_count: 6
  name: Xero Deletefeedconnections Example
  slug: xero-deletefeedconnections-example
- key_count: 6
  name: Xero Deleteoverpaymentallocations Example
  slug: xero-deleteoverpaymentallocations-example
- key_count: 6
  name: Xero Deletepayment Example
  slug: xero-deletepayment-example
- key_count: 6
  name: Xero Deleteprepaymentallocations Example
  slug: xero-deleteprepaymentallocations-example
- key_count: 6
  name: Xero Deletetimesheet Example
  slug: xero-deletetimesheet-example
- key_count: 6
  name: Xero Deletetimesheetline Example
  slug: xero-deletetimesheetline-example
- key_count: 6
  name: Xero Deletetrackingcategory Example
  slug: xero-deletetrackingcategory-example
- key_count: 6
  name: Xero Deletetrackingoptions Example
  slug: xero-deletetrackingoptions-example
- key_count: 6
  name: Xero Emailinvoice Example
  slug: xero-emailinvoice-example
- key_count: 6
  name: Xero Getaccount Example
  slug: xero-getaccount-example
- key_count: 6
  name: Xero Getaccountattachments Example
  slug: xero-getaccountattachments-example
- key_count: 6
  name: Xero Getaccounts Example
  slug: xero-getaccounts-example
- key_count: 6
  name: Xero Getassetbyid Example
  slug: xero-getassetbyid-example
- key_count: 6
  name: Xero Getassets Example
  slug: xero-getassets-example
- key_count: 6
  name: Xero Getassetsettings Example
  slug: xero-getassetsettings-example
- key_count: 6
  name: Xero Getassettypes Example
  slug: xero-getassettypes-example
- key_count: 6
  name: Xero Getassociationsbyobject Example
  slug: xero-getassociationsbyobject-example
- key_count: 6
  name: Xero Getbankstatementaccounting Example
  slug: xero-getbankstatementaccounting-example
- key_count: 6
  name: Xero Getbanktransaction Example
  slug: xero-getbanktransaction-example
- key_count: 6
  name: Xero Getbanktransactionattachments Example
  slug: xero-getbanktransactionattachments-example
- key_count: 6
  name: Xero Getbanktransactions Example
  slug: xero-getbanktransactions-example
- key_count: 6
  name: Xero Getbanktransfer Example
  slug: xero-getbanktransfer-example
- key_count: 6
  name: Xero Getbanktransferattachments Example
  slug: xero-getbanktransferattachments-example
- key_count: 6
  name: Xero Getbanktransfers Example
  slug: xero-getbanktransfers-example
- key_count: 6
  name: Xero Getbatchpayment Example
  slug: xero-getbatchpayment-example
- key_count: 6
  name: Xero Getbatchpaymenthistory Example
  slug: xero-getbatchpaymenthistory-example
- key_count: 6
  name: Xero Getbatchpayments Example
  slug: xero-getbatchpayments-example
- key_count: 6
  name: Xero Getbenefit Example
  slug: xero-getbenefit-example
- key_count: 6
  name: Xero Getbenefits Example
  slug: xero-getbenefits-example
- key_count: 6
  name: Xero Getbrandingtheme Example
  slug: xero-getbrandingtheme-example
- key_count: 6
  name: Xero Getbrandingthemepaymentservices Example
  slug: xero-getbrandingthemepaymentservices-example
- key_count: 6
  name: Xero Getbrandingthemes Example
  slug: xero-getbrandingthemes-example
- key_count: 6
  name: Xero Getbudget Example
  slug: xero-getbudget-example
- key_count: 6
  name: Xero Getbudgets Example
  slug: xero-getbudgets-example
- key_count: 6
  name: Xero Getcashvalidation Example
  slug: xero-getcashvalidation-example
- key_count: 6
  name: Xero Getconnections Example
  slug: xero-getconnections-example
- key_count: 6
  name: Xero Getcontact Example
  slug: xero-getcontact-example
- key_count: 6
  name: Xero Getcontactattachments Example
  slug: xero-getcontactattachments-example
- key_count: 6
  name: Xero Getcontactbycontactnumber Example
  slug: xero-getcontactbycontactnumber-example
- key_count: 6
  name: Xero Getcontactcissettings Example
  slug: xero-getcontactcissettings-example
- key_count: 6
  name: Xero Getcontactgroup Example
  slug: xero-getcontactgroup-example
- key_count: 6
  name: Xero Getcontactgroups Example
  slug: xero-getcontactgroups-example
- key_count: 6
  name: Xero Getcontacts Example
  slug: xero-getcontacts-example
- key_count: 6
  name: Xero Getcreditnote Example
  slug: xero-getcreditnote-example
- key_count: 6
  name: Xero Getcreditnoteattachments Example
  slug: xero-getcreditnoteattachments-example
- key_count: 6
  name: Xero Getcreditnotes Example
  slug: xero-getcreditnotes-example
- key_count: 6
  name: Xero Getcurrencies Example
  slug: xero-getcurrencies-example
- key_count: 6
  name: Xero Getdeduction Example
  slug: xero-getdeduction-example
- key_count: 6
  name: Xero Getdeductions Example
  slug: xero-getdeductions-example
- key_count: 6
  name: Xero Getearningsorder Example
  slug: xero-getearningsorder-example
- key_count: 6
  name: Xero Getearningsorders Example
  slug: xero-getearningsorders-example
- key_count: 6
  name: Xero Getearningsrate Example
  slug: xero-getearningsrate-example
- key_count: 6
  name: Xero Getearningsrates Example
  slug: xero-getearningsrates-example
- key_count: 6
  name: Xero Getemployee Example
  slug: xero-getemployee-example
- key_count: 6
  name: Xero Getemployeeleave Example
  slug: xero-getemployeeleave-example
- key_count: 6
  name: Xero Getemployeeleavebalances Example
  slug: xero-getemployeeleavebalances-example
- key_count: 6
  name: Xero Getemployeeleaveperiods Example
  slug: xero-getemployeeleaveperiods-example
- key_count: 6
  name: Xero Getemployeeleaves Example
  slug: xero-getemployeeleaves-example
- key_count: 6
  name: Xero Getemployeeleavetypes Example
  slug: xero-getemployeeleavetypes-example
- key_count: 6
  name: Xero Getemployeeopeningbalances Example
  slug: xero-getemployeeopeningbalances-example
- key_count: 6
  name: Xero Getemployeepaymentmethod Example
  slug: xero-getemployeepaymentmethod-example
- key_count: 6
  name: Xero Getemployeepaytemplate Example
  slug: xero-getemployeepaytemplate-example
- key_count: 6
  name: Xero Getemployeepaytemplates Example
  slug: xero-getemployeepaytemplates-example
- key_count: 6
  name: Xero Getemployees Example
  slug: xero-getemployees-example
- key_count: 6
  name: Xero Getemployeesalaryandwage Example
  slug: xero-getemployeesalaryandwage-example
- key_count: 6
  name: Xero Getemployeesalaryandwages Example
  slug: xero-getemployeesalaryandwages-example
- key_count: 6
  name: Xero Getemployeestatutoryleavebalances Example
  slug: xero-getemployeestatutoryleavebalances-example
- key_count: 6
  name: Xero Getemployeestatutorysickleave Example
  slug: xero-getemployeestatutorysickleave-example
- key_count: 6
  name: Xero Getemployeetax Example
  slug: xero-getemployeetax-example
- key_count: 6
  name: Xero Getemployeeworkingpattern Example
  slug: xero-getemployeeworkingpattern-example
- key_count: 6
  name: Xero Getemployeeworkingpatterns Example
  slug: xero-getemployeeworkingpatterns-example
- key_count: 6
  name: Xero Getexpenseclaim Example
  slug: xero-getexpenseclaim-example
- key_count: 6
  name: Xero Getexpenseclaims Example
  slug: xero-getexpenseclaims-example
- key_count: 6
  name: Xero Getfeedconnection Example
  slug: xero-getfeedconnection-example
- key_count: 6
  name: Xero Getfeedconnections Example
  slug: xero-getfeedconnections-example
- key_count: 6
  name: Xero Getfile Example
  slug: xero-getfile-example
- key_count: 6
  name: Xero Getfileassociations Example
  slug: xero-getfileassociations-example
- key_count: 6
  name: Xero Getfiles Example
  slug: xero-getfiles-example
- key_count: 6
  name: Xero Getfinancialstatementbalancesheet Example
  slug: xero-getfinancialstatementbalancesheet-example
- key_count: 6
  name: Xero Getfinancialstatementcashflow Example
  slug: xero-getfinancialstatementcashflow-example
- key_count: 6
  name: Xero Getfinancialstatementcontactsexpense Example
  slug: xero-getfinancialstatementcontactsexpense-example
- key_count: 6
  name: Xero Getfinancialstatementcontactsrevenue Example
  slug: xero-getfinancialstatementcontactsrevenue-example
- key_count: 6
  name: Xero Getfinancialstatementprofitandloss Example
  slug: xero-getfinancialstatementprofitandloss-example
- key_count: 6
  name: Xero Getfinancialstatementtrialbalance Example
  slug: xero-getfinancialstatementtrialbalance-example
- key_count: 6
  name: Xero Getfolder Example
  slug: xero-getfolder-example
- key_count: 6
  name: Xero Getfolders Example
  slug: xero-getfolders-example
- key_count: 6
  name: Xero Getinbox Example
  slug: xero-getinbox-example
- key_count: 6
  name: Xero Getinvoice Example
  slug: xero-getinvoice-example
- key_count: 6
  name: Xero Getinvoiceattachments Example
  slug: xero-getinvoiceattachments-example
- key_count: 6
  name: Xero Getinvoicereminders Example
  slug: xero-getinvoicereminders-example
- key_count: 6
  name: Xero Getinvoices Example
  slug: xero-getinvoices-example
- key_count: 6
  name: Xero Getitem Example
  slug: xero-getitem-example
- key_count: 6
  name: Xero Getitems Example
  slug: xero-getitems-example
- key_count: 6
  name: Xero Getjournal Example
  slug: xero-getjournal-example
- key_count: 6
  name: Xero Getjournalbynumber Example
  slug: xero-getjournalbynumber-example
- key_count: 6
  name: Xero Getjournals Example
  slug: xero-getjournals-example
- key_count: 6
  name: Xero Getleaveapplication Example
  slug: xero-getleaveapplication-example
- key_count: 6
  name: Xero Getleaveapplications Example
  slug: xero-getleaveapplications-example
- key_count: 6
  name: Xero Getleaveapplicationsv2 Example
  slug: xero-getleaveapplicationsv2-example
- key_count: 6
  name: Xero Getleavetype Example
  slug: xero-getleavetype-example
- key_count: 6
  name: Xero Getleavetypes Example
  slug: xero-getleavetypes-example
- key_count: 6
  name: Xero Getlinkedtransaction Example
  slug: xero-getlinkedtransaction-example
- key_count: 6
  name: Xero Getlinkedtransactions Example
  slug: xero-getlinkedtransactions-example
- key_count: 6
  name: Xero Getmanualjournal Example
  slug: xero-getmanualjournal-example
- key_count: 6
  name: Xero Getmanualjournalattachments Example
  slug: xero-getmanualjournalattachments-example
- key_count: 6
  name: Xero Getmanualjournals Example
  slug: xero-getmanualjournals-example
- key_count: 6
  name: Xero Getonlineinvoice Example
  slug: xero-getonlineinvoice-example
- key_count: 6
  name: Xero Getorganisationactions Example
  slug: xero-getorganisationactions-example
- key_count: 6
  name: Xero Getorganisationcissettings Example
  slug: xero-getorganisationcissettings-example
- key_count: 6
  name: Xero Getorganisations Example
  slug: xero-getorganisations-example
- key_count: 6
  name: Xero Getoverpayment Example
  slug: xero-getoverpayment-example
- key_count: 6
  name: Xero Getoverpayments Example
  slug: xero-getoverpayments-example
- key_count: 6
  name: Xero Getpayitems Example
  slug: xero-getpayitems-example
- key_count: 6
  name: Xero Getpayment Example
  slug: xero-getpayment-example
- key_count: 6
  name: Xero Getpayments Example
  slug: xero-getpayments-example
- key_count: 6
  name: Xero Getpaymentservices Example
  slug: xero-getpaymentservices-example
- key_count: 6
  name: Xero Getpayrollcalendar Example
  slug: xero-getpayrollcalendar-example
- key_count: 6
  name: Xero Getpayrollcalendars Example
  slug: xero-getpayrollcalendars-example
- key_count: 6
  name: Xero Getpayrun Example
  slug: xero-getpayrun-example
- key_count: 6
  name: Xero Getpayruncalendar Example
  slug: xero-getpayruncalendar-example
- key_count: 6
  name: Xero Getpayruncalendars Example
  slug: xero-getpayruncalendars-example
- key_count: 6
  name: Xero Getpayruns Example
  slug: xero-getpayruns-example
- key_count: 6
  name: Xero Getpayslip Example
  slug: xero-getpayslip-example
- key_count: 6
  name: Xero Getpayslips Example
  slug: xero-getpayslips-example
- key_count: 6
  name: Xero Getprepayment Example
  slug: xero-getprepayment-example
- key_count: 6
  name: Xero Getprepayments Example
  slug: xero-getprepayments-example
- key_count: 6
  name: Xero Getproject Example
  slug: xero-getproject-example
- key_count: 6
  name: Xero Getprojects Example
  slug: xero-getprojects-example
- key_count: 6
  name: Xero Getprojectusers Example
  slug: xero-getprojectusers-example
- key_count: 6
  name: Xero Getpurchaseorder Example
  slug: xero-getpurchaseorder-example
- key_count: 6
  name: Xero Getpurchaseorderattachments Example
  slug: xero-getpurchaseorderattachments-example
- key_count: 6
  name: Xero Getpurchaseorderbynumber Example
  slug: xero-getpurchaseorderbynumber-example
- key_count: 6
  name: Xero Getpurchaseorders Example
  slug: xero-getpurchaseorders-example
- key_count: 6
  name: Xero Getquote Example
  slug: xero-getquote-example
- key_count: 6
  name: Xero Getquoteattachments Example
  slug: xero-getquoteattachments-example
- key_count: 6
  name: Xero Getquotes Example
  slug: xero-getquotes-example
- key_count: 6
  name: Xero Getreceipt Example
  slug: xero-getreceipt-example
- key_count: 6
  name: Xero Getreceiptattachments Example
  slug: xero-getreceiptattachments-example
- key_count: 6
  name: Xero Getreceipts Example
  slug: xero-getreceipts-example
- key_count: 6
  name: Xero Getreimbursement Example
  slug: xero-getreimbursement-example
- key_count: 6
  name: Xero Getreimbursements Example
  slug: xero-getreimbursements-example
- key_count: 6
  name: Xero Getrepeatinginvoice Example
  slug: xero-getrepeatinginvoice-example
- key_count: 6
  name: Xero Getrepeatinginvoiceattachments Example
  slug: xero-getrepeatinginvoiceattachments-example
- key_count: 6
  name: Xero Getrepeatinginvoices Example
  slug: xero-getrepeatinginvoices-example
- key_count: 6
  name: Xero Getreportagedpayablesbycontact Example
  slug: xero-getreportagedpayablesbycontact-example
- key_count: 6
  name: Xero Getreportagedreceivablesbycontact Example
  slug: xero-getreportagedreceivablesbycontact-example
- key_count: 6
  name: Xero Getreportbalancesheet Example
  slug: xero-getreportbalancesheet-example
- key_count: 6
  name: Xero Getreportbanksummary Example
  slug: xero-getreportbanksummary-example
- key_count: 6
  name: Xero Getreportbudgetsummary Example
  slug: xero-getreportbudgetsummary-example
- key_count: 6
  name: Xero Getreportexecutivesummary Example
  slug: xero-getreportexecutivesummary-example
- key_count: 6
  name: Xero Getreporttenninetynine Example
  slug: xero-getreporttenninetynine-example
- key_count: 6
  name: Xero Getreporttrialbalance Example
  slug: xero-getreporttrialbalance-example
- key_count: 6
  name: Xero Getsettings Example
  slug: xero-getsettings-example
- key_count: 6
  name: Xero Getstatement Example
  slug: xero-getstatement-example
- key_count: 6
  name: Xero Getstatements Example
  slug: xero-getstatements-example
- key_count: 6
  name: Xero Getstatutorydeduction Example
  slug: xero-getstatutorydeduction-example
- key_count: 6
  name: Xero Getstatutorydeductions Example
  slug: xero-getstatutorydeductions-example
- key_count: 6
  name: Xero Getstatutoryleavesummary Example
  slug: xero-getstatutoryleavesummary-example
- key_count: 6
  name: Xero Getsuperannuation Example
  slug: xero-getsuperannuation-example
- key_count: 6
  name: Xero Getsuperannuations Example
  slug: xero-getsuperannuations-example
- key_count: 6
  name: Xero Getsuperfund Example
  slug: xero-getsuperfund-example
- key_count: 6
  name: Xero Getsuperfundproducts Example
  slug: xero-getsuperfundproducts-example
- key_count: 6
  name: Xero Getsuperfunds Example
  slug: xero-getsuperfunds-example
- key_count: 6
  name: Xero Gettask Example
  slug: xero-gettask-example
- key_count: 6
  name: Xero Gettasks Example
  slug: xero-gettasks-example
- key_count: 6
  name: Xero Gettaxratebytaxtype Example
  slug: xero-gettaxratebytaxtype-example
- key_count: 6
  name: Xero Gettaxrates Example
  slug: xero-gettaxrates-example
- key_count: 6
  name: Xero Gettimeentries Example
  slug: xero-gettimeentries-example
- key_count: 6
  name: Xero Gettimeentry Example
  slug: xero-gettimeentry-example
- key_count: 6
  name: Xero Gettimesheet Example
  slug: xero-gettimesheet-example
- key_count: 6
  name: Xero Gettimesheets Example
  slug: xero-gettimesheets-example
- key_count: 6
  name: Xero Gettrackingcategories Example
  slug: xero-gettrackingcategories-example
- key_count: 6
  name: Xero Gettrackingcategory Example
  slug: xero-gettrackingcategory-example
- key_count: 6
  name: Xero Getuser Example
  slug: xero-getuser-example
- key_count: 6
  name: Xero Getusers Example
  slug: xero-getusers-example
- key_count: 6
  name: Xero Patchproject Example
  slug: xero-patchproject-example
- key_count: 6
  name: Xero Postsetup Example
  slug: xero-postsetup-example
- key_count: 6
  name: Xero Rejectleaveapplication Example
  slug: xero-rejectleaveapplication-example
- key_count: 6
  name: Xero Reverttimesheet Example
  slug: xero-reverttimesheet-example
- key_count: 6
  name: Xero Updateaccount Example
  slug: xero-updateaccount-example
- key_count: 6
  name: Xero Updateaccountattachmentbyfilename Example
  slug: xero-updateaccountattachmentbyfilename-example
- key_count: 6
  name: Xero Updatebanktransaction Example
  slug: xero-updatebanktransaction-example
- key_count: 6
  name: Xero Updatebanktransactionattachmentbyfilename Example
  slug: xero-updatebanktransactionattachmentbyfilename-example
- key_count: 6
  name: Xero Updatebanktransferattachmentbyfilename Example
  slug: xero-updatebanktransferattachmentbyfilename-example
- key_count: 6
  name: Xero Updatecontact Example
  slug: xero-updatecontact-example
- key_count: 6
  name: Xero Updatecontactattachmentbyfilename Example
  slug: xero-updatecontactattachmentbyfilename-example
- key_count: 6
  name: Xero Updatecontactgroup Example
  slug: xero-updatecontactgroup-example
- key_count: 6
  name: Xero Updatecreditnote Example
  slug: xero-updatecreditnote-example
- key_count: 6
  name: Xero Updatecreditnoteattachmentbyfilename Example
  slug: xero-updatecreditnoteattachmentbyfilename-example
- key_count: 6
  name: Xero Updateemployee Example
  slug: xero-updateemployee-example
- key_count: 6
  name: Xero Updateemployeeearningstemplate Example
  slug: xero-updateemployeeearningstemplate-example
- key_count: 6
  name: Xero Updateemployeeleave Example
  slug: xero-updateemployeeleave-example
- key_count: 6
  name: Xero Updateemployeeopeningbalances Example
  slug: xero-updateemployeeopeningbalances-example
- key_count: 6
  name: Xero Updateemployeesalaryandwage Example
  slug: xero-updateemployeesalaryandwage-example
- key_count: 6
  name: Xero Updateemployeetax Example
  slug: xero-updateemployeetax-example
- key_count: 6
  name: Xero Updateexpenseclaim Example
  slug: xero-updateexpenseclaim-example
- key_count: 6
  name: Xero Updatefile Example
  slug: xero-updatefile-example
- key_count: 6
  name: Xero Updatefolder Example
  slug: xero-updatefolder-example
- key_count: 6
  name: Xero Updateinvoice Example
  slug: xero-updateinvoice-example
- key_count: 6
  name: Xero Updateinvoiceattachmentbyfilename Example
  slug: xero-updateinvoiceattachmentbyfilename-example
- key_count: 6
  name: Xero Updateitem Example
  slug: xero-updateitem-example
- key_count: 6
  name: Xero Updateleaveapplication Example
  slug: xero-updateleaveapplication-example
- key_count: 6
  name: Xero Updatelinkedtransaction Example
  slug: xero-updatelinkedtransaction-example
- key_count: 6
  name: Xero Updatemanualjournal Example
  slug: xero-updatemanualjournal-example
- key_count: 6
  name: Xero Updatemanualjournalattachmentbyfilename Example
  slug: xero-updatemanualjournalattachmentbyfilename-example
- key_count: 6
  name: Xero Updateorcreatebanktransactions Example
  slug: xero-updateorcreatebanktransactions-example
- key_count: 6
  name: Xero Updateorcreatecontacts Example
  slug: xero-updateorcreatecontacts-example
- key_count: 6
  name: Xero Updateorcreatecreditnotes Example
  slug: xero-updateorcreatecreditnotes-example
- key_count: 6
  name: Xero Updateorcreateemployees Example
  slug: xero-updateorcreateemployees-example
- key_count: 6
  name: Xero Updateorcreateinvoices Example
  slug: xero-updateorcreateinvoices-example
- key_count: 6
  name: Xero Updateorcreateitems Example
  slug: xero-updateorcreateitems-example
- key_count: 6
  name: Xero Updateorcreatemanualjournals Example
  slug: xero-updateorcreatemanualjournals-example
- key_count: 6
  name: Xero Updateorcreatepurchaseorders Example
  slug: xero-updateorcreatepurchaseorders-example
- key_count: 6
  name: Xero Updateorcreatequotes Example
  slug: xero-updateorcreatequotes-example
- key_count: 6
  name: Xero Updateorcreaterepeatinginvoices Example
  slug: xero-updateorcreaterepeatinginvoices-example
- key_count: 6
  name: Xero Updatepayrun Example
  slug: xero-updatepayrun-example
- key_count: 6
  name: Xero Updatepayslip Example
  slug: xero-updatepayslip-example
- key_count: 6
  name: Xero Updatepaysliplineitems Example
  slug: xero-updatepaysliplineitems-example
- key_count: 6
  name: Xero Updateproject Example
  slug: xero-updateproject-example
- key_count: 6
  name: Xero Updatepurchaseorder Example
  slug: xero-updatepurchaseorder-example
- key_count: 6
  name: Xero Updatepurchaseorderattachmentbyfilename Example
  slug: xero-updatepurchaseorderattachmentbyfilename-example
- key_count: 6
  name: Xero Updatequote Example
  slug: xero-updatequote-example
- key_count: 6
  name: Xero Updatequoteattachmentbyfilename Example
  slug: xero-updatequoteattachmentbyfilename-example
- key_count: 6
  name: Xero Updatereceipt Example
  slug: xero-updatereceipt-example
- key_count: 6
  name: Xero Updatereceiptattachmentbyfilename Example
  slug: xero-updatereceiptattachmentbyfilename-example
- key_count: 6
  name: Xero Updaterepeatinginvoice Example
  slug: xero-updaterepeatinginvoice-example
- key_count: 6
  name: Xero Updaterepeatinginvoiceattachmentbyfilename Example
  slug: xero-updaterepeatinginvoiceattachmentbyfilename-example
- key_count: 6
  name: Xero Updatesuperfund Example
  slug: xero-updatesuperfund-example
- key_count: 6
  name: Xero Updatetask Example
  slug: xero-updatetask-example
- key_count: 6
  name: Xero Updatetaxrate Example
  slug: xero-updatetaxrate-example
- key_count: 6
  name: Xero Updatetimeentry Example
  slug: xero-updatetimeentry-example
- key_count: 6
  name: Xero Updatetimesheet Example
  slug: xero-updatetimesheet-example
- key_count: 6
  name: Xero Updatetimesheetline Example
  slug: xero-updatetimesheetline-example
- key_count: 6
  name: Xero Updatetrackingcategory Example
  slug: xero-updatetrackingcategory-example
- key_count: 6
  name: Xero Updatetrackingoptions Example
  slug: xero-updatetrackingoptions-example
- key_count: 6
  name: Xero Uploadfile Example
  slug: xero-uploadfile-example
- key_count: 6
  name: Xero Uploadfiletofolder Example
  slug: xero-uploadfiletofolder-example
finops:
- has_sources: true
  method: derived
  name: Xero Finops
  primary_unit: subscription
  service_category: ''
  slug: xero-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xero.png
json_schemas:
- name: AccessToken
  property_count: 5
  slug: xero-accesstoken
- name: AccountBalancesResponse
  property_count: 1
  slug: xero-account-balances-response
- name: AccountMovementsResponse
  property_count: 1
  slug: xero-account-movements-response
- name: Account
  property_count: 20
  slug: xero-account
- name: AccountTransactionsResponse
  property_count: 4
  slug: xero-account-transactions-response
- name: Accounts
  property_count: 1
  slug: xero-accounts
- name: AccountsPayable
  property_count: 2
  slug: xero-accountspayable
- name: AccountsReceivable
  property_count: 2
  slug: xero-accountsreceivable
- name: AccountType
  property_count: 0
  slug: xero-accounttype
- name: Action
  property_count: 2
  slug: xero-action
- name: Actions
  property_count: 1
  slug: xero-actions
- name: Address
  property_count: 10
  slug: xero-address
- name: AddressForOrganisation
  property_count: 10
  slug: xero-addressfororganisation
- name: Allocation
  property_count: 10
  slug: xero-allocation
- name: Allocations
  property_count: 1
  slug: xero-allocations
- name: AllowanceCategory
  property_count: 0
  slug: xero-allowancecategory
- name: AllowanceType
  property_count: 0
  slug: xero-allowancetype
- name: Amount
  property_count: 2
  slug: xero-amount
- name: APIException
  property_count: 3
  slug: xero-apiexception
- name: Asset
  property_count: 16
  slug: xero-asset
- name: AssetType
  property_count: 7
  slug: xero-asset-type
- name: Assets
  property_count: 2
  slug: xero-assets
- name: AssetStatus
  property_count: 0
  slug: xero-assetstatus
- name: AssetStatusQueryParam
  property_count: 0
  slug: xero-assetstatusqueryparam
- name: AssetType
  property_count: 7
  slug: xero-assettype
- name: Association
  property_count: 9
  slug: xero-association
- name: Attachment
  property_count: 6
  slug: xero-attachment
- name: Attachments
  property_count: 1
  slug: xero-attachments
- name: BalanceDetails
  property_count: 3
  slug: xero-balancedetails
- name: Balances
  property_count: 2
  slug: xero-balances
- name: BalanceSheetAccountDetail
  property_count: 5
  slug: xero-balancesheetaccountdetail
- name: BalanceSheetAccountGroup
  property_count: 2
  slug: xero-balancesheetaccountgroup
- name: BalanceSheetAccountType
  property_count: 3
  slug: xero-balancesheetaccounttype
- name: BalanceSheetResponse
  property_count: 4
  slug: xero-balancesheetresponse
- name: BankStatementAccountingResponse
  property_count: 4
  slug: xero-bank-statement-accounting-response
- name: BankAccount
  property_count: 6
  slug: xero-bankaccount
- name: BankAccounts
  property_count: 0
  slug: xero-bankaccounts
- name: BankStatementAccountingResponse
  property_count: 4
  slug: xero-bankstatementaccountingresponse
- name: BankStatementResponse
  property_count: 2
  slug: xero-bankstatementresponse
- name: BankTransaction
  property_count: 22
  slug: xero-banktransaction
- name: BankTransactionResponse
  property_count: 6
  slug: xero-banktransactionresponse
- name: BankTransactions
  property_count: 3
  slug: xero-banktransactions
- name: BankTransfer
  property_count: 14
  slug: xero-banktransfer
- name: BankTransfers
  property_count: 1
  slug: xero-banktransfers
- name: BatchPayment
  property_count: 17
  slug: xero-batchpayment
- name: BatchPaymentDelete
  property_count: 2
  slug: xero-batchpaymentdelete
- name: BatchPaymentDeleteByUrlParam
  property_count: 1
  slug: xero-batchpaymentdeletebyurlparam
- name: BatchPaymentDetails
  property_count: 5
  slug: xero-batchpaymentdetails
- name: BatchPayments
  property_count: 1
  slug: xero-batchpayments
- name: Benefit
  property_count: 10
  slug: xero-benefit
- name: BenefitLine
  property_count: 5
  slug: xero-benefitline
- name: BenefitLines
  property_count: 0
  slug: xero-benefitlines
- name: BenefitObject
  property_count: 3
  slug: xero-benefitobject
- name: Benefits
  property_count: 3
  slug: xero-benefits
- name: Bill
  property_count: 2
  slug: xero-bill
- name: BookDepreciationDetail
  property_count: 12
  slug: xero-bookdepreciationdetail
- name: BookDepreciationSetting
  property_count: 8
  slug: xero-bookdepreciationsetting
- name: BrandingTheme
  property_count: 6
  slug: xero-brandingtheme
- name: BrandingThemes
  property_count: 1
  slug: xero-brandingthemes
- name: Budget
  property_count: 6
  slug: xero-budget
- name: BudgetBalance
  property_count: 4
  slug: xero-budgetbalance
- name: BudgetLine
  property_count: 3
  slug: xero-budgetline
- name: Budgets
  property_count: 1
  slug: xero-budgets
- name: BulkFeedConnectionResponse
  property_count: 1
  slug: xero-bulk-feed-connection-response
- name: CalendarType
  property_count: 0
  slug: xero-calendartype
- name: CashValidationResponse
  property_count: 5
  slug: xero-cash-validation-response
- name: CashAccountResponse
  property_count: 5
  slug: xero-cashaccountresponse
- name: CashBalance
  property_count: 3
  slug: xero-cashbalance
- name: CashflowResponse
  property_count: 4
  slug: xero-cashflow-response
- name: CashflowAccount
  property_count: 7
  slug: xero-cashflowaccount
- name: CashflowActivity
  property_count: 3
  slug: xero-cashflowactivity
- name: CashflowResponse
  property_count: 4
  slug: xero-cashflowresponse
- name: CashflowType
  property_count: 3
  slug: xero-cashflowtype
- name: CashValidationResponse
  property_count: 5
  slug: xero-cashvalidationresponse
- name: ChargeType
  property_count: 0
  slug: xero-chargetype
- name: CISOrgSetting
  property_count: 3
  slug: xero-cisorgsetting
- name: CISOrgSettings
  property_count: 1
  slug: xero-cisorgsettings
- name: CISSetting
  property_count: 2
  slug: xero-cissetting
- name: CISSettings
  property_count: 1
  slug: xero-cissettings
- name: Connection
  property_count: 7
  slug: xero-connection
- name: Contact
  property_count: 43
  slug: xero-contact
- name: ContactDetail
  property_count: 6
  slug: xero-contactdetail
- name: ContactGroup
  property_count: 4
  slug: xero-contactgroup
- name: ContactGroups
  property_count: 1
  slug: xero-contactgroups
- name: ContactPerson
  property_count: 4
  slug: xero-contactperson
- name: ContactResponse
  property_count: 2
  slug: xero-contactresponse
- name: Contacts
  property_count: 3
  slug: xero-contacts
- name: ContactTotalDetail
  property_count: 3
  slug: xero-contacttotaldetail
- name: ContactTotalOther
  property_count: 4
  slug: xero-contacttotalother
- name: Contracts
  property_count: 7
  slug: xero-contracts
- name: ContractType
  property_count: 0
  slug: xero-contracttype
- name: ConversionBalances
  property_count: 3
  slug: xero-conversionbalances
- name: ConversionDate
  property_count: 2
  slug: xero-conversiondate
- name: CountryCode
  property_count: 0
  slug: xero-countrycode
- name: CountryOfResidence
  property_count: 0
  slug: xero-countryofresidence
- name: CourtOrderLine
  property_count: 2
  slug: xero-courtorderline
- name: CourtOrderLines
  property_count: 0
  slug: xero-courtorderlines
- name: CreditDebitIndicator
  property_count: 0
  slug: xero-creditdebitindicator
- name: CreditNote
  property_count: 31
  slug: xero-creditnote
- name: CreditNoteResponse
  property_count: 4
  slug: xero-creditnoteresponse
- name: CreditNotes
  property_count: 3
  slug: xero-creditnotes
- name: Currencies
  property_count: 1
  slug: xero-currencies
- name: Currency
  property_count: 2
  slug: xero-currency
- name: CurrencyCode
  property_count: 0
  slug: xero-currencycode
- name: CurrentStatementResponse
  property_count: 6
  slug: xero-currentstatementresponse
- name: DataSourceResponse
  property_count: 12
  slug: xero-datasourceresponse
- name: Deduction
  property_count: 6
  slug: xero-deduction
- name: DeductionLine
  property_count: 5
  slug: xero-deductionline
- name: DeductionLines
  property_count: 0
  slug: xero-deductionlines
- name: DeductionObject
  property_count: 3
  slug: xero-deductionobject
- name: Deductions
  property_count: 3
  slug: xero-deductions
- name: DeductionType
  property_count: 9
  slug: xero-deductiontype
- name: DeductionTypeCalculationType
  property_count: 0
  slug: xero-deductiontypecalculationtype
- name: DeleteFeedConnectionsRequest
  property_count: 1
  slug: xero-delete-feed-connections-request
- name: DevelopmentalRoleDetails
  property_count: 4
  slug: xero-developmentalroledetails
- name: EarningsRate
  property_count: 10
  slug: xero-earnings-rate
- name: EarningsLine
  property_count: 9
  slug: xero-earningsline
- name: EarningsLines
  property_count: 0
  slug: xero-earningslines
- name: EarningsOrder
  property_count: 5
  slug: xero-earningsorder
- name: EarningsOrderObject
  property_count: 3
  slug: xero-earningsorderobject
- name: EarningsOrders
  property_count: 3
  slug: xero-earningsorders
- name: EarningsRate
  property_count: 21
  slug: xero-earningsrate
- name: EarningsRateCalculationType
  property_count: 0
  slug: xero-earningsratecalculationtype
- name: EarningsRateObject
  property_count: 3
  slug: xero-earningsrateobject
- name: EarningsRates
  property_count: 3
  slug: xero-earningsrates
- name: EarningsTemplate
  property_count: 6
  slug: xero-earningstemplate
- name: EarningsTemplateObject
  property_count: 3
  slug: xero-earningstemplateobject
- name: EarningsTemplates
  property_count: 0
  slug: xero-earningstemplates
- name: EarningsType
  property_count: 0
  slug: xero-earningstype
- name: Element
  property_count: 8
  slug: xero-element
- name: EmployeeLeaveSetup
  property_count: 10
  slug: xero-employee-leave-setup
- name: EmployeeLeaveType
  property_count: 13
  slug: xero-employee-leave-type
- name: Employee
  property_count: 8
  slug: xero-employee
- name: EmployeeStatutorySickLeave
  property_count: 16
  slug: xero-employee-statutory-sick-leave
- name: EmployeeTax
  property_count: 16
  slug: xero-employee-tax
- name: EmployeeEarningsTemplates
  property_count: 3
  slug: xero-employeeearningstemplates
- name: EmployeeLeave
  property_count: 7
  slug: xero-employeeleave
- name: EmployeeLeaveBalance
  property_count: 4
  slug: xero-employeeleavebalance
- name: EmployeeLeaveBalances
  property_count: 3
  slug: xero-employeeleavebalances
- name: EmployeeLeaveObject
  property_count: 3
  slug: xero-employeeleaveobject
- name: EmployeeLeaves
  property_count: 3
  slug: xero-employeeleaves
- name: EmployeeLeaveSetup
  property_count: 10
  slug: xero-employeeleavesetup
- name: EmployeeLeaveSetupObject
  property_count: 3
  slug: xero-employeeleavesetupobject
- name: EmployeeLeaveType
  property_count: 13
  slug: xero-employeeleavetype
- name: EmployeeLeaveTypeObject
  property_count: 3
  slug: xero-employeeleavetypeobject
- name: EmployeeLeaveTypes
  property_count: 3
  slug: xero-employeeleavetypes
- name: EmployeeObject
  property_count: 3
  slug: xero-employeeobject
- name: EmployeeOpeningBalance
  property_count: 4
  slug: xero-employeeopeningbalance
- name: EmployeeOpeningBalances
  property_count: 0
  slug: xero-employeeopeningbalances
- name: EmployeeOpeningBalancesObject
  property_count: 3
  slug: xero-employeeopeningbalancesobject
- name: EmployeePayTemplate
  property_count: 2
  slug: xero-employeepaytemplate
- name: EmployeePayTemplateObject
  property_count: 3
  slug: xero-employeepaytemplateobject
- name: EmployeePayTemplates
  property_count: 3
  slug: xero-employeepaytemplates
- name: Employees
  property_count: 1
  slug: xero-employees
- name: EmployeeStatus
  property_count: 0
  slug: xero-employeestatus
- name: EmployeeStatutoryLeaveBalance
  property_count: 3
  slug: xero-employeestatutoryleavebalance
- name: EmployeeStatutoryLeaveBalanceObject
  property_count: 3
  slug: xero-employeestatutoryleavebalanceobject
- name: EmployeeStatutoryLeavesSummaries
  property_count: 3
  slug: xero-employeestatutoryleavessummaries
- name: EmployeeStatutoryLeaveSummary
  property_count: 7
  slug: xero-employeestatutoryleavesummary
- name: EmployeeStatutorySickLeave
  property_count: 16
  slug: xero-employeestatutorysickleave
- name: EmployeeStatutorySickLeaveObject
  property_count: 3
  slug: xero-employeestatutorysickleaveobject
- name: EmployeeStatutorySickLeaves
  property_count: 3
  slug: xero-employeestatutorysickleaves
- name: EmployeeTax
  property_count: 16
  slug: xero-employeetax
- name: EmployeeTaxObject
  property_count: 3
  slug: xero-employeetaxobject
- name: EmployeeWorkingPattern
  property_count: 2
  slug: xero-employeeworkingpattern
- name: EmployeeWorkingPatterns
  property_count: 0
  slug: xero-employeeworkingpatterns
- name: EmployeeWorkingPatternsObject
  property_count: 3
  slug: xero-employeeworkingpatternsobject
- name: EmployeeWorkingPatternWithWorkingWeeks
  property_count: 3
  slug: xero-employeeworkingpatternwithworkingweeks
- name: EmployeeWorkingPatternWithWorkingWeeksObject
  property_count: 3
  slug: xero-employeeworkingpatternwithworkingweeksobject
- name: EmployeeWorkingPatternWithWorkingWeeksRequest
  property_count: 2
  slug: xero-employeeworkingpatternwithworkingweeksrequest
- name: Employment
  property_count: 5
  slug: xero-employment
- name: EmploymentBasis
  property_count: 0
  slug: xero-employmentbasis
- name: EmploymentObject
  property_count: 3
  slug: xero-employmentobject
- name: EmploymentStatus
  property_count: 0
  slug: xero-employmentstatus
- name: EmploymentTerminationPaymentType
  property_count: 0
  slug: xero-employmentterminationpaymenttype
- name: EmploymentType
  property_count: 0
  slug: xero-employmenttype
- name: EndBalance
  property_count: 2
  slug: xero-endbalance
- name: EntitlementFinalPayPayoutType
  property_count: 0
  slug: xero-entitlementfinalpaypayouttype
- name: Error
  property_count: 4
  slug: xero-error
- name: ExistingAccountFeedConnectionsRequest
  property_count: 1
  slug: xero-existing-account-feed-connections-request
- name: ExpenseClaim
  property_count: 12
  slug: xero-expenseclaim
- name: ExpenseClaims
  property_count: 1
  slug: xero-expenseclaims
- name: ExternalLink
  property_count: 3
  slug: xero-externallink
- name: FeedConnection
  property_count: 10
  slug: xero-feed-connection
- name: FeedConnections
  property_count: 2
  slug: xero-feed-connections
- name: FeedConnection
  property_count: 10
  slug: xero-feedconnection
- name: FeedConnections
  property_count: 2
  slug: xero-feedconnections
- name: FieldValidationErrorsElement
  property_count: 6
  slug: xero-fieldvalidationerrorselement
- name: FileObject
  property_count: 8
  slug: xero-file-object
- name: FileObject
  property_count: 8
  slug: xero-fileobject
- name: Files
  property_count: 4
  slug: xero-files
- name: Folder
  property_count: 5
  slug: xero-folder
- name: Folders
  property_count: 1
  slug: xero-folders
- name: GrossEarningsHistory
  property_count: 2
  slug: xero-grossearningshistory
- name: HistoryRecord
  property_count: 4
  slug: xero-historyrecord
- name: HistoryRecords
  property_count: 1
  slug: xero-historyrecords
- name: HomeAddress
  property_count: 6
  slug: xero-homeaddress
- name: ImportSummary
  property_count: 2
  slug: xero-importsummary
- name: ImportSummaryAccounts
  property_count: 9
  slug: xero-importsummaryaccounts
- name: ImportSummaryObject
  property_count: 1
  slug: xero-importsummaryobject
- name: ImportSummaryOrganisation
  property_count: 1
  slug: xero-importsummaryorganisation
- name: IncomeByContactResponse
  property_count: 7
  slug: xero-income-by-contact-response
- name: IncomeByContactResponse
  property_count: 7
  slug: xero-incomebycontactresponse
- name: IncomeType
  property_count: 0
  slug: xero-incometype
- name: InvalidField
  property_count: 2
  slug: xero-invalidfield
- name: Invoice
  property_count: 41
  slug: xero-invoice
- name: InvoiceAddress
  property_count: 9
  slug: xero-invoiceaddress
- name: InvoiceReminder
  property_count: 1
  slug: xero-invoicereminder
- name: InvoiceReminders
  property_count: 1
  slug: xero-invoicereminders
- name: InvoiceResponse
  property_count: 4
  slug: xero-invoiceresponse
- name: Invoices
  property_count: 3
  slug: xero-invoices
- name: Item
  property_count: 16
  slug: xero-item
- name: Items
  property_count: 1
  slug: xero-items
- name: Journal
  property_count: 8
  slug: xero-journal
- name: JournalLine
  property_count: 12
  slug: xero-journalline
- name: Journals
  property_count: 2
  slug: xero-journals
- name: LeaveApplication
  property_count: 11
  slug: xero-leave-application
- name: LeaveAccrualLine
  property_count: 3
  slug: xero-leaveaccrualline
- name: LeaveAccrualLines
  property_count: 0
  slug: xero-leaveaccruallines
- name: LeaveApplication
  property_count: 11
  slug: xero-leaveapplication
- name: LeaveApplications
  property_count: 1
  slug: xero-leaveapplications
- name: LeaveBalance
  property_count: 4
  slug: xero-leavebalance
- name: LeaveCategoryCode
  property_count: 0
  slug: xero-leavecategorycode
- name: LeaveEarningsLine
  property_count: 4
  slug: xero-leaveearningsline
- name: LeaveEarningsLines
  property_count: 0
  slug: xero-leaveearningslines
- name: LeaveLine
  property_count: 9
  slug: xero-leaveline
- name: LeaveLineCalculationType
  property_count: 0
  slug: xero-leavelinecalculationtype
- name: LeaveLines
  property_count: 1
  slug: xero-leavelines
- name: LeavePeriod
  property_count: 4
  slug: xero-leaveperiod
- name: LeavePeriods
  property_count: 3
  slug: xero-leaveperiods
- name: LeavePeriodStatus
  property_count: 0
  slug: xero-leaveperiodstatus
- name: LeaveType
  property_count: 12
  slug: xero-leavetype
- name: LeaveTypeContributionType
  property_count: 0
  slug: xero-leavetypecontributiontype
- name: LeaveTypeObject
  property_count: 3
  slug: xero-leavetypeobject
- name: LeaveTypes
  property_count: 3
  slug: xero-leavetypes
- name: LineAmountTypes
  property_count: 0
  slug: xero-lineamounttypes
- name: LineItem
  property_count: 18
  slug: xero-lineitem
- name: LineItemItem
  property_count: 3
  slug: xero-lineitemitem
- name: LineItemResponse
  property_count: 4
  slug: xero-lineitemresponse
- name: LineItemTracking
  property_count: 4
  slug: xero-lineitemtracking
- name: LinkedTransaction
  property_count: 11
  slug: xero-linked-transaction
- name: LinkedTransaction
  property_count: 11
  slug: xero-linkedtransaction
- name: LinkedTransactions
  property_count: 1
  slug: xero-linkedtransactions
- name: ManualJournal
  property_count: 14
  slug: xero-manualjournal
- name: ManualJournalLine
  property_count: 8
  slug: xero-manualjournalline
- name: ManualJournals
  property_count: 3
  slug: xero-manualjournals
- name: ManualJournalTotal
  property_count: 1
  slug: xero-manualjournaltotal
- name: ManualTaxType
  property_count: 0
  slug: xero-manualtaxtype
- name: NewAccountFeedConnectionsRequest
  property_count: 1
  slug: xero-new-account-feed-connections-request
- name: NICategory
  property_count: 5
  slug: xero-nicategory
- name: NICategoryLetter
  property_count: 0
  slug: xero-nicategoryletter
- name: ObjectGroup
  property_count: 0
  slug: xero-objectgroup
- name: ObjectType
  property_count: 0
  slug: xero-objecttype
- name: OnlineInvoice
  property_count: 1
  slug: xero-onlineinvoice
- name: OnlineInvoices
  property_count: 1
  slug: xero-onlineinvoices
- name: OpeningBalanceLeaveLine
  property_count: 2
  slug: xero-openingbalanceleaveline
- name: OpeningBalances
  property_count: 8
  slug: xero-openingbalances
- name: Organisation
  property_count: 33
  slug: xero-organisation
- name: Organisations
  property_count: 1
  slug: xero-organisations
- name: Overpayment
  property_count: 20
  slug: xero-overpayment
- name: OverpaymentResponse
  property_count: 4
  slug: xero-overpaymentresponse
- name: Overpayments
  property_count: 3
  slug: xero-overpayments
- name: PagedFeedConnections
  property_count: 2
  slug: xero-paged-feed-connections
- name: Pagination
  property_count: 4
  slug: xero-pagination
- name: PaidLeaveEarningsLine
  property_count: 5
  slug: xero-paidleaveearningsline
- name: PayRun
  property_count: 16
  slug: xero-pay-run
- name: PaySlip
  property_count: 30
  slug: xero-pay-slip
- name: PayItem
  property_count: 4
  slug: xero-payitem
- name: PayItems
  property_count: 1
  slug: xero-payitems
- name: Payment
  property_count: 28
  slug: xero-payment
- name: PaymentDelete
  property_count: 1
  slug: xero-paymentdelete
- name: PaymentFrequencyType
  property_count: 0
  slug: xero-paymentfrequencytype
- name: PaymentLine
  property_count: 5
  slug: xero-paymentline
- name: PaymentLines
  property_count: 0
  slug: xero-paymentlines
- name: PaymentMethod
  property_count: 2
  slug: xero-paymentmethod
- name: PaymentMethodObject
  property_count: 3
  slug: xero-paymentmethodobject
- name: PaymentResponse
  property_count: 10
  slug: xero-paymentresponse
- name: Payments
  property_count: 3
  slug: xero-payments
- name: PaymentService
  property_count: 6
  slug: xero-paymentservice
- name: PaymentServices
  property_count: 1
  slug: xero-paymentservices
- name: PaymentTerm
  property_count: 2
  slug: xero-paymentterm
- name: PaymentTermType
  property_count: 0
  slug: xero-paymenttermtype
- name: PayOutType
  property_count: 0
  slug: xero-payouttype
- name: PayrollCalendar
  property_count: 8
  slug: xero-payroll-calendar
- name: PayrollCalendar
  property_count: 8
  slug: xero-payrollcalendar
- name: PayrollCalendars
  property_count: 1
  slug: xero-payrollcalendars
- name: PayRun
  property_count: 16
  slug: xero-payrun
- name: PayRunCalendar
  property_count: 7
  slug: xero-payruncalendar
- name: PayRunCalendarObject
  property_count: 3
  slug: xero-payruncalendarobject
- name: PayRunCalendars
  property_count: 3
  slug: xero-payruncalendars
- name: PayRunObject
  property_count: 3
  slug: xero-payrunobject
- name: PayRuns
  property_count: 1
  slug: xero-payruns
- name: PayRunStatus
  property_count: 0
  slug: xero-payrunstatus
- name: Payslip
  property_count: 19
  slug: xero-payslip
- name: PayslipLines
  property_count: 8
  slug: xero-paysliplines
- name: PayslipObject
  property_count: 1
  slug: xero-payslipobject
- name: Payslips
  property_count: 1
  slug: xero-payslips
- name: PayslipSummary
  property_count: 12
  slug: xero-payslipsummary
- name: PayTemplate
  property_count: 5
  slug: xero-paytemplate
- name: Phone
  property_count: 4
  slug: xero-phone
- name: PnlAccount
  property_count: 6
  slug: xero-pnlaccount
- name: PnlAccountClass
  property_count: 2
  slug: xero-pnlaccountclass
- name: PnlAccountType
  property_count: 3
  slug: xero-pnlaccounttype
- name: Prepayment
  property_count: 21
  slug: xero-prepayment
- name: PrepaymentResponse
  property_count: 4
  slug: xero-prepaymentresponse
- name: Prepayments
  property_count: 3
  slug: xero-prepayments
- name: Problem
  property_count: 4
  slug: xero-problem
- name: ProblemType
  property_count: 0
  slug: xero-problemtype
- name: ProfitAndLossResponse
  property_count: 5
  slug: xero-profit-and-loss-response
- name: ProfitAndLossResponse
  property_count: 5
  slug: xero-profitandlossresponse
- name: ProjectCreateOrUpdate
  property_count: 4
  slug: xero-project-create-or-update
- name: Project
  property_count: 22
  slug: xero-project
- name: ProjectCreateOrUpdate
  property_count: 4
  slug: xero-projectcreateorupdate
- name: ProjectPatch
  property_count: 1
  slug: xero-projectpatch
- name: Projects
  property_count: 2
  slug: xero-projects
- name: ProjectStatus
  property_count: 0
  slug: xero-projectstatus
- name: ProjectUser
  property_count: 3
  slug: xero-projectuser
- name: ProjectUsers
  property_count: 2
  slug: xero-projectusers
- name: Purchase
  property_count: 4
  slug: xero-purchase
- name: PurchaseOrder
  property_count: 28
  slug: xero-purchaseorder
- name: PurchaseOrders
  property_count: 3
  slug: xero-purchaseorders
- name: Quote
  property_count: 24
  slug: xero-quote
- name: QuoteLineAmountTypes
  property_count: 0
  slug: xero-quotelineamounttypes
- name: Quotes
  property_count: 1
  slug: xero-quotes
- name: QuoteStatusCodes
  property_count: 0
  slug: xero-quotestatuscodes
- name: RateType
  property_count: 0
  slug: xero-ratetype
- name: Receipt
  property_count: 18
  slug: xero-receipt
- name: Receipts
  property_count: 1
  slug: xero-receipts
- name: RefreshToken
  property_count: 4
  slug: xero-refreshtoken
- name: Reimbursement
  property_count: 9
  slug: xero-reimbursement
- name: ReimbursementLine
  property_count: 4
  slug: xero-reimbursementline
- name: ReimbursementLines
  property_count: 1
  slug: xero-reimbursementlines
- name: ReimbursementObject
  property_count: 3
  slug: xero-reimbursementobject
- name: Reimbursements
  property_count: 3
  slug: xero-reimbursements
- name: ReimbursementType
  property_count: 5
  slug: xero-reimbursementtype
- name: RepeatingInvoice
  property_count: 20
  slug: xero-repeatinginvoice
- name: RepeatingInvoices
  property_count: 1
  slug: xero-repeatinginvoices
- name: Report
  property_count: 6
  slug: xero-report
- name: ReportAttribute
  property_count: 2
  slug: xero-reportattribute
- name: ReportCell
  property_count: 2
  slug: xero-reportcell
- name: ReportFields
  property_count: 3
  slug: xero-reportfields
- name: ReportRow
  property_count: 3
  slug: xero-reportrow
- name: ReportRows
  property_count: 4
  slug: xero-reportrows
- name: Reports
  property_count: 1
  slug: xero-reports
- name: ReportWithRow
  property_count: 9
  slug: xero-reportwithrow
- name: ReportWithRows
  property_count: 1
  slug: xero-reportwithrows
- name: RequestEmpty
  property_count: 1
  slug: xero-requestempty
- name: ResidencyStatus
  property_count: 0
  slug: xero-residencystatus
- name: ResourceValidationErrorsElement
  property_count: 5
  slug: xero-resourcevalidationerrorselement
- name: RowType
  property_count: 0
  slug: xero-rowtype
- name: SalaryAndWage
  property_count: 9
  slug: xero-salary-and-wage
- name: SalaryAndWage
  property_count: 11
  slug: xero-salaryandwage
- name: SalaryAndWageObject
  property_count: 3
  slug: xero-salaryandwageobject
- name: SalaryAndWages
  property_count: 3
  slug: xero-salaryandwages
- name: SalesTrackingCategory
  property_count: 2
  slug: xero-salestrackingcategory
- name: Schedule
  property_count: 7
  slug: xero-schedule
- name: SeniorMaritalStatus
  property_count: 0
  slug: xero-seniormaritalstatus
- name: Setting
  property_count: 8
  slug: xero-setting
- name: Settings
  property_count: 4
  slug: xero-settings
- name: SettingsObject
  property_count: 1
  slug: xero-settingsobject
- name: Setup
  property_count: 3
  slug: xero-setup
- name: StartBalance
  property_count: 2
  slug: xero-startbalance
- name: State
  property_count: 0
  slug: xero-state
- name: Statement
  property_count: 10
  slug: xero-statement
- name: StatementBalanceResponse
  property_count: 2
  slug: xero-statementbalanceresponse
- name: StatementLine
  property_count: 9
  slug: xero-statementline
- name: StatementLineResponse
  property_count: 14
  slug: xero-statementlineresponse
- name: StatementLines
  property_count: 0
  slug: xero-statementlines
- name: StatementLinesResponse
  property_count: 17
  slug: xero-statementlinesresponse
- name: StatementResponse
  property_count: 10
  slug: xero-statementresponse
- name: Statements
  property_count: 2
  slug: xero-statements
- name: StatutoryDeduction
  property_count: 5
  slug: xero-statutorydeduction
- name: StatutoryDeductionCategory
  property_count: 0
  slug: xero-statutorydeductioncategory
- name: StatutoryDeductionLine
  property_count: 4
  slug: xero-statutorydeductionline
- name: StatutoryDeductionLines
  property_count: 0
  slug: xero-statutorydeductionlines
- name: StatutoryDeductionObject
  property_count: 3
  slug: xero-statutorydeductionobject
- name: StatutoryDeductions
  property_count: 3
  slug: xero-statutorydeductions
- name: Subscription
  property_count: 8
  slug: xero-subscription
- name: SuperFund
  property_count: 13
  slug: xero-super-fund
- name: SuperannuationCalculationType
  property_count: 0
  slug: xero-superannuationcalculationtype
- name: SuperannuationContributionType
  property_count: 0
  slug: xero-superannuationcontributiontype
- name: SuperannuationLine
  property_count: 9
  slug: xero-superannuationline
- name: SuperannuationLines
  property_count: 0
  slug: xero-superannuationlines
- name: SuperannuationObject
  property_count: 3
  slug: xero-superannuationobject
- name: Superannuations
  property_count: 3
  slug: xero-superannuations
- name: SuperFund
  property_count: 13
  slug: xero-superfund
- name: SuperFundProduct
  property_count: 4
  slug: xero-superfundproduct
- name: SuperFundProducts
  property_count: 1
  slug: xero-superfundproducts
- name: SuperFunds
  property_count: 1
  slug: xero-superfunds
- name: SuperFundType
  property_count: 0
  slug: xero-superfundtype
- name: SuperLine
  property_count: 8
  slug: xero-superline
- name: SuperMembership
  property_count: 3
  slug: xero-supermembership
- name: TaskCreateOrUpdate
  property_count: 4
  slug: xero-task-create-or-update
- name: Task
  property_count: 15
  slug: xero-task
- name: TaskCreateOrUpdate
  property_count: 4
  slug: xero-taskcreateorupdate
- name: Tasks
  property_count: 2
  slug: xero-tasks
- name: TaxBreakdownComponent
  property_count: 10
  slug: xero-taxbreakdowncomponent
- name: TaxCode
  property_count: 0
  slug: xero-taxcode
- name: TaxComponent
  property_count: 4
  slug: xero-taxcomponent
- name: TaxDeclaration
  property_count: 22
  slug: xero-taxdeclaration
- name: TaxLine
  property_count: 6
  slug: xero-taxline
- name: TaxLines
  property_count: 0
  slug: xero-taxlines
- name: TaxRate
  property_count: 12
  slug: xero-taxrate
- name: TaxRates
  property_count: 1
  slug: xero-taxrates
- name: TaxScaleType
  property_count: 0
  slug: xero-taxscaletype
- name: TaxSettings
  property_count: 6
  slug: xero-taxsettings
- name: TaxType
  property_count: 0
  slug: xero-taxtype
- name: TenNinetyNineContact
  property_count: 25
  slug: xero-tenninetyninecontact
- name: TFNExemptionType
  property_count: 0
  slug: xero-tfnexemptiontype
- name: TimeEntryCreateOrUpdate
  property_count: 5
  slug: xero-time-entry-create-or-update
- name: TimeEntry
  property_count: 9
  slug: xero-time-entry
- name: TimeEntries
  property_count: 2
  slug: xero-timeentries
- name: TimeEntry
  property_count: 9
  slug: xero-timeentry
- name: TimeEntryCreateOrUpdate
  property_count: 5
  slug: xero-timeentrycreateorupdate
- name: TimesheetLineObject
  property_count: 3
  slug: xero-timesheet-line-object
- name: TimesheetLine
  property_count: 5
  slug: xero-timesheet-line
- name: TimesheetObject
  property_count: 3
  slug: xero-timesheet-object
- name: Timesheet
  property_count: 9
  slug: xero-timesheet
- name: TimesheetEarningsLine
  property_count: 10
  slug: xero-timesheetearningsline
- name: TimesheetEarningsLines
  property_count: 0
  slug: xero-timesheetearningslines
- name: TimesheetLine
  property_count: 4
  slug: xero-timesheetline
- name: TimesheetLineObject
  property_count: 3
  slug: xero-timesheetlineobject
- name: TimesheetLines
  property_count: 0
  slug: xero-timesheetlines
- name: TimesheetObject
  property_count: 1
  slug: xero-timesheetobject
- name: Timesheets
  property_count: 1
  slug: xero-timesheets
- name: TimesheetStatus
  property_count: 0
  slug: xero-timesheetstatus
- name: TimeZone
  property_count: 0
  slug: xero-timezone
- name: TotalDetail
  property_count: 3
  slug: xero-totaldetail
- name: TotalOther
  property_count: 3
  slug: xero-totalother
- name: TrackingCategory
  property_count: 6
  slug: xero-tracking-category
- name: TrackingOption
  property_count: 4
  slug: xero-tracking-option
- name: TrackingCategories
  property_count: 1
  slug: xero-trackingcategories
- name: TrackingCategory
  property_count: 6
  slug: xero-trackingcategory
- name: TrackingOption
  property_count: 4
  slug: xero-trackingoption
- name: TrackingOptions
  property_count: 1
  slug: xero-trackingoptions
- name: TrialBalanceResponse
  property_count: 3
  slug: xero-trial-balance-response
- name: TrialBalanceAccount
  property_count: 10
  slug: xero-trialbalanceaccount
- name: TrialBalanceEntry
  property_count: 2
  slug: xero-trialbalanceentry
- name: TrialBalanceMovement
  property_count: 4
  slug: xero-trialbalancemovement
- name: TrialBalanceResponse
  property_count: 3
  slug: xero-trialbalanceresponse
- name: UploadObject
  property_count: 4
  slug: xero-upload-object
- name: UploadObject
  property_count: 4
  slug: xero-uploadobject
- name: User
  property_count: 7
  slug: xero-user
- name: Users
  property_count: 1
  slug: xero-users
- name: ValidationError
  property_count: 1
  slug: xero-validationerror
- name: WorkCondition
  property_count: 0
  slug: xero-workcondition
- name: WorkingWeek
  property_count: 7
  slug: xero-workingweek
- name: WorkingWeeks
  property_count: 0
  slug: xero-workingweeks
json_structures:
- name: Xero Structure
  property_count: 0
  slug: xero-structure
jsonld:
- class_count: 120
  name: Xero Context
  property_count: 352
  slug: xero-context
layout: provider
mcp_servers:
- description: ''
  name: Xero MCP Server
  slug: xero-mcp-server
modified: '2026-10-20'
name: Xero
nav: Providers
network: true
overview: 'Xero publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounting API, Asset API, Files API, and 11 more. Tagged areas include Accounting, Bank Feeds, Finance, Financial Services, and Invoicing.


  The Xero catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 4 Spectral governance rulesets.


  Xero''s developer surface includes CLI, changelog, sandbox, signup flow, authentication, developer portal, documentation, and 57 more developer resources.'
plans:
- name: Xero Plans Pricing
  plan_count: 5
  slug: xero-plans-pricing
- name: Xero Price Estimates
  plan_count: 0
  slug: xero-price-estimates
random_paper: 14
rate_limits:
- limit_count: 7
  name: Xero Rate Limits
  slug: xero-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Xero — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: xero-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Xero — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: xero-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Xero API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: xero-rules
- authorship: provider
  effective_rule_count: 56
  extends:
  - spectral:oas
  - '@stoplight/spectral-owasp-ruleset'
  name: Xero — xero openapi rules
  rule_count: 15
  severity_counts:
    error: 6
    warn: 6
    info: 2
    hint: 0
    false: 1
  slug: xero-xero-openapi-spectral-rules
scopes:
- name: Xero Scopes
  scope_count: 68
  slug: xero-scopes
  summary_line: 68 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 82.4
  coverage:
    artifact_dirs: 42
    catalog_earned: 109.5
    catalog_earned_first_party: 42.0
    catalog_gap: 5.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 72.4
    contract_governance: 86.4
    contract_quality: 75.7
    developer_ergonomics: 79.2
    discoverability: 81.7
    operational_transparency: 82.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 85.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 46.2
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/xero/xero-2026-06-20T201700.png
security:
- kind: authentication
  name: Xero Authentication
  slug: xero-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Xero Domain Security
  slug: xero-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: xero-invoice-a-customer-and-record-payment
  slug: xero-invoice-a-customer-and-record-payment
- name: xero-month-end-financial-reports
  slug: xero-month-end-financial-reports
- name: xero-nz-payroll-timesheet
  slug: xero-nz-payroll-timesheet
- name: xero-record-and-correct-bank-transactions
  slug: xero-record-and-correct-bank-transactions
slug: xero
tags:
- Accounting
- Bank Feeds
- Finance
- Financial Services
- Invoicing
- Payroll
- Small Business
website: https://www.xero.com/
---
