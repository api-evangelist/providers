---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.8
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 76
  human_in_the_loop: 0
  name: Acceldata Agentic Access
  operation_count: 149
  slug: acceldata-agentic-access
  summary_line: 149 operations · 76 acting
api_count: 3
apis:
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Monitor and manage data quality and pipeline alerts
  name: Acceldata Alerts API
  slug: acceldata-alerts-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Manage data quality rules and monitoring policies
  name: Acceldata Data Quality Rules API
  slug: acceldata-data-quality-rules-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Manage and query dataset metadata and quality metrics
  name: Acceldata Datasets API
  slug: acceldata-datasets-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Query data lineage and impact analysis
  name: Acceldata Lineage API
  slug: acceldata-lineage-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Monitor data pipeline job execution and health
  name: Acceldata Pipeline Jobs API
  slug: acceldata-pipeline-jobs-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Manage roles and permissions
  name: Acceldata Roles API
  slug: acceldata-roles-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Manage users and user invitations
  name: Acceldata Users API
  slug: acceldata-users-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: List and revoke API keys belonging to individual users or across the realm. API keys authenticate programmatic requests made on behalf of a user.
  name: Acceldata API Keys API
  slug: acceldata-api-keys-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Asset Activity API from Acceldata — 2 operation(s) for asset activity.
  name: Acceldata Asset Activity API
  slug: acceldata-asset-activity-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Asset Configuration API from Acceldata — 1 operation(s) for asset configuration.
  name: Acceldata Asset Configuration API
  slug: acceldata-asset-configuration-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Asset Metadata API from Acceldata — 1 operation(s) for asset metadata.
  name: Acceldata Asset Metadata API
  slug: acceldata-asset-metadata-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Asset Sampling API from Acceldata — 2 operation(s) for asset sampling.
  name: Acceldata Asset Sampling API
  slug: acceldata-asset-sampling-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Asset Tags & Labels API from Acceldata — 4 operation(s) for asset tags & labels.
  name: Acceldata Asset Tags & Labels API
  slug: acceldata-asset-tags-labels-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Asset Types API from Acceldata — 1 operation(s) for asset types.
  name: Acceldata Asset Types API
  slug: acceldata-asset-types-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Asset UDF Variables API from Acceldata — 2 operation(s) for asset udf variables.
  name: Acceldata Asset UDF Variables API
  slug: acceldata-asset-udf-variables-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Asset Watch API from Acceldata — 2 operation(s) for asset watch.
  name: Acceldata Asset Watch API
  slug: acceldata-asset-watch-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Assign and remove client (platform) roles for a user. Client roles determine which platform-wide actions a user can perform, independent of any domain-scoped access.
  name: Acceldata Client Roles API
  slug: acceldata-client-roles-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Custom Assets API from Acceldata — 1 operation(s) for custom assets.
  name: Acceldata Custom Assets API
  slug: acceldata-custom-assets-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Data Cadence Rules API from Acceldata — 3 operation(s) for data cadence rules.
  name: Acceldata Data Cadence Rules API
  slug: acceldata-data-cadence-rules-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Data Drift Rules API from Acceldata — 8 operation(s) for data drift rules.
  name: Acceldata Data Drift Rules API
  slug: acceldata-data-drift-rules-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Create, retrieve, update, and delete user groups, and view the roles available to a group. Groups let administrators assign roles and permissions to multiple users at once instead of managing them ind
  name: Acceldata Group Management API
  slug: acceldata-group-management-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Profile Anomaly Rules API from Acceldata — 5 operation(s) for profile anomaly rules.
  name: Acceldata Profile Anomaly Rules API
  slug: acceldata-profile-anomaly-rules-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Self-service account operations, such as triggering a forgot-password email for a user.
  name: Acceldata Profile Update API
  slug: acceldata-profile-update-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Reconciliation Rules API from Acceldata — 12 operation(s) for reconciliation rules.
  name: Acceldata Reconciliation Rules API
  slug: acceldata-reconciliation-rules-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Reference Assets API from Acceldata — 1 operation(s) for reference assets.
  name: Acceldata Reference Assets API
  slug: acceldata-reference-assets-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Retrieve the client roles currently assigned to a user.
  name: Acceldata Role Mapping API
  slug: acceldata-role-mapping-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Rule Configuration API from Acceldata — 2 operation(s) for rule configuration.
  name: Acceldata Rule Configuration API
  slug: acceldata-rule-configuration-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Rule Tags API from Acceldata — 1 operation(s) for rule tags.
  name: Acceldata Rule Tags API
  slug: acceldata-rule-tags-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Rules API from Acceldata — 2 operation(s) for rules.
  name: Acceldata Rules API
  slug: acceldata-rules-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The Schema Drift Rules API from Acceldata — 6 operation(s) for schema drift rules.
  name: Acceldata Schema Drift Rules API
  slug: acceldata-schema-drift-rules-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: 'Create, retrieve, update, and manage service users — non-human identities used for automated access and system-to-system integrations in place of personal user API keys. Includes assigning roles to a '
  name: Acceldata Service Users API
  slug: acceldata-service-users-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Unified tag association endpoints (associate tags with, and read tags for, catalog entities)
  name: Acceldata Tag Associations API
  slug: acceldata-tag-associations-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Create tag keys, add values to a key, and search across tag key/value pairs.
  name: Acceldata Tags API
  slug: acceldata-tags-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The UDF Templates API from Acceldata — 2 operation(s) for udf templates.
  name: Acceldata UDF Templates API
  slug: acceldata-udf-templates-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: The UDF Validation API from Acceldata — 2 operation(s) for udf validation.
  name: Acceldata UDF Validation API
  slug: acceldata-udf-validation-api
- baseURL: https://api.acceldata.app/v1
  baseurl_source: declared
  description: Create, retrieve, update, and remove users, and manage their group memberships. Users provisioned through SCIM are synced from the identity provider and have restricted edit and delete operations.
  name: Acceldata User Management API
  slug: acceldata-user-management-api
arazzos:
- description: List organization users and the platform roles so access can be reviewed against defined permissions.
  name: Acceldata Access Review
  slug: acceldata-access-review-workflow
- description: Resolve a dataset, create a data quality rule on it, and confirm the rule is registered.
  name: Acceldata Create and Verify Data Quality Rule
  slug: acceldata-create-and-verify-rule-workflow
- description: List open critical alerts and acknowledge the first one when any are present.
  name: Acceldata Critical Alert Sweep
  slug: acceldata-critical-alert-sweep-workflow
- description: Resolve a dataset, list its data quality rules, and map its lineage for impact analysis.
  name: Acceldata Dataset Quality Audit
  slug: acceldata-dataset-quality-audit-workflow
- description: Resolve a dataset, review its existing rules, create a new rule, and map downstream impact.
  name: Acceldata Onboard Rule With Impact
  slug: acceldata-onboard-rule-with-impact-workflow
- description: Find failed pipeline jobs, pull related critical alerts, and acknowledge the first one.
  name: Acceldata Pipeline Failure Investigation
  slug: acceldata-pipeline-failure-investigation-workflow
- description: Resolve a dataset, pull its open alerts, and acknowledge the most severe one.
  name: Acceldata Triage Dataset Alerts
  slug: acceldata-triage-dataset-alerts-workflow
artifact_total: 131
collections:
- collection_type: postman
  name: Acceldata - Data Observability Cloud API
  slug: postman-acceldata-adoc-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acceldata - Data Observability Cloud Alerts API
  slug: open-acceldata-alerts-api
- collection_type: open
  name: Acceldata - Data Observability Cloud Alerts Data Quality Rules API
  slug: open-acceldata-data-quality-rules-api
- collection_type: open
  name: Acceldata - Data Observability Cloud Alerts Datasets API
  slug: open-acceldata-datasets-api
- collection_type: open
  name: Acceldata - Data Observability Cloud Alerts Lineage API
  slug: open-acceldata-lineage-api
- collection_type: open
  name: Acceldata - Data Observability Cloud Alerts Pipeline Jobs API
  slug: open-acceldata-pipeline-jobs-api
- collection_type: open
  name: Acceldata - Data Observability Cloud Alerts Roles API
  slug: open-acceldata-roles-api
- collection_type: open
  name: Acceldata - Data Observability Cloud Alerts Users API
  slug: open-acceldata-users-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/overlays/acceldata-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/acceldata-catalog-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/skills/acceldata-create-and-run-data-quality-policy.md
  title: ''
  type: AgentSkill
  url: skills/acceldata-create-and-run-data-quality-policy.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/skills/acceldata-discover-and-tag-assets.md
  title: ''
  type: AgentSkill
  url: skills/acceldata-discover-and-tag-assets.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/overlays/acceldata-administration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/acceldata-administration-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/skills/acceldata-provision-service-user-and-api-key.md
  title: ''
  type: AgentSkill
  url: skills/acceldata-provision-service-user-and-api-key.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/overlays/acceldata-tags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/acceldata-tags-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/agentic-access/acceldata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acceldata-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/security/acceldata-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/acceldata-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/security/acceldata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acceldata-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/authentication/acceldata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acceldata-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/acceldata/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/arazzo/acceldata-access-review-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/acceldata-access-review-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/arazzo/acceldata-create-and-verify-rule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/acceldata-create-and-verify-rule-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/arazzo/acceldata-critical-alert-sweep-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/acceldata-critical-alert-sweep-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/arazzo/acceldata-dataset-quality-audit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/acceldata-dataset-quality-audit-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/arazzo/acceldata-onboard-rule-with-impact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/acceldata-onboard-rule-with-impact-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/arazzo/acceldata-pipeline-failure-investigation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/acceldata-pipeline-failure-investigation-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/arazzo/acceldata-triage-dataset-alerts-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/acceldata-triage-dataset-alerts-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acceldata-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acceldata
- group: company
  title: ''
  type: Website
  url: https://www.acceldata.io/
- group: start
  title: ''
  type: Portal
  url: https://accounts.acceldata.app/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.acceldata.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.acceldata.io/api/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acceldata.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.acceldata.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acceldata.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acceldata.io/terms-of-use
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/rules/acceldata-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/acceldata-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/vocabulary/acceldata-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/acceldata-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/json-ld/acceldata-adoc-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/acceldata-adoc-api-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.acceldata.io/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/packages/acceldata-packages.yml
  title: ''
  type: Packages
  url: packages/acceldata-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/packages/acceldata-packages.yml
  title: ''
  type: SDKs
  url: packages/acceldata-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/well-known/acceldata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acceldata-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/mcp/acceldata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/acceldata-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/mcp/acceldata-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/acceldata-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/llms/acceldata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acceldata-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/conformance/acceldata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acceldata-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/conformance/acceldata-conformance.yml
  title: ''
  type: Compliance
  url: conformance/acceldata-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/errors/acceldata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acceldata-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/lifecycle/acceldata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/acceldata-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/lifecycle/acceldata-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/acceldata-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/scopes/acceldata-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/acceldata-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/conventions/acceldata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/acceldata-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/changelog/acceldata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/acceldata-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/cli/acceldata-cli.yml
  title: ''
  type: CLI
  url: cli/acceldata-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/data-model/acceldata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acceldata-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/plans/acceldata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acceldata-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/rate-limits/acceldata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/acceldata-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/security/acceldata-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/acceldata-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/security/acceldata-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/acceldata-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.acceldata.io/api
- group: start
  title: ''
  type: SignUp
  url: https://www.acceldata.io/free-trial
- group: operate
  title: ''
  type: Support
  url: https://acceldatatechnology.my.site.com/s/login/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/finops/acceldata-finops.yml
  title: ''
  type: FinOps
  url: finops/acceldata-finops.yml
created: '2025-02-24'
description: Acceldata is an agentic data management platform that helps enterprises monitor, govern, and optimize data across cloud, lakehouse, and hybrid environments. The platform combines AI-powered agents with data observability to proactively detect issues, trace root causes, and automate remediation workflows. Key products include ADM (Agentic Data Management), ADOC (Acceldata Data Observability Cloud), Pulse for Hadoop environments, and Agent Studio for building custom AI agents. It supports integrations with Snowflake, Databricks, AWS, GCP, Azure, and Hadoop.
examples:
- key_count: 2
  name: Adoc Api Acknowledge Alert Request Example
  slug: adoc-api-acknowledge-alert-request-example
- key_count: 9
  name: Adoc Api Alert Example
  slug: adoc-api-alert-example
- key_count: 4
  name: Adoc Api Alert List Example
  slug: adoc-api-alert-list-example
- key_count: 7
  name: Adoc Api Create Data Quality Rule Request Example
  slug: adoc-api-create-data-quality-rule-request-example
- key_count: 10
  name: Adoc Api Data Quality Rule Example
  slug: adoc-api-data-quality-rule-example
- key_count: 4
  name: Adoc Api Data Quality Rule List Example
  slug: adoc-api-data-quality-rule-list-example
- key_count: 10
  name: Adoc Api Dataset Example
  slug: adoc-api-dataset-example
- key_count: 4
  name: Adoc Api Dataset List Example
  slug: adoc-api-dataset-list-example
- key_count: 3
  name: Adoc Api Error Response Example
  slug: adoc-api-error-response-example
- key_count: 3
  name: Adoc Api Lineage Graph Example
  slug: adoc-api-lineage-graph-example
- key_count: 6
  name: Adoc Api Lineage Node Example
  slug: adoc-api-lineage-node-example
- key_count: 8
  name: Adoc Api Pipeline Job Example
  slug: adoc-api-pipeline-job-example
- key_count: 4
  name: Adoc Api Pipeline Job List Example
  slug: adoc-api-pipeline-job-list-example
- key_count: 5
  name: Adoc Api Role Example
  slug: adoc-api-role-example
- key_count: 4
  name: Adoc Api Role List Example
  slug: adoc-api-role-list-example
- key_count: 8
  name: Adoc Api User Example
  slug: adoc-api-user-example
- key_count: 4
  name: Adoc Api User List Example
  slug: adoc-api-user-list-example
features:
- description: AI-powered agents that proactively detect issues, trace root causes, and automate data quality remediation workflows
  name: Agentic Data Management
- description: Multi-variate anomaly detection, column-level profiling, and proactive monitoring across all data platforms
  name: Data Quality Monitoring
- description: End-to-end data lineage visualization with schema change management and column-level impact analysis
  name: Data Lineage
- description: Real-time SLA monitoring, bottleneck identification, and root cause analysis for data pipelines
  name: Pipeline Health Monitoring
- description: Visibility into data spending, budget optimization, chargebacks, and cost forecasting across cloud environments
  name: Data Cost Management
- description: Natural language interface with contextual memory for querying data quality and observability insights
  name: Business Notebook
- description: Low-code environment for building and deploying custom AI agents for data management workflows
  name: Agent Studio
- description: Bring Your Own Large Language Model for enterprise-controlled AI inference within data operations
  name: BYOLLM Support
- description: Exabyte-scale, AI-aware processing engine supporting cloud hyperscalers and on-premises deployments
  name: xLake Reasoning Engine
finops:
- name: Acceldata Finops
  service_category: API
  slug: acceldata-finops
image: /assets/icons/acceldata.png
json_schemas:
- name: AcknowledgeAlertRequest
  property_count: 1
  slug: adoc-api-acknowledge-alert-request
- name: AlertList
  property_count: 4
  slug: adoc-api-alert-list
- name: Alert
  property_count: 10
  slug: adoc-api-alert
- name: CreateDataQualityRuleRequest
  property_count: 6
  slug: adoc-api-create-data-quality-rule-request
- name: DataQualityRuleList
  property_count: 4
  slug: adoc-api-data-quality-rule-list
- name: DataQualityRule
  property_count: 10
  slug: adoc-api-data-quality-rule
- name: DatasetList
  property_count: 4
  slug: adoc-api-dataset-list
- name: Dataset
  property_count: 9
  slug: adoc-api-dataset
- name: ErrorResponse
  property_count: 3
  slug: adoc-api-error-response
- name: LineageGraph
  property_count: 4
  slug: adoc-api-lineage-graph
- name: LineageNode
  property_count: 3
  slug: adoc-api-lineage-node
- name: PipelineJobList
  property_count: 4
  slug: adoc-api-pipeline-job-list
- name: PipelineJob
  property_count: 8
  slug: adoc-api-pipeline-job
- name: RoleList
  property_count: 4
  slug: adoc-api-role-list
- name: Role
  property_count: 4
  slug: adoc-api-role
- name: UserList
  property_count: 4
  slug: adoc-api-user-list
- name: User
  property_count: 6
  slug: adoc-api-user
json_structures:
- name: Adoc Api Acknowledge Alert Request Structure
  property_count: 1
  slug: adoc-api-acknowledge-alert-request-structure
- name: Adoc Api Alert List Structure
  property_count: 4
  slug: adoc-api-alert-list-structure
- name: Adoc Api Alert Structure
  property_count: 10
  slug: adoc-api-alert-structure
- name: Adoc Api Create Data Quality Rule Request Structure
  property_count: 6
  slug: adoc-api-create-data-quality-rule-request-structure
- name: Adoc Api Data Quality Rule List Structure
  property_count: 4
  slug: adoc-api-data-quality-rule-list-structure
- name: Adoc Api Data Quality Rule Structure
  property_count: 10
  slug: adoc-api-data-quality-rule-structure
- name: Adoc Api Dataset List Structure
  property_count: 4
  slug: adoc-api-dataset-list-structure
- name: Adoc Api Dataset Structure
  property_count: 9
  slug: adoc-api-dataset-structure
- name: Adoc Api Error Response Structure
  property_count: 3
  slug: adoc-api-error-response-structure
- name: Adoc Api Lineage Graph Structure
  property_count: 4
  slug: adoc-api-lineage-graph-structure
- name: Adoc Api Lineage Node Structure
  property_count: 3
  slug: adoc-api-lineage-node-structure
- name: Adoc Api Pipeline Job List Structure
  property_count: 4
  slug: adoc-api-pipeline-job-list-structure
- name: Adoc Api Pipeline Job Structure
  property_count: 8
  slug: adoc-api-pipeline-job-structure
- name: Adoc Api Role List Structure
  property_count: 4
  slug: adoc-api-role-list-structure
- name: Adoc Api Role Structure
  property_count: 4
  slug: adoc-api-role-structure
- name: Adoc Api User List Structure
  property_count: 4
  slug: adoc-api-user-list-structure
- name: Adoc Api User Structure
  property_count: 6
  slug: adoc-api-user-structure
jsonld:
- class_count: 55
  name: Acceldata Adoc Api Context
  property_count: 5
  slug: acceldata-adoc-api-context
layout: provider
mcp_servers:
- description: ''
  name: Acceldata MCP Server
  slug: acceldata-mcp-server
modified: '2026-08-29'
name: Acceldata
nav: Providers
network: true
overview: 'Acceldata publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Data Quality Rules API, Datasets API, and 33 more. Tagged areas include AI Agents, Data Management, Data Observability, Data Pipeline, and Data Quality.


  The Acceldata catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Acceldata''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, changelog, and 50 more developer resources.'
plans:
- name: Acceldata Plans Pricing
  plan_count: 4
  slug: acceldata-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Acceldata Rate Limits
  slug: acceldata-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Acceldata API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: acceldata-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Acceldata API Rules
  rule_count: 32
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 17
  slug: acceldata-spectral-rules
scopes:
- name: Acceldata Scopes
  scope_count: 0
  slug: acceldata-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.3
  facets:
    access_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 57.1
    developer_ergonomics: 41.1
    discoverability: 57.4
    operational_transparency: 36.8
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 21.6
      derived: 7
      marker_coverage: 18.9
      total: 37
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/screenshots/acceldata-2026-08-17T082111.png
security:
- kind: authentication
  name: Acceldata Authentication
  slug: acceldata-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Acceldata Domain Security
  slug: acceldata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acceldata Vulnerability Disclosure
  slug: acceldata-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Acceldata Trust Center
  slug: acceldata-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: acceldata
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
use_cases:
- description: Continuously monitor and automatically remediate data quality issues across cloud and hybrid environments
  name: Data Quality Assurance
- description: Validate data completeness, consistency, and accuracy during cloud migration projects
  name: Cloud Migration Validation
- description: Ensure data pipelines produce clean, reliable, and AI-ready datasets for training and inference
  name: AI and LLM Data Readiness
- description: Identify and reduce wasteful data pipeline and infrastructure costs with granular usage analytics
  name: Cost Optimization and FinOps
- description: Automatically detect and resolve discrepancies between source and target systems across platforms
  name: Data Reconciliation
- description: Track data lineage and access patterns to support regulatory compliance and data governance programs
  name: Compliance and Data Governance
website: https://www.acceldata.io/
---
