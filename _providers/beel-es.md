---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 82.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 154
  human_in_the_loop: 2
  name: Beel Es Agentic Access
  operation_count: 244
  slug: beel-es-agentic-access
  summary_line: 244 operations · 154 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Listing and creating the NIFs of an account, under `/v1/accounts/{account_id}/companies`. Operating on one NIF is the `Company` resource.
  name: beel-es Account Companies API
  slug: beel-es-accountcompanies-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: The domains an account sends its emails from, addressed by `/v1/accounts/{account_id}/email-domains`. The account in the path is the only source of context, instead of being derived from the credentia
  name: beel-es Account Email Domains API
  slug: beel-es-accountemaildomains-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: The sent-email history of an account, addressed by `/v1/accounts/{account_id}/emails` and `/v1/accounts/{account_id}/email-indicators`. The account in the path is the only source of context, instead o
  name: beel-es Account Emails API
  slug: beel-es-accountemails-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'Onboarding managed accounts in bulk from a file, addressed by `/v1/accounts/imports`. The file is declarative and the import is re-runnable: each pass applies only what is missing, and previewing is a'
  name: beel-es Account Imports API
  slug: beel-es-accountimports-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'Canonical form of the request logs, addressed by `/v1/accounts/{account_id}/request-logs`. The account in the path authorizes the call; the logs returned are always the requests made by you, with any '
  name: beel-es Account Request Logs API
  slug: beel-es-accountrequestlogs-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'Account provisioning for partners managing multiple accounts and NIFs. The whole onboarding flow — provisioning, claim tokens and usage — works with either API key: the account is born inert (no NIF s'
  name: beel-es Accounts API
  slug: beel-es-accounts-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Outbound webhook subscriptions as a sub-resource of the account itself, addressed by `/v1/accounts/{account_id}/webhooks`. The account in the path is the only source of context — the credential does n
  name: beel-es Account Webhooks API
  slug: beel-es-accountwebhooks-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The company as a resource of its own, addressed by `/v1/companies/{company_id}`. The NIF in the path is the only source of context: the account that owns it is derived from it.'
  name: beel-es Company API
  slug: beel-es-company-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'Switching a company on or off in Test or Live, as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/activations`. The NIF in the path is the only source of context: the ac'
  name: beel-es Company Activations API
  slug: beel-es-companyactivations-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: The invoice branding of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/logo` and `/v1/companies/{company_id}/invoice-customization`. The NIF in the path is
  name: beel-es Company Branding API
  slug: beel-es-companybranding-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Importing customers into a company, addressed by `/v1/companies/{company_id}/customers/imports`. The origin of the file travels in the body as `source`, so adding an origin never adds a route, and pre
  name: beel-es Company Customer Imports API
  slug: beel-es-companycustomerimports-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The customers of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/customers`. The NIF in the path is the only source of context: the account that owns it is '
  name: beel-es Company Customers API
  slug: beel-es-companycustomers-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The invoice custom fields of a company, addressed by `/v1/companies/{company_id}/custom-fields`: labels a company adds to its invoices, such as a store, a project or a cost centre, so that people can '
  name: beel-es Company Custom Fields API
  slug: beel-es-companycustomfields-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The email configuration of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/email-configuration`. It sets the address the invoice emails of that company are '
  name: beel-es Company Email Configuration API
  slug: beel-es-companyemailconfiguration-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The fiscal summary of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/fiscal-summary`. The NIF in the path is the only source of context: the account that o'
  name: beel-es Company Fiscal Summary API
  slug: beel-es-companyfiscalsummary-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Delivery, bulk operations and exports of a NIF's invoices (send, deliveries, batches, exports, PDF archive), under `/v1/companies/{company_id}/invoices/...`. Canonical form of `InvoiceDelivery`.
  name: beel-es Company Invoice Delivery API
  slug: beel-es-companyinvoicedelivery-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: State transitions and scheduling of a NIF's invoices (issue, void, corrective, status, schedule), under `/v1/companies/{company_id}/invoices/{invoice_id}/...`. Canonical form of `InvoiceLifecycle`.
  name: beel-es Company Invoice Lifecycle API
  slug: beel-es-companyinvoicelifecycle-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The invoices of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/invoices`. The NIF in the path is the only source of context: the account that owns it is de'
  name: beel-es Company Invoices API
  slug: beel-es-companyinvoices-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The payment provider connections of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/payment-connections`. The NIF in the path is the only source of context:'
  name: beel-es Company Payment Connections API
  slug: beel-es-companypaymentconnections-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The payment events of a company connection, addressed by `/v1/companies/{company_id}/payment-connections/{connection_id}/events`. The NIF in the path is the only source of context: the account that ow'
  name: beel-es Company Payment Events API
  slug: beel-es-companypaymentevents-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The product/service catalog of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/products`. The NIF in the path is the only source of context: the account tha'
  name: beel-es Company Products API
  slug: beel-es-companyproducts-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Converting a NIF's proforma into a fiscal invoice (`POST /v1/companies/{company_id}/invoices/{invoice_id}/convert-to-invoice`). The rest of the proforma workflow happens through the regular `CompanyIn
  name: beel-es Company Proforma API
  slug: beel-es-companyproforma-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The recurring invoice templates of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/recurring-invoices`. The NIF in the path is the only source of context: t'
  name: beel-es Company Recurring Invoices API
  slug: beel-es-companyrecurringinvoices-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The AEAT fiscal representation of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/representation`. The NIF in the path is the only source of context: the ac'
  name: beel-es Company Representation API
  slug: beel-es-companyrepresentation-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: The invoice series of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/series`. The NIF in the path is the only source of context. It is the canonical form o
  name: beel-es Company Series API
  slug: beel-es-companyseries-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: The tax configuration of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/tax-configuration`. The NIF in the path is the only source of context. It is the ca
  name: beel-es Company Tax Configuration API
  slug: beel-es-companytaxconfiguration-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'The VeriFactu configuration of a company as a sub-resource of the company itself, addressed by `/v1/companies/{company_id}/verifactu-configuration`. The NIF in the path is the only source of context. '
  name: beel-es Company Veri Factu Configuration API
  slug: beel-es-companyverifactuconfiguration-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: User language preferences
  name: beel-es Configuration Preferences API
  slug: beel-es-configurationpreferences-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Tax configuration and tax type catalogs
  name: beel-es Configuration Tax API
  slug: beel-es-configurationtax-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: VeriFactu compliance configuration
  name: beel-es Configuration Veri Factu API
  slug: beel-es-configurationverifactu-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Bulk creation, CSV import, and Holded import operations
  name: beel-es Customer Import API
  slug: beel-es-customer-import-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Templates and sample files for customer imports
  name: beel-es Customer Templates API
  slug: beel-es-customer-templates-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Customer management
  name: beel-es Customers API
  slug: beel-es-customers-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: History of emails the system has sent on your behalf (invoices, verification, onboarding, etc.). Read-only.
  name: beel-es Emails API
  slug: beel-es-emails-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: The variables the email templates accept, addressed by `/v1/email-template-variables`. The catalogue is the same for every credential and takes no identifier.
  name: beel-es Email Template Variables API
  slug: beel-es-emailtemplatevariables-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'Who am I (`GET /v1/me`): the authenticated principal — credential type, environment it operates on and the permissions it holds — so a client can adapt what it offers instead of discovering the limits'
  name: beel-es Identity API
  slug: beel-es-identity-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'Member invitations — invite people to the account and revoke pending invites (multi-NIF). Like members, invitations are **shared between Test and Live**: accepting one grants real access, so creating '
  name: beel-es Invitations API
  slug: beel-es-invitations-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: The PDF templates a NIF can be rendered with, each one with a readable, translated name. The same for every account.
  name: beel-es Invoice Customization API
  slug: beel-es-invoicecustomization-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Invoice delivery, bulk operations and exports
  name: beel-es Invoice Delivery API
  slug: beel-es-invoicedelivery-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Invoice state transitions and scheduling
  name: beel-es Invoice Lifecycle API
  slug: beel-es-invoicelifecycle-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Invoice CRUD operations
  name: beel-es Invoices API
  slug: beel-es-invoices-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Invoice series management
  name: beel-es Invoice Series API
  slug: beel-es-invoiceseries-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Preferences of the authenticated principal (`PATCH /v1/me`), such as the language BeeL uses to talk to the account.
  name: beel-es Me API
  slug: beel-es-me-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'Account member management (multi-NIF). Members and their company grants are **shared between Test and Live**: a collaborator is the same person, with the same role and the same grants, in both environ'
  name: beel-es Members API
  slug: beel-es-members-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Tax ID validation against AEAT tax registry
  name: beel-es NIF API
  slug: beel-es-nif-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Product and service catalog management
  name: beel-es Products API
  slug: beel-es-products-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: A proforma is a non-fiscal commercial document, a formal quote you send a customer before invoicing. It lives on the same `/invoices` resource as any other document, so you work with it through the in
  name: beel-es Proforma API
  slug: beel-es-proforma-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: 'Lifecycle view for accounts you provisioned: track their activation state and manage the access level you hold over them.'
  name: beel-es Provisioning API
  slug: beel-es-provisioning-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: '**Deprecated.** VeriFactu representation flow for digital signature and AEAT registration, in its account-nested form. Use `CompanyRepresentation` (`/v1/companies/{company_id}/representation`), which '
  name: beel-es Public Company Representations API
  slug: beel-es-publiccompanyrepresentations-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Recurring invoice template management and automated invoice generation. Create templates that automatically generate invoices on a schedule. Supports monthly, quarterly and yearly recurrence, pause/re
  name: beel-es Recurring Invoices API
  slug: beel-es-recurringinvoices-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Read-only access to the API request logs generated by your own API keys (live + test). Inspect method, path, status, timing, and full request/response detail of past calls. Cursor-paginated; sourced f
  name: beel-es Request Logs API
  slug: beel-es-requestlogs-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: The tax regimes, percentages, withholdings and exemption reasons BeeL accepts. The same for every credential, and readable before the first NIF exists.
  name: beel-es Tax Types API
  slug: beel-es-taxtypes-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Downloadable file templates. They are fixed files, the same for every credential, and belong to no account and no NIF.
  name: beel-es Templates API
  slug: beel-es-templates-api
- baseURL: https://app.beel.es/api
  baseurl_source: declared
  description: Outbound webhook subscriptions for real-time event notifications. Register HTTPS endpoints to receive event payloads when key actions occur (e.g. VeriFactu submission accepted/rejected by AEAT). All d
  name: beel-es Webhooks API
  slug: beel-es-webhooks-api
artifact_total: 73
asyncapis:
- description: ''
  name: Beel Es Webhooks
  slug: beel-es-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/beel-es/agentic-access/beel-es-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beel-es-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/beel-es/plans/beel-es-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beel-es-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/beel-es/rules/beel-es-rules.yml
  title: ''
  type: Spectral
  url: rules/beel-es-rules.yml
- group: design
  href: https://artifacts.apis.io/beel-es/json-ld/beel-es-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beel-es-context.jsonld
- group: design
  href: https://artifacts.apis.io/beel-es/vocabulary/beel-es-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beel-es-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/beel-es/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/beel-es/asyncapi/beel-es-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/beel-es-webhooks.yml
- group: design
  href: https://artifacts.apis.io/beel-es/data-model/beel-es-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beel-es-data-model.yml
- group: build
  href: https://artifacts.apis.io/beel-es/cli/beel-es-cli.yml
  title: ''
  type: CLI
  url: cli/beel-es-cli.yml
- group: design
  href: https://artifacts.apis.io/beel-es/conventions/beel-es-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/beel-es-conventions.yml
- group: design
  href: https://artifacts.apis.io/beel-es/conventions/beel-es-conventions.yml
  title: ''
  type: Conventions
  url: conventions/beel-es-conventions.yml
- group: auth
  href: https://artifacts.apis.io/beel-es/security/beel-es-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/beel-es-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beel-es/authentication/beel-es-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beel-es-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.beel.es/guides/deprecation-policy.md
- group: design
  href: https://artifacts.apis.io/beel-es/lifecycle/beel-es-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/beel-es-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/beel-es/errors/beel-es-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beel-es-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beel-es/conformance/beel-es-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beel-es-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beel-es/llms/beel-es-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beel-es-llms.txt
- group: other
  href: https://artifacts.apis.io/beel-es/a2a/beel-es-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/beel-es-a2a.yml
- group: auth
  href: https://artifacts.apis.io/beel-es/well-known/beel-es-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beel-es-security.txt
- group: auth
  href: https://artifacts.apis.io/beel-es/well-known/beel-es-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beel-es-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/beel-es/well-known/beel-es-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beel-es-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/beel-es/well-known/beel-es-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beel-es-app-security.txt
- group: agent
  href: https://artifacts.apis.io/beel-es/well-known/beel-es-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beel-es-well-known.yml
- group: other
  href: https://artifacts.apis.io/beel-es/hosts/beel-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beel-es-hosts.yml
- group: other
  href: https://artifacts.apis.io/beel-es/vendors/beel-es-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beel-es-vendors.yml
- group: build
  href: https://artifacts.apis.io/beel-es/packages/beel-es-packages.yml
  title: ''
  type: Packages
  url: packages/beel-es-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://beel.es/sandbox
- group: build
  title: ''
  type: SDKs
  url: https://beel.es/api-verifactu/sdks
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.beel.es/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beel.es/invoices/createCompanyInvoice
- group: auth
  href: https://artifacts.apis.io/beel-es/scopes/beel-es-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/beel-es-scopes.yml
- group: auth
  href: https://artifacts.apis.io/beel-es/security/beel-es-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beel-es-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beel-es/security/beel-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beel-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beel.es/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beel.es/
- group: commercial
  title: ''
  type: Pricing
  url: https://beel.es/precios
- group: company
  title: ''
  type: Blog
  url: https://beel.es/blog
- group: operate
  title: ''
  type: Support
  url: https://beel.es/contacto
created: '2026-10-30'
description: BeeL (beel.es) provides a cloud‑based invoicing platform for Spanish businesses, offering the VeriFactu API that automates invoice creation, submission to the AEAT, and integration with Stripe. The service includes SDKs, CLI tools, sandbox testing, and AI‑assisted agents, supporting multi‑NIF, recurring invoices, and compliance features. Documentation, pricing, and support are publicly available.
image: https://beel.es/opengraph-image
json_schemas:
- name: CreateCorrectiveInvoiceRequest
  property_count: 12
  slug: beel-es-create-corrective-invoice-request
- name: CreateInvoiceRequest
  property_count: 13
  slug: beel-es-create-invoice-request
- name: PatchRecurringInvoiceRequest
  property_count: 20
  slug: beel-es-patch-recurring-invoice-request
- name: RecurringInvoiceResponse
  property_count: 36
  slug: beel-es-recurring-invoice-response
- name: UpdateInvoiceRequest
  property_count: 11
  slug: beel-es-update-invoice-request
- name: UpdateRecurringInvoiceRequest
  property_count: 19
  slug: beel-es-update-recurring-invoice-request
jsonld:
- class_count: 120
  name: Beel Es Context
  property_count: 315
  slug: beel-es-context
layout: provider
modified: '2026-10-30'
name: beel-es
nav: Providers
network: true
overview: 'beel-es publishes 54 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Companies API, Account Email Domains API, Account Emails API, and 51 more. Tagged areas include invoicing, Spain, API, fintech, and SaaS.


  The beel-es catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  beel-es'' developer surface includes CLI, authentication, sandbox, changelog, API reference, documentation, pricing, and 32 more developer resources.'
plans:
- name: Beel Es Plans Pricing
  plan_count: 7
  slug: beel-es-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: beel-es API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: beel-es-rules
scopes:
- name: Beel Es Scopes
  scope_count: 29
  slug: beel-es-scopes
  summary_line: 29 scopes · authorizationCode
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.9
    contract_governance: 79.1
    contract_quality: 71.0
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 42.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Beel Es Authentication
  slug: beel-es-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Beel Es Domain Security
  slug: beel-es-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Beel Es Vulnerability Disclosure
  slug: beel-es-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: beel-es-create-and-retrieve-customer
  slug: beel-es-create-and-retrieve-customer
- name: beel-es-create-and-retrieve-invoice
  slug: beel-es-create-and-retrieve-invoice
- name: beel-es-handle-company-payment-event
  slug: beel-es-handle-company-payment-event
- name: beel-es-manage-webhook-subscription
  slug: beel-es-manage-webhook-subscription
slug: beel-es
tags:
- invoicing
- Spain
- API
- fintech
- SaaS
website: https://beel.es/
---
