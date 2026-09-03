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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 127
  human_in_the_loop: 1
  name: Microsoft Purview Agentic Access
  operation_count: 214
  slug: microsoft-purview-agentic-access
  summary_line: 214 operations · 127 acting · 1 human-in-the-loop
api_count: 12
apis:
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing Purview accounts
  name: Microsoft Purview Accounts API
  slug: microsoft-purview-accounts-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for approving or rejecting workflow tasks
  name: Microsoft Purview Approval API
  slug: microsoft-purview-approval-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing business domains
  name: Microsoft Purview Business Domains API
  slug: microsoft-purview-business-domains-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing eDiscovery cases
  name: Microsoft Purview Cases API
  slug: microsoft-purview-cases-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing classification rules
  name: Microsoft Purview Classification Rules API
  slug: microsoft-purview-classification-rules-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing critical data elements
  name: Microsoft Purview Critical Data Elements API
  slug: microsoft-purview-critical-data-elements-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing custodians within cases
  name: Microsoft Purview Custodians API
  slug: microsoft-purview-custodians-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing data products
  name: Microsoft Purview Data Products API
  slug: microsoft-purview-data-products-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for data profiling operations
  name: Microsoft Purview Data Profiling API
  slug: microsoft-purview-data-profiling-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing data quality rules
  name: Microsoft Purview Data Quality Rules API
  slug: microsoft-purview-data-quality-rules-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for running data quality scans
  name: Microsoft Purview Data Quality Scans API
  slug: microsoft-purview-data-quality-scans-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for retrieving data quality scores
  name: Microsoft Purview Data Quality Scores API
  slug: microsoft-purview-data-quality-scores-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing data source registrations
  name: Microsoft Purview Data Sources API
  slug: microsoft-purview-data-sources-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for searching and discovering data assets
  name: Microsoft Purview Discovery API
  slug: microsoft-purview-discovery-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for evaluating DLP policies on content
  name: Microsoft Purview DLP Policies API
  slug: microsoft-purview-dlp-policies-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing catalog entities
  name: Microsoft Purview Entity API
  slug: microsoft-purview-entity-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing glossary terms, categories, and assignments
  name: Microsoft Purview Glossary API
  slug: microsoft-purview-glossary-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing glossary terms in the unified catalog
  name: Microsoft Purview Glossary Terms API
  slug: microsoft-purview-glossary-terms-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing label policy settings
  name: Microsoft Purview Label Policy Settings API
  slug: microsoft-purview-label-policy-settings-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing legal holds
  name: Microsoft Purview Legal Holds API
  slug: microsoft-purview-legal-holds-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for tracking data lineage
  name: Microsoft Purview Lineage API
  slug: microsoft-purview-lineage-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing metadata policies
  name: Microsoft Purview Metadata Policy API
  slug: microsoft-purview-metadata-policy-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing metadata roles
  name: Microsoft Purview Metadata Roles API
  slug: microsoft-purview-metadata-roles-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing Objectives and Key Results
  name: Microsoft Purview OKRs API
  slug: microsoft-purview-okrs-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations available on the Purview resource provider
  name: Microsoft Purview Operations API
  slug: microsoft-purview-operations-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing private endpoint connections
  name: Microsoft Purview Private Endpoint Connections API
  slug: microsoft-purview-private-endpoint-connections-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for computing protection scopes
  name: Microsoft Purview Protection Scopes API
  slug: microsoft-purview-protection-scopes-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing relationships between entities
  name: Microsoft Purview Relationship API
  slug: microsoft-purview-relationship-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing retention event types
  name: Microsoft Purview Retention Event Types API
  slug: microsoft-purview-retention-event-types-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing retention events
  name: Microsoft Purview Retention Events API
  slug: microsoft-purview-retention-events-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing retention labels
  name: Microsoft Purview Retention Labels API
  slug: microsoft-purview-retention-labels-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing review sets
  name: Microsoft Purview Review Sets API
  slug: microsoft-purview-review-sets-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for running scans and viewing scan results
  name: Microsoft Purview Scan Result API
  slug: microsoft-purview-scan-result-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing scan rulesets
  name: Microsoft Purview Scan Rulesets API
  slug: microsoft-purview-scan-rulesets-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing scan configurations
  name: Microsoft Purview Scans API
  slug: microsoft-purview-scans-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing eDiscovery searches
  name: Microsoft Purview Searches API
  slug: microsoft-purview-searches-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for accessing tenant-level sensitivity labels
  name: Microsoft Purview Sensitivity Labels API
  slug: microsoft-purview-sensitivity-labels-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing scan triggers and schedules
  name: Microsoft Purview Triggers API
  slug: microsoft-purview-triggers-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing type definitions
  name: Microsoft Purview Type API
  slug: microsoft-purview-type-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for submitting user requests
  name: Microsoft Purview User Requests API
  slug: microsoft-purview-user-requests-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing individual workflows
  name: Microsoft Purview Workflow API
  slug: microsoft-purview-workflow-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing workflow runs
  name: Microsoft Purview Workflow Run API
  slug: microsoft-purview-workflow-run-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing workflow tasks
  name: Microsoft Purview Workflow Task API
  slug: microsoft-purview-workflow-task-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for listing workflows
  name: Microsoft Purview Workflows API
  slug: microsoft-purview-workflows-api
arazzos:
- description: Create a glossary term and assign it to one or more catalog entities.
  name: Microsoft Purview Assign a Glossary Term to Entities
  slug: microsoft-purview-assign-term-to-entities-workflow
- description: Create a glossary category and a term that is filed under that category.
  name: Microsoft Purview Categorize a Glossary Term
  slug: microsoft-purview-categorize-glossary-term-workflow
- description: Register a catalog entity, confirm it, then apply and verify a classification.
  name: Microsoft Purview Classify a Data Asset Entity
  slug: microsoft-purview-classify-entity-workflow
- description: Register a custom classification typedef, confirm it, then classify an entity with it.
  name: Microsoft Purview Define a Classification Type and Apply It
  slug: microsoft-purview-define-and-apply-classification-type-workflow
- description: Create a data quality rule, confirm it, then run a quality scan that evaluates it.
  name: Microsoft Purview Define a Data Quality Rule and Scan
  slug: microsoft-purview-define-rule-and-scan-quality-workflow
- description: Search the catalog, then move the discovered entities into a target collection.
  name: Microsoft Purview Move Found Entities into a Collection
  slug: microsoft-purview-move-entities-to-collection-workflow
- description: Create a Data Map entity, confirm it, move it into a collection, and classify it.
  name: Microsoft Purview Onboard an Entity into a Collection
  slug: microsoft-purview-onboard-entity-to-collection-workflow
- description: Kick off data profiling for an asset, then poll until the profiling completes.
  name: Microsoft Purview Profile a Data Asset and Poll for Results
  slug: microsoft-purview-profile-asset-and-poll-workflow
- description: Create a custom classification rule, build a scan ruleset that uses it, and confirm.
  name: Microsoft Purview Provision a Custom Scan Ruleset
  slug: microsoft-purview-provision-scan-ruleset-workflow
- description: Create a business domain, confirm it, then publish a data product under it.
  name: Microsoft Purview Publish a Data Product
  slug: microsoft-purview-publish-data-product-workflow
- description: Create a glossary, confirm it, then create a term anchored to that glossary.
  name: Microsoft Purview Publish a Glossary Term
  slug: microsoft-purview-publish-glossary-term-workflow
- description: Register a data source, configure a scan, and kick off a scan run.
  name: Microsoft Purview Register a Data Source and Launch a Scan
  slug: microsoft-purview-register-source-and-scan-workflow
- description: Create an entity, then create a relationship linking it to another entity.
  name: Microsoft Purview Relate Two Catalog Entities
  slug: microsoft-purview-relate-entities-workflow
- description: Launch a scan run, then poll scan history until the run reaches a terminal state.
  name: Microsoft Purview Run a Scan and Poll to Completion
  slug: microsoft-purview-run-and-poll-scan-workflow
- description: Configure a scan, attach a recurring trigger, enable it, and confirm the schedule.
  name: Microsoft Purview Schedule a Recurring Scan
  slug: microsoft-purview-schedule-recurring-scan-workflow
- description: Search the catalog, read the top hit, and apply a classification to it.
  name: Microsoft Purview Search and Classify a Found Asset
  slug: microsoft-purview-search-and-classify-workflow
- description: Search for an asset, read its entity, then walk its lineage graph with pagination.
  name: Microsoft Purview Trace Data Asset Lineage
  slug: microsoft-purview-trace-asset-lineage-workflow
artifact_total: 279
collections:
- collection_type: postman
  name: Microsoft Purview Account API
  slug: postman-microsoft-purview-account
- collection_type: postman
  name: Microsoft Purview Catalog API
  slug: postman-microsoft-purview-catalog
- collection_type: postman
  name: Microsoft Purview Data Map API
  slug: postman-microsoft-purview-data-map
- collection_type: postman
  name: Microsoft Purview Data Quality API
  slug: postman-microsoft-purview-data-quality
- collection_type: postman
  name: Microsoft Purview Data Security and Governance API
  slug: postman-microsoft-purview-data-security-governance
- collection_type: postman
  name: Microsoft Purview eDiscovery API
  slug: postman-microsoft-purview-ediscovery
- collection_type: postman
  name: Microsoft Purview Information Protection API
  slug: postman-microsoft-purview-information-protection
- collection_type: postman
  name: Microsoft Purview Metadata Policies API
  slug: postman-microsoft-purview-metadata-policies
- collection_type: postman
  name: Microsoft Purview Records Management API
  slug: postman-microsoft-purview-records-management
- collection_type: postman
  name: Microsoft Purview Scanning API
  slug: postman-microsoft-purview-scanning
- collection_type: postman
  name: Microsoft Purview Unified Catalog API
  slug: postman-microsoft-purview-unified-catalog
- collection_type: postman
  name: Microsoft Purview Workflow API
  slug: postman-microsoft-purview-workflow
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Purview Account API
  slug: open-microsoft-purview-account
- collection_type: open
  name: Microsoft Purview Account Accounts API
  slug: open-microsoft-purview-accounts-api
- collection_type: open
  name: Microsoft Purview Account Accounts Approval API
  slug: open-microsoft-purview-approval-api
- collection_type: open
  name: Microsoft Purview Account Accounts Business Domains API
  slug: open-microsoft-purview-business-domains-api
- collection_type: open
  name: Microsoft Purview Account Accounts Cases API
  slug: open-microsoft-purview-cases-api
- collection_type: open
  name: Microsoft Purview Catalog API
  slug: open-microsoft-purview-catalog
- collection_type: open
  name: Microsoft Purview Account Accounts Classification Rules API
  slug: open-microsoft-purview-classification-rules-api
- collection_type: open
  name: Microsoft Purview Account Accounts Critical Data Elements API
  slug: open-microsoft-purview-critical-data-elements-api
- collection_type: open
  name: Microsoft Purview Account Accounts Custodians API
  slug: open-microsoft-purview-custodians-api
- collection_type: open
  name: Microsoft Purview Data Map API
  slug: open-microsoft-purview-data-map
- collection_type: open
  name: Microsoft Purview Account Accounts Data Products API
  slug: open-microsoft-purview-data-products-api
- collection_type: open
  name: Microsoft Purview Account Accounts Data Profiling API
  slug: open-microsoft-purview-data-profiling-api
- collection_type: open
  name: Microsoft Purview Account Accounts Data Quality Rules API
  slug: open-microsoft-purview-data-quality-rules-api
- collection_type: open
  name: Microsoft Purview Account Accounts Data Quality Scans API
  slug: open-microsoft-purview-data-quality-scans-api
- collection_type: open
  name: Microsoft Purview Account Accounts Data Quality Scores API
  slug: open-microsoft-purview-data-quality-scores-api
- collection_type: open
  name: Microsoft Purview Data Quality API
  slug: open-microsoft-purview-data-quality
- collection_type: open
  name: Microsoft Purview Data Security and Governance API
  slug: open-microsoft-purview-data-security-governance
- collection_type: open
  name: Microsoft Purview Account Accounts Data Sources API
  slug: open-microsoft-purview-data-sources-api
- collection_type: open
  name: Microsoft Purview Account Accounts Discovery API
  slug: open-microsoft-purview-discovery-api
- collection_type: open
  name: Microsoft Purview Account Accounts DLP Policies API
  slug: open-microsoft-purview-dlp-policies-api
- collection_type: open
  name: Microsoft Purview eDiscovery API
  slug: open-microsoft-purview-ediscovery
- collection_type: open
  name: Microsoft Purview Account Accounts Entity API
  slug: open-microsoft-purview-entity-api
- collection_type: open
  name: Microsoft Purview Account Accounts Glossary API
  slug: open-microsoft-purview-glossary-api
- collection_type: open
  name: Microsoft Purview Account Accounts Glossary Terms API
  slug: open-microsoft-purview-glossary-terms-api
- collection_type: open
  name: Microsoft Purview Information Protection API
  slug: open-microsoft-purview-information-protection
- collection_type: open
  name: Microsoft Purview Account Accounts Label Policy Settings API
  slug: open-microsoft-purview-label-policy-settings-api
- collection_type: open
  name: Microsoft Purview Account Accounts Legal Holds API
  slug: open-microsoft-purview-legal-holds-api
- collection_type: open
  name: Microsoft Purview Account Accounts Lineage API
  slug: open-microsoft-purview-lineage-api
- collection_type: open
  name: Microsoft Purview Metadata Policies API
  slug: open-microsoft-purview-metadata-policies
- collection_type: open
  name: Microsoft Purview Account Accounts Metadata Policy API
  slug: open-microsoft-purview-metadata-policy-api
- collection_type: open
  name: Microsoft Purview Account Accounts Metadata Roles API
  slug: open-microsoft-purview-metadata-roles-api
- collection_type: open
  name: Microsoft Purview Account Accounts OKRs API
  slug: open-microsoft-purview-okrs-api
- collection_type: open
  name: Microsoft Purview Account Accounts Operations API
  slug: open-microsoft-purview-operations-api
- collection_type: open
  name: Microsoft Purview Account Accounts Private Endpoint Connections API
  slug: open-microsoft-purview-private-endpoint-connections-api
- collection_type: open
  name: Microsoft Purview Account Accounts Protection Scopes API
  slug: open-microsoft-purview-protection-scopes-api
- collection_type: open
  name: Microsoft Purview Records Management API
  slug: open-microsoft-purview-records-management
- collection_type: open
  name: Microsoft Purview Account Accounts Relationship API
  slug: open-microsoft-purview-relationship-api
- collection_type: open
  name: Microsoft Purview Account Accounts Retention Event Types API
  slug: open-microsoft-purview-retention-event-types-api
- collection_type: open
  name: Microsoft Purview Account Accounts Retention Events API
  slug: open-microsoft-purview-retention-events-api
- collection_type: open
  name: Microsoft Purview Account Accounts Retention Labels API
  slug: open-microsoft-purview-retention-labels-api
- collection_type: open
  name: Microsoft Purview Account Accounts Scan Result API
  slug: open-microsoft-purview-scan-result-api
- collection_type: open
  name: Microsoft Purview Account Accounts Scan Rulesets API
  slug: open-microsoft-purview-scan-rulesets-api
- collection_type: open
  name: Microsoft Purview Scanning API
  slug: open-microsoft-purview-scanning
- collection_type: open
  name: Microsoft Purview Account Accounts Scans API
  slug: open-microsoft-purview-scans-api
- collection_type: open
  name: Microsoft Purview Account Accounts Searches API
  slug: open-microsoft-purview-searches-api
- collection_type: open
  name: Microsoft Purview Account Accounts Sensitivity Labels API
  slug: open-microsoft-purview-sensitivity-labels-api
- collection_type: open
  name: Microsoft Purview Account Accounts Triggers API
  slug: open-microsoft-purview-triggers-api
- collection_type: open
  name: Microsoft Purview Account Accounts Type API
  slug: open-microsoft-purview-type-api
- collection_type: open
  name: Microsoft Purview Unified Catalog API
  slug: open-microsoft-purview-unified-catalog
- collection_type: open
  name: Microsoft Purview Account Accounts User Requests API
  slug: open-microsoft-purview-user-requests-api
- collection_type: open
  name: Microsoft Purview Account Accounts Workflow API
  slug: open-microsoft-purview-workflow-api
- collection_type: open
  name: Microsoft Purview Account Accounts Workflow Run API
  slug: open-microsoft-purview-workflow-run-api
- collection_type: open
  name: Microsoft Purview Account Accounts Workflow Task API
  slug: open-microsoft-purview-workflow-task-api
- collection_type: open
  name: Microsoft Purview Workflow API
  slug: open-microsoft-purview-workflow
- collection_type: open
  name: Microsoft Purview Account Accounts Workflows API
  slug: open-microsoft-purview-workflows-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-purview-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-purview-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-purview-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-purview-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-purview-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-purview-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-purview-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-purview-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-purview-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-purview-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-purview-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-purview-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-purview-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-purview-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-purview-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-purview-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-purview-changelog.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-account-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-catalog-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-data-map-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-data-quality-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-data-security-governance-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-ediscovery-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-information-protection-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-metadata-policies-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-records-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-scanning-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-unified-catalog-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-workflow-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-purview/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-assign-term-to-entities-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-categorize-glossary-term-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-classify-entity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-define-and-apply-classification-type-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-define-rule-and-scan-quality-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-move-entities-to-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-onboard-entity-to-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-profile-asset-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-provision-scan-ruleset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-publish-data-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-publish-glossary-term-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-register-source-and-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-relate-entities-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-run-and-poll-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-schedule-recurring-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-search-and-classify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-trace-asset-lineage-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://purview.microsoft.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/purview/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/purview/use-azure-purview-studio
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/purview/data-gov-api-rest-data-plane
- group: docs
  title: ''
  type: Reference
  url: https://learn.microsoft.com/en-us/rest/api/purview/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/purview/data-gov-python-sdk
- group: other
  title: ''
  type: Best Practices
  url: https://learn.microsoft.com/en-us/purview/concept-best-practices-accounts
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/purview/whats-new
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/microsoft-purview-blog/bg-p/MicrosoftPurviewBlog
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/answers/topics/azure-purview.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/purview
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/microsoft-purview/ct-p/MicrosoftPurview
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/security/business/microsoft-purview
- group: start
  title: ''
  type: Login
  url: https://purview.microsoft.com
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/products/purview/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/microsoft-purview-context.jsonld
created: 2024-01-15 00:00:00+00:00
description: Microsoft Purview is a comprehensive data governance service that helps organizations discover, catalog, classify, and manage their data estate across on-premises, multi-cloud, and SaaS environments.
finops:
- name: Microsoft Purview Finops
  service_category: Compliance / Data Governance
  slug: microsoft-purview-finops
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2021/04/Microsoft-Purview-logo.png
json_schemas:
- name: AccessKeys
  property_count: 2
  slug: microsoft-purview-accesskeys
- name: Microsoft Purview Account
  property_count: 8
  slug: microsoft-purview-account
- name: AccountEndpoints
  property_count: 3
  slug: microsoft-purview-accountendpoints
- name: AccountList
  property_count: 3
  slug: microsoft-purview-accountlist
- name: AccountProperties
  property_count: 11
  slug: microsoft-purview-accountproperties
- name: AccountSku
  property_count: 2
  slug: microsoft-purview-accountsku
- name: AccountUpdateParameters
  property_count: 3
  slug: microsoft-purview-accountupdateparameters
- name: AtlasClassification
  property_count: 8
  slug: microsoft-purview-atlasclassification
- name: AtlasClassifications
  property_count: 6
  slug: microsoft-purview-atlasclassifications
- name: AtlasEntitiesWithExtInfo
  property_count: 2
  slug: microsoft-purview-atlasentitieswithextinfo
- name: AtlasEntity
  property_count: 19
  slug: microsoft-purview-atlasentity
- name: AtlasEntityHeader
  property_count: 11
  slug: microsoft-purview-atlasentityheader
- name: AtlasEntityHeaders
  property_count: 1
  slug: microsoft-purview-atlasentityheaders
- name: AtlasEntityWithExtInfo
  property_count: 2
  slug: microsoft-purview-atlasentitywithextinfo
- name: AtlasGlossary
  property_count: 9
  slug: microsoft-purview-atlasglossary
- name: AtlasGlossaryCategory
  property_count: 9
  slug: microsoft-purview-atlasglossarycategory
- name: AtlasGlossaryHeader
  property_count: 3
  slug: microsoft-purview-atlasglossaryheader
- name: AtlasGlossaryTerm
  property_count: 13
  slug: microsoft-purview-atlasglossaryterm
- name: AtlasLineageInfo
  property_count: 8
  slug: microsoft-purview-atlaslineageinfo
- name: AtlasObjectId
  property_count: 3
  slug: microsoft-purview-atlasobjectid
- name: AtlasRelatedCategoryHeader
  property_count: 5
  slug: microsoft-purview-atlasrelatedcategoryheader
- name: AtlasRelatedObjectId
  property_count: 8
  slug: microsoft-purview-atlasrelatedobjectid
- name: AtlasRelatedTermHeader
  property_count: 7
  slug: microsoft-purview-atlasrelatedtermheader
- name: AtlasRelationship
  property_count: 15
  slug: microsoft-purview-atlasrelationship
- name: AtlasRelationshipWithExtInfo
  property_count: 2
  slug: microsoft-purview-atlasrelationshipwithextinfo
- name: AtlasTermAssignmentHeader
  property_count: 9
  slug: microsoft-purview-atlastermassignmentheader
- name: AtlasTermCategorizationHeader
  property_count: 5
  slug: microsoft-purview-atlastermcategorizationheader
- name: AtlasTypeDef
  property_count: 13
  slug: microsoft-purview-atlastypedef
- name: AtlasTypeDefHeader
  property_count: 3
  slug: microsoft-purview-atlastypedefheader
- name: AtlasTypesDef
  property_count: 7
  slug: microsoft-purview-atlastypesdef
- name: AttributeMatcher
  property_count: 5
  slug: microsoft-purview-attributematcher
- name: AttributeRule
  property_count: 4
  slug: microsoft-purview-attributerule
- name: AuthorityTemplate
  property_count: 2
  slug: microsoft-purview-authoritytemplate
- name: AutoCompleteRequest
  property_count: 3
  slug: microsoft-purview-autocompleterequest
- name: AutoCompleteResult
  property_count: 1
  slug: microsoft-purview-autocompleteresult
- name: AutoCompleteResultValue
  property_count: 2
  slug: microsoft-purview-autocompleteresultvalue
- name: BusinessDomain
  property_count: 9
  slug: microsoft-purview-businessdomain
- name: BusinessDomainList
  property_count: 2
  slug: microsoft-purview-businessdomainlist
- name: CategoryTemplate
  property_count: 2
  slug: microsoft-purview-categorytemplate
- name: CheckNameAvailabilityRequest
  property_count: 2
  slug: microsoft-purview-checknameavailabilityrequest
- name: CheckNameAvailabilityResult
  property_count: 3
  slug: microsoft-purview-checknameavailabilityresult
- name: CitationTemplate
  property_count: 4
  slug: microsoft-purview-citationtemplate
- name: Microsoft Purview Classification
  property_count: 8
  slug: microsoft-purview-classification
- name: ClassificationResult
  property_count: 3
  slug: microsoft-purview-classificationresult
- name: ClassificationRule
  property_count: 4
  slug: microsoft-purview-classificationrule
- name: ClassificationRuleList
  property_count: 3
  slug: microsoft-purview-classificationrulelist
- name: ClassificationRulePattern
  property_count: 2
  slug: microsoft-purview-classificationrulepattern
- name: CollectionAdminUpdate
  property_count: 1
  slug: microsoft-purview-collectionadminupdate
- name: CollectionReference
  property_count: 2
  slug: microsoft-purview-collectionreference
- name: ColumnProfile
  property_count: 10
  slug: microsoft-purview-columnprofile
- name: ConnectedVia
  property_count: 2
  slug: microsoft-purview-connectedvia
- name: ContentInfo
  property_count: 4
  slug: microsoft-purview-contentinfo
- name: CriticalDataElement
  property_count: 8
  slug: microsoft-purview-criticaldataelement
- name: CriticalDataElementList
  property_count: 2
  slug: microsoft-purview-criticaldataelementlist
- name: Microsoft Purview Data Source
  property_count: 4
  slug: microsoft-purview-data-source
- name: DataProduct
  property_count: 9
  slug: microsoft-purview-dataproduct
- name: DataProductList
  property_count: 2
  slug: microsoft-purview-dataproductlist
- name: DataQualityRule
  property_count: 11
  slug: microsoft-purview-dataqualityrule
- name: DataQualityRuleList
  property_count: 2
  slug: microsoft-purview-dataqualityrulelist
- name: DataQualityScanRequest
  property_count: 2
  slug: microsoft-purview-dataqualityscanrequest
- name: DataQualityScanResult
  property_count: 3
  slug: microsoft-purview-dataqualityscanresult
- name: DataQualityScore
  property_count: 7
  slug: microsoft-purview-dataqualityscore
- name: DataQualityScoreList
  property_count: 2
  slug: microsoft-purview-dataqualityscorelist
- name: DataSource
  property_count: 5
  slug: microsoft-purview-datasource
- name: DataSourceList
  property_count: 3
  slug: microsoft-purview-datasourcelist
- name: DecisionRule
  property_count: 3
  slug: microsoft-purview-decisionrule
- name: DepartmentTemplate
  property_count: 2
  slug: microsoft-purview-departmenttemplate
- name: DlpAction
  property_count: 3
  slug: microsoft-purview-dlpaction
- name: DlpMatchedRule
  property_count: 6
  slug: microsoft-purview-dlpmatchedrule
- name: DowngradeJustification
  property_count: 2
  slug: microsoft-purview-downgradejustification
- name: EdiscoveryCase
  property_count: 10
  slug: microsoft-purview-ediscoverycase
- name: EdiscoveryCustodian
  property_count: 8
  slug: microsoft-purview-ediscoverycustodian
- name: EdiscoveryHoldPolicy
  property_count: 9
  slug: microsoft-purview-ediscoveryholdpolicy
- name: EdiscoveryReviewSet
  property_count: 4
  slug: microsoft-purview-ediscoveryreviewset
- name: EdiscoverySearch
  property_count: 8
  slug: microsoft-purview-ediscoverysearch
- name: Microsoft Purview Atlas Entity
  property_count: 19
  slug: microsoft-purview-entity
- name: EntityMutationResponse
  property_count: 3
  slug: microsoft-purview-entitymutationresponse
- name: FilePlanReferenceTemplate
  property_count: 2
  slug: microsoft-purview-fileplanreferencetemplate
- name: Microsoft Purview Glossary Term
  property_count: 17
  slug: microsoft-purview-glossary-term
- name: GlossaryTermList
  property_count: 2
  slug: microsoft-purview-glossarytermlist
- name: GovernanceContact
  property_count: 3
  slug: microsoft-purview-governancecontact
- name: Identity
  property_count: 4
  slug: microsoft-purview-identity
- name: IdentitySet
  property_count: 3
  slug: microsoft-purview-identityset
- name: InformationProtectionAction
  property_count: 1
  slug: microsoft-purview-informationprotectionaction
- name: InformationProtectionPolicySetting
  property_count: 5
  slug: microsoft-purview-informationprotectionpolicysetting
- name: KeyValuePair
  property_count: 2
  slug: microsoft-purview-keyvaluepair
- name: LabelingOptions
  property_count: 2
  slug: microsoft-purview-labelingoptions
- name: LineageRelation
  property_count: 3
  slug: microsoft-purview-lineagerelation
- name: MetadataPolicy
  property_count: 4
  slug: microsoft-purview-metadatapolicy
- name: MetadataPolicyList
  property_count: 2
  slug: microsoft-purview-metadatapolicylist
- name: MetadataRole
  property_count: 4
  slug: microsoft-purview-metadatarole
- name: MetadataRoleList
  property_count: 2
  slug: microsoft-purview-metadatarolelist
- name: MoveEntitiesRequest
  property_count: 1
  slug: microsoft-purview-moveentitiesrequest
- name: OKR
  property_count: 9
  slug: microsoft-purview-okr
- name: OKRList
  property_count: 2
  slug: microsoft-purview-okrlist
- name: Operation
  property_count: 4
  slug: microsoft-purview-operation
- name: OperationList
  property_count: 3
  slug: microsoft-purview-operationlist
- name: OperationResponse
  property_count: 2
  slug: microsoft-purview-operationresponse
- name: ParentRelation
  property_count: 3
  slug: microsoft-purview-parentrelation
- name: PrivateEndpointConnection
  property_count: 4
  slug: microsoft-purview-privateendpointconnection
- name: PrivateEndpointConnectionList
  property_count: 3
  slug: microsoft-purview-privateendpointconnectionlist
- name: ProfilingRequest
  property_count: 2
  slug: microsoft-purview-profilingrequest
- name: ProfilingResult
  property_count: 5
  slug: microsoft-purview-profilingresult
- name: ProtectionScope
  property_count: 4
  slug: microsoft-purview-protectionscope
- name: RecurrenceSchedule
  property_count: 4
  slug: microsoft-purview-recurrenceschedule
- name: ResourceLink
  property_count: 2
  slug: microsoft-purview-resourcelink
- name: Microsoft Purview Retention Label
  property_count: 12
  slug: microsoft-purview-retention-label
- name: RetentionEvent
  property_count: 11
  slug: microsoft-purview-retentionevent
- name: RetentionEventType
  property_count: 7
  slug: microsoft-purview-retentioneventtype
- name: RetentionLabel
  property_count: 17
  slug: microsoft-purview-retentionlabel
- name: RuleResult
  property_count: 5
  slug: microsoft-purview-ruleresult
- name: Microsoft Purview Scan
  property_count: 4
  slug: microsoft-purview-scan
- name: ScanList
  property_count: 3
  slug: microsoft-purview-scanlist
- name: ScanResult
  property_count: 13
  slug: microsoft-purview-scanresult
- name: ScanResultList
  property_count: 3
  slug: microsoft-purview-scanresultlist
- name: ScanRuleset
  property_count: 4
  slug: microsoft-purview-scanruleset
- name: ScanRulesetList
  property_count: 3
  slug: microsoft-purview-scanrulesetlist
- name: SearchFacetItem
  property_count: 3
  slug: microsoft-purview-searchfacetitem
- name: SearchRequest
  property_count: 6
  slug: microsoft-purview-searchrequest
- name: SearchResult
  property_count: 3
  slug: microsoft-purview-searchresult
- name: SearchResultValue
  property_count: 15
  slug: microsoft-purview-searchresultvalue
- name: Microsoft Purview Sensitivity Label
  property_count: 11
  slug: microsoft-purview-sensitivity-label
- name: SensitivityLabel
  property_count: 10
  slug: microsoft-purview-sensitivitylabel
- name: SuggestRequest
  property_count: 3
  slug: microsoft-purview-suggestrequest
- name: SuggestResult
  property_count: 1
  slug: microsoft-purview-suggestresult
- name: TermSearchResultValue
  property_count: 3
  slug: microsoft-purview-termsearchresultvalue
- name: TimeBoundary
  property_count: 3
  slug: microsoft-purview-timeboundary
- name: Trigger
  property_count: 3
  slug: microsoft-purview-trigger
- name: TriggerRecurrence
  property_count: 6
  slug: microsoft-purview-triggerrecurrence
- name: UserRequestPayload
  property_count: 2
  slug: microsoft-purview-userrequestpayload
- name: UserRequestResponse
  property_count: 2
  slug: microsoft-purview-userrequestresponse
- name: ValidationResult
  property_count: 1
  slug: microsoft-purview-validationresult
- name: Workflow
  property_count: 6
  slug: microsoft-purview-workflow
- name: WorkflowCreateOrUpdateCommand
  property_count: 5
  slug: microsoft-purview-workflowcreateorupdatecommand
- name: WorkflowList
  property_count: 2
  slug: microsoft-purview-workflowlist
- name: WorkflowRun
  property_count: 10
  slug: microsoft-purview-workflowrun
- name: WorkflowTask
  property_count: 12
  slug: microsoft-purview-workflowtask
- name: WorkflowTrigger
  property_count: 3
  slug: microsoft-purview-workflowtrigger
json_structures:
- name: Microsoft Purview Structure
  property_count: 0
  slug: microsoft-purview-structure
jsonld:
- class_count: 0
  name: Microsoft Purview Context
  property_count: 19
  slug: microsoft-purview-context
layout: provider
mcp_servers:
- description: First-party Microsoft MCP server for Purview Data Lifecycle Management diagnostics. Local stdio server (TypeScript, @modelcontextprotocol/sdk) that authenticates to Exchange Online with MSAL interacti
  name: Microsoft Purview MCP Server
  slug: microsoft-purview-mcp-server
modified: '2026-06-20'
name: Microsoft Purview
nav: Providers
network: true
overview: 'Microsoft Purview publishes 44 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Approval API, Business Domains API, and 41 more. Tagged areas include Compliance, Data Catalog, Data Classification, Data Governance, and Data Loss Prevention.


  The Microsoft Purview catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Purview''s developer surface includes authentication, CLI, changelog, developer portal, documentation, getting-started guide, engineering blog, and 59 more developer resources.'
plans:
- name: Microsoft Purview Plans Pricing
  plan_count: 4
  slug: microsoft-purview-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Microsoft Purview Rate Limits
  slug: microsoft-purview-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Purview API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-purview-jsonschema-spectral-rules
scopes:
- name: Microsoft Purview Scopes
  scope_count: 8
  slug: microsoft-purview-scopes
  summary_line: 8 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 32
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 14.4
    contract_quality: 69.2
    developer_ergonomics: 76.2
    discoverability: 74.1
    governance: 14.4
    operational_transparency: 42.1
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/screenshots/microsoft-purview-2026-08-17T124207.png
security:
- kind: authentication
  name: Microsoft Purview Authentication
  slug: microsoft-purview-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Purview Domain Security
  slug: microsoft-purview-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Purview Vulnerability Disclosure
  slug: microsoft-purview-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-purview
tags:
- Compliance
- Data Catalog
- Data Classification
- Data Governance
- Data Loss Prevention
- Information Protection
website: https://www.microsoft.com/en-us/security/business/microsoft-purview
---
