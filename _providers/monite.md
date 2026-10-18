---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 246
  human_in_the_loop: 4
  name: Monite Agentic Access
  operation_count: 408
  slug: monite-agentic-access
  summary_line: 408 operations · 246 acting · 4 human-in-the-loop
api_count: 5
apis:
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Access tokens API from Monite — 2 operation(s) for access tokens.
  name: Monite Access tokens API
  slug: monite-access-tokens-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Accounting connections API from Monite — 4 operation(s) for accounting connections.
  name: Monite Accounting connections API
  slug: monite-accounting-connections-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Accounting data pull API from Monite — 4 operation(s) for accounting data pull.
  name: Monite Accounting data pull API
  slug: monite-accounting-data-pull-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Accounting synchronized records API from Monite — 3 operation(s) for accounting synchronized records.
  name: Monite Accounting synchronized records API
  slug: monite-accounting-synchronized-records-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Accounting tax rates API from Monite — 2 operation(s) for accounting tax rates.
  name: Monite Accounting tax rates API
  slug: monite-accounting-tax-rates-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Analytics API from Monite — 3 operation(s) for analytics.
  name: Monite Analytics API
  slug: monite-analytics-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Approval policies API from Monite — 6 operation(s) for approval policies.
  name: Monite Approval policies API
  slug: monite-approval-policies-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Approval requests API from Monite — 5 operation(s) for approval requests.
  name: Monite Approval requests API
  slug: monite-approval-requests-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Batch payment links API from Monite — 3 operation(s) for batch payment links.
  name: Monite Batch payment links API
  slug: monite-batch-payment-links-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Batch payments API from Monite — 2 operation(s) for batch payments.
  name: Monite Batch payments API
  slug: monite-batch-payments-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Comments API from Monite — 2 operation(s) for comments.
  name: Monite Comments API
  slug: monite-comments-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Cost centers API from Monite — 2 operation(s) for cost centers.
  name: Monite Cost centers API
  slug: monite-cost-centers-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Counterpart addresses API from Monite — 3 operation(s) for counterpart addresses.
  name: Monite Counterpart addresses API
  slug: monite-counterpart-addresses-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Counterpart bank accounts API from Monite — 4 operation(s) for counterpart bank accounts.
  name: Monite Counterpart bank accounts API
  slug: monite-counterpart-bank-accounts-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Counterpart contacts API from Monite — 3 operation(s) for counterpart contacts.
  name: Monite Counterpart contacts API
  slug: monite-counterpart-contacts-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Counterpart e-invoicing credentials API from Monite — 2 operation(s) for counterpart e-invoicing credentials.
  name: Monite Counterpart e-invoicing credentials API
  slug: monite-counterpart-e-invoicing-credentials-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Counterpart VAT IDs API from Monite — 2 operation(s) for counterpart vat ids.
  name: Monite Counterpart VAT IDs API
  slug: monite-counterpart-vat-ids-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Counterparts API from Monite — 3 operation(s) for counterparts.
  name: Monite Counterparts API
  slug: monite-counterparts-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Credit notes API from Monite — 13 operation(s) for credit notes.
  name: Monite Credit notes API
  slug: monite-credit-notes-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Custom VAT rates API from Monite — 2 operation(s) for custom vat rates.
  name: Monite Custom VAT rates API
  slug: monite-custom-vat-rates-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Data export API from Monite — 3 operation(s) for data export.
  name: Monite Data export API
  slug: monite-data-export-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Data export - extra data API from Monite — 2 operation(s) for data export - extra data.
  name: Monite Data export - extra data API
  slug: monite-data-export-extra-data-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Delivery notes API from Monite — 4 operation(s) for delivery notes.
  name: Monite Delivery notes API
  slug: monite-delivery-notes-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The E-invoicing connections API from Monite — 3 operation(s) for e-invoicing connections.
  name: Monite E-invoicing connections API
  slug: monite-e-invoicing-connections-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The E-invoicing search API from Monite — 1 operation(s) for e-invoicing search.
  name: Monite E-invoicing search API
  slug: monite-e-invoicing-search-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Entities API from Monite — 10 operation(s) for entities.
  name: Monite Entities API
  slug: monite-entities-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Entity bank account verifications API from Monite — 5 operation(s) for entity bank account verifications.
  name: Monite Entity bank account verifications API
  slug: monite-entity-bank-account-verifications-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Entity bank accounts API from Monite — 4 operation(s) for entity bank accounts.
  name: Monite Entity bank accounts API
  slug: monite-entity-bank-accounts-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Entity onboarding data API from Monite — 1 operation(s) for entity onboarding data.
  name: Monite Entity onboarding data API
  slug: monite-entity-onboarding-data-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Entity persons API from Monite — 2 operation(s) for entity persons.
  name: Monite Entity persons API
  slug: monite-entity-persons-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Entity users API from Monite — 4 operation(s) for entity users.
  name: Monite Entity users API
  slug: monite-entity-users-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Entity VAT IDs API from Monite — 2 operation(s) for entity vat ids.
  name: Monite Entity VAT IDs API
  slug: monite-entity-vat-ids-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Events API from Monite — 2 operation(s) for events.
  name: Monite Events API
  slug: monite-events-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Files API from Monite — 2 operation(s) for files.
  name: Monite Files API
  slug: monite-files-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Financing API from Monite — 3 operation(s) for financing.
  name: Monite Financing API
  slug: monite-financing-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Ledger accounts API from Monite — 2 operation(s) for ledger accounts.
  name: Monite Ledger accounts API
  slug: monite-ledger-accounts-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Mail templates API from Monite — 5 operation(s) for mail templates.
  name: Monite Mail templates API
  slug: monite-mail-templates-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Mailbox domains API from Monite — 3 operation(s) for mailbox domains.
  name: Monite Mailbox domains API
  slug: monite-mailbox-domains-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Mailboxes API from Monite — 3 operation(s) for mailboxes.
  name: Monite Mailboxes API
  slug: monite-mailboxes-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Measure units API from Monite — 2 operation(s) for measure units.
  name: Monite Measure units API
  slug: monite-measure-units-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Monite AI API from Monite — 7 operation(s) for monite ai.
  name: Monite Monite AI API
  slug: monite-monite-ai-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The OCR API from Monite — 3 operation(s) for ocr.
  name: Monite OCR API
  slug: monite-ocr-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Onboarding documents API from Monite — 4 operation(s) for onboarding documents.
  name: Monite Onboarding documents API
  slug: monite-onboarding-documents-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Onboarding links API from Monite — 2 operation(s) for onboarding links.
  name: Monite Onboarding links API
  slug: monite-onboarding-links-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Onboarding requirements API from Monite — 2 operation(s) for onboarding requirements.
  name: Monite Onboarding requirements API
  slug: monite-onboarding-requirements-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Overdue reminders API from Monite — 2 operation(s) for overdue reminders.
  name: Monite Overdue reminders API
  slug: monite-overdue-reminders-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Partner settings API from Monite — 1 operation(s) for partner settings.
  name: Monite Partner settings API
  slug: monite-partner-settings-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Payable line items API from Monite — 2 operation(s) for payable line items.
  name: Monite Payable line items API
  slug: monite-payable-line-items-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Payables API from Monite — 19 operation(s) for payables.
  name: Monite Payables API
  slug: monite-payables-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Payment intents API from Monite — 3 operation(s) for payment intents.
  name: Monite Payment intents API
  slug: monite-payment-intents-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Payment links API from Monite — 3 operation(s) for payment links.
  name: Monite Payment links API
  slug: monite-payment-links-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Payment methods API from Monite — 1 operation(s) for payment methods.
  name: Monite Payment methods API
  slug: monite-payment-methods-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Payment records API from Monite — 5 operation(s) for payment records.
  name: Monite Payment records API
  slug: monite-payment-records-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Payment reminders API from Monite — 2 operation(s) for payment reminders.
  name: Monite Payment reminders API
  slug: monite-payment-reminders-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Payment terms API from Monite — 2 operation(s) for payment terms.
  name: Monite Payment terms API
  slug: monite-payment-terms-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The PDF templates API from Monite — 5 operation(s) for pdf templates.
  name: Monite PDF templates API
  slug: monite-pdf-templates-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Products API from Monite — 2 operation(s) for products.
  name: Monite Products API
  slug: monite-products-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Projects API from Monite — 2 operation(s) for projects.
  name: Monite Projects API
  slug: monite-projects-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Purchase orders API from Monite — 5 operation(s) for purchase orders.
  name: Monite Purchase orders API
  slug: monite-purchase-orders-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Receipts API from Monite — 6 operation(s) for receipts.
  name: Monite Receipts API
  slug: monite-receipts-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Receivables API from Monite — 23 operation(s) for receivables.
  name: Monite Receivables API
  slug: monite-receivables-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Recurrences API from Monite — 5 operation(s) for recurrences.
  name: Monite Recurrences API
  slug: monite-recurrences-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Roles API from Monite — 2 operation(s) for roles.
  name: Monite Roles API
  slug: monite-roles-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The System health API from Monite — 1 operation(s) for system health.
  name: Monite System health API
  slug: monite-system-health-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Tags API from Monite — 2 operation(s) for tags.
  name: Monite Tags API
  slug: monite-tags-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Text templates API from Monite — 3 operation(s) for text templates.
  name: Monite Text templates API
  slug: monite-text-templates-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Transactions API from Monite — 3 operation(s) for transactions.
  name: Monite Transactions API
  slug: monite-transactions-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The VAT rates API from Monite — 1 operation(s) for vat rates.
  name: Monite VAT rates API
  slug: monite-vat-rates-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Webhook deliveries API from Monite — 2 operation(s) for webhook deliveries.
  name: Monite Webhook deliveries API
  slug: monite-webhook-deliveries-api
- baseURL: https://api.monite.com/v1
  baseurl_source: declared
  description: The Webhook subscriptions API from Monite — 10 operation(s) for webhook subscriptions.
  name: Monite Webhook subscriptions API
  slug: monite-webhook-subscriptions-api
artifact_total: 87
asyncapis:
- description: ''
  name: Monite Webhooks
  slug: monite-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/capabilities/monite-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/monite-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/agentic-access/monite-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/monite-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/rate-limits/monite-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/monite-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/rules/monite-rules.yml
  title: ''
  type: Spectral
  url: rules/monite-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/rules/monite-api-style-guide-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/monite-api-style-guide-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/json-ld/monite-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/monite-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/vocabulary/monite-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/monite-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/asyncapi/monite-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/monite-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/data-model/monite-data-model.yml
  title: ''
  type: DataModel
  url: data-model/monite-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/components/monite-components.yml
  title: ''
  type: Components
  url: components/monite-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/changelog/monite-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/monite-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/conventions/monite-conventions.yml
  title: ''
  type: Conventions
  url: conventions/monite-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/sandbox/monite-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/monite-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/scopes/monite-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/monite-scopes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/lifecycle/monite-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/monite-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/lifecycle/monite-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/monite-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/errors/monite-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/monite-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/conformance/monite-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monite-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/overlays/monite-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/monite-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/llms/monite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monite-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/mcp/monite-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/monite-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/mcp/monite-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/monite-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/well-known/monite-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/monite-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/hosts/monite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monite-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/vendors/monite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monite-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/packages/monite-packages.yml
  title: ''
  type: SDKs
  url: packages/monite-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/packages/monite-packages.yml
  title: ''
  type: Packages
  url: packages/monite-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/authentication/monite-authentication.yml
  title: ''
  type: Authentication
  url: authentication/monite-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/security/monite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.monite.com/api/concepts/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.monite.com/home
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.monite.com/get-started/credentials
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.monite.com/intro/release-notes/index
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.sandbox.monite.com/
- group: start
  title: ''
  type: SignUp
  url: https://portal.sandbox.monite.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://portal.sandbox.monite.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://docs.monite.com/intro/support
- group: company
  title: ''
  type: Blog
  url: https://www.monite.com/blog
- group: company
  title: ''
  type: About
  url: https://www.monite.com/about
- group: start
  title: ''
  type: Demo
  url: https://www.monite.com/free-demo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/team-monite
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/monite/workspace/monite-public-workspace
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monite.com/data-privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.monite.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monitehq
- group: other
  title: ''
  type: X
  url: https://x.com/Monite_
- group: docs
  title: ''
  type: StyleGuide
  url: https://github.com/team-monite/api-style-guide
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/team-monite/api-style-guide/blob/6b3d64c03345a46a5bd643a7e93d15b49716332f/spectral/monite.all.yaml
created: '2026-10-09'
description: Monite (Monite GmbH) is an embedded finance API platform that lets neobanks and B2B SaaS platforms add invoicing, accounts payable automation, payments and related financial workflows to their own products, with a fully embeddable SDK and UI components. Its REST API (api.monite.com, with a sandbox at api.sandbox.monite.com) is documented at docs.monite.com, and the company publishes a public API style guide with Spectral rules on GitHub.
image: https://framerusercontent.com/images/PH8mkvz4WO907aVf6N6yabuqhA.png
json_schemas:
- name: CreditNoteResponse
  property_count: 34
  slug: monite-credit-note-response
- name: DeliveryNoteResource
  property_count: 23
  slug: monite-delivery-note-resource
- name: PayableResponseSchema
  property_count: 49
  slug: monite-payable-response-schema
- name: PayableUpdateSchema
  property_count: 24
  slug: monite-payable-update-schema
- name: PayableUploadWithDataSchema
  property_count: 24
  slug: monite-payable-upload-with-data-schema
- name: ReceivablesSearchRequest
  property_count: 48
  slug: monite-receivables-search-request
jsonld:
- class_count: 120
  name: Monite Context
  property_count: 166
  slug: monite-context
layout: provider
mcp_servers:
- description: Monite's llms.txt instructs AI clients (Claude Code, Cursor, etc.) to connect to the MCP server at https://docs.monite.com/_mcp/server. It is a Fern-hosted documentation MCP server (serverInfo name "f
  name: Monite Docs MCP Server
  slug: monite-docs-mcp-server
modified: '2026-10-09'
name: Monite
nav: Providers
network: true
overview: 'Monite publishes 70 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access tokens API, Accounting connections API, Accounting data pull API, and 67 more. Tagged areas include Company, Embedded Finance, Invoicing, Accounts Payable, and Payments.


  The Monite catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Monite''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, signup flow, support, and 43 more developer resources.'
plans:
- name: Monite Plans Pricing
  plan_count: 0
  slug: monite-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Monite Rate Limits
  slug: monite-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  - monite.openapi-structure.yaml
  - monite.section1-general.yaml
  - monite.section2-language.yaml
  - monite.section3-security.yaml
  - monite.section4-data-types.yaml
  - monite.section5-uri.yaml
  - monite.section6-rest.yaml
  - monite.section7-json.yaml
  - monite.section8-requests.yaml
  - monite.section9-responses.yaml
  - monite.section10-headers.yaml
  - monite.section13-performance.yaml
  - monite.section15-versioning.yaml
  name: Monite — api style guide rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: monite-api-style-guide-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Monite API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: monite-rules
scopes:
- name: Monite Scopes
  scope_count: 27
  slug: monite-scopes
  summary_line: 27 scopes
score:
  band: strong
  composite: 66.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 77.6
    developer_ergonomics: 70.8
    discoverability: 80.0
    operational_transparency: 57.9
  previous_composite: 67.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 70
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/monite/refs/heads/main/screenshots/monite-2026-10-11T111245.png
security:
- kind: authentication
  name: Monite Authentication
  slug: monite-authentication
  summary_line: http/oauth2-style token endpoint · 1 scheme
- kind: domain-security
  name: Monite Domain Security
  slug: monite-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: monite
tags:
- Company
- Embedded Finance
- Invoicing
- Accounts Payable
- Payments
- B2B
- Fintech
- Software-as-a-Service
website: https://docs.monite.com/api/concepts/overview
---
