---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.7
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Google Cloud Platform Agentic Access
  operation_count: 28
  slug: google-cloud-platform-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 7
apis:
- description: Manage Google Cloud folders. Folders provide an additional grouping mechanism and isolation boundary between projects. They can be used to model organizational structure, departments, teams, or enviro
  name: Google Cloud Platform Folders API
  slug: google-cloud-platform-folders-api
- description: Long-running operations returned by Resource Manager API methods. Some methods return an Operation resource to track the progress of asynchronous requests.
  name: Google Cloud Platform Operations API
  slug: google-cloud-platform-operations-api
- description: Manage Google Cloud organizations. An organization is the root node in the Google Cloud resource hierarchy, typically representing a company or business entity. Organizations are tied to a Google Work
  name: Google Cloud Platform Organizations API
  slug: google-cloud-platform-organizations-api
- description: Manage Google Cloud projects. A project is the base-level organizing entity in Google Cloud and is required to use most Google Cloud services. Projects contain resources and are associated with billin
  name: Google Cloud Platform Projects API
  slug: google-cloud-platform-projects-api
- description: Manage tag bindings that associate tag values with Google Cloud resources. Tag bindings connect tag values to specific resources in the hierarchy.
  name: Google Cloud Platform TagBindings API
  slug: google-cloud-platform-tagbindings-api
- description: Manage tag keys used to organize and categorize Google Cloud resources. Tag keys define the namespace for tag values that can be attached to resources.
  name: Google Cloud Platform TagKeys API
  slug: google-cloud-platform-tagkeys-api
- description: Manage tag values associated with tag keys. Tag values are the specific labels that can be bound to resources through tag bindings.
  name: Google Cloud Platform TagValues API
  slug: google-cloud-platform-tagvalues-api
arazzos:
- description: Search for a folder, fetch its record, then list the projects directly under it.
  name: Google Cloud Platform Audit Folder and Projects
  slug: google-cloud-platform-audit-folder-and-projects-workflow
- description: Look up a tag value for a key, create a tag binding to a resource, poll, then list bindings.
  name: Google Cloud Platform Bind Tag to Project
  slug: google-cloud-platform-bind-tag-to-project-workflow
- description: Read the IAM policy of a source project and apply its bindings to a target project.
  name: Google Cloud Platform Copy Project IAM Policy
  slug: google-cloud-platform-copy-project-iam-policy-workflow
- description: Create a folder, poll the long-running operation until done, then read back the folder.
  name: Google Cloud Platform Create Folder and Poll Operation
  slug: google-cloud-platform-create-folder-and-poll-workflow
- description: Create a project, poll the long-running operation until done, then read back the project.
  name: Google Cloud Platform Create Project and Poll Operation
  slug: google-cloud-platform-create-project-and-poll-workflow
- description: Create a tag key, poll the operation, then create a tag value under it and poll again.
  name: Google Cloud Platform Create Tag Key and Value
  slug: google-cloud-platform-create-tag-key-and-value-workflow
- description: Mark a folder for deletion, wait for it, then undelete it within the grace period.
  name: Google Cloud Platform Delete and Restore Folder
  slug: google-cloud-platform-delete-and-restore-folder-workflow
- description: Mark a project for deletion, confirm DELETE_REQUESTED, then undelete it back to active.
  name: Google Cloud Platform Delete and Restore Project
  slug: google-cloud-platform-delete-and-restore-project-workflow
- description: Confirm a folder has no child projects, then delete it and poll the operation.
  name: Google Cloud Platform Delete Empty Folder
  slug: google-cloud-platform-delete-empty-folder-workflow
- description: Search for an organization, fetch its record, then read its IAM policy.
  name: Google Cloud Platform Inspect Organization Access
  slug: google-cloud-platform-inspect-organization-access-workflow
- description: List an organization's tag keys, then list the tag values under the first key.
  name: Google Cloud Platform Inventory Organization Tags
  slug: google-cloud-platform-inventory-organization-tags-workflow
- description: Read a project, patch its labels, poll the operation, then confirm the new labels.
  name: Google Cloud Platform Label Project and Poll Operation
  slug: google-cloud-platform-label-project-and-poll-workflow
- description: Read a folder, move it under a new parent, poll the operation, then confirm the new parent.
  name: Google Cloud Platform Move Folder and Poll Operation
  slug: google-cloud-platform-move-folder-and-poll-workflow
- description: Create a folder, wait for it, then create a project under that folder and wait for it.
  name: Google Cloud Platform Provision Folder with Project
  slug: google-cloud-platform-provision-folder-with-project-workflow
- description: Read a folder, patch its display name, poll the operation, then confirm the new name.
  name: Google Cloud Platform Rename Folder and Poll Operation
  slug: google-cloud-platform-rename-folder-and-poll-workflow
- description: Read a project, patch its display name, poll the operation, then confirm the new name.
  name: Google Cloud Platform Rename Project and Poll Operation
  slug: google-cloud-platform-rename-project-and-poll-workflow
- description: Read a project IAM policy, then overwrite it with a single owner binding using the etag.
  name: Google Cloud Platform Reset Project IAM Policy
  slug: google-cloud-platform-reset-project-iam-policy-workflow
- description: Fetch a project, read its IAM policy, then list the tag bindings applied to it.
  name: Google Cloud Platform Review Project Governance
  slug: google-cloud-platform-review-project-governance-workflow
- description: Search for a project, fetch its full record, then read its IAM policy.
  name: Google Cloud Platform Search and Inspect Project
  slug: google-cloud-platform-search-and-inspect-project-workflow
- description: Read an organization IAM policy, add a member binding, and write it back with the etag.
  name: Google Cloud Platform Update Organization IAM Policy
  slug: google-cloud-platform-update-organization-iam-policy-workflow
- description: Read a project IAM policy, add a member binding, and write the policy back with the etag.
  name: Google Cloud Platform Update Project IAM Policy
  slug: google-cloud-platform-update-project-iam-policy-workflow
- description: Find an organization, list its folders, then list the projects directly under it.
  name: Google Cloud Platform Walk Resource Hierarchy
  slug: google-cloud-platform-walk-resource-hierarchy-workflow
artifact_total: 194
collections:
- collection_type: postman
  name: Google Cloud Platform Google Cloud Resource Manager API
  slug: postman-cloud-resource-manager
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Platform Google Cloud Resource Manager API
  slug: open-cloud-resource-manager
- collection_type: open
  name: Google Cloud Platform Google Cloud Resource Manager Folders API
  slug: open-google-cloud-platform-folders-api
- collection_type: open
  name: Google Cloud Platform Google Cloud Resource Manager Folders Operations API
  slug: open-google-cloud-platform-operations-api
- collection_type: open
  name: Google Cloud Platform Google Cloud Resource Manager Folders Organizations API
  slug: open-google-cloud-platform-organizations-api
- collection_type: open
  name: Google Cloud Platform Google Cloud Resource Manager Folders Projects API
  slug: open-google-cloud-platform-projects-api
- collection_type: open
  name: Google Cloud Platform Google Cloud Resource Manager Folders TagBindings API
  slug: open-google-cloud-platform-tagbindings-api
- collection_type: open
  name: Google Cloud Platform Google Cloud Resource Manager Folders TagKeys API
  slug: open-google-cloud-platform-tagkeys-api
- collection_type: open
  name: Google Cloud Platform Google Cloud Resource Manager Folders TagValues API
  slug: open-google-cloud-platform-tagvalues-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-platform-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/google-cloud-platform-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/google-cloud-platform-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-cloud-platform-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-cloud-platform-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-cloud-platform-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-cloud-platform-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/google-cloud-platform-cloud-resource-manager-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/google-cloud-platform-grpc.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-cloud-platform-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-cloud-platform-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-cloud-platform-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-cloud-platform-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-cloud-platform-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-cloud-platform-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/google-cloud-platform-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/google-cloud-platform-sandbox.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-platform/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-audit-folder-and-projects-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-bind-tag-to-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-copy-project-iam-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-create-folder-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-create-project-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-create-tag-key-and-value-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-delete-and-restore-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-delete-and-restore-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-delete-empty-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-inspect-organization-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-inventory-organization-tags-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-label-project-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-move-folder-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-provision-folder-with-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-rename-folder-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-rename-project-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-reset-project-iam-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-review-project-governance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-search-and-inspect-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-update-organization-iam-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-update-project-iam-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-cloud-platform-walk-resource-hierarchy-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.google.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/docs/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/apis
- group: start
  title: ''
  type: Signup
  url: https://cloud.google.com/free
- group: start
  title: ''
  type: Login
  url: https://console.cloud.google.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud.google.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/support
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/pricing
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/sdk
- group: auth
  title: ''
  type: Security
  url: https://cloud.google.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/compliance
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cloud.google.com/release-notes
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/googlecloudplatform
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-cloud-platform
- group: other
  title: ''
  type: X
  url: https://twitter.com/googlecloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-cloud/
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-cloud-platform-spectral-rules.yml
created: '2024-01-15'
description: Google Cloud Platform enables developers to build, test, and deploy applications on Google's highly-scalable and reliable infrastructure.
examples:
- key_count: 2
  name: Cloud Resource Manager Binding Example
  slug: cloud-resource-manager-binding-example
- key_count: 4
  name: Cloud Resource Manager Expr Example
  slug: cloud-resource-manager-expr-example
- key_count: 8
  name: Cloud Resource Manager Folder Example
  slug: cloud-resource-manager-folder-example
- key_count: 1
  name: Cloud Resource Manager Get Iam Policy Request Example
  slug: cloud-resource-manager-get-iam-policy-request-example
- key_count: 2
  name: Cloud Resource Manager List Folders Response Example
  slug: cloud-resource-manager-list-folders-response-example
- key_count: 2
  name: Cloud Resource Manager List Projects Response Example
  slug: cloud-resource-manager-list-projects-response-example
- key_count: 2
  name: Cloud Resource Manager List Tag Bindings Response Example
  slug: cloud-resource-manager-list-tag-bindings-response-example
- key_count: 2
  name: Cloud Resource Manager List Tag Keys Response Example
  slug: cloud-resource-manager-list-tag-keys-response-example
- key_count: 2
  name: Cloud Resource Manager List Tag Values Response Example
  slug: cloud-resource-manager-list-tag-values-response-example
- key_count: 1
  name: Cloud Resource Manager Move Folder Request Example
  slug: cloud-resource-manager-move-folder-request-example
- key_count: 4
  name: Cloud Resource Manager Operation Example
  slug: cloud-resource-manager-operation-example
- key_count: 8
  name: Cloud Resource Manager Organization Example
  slug: cloud-resource-manager-organization-example
- key_count: 3
  name: Cloud Resource Manager Policy Example
  slug: cloud-resource-manager-policy-example
- key_count: 10
  name: Cloud Resource Manager Project Example
  slug: cloud-resource-manager-project-example
- key_count: 2
  name: Cloud Resource Manager Search Folders Response Example
  slug: cloud-resource-manager-search-folders-response-example
- key_count: 2
  name: Cloud Resource Manager Search Organizations Response Example
  slug: cloud-resource-manager-search-organizations-response-example
- key_count: 2
  name: Cloud Resource Manager Search Projects Response Example
  slug: cloud-resource-manager-search-projects-response-example
- key_count: 1
  name: Cloud Resource Manager Set Iam Policy Request Example
  slug: cloud-resource-manager-set-iam-policy-request-example
- key_count: 3
  name: Cloud Resource Manager Status Example
  slug: cloud-resource-manager-status-example
- key_count: 4
  name: Cloud Resource Manager Tag Binding Example
  slug: cloud-resource-manager-tag-binding-example
- key_count: 8
  name: Cloud Resource Manager Tag Key Example
  slug: cloud-resource-manager-tag-key-example
- key_count: 8
  name: Cloud Resource Manager Tag Value Example
  slug: cloud-resource-manager-tag-value-example
- key_count: 0
  name: Cloud Resource Manager Undelete Folder Request Example
  slug: cloud-resource-manager-undelete-folder-request-example
- key_count: 0
  name: Cloud Resource Manager Undelete Project Request Example
  slug: cloud-resource-manager-undelete-project-request-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerfolderscreate Example
  slug: google-cloud-platform-cloudresourcemanagerfolderscreate-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerfoldersdelete Example
  slug: google-cloud-platform-cloudresourcemanagerfoldersdelete-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerfoldersget Example
  slug: google-cloud-platform-cloudresourcemanagerfoldersget-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerfolderslist Example
  slug: google-cloud-platform-cloudresourcemanagerfolderslist-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerfoldersmove Example
  slug: google-cloud-platform-cloudresourcemanagerfoldersmove-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerfolderspatch Example
  slug: google-cloud-platform-cloudresourcemanagerfolderspatch-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerfolderssearch Example
  slug: google-cloud-platform-cloudresourcemanagerfolderssearch-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerfoldersundelete Example
  slug: google-cloud-platform-cloudresourcemanagerfoldersundelete-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanageroperationsget Example
  slug: google-cloud-platform-cloudresourcemanageroperationsget-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerorganizationsget Example
  slug: google-cloud-platform-cloudresourcemanagerorganizationsget-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerorganizationsgetiampolicy Example
  slug: google-cloud-platform-cloudresourcemanagerorganizationsgetiampolicy-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerorganizationssearch Example
  slug: google-cloud-platform-cloudresourcemanagerorganizationssearch-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerorganizationssetiampolicy Example
  slug: google-cloud-platform-cloudresourcemanagerorganizationssetiampolicy-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectscreate Example
  slug: google-cloud-platform-cloudresourcemanagerprojectscreate-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectsdelete Example
  slug: google-cloud-platform-cloudresourcemanagerprojectsdelete-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectsget Example
  slug: google-cloud-platform-cloudresourcemanagerprojectsget-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectsgetiampolicy Example
  slug: google-cloud-platform-cloudresourcemanagerprojectsgetiampolicy-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectslist Example
  slug: google-cloud-platform-cloudresourcemanagerprojectslist-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectspatch Example
  slug: google-cloud-platform-cloudresourcemanagerprojectspatch-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectssearch Example
  slug: google-cloud-platform-cloudresourcemanagerprojectssearch-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectssetiampolicy Example
  slug: google-cloud-platform-cloudresourcemanagerprojectssetiampolicy-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagerprojectsundelete Example
  slug: google-cloud-platform-cloudresourcemanagerprojectsundelete-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagertagbindingscreate Example
  slug: google-cloud-platform-cloudresourcemanagertagbindingscreate-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagertagbindingslist Example
  slug: google-cloud-platform-cloudresourcemanagertagbindingslist-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagertagkeyscreate Example
  slug: google-cloud-platform-cloudresourcemanagertagkeyscreate-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagertagkeyslist Example
  slug: google-cloud-platform-cloudresourcemanagertagkeyslist-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagertagvaluescreate Example
  slug: google-cloud-platform-cloudresourcemanagertagvaluescreate-example
- key_count: 6
  name: Google Cloud Platform Cloudresourcemanagertagvalueslist Example
  slug: google-cloud-platform-cloudresourcemanagertagvalueslist-example
features:
- description: Run workloads on virtual machines, containers, and serverless platforms with automatic scaling.
  name: Compute Services
- description: Store data in object storage, relational databases, NoSQL databases, and in-memory stores.
  name: Storage and Databases
- description: Build and deploy ML models with Vertex AI, Vision, Natural Language, Speech, and Translation APIs.
  name: AI and Machine Learning
- description: Process and analyze data at scale with BigQuery, Dataflow, Dataproc, and Pub/Sub.
  name: Data Analytics
- description: Connect resources with DNS, load balancing, VPN, and CDN services.
  name: Networking
- description: Protect resources with IAM, KMS, Secret Manager, and data loss prevention services.
  name: Security and Identity
- description: Build, deploy, and manage applications with Cloud Build, Artifact Registry, and Cloud Deploy.
  name: DevOps and CI/CD
- description: Run code without managing infrastructure using Cloud Functions, Cloud Run, and App Engine.
  name: Serverless Computing
- description: Organize resources with projects, folders, organizations, and tags in a hierarchical structure.
  name: Resource Management
- description: Monitor, log, and trace applications with Cloud Monitoring, Logging, and Trace services.
  name: Observability
finops:
- name: Google Cloud Platform Finops
  service_category: Cloud Platform
  slug: google-cloud-platform-finops
image: https://cloud.google.com/_static/images/cloud/icons/favicons/onecloud/super_cloud.png
json_schemas:
- name: Binding
  property_count: 2
  slug: cloud-resource-manager-binding
- name: Expr
  property_count: 4
  slug: cloud-resource-manager-expr
- name: Folder
  property_count: 8
  slug: cloud-resource-manager-folder
- name: GetIamPolicyRequest
  property_count: 1
  slug: cloud-resource-manager-get-iam-policy-request
- name: ListFoldersResponse
  property_count: 2
  slug: cloud-resource-manager-list-folders-response
- name: ListProjectsResponse
  property_count: 2
  slug: cloud-resource-manager-list-projects-response
- name: ListTagBindingsResponse
  property_count: 2
  slug: cloud-resource-manager-list-tag-bindings-response
- name: ListTagKeysResponse
  property_count: 2
  slug: cloud-resource-manager-list-tag-keys-response
- name: ListTagValuesResponse
  property_count: 2
  slug: cloud-resource-manager-list-tag-values-response
- name: MoveFolderRequest
  property_count: 1
  slug: cloud-resource-manager-move-folder-request
- name: Operation
  property_count: 4
  slug: cloud-resource-manager-operation
- name: Organization
  property_count: 8
  slug: cloud-resource-manager-organization
- name: Policy
  property_count: 3
  slug: cloud-resource-manager-policy
- name: Project
  property_count: 10
  slug: cloud-resource-manager-project
- name: SearchFoldersResponse
  property_count: 2
  slug: cloud-resource-manager-search-folders-response
- name: SearchOrganizationsResponse
  property_count: 2
  slug: cloud-resource-manager-search-organizations-response
- name: SearchProjectsResponse
  property_count: 2
  slug: cloud-resource-manager-search-projects-response
- name: SetIamPolicyRequest
  property_count: 1
  slug: cloud-resource-manager-set-iam-policy-request
- name: Status
  property_count: 3
  slug: cloud-resource-manager-status
- name: TagBinding
  property_count: 4
  slug: cloud-resource-manager-tag-binding
- name: TagKey
  property_count: 8
  slug: cloud-resource-manager-tag-key
- name: TagValue
  property_count: 8
  slug: cloud-resource-manager-tag-value
- name: UndeleteFolderRequest
  property_count: 0
  slug: cloud-resource-manager-undelete-folder-request
- name: UndeleteProjectRequest
  property_count: 0
  slug: cloud-resource-manager-undelete-project-request
- name: Google Cloud Platform Project Schema
  property_count: 9
  slug: gcp-project
- name: Binding
  property_count: 3
  slug: google-cloud-platform-binding
- name: Expr
  property_count: 4
  slug: google-cloud-platform-expr
- name: Folder
  property_count: 8
  slug: google-cloud-platform-folder
- name: GetIamPolicyRequest
  property_count: 1
  slug: google-cloud-platform-getiampolicyrequest
- name: ListFoldersResponse
  property_count: 2
  slug: google-cloud-platform-listfoldersresponse
- name: ListProjectsResponse
  property_count: 2
  slug: google-cloud-platform-listprojectsresponse
- name: ListTagBindingsResponse
  property_count: 2
  slug: google-cloud-platform-listtagbindingsresponse
- name: ListTagKeysResponse
  property_count: 2
  slug: google-cloud-platform-listtagkeysresponse
- name: ListTagValuesResponse
  property_count: 2
  slug: google-cloud-platform-listtagvaluesresponse
- name: MoveFolderRequest
  property_count: 1
  slug: google-cloud-platform-movefolderrequest
- name: Operation
  property_count: 5
  slug: google-cloud-platform-operation
- name: Organization
  property_count: 8
  slug: google-cloud-platform-organization
- name: Policy
  property_count: 3
  slug: google-cloud-platform-policy
- name: Project
  property_count: 10
  slug: google-cloud-platform-project
- name: SearchFoldersResponse
  property_count: 2
  slug: google-cloud-platform-searchfoldersresponse
- name: SearchOrganizationsResponse
  property_count: 2
  slug: google-cloud-platform-searchorganizationsresponse
- name: SearchProjectsResponse
  property_count: 2
  slug: google-cloud-platform-searchprojectsresponse
- name: SetIamPolicyRequest
  property_count: 2
  slug: google-cloud-platform-setiampolicyrequest
- name: Status
  property_count: 3
  slug: google-cloud-platform-status
- name: TagBinding
  property_count: 4
  slug: google-cloud-platform-tagbinding
- name: TagKey
  property_count: 8
  slug: google-cloud-platform-tagkey
- name: TagValue
  property_count: 8
  slug: google-cloud-platform-tagvalue
- name: UndeleteFolderRequest
  property_count: 0
  slug: google-cloud-platform-undeletefolderrequest
- name: UndeleteProjectRequest
  property_count: 0
  slug: google-cloud-platform-undeleteprojectrequest
json_structures:
- name: Cloud Resource Manager Binding Structure
  property_count: 2
  slug: cloud-resource-manager-binding-structure
- name: Cloud Resource Manager Expr Structure
  property_count: 4
  slug: cloud-resource-manager-expr-structure
- name: Cloud Resource Manager Folder Structure
  property_count: 8
  slug: cloud-resource-manager-folder-structure
- name: Cloud Resource Manager Get Iam Policy Request Structure
  property_count: 1
  slug: cloud-resource-manager-get-iam-policy-request-structure
- name: Cloud Resource Manager List Folders Response Structure
  property_count: 2
  slug: cloud-resource-manager-list-folders-response-structure
- name: Cloud Resource Manager List Projects Response Structure
  property_count: 2
  slug: cloud-resource-manager-list-projects-response-structure
- name: Cloud Resource Manager List Tag Bindings Response Structure
  property_count: 2
  slug: cloud-resource-manager-list-tag-bindings-response-structure
- name: Cloud Resource Manager List Tag Keys Response Structure
  property_count: 2
  slug: cloud-resource-manager-list-tag-keys-response-structure
- name: Cloud Resource Manager List Tag Values Response Structure
  property_count: 2
  slug: cloud-resource-manager-list-tag-values-response-structure
- name: Cloud Resource Manager Move Folder Request Structure
  property_count: 1
  slug: cloud-resource-manager-move-folder-request-structure
- name: Cloud Resource Manager Operation Structure
  property_count: 4
  slug: cloud-resource-manager-operation-structure
- name: Cloud Resource Manager Organization Structure
  property_count: 8
  slug: cloud-resource-manager-organization-structure
- name: Cloud Resource Manager Policy Structure
  property_count: 3
  slug: cloud-resource-manager-policy-structure
- name: Cloud Resource Manager Project Structure
  property_count: 10
  slug: cloud-resource-manager-project-structure
- name: Cloud Resource Manager Search Folders Response Structure
  property_count: 2
  slug: cloud-resource-manager-search-folders-response-structure
- name: Cloud Resource Manager Search Organizations Response Structure
  property_count: 2
  slug: cloud-resource-manager-search-organizations-response-structure
- name: Cloud Resource Manager Search Projects Response Structure
  property_count: 2
  slug: cloud-resource-manager-search-projects-response-structure
- name: Cloud Resource Manager Set Iam Policy Request Structure
  property_count: 1
  slug: cloud-resource-manager-set-iam-policy-request-structure
- name: Cloud Resource Manager Status Structure
  property_count: 3
  slug: cloud-resource-manager-status-structure
- name: Cloud Resource Manager Tag Binding Structure
  property_count: 4
  slug: cloud-resource-manager-tag-binding-structure
- name: Cloud Resource Manager Tag Key Structure
  property_count: 8
  slug: cloud-resource-manager-tag-key-structure
- name: Cloud Resource Manager Tag Value Structure
  property_count: 8
  slug: cloud-resource-manager-tag-value-structure
- name: Cloud Resource Manager Undelete Folder Request Structure
  property_count: 0
  slug: cloud-resource-manager-undelete-folder-request-structure
- name: Cloud Resource Manager Undelete Project Request Structure
  property_count: 0
  slug: cloud-resource-manager-undelete-project-request-structure
- name: Google Cloud Platform Structure
  property_count: 0
  slug: google-cloud-platform-structure
jsonld:
- class_count: 0
  name: Cloud Resource Manager Context
  property_count: 0
  slug: cloud-resource-manager-context
- class_count: 0
  name: Google Cloud Platform Context
  property_count: 22
  slug: google-cloud-platform-context
layout: provider
mcp_servers:
- description: ''
  name: google-cloud-platform-mcp.yml
  slug: google-cloud-platform-mcpyml
modified: '2026-06-20'
name: Google Cloud Platform
nav: Providers
network: true
overview: 'Google Cloud Platform publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Folders API, Operations API, Organizations API, and 4 more. Tagged areas include API Management, Cloud Computing, Infrastructure, and Platform as a Service.


  The Google Cloud Platform catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Google Cloud Platform''s developer surface includes authentication, changelog, CLI, sandbox, developer portal, documentation, getting-started guide, and 61 more developer resources.'
plans:
- name: Google Cloud Platform Plans Pricing
  plan_count: 5
  slug: google-cloud-platform-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 7
  name: Google Cloud Platform Rate Limits
  slug: google-cloud-platform-rate-limits
rules:
- name: Google Cloud Platform API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-cloud-platform-jsonschema-spectral-rules
- name: Google Cloud Platform API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 7
  slug: google-cloud-platform-spectral-rules
scopes:
- name: Google Cloud Platform Scopes
  scope_count: 2
  slug: google-cloud-platform-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.6
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 73.9
    developer_ergonomics: 78.3
    discoverability: 75.9
    governance: 69.8
    operational_transparency: 55.3
  previous_composite: 72.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-platform/refs/heads/main/screenshots/google-cloud-platform-2026-06-20T182128.png
security:
- kind: authentication
  name: Google Cloud Platform Authentication
  slug: google-cloud-platform-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Google Cloud Platform Domain Security
  slug: google-cloud-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Platform Vulnerability Disclosure
  slug: google-cloud-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Cloud Platform Trust Center
  slug: google-cloud-platform-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, PCI DSS, HIPAA, FedRAMP High, CSA STAR, GDPR, FIPS 140-2
slug: google-cloud-platform
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
use_cases:
- description: Migrate and modernize legacy applications to cloud-native architectures using containers and serverless.
  name: Application Modernization
- description: Build data lakes and run analytics pipelines with BigQuery, Dataflow, and Cloud Storage.
  name: Data Lake and Analytics
- description: Build intelligent applications with Vertex AI, Dialogflow, and pre-trained ML APIs.
  name: AI Application Development
- description: Manage workloads across multiple cloud providers with Anthos and GKE Enterprise.
  name: Multi-Cloud Management
- description: Deploy and manage IoT devices and edge computing workloads at scale.
  name: IoT and Edge Computing
website: https://cloud.google.com/developers
---
