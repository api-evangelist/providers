---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 40
  human_in_the_loop: 2
  name: Contraforce Agentic Access
  operation_count: 81
  slug: contraforce-agentic-access
  summary_line: 81 operations · 40 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: API for ContraForce security platform
  name: ContraForce API
  slug: contraforce-api
- description: The agent-tools API from Contraforce — 10 operation(s) for agent-tools.
  name: Contraforce Agent Tools API
  slug: contraforce-agent-tools-api
- description: The Azure resources API from Contraforce — 8 operation(s) for azure resources.
  name: Contraforce Azure resources API
  slug: contraforce-azure-resources-api
- description: The Cross-workspace data sources API from Contraforce — 2 operation(s) for cross-workspace data sources.
  name: Contraforce Cross-workspace data sources API
  slug: contraforce-cross-workspace-data-sources-api
- description: The Cross-workspace gamebooks API from Contraforce — 1 operation(s) for cross-workspace gamebooks.
  name: Contraforce Cross-workspace gamebooks API
  slug: contraforce-cross-workspace-gamebooks-api
- description: The Cross-workspace incidents API from Contraforce — 2 operation(s) for cross-workspace incidents.
  name: Contraforce Cross-workspace incidents API
  slug: contraforce-cross-workspace-incidents-api
- description: The Data sources API from Contraforce — 1 operation(s) for data sources.
  name: Contraforce Data sources API
  slug: contraforce-data-sources-api
- description: The Export API from Contraforce — 1 operation(s) for export.
  name: Contraforce Export API
  slug: contraforce-export-api
- description: The Gamebooks API from Contraforce — 5 operation(s) for gamebooks.
  name: Contraforce Gamebooks API
  slug: contraforce-gamebooks-api
- description: The Incidents API from Contraforce — 9 operation(s) for incidents.
  name: Contraforce Incidents API
  slug: contraforce-incidents-api
- description: The Investigation API from Contraforce — 2 operation(s) for investigation.
  name: Contraforce Investigation API
  slug: contraforce-investigation-api
- description: The Service accounts API from Contraforce — 7 operation(s) for service accounts.
  name: Contraforce Service accounts API
  slug: contraforce-service-accounts-api
- description: The Service tickets API from Contraforce — 4 operation(s) for service tickets.
  name: Contraforce Service tickets API
  slug: contraforce-service-tickets-api
- description: The Users API from Contraforce — 7 operation(s) for users.
  name: Contraforce Users API
  slug: contraforce-users-api
- description: The Webhooks API from Contraforce — 11 operation(s) for webhooks.
  name: Contraforce Webhooks API
  slug: contraforce-webhooks-api
artifact_total: 82
asyncapis:
- description: ''
  name: Contraforce Webhooks
  slug: contraforce-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/contraforce/finops/contraforce-finops.yml
  title: ''
  type: FinOps
  url: finops/contraforce-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.contraforce.com
- group: other
  href: https://artifacts.apis.io/contraforce/capabilities/contraforce-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/contraforce-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/contraforce/agentic-access/contraforce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/contraforce-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/contraforce/plans/contraforce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contraforce-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contraforce/rules/contraforce-rules.yml
  title: ''
  type: Spectral
  url: rules/contraforce-rules.yml
- group: design
  href: https://artifacts.apis.io/contraforce/json-ld/contraforce-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contraforce-context.jsonld
- group: design
  href: https://artifacts.apis.io/contraforce/vocabulary/contraforce-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contraforce-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/contraforce/asyncapi/contraforce-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/contraforce-webhooks.yml
- group: design
  href: https://artifacts.apis.io/contraforce/data-model/contraforce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contraforce-data-model.yml
- group: operate
  href: https://artifacts.apis.io/contraforce/changelog/contraforce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contraforce-changelog.yml
- group: auth
  href: https://artifacts.apis.io/contraforce/authentication/contraforce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contraforce-authentication.yml
- group: design
  href: https://artifacts.apis.io/contraforce/errors/contraforce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contraforce-problem-types.yml
- group: design
  href: https://artifacts.apis.io/contraforce/conformance/contraforce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contraforce-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contraforce/llms/contraforce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contraforce-llms.txt
- group: other
  href: https://artifacts.apis.io/contraforce/a2a/contraforce-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/contraforce-a2a.yml
- group: auth
  href: https://artifacts.apis.io/contraforce/well-known/contraforce-tickets-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contraforce-tickets-security.txt
- group: auth
  href: https://artifacts.apis.io/contraforce/well-known/contraforce-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contraforce-security.txt
- group: agent
  href: https://artifacts.apis.io/contraforce/well-known/contraforce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contraforce-well-known.yml
- group: other
  href: https://artifacts.apis.io/contraforce/hosts/contraforce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contraforce-hosts.yml
- group: other
  href: https://artifacts.apis.io/contraforce/vendors/contraforce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contraforce-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.contraforce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.contraforce.com/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://www.contraforce.com/signup
- group: auth
  title: ''
  type: Security
  url: https://www.contraforce.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.contraforce.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.contraforce.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.contraforce.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.contraforce.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.contraforce.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.contraforce.com/guides/getting-started/command-dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contraforce.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.contraforce.com/api-reference/endpoints
- group: auth
  href: https://artifacts.apis.io/contraforce/security/contraforce-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contraforce-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contraforce/security/contraforce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contraforce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.contraforce.com/
coverage:
  checked: '2026-10-11'
  detail: API reference page is a JavaScript‑rendered Mintlify site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.contraforce.com/api-reference/endpoints
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: ContraForce is the Agentic Security Delivery Platform for Microsoft security teams, MSPs, MSSPs, and security operations teams. It provides AI‑powered triage, investigation, response, tuning, ticketing, and reporting on Microsoft Defender XDR and Sentinel. The platform offers a free 30‑day trial with no credit card required, enabling service providers to scale SOC delivery without hiring additional analysts.
finops:
- has_sources: true
  method: derived
  name: Contraforce Finops
  primary_unit: subscription
  service_category: ''
  slug: contraforce-finops
  template: false
image: https://www.contraforce.com/og-image.png
json_schemas:
- name: AgentToolGamebookSubmissionRequest
  property_count: 4
  slug: contraforce-agent-tool-gamebook-submission-request
- name: AgentToolInvestigationSubmissionRequest
  property_count: 9
  slug: contraforce-agent-tool-investigation-submission-request
- name: AgentToolKqlQueryRequest
  property_count: 2
  slug: contraforce-agent-tool-kql-query-request
- name: AgentToolKqlTableColumnsRequest
  property_count: 1
  slug: contraforce-agent-tool-kql-table-columns-request
- name: ApiResponseOfAgentToolKqlQueryResult
  property_count: 2
  slug: contraforce-api-response-of-agent-tool-kql-query-result
- name: ApiResponseOfAgentToolUserDetailsResult
  property_count: 2
  slug: contraforce-api-response-of-agent-tool-user-details-result
- name: ApiResponseOfAuditLogsResultDto
  property_count: 2
  slug: contraforce-api-response-of-audit-logs-result-dto
- name: ApiResponseOfBulkUpdateIncidentResultDto
  property_count: 2
  slug: contraforce-api-response-of-bulk-update-incident-result-dto
- name: ApiResponseOfContraForceIncident
  property_count: 2
  slug: contraforce-api-response-of-contra-force-incident
- name: ApiResponseOfDataConnectorAnomaliesDto
  property_count: 2
  slug: contraforce-api-response-of-data-connector-anomalies-dto
- name: ApiResponseOfDataConnectorWorkspacesDto
  property_count: 2
  slug: contraforce-api-response-of-data-connector-workspaces-dto
- name: ApiResponseOfIEnumerableOfAzureResourceDto
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-azure-resource-dto
- name: ApiResponseOfIEnumerableOfAzureSubscriptionDto
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-azure-subscription-dto
- name: ApiResponseOfIEnumerableOfDataSource
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-data-source
- name: ApiResponseOfIEnumerableOfGamebookDto
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-gamebook-dto
- name: ApiResponseOfIEnumerableOfNetworkSecurityGroupDto
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-network-security-group-dto
- name: ApiResponseOfIEnumerableOfPlaybookGameplanDto
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-playbook-gameplan-dto
- name: ApiResponseOfIEnumerableOfPlaybookMetadataDto
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-playbook-metadata-dto
- name: ApiResponseOfIEnumerableOfUser
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-user
- name: ApiResponseOfIEnumerableOfWorkspaceUserDto
  property_count: 2
  slug: contraforce-api-response-of-ienumerable-of-workspace-user-dto
- name: ApiResponseOfListGamebooksResultDto
  property_count: 2
  slug: contraforce-api-response-of-list-gamebooks-result-dto
- name: ApiResponseOfListIncidentsForWorkspacesResultDto
  property_count: 2
  slug: contraforce-api-response-of-list-incidents-for-workspaces-result-dto
- name: ApiResponseOfPageListOfGamebookDto
  property_count: 2
  slug: contraforce-api-response-of-page-list-of-gamebook-dto
- name: ApiResponseOfPagedResultOfWebhookDeliveryLogDto
  property_count: 2
  slug: contraforce-api-response-of-paged-result-of-webhook-delivery-log-dto
- name: ApiResponseOfRunGamebookResponse
  property_count: 2
  slug: contraforce-api-response-of-run-gamebook-response
- name: ApiResponseOfSendTestWebhookResult
  property_count: 2
  slug: contraforce-api-response-of-send-test-webhook-result
- name: ApiResponseOfSentinelIngestDeploymentCardDto
  property_count: 2
  slug: contraforce-api-response-of-sentinel-ingest-deployment-card-dto
- name: ApiResponseOfServiceAccountCreatedDto
  property_count: 2
  slug: contraforce-api-response-of-service-account-created-dto
- name: ApiResponseOfServiceAccountCredentialCreatedDto
  property_count: 2
  slug: contraforce-api-response-of-service-account-credential-created-dto
- name: ApiResponseOfServiceTicketResponse
  property_count: 2
  slug: contraforce-api-response-of-service-ticket-response
- name: ApiResponseOfSignInLogsResultDto
  property_count: 2
  slug: contraforce-api-response-of-sign-in-logs-result-dto
- name: ApiResponseOfUser
  property_count: 2
  slug: contraforce-api-response-of-user
- name: ApiResponseOfWebhookSecretRegeneratedDto
  property_count: 2
  slug: contraforce-api-response-of-webhook-secret-regenerated-dto
- name: ApiResponseOfboolean
  property_count: 2
  slug: contraforce-api-response-ofboolean
- name: AssignIncidentRequest
  property_count: 2
  slug: contraforce-assign-incident-request
- name: BulkUpdateIncidentsRequest
  property_count: 1
  slug: contraforce-bulk-update-incidents-request
- name: CreateIncidentCommentRequest
  property_count: 2
  slug: contraforce-create-incident-comment-request
- name: CreateServiceAccountRequest
  property_count: 6
  slug: contraforce-create-service-account-request
- name: CreateWebhookConfigurationRequest
  property_count: 10
  slug: contraforce-create-webhook-configuration-request
- name: ExportAuditResponse
  property_count: 2
  slug: contraforce-export-audit-response
- name: GetWorkspaceUsersRequest
  property_count: 3
  slug: contraforce-get-workspace-users-request
- name: IngestIncidentRequest
  property_count: 4
  slug: contraforce-ingest-incident-request
- name: LinkServiceTicketRequest
  property_count: 2
  slug: contraforce-link-service-ticket-request
- name: ListIncidentsAcrossWorkspacesRequest
  property_count: 11
  slug: contraforce-list-incidents-across-workspaces-request
- name: ListMultipleWorkspacesGeneralRequestDto
  property_count: 2
  slug: contraforce-list-multiple-workspaces-general-request-dto
- name: PaginatedApiResponseOfServiceTicketResponse
  property_count: 3
  slug: contraforce-paginated-api-response-of-service-ticket-response
- name: ProvisionSentinelIngestRequest
  property_count: 1
  slug: contraforce-provision-sentinel-ingest-request
- name: RunGamebookRequest
  property_count: 6
  slug: contraforce-run-gamebook-request
- name: ServiceTicketUpdatePriorityRequest
  property_count: 6
  slug: contraforce-service-ticket-update-priority-request
- name: SubmitAddUsersRequest
  property_count: 2
  slug: contraforce-submit-add-users-request
- name: SubmitUserManagementRequest
  property_count: 6
  slug: contraforce-submit-user-management-request
- name: UnlinkServiceTicketRequest
  property_count: 1
  slug: contraforce-unlink-service-ticket-request
- name: UpdateIncidentCommentRequest
  property_count: 2
  slug: contraforce-update-incident-comment-request
- name: UpdateIncidentStatusRequest
  property_count: 6
  slug: contraforce-update-incident-status-request
- name: UpdateServiceAccountRequest
  property_count: 4
  slug: contraforce-update-service-account-request
- name: UpdateWebhookConfigurationRequest
  property_count: 4
  slug: contraforce-update-webhook-configuration-request
- name: UpdateWebhookCredentialsRequest
  property_count: 5
  slug: contraforce-update-webhook-credentials-request
jsonld:
- class_count: 120
  name: Contraforce Context
  property_count: 238
  slug: contraforce-context
layout: provider
modified: '2026-10-10'
name: Contraforce
nav: Providers
network: true
overview: 'Contraforce publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Tools API, Azure resources API, Cross-workspace data sources API, and 12 more. Tagged areas include Security, Software-as-a-Service, Cybersecurity, Microsoft, and MSP.


  The Contraforce catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Contraforce''s developer surface includes changelog, authentication, signup flow, pricing, engineering blog, getting-started guide, documentation, and 29 more developer resources.'
plans:
- name: Contraforce Plans Pricing
  plan_count: 3
  slug: contraforce-plans-pricing
- name: Contraforce Price Estimates
  plan_count: 0
  slug: contraforce-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Contraforce API Rules
  rule_count: 38
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 4
  slug: contraforce-rules
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 63.4
    developer_ergonomics: 36.9
    discoverability: 65.2
    operational_transparency: 21.1
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/contraforce/contraforce-2026-11-03T125220.png
security:
- kind: authentication
  name: Contraforce Authentication
  slug: contraforce-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Contraforce Domain Security
  slug: contraforce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contraforce Vulnerability Disclosure
  slug: contraforce-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: contraforce
tags:
- Security
- Software-as-a-Service
- Cybersecurity
- Microsoft
- MSP
website: https://www.contraforce.com/
---
