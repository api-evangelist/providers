---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Amazon Detective Agentic Access
  operation_count: 29
  slug: amazon-detective-agentic-access
  summary_line: 29 operations · 28 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Data source package management operations
  name: Amazon Detective Datasources API
  slug: amazon-detective-datasources-api
- description: Behavior graph management operations
  name: Amazon Detective Graph API
  slug: amazon-detective-graph-api
- description: Security investigation operations
  name: Amazon Detective Investigations API
  slug: amazon-detective-investigations-api
- description: Invitation management for member accounts
  name: Amazon Detective Invitations API
  slug: amazon-detective-invitations-api
- description: Member account management operations
  name: Amazon Detective Members API
  slug: amazon-detective-members-api
- description: AWS Organizations integration operations
  name: Amazon Detective Organizations API
  slug: amazon-detective-organizations-api
- description: Resource tagging operations
  name: Amazon Detective Tags API
  slug: amazon-detective-tags-api
arazzos:
- description: Find a behavior graph's investigations, inspect one, and archive it when it has succeeded.
  name: Amazon Detective Archive a Resolved Investigation
  slug: amazon-detective-archive-resolved-investigation-workflow
- description: Start a data source package on a behavior graph and verify its ingest state.
  name: Amazon Detective Enable a Data Source Package
  slug: amazon-detective-enable-datasource-package-workflow
- description: Create a new behavior graph and invite member accounts, then confirm their membership status.
  name: Amazon Detective Onboard a Behavior Graph with Member Accounts
  slug: amazon-detective-graph-onboard-members-workflow
- description: List open invitations for a member account, accept one, and confirm enrollment.
  name: Amazon Detective Member Accepts a Behavior Graph Invitation
  slug: amazon-detective-member-accept-invitation-workflow
- description: Start an investigation on an entity, poll until it completes, then list its indicators.
  name: Amazon Detective Run an Investigation and Collect Indicators
  slug: amazon-detective-run-investigation-workflow
- description: Invite a member account, enable data ingest for it, and confirm it is being monitored.
  name: Amazon Detective Start Monitoring a Member Account
  slug: amazon-detective-start-monitoring-member-workflow
- description: Discover behavior graphs, apply tag values to one, and read the tags back.
  name: Amazon Detective Tag a Behavior Graph
  slug: amazon-detective-tag-behavior-graph-workflow
artifact_total: 210
collections:
- collection_type: postman
  name: Amazon Detective
  slug: postman-amazon-detective
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Detective Datasources API
  slug: open-amazon-detective-datasources-api
- collection_type: open
  name: Amazon Detective Datasources Graph API
  slug: open-amazon-detective-graph-api
- collection_type: open
  name: Amazon Detective Datasources Investigations API
  slug: open-amazon-detective-investigations-api
- collection_type: open
  name: Amazon Detective Datasources Invitations API
  slug: open-amazon-detective-invitations-api
- collection_type: open
  name: Amazon Detective Datasources Members API
  slug: open-amazon-detective-members-api
- collection_type: open
  name: Amazon Detective Datasources Organizations API
  slug: open-amazon-detective-organizations-api
- collection_type: open
  name: Amazon Detective Datasources Tags API
  slug: open-amazon-detective-tags-api
- collection_type: open
  name: Amazon Detective
  slug: open-amazon-detective
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-detective-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-detective-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-detective-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-detective-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-detective-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-detective/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-detective-archive-resolved-investigation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-detective-enable-datasource-package-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-detective-graph-onboard-members-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-detective-member-accept-invitation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-detective-run-investigation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-detective-start-monitoring-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-detective-tag-behavior-graph-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/detective/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/detective/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/detective/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/tag/amazon-detective/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.aws.amazon.com/detective/latest/userguide/release-notes.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-detective-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-detective-vocabulary.yaml
created: '2024-01-15'
description: Amazon Detective is a security investigation service that makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. It automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build interactive visualizations that help you conduct faster and more efficient security investigations.
examples:
- key_count: 1
  name: Amazon Detective Accept Invitation Request Example
  slug: amazon-detective-accept-invitation-request-example
- key_count: 2
  name: Amazon Detective Account Example
  slug: amazon-detective-account-example
- key_count: 3
  name: Amazon Detective Administrator Example
  slug: amazon-detective-administrator-example
- key_count: 2
  name: Amazon Detective Batch Get Graph Member Datasources Request Example
  slug: amazon-detective-batch-get-graph-member-datasources-request-example
- key_count: 2
  name: Amazon Detective Batch Get Graph Member Datasources Response Example
  slug: amazon-detective-batch-get-graph-member-datasources-response-example
- key_count: 1
  name: Amazon Detective Batch Get Membership Datasources Request Example
  slug: amazon-detective-batch-get-membership-datasources-request-example
- key_count: 2
  name: Amazon Detective Batch Get Membership Datasources Response Example
  slug: amazon-detective-batch-get-membership-datasources-response-example
- key_count: 1
  name: Amazon Detective Create Graph Request Example
  slug: amazon-detective-create-graph-request-example
- key_count: 1
  name: Amazon Detective Create Graph Response Example
  slug: amazon-detective-create-graph-response-example
- key_count: 4
  name: Amazon Detective Create Members Request Example
  slug: amazon-detective-create-members-request-example
- key_count: 2
  name: Amazon Detective Create Members Response Example
  slug: amazon-detective-create-members-response-example
- key_count: 2
  name: Amazon Detective Datasource Package Ingest Detail Example
  slug: amazon-detective-datasource-package-ingest-detail-example
- key_count: 1
  name: Amazon Detective Delete Graph Request Example
  slug: amazon-detective-delete-graph-request-example
- key_count: 2
  name: Amazon Detective Delete Members Request Example
  slug: amazon-detective-delete-members-request-example
- key_count: 2
  name: Amazon Detective Delete Members Response Example
  slug: amazon-detective-delete-members-response-example
- key_count: 1
  name: Amazon Detective Describe Organization Configuration Request Example
  slug: amazon-detective-describe-organization-configuration-request-example
- key_count: 1
  name: Amazon Detective Describe Organization Configuration Response Example
  slug: amazon-detective-describe-organization-configuration-response-example
- key_count: 1
  name: Amazon Detective Disassociate Membership Request Example
  slug: amazon-detective-disassociate-membership-request-example
- key_count: 1
  name: Amazon Detective Enable Organization Admin Account Request Example
  slug: amazon-detective-enable-organization-admin-account-request-example
- key_count: 2
  name: Amazon Detective Get Investigation Request Example
  slug: amazon-detective-get-investigation-request-example
- key_count: 10
  name: Amazon Detective Get Investigation Response Example
  slug: amazon-detective-get-investigation-response-example
- key_count: 2
  name: Amazon Detective Get Members Request Example
  slug: amazon-detective-get-members-request-example
- key_count: 2
  name: Amazon Detective Get Members Response Example
  slug: amazon-detective-get-members-response-example
- key_count: 2
  name: Amazon Detective Graph Example
  slug: amazon-detective-graph-example
- key_count: 2
  name: Amazon Detective Indicator Example
  slug: amazon-detective-indicator-example
- key_count: 7
  name: Amazon Detective Investigation Detail Example
  slug: amazon-detective-investigation-detail-example
- key_count: 3
  name: Amazon Detective List Datasource Packages Request Example
  slug: amazon-detective-list-datasource-packages-request-example
- key_count: 2
  name: Amazon Detective List Datasource Packages Response Example
  slug: amazon-detective-list-datasource-packages-response-example
- key_count: 2
  name: Amazon Detective List Graphs Request Example
  slug: amazon-detective-list-graphs-request-example
- key_count: 2
  name: Amazon Detective List Graphs Response Example
  slug: amazon-detective-list-graphs-response-example
- key_count: 5
  name: Amazon Detective List Indicators Request Example
  slug: amazon-detective-list-indicators-request-example
- key_count: 4
  name: Amazon Detective List Indicators Response Example
  slug: amazon-detective-list-indicators-response-example
- key_count: 5
  name: Amazon Detective List Investigations Request Example
  slug: amazon-detective-list-investigations-request-example
- key_count: 2
  name: Amazon Detective List Investigations Response Example
  slug: amazon-detective-list-investigations-response-example
- key_count: 2
  name: Amazon Detective List Invitations Request Example
  slug: amazon-detective-list-invitations-request-example
- key_count: 2
  name: Amazon Detective List Invitations Response Example
  slug: amazon-detective-list-invitations-response-example
- key_count: 3
  name: Amazon Detective List Members Request Example
  slug: amazon-detective-list-members-request-example
- key_count: 2
  name: Amazon Detective List Members Response Example
  slug: amazon-detective-list-members-response-example
- key_count: 2
  name: Amazon Detective List Organization Admin Accounts Request Example
  slug: amazon-detective-list-organization-admin-accounts-request-example
- key_count: 2
  name: Amazon Detective List Organization Admin Accounts Response Example
  slug: amazon-detective-list-organization-admin-accounts-response-example
- key_count: 1
  name: Amazon Detective List Tags For Resource Response Example
  slug: amazon-detective-list-tags-for-resource-response-example
- key_count: 12
  name: Amazon Detective Member Detail Example
  slug: amazon-detective-member-detail-example
- key_count: 3
  name: Amazon Detective Membership Datasources Example
  slug: amazon-detective-membership-datasources-example
- key_count: 1
  name: Amazon Detective Reject Invitation Request Example
  slug: amazon-detective-reject-invitation-request-example
- key_count: 4
  name: Amazon Detective Start Investigation Request Example
  slug: amazon-detective-start-investigation-request-example
- key_count: 1
  name: Amazon Detective Start Investigation Response Example
  slug: amazon-detective-start-investigation-response-example
- key_count: 2
  name: Amazon Detective Start Monitoring Member Request Example
  slug: amazon-detective-start-monitoring-member-request-example
- key_count: 1
  name: Amazon Detective Tag Resource Request Example
  slug: amazon-detective-tag-resource-request-example
- key_count: 1
  name: Amazon Detective Timestamp For Collection Example
  slug: amazon-detective-timestamp-for-collection-example
- key_count: 2
  name: Amazon Detective Unprocessed Account Example
  slug: amazon-detective-unprocessed-account-example
- key_count: 2
  name: Amazon Detective Unprocessed Graph Example
  slug: amazon-detective-unprocessed-graph-example
- key_count: 2
  name: Amazon Detective Update Datasource Packages Request Example
  slug: amazon-detective-update-datasource-packages-request-example
- key_count: 3
  name: Amazon Detective Update Investigation State Request Example
  slug: amazon-detective-update-investigation-state-request-example
- key_count: 2
  name: Amazon Detective Update Organization Configuration Request Example
  slug: amazon-detective-update-organization-configuration-request-example
features:
- description: Automatically builds a behavior graph from log data using machine learning and graph theory to visualize security issues.
  name: Behavior Graph Analysis
- description: Start and manage structured investigations on IAM users and roles with scoped time ranges and severity scoring.
  name: Security Investigations
- description: Automatically identifies indicators including impossible travel, flagged IP addresses, new geolocations, new user agents, and TTP observations.
  name: Indicators of Compromise
- description: Aggregate security data from multiple AWS accounts using an administrator account and member account model.
  name: Multi-Account Support
- description: Automatically enable new organization accounts as member accounts in the organization behavior graph.
  name: AWS Organizations Integration
- description: Ingest security telemetry from CloudTrail, VPC Flow Logs, GuardDuty findings, EKS audit logs, and Active Directory audit logs.
  name: Data Source Packages
- description: Provides interactive graph visualizations in the AWS console to explore entity relationships and security events.
  name: Interactive Visualizations
- description: Assigns severity levels (Informational, Low, Medium, High, Critical) based on likelihood and impact of compromise indicators.
  name: Investigation Severity Scoring
finops:
- name: Amazon Detective Finops
  service_category: API
  slug: amazon-detective-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AcceptInvitationRequest
  property_count: 1
  slug: amazon-detective-accept-invitation-request
- name: Account
  property_count: 2
  slug: amazon-detective-account
- name: Administrator
  property_count: 3
  slug: amazon-detective-administrator
- name: BatchGetGraphMemberDatasourcesRequest
  property_count: 2
  slug: amazon-detective-batch-get-graph-member-datasources-request
- name: BatchGetGraphMemberDatasourcesResponse
  property_count: 2
  slug: amazon-detective-batch-get-graph-member-datasources-response
- name: BatchGetMembershipDatasourcesRequest
  property_count: 1
  slug: amazon-detective-batch-get-membership-datasources-request
- name: BatchGetMembershipDatasourcesResponse
  property_count: 2
  slug: amazon-detective-batch-get-membership-datasources-response
- name: CreateGraphRequest
  property_count: 1
  slug: amazon-detective-create-graph-request
- name: CreateGraphResponse
  property_count: 1
  slug: amazon-detective-create-graph-response
- name: CreateMembersRequest
  property_count: 4
  slug: amazon-detective-create-members-request
- name: CreateMembersResponse
  property_count: 2
  slug: amazon-detective-create-members-response
- name: DatasourcePackageIngestDetail
  property_count: 2
  slug: amazon-detective-datasource-package-ingest-detail
- name: DeleteGraphRequest
  property_count: 1
  slug: amazon-detective-delete-graph-request
- name: DeleteMembersRequest
  property_count: 2
  slug: amazon-detective-delete-members-request
- name: DeleteMembersResponse
  property_count: 2
  slug: amazon-detective-delete-members-response
- name: DescribeOrganizationConfigurationRequest
  property_count: 1
  slug: amazon-detective-describe-organization-configuration-request
- name: DescribeOrganizationConfigurationResponse
  property_count: 1
  slug: amazon-detective-describe-organization-configuration-response
- name: DisassociateMembershipRequest
  property_count: 1
  slug: amazon-detective-disassociate-membership-request
- name: EnableOrganizationAdminAccountRequest
  property_count: 1
  slug: amazon-detective-enable-organization-admin-account-request
- name: GetInvestigationRequest
  property_count: 2
  slug: amazon-detective-get-investigation-request
- name: GetInvestigationResponse
  property_count: 10
  slug: amazon-detective-get-investigation-response
- name: GetMembersRequest
  property_count: 2
  slug: amazon-detective-get-members-request
- name: GetMembersResponse
  property_count: 2
  slug: amazon-detective-get-members-response
- name: Graph
  property_count: 2
  slug: amazon-detective-graph
- name: Indicator
  property_count: 2
  slug: amazon-detective-indicator
- name: InvestigationDetail
  property_count: 7
  slug: amazon-detective-investigation-detail
- name: ListDatasourcePackagesRequest
  property_count: 3
  slug: amazon-detective-list-datasource-packages-request
- name: ListDatasourcePackagesResponse
  property_count: 2
  slug: amazon-detective-list-datasource-packages-response
- name: ListGraphsRequest
  property_count: 2
  slug: amazon-detective-list-graphs-request
- name: ListGraphsResponse
  property_count: 2
  slug: amazon-detective-list-graphs-response
- name: ListIndicatorsRequest
  property_count: 5
  slug: amazon-detective-list-indicators-request
- name: ListIndicatorsResponse
  property_count: 4
  slug: amazon-detective-list-indicators-response
- name: ListInvestigationsRequest
  property_count: 5
  slug: amazon-detective-list-investigations-request
- name: ListInvestigationsResponse
  property_count: 2
  slug: amazon-detective-list-investigations-response
- name: ListInvitationsRequest
  property_count: 2
  slug: amazon-detective-list-invitations-request
- name: ListInvitationsResponse
  property_count: 2
  slug: amazon-detective-list-invitations-response
- name: ListMembersRequest
  property_count: 3
  slug: amazon-detective-list-members-request
- name: ListMembersResponse
  property_count: 2
  slug: amazon-detective-list-members-response
- name: ListOrganizationAdminAccountsRequest
  property_count: 2
  slug: amazon-detective-list-organization-admin-accounts-request
- name: ListOrganizationAdminAccountsResponse
  property_count: 2
  slug: amazon-detective-list-organization-admin-accounts-response
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-detective-list-tags-for-resource-response
- name: MemberDetail
  property_count: 12
  slug: amazon-detective-member-detail
- name: MembershipDatasources
  property_count: 3
  slug: amazon-detective-membership-datasources
- name: RejectInvitationRequest
  property_count: 1
  slug: amazon-detective-reject-invitation-request
- name: StartInvestigationRequest
  property_count: 4
  slug: amazon-detective-start-investigation-request
- name: StartInvestigationResponse
  property_count: 1
  slug: amazon-detective-start-investigation-response
- name: StartMonitoringMemberRequest
  property_count: 2
  slug: amazon-detective-start-monitoring-member-request
- name: TagResourceRequest
  property_count: 1
  slug: amazon-detective-tag-resource-request
- name: TimestampForCollection
  property_count: 1
  slug: amazon-detective-timestamp-for-collection
- name: UnprocessedAccount
  property_count: 2
  slug: amazon-detective-unprocessed-account
- name: UnprocessedGraph
  property_count: 2
  slug: amazon-detective-unprocessed-graph
- name: UpdateDatasourcePackagesRequest
  property_count: 2
  slug: amazon-detective-update-datasource-packages-request
- name: UpdateInvestigationStateRequest
  property_count: 3
  slug: amazon-detective-update-investigation-state-request
- name: UpdateOrganizationConfigurationRequest
  property_count: 2
  slug: amazon-detective-update-organization-configuration-request
json_structures:
- name: Amazon Detective Accept Invitation Request Structure
  property_count: 1
  slug: amazon-detective-accept-invitation-request-structure
- name: Amazon Detective Account Structure
  property_count: 2
  slug: amazon-detective-account-structure
- name: Amazon Detective Administrator Structure
  property_count: 3
  slug: amazon-detective-administrator-structure
- name: Amazon Detective Batch Get Graph Member Datasources Request Structure
  property_count: 2
  slug: amazon-detective-batch-get-graph-member-datasources-request-structure
- name: Amazon Detective Batch Get Graph Member Datasources Response Structure
  property_count: 2
  slug: amazon-detective-batch-get-graph-member-datasources-response-structure
- name: Amazon Detective Batch Get Membership Datasources Request Structure
  property_count: 1
  slug: amazon-detective-batch-get-membership-datasources-request-structure
- name: Amazon Detective Batch Get Membership Datasources Response Structure
  property_count: 2
  slug: amazon-detective-batch-get-membership-datasources-response-structure
- name: Amazon Detective Create Graph Request Structure
  property_count: 1
  slug: amazon-detective-create-graph-request-structure
- name: Amazon Detective Create Graph Response Structure
  property_count: 1
  slug: amazon-detective-create-graph-response-structure
- name: Amazon Detective Create Members Request Structure
  property_count: 4
  slug: amazon-detective-create-members-request-structure
- name: Amazon Detective Create Members Response Structure
  property_count: 2
  slug: amazon-detective-create-members-response-structure
- name: Amazon Detective Datasource Package Ingest Detail Structure
  property_count: 2
  slug: amazon-detective-datasource-package-ingest-detail-structure
- name: Amazon Detective Delete Graph Request Structure
  property_count: 1
  slug: amazon-detective-delete-graph-request-structure
- name: Amazon Detective Delete Members Request Structure
  property_count: 2
  slug: amazon-detective-delete-members-request-structure
- name: Amazon Detective Delete Members Response Structure
  property_count: 2
  slug: amazon-detective-delete-members-response-structure
- name: Amazon Detective Describe Organization Configuration Request Structure
  property_count: 1
  slug: amazon-detective-describe-organization-configuration-request-structure
- name: Amazon Detective Describe Organization Configuration Response Structure
  property_count: 1
  slug: amazon-detective-describe-organization-configuration-response-structure
- name: Amazon Detective Disassociate Membership Request Structure
  property_count: 1
  slug: amazon-detective-disassociate-membership-request-structure
- name: Amazon Detective Enable Organization Admin Account Request Structure
  property_count: 1
  slug: amazon-detective-enable-organization-admin-account-request-structure
- name: Amazon Detective Get Investigation Request Structure
  property_count: 2
  slug: amazon-detective-get-investigation-request-structure
- name: Amazon Detective Get Investigation Response Structure
  property_count: 10
  slug: amazon-detective-get-investigation-response-structure
- name: Amazon Detective Get Members Request Structure
  property_count: 2
  slug: amazon-detective-get-members-request-structure
- name: Amazon Detective Get Members Response Structure
  property_count: 2
  slug: amazon-detective-get-members-response-structure
- name: Amazon Detective Graph Structure
  property_count: 2
  slug: amazon-detective-graph-structure
- name: Amazon Detective Indicator Structure
  property_count: 2
  slug: amazon-detective-indicator-structure
- name: Amazon Detective Investigation Detail Structure
  property_count: 7
  slug: amazon-detective-investigation-detail-structure
- name: Amazon Detective List Datasource Packages Request Structure
  property_count: 3
  slug: amazon-detective-list-datasource-packages-request-structure
- name: Amazon Detective List Datasource Packages Response Structure
  property_count: 2
  slug: amazon-detective-list-datasource-packages-response-structure
- name: Amazon Detective List Graphs Request Structure
  property_count: 2
  slug: amazon-detective-list-graphs-request-structure
- name: Amazon Detective List Graphs Response Structure
  property_count: 2
  slug: amazon-detective-list-graphs-response-structure
- name: Amazon Detective List Indicators Request Structure
  property_count: 5
  slug: amazon-detective-list-indicators-request-structure
- name: Amazon Detective List Indicators Response Structure
  property_count: 4
  slug: amazon-detective-list-indicators-response-structure
- name: Amazon Detective List Investigations Request Structure
  property_count: 5
  slug: amazon-detective-list-investigations-request-structure
- name: Amazon Detective List Investigations Response Structure
  property_count: 2
  slug: amazon-detective-list-investigations-response-structure
- name: Amazon Detective List Invitations Request Structure
  property_count: 2
  slug: amazon-detective-list-invitations-request-structure
- name: Amazon Detective List Invitations Response Structure
  property_count: 2
  slug: amazon-detective-list-invitations-response-structure
- name: Amazon Detective List Members Request Structure
  property_count: 3
  slug: amazon-detective-list-members-request-structure
- name: Amazon Detective List Members Response Structure
  property_count: 2
  slug: amazon-detective-list-members-response-structure
- name: Amazon Detective List Organization Admin Accounts Request Structure
  property_count: 2
  slug: amazon-detective-list-organization-admin-accounts-request-structure
- name: Amazon Detective List Organization Admin Accounts Response Structure
  property_count: 2
  slug: amazon-detective-list-organization-admin-accounts-response-structure
- name: Amazon Detective List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-detective-list-tags-for-resource-response-structure
- name: Amazon Detective Member Detail Structure
  property_count: 12
  slug: amazon-detective-member-detail-structure
- name: Amazon Detective Membership Datasources Structure
  property_count: 3
  slug: amazon-detective-membership-datasources-structure
- name: Amazon Detective Reject Invitation Request Structure
  property_count: 1
  slug: amazon-detective-reject-invitation-request-structure
- name: Amazon Detective Start Investigation Request Structure
  property_count: 4
  slug: amazon-detective-start-investigation-request-structure
- name: Amazon Detective Start Investigation Response Structure
  property_count: 1
  slug: amazon-detective-start-investigation-response-structure
- name: Amazon Detective Start Monitoring Member Request Structure
  property_count: 2
  slug: amazon-detective-start-monitoring-member-request-structure
- name: Amazon Detective Tag Resource Request Structure
  property_count: 1
  slug: amazon-detective-tag-resource-request-structure
- name: Amazon Detective Timestamp For Collection Structure
  property_count: 1
  slug: amazon-detective-timestamp-for-collection-structure
- name: Amazon Detective Unprocessed Account Structure
  property_count: 2
  slug: amazon-detective-unprocessed-account-structure
- name: Amazon Detective Unprocessed Graph Structure
  property_count: 2
  slug: amazon-detective-unprocessed-graph-structure
- name: Amazon Detective Update Datasource Packages Request Structure
  property_count: 2
  slug: amazon-detective-update-datasource-packages-request-structure
- name: Amazon Detective Update Investigation State Request Structure
  property_count: 3
  slug: amazon-detective-update-investigation-state-request-structure
- name: Amazon Detective Update Organization Configuration Request Structure
  property_count: 2
  slug: amazon-detective-update-organization-configuration-request-structure
jsonld:
- class_count: 53
  name: Amazon Detective Context
  property_count: 55
  slug: amazon-detective-context
layout: provider
modified: '2026-05-19'
name: Amazon Detective
nav: Providers
network: true
overview: 'Amazon Detective publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Datasources API, Graph API, Investigations API, and 4 more. Tagged areas include Forensics, Investigation, and Security.


  The Amazon Detective catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Detective''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, engineering blog, and 22 more developer resources.'
plans:
- name: Amazon Detective Plans Pricing
  plan_count: 3
  slug: amazon-detective-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Amazon Detective Rate Limits
  slug: amazon-detective-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Detective API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-detective-jsonschema-spectral-rules
- effective_rule_count: 87
  extends:
  - spectral:oas
  name: Amazon Detective API Rules
  rule_count: 46
  severity_counts:
    error: 18
    hint: 0
    info: 9
    warn: 19
  slug: amazon-detective-spectral-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 32.4
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 42.1
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-detective/refs/heads/main/screenshots/amazon-detective-2026-06-20T171627.png
security:
- kind: authentication
  name: Amazon Detective Authentication
  slug: amazon-detective-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Detective Domain Security
  slug: amazon-detective-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Detective Vulnerability Disclosure
  slug: amazon-detective-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Detective Trust Center
  slug: amazon-detective-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-detective
tags:
- Forensics
- Investigation
- Security
use_cases:
- description: Rapidly investigate security incidents by analyzing entity behavior, network activity, and API call patterns across your AWS environment.
  name: Security Incident Investigation
- description: Proactively search for suspicious activity and potential threats using behavior analysis and machine learning across your AWS accounts.
  name: Threat Hunting
- description: Identify the root cause of security issues by exploring the relationships between resources, users, and events in a behavior graph.
  name: Root Cause Analysis
- description: Collect and preserve forensic evidence for compliance investigations using structured investigations with defined scope and time ranges.
  name: Compliance Forensics
- description: Centrally manage security investigations across an AWS Organization from a single administrator account.
  name: Multi-Account Security Operations
website: https://aws.amazon.com/detective/
---
