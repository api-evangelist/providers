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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 168
  human_in_the_loop: 5
  name: Acronis Agentic Access
  operation_count: 320
  slug: acronis-agentic-access
  summary_line: 320 operations · 168 acting · 5 human-in-the-loop
api_count: 12
apis:
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: Task activity and sub-operation tracking
  name: Acronis Activities API
  slug: acronis-activities-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: Agent update configuration and execution
  name: Acronis Agent Updates API
  slug: acronis-agent-updates-api
- baseURL: https://{datacenter}.acronis.com/api/agent_manager/v2
  baseurl_source: declared
  description: Acronis protection agent management
  name: Acronis Agents API
  slug: acronis-agents-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: OAuth2 client credential management
  name: Acronis Clients API
  slug: acronis-clients-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: Hardware node management
  name: Acronis Hardware Nodes API
  slug: acronis-hardware-nodes-api
- baseURL: https://{datacenter}.acronis.com/api/task_manager/v2
  baseurl_source: declared
  description: Backup and protection task monitoring
  name: Acronis Tasks API
  slug: acronis-tasks-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: Tenant hierarchy management and configuration
  name: Acronis Tenants API
  slug: acronis-tenants-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: User account management within tenants
  name: Acronis Users API
  slug: acronis-users-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Abgw Storages API from Acronis — 1 operation(s) for abgw storages.
  name: Acronis Abgw Storages API
  slug: acronis-abgw-storages-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Accounts API from Acronis — 1 operation(s) for accounts.
  name: Acronis Accounts API
  slug: acronis-accounts-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Agent Update References API from Acronis — 1 operation(s) for agent update references.
  name: Acronis Agent Update References API
  slug: acronis-agent-update-references-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Agent Update Settings API from Acronis — 2 operation(s) for agent update settings.
  name: Acronis Agent Update Settings API
  slug: acronis-agent-update-settings-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Alerts API from Acronis — 3 operation(s) for alerts.
  name: Acronis Alerts API
  slug: acronis-alerts-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Antimalware Scan Stats API from Acronis — 1 operation(s) for antimalware scan stats.
  name: Acronis Antimalware Scan Stats API
  slug: acronis-antimalware-scan-stats-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Applications API from Acronis — 4 operation(s) for applications.
  name: Acronis Applications API
  slug: acronis-applications-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Archives API from Acronis — 2 operation(s) for archives.
  name: Acronis Archives API
  slug: acronis-archives-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Audit Log API from Acronis — 1 operation(s) for audit log.
  name: Acronis Audit Log API
  slug: acronis-audit-log-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Backed Up Resources API from Acronis — 1 operation(s) for backed up resources.
  name: Acronis Backed Up Resources API
  slug: acronis-backed-up-resources-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Backups API from Acronis — 1 operation(s) for backups.
  name: Acronis Backups API
  slug: acronis-backups-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Call API from Acronis — 1 operation(s) for call.
  name: Acronis Call API
  slug: acronis-call-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Categories API from Acronis — 1 operation(s) for categories.
  name: Acronis Categories API
  slug: acronis-categories-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The ContractPart API from Acronis — 1 operation(s) for contractpart.
  name: Acronis Contract Part API
  slug: acronis-contractpart-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Contracts API from Acronis — 1 operation(s) for contracts.
  name: Acronis Contracts API
  slug: acronis-contracts-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Count API from Acronis — 1 operation(s) for count.
  name: Acronis Count API
  slug: acronis-count-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Customer Alerts API from Acronis — 1 operation(s) for customer alerts.
  name: Acronis Customer Alerts API
  slug: acronis-customer-alerts-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Customer Alerts Count API from Acronis — 1 operation(s) for customer alerts count.
  name: Acronis Customer Alerts Count API
  slug: acronis-customer-alerts-count-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Devices API from Acronis — 2 operation(s) for devices.
  name: Acronis Devices API
  slug: acronis-devices-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The DownloadInvoice API from Acronis — 1 operation(s) for downloadinvoice.
  name: Acronis Download Invoice API
  slug: acronis-downloadinvoice-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Effective Price Lists API from Acronis — 1 operation(s) for effective price lists.
  name: Acronis Effective Price Lists API
  slug: acronis-effective-price-lists-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The EmailUpdates API from Acronis — 1 operation(s) for emailupdates.
  name: Acronis Email Updates API
  slug: acronis-emailupdates-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Events API from Acronis — 1 operation(s) for events.
  name: Acronis Events API
  slug: acronis-events-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The ExportInvoice API from Acronis — 1 operation(s) for exportinvoice.
  name: Acronis Export Invoice API
  slug: acronis-exportinvoice-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Idp API from Acronis — 9 operation(s) for idp.
  name: Acronis Idp API
  slug: acronis-idp-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Incidents API from Acronis — 5 operation(s) for incidents.
  name: Acronis Incidents API
  slug: acronis-incidents-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Infra API from Acronis — 2 operation(s) for infra.
  name: Acronis Infra API
  slug: acronis-infra-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The InvoiceOverview API from Acronis — 1 operation(s) for invoiceoverview.
  name: Acronis Invoice Overview API
  slug: acronis-invoiceoverview-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Ledger API from Acronis — 1 operation(s) for ledger.
  name: Acronis Ledger API
  slug: acronis-ledger-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Ledgers API from Acronis — 1 operation(s) for ledgers.
  name: Acronis Ledgers API
  slug: acronis-ledgers-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Locations API from Acronis — 3 operation(s) for locations.
  name: Acronis Locations API
  slug: acronis-locations-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Policy Management API from Acronis — 21 operation(s) for policy management.
  name: Acronis Policy Management API
  slug: acronis-policy-management-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Priorities API from Acronis — 1 operation(s) for priorities.
  name: Acronis Priorities API
  slug: acronis-priorities-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Product API from Acronis — 1 operation(s) for product.
  name: Acronis Product API
  slug: acronis-product-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Registration Tokens API from Acronis — 2 operation(s) for registration tokens.
  name: Acronis Registration Tokens API
  slug: acronis-registration-tokens-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Reports API from Acronis — 4 operation(s) for reports.
  name: Acronis Reports API
  slug: acronis-reports-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Resource Management API from Acronis — 6 operation(s) for resource management.
  name: Acronis Resource Management API
  slug: acronis-resource-management-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Resource Status API from Acronis — 1 operation(s) for resource status.
  name: Acronis Resource Status API
  slug: acronis-resource-status-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The SalesItems API from Acronis — 1 operation(s) for salesitems.
  name: Acronis Sales Items API
  slug: acronis-salesitems-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The SchedulerTickets API from Acronis — 1 operation(s) for schedulertickets.
  name: Acronis Scheduler Tickets API
  slug: acronis-schedulertickets-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Search API from Acronis — 1 operation(s) for search.
  name: Acronis Search API
  slug: acronis-search-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Search Index Size Stats API from Acronis — 1 operation(s) for search index size stats.
  name: Acronis Search Index Size Stats API
  slug: acronis-search-index-size-stats-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Servers API from Acronis — 5 operation(s) for servers.
  name: Acronis Servers API
  slug: acronis-servers-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Settings API from Acronis — 5 operation(s) for settings.
  name: Acronis Settings API
  slug: acronis-settings-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Sites API from Acronis — 2 operation(s) for sites.
  name: Acronis Sites API
  slug: acronis-sites-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The SLA API from Acronis — 1 operation(s) for sla.
  name: Acronis SLA API
  slug: acronis-sla-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Stats API from Acronis — 1 operation(s) for stats.
  name: Acronis Stats API
  slug: acronis-stats-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Status API from Acronis — 1 operation(s) for status.
  name: Acronis Status API
  slug: acronis-status-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Statuses API from Acronis — 1 operation(s) for statuses.
  name: Acronis Statuses API
  slug: acronis-statuses-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Storage Dirs API from Acronis — 2 operation(s) for storage dirs.
  name: Acronis Storage Dirs API
  slug: acronis-storage-dirs-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Storage Nodes API from Acronis — 3 operation(s) for storage nodes.
  name: Acronis Storage Nodes API
  slug: acronis-storage-nodes-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Storage Usage Stats API from Acronis — 1 operation(s) for storage usage stats.
  name: Acronis Storage Usage Stats API
  slug: acronis-storage-usage-stats-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Subscriptions API from Acronis — 2 operation(s) for subscriptions.
  name: Acronis Subscriptions API
  slug: acronis-subscriptions-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Sync And Share Nodes API from Acronis — 14 operation(s) for sync and share nodes.
  name: Acronis Sync And Share Nodes API
  slug: acronis-sync-and-share-nodes-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Sync API from Acronis — 11 operation(s) for sync.
  name: Acronis Sync API
  slug: acronis-sync-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Taxes API from Acronis — 1 operation(s) for taxes.
  name: Acronis Taxes API
  slug: acronis-taxes-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Topics API from Acronis — 2 operation(s) for topics.
  name: Acronis Topics API
  slug: acronis-topics-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Types API from Acronis — 2 operation(s) for types.
  name: Acronis Types API
  slug: acronis-types-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The UploadedFiles API from Acronis — 1 operation(s) for uploadedfiles.
  name: Acronis Uploaded Files API
  slug: acronis-uploadedfiles-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Vaults API from Acronis — 22 operation(s) for vaults.
  name: Acronis Vaults API
  slug: acronis-vaults-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The .well Known API from Acronis — 1 operation(s) for .well known.
  name: Acronis .well Known API
  slug: acronis-well-known-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: The Dashboard Data API from Acronis — 1 operation(s) for dashboard data.
  name: Acronis Dashboard Data API
  slug: acronis-dashboard-data-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: The Health Check API from Acronis — 1 operation(s) for health check.
  name: Acronis Health Check API
  slug: acronis-health-check-api
artifact_total: 211
asyncapis:
- description: ''
  name: Acronis Events Webhooks
  slug: acronis-events-webhooks
collections:
- collection_type: postman
  name: Acronis Account Management Activities API
  slug: postman-acronis-activities-api
- collection_type: postman
  name: Acronis Account Management Activities Agent Updates API
  slug: postman-acronis-agent-updates-api
- collection_type: postman
  name: Acronis Account Management Activities Agents API
  slug: postman-acronis-agents-api
- collection_type: postman
  name: Acronis Account Management Activities Authentication API
  slug: postman-acronis-authentication-api
- collection_type: postman
  name: Acronis Account Management Activities Clients API
  slug: postman-acronis-clients-api
- collection_type: postman
  name: Acronis Account Management Activities Hardware Nodes API
  slug: postman-acronis-hardware-nodes-api
- collection_type: postman
  name: Acronis Account Management Activities Licensing API
  slug: postman-acronis-licensing-api
- collection_type: postman
  name: Acronis Account Management Activities Tasks API
  slug: postman-acronis-tasks-api
- collection_type: postman
  name: Acronis Account Management Activities Tenants API
  slug: postman-acronis-tenants-api
- collection_type: postman
  name: Acronis Account Management Activities Usage API
  slug: postman-acronis-usage-api
- collection_type: postman
  name: Acronis Account Management Activities Users API
  slug: postman-acronis-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acronis Account Management Activities API
  slug: open-acronis-activities-api
- collection_type: open
  name: Acronis Account Management Activities Agent Updates API
  slug: open-acronis-agent-updates-api
- collection_type: open
  name: Acronis Account Management Activities Agents API
  slug: open-acronis-agents-api
- collection_type: open
  name: Acronis Account Management Activities Authentication API
  slug: open-acronis-authentication-api
- collection_type: open
  name: Acronis Account Management Activities Clients API
  slug: open-acronis-clients-api
- collection_type: open
  name: Acronis Account Management Activities Hardware Nodes API
  slug: open-acronis-hardware-nodes-api
- collection_type: open
  name: Acronis Account Management Activities Licensing API
  slug: open-acronis-licensing-api
- collection_type: open
  name: Acronis Account Management Activities Tasks API
  slug: open-acronis-tasks-api
- collection_type: open
  name: Acronis Account Management Activities Tenants API
  slug: open-acronis-tenants-api
- collection_type: open
  name: Acronis Account Management Activities Usage API
  slug: open-acronis-usage-api
- collection_type: open
  name: Acronis Account Management Activities Users API
  slug: open-acronis-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.acronis.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/acronis/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/agentic-access/acronis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acronis-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/security/acronis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/acronis-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/security/acronis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acronis-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/authentication/acronis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acronis-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acronis
- group: start
  title: ''
  type: Portal
  url: https://developer.acronis.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.acronis.com/doc/outbound/apis/getting-started/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.acronis.com/doc/outbound/apis/authentication/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.acronis.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.acronis.com/en-us/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acronis.com/en-us/products/cloud/cyber-protect/pricing/
- group: company
  title: ''
  type: Partners
  url: https://www.acronis.com/en-us/partners/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.acronis.com/en-us/resource-center/category/case-studies/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acronis
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rules/acronis-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/vocabulary/acronis-vocabulary.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acronis.com/en-us/legal/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/changelog/acronis-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/acronis-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/packages/acronis-packages.yml
  title: ''
  type: Packages
  url: packages/acronis-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/packages/acronis-packages.yml
  title: ''
  type: SDKs
  url: packages/acronis-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/well-known/acronis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acronis-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/well-known/acronis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/acronis-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/mcp/acronis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/acronis-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/mcp/acronis-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/acronis-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/llms/acronis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acronis-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/overlays/acronis-account-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/acronis-account-management-v2-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/conformance/acronis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acronis-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/conformance/acronis-conformance.yml
  title: ''
  type: Compliance
  url: conformance/acronis-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/errors/acronis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acronis-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/lifecycle/acronis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/acronis-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acronis.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/scopes/acronis-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/acronis-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/security/acronis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/acronis-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/security/acronis-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/acronis-vulnerability-disclosure.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/sandbox/acronis-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/acronis-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/conventions/acronis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/acronis-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/conventions/acronis-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/acronis-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/cli/acronis-cli.yml
  title: ''
  type: CLI
  url: cli/acronis-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/components/acronis-components.yml
  title: ''
  type: Components
  url: components/acronis-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/data-model/acronis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acronis-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/asyncapi/acronis-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/acronis-events-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.acronis.com/doc/outbound/apis/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.acronis.com/doc/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.acronis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acronis.com/en-us/company/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://www.acronis.com/en-us/my/
- group: start
  title: ''
  type: Login
  url: https://cloud.acronis.com/login
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/acronis/overview
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/plans/acronis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acronis-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rate-limits/acronis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/acronis-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/finops/acronis-finops.yml
  title: ''
  type: FinOps
  url: finops/acronis-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://dl.acronis.com/u/baas/rn/API_change_log/en-US/AcronisCyberCloud_API_change_log.pdf
created: '2025-02-17'
description: Acronis is a leading provider of cyber protection solutions that deliver innovative technology to protect data, applications, and systems from the ever-evolving threats of today's digital world. They offer a comprehensive suite of products, including backup and disaster recovery solutions, file sync and share services, and anti-malware protection.
examples:
- key_count: 6
  name: Account Management Client Example
  slug: account-management-client-example
- key_count: 7
  name: Account Management Contact Example
  slug: account-management-contact-example
- key_count: 5
  name: Account Management Offering Item Example
  slug: account-management-offering-item-example
- key_count: 3
  name: Account Management Quota Example
  slug: account-management-quota-example
- key_count: 3
  name: Account Management Report Example
  slug: account-management-report-example
- key_count: 2
  name: Account Management Search Results Example
  slug: account-management-search-results-example
- key_count: 10
  name: Account Management Tenant Example
  slug: account-management-tenant-example
- key_count: 5
  name: Account Management Token Response Example
  slug: account-management-token-response-example
- key_count: 4
  name: Account Management Usage Item Example
  slug: account-management-usage-item-example
- key_count: 8
  name: Account Management User Example
  slug: account-management-user-example
- key_count: 6
  name: Acronis Createtenant Example
  slug: acronis-createtenant-example
- key_count: 6
  name: Acronis Getagent Example
  slug: acronis-getagent-example
- key_count: 6
  name: Acronis Gettask Example
  slug: acronis-gettask-example
- key_count: 6
  name: Acronis Listagents Example
  slug: acronis-listagents-example
- key_count: 6
  name: Acronis Listtasks Example
  slug: acronis-listtasks-example
- key_count: 6
  name: Acronis Listtenants Example
  slug: acronis-listtenants-example
- key_count: 8
  name: Agent Management Agent Example
  slug: agent-management-agent-example
- key_count: 4
  name: Agent Management Agent O S Example
  slug: agent-management-agent-o-s-example
- key_count: 3
  name: Agent Management Agent Update Settings Example
  slug: agent-management-agent-update-settings-example
- key_count: 5
  name: Agent Management Hardware Node Example
  slug: agent-management-hardware-node-example
- key_count: 10
  name: Task Manager Activity Example
  slug: task-manager-activity-example
- key_count: 14
  name: Task Manager Task Example
  slug: task-manager-task-example
features:
- description: Multi-tier tenant management for MSPs, partners, and customers with offering item quotas.
  name: Tenant Hierarchy Management
- description: Remote management of Acronis backup agents across Windows, Linux, macOS, and cloud workloads.
  name: Agent Management
- description: Real-time monitoring of backup and protection tasks with state, result, and activity tracking.
  name: Backup Task Monitoring
- description: Automated usage metrics collection and report generation for billing and capacity planning.
  name: Usage Reporting
- description: Programmatic creation and application of protection policies to resources.
  name: Policy Management
- description: Automated failover and recovery orchestration for business continuity.
  name: Disaster Recovery API
- description: EDR capabilities for threat detection, investigation, and response via API.
  name: Endpoint Detection and Response
finops:
- name: Acronis Finops
  service_category: Cyber Protection / Backup / Endpoint Security
  slug: acronis-finops
image: /assets/icons/acronis.png
integrations:
- description: Integration with ConnectWise, Autotask, and other PSA platforms for MSP billing and ticketing.
  name: PSA Platforms
- description: Event streaming to SIEM platforms via Event Manager API for security monitoring.
  name: SIEM Systems
- description: Integration with RMM platforms for agent deployment and backup policy management.
  name: RMM Tools
- description: Usage data export for automated billing via usage and offering item APIs.
  name: Billing Systems
json_schemas:
- name: Client
  property_count: 6
  slug: account-management-client
- name: Contact
  property_count: 7
  slug: account-management-contact
- name: OfferingItem
  property_count: 5
  slug: account-management-offering-item
- name: Quota
  property_count: 3
  slug: account-management-quota
- name: Report
  property_count: 3
  slug: account-management-report
- name: SearchResults
  property_count: 2
  slug: account-management-search-results
- name: Tenant
  property_count: 10
  slug: account-management-tenant
- name: TokenResponse
  property_count: 5
  slug: account-management-token-response
- name: UsageItem
  property_count: 4
  slug: account-management-usage-item
- name: User
  property_count: 8
  slug: account-management-user
- name: Activity
  property_count: 10
  slug: acronis-activity
- name: ActivityList
  property_count: 2
  slug: acronis-activitylist
- name: Agent
  property_count: 8
  slug: acronis-agent
- name: AgentList
  property_count: 2
  slug: acronis-agentlist
- name: AgentOS
  property_count: 4
  slug: acronis-agentos
- name: AgentUpdateSettings
  property_count: 3
  slug: acronis-agentupdatesettings
- name: Client
  property_count: 6
  slug: acronis-client
- name: ClientList
  property_count: 1
  slug: acronis-clientlist
- name: ClientRequest
  property_count: 3
  slug: acronis-clientrequest
- name: Contact
  property_count: 7
  slug: acronis-contact
- name: Error
  property_count: 3
  slug: acronis-error
- name: HardwareNode
  property_count: 5
  slug: acronis-hardwarenode
- name: HardwareNodeList
  property_count: 1
  slug: acronis-hardwarenodelist
- name: MaintenanceWindow
  property_count: 3
  slug: acronis-maintenancewindow
- name: OfferingItem
  property_count: 5
  slug: acronis-offeringitem
- name: OfferingItemList
  property_count: 1
  slug: acronis-offeringitemlist
- name: OfferingItemUpdateRequest
  property_count: 1
  slug: acronis-offeringitemupdaterequest
- name: Paging
  property_count: 1
  slug: acronis-paging
- name: Quota
  property_count: 3
  slug: acronis-quota
- name: Report
  property_count: 3
  slug: acronis-report
- name: ReportRequest
  property_count: 2
  slug: acronis-reportrequest
- name: SearchResults
  property_count: 2
  slug: acronis-searchresults
- name: Task
  property_count: 14
  slug: acronis-task
- name: TaskList
  property_count: 2
  slug: acronis-tasklist
- name: Tenant
  property_count: 10
  slug: acronis-tenant
- name: TenantList
  property_count: 2
  slug: acronis-tenantlist
- name: TenantRequest
  property_count: 5
  slug: acronis-tenantrequest
- name: TokenResponse
  property_count: 5
  slug: acronis-tokenresponse
- name: UsageItem
  property_count: 4
  slug: acronis-usageitem
- name: UsageList
  property_count: 1
  slug: acronis-usagelist
- name: User
  property_count: 8
  slug: acronis-user
- name: UserList
  property_count: 2
  slug: acronis-userlist
- name: AgentOS
  property_count: 4
  slug: agent-management-agent-o-s
- name: Agent
  property_count: 8
  slug: agent-management-agent
- name: AgentUpdateSettings
  property_count: 3
  slug: agent-management-agent-update-settings
- name: HardwareNode
  property_count: 5
  slug: agent-management-hardware-node
- name: Activity
  property_count: 10
  slug: task-manager-activity
- name: Task
  property_count: 14
  slug: task-manager-task
json_structures:
- name: Account Management Client Structure
  property_count: 6
  slug: account-management-client-structure
- name: Account Management Contact Structure
  property_count: 7
  slug: account-management-contact-structure
- name: Account Management Offering Item Structure
  property_count: 5
  slug: account-management-offering-item-structure
- name: Account Management Quota Structure
  property_count: 3
  slug: account-management-quota-structure
- name: Account Management Report Structure
  property_count: 3
  slug: account-management-report-structure
- name: Account Management Search Results Structure
  property_count: 2
  slug: account-management-search-results-structure
- name: Account Management Tenant Structure
  property_count: 10
  slug: account-management-tenant-structure
- name: Account Management Token Response Structure
  property_count: 5
  slug: account-management-token-response-structure
- name: Account Management Usage Item Structure
  property_count: 4
  slug: account-management-usage-item-structure
- name: Account Management User Structure
  property_count: 8
  slug: account-management-user-structure
- name: Acronis Structure
  property_count: 0
  slug: acronis-structure
- name: Agent Management Agent O S Structure
  property_count: 4
  slug: agent-management-agent-o-s-structure
- name: Agent Management Agent Structure
  property_count: 8
  slug: agent-management-agent-structure
- name: Agent Management Agent Update Settings Structure
  property_count: 3
  slug: agent-management-agent-update-settings-structure
- name: Agent Management Hardware Node Structure
  property_count: 5
  slug: agent-management-hardware-node-structure
- name: Task Manager Activity Structure
  property_count: 10
  slug: task-manager-activity-structure
- name: Task Manager Task Structure
  property_count: 14
  slug: task-manager-task-structure
jsonld:
- class_count: 18
  name: Acronis Context
  property_count: 61
  slug: acronis-context
layout: provider
mcp_servers:
- description: Provides Acronis Cyber Protect Cloud platform APIs as MCP tools — tenant and user provisioning, service and quota management, backup policy configuration, resource protection, agent management, and mo
  name: Acronis API MCP
  slug: acronis-api-mcp
modified: '2026-08-30'
name: Acronis
nav: Providers
network: true
overview: 'Acronis publishes 71 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Agent Updates API, Agents API, and 68 more. Tagged areas include Cybersecurity, Data Protection, Endpoint Management, Backup and Recovery, and Disaster Recovery.


  The Acronis catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Acronis'' developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, pricing, changelog, and 48 more developer resources.'
plans:
- name: Acronis Plans Pricing
  plan_count: 4
  slug: acronis-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Acronis Rate Limits
  slug: acronis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Acronis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: acronis-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: Acronis API Rules
  rule_count: 38
  severity_counts:
    error: 15
    hint: 0
    info: 7
    warn: 16
  slug: acronis-spectral-rules
scopes:
- name: Acronis Scopes
  scope_count: 0
  slug: acronis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 81.3
  coverage:
    artifact_dirs: 34
    catalog_earned: 84.5
    catalog_earned_first_party: 24.0
    catalog_gap: 30.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.4
  facets:
    access_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 66.2
    developer_ergonomics: 86.3
    discoverability: 75.9
    operational_transparency: 76.3
  previous_composite: 72.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 5.4
      total: 74
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/screenshots/acronis-2026-06-20T164007.png
security:
- kind: authentication
  name: Acronis Authentication
  slug: acronis-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Acronis Domain Security
  slug: acronis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acronis Vulnerability Disclosure
  slug: acronis-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Acronis Trust Center
  slug: acronis-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO 9001, SOC 2, PCI DSS, IEC 62443-4-1, IT-Grundschutz, Cyber Essentials, ENS, Cloud Italia, FIPS 140-2, UAE IAR, HIPAA, PHIPA, HDS, NEN 7510, 2G3M, EU-US Data Privacy Framework, CSA STAR Level 1
slug: acronis
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
- Backup and Recovery
- Disaster Recovery
- Managed Service Providers
- Endpoint Detection and Response
- Cloud Storage
use_cases:
- description: Automate tenant provisioning, licensing management, and usage reporting for managed service providers.
  name: MSP Platform Automation
- description: Build custom dashboards tracking backup task status, failures, and completion rates.
  name: Backup Monitoring Dashboard
- description: Monitor agent online status, version compliance, and update management across endpoints.
  name: Agent Health Monitoring
- description: Generate automated reports on data protection status for compliance and audit requirements.
  name: Compliance Reporting
- description: Trigger and monitor DR failover workflows programmatically for RTO/RPO compliance.
  name: Disaster Recovery Automation
website: https://www.acronis.com/
---
