---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 421
  human_in_the_loop: 21
  name: Relativity Agentic Access
  operation_count: 733
  slug: relativity-agentic-access
  summary_line: 733 operations · 421 acting · 21 human-in-the-loop
api_count: 51
apis:
- description: The AnnotationService API from Relativity — 2 operation(s) for annotationservice.
  name: Relativity AnnotationService API
  slug: relativity-annotationservice-api
- description: The ArchiveJobs API from Relativity — 2 operation(s) for archivejobs.
  name: Relativity ArchiveJobs API
  slug: relativity-archivejobs-api
- description: The ARM Module v1 API from Relativity — 20 operation(s) for arm module v1.
  name: Relativity ARM Module v1 API
  slug: relativity-arm-module-v1-api
- description: The ARM Module v3 API from Relativity — 7 operation(s) for arm module v3.
  name: Relativity ARM Module v3 API
  slug: relativity-arm-module-v3-api
- description: The BillableSummaryReports API from Relativity — 4 operation(s) for billablesummaryreports.
  name: Relativity BillableSummaryReports API
  slug: relativity-billablesummaryreports-api
- description: The BillingConfiguration API from Relativity — 10 operation(s) for billingconfiguration.
  name: Relativity BillingConfiguration API
  slug: relativity-billingconfiguration-api
- description: The BillingInsights API from Relativity — 6 operation(s) for billinginsights.
  name: Relativity BillingInsights API
  slug: relativity-billinginsights-api
- description: The Client Side Libraries Module API from Relativity — 1 operation(s) for client side libraries module.
  name: Relativity Client Side Libraries Module API
  slug: relativity-client-side-libraries-module-api
- description: The ColdStorage API from Relativity — 1 operation(s) for coldstorage.
  name: Relativity ColdStorage API
  slug: relativity-coldstorage-api
- description: The CollectAPI API from Relativity — 6 operation(s) for collectapi.
  name: Relativity CollectAPI API
  slug: relativity-collectapi-api
- description: The Conceptual Analytics v1 API from Relativity — 4 operation(s) for conceptual analytics v1.
  name: Relativity Conceptual Analytics v1 API
  slug: relativity-conceptual-analytics-v1-api
- description: The Directory API from Relativity — 2 operation(s) for directory.
  name: Relativity Directory API
  slug: relativity-directory-api
- description: The Document Configuration Module API from Relativity — 2 operation(s) for document configuration module.
  name: Relativity Document Configuration Module API
  slug: relativity-document-configuration-module-api
- description: The DocumentViewerService API from Relativity — 1 operation(s) for documentviewerservice.
  name: Relativity DocumentViewerService API
  slug: relativity-documentviewerservice-api
- description: The DtSearchIndex Module v1 API from Relativity — 39 operation(s) for dtsearchindex module v1.
  name: Relativity DtSearchIndex Module v1 API
  slug: relativity-dtsearchindex-module-v1-api
- description: The Glacier Jobs API from Relativity — 1 operation(s) for glacier jobs.
  name: Relativity Glacier Jobs API
  slug: relativity-glacier-jobs-api
- description: The Glacier Restore API from Relativity — 1 operation(s) for glacier restore.
  name: Relativity Glacier Restore API
  slug: relativity-glacier-restore-api
- description: The Glacier Storage API from Relativity — 2 operation(s) for glacier storage.
  name: Relativity Glacier Storage API
  slug: relativity-glacier-storage-api
- description: The Glacier Store API from Relativity — 1 operation(s) for glacier store.
  name: Relativity Glacier Store API
  slug: relativity-glacier-store-api
- description: The Health Check Module API from Relativity — 1 operation(s) for health check module.
  name: Relativity Health Check Module API
  slug: relativity-health-check-module-api
- description: The Identity Module v1 API from Relativity — 62 operation(s) for identity module v1.
  name: Relativity Identity Module v1 API
  slug: relativity-identity-module-v1-api
- description: The Import Job Module API from Relativity — 11 operation(s) for import job module.
  name: Relativity Import Job Module API
  slug: relativity-import-job-module-api
- description: The Import Source Module API from Relativity — 8 operation(s) for import source module.
  name: Relativity Import Source Module API
  slug: relativity-import-source-module-api
- description: The JobActions API from Relativity — 2 operation(s) for jobactions.
  name: Relativity JobActions API
  slug: relativity-jobactions-api
- description: The JobInformation API from Relativity — 1 operation(s) for jobinformation.
  name: Relativity JobInformation API
  slug: relativity-jobinformation-api
- description: The Legal Hold Module API from Relativity — 14 operation(s) for legal hold module.
  name: Relativity Legal Hold Module API
  slug: relativity-legal-hold-module-api
- description: The Metadata API from Relativity — 1 operation(s) for metadata.
  name: Relativity Metadata API
  slug: relativity-metadata-api
- description: The Metrics Module API from Relativity — 8 operation(s) for metrics module.
  name: Relativity Metrics Module API
  slug: relativity-metrics-module-api
- description: The Object Manager v1 API from Relativity — 12 operation(s) for object manager v1.
  name: Relativity Object Manager v1 API
  slug: relativity-object-manager-v1-api
- description: Use the Relativity Object Manager to discover prerequisite artifact IDs before creating Collect collections. These calls are read-only and use the same Bearer token authentication as the Collect API.
  name: Relativity ObjectManagerAPI API
  slug: relativity-objectmanagerapi-api
- description: External public API for managing role assignments. Role keys must use the r1_ prefix (e.g. r1_staging_viewer). End user token is required
  name: Relativity Permissions Access Control API
  slug: relativity-permissions-access-control-api
- description: The PersistentHighlightService API from Relativity — 4 operation(s) for persistenthighlightservice.
  name: Relativity PersistentHighlightService API
  slug: relativity-persistenthighlightservice-api
- description: The Processing Module v1 API from Relativity — 51 operation(s) for processing module v1.
  name: Relativity Processing Module v1 API
  slug: relativity-processing-module-v1-api
- description: The Processing Module v2 API from Relativity — 19 operation(s) for processing module v2.
  name: Relativity Processing Module v2 API
  slug: relativity-processing-module-v2-api
- description: The RDO Configuration Module API from Relativity — 2 operation(s) for rdo configuration module.
  name: Relativity RDO Configuration Module API
  slug: relativity-rdo-configuration-module-api
- description: The Relativity Automated Workflows API from Relativity — 4 operation(s) for relativity automated workflows.
  name: Relativity Relativity Automated Workflows API
  slug: relativity-relativity-automated-workflows-api
- description: The Relativity Environment Module v1 API from Relativity — 93 operation(s) for relativity environment module v1.
  name: Relativity Relativity Environment Module v1 API
  slug: relativity-relativity-environment-module-v1-api
- description: The Relativity Infrastructure Module v1 API from Relativity — 70 operation(s) for relativity infrastructure module v1.
  name: Relativity Relativity Infrastructure Module v1 API
  slug: relativity-relativity-infrastructure-module-v1-api
- description: The Relativity Mass Operation Module v2 API from Relativity — 26 operation(s) for relativity mass operation module v2.
  name: Relativity Relativity Mass Operation Module v2 API
  slug: relativity-relativity-mass-operation-module-v2-api
- description: The Relativity Notifications Module v1 API from Relativity — 1 operation(s) for relativity notifications module v1.
  name: Relativity Relativity Notifications Module v1 API
  slug: relativity-relativity-notifications-module-v1-api
- description: The Relativity Pivot Module v1 API from Relativity — 7 operation(s) for relativity pivot module v1.
  name: Relativity Relativity Pivot Module v1 API
  slug: relativity-relativity-pivot-module-v1-api
- description: The Relativity Structured Analytics v1 API from Relativity — 10 operation(s) for relativity structured analytics v1.
  name: Relativity Relativity Structured Analytics v1 API
  slug: relativity-relativity-structured-analytics-v1-api
- description: The Reports API from Relativity — 7 operation(s) for reports.
  name: Relativity Reports API
  slug: relativity-reports-api
- description: The RestoreJobs API from Relativity — 2 operation(s) for restorejobs.
  name: Relativity RestoreJobs API
  slug: relativity-restorejobs-api
- description: The ShortMessageViewerService API from Relativity — 5 operation(s) for shortmessageviewerservice.
  name: Relativity ShortMessageViewerService API
  slug: relativity-shortmessageviewerservice-api
- description: The TransferControllerV2 API from Relativity — 3 operation(s) for transfercontrollerv2.
  name: Relativity TransferControllerV2 API
  slug: relativity-transfercontrollerv2-api
- description: The Versioned Imaging Module v1 API from Relativity — 20 operation(s) for versioned imaging module v1.
  name: Relativity Versioned Imaging Module v1 API
  slug: relativity-versioned-imaging-module-v1-api
- description: The Versioned Production Module v1 API from Relativity — 41 operation(s) for versioned production module v1.
  name: Relativity Versioned Production Module v1 API
  slug: relativity-versioned-production-module-v1-api
- description: The Web Import Export v1 API from Relativity — 2 operation(s) for web import export v1.
  name: Relativity Web Import Export v1 API
  slug: relativity-web-import-export-v1-api
- description: The Workspace API from Relativity — 2 operation(s) for workspace.
  name: Relativity Workspace API
  slug: relativity-workspace-api
- description: The WorkspaceJob API from Relativity — 2 operation(s) for workspacejob.
  name: Relativity WorkspaceJob API
  slug: relativity-workspacejob-api
artifact_total: 115
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService API
  slug: open-relativity-annotationservice-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService ArchiveJobs API
  slug: open-relativity-archivejobs-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService ARM Module v1 API
  slug: open-relativity-arm-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService ARM Module v3 API
  slug: open-relativity-arm-module-v3-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService BillableSummaryReports API
  slug: open-relativity-billablesummaryreports-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService BillingConfiguration API
  slug: open-relativity-billingconfiguration-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService BillingInsights API
  slug: open-relativity-billinginsights-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Client Side Libraries Module API
  slug: open-relativity-client-side-libraries-module-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService ColdStorage API
  slug: open-relativity-coldstorage-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService CollectAPI API
  slug: open-relativity-collectapi-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Conceptual Analytics v1 API
  slug: open-relativity-conceptual-analytics-v1-api
- collection_type: open
  name: Relativity.Services.DataVisualization
  slug: open-relativity-data-visualization
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Directory API
  slug: open-relativity-directory-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Document Configuration Module API
  slug: open-relativity-document-configuration-module-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService DocumentViewerService API
  slug: open-relativity-documentviewerservice-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService DtSearchIndex Module v1 API
  slug: open-relativity-dtsearchindex-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Glacier Jobs API
  slug: open-relativity-glacier-jobs-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Glacier Restore API
  slug: open-relativity-glacier-restore-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Glacier Storage API
  slug: open-relativity-glacier-storage-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Glacier Store API
  slug: open-relativity-glacier-store-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Health Check Module API
  slug: open-relativity-health-check-module-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Identity Module v1 API
  slug: open-relativity-identity-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Import Job Module API
  slug: open-relativity-import-job-module-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Import Source Module API
  slug: open-relativity-import-source-module-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService JobActions API
  slug: open-relativity-jobactions-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService JobInformation API
  slug: open-relativity-jobinformation-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Legal Hold Module API
  slug: open-relativity-legal-hold-module-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Metadata API
  slug: open-relativity-metadata-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Metrics Module API
  slug: open-relativity-metrics-module-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Object Manager v1 API
  slug: open-relativity-object-manager-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService ObjectManagerAPI API
  slug: open-relativity-objectmanagerapi-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Permissions Access Control API
  slug: open-relativity-permissions-access-control-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService PersistentHighlightService API
  slug: open-relativity-persistenthighlightservice-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Processing Module v1 API
  slug: open-relativity-processing-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Processing Module v2 API
  slug: open-relativity-processing-module-v2-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService RDO Configuration Module API
  slug: open-relativity-rdo-configuration-module-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Relativity Automated Workflows API
  slug: open-relativity-relativity-automated-workflows-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Relativity Environment Module v1 API
  slug: open-relativity-relativity-environment-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Relativity Infrastructure Module v1 API
  slug: open-relativity-relativity-infrastructure-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Relativity Mass Operation Module v2 API
  slug: open-relativity-relativity-mass-operation-module-v2-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Relativity Notifications Module v1 API
  slug: open-relativity-relativity-notifications-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Relativity Pivot Module v1 API
  slug: open-relativity-relativity-pivot-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Relativity Structured Analytics v1 API
  slug: open-relativity-relativity-structured-analytics-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Reports API
  slug: open-relativity-reports-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService RestoreJobs API
  slug: open-relativity-restorejobs-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService ShortMessageViewerService API
  slug: open-relativity-shortmessageviewerservice-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService TransferControllerV2 API
  slug: open-relativity-transfercontrollerv2-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Versioned Imaging Module v1 API
  slug: open-relativity-versioned-imaging-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Versioned Production Module v1 API
  slug: open-relativity-versioned-production-module-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Web Import Export v1 API
  slug: open-relativity-web-import-export-v1-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService Workspace API
  slug: open-relativity-workspace-api
- collection_type: open
  name: Analytics.Conceptual.Service.Interfaces.Public.V1 AnnotationService WorkspaceJob API
  slug: open-relativity-workspacejob-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/relativity-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/relativity-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/relativity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relativity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/relativity-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/relativity-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/relativity/refs/heads/main/plans/relativity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/relativity/refs/heads/main/rate-limits/relativity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/relativity/refs/heads/main/finops/relativity-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://platform.relativity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/Platform_APIs.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.relativity.com/RelativityOne/Content/Getting_Started/Basic_REST_API_concepts.htm
- group: operate
  title: ''
  type: ChangeLog
  url: https://platform.relativity.com/RelativityOne/Content/What_s_new/What_s_new.htm
- group: operate
  title: ''
  type: PlatformChangeLog
  url: https://platform.relativity.com/RelativityOne/Content/What_s_new/Platform_change_log.htm
- group: build
  title: ''
  type: GitHub
  url: https://github.com/relativitydev
- group: build
  title: ''
  type: GitHubDevTools
  url: https://relativitydev.github.io/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/relativity/refs/heads/main/openapi/relativity-object-manager-openapi.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/relativity/refs/heads/main/json-ld/relativity-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: https://platform.relativity.com/RelativityOne/Content/Getting_Started/Basic_REST_API_concepts.htm
- group: operate
  title: ''
  type: KnownIssues
  url: https://help.relativity.com/RelativityOne/Content/What_s_New/Known_issues_list.htm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.relativity.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.relativity.com/blog/
created: '2026-06-13'
description: Relativity is an eDiscovery and legal review platform offering RelativityOne, a cloud-based SaaS solution for managing the full legal data lifecycle. Its REST API enables programmatic access to workspaces, document import and export, processing pipelines, search and analytics, production management, legal hold, automated workflows, user and permission management, and AI-powered review features. Relativity exposes 80+ integration APIs organized by business domain, supporting OAuth2, basic, and cookie-based authentication.
finops:
- name: Relativity Finops
  service_category: ''
  slug: relativity-finops
graphqls:
- description: Relativity is an e-discovery platform for legal review. The API covers workspace management, document import and review, coding, search, production, analytics, imaging, and case management for legal d
  name: Relativity GraphQL API
  slug: relativity-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relativity.png
jsonld:
- class_count: 9
  name: Relativity Context
  property_count: 22
  slug: relativity-context
layout: provider
modified: '2026-06-13'
name: Relativity
nav: Providers
network: true
overview: 'Relativity publishes 51 APIs on the [APIs.io](https://apis.io/) network, including AnnotationService API, ArchiveJobs API, ARM Module v1 API, and 48 more. Tagged areas include eDiscovery, Legal, Document Review, Legal Technology, and Data Processing.


  The Relativity catalog on APIs.io includes 1 JSON-LD context.


  Relativity''s developer surface includes authentication, documentation, getting-started guide, changelog, GitHub presence, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Relativity Plans Pricing
  plan_count: 3
  slug: relativity-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Relativity Rate Limits
  slug: relativity-rate-limits
scopes:
- name: Relativity Scopes
  scope_count: 1
  slug: relativity-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 45.6
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 58.1
    developer_ergonomics: 45.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 53
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relativity/refs/heads/main/screenshots/relativity-2026-06-20T192818.png
security:
- kind: authentication
  name: Relativity Authentication
  slug: relativity-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Relativity Domain Security
  slug: relativity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Relativity Vulnerability Disclosure
  slug: relativity-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Relativity Trust Center
  slug: relativity-trust-center
  summary_line: FedRAMP, GDPR
slug: relativity
tags:
- eDiscovery
- Legal
- Document Review
- Legal Technology
- Data Processing
- AI Review
- Litigation
- Compliance
website: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/Platform_APIs.htm
---
