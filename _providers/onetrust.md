---
access_model:
  confidence: high
  label: Enterprise · Public docs + public OpenAPI, tenant-gated keys
  onboarding: unknown
  pricing: enterprise
  public: true
  source:
  - plans
  - authentication
  - openapi
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.9
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 389
  human_in_the_loop: 30
  name: Onetrust Agentic Access
  operation_count: 631
  slug: onetrust-agentic-access
  summary_line: 631 operations · 389 acting · 30 human-in-the-loop
api_count: 37
apis:
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Activity Log API from OneTrust — 1 operation(s) for activity log.
  name: OneTrust Activity Log API
  slug: onetrust-activity-log-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Applications APIs are used to manage application configurations and their associated consent experiences.
  name: OneTrust Applications API
  slug: onetrust-applications-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Assessment Actions APIs are used to perform workflows on assessments, such as launching, approving, or creating tasks.
  name: OneTrust Assessment Actions API
  slug: onetrust-assessment-actions-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Assessment Management APIs are used to modify, link, and manage existing assessments.
  name: OneTrust Assessment Management API
  slug: onetrust-assessment-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Assessments APIs are used to retrieve assessment data and details.
  name: OneTrust Assessments API
  slug: onetrust-assessments-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Attachments APIs are used to upload and obtain the location of files uploaded in the OneTrust Platform.
  name: OneTrust Attachments API
  slug: onetrust-attachments-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Attachments V4 API from OneTrust — 1 operation(s) for attachments v4.
  name: OneTrust Attachments V4 API
  slug: onetrust-attachments-v4-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Attribute Management APIs are used to manage attributes associated with AI Governance entities.
  name: OneTrust Attribute Management API
  slug: onetrust-attribute-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage and retrieve audit logs for user activities, including login history and access patterns. These endpoints help you monitor security events, track user authentication attempts, and maint
  name: OneTrust Audit Records API
  slug: onetrust-audit-records-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage the complete audit lifecycle including creation, updates, deletion, scope assignment, and retrieval with support for approvers, auditors, and custom attributes.
  name: OneTrust Audits API
  slug: onetrust-audits-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage cookie consent banner configuration and behavior.
  name: OneTrust Banner API
  slug: onetrust-banner-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Bulk Export APIs are used to extract large volumes of cookie receipts, consent receipts, and data subjects.
  name: OneTrust Bulk Export API
  slug: onetrust-bulk-export-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage emission factors and emission transactions.
  name: OneTrust Carbon Management API
  slug: onetrust-carbon-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage catalog search operations with basic functionality and providing comprehensive filtering, faceting, and field selection capabilities for data asset discovery.
  name: OneTrust Catalog Search V1 API
  slug: onetrust-catalog-search-v1-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage catalog search operations with enhanced scalability, featuring continuation token-based pagination for handling large volumes of search results and improved performance for enterprise-s
  name: OneTrust Catalog Search V2 API
  slug: onetrust-catalog-search-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Categorizations API from OneTrust — 2 operation(s) for categorizations.
  name: OneTrust Categorizations API
  slug: onetrust-categorizations-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Classification APIs are used to manage custom data classifiers and classification rules for Data Discovery.
  name: OneTrust Classification API
  slug: onetrust-classification-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Collection Points APIs are used to manage where and how consent is collected.
  name: OneTrust Collection Points API
  slug: onetrust-collection-points-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Collection Points V2 APIs are used to manage collection points using version 2 of the API.
  name: OneTrust Collection Points V2 API
  slug: onetrust-collection-points-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing Consent Attachments.
  name: OneTrust Consent Attachments API
  slug: onetrust-consent-attachments-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing Consent Groups and their configurations.
  name: OneTrust Consent Groups API
  slug: onetrust-consent-groups-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: API for optimizing consent rate.
  name: OneTrust Consent Rate Optimization API
  slug: onetrust-consent-rate-optimization-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Consent Receipts APIs are used to create consent receipts from a collection point to store data subject consent.
  name: OneTrust Consent Receipts API
  slug: onetrust-consent-receipts-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Contracts APIs are used to manage vendor contract operations including contract creation, updates, search functionality, contract type management, and schema configuration for comprehensive contra
  name: OneTrust Contracts API
  slug: onetrust-contracts-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to handle control implementation operations including creation, updates, entity associations, attachment management, and comprehensive search across multiple entity types.
  name: OneTrust Control Implementations API
  slug: onetrust-control-implementations-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to create and manage relationships between controls through bulk linking operations with support for various relationship types and custom parameters.
  name: OneTrust Control Links API
  slug: onetrust-control-links-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage the complete control lifecycle including creation, updates, deletion, retrieval, and entity type management with framework integration and custom attributes.
  name: OneTrust Controls API
  slug: onetrust-controls-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Cookies APIs are used to manage cookie definitions, categories, and their properties.
  name: OneTrust Cookies API
  slug: onetrust-cookies-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage credential operations including creation, updates, deletion, retrieval, and secure reference key management for multiple system authentication types.
  name: OneTrust Credentials API
  slug: onetrust-credentials-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Custom Index Management API from OneTrust — 2 operation(s) for custom index management.
  name: OneTrust Custom Index Management API
  slug: onetrust-custom-index-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage and execute custom data discovery scans across specified data sources.
  name: OneTrust Custom Scan API
  slug: onetrust-custom-scan-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Asset Attributes API from OneTrust — 2 operation(s) for data asset attributes.
  name: OneTrust Data Asset Attributes API
  slug: onetrust-data-asset-attributes-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Asset Management API from OneTrust — 2 operation(s) for data asset management.
  name: OneTrust Data Asset Management API
  slug: onetrust-data-asset-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Assets APIs are used to manage data asset metadata.
  name: OneTrust Data Assets API
  slug: onetrust-data-assets-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage data sources including creation, retrieval, updates, deletion, and comprehensive filtering with support for multiple system types and asset integration.
  name: OneTrust Data Sources API
  slug: onetrust-data-sources-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subject Access Request (DSAR) API from OneTrust — 1 operation(s) for data subject access request (dsar).
  name: OneTrust Data Subject Access Request (DSAR) API
  slug: onetrust-data-subject-access-request-dsar-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subject Groups APIs are used to manage groups of data subjects.
  name: OneTrust Data Subject Groups API
  slug: onetrust-data-subject-groups-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects V4 APIs are used to manage data subject information, preferences, and consent records.
  name: OneTrust Data Subject Groups V4 API
  slug: onetrust-data-subject-groups-v4-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects APIs are used to manage individuals whose data is being processed.
  name: OneTrust Data Subjects API
  slug: onetrust-data-subjects-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects V2 APIs are used to manage data subjects using version 2 of the API.
  name: OneTrust Data Subjects V2 API
  slug: onetrust-data-subjects-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects V3 APIs are used to manage data subject information, preferences, and consent records.
  name: OneTrust Data Subjects V3 API
  slug: onetrust-data-subjects-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects V4 APIs are used to manage data subject information, preferences, and consent records.
  name: OneTrust Data Subjects V4 API
  slug: onetrust-data-subjects-v4-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Deduplicate Data Subjects APIs are used to merge duplicate data subject profiles.
  name: OneTrust Deduplicate Data Subjects API
  slug: onetrust-deduplicate-data-subjects-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to retrieve a paginated list of deletion certificates.
  name: OneTrust Deletion Certificates API
  slug: onetrust-deletion-certificates-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Document Attachments APIs are used to manage attachments on document objects such as policies, standards, procedures, and privacy notices.
  name: OneTrust Document Attachments API
  slug: onetrust-document-attachments-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Document Gateway API provides secure document download functionality using tokens from the Document Service V4.
  name: OneTrust Document Gateway API
  slug: onetrust-document-gateway-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Documents APIs are used to manage document objects such as policies, standards, procedures, and privacy notices.
  name: OneTrust Documents API
  slug: onetrust-documents-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Domain Data API from OneTrust — 1 operation(s) for domain data.
  name: OneTrust Domain Data API
  slug: onetrust-domain-data-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Domains APIs are used to manage domain configurations and cookie scanning settings.
  name: OneTrust Domains API
  slug: onetrust-domains-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing DROP records and privacy requests
  name: OneTrust DROP Management API
  slug: onetrust-drop-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Engagements APIs are used to manage vendor engagement operations including creating, retrieving, updating, and searching engagements with comprehensive attribute management, status control, workfl
  name: OneTrust Engagements API
  slug: onetrust-engagements-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Entity Management APIs are used to manage AI Governance entities.
  name: OneTrust Entity Management API
  slug: onetrust-entity-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Entity Type Management APIs are used to manage AI Governance entity types.
  name: OneTrust Entity Type Management API
  slug: onetrust-entity-type-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage risk entity types and source entity types, including retrieval of enabled entity configurations for risk associations.
  name: OneTrust Entity Types API
  slug: onetrust-entity-types-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Entity Workflow Management APIs are used to manage AI Governance entity workflows.
  name: OneTrust Entity Workflow Management API
  slug: onetrust-entity-workflow-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage evidence collection tasks including implementation retrieval, attachment handling (files, links, notes), and comprehensive search with interval-based collection tracking.
  name: OneTrust Evidence Task Implementations API
  slug: onetrust-evidence-task-implementations-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Geolocation Rules APIs are used to manage geographic rules that determine how consent experiences are applied based on user location.
  name: OneTrust Geolocation Rules API
  slug: onetrust-geolocation-rules-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage business glossaries, including retrieving glossary details, listing all available glossaries, and accessing glossary-specific information with associated terms and metadata.
  name: OneTrust Glossaries API
  slug: onetrust-glossaries-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V2 version APIs to manage Groups.
  name: OneTrust Groups V2 API
  slug: onetrust-groups-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, search, and manage incidents, including linking incidents to inventories, retrieving details, and tracking their lifecycle.
  name: OneTrust Incidents API
  slug: onetrust-incidents-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Initiatives APIs are used to manage compliance initiatives for standards and frameworks.
  name: OneTrust Initiatives API
  slug: onetrust-initiatives-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to retrieve Docker image tags and installation resources for worker node deployment and version management across different environments.
  name: OneTrust Installer API
  slug: onetrust-installer-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create and manage inventory records for supported schema types (processing-activities, vendors, assets, entities).
  name: OneTrust Inventory API
  slug: onetrust-inventory-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to list, link, and unlink child inventories under a root inventory to model organizational or data-flow trees.
  name: OneTrust Inventory Hierarchies API
  slug: onetrust-inventory-hierarchies-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The inventory-management-controller API from OneTrust — 3 operation(s) for inventory-management-controller.
  name: OneTrust Inventory Management Controller API
  slug: onetrust-inventory-management-controller-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, and delete bidirectional links between inventories and to manage associations to related items (including personal data).
  name: OneTrust Inventory Relationships V1 API
  slug: onetrust-inventory-relationships-v1-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Inventory Relationships V2 APIs are used to manage V2 inventory relationships.
  name: OneTrust Inventory Relationships V2 API
  slug: onetrust-inventory-relationships-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to define and maintain schema attributes that shape inventory data collection and validation.
  name: OneTrust Inventory Schema API
  slug: onetrust-inventory-schema-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Issues APIs are used to manage issues, issue tasks, and issue relationships.
  name: OneTrust Issues API
  slug: onetrust-issues-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Jobs APIs are used to manage scheduled jobs for bulk actions.
  name: OneTrust Jobs API
  slug: onetrust-jobs-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to record and retrieve user consent transactions and preferences.
  name: OneTrust Log Consent API
  slug: onetrust-log-consent-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Magic Link Tokens APIs are used to generate secure, one-time-use links for authentication.
  name: OneTrust Magic Link Tokens API
  slug: onetrust-magic-link-tokens-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Magic Link Tokens V4 APIs are used to manage secure, time-limited tokens for data subject verification and authentication.
  name: OneTrust Magic Link Tokens V4 API
  slug: onetrust-magic-link-tokens-v4-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage Metric related Information.
  name: OneTrust Metric Details API
  slug: onetrust-metric-details-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Mobile App Data API from OneTrust — 1 operation(s) for mobile app data.
  name: OneTrust Mobile App Data API
  slug: onetrust-mobile-app-data-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Model Management APIs are used to conduct full management of Model objects.
  name: OneTrust Model Management API
  slug: onetrust-model-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage OAuth 2.0 authentication for secure API access. Generate access tokens using client credentials, retrieve token information, and manage API authentication for your applications.
  name: OneTrust OAuth Token API
  slug: onetrust-oauth-token-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Attribute Management APIs are used to manage object attributes.
  name: OneTrust Object Attribute Management API
  slug: onetrust-object-attribute-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Management APIs are used to manage objects created via Object Manager, including Projects, Models, and Datasets.
  name: OneTrust Object Management API
  slug: onetrust-object-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Relationship Management APIs are used to manage relationships between objects.
  name: OneTrust Object Relationship Management API
  slug: onetrust-object-relationship-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Relationship Type Management APIs are used to manage the types of relationships that can exist between objects.
  name: OneTrust Object Relationship Type Management API
  slug: onetrust-object-relationship-type-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Task Management APIs are used to manage tasks associated with objects.
  name: OneTrust Object Task Management API
  slug: onetrust-object-task-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Type Management APIs are used to manage custom object types.
  name: OneTrust Object Type Management API
  slug: onetrust-object-type-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage your organizational hierarchy and structure. Create, update, and delete organizations, define parent-child relationships, and configure organization-specific settings such as default la
  name: OneTrust Organizations API
  slug: onetrust-organizations-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to list links to personal-data items for an inventory and update advanced attributes on those associations.
  name: OneTrust Personal Data API
  slug: onetrust-personal-data-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage preference center configuration and user consent choices.
  name: OneTrust Preference Center API
  slug: onetrust-preference-center-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Preference Centers APIs are used to manage data subjects' preferences in a preference center.
  name: OneTrust Preference Centers API
  slug: onetrust-preference-centers-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Preference Centers V2 APIs are used to manage preference centers using version 2 of the API.
  name: OneTrust Preference Centers V2 API
  slug: onetrust-preference-centers-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Preferences API from OneTrust — 1 operation(s) for preferences.
  name: OneTrust Preferences API
  slug: onetrust-preferences-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Consent Interfaces APIs are used by Consent & Preferences user interfaces to retrieve data subjects' preferences.
  name: OneTrust Preferences V2 API
  slug: onetrust-preferences-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to list privacy notices, fetch versions for a notice, and get the notice version active on a given date/time.
  name: OneTrust Privacy Notice V2 API
  slug: onetrust-privacy-notice-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Project Management APIs are used to conduct full management of Project objects.
  name: OneTrust Project Management API
  slug: onetrust-project-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Purpose Preferences APIs are used to manage preferences related to specific data collection purposes.
  name: OneTrust Purpose Preferences API
  slug: onetrust-purpose-preferences-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Purposes APIs are used to manage the reasons for which data is collected.
  name: OneTrust Purposes API
  slug: onetrust-purposes-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Purposes V2 APIs are used to manage purposes using version 2 of the API.
  name: OneTrust Purposes V2 API
  slug: onetrust-purposes-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Receipts APIs are used to manage records of consent transactions.
  name: OneTrust Receipts API
  slug: onetrust-receipts-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing consent receipts (V2).
  name: OneTrust Receipts V2 API
  slug: onetrust-receipts-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Relationship Management APIs are used to manage relationships between AI Governance entities.
  name: OneTrust Relationship Management API
  slug: onetrust-relationship-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, search, update, and manage privacy request queues.
  name: OneTrust Request Queues API
  slug: onetrust-request-queues-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, delete, and retrieve resolution codes for privacy requests and subtasks.
  name: OneTrust Resolutions API
  slug: onetrust-resolutions-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager Resources Type.
  name: OneTrust Resources V3 API
  slug: onetrust-resources-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to share results summaries.
  name: OneTrust Results Summary API
  slug: onetrust-results-summary-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage risk workflow actions including submissions, approvals, exceptions, and stage transitions within the risk lifecycle.
  name: OneTrust Risk Actions API
  slug: onetrust-risk-actions-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage risk configurations, scoring settings, categories, and metadata used across the risk management system.
  name: OneTrust Risk Management API
  slug: onetrust-risk-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage relationships between risks and other entities including threats, vulnerabilities, controls, and inventory items.
  name: OneTrust Risk Relationships API
  slug: onetrust-risk-relationships-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage risk template retrieval operations, enabling users to access detailed risk template information including inherent and target risk levels, associated threats and vulnerabilities, contro
  name: OneTrust Risk Templates API
  slug: onetrust-risk-templates-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage the complete risk lifecycle including creation, updates, deletion, search, and retrieval of risk details and attributes.
  name: OneTrust Risks API
  slug: onetrust-risks-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to control scan job execution including creation, cancellation, status monitoring, and comprehensive job history retrieval with filtering and pagination support.
  name: OneTrust Scan Jobs API
  slug: onetrust-scan-jobs-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to handle scan profile lifecycle management including creation, updates, deletion, and retrieval with support for catalog and catalog-scan types across various system platforms.
  name: OneTrust Scan Profiles API
  slug: onetrust-scan-profiles-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Scans APIs are used to manage website cookie scanning operations and results.
  name: OneTrust Scans API
  slug: onetrust-scans-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager Schemas.
  name: OneTrust SCIM Schemas V3 API
  slug: onetrust-scim-schemas-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Scripts APIs are used to manage publishing of scripts to websites.
  name: OneTrust Scripts API
  slug: onetrust-scripts-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager the Service Provider.
  name: OneTrust Service Provider V3 API
  slug: onetrust-service-provider-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, complete, and reprocess subtasks associated with privacy requests.
  name: OneTrust Subtasks API
  slug: onetrust-subtasks-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create and update system credentials required for integrations, such as authentication keys and connection details.
  name: OneTrust System Credentials API
  slug: onetrust-system-credentials-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage tags for data classification, including creating new tags with various types and retrieving tag details with their associated terms.
  name: OneTrust Tags API
  slug: onetrust-tags-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to add, update, and retrieve structured or unstructured data discovery results linked to privacy requests.
  name: OneTrust Targeted Data Discovery API
  slug: onetrust-targeted-data-discovery-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Task Management APIs are used to manage tasks associated with AI Governance entities.
  name: OneTrust Task Management API
  slug: onetrust-task-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Tasks APIs are used to manage tasks, including creation, updates, and retrieval.
  name: OneTrust Tasks API
  slug: onetrust-tasks-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage assessment template operations including import and export functionality for cross-tenant migration, retrieval of published template listings with type-based filtering, and template del
  name: OneTrust Template API
  slug: onetrust-template-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Templates APIs are used to manage reusable consent templates that define the structure and behavior of consent experiences.
  name: OneTrust Templates API
  slug: onetrust-templates-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: 'APIs to manage glossary terms, including creating new terms with custom attributes, retrieving term lists with search and pagination capabilities, accessing individual term details, and managing term '
  name: OneTrust Terms API
  slug: onetrust-terms-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to handle threat library operations including threat creation, modification, deletion, and comprehensive search functionality with framework and category support.
  name: OneTrust Threats API
  slug: onetrust-threats-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Training API from OneTrust — 5 operation(s) for training.
  name: OneTrust Training API
  slug: onetrust-training-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Transactions APIs are used to manage consent transactions.
  name: OneTrust Transactions API
  slug: onetrust-transactions-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing consent transactions.
  name: OneTrust Transactions V2 API
  slug: onetrust-transactions-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage Universal Consent purposes and their associated metadata.
  name: OneTrust UC Purposes API
  slug: onetrust-uc-purposes-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage user groups and their memberships. Create groups to organize users, assign permissions collectively, add or remove members, and retrieve information about existing groups and their memb
  name: OneTrust User Groups API
  slug: onetrust-user-groups-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage user groups and their memberships. Create groups to organize users, assign permissions collectively, add or remove members, and retrieve information about existing groups and their memb
  name: OneTrust User Groups V2 API
  slug: onetrust-user-groups-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager User Groups.
  name: OneTrust User Groups V3 API
  slug: onetrust-user-groups-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage users and their memberships and access levels.
  name: OneTrust Users V2 API
  slug: onetrust-users-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager Users.
  name: OneTrust Users V3 API
  slug: onetrust-users-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage third-party vendor information and their data processing activities.
  name: OneTrust Vendors API
  slug: onetrust-vendors-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, and retrieve methods for verifying a data subject's identity.
  name: OneTrust Verification Methods API
  slug: onetrust-verification-methods-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage vulnerabilities in the vulnerability library including creation, updates, deletion, and retrieval with support for bulk operations and custom attributes.
  name: OneTrust Vulnerabilities API
  slug: onetrust-vulnerabilities-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Websites V2 API from OneTrust — 1 operation(s) for websites v2.
  name: OneTrust Websites V2 API
  slug: onetrust-websites-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to import and export workflows in JSON format for version 2 workflows.
  name: OneTrust Workflows V2 API
  slug: onetrust-workflows-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to handle audit workpaper operations including testing results, sampling outcomes, interview findings, control assessments, and workpaper attribute management.
  name: OneTrust Workpapers API
  slug: onetrust-workpapers-api
artifact_total: 150
asyncapis:
- description: ''
  name: Onetrust Webhooks
  slug: onetrust-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-ai-governance-ai-governance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-ai-governance-ai-governance-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-global-activity-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-global-activity-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-consent-interfaces-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-consent-interfaces-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-consent-management-platform-cmp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-consent-management-platform-cmp-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-consent-receipts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-consent-receipts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-cookie-consent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-cookie-consent-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-cookie-consent-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-cookie-consent-swagger-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-cookie-domain-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-cookie-domain-data-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-cross-device-consent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-cross-device-consent-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-mobile-app-consent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-mobile-app-consent-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-policy-and-notice-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-policy-and-notice-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-consent-and-preferences-universal-consent-and-preference-management-oas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-universal-consent-and-preference-management-oas-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-data-use-governance-data-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-data-use-governance-data-catalog-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-data-use-governance-data-discovery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-data-use-governance-data-discovery-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-data-use-governance-data-discovery-worker-node-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-data-use-governance-data-discovery-worker-node-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-esg-program-reporting-and-disclosures-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-esg-program-reporting-and-disclosures-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-access-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-access-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-bulk-export-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-bulk-export-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-documents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-documents-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-integrations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-inventory-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-inventory-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-object-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-object-manager-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-task-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-task-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-platform-user-provisioning-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-user-provisioning-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-privacy-automation-assessment-automation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-assessment-automation-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-privacy-automation-data-mapping-automation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-data-mapping-automation-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-privacy-automation-data-mapping-automation-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-data-mapping-automation-swagger-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-privacy-automation-data-subject-request-dsr-automation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-data-subject-request-dsr-automation-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-privacy-automation-incident-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-incident-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-the-trust-intelligence-platform-document-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-the-trust-intelligence-platform-document-gateway-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-tech-risk-and-compliance-audit-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-audit-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-tech-risk-and-compliance-compliance-automation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-compliance-automation-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-tech-risk-and-compliance-enterprise-policy-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-enterprise-policy-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-tech-risk-and-compliance-issues-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-issues-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-tech-risk-and-compliance-it-risk-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-it-risk-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-tech-risk-and-compliance-training-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-training-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/overlays/onetrust-third-party-management-third-party-risk-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-third-party-management-third-party-risk-management-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.onetrust.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.onetrust.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.onetrust.com/onetrust/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.onetrust.com/onetrust/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.onetrust.com/onetrust/reference/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://my.onetrust.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.onetrust.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onetrust-oss
- group: commercial
  title: ''
  type: Pricing
  url: https://www.onetrust.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.onetrust.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onetrust.com/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onetrust
- group: operate
  title: ''
  type: StatusPage
  url: https://my.onetrust.com/s/system-status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/lifecycle/onetrust-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/onetrust-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/lifecycle/onetrust-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/onetrust-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/changelog/onetrust-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/onetrust-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/authentication/onetrust-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onetrust-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/scopes/onetrust-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/onetrust-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/conventions/onetrust-conventions.yml
  title: ''
  type: Conventions
  url: conventions/onetrust-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/errors/onetrust-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/onetrust-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/data-model/onetrust-data-model.yml
  title: ''
  type: DataModel
  url: data-model/onetrust-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/rate-limits/onetrust-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/onetrust-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/plans/onetrust-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onetrust-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/finops/onetrust-finops.yml
  title: ''
  type: FinOps
  url: finops/onetrust-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/packages/onetrust-packages.yml
  title: ''
  type: Packages
  url: packages/onetrust-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/packages/onetrust-packages.yml
  title: ''
  type: SDKs
  url: packages/onetrust-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/components/onetrust-components.yml
  title: ''
  type: Components
  url: components/onetrust-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/sandbox/onetrust-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/onetrust-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/mcp/onetrust-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/onetrust-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/mcp/onetrust-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/onetrust-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/agentic-access/onetrust-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/onetrust-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/llms/onetrust-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onetrust-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/well-known/onetrust-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onetrust-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/well-known/onetrust-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/onetrust-api-catalog.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/asyncapi/onetrust-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/onetrust-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/conformance/onetrust-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onetrust-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/conformance/onetrust-conformance.yml
  title: ''
  type: Compliance
  url: conformance/onetrust-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/security/onetrust-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/onetrust-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/security/onetrust-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/onetrust-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/security/onetrust-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/onetrust-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/security/onetrust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onetrust-domain-security.yml
created: '2026-05-08'
description: OneTrust is an enterprise trust, privacy, and AI-governance platform. Its developer portal publishes 37 downloadable OpenAPI definitions covering roughly 631 operations across Universal Consent & Preference Management, Cookie Consent / CMP, Consent Receipts, Data Subject Request (DSR) Automation, Assessment Automation (PIA/DPIA), Data Mapping, Data Catalog and Data Discovery, Incident Management, IT & Security Risk Management, Audit Management, Issues Management, Enterprise Policy Management, Compliance Automation, Third-Party Risk Management, ESG Program Reporting, AI Governance, and the shared platform services (Access Management, SCIM 2.0 User Provisioning, Object Manager, Inventory, Bulk Export, Documents, Integrations, Task Management, Global Activity). Every API is authorized with OAuth 2.0 client credentials against a per-tenant environment host, and the portal also serves an RFC 9727 /.well-known/api-catalog, an llms.txt, and a public remote MCP server.
finops:
- name: Onetrust Finops
  service_category: Compliance & Governance
  slug: onetrust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onetrust.png
layout: provider
mcp_servers:
- description: OneTrust hosts a public remote MCP server on its developer portal. It is documented on a dedicated "MCP Server" page in the API reference, requires no authentication headers, and answered a live tools
  name: OneTrust Developer Portal MCP Server
  slug: onetrust-developer-portal-mcp-server
modified: '2026-08-27'
name: OneTrust
nav: Providers
network: true
overview: 'OneTrust publishes 138 APIs on the [APIs.io](https://apis.io/) network, including Activity Log API, Applications API, Assessment Actions API, and 135 more. Tagged areas include Privacy, GRC, Compliance, Consent, and TPRM.


  The OneTrust catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OneTrust''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 72 more developer resources.'
plans:
- name: Onetrust Plans Pricing
  plan_count: 1
  slug: onetrust-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 12
  name: Onetrust Rate Limits
  slug: onetrust-rate-limits
scopes:
- name: Onetrust Scopes
  scope_count: 51
  slug: onetrust-scopes
  summary_line: 51 scopes · clientCredentials
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 73.1
    developer_ergonomics: 51.8
    discoverability: 75.9
    operational_transparency: 92.1
  previous_composite: 68.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 146
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/screenshots/onetrust-2026-06-20T190718.png
security:
- kind: authentication
  name: Onetrust Authentication
  slug: onetrust-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Onetrust Domain Security
  slug: onetrust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Onetrust Vulnerability Disclosure
  slug: onetrust-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Onetrust Trust Center
  slug: onetrust-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: onetrust
tags:
- Privacy
- GRC
- Compliance
- Consent
- TPRM
- AI Governance
- Data Governance
- Risk Management
- Data Discovery
- ESG
- Security
- SCIM
website: https://www.onetrust.com/
---
