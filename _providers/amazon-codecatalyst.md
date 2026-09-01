---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 25
  human_in_the_loop: 2
  name: Amazon Codecatalyst Agentic Access
  operation_count: 33
  slug: amazon-codecatalyst-agentic-access
  summary_line: 33 operations · 25 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The AccessTokens API from Amazon CodeCatalyst — 2 operation(s) for accesstokens.
  name: Amazon CodeCatalyst AccessTokens API
  slug: amazon-codecatalyst-accesstokens-api
- description: The Session API from Amazon CodeCatalyst — 1 operation(s) for session.
  name: Amazon CodeCatalyst Session API
  slug: amazon-codecatalyst-session-api
- description: The Spaces API from Amazon CodeCatalyst — 18 operation(s) for spaces.
  name: Amazon CodeCatalyst Spaces API
  slug: amazon-codecatalyst-spaces-api
- description: The UserDetails API from Amazon CodeCatalyst — 1 operation(s) for userdetails.
  name: Amazon CodeCatalyst UserDetails API
  slug: amazon-codecatalyst-userdetails-api
artifact_total: 466
collections:
- collection_type: postman
  name: Amazon CodeCatalyst AccessTokens API
  slug: postman-amazon-codecatalyst-accesstokens-api
- collection_type: postman
  name: Amazon CodeCatalyst AccessTokens Session API
  slug: postman-amazon-codecatalyst-session-api
- collection_type: postman
  name: Amazon CodeCatalyst AccessTokens Spaces API
  slug: postman-amazon-codecatalyst-spaces-api
- collection_type: postman
  name: Amazon CodeCatalyst AccessTokens UserDetails API
  slug: postman-amazon-codecatalyst-userdetails-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon CodeCatalyst AccessTokens API
  slug: open-amazon-codecatalyst-accesstokens-api
- collection_type: open
  name: Amazon CodeCatalyst AccessTokens Session API
  slug: open-amazon-codecatalyst-session-api
- collection_type: open
  name: Amazon CodeCatalyst AccessTokens Spaces API
  slug: open-amazon-codecatalyst-spaces-api
- collection_type: open
  name: Amazon CodeCatalyst AccessTokens UserDetails API
  slug: open-amazon-codecatalyst-userdetails-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-codecatalyst-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-codecatalyst-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-codecatalyst/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-codecatalyst-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-codecatalyst-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-codecatalyst-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-codecatalyst-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-codecatalyst-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/getting-started-overview.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/tokens-overview.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/codecatalyst/pricing/
- group: start
  title: ''
  type: Console
  url: https://codecatalyst.aws/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/codecatalyst/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/
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
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/
- group: company
  title: ''
  type: BlogRSS
  url: https://aws.amazon.com/blogs/devops/tag/amazon-codecatalyst/feed/
- group: start
  title: ''
  type: SignUp
  url: https://codecatalyst.aws/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-codecatalyst-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-codecatalyst-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-codecatalyst-context.jsonld
- group: build
  title: ''
  type: Packages
  url: packages/amazon-codecatalyst-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-codecatalyst-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-codecatalyst-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-codecatalyst-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-codecatalyst-lifecycle.yml
created: '2026-03-16'
description: Amazon CodeCatalyst is a unified software development service that helps teams collaborate more effectively on software projects. It provides integrated tools for source code management, CI/CD workflows, issue tracking, and cloud-based development environments (Dev Environments). Teams can use CodeCatalyst to accelerate development velocity, standardize workflows, and integrate natively with AWS services and third-party tools.
examples:
- key_count: 3
  name: Amazon Codecatalyst Access Token Summary Example
  slug: amazon-codecatalyst-access-token-summary-example
- key_count: 2
  name: Amazon Codecatalyst Create Access Token Request Example
  slug: amazon-codecatalyst-create-access-token-request-example
- key_count: 4
  name: Amazon Codecatalyst Create Access Token Response Example
  slug: amazon-codecatalyst-create-access-token-response-example
- key_count: 7
  name: Amazon Codecatalyst Create Dev Environment Request Example
  slug: amazon-codecatalyst-create-dev-environment-request-example
- key_count: 3
  name: Amazon Codecatalyst Create Dev Environment Response Example
  slug: amazon-codecatalyst-create-dev-environment-response-example
- key_count: 2
  name: Amazon Codecatalyst Create Project Request Example
  slug: amazon-codecatalyst-create-project-request-example
- key_count: 4
  name: Amazon Codecatalyst Create Project Response Example
  slug: amazon-codecatalyst-create-project-response-example
- key_count: 1
  name: Amazon Codecatalyst Create Source Repository Branch Request Example
  slug: amazon-codecatalyst-create-source-repository-branch-request-example
- key_count: 4
  name: Amazon Codecatalyst Create Source Repository Branch Response Example
  slug: amazon-codecatalyst-create-source-repository-branch-response-example
- key_count: 1
  name: Amazon Codecatalyst Create Source Repository Request Example
  slug: amazon-codecatalyst-create-source-repository-request-example
- key_count: 4
  name: Amazon Codecatalyst Create Source Repository Response Example
  slug: amazon-codecatalyst-create-source-repository-response-example
- key_count: 0
  name: Amazon Codecatalyst Delete Access Token Request Example
  slug: amazon-codecatalyst-delete-access-token-request-example
- key_count: 0
  name: Amazon Codecatalyst Delete Access Token Response Example
  slug: amazon-codecatalyst-delete-access-token-response-example
- key_count: 0
  name: Amazon Codecatalyst Delete Dev Environment Request Example
  slug: amazon-codecatalyst-delete-dev-environment-request-example
- key_count: 3
  name: Amazon Codecatalyst Delete Dev Environment Response Example
  slug: amazon-codecatalyst-delete-dev-environment-response-example
- key_count: 0
  name: Amazon Codecatalyst Delete Project Request Example
  slug: amazon-codecatalyst-delete-project-request-example
- key_count: 3
  name: Amazon Codecatalyst Delete Project Response Example
  slug: amazon-codecatalyst-delete-project-response-example
- key_count: 0
  name: Amazon Codecatalyst Delete Source Repository Request Example
  slug: amazon-codecatalyst-delete-source-repository-request-example
- key_count: 3
  name: Amazon Codecatalyst Delete Source Repository Response Example
  slug: amazon-codecatalyst-delete-source-repository-response-example
- key_count: 0
  name: Amazon Codecatalyst Delete Space Request Example
  slug: amazon-codecatalyst-delete-space-request-example
- key_count: 2
  name: Amazon Codecatalyst Delete Space Response Example
  slug: amazon-codecatalyst-delete-space-response-example
- key_count: 2
  name: Amazon Codecatalyst Dev Environment Access Details Example
  slug: amazon-codecatalyst-dev-environment-access-details-example
- key_count: 2
  name: Amazon Codecatalyst Dev Environment Repository Summary Example
  slug: amazon-codecatalyst-dev-environment-repository-summary-example
- key_count: 2
  name: Amazon Codecatalyst Dev Environment Session Configuration Example
  slug: amazon-codecatalyst-dev-environment-session-configuration-example
- key_count: 5
  name: Amazon Codecatalyst Dev Environment Session Summary Example
  slug: amazon-codecatalyst-dev-environment-session-summary-example
- key_count: 8
  name: Amazon Codecatalyst Dev Environment Summary Example
  slug: amazon-codecatalyst-dev-environment-summary-example
- key_count: 2
  name: Amazon Codecatalyst Email Address Example
  slug: amazon-codecatalyst-email-address-example
- key_count: 8
  name: Amazon Codecatalyst Event Log Entry Example
  slug: amazon-codecatalyst-event-log-entry-example
- key_count: 2
  name: Amazon Codecatalyst Event Payload Example
  slug: amazon-codecatalyst-event-payload-example
- key_count: 2
  name: Amazon Codecatalyst Execute Command Session Configuration Example
  slug: amazon-codecatalyst-execute-command-session-configuration-example
- key_count: 3
  name: Amazon Codecatalyst Filter Example
  slug: amazon-codecatalyst-filter-example
- key_count: 0
  name: Amazon Codecatalyst Get Dev Environment Request Example
  slug: amazon-codecatalyst-get-dev-environment-request-example
- key_count: 8
  name: Amazon Codecatalyst Get Dev Environment Response Example
  slug: amazon-codecatalyst-get-dev-environment-response-example
- key_count: 0
  name: Amazon Codecatalyst Get Project Request Example
  slug: amazon-codecatalyst-get-project-request-example
- key_count: 4
  name: Amazon Codecatalyst Get Project Response Example
  slug: amazon-codecatalyst-get-project-response-example
- key_count: 0
  name: Amazon Codecatalyst Get Source Repository Clone Urls Request Example
  slug: amazon-codecatalyst-get-source-repository-clone-urls-request-example
- key_count: 1
  name: Amazon Codecatalyst Get Source Repository Clone Urls Response Example
  slug: amazon-codecatalyst-get-source-repository-clone-urls-response-example
- key_count: 0
  name: Amazon Codecatalyst Get Source Repository Request Example
  slug: amazon-codecatalyst-get-source-repository-request-example
- key_count: 6
  name: Amazon Codecatalyst Get Source Repository Response Example
  slug: amazon-codecatalyst-get-source-repository-response-example
- key_count: 0
  name: Amazon Codecatalyst Get Space Request Example
  slug: amazon-codecatalyst-get-space-request-example
- key_count: 4
  name: Amazon Codecatalyst Get Space Response Example
  slug: amazon-codecatalyst-get-space-response-example
- key_count: 0
  name: Amazon Codecatalyst Get Subscription Request Example
  slug: amazon-codecatalyst-get-subscription-request-example
- key_count: 2
  name: Amazon Codecatalyst Get Subscription Response Example
  slug: amazon-codecatalyst-get-subscription-response-example
- key_count: 0
  name: Amazon Codecatalyst Get User Details Request Example
  slug: amazon-codecatalyst-get-user-details-request-example
- key_count: 5
  name: Amazon Codecatalyst Get User Details Response Example
  slug: amazon-codecatalyst-get-user-details-response-example
- key_count: 2
  name: Amazon Codecatalyst Ide Configuration Example
  slug: amazon-codecatalyst-ide-configuration-example
- key_count: 2
  name: Amazon Codecatalyst Ide Example
  slug: amazon-codecatalyst-ide-example
- key_count: 2
  name: Amazon Codecatalyst List Access Tokens Request Example
  slug: amazon-codecatalyst-list-access-tokens-request-example
- key_count: 2
  name: Amazon Codecatalyst List Access Tokens Response Example
  slug: amazon-codecatalyst-list-access-tokens-response-example
- key_count: 2
  name: Amazon Codecatalyst List Dev Environment Sessions Request Example
  slug: amazon-codecatalyst-list-dev-environment-sessions-request-example
- key_count: 2
  name: Amazon Codecatalyst List Dev Environment Sessions Response Example
  slug: amazon-codecatalyst-list-dev-environment-sessions-response-example
- key_count: 3
  name: Amazon Codecatalyst List Dev Environments Request Example
  slug: amazon-codecatalyst-list-dev-environments-request-example
- key_count: 2
  name: Amazon Codecatalyst List Dev Environments Response Example
  slug: amazon-codecatalyst-list-dev-environments-response-example
- key_count: 5
  name: Amazon Codecatalyst List Event Logs Request Example
  slug: amazon-codecatalyst-list-event-logs-request-example
- key_count: 2
  name: Amazon Codecatalyst List Event Logs Response Example
  slug: amazon-codecatalyst-list-event-logs-response-example
- key_count: 3
  name: Amazon Codecatalyst List Projects Request Example
  slug: amazon-codecatalyst-list-projects-request-example
- key_count: 2
  name: Amazon Codecatalyst List Projects Response Example
  slug: amazon-codecatalyst-list-projects-response-example
- key_count: 5
  name: Amazon Codecatalyst List Source Repositories Item Example
  slug: amazon-codecatalyst-list-source-repositories-item-example
- key_count: 2
  name: Amazon Codecatalyst List Source Repositories Request Example
  slug: amazon-codecatalyst-list-source-repositories-request-example
- key_count: 2
  name: Amazon Codecatalyst List Source Repositories Response Example
  slug: amazon-codecatalyst-list-source-repositories-response-example
- key_count: 4
  name: Amazon Codecatalyst List Source Repository Branches Item Example
  slug: amazon-codecatalyst-list-source-repository-branches-item-example
- key_count: 2
  name: Amazon Codecatalyst List Source Repository Branches Request Example
  slug: amazon-codecatalyst-list-source-repository-branches-request-example
- key_count: 2
  name: Amazon Codecatalyst List Source Repository Branches Response Example
  slug: amazon-codecatalyst-list-source-repository-branches-response-example
- key_count: 1
  name: Amazon Codecatalyst List Spaces Request Example
  slug: amazon-codecatalyst-list-spaces-request-example
- key_count: 2
  name: Amazon Codecatalyst List Spaces Response Example
  slug: amazon-codecatalyst-list-spaces-response-example
- key_count: 1
  name: Amazon Codecatalyst Persistent Storage Configuration Example
  slug: amazon-codecatalyst-persistent-storage-configuration-example
- key_count: 1
  name: Amazon Codecatalyst Persistent Storage Example
  slug: amazon-codecatalyst-persistent-storage-example
- key_count: 2
  name: Amazon Codecatalyst Project Information Example
  slug: amazon-codecatalyst-project-information-example
- key_count: 3
  name: Amazon Codecatalyst Project List Filter Example
  slug: amazon-codecatalyst-project-list-filter-example
- key_count: 3
  name: Amazon Codecatalyst Project Summary Example
  slug: amazon-codecatalyst-project-summary-example
- key_count: 2
  name: Amazon Codecatalyst Repository Input Example
  slug: amazon-codecatalyst-repository-input-example
- key_count: 4
  name: Amazon Codecatalyst Space Summary Example
  slug: amazon-codecatalyst-space-summary-example
- key_count: 3
  name: Amazon Codecatalyst Start Dev Environment Request Example
  slug: amazon-codecatalyst-start-dev-environment-request-example
- key_count: 4
  name: Amazon Codecatalyst Start Dev Environment Response Example
  slug: amazon-codecatalyst-start-dev-environment-response-example
- key_count: 1
  name: Amazon Codecatalyst Start Dev Environment Session Request Example
  slug: amazon-codecatalyst-start-dev-environment-session-request-example
- key_count: 5
  name: Amazon Codecatalyst Start Dev Environment Session Response Example
  slug: amazon-codecatalyst-start-dev-environment-session-response-example
- key_count: 0
  name: Amazon Codecatalyst Stop Dev Environment Request Example
  slug: amazon-codecatalyst-stop-dev-environment-request-example
- key_count: 4
  name: Amazon Codecatalyst Stop Dev Environment Response Example
  slug: amazon-codecatalyst-stop-dev-environment-response-example
- key_count: 0
  name: Amazon Codecatalyst Stop Dev Environment Session Request Example
  slug: amazon-codecatalyst-stop-dev-environment-session-request-example
- key_count: 4
  name: Amazon Codecatalyst Stop Dev Environment Session Response Example
  slug: amazon-codecatalyst-stop-dev-environment-session-response-example
- key_count: 5
  name: Amazon Codecatalyst Update Dev Environment Request Example
  slug: amazon-codecatalyst-update-dev-environment-request-example
- key_count: 8
  name: Amazon Codecatalyst Update Dev Environment Response Example
  slug: amazon-codecatalyst-update-dev-environment-response-example
- key_count: 1
  name: Amazon Codecatalyst Update Project Request Example
  slug: amazon-codecatalyst-update-project-request-example
- key_count: 4
  name: Amazon Codecatalyst Update Project Response Example
  slug: amazon-codecatalyst-update-project-response-example
- key_count: 1
  name: Amazon Codecatalyst Update Space Request Example
  slug: amazon-codecatalyst-update-space-request-example
- key_count: 3
  name: Amazon Codecatalyst Update Space Response Example
  slug: amazon-codecatalyst-update-space-response-example
- key_count: 4
  name: Amazon Codecatalyst User Identity Example
  slug: amazon-codecatalyst-user-identity-example
- key_count: 1
  name: Amazon Codecatalyst Verify Session Response Example
  slug: amazon-codecatalyst-verify-session-response-example
features:
- description: Cloud-based development environments pre-configured with your project code and tools enabling instant onboarding and eliminating local setup friction.
  name: Dev Environments
- description: Built-in Git repositories for hosting and managing source code with branching, pull requests, and code review capabilities.
  name: Source Repositories
- description: Visual workflow builder for creating automated build, test, and deployment pipelines with native AWS service integrations.
  name: CI/CD Workflows
- description: Integrated issue tracking and project boards for organizing work, tracking bugs, and managing feature development alongside code.
  name: Project Management
- description: Organizational units for grouping projects and managing team membership, billing, and resource access across an organization.
  name: Spaces
- description: Connect to GitHub repositories, Jira, Slack, and other third-party tools to incorporate CodeCatalyst into existing development workflows.
  name: Third-Party Integrations
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-codecatalyst.png
integrations:
- description: Connect GitHub repositories to CodeCatalyst projects and sync code.
  name: GitHub
- description: Link CodeCatalyst issues with Jira for unified project tracking.
  name: Jira
- description: Receive CodeCatalyst notifications and workflow status updates in Slack.
  name: Slack
- description: AI coding assistance integrated into Dev Environments and code reviews.
  name: Amazon Q Developer
- description: Deploy serverless functions as part of CodeCatalyst CI/CD workflows.
  name: AWS Lambda
- description: Deploy containerized applications to ECS from CodeCatalyst pipelines.
  name: Amazon ECS
- description: Deploy infrastructure as code using CloudFormation actions in workflows.
  name: AWS CloudFormation
json_schemas:
- name: AccessTokenId
  property_count: 0
  slug: amazon-codecatalyst-access-token-id
- name: AccessTokenName
  property_count: 0
  slug: amazon-codecatalyst-access-token-name
- name: AccessTokenSecret
  property_count: 0
  slug: amazon-codecatalyst-access-token-secret
- name: AccessTokenSummaries
  property_count: 0
  slug: amazon-codecatalyst-access-token-summaries
- name: AccessTokenSummary
  property_count: 3
  slug: amazon-codecatalyst-access-token-summary
- name: Boolean
  property_count: 0
  slug: amazon-codecatalyst-boolean
- name: ClientToken
  property_count: 0
  slug: amazon-codecatalyst-client-token
- name: ComparisonOperator
  property_count: 0
  slug: amazon-codecatalyst-comparison-operator
- name: CreateAccessTokenRequest
  property_count: 2
  slug: amazon-codecatalyst-create-access-token-request
- name: CreateAccessTokenResponse
  property_count: 4
  slug: amazon-codecatalyst-create-access-token-response
- name: CreateDevEnvironmentRequestAliasString
  property_count: 0
  slug: amazon-codecatalyst-create-dev-environment-request-alias-string
- name: CreateDevEnvironmentRequest
  property_count: 7
  slug: amazon-codecatalyst-create-dev-environment-request
- name: CreateDevEnvironmentResponse
  property_count: 3
  slug: amazon-codecatalyst-create-dev-environment-response
- name: CreateProjectRequest
  property_count: 2
  slug: amazon-codecatalyst-create-project-request
- name: CreateProjectResponse
  property_count: 4
  slug: amazon-codecatalyst-create-project-response
- name: CreateSourceRepositoryBranchRequest
  property_count: 1
  slug: amazon-codecatalyst-create-source-repository-branch-request
- name: CreateSourceRepositoryBranchResponse
  property_count: 4
  slug: amazon-codecatalyst-create-source-repository-branch-response
- name: CreateSourceRepositoryRequest
  property_count: 1
  slug: amazon-codecatalyst-create-source-repository-request
- name: CreateSourceRepositoryResponse
  property_count: 4
  slug: amazon-codecatalyst-create-source-repository-response
- name: DeleteAccessTokenRequest
  property_count: 0
  slug: amazon-codecatalyst-delete-access-token-request
- name: DeleteAccessTokenResponse
  property_count: 0
  slug: amazon-codecatalyst-delete-access-token-response
- name: DeleteDevEnvironmentRequest
  property_count: 0
  slug: amazon-codecatalyst-delete-dev-environment-request
- name: DeleteDevEnvironmentResponse
  property_count: 3
  slug: amazon-codecatalyst-delete-dev-environment-response
- name: DeleteProjectRequest
  property_count: 0
  slug: amazon-codecatalyst-delete-project-request
- name: DeleteProjectResponse
  property_count: 3
  slug: amazon-codecatalyst-delete-project-response
- name: DeleteSourceRepositoryRequest
  property_count: 0
  slug: amazon-codecatalyst-delete-source-repository-request
- name: DeleteSourceRepositoryResponse
  property_count: 3
  slug: amazon-codecatalyst-delete-source-repository-response
- name: DeleteSpaceRequest
  property_count: 0
  slug: amazon-codecatalyst-delete-space-request
- name: DeleteSpaceResponse
  property_count: 2
  slug: amazon-codecatalyst-delete-space-response
- name: DevEnvironmentAccessDetails
  property_count: 2
  slug: amazon-codecatalyst-dev-environment-access-details
- name: DevEnvironmentRepositorySummaries
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-repository-summaries
- name: DevEnvironmentRepositorySummary
  property_count: 2
  slug: amazon-codecatalyst-dev-environment-repository-summary
- name: DevEnvironmentSessionConfiguration
  property_count: 2
  slug: amazon-codecatalyst-dev-environment-session-configuration
- name: DevEnvironmentSessionSummaryIdString
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-session-summary-id-string
- name: DevEnvironmentSessionSummary
  property_count: 5
  slug: amazon-codecatalyst-dev-environment-session-summary
- name: DevEnvironmentSessionType
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-session-type
- name: DevEnvironmentSessionsSummaryList
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-sessions-summary-list
- name: DevEnvironmentStatus
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-status
- name: DevEnvironmentSummaryAliasString
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-summary-alias-string
- name: DevEnvironmentSummaryCreatorIdString
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-summary-creator-id-string
- name: DevEnvironmentSummaryList
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-summary-list
- name: DevEnvironmentSummary
  property_count: 13
  slug: amazon-codecatalyst-dev-environment-summary
- name: EmailAddress
  property_count: 2
  slug: amazon-codecatalyst-email-address
- name: EventLogEntries
  property_count: 0
  slug: amazon-codecatalyst-event-log-entries
- name: EventLogEntry
  property_count: 15
  slug: amazon-codecatalyst-event-log-entry
- name: EventPayload
  property_count: 2
  slug: amazon-codecatalyst-event-payload
- name: ExecuteCommandSessionConfigurationArgumentsMemberString
  property_count: 0
  slug: amazon-codecatalyst-execute-command-session-configuration-arguments-member-string
- name: ExecuteCommandSessionConfigurationArguments
  property_count: 0
  slug: amazon-codecatalyst-execute-command-session-configuration-arguments
- name: ExecuteCommandSessionConfigurationCommandString
  property_count: 0
  slug: amazon-codecatalyst-execute-command-session-configuration-command-string
- name: ExecuteCommandSessionConfiguration
  property_count: 2
  slug: amazon-codecatalyst-execute-command-session-configuration
- name: FilterKey
  property_count: 0
  slug: amazon-codecatalyst-filter-key
- name: Filter
  property_count: 3
  slug: amazon-codecatalyst-filter
- name: Filters
  property_count: 0
  slug: amazon-codecatalyst-filters
- name: GetDevEnvironmentRequest
  property_count: 0
  slug: amazon-codecatalyst-get-dev-environment-request
- name: GetDevEnvironmentResponseAliasString
  property_count: 0
  slug: amazon-codecatalyst-get-dev-environment-response-alias-string
- name: GetDevEnvironmentResponseCreatorIdString
  property_count: 0
  slug: amazon-codecatalyst-get-dev-environment-response-creator-id-string
- name: GetDevEnvironmentResponse
  property_count: 13
  slug: amazon-codecatalyst-get-dev-environment-response
- name: GetProjectRequest
  property_count: 0
  slug: amazon-codecatalyst-get-project-request
- name: GetProjectResponse
  property_count: 4
  slug: amazon-codecatalyst-get-project-response
- name: GetSourceRepositoryCloneUrlsRequest
  property_count: 0
  slug: amazon-codecatalyst-get-source-repository-clone-urls-request
- name: GetSourceRepositoryCloneUrlsResponse
  property_count: 1
  slug: amazon-codecatalyst-get-source-repository-clone-urls-response
- name: GetSourceRepositoryRequest
  property_count: 0
  slug: amazon-codecatalyst-get-source-repository-request
- name: GetSourceRepositoryResponse
  property_count: 6
  slug: amazon-codecatalyst-get-source-repository-response
- name: GetSpaceRequest
  property_count: 0
  slug: amazon-codecatalyst-get-space-request
- name: GetSpaceResponse
  property_count: 4
  slug: amazon-codecatalyst-get-space-response
- name: GetSubscriptionRequest
  property_count: 0
  slug: amazon-codecatalyst-get-subscription-request
- name: GetSubscriptionResponse
  property_count: 2
  slug: amazon-codecatalyst-get-subscription-response
- name: GetUserDetailsRequestIdString
  property_count: 0
  slug: amazon-codecatalyst-get-user-details-request-id-string
- name: GetUserDetailsRequest
  property_count: 0
  slug: amazon-codecatalyst-get-user-details-request
- name: GetUserDetailsRequestUserNameString
  property_count: 0
  slug: amazon-codecatalyst-get-user-details-request-user-name-string
- name: GetUserDetailsResponse
  property_count: 5
  slug: amazon-codecatalyst-get-user-details-response
- name: IdeConfigurationList
  property_count: 0
  slug: amazon-codecatalyst-ide-configuration-list
- name: IdeConfigurationNameString
  property_count: 0
  slug: amazon-codecatalyst-ide-configuration-name-string
- name: IdeConfigurationRuntimeString
  property_count: 0
  slug: amazon-codecatalyst-ide-configuration-runtime-string
- name: IdeConfiguration
  property_count: 2
  slug: amazon-codecatalyst-ide-configuration
- name: IdeNameString
  property_count: 0
  slug: amazon-codecatalyst-ide-name-string
- name: IdeRuntimeString
  property_count: 0
  slug: amazon-codecatalyst-ide-runtime-string
- name: Ide
  property_count: 2
  slug: amazon-codecatalyst-ide
- name: Ides
  property_count: 0
  slug: amazon-codecatalyst-ides
- name: InactivityTimeoutMinutes
  property_count: 0
  slug: amazon-codecatalyst-inactivity-timeout-minutes
- name: InstanceType
  property_count: 0
  slug: amazon-codecatalyst-instance-type
- name: ListAccessTokensRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codecatalyst-list-access-tokens-request-max-results-integer
- name: ListAccessTokensRequestNextTokenString
  property_count: 0
  slug: amazon-codecatalyst-list-access-tokens-request-next-token-string
- name: ListAccessTokensRequest
  property_count: 2
  slug: amazon-codecatalyst-list-access-tokens-request
- name: ListAccessTokensResponse
  property_count: 2
  slug: amazon-codecatalyst-list-access-tokens-response
- name: ListDevEnvironmentSessionsRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codecatalyst-list-dev-environment-sessions-request-max-results-integer
- name: ListDevEnvironmentSessionsRequestNextTokenString
  property_count: 0
  slug: amazon-codecatalyst-list-dev-environment-sessions-request-next-token-string
- name: ListDevEnvironmentSessionsRequest
  property_count: 2
  slug: amazon-codecatalyst-list-dev-environment-sessions-request
- name: ListDevEnvironmentSessionsResponse
  property_count: 2
  slug: amazon-codecatalyst-list-dev-environment-sessions-response
- name: ListDevEnvironmentsRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codecatalyst-list-dev-environments-request-max-results-integer
- name: ListDevEnvironmentsRequestNextTokenString
  property_count: 0
  slug: amazon-codecatalyst-list-dev-environments-request-next-token-string
- name: ListDevEnvironmentsRequest
  property_count: 3
  slug: amazon-codecatalyst-list-dev-environments-request
- name: ListDevEnvironmentsResponse
  property_count: 2
  slug: amazon-codecatalyst-list-dev-environments-response
- name: ListEventLogsRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codecatalyst-list-event-logs-request-max-results-integer
- name: ListEventLogsRequestNextTokenString
  property_count: 0
  slug: amazon-codecatalyst-list-event-logs-request-next-token-string
- name: ListEventLogsRequest
  property_count: 5
  slug: amazon-codecatalyst-list-event-logs-request
- name: ListEventLogsResponse
  property_count: 2
  slug: amazon-codecatalyst-list-event-logs-response
- name: ListProjectsRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codecatalyst-list-projects-request-max-results-integer
- name: ListProjectsRequestNextTokenString
  property_count: 0
  slug: amazon-codecatalyst-list-projects-request-next-token-string
- name: ListProjectsRequest
  property_count: 3
  slug: amazon-codecatalyst-list-projects-request
- name: ListProjectsResponse
  property_count: 2
  slug: amazon-codecatalyst-list-projects-response
- name: ListSourceRepositoriesItem
  property_count: 5
  slug: amazon-codecatalyst-list-source-repositories-item
- name: ListSourceRepositoriesItems
  property_count: 0
  slug: amazon-codecatalyst-list-source-repositories-items
- name: ListSourceRepositoriesRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codecatalyst-list-source-repositories-request-max-results-integer
- name: ListSourceRepositoriesRequestNextTokenString
  property_count: 0
  slug: amazon-codecatalyst-list-source-repositories-request-next-token-string
- name: ListSourceRepositoriesRequest
  property_count: 2
  slug: amazon-codecatalyst-list-source-repositories-request
- name: ListSourceRepositoriesResponse
  property_count: 2
  slug: amazon-codecatalyst-list-source-repositories-response
- name: ListSourceRepositoryBranchesItem
  property_count: 4
  slug: amazon-codecatalyst-list-source-repository-branches-item
- name: ListSourceRepositoryBranchesItems
  property_count: 0
  slug: amazon-codecatalyst-list-source-repository-branches-items
- name: ListSourceRepositoryBranchesRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codecatalyst-list-source-repository-branches-request-max-results-integer
- name: ListSourceRepositoryBranchesRequestNextTokenString
  property_count: 0
  slug: amazon-codecatalyst-list-source-repository-branches-request-next-token-string
- name: ListSourceRepositoryBranchesRequest
  property_count: 2
  slug: amazon-codecatalyst-list-source-repository-branches-request
- name: ListSourceRepositoryBranchesResponse
  property_count: 2
  slug: amazon-codecatalyst-list-source-repository-branches-response
- name: ListSpacesRequestNextTokenString
  property_count: 0
  slug: amazon-codecatalyst-list-spaces-request-next-token-string
- name: ListSpacesRequest
  property_count: 1
  slug: amazon-codecatalyst-list-spaces-request
- name: ListSpacesResponse
  property_count: 2
  slug: amazon-codecatalyst-list-spaces-response
- name: NameString
  property_count: 0
  slug: amazon-codecatalyst-name-string
- name: OperationType
  property_count: 0
  slug: amazon-codecatalyst-operation-type
- name: PersistentStorageConfiguration
  property_count: 1
  slug: amazon-codecatalyst-persistent-storage-configuration
- name: PersistentStorageConfigurationSizeInGiBInteger
  property_count: 0
  slug: amazon-codecatalyst-persistent-storage-configuration-size-in-gi-b-integer
- name: PersistentStorage
  property_count: 1
  slug: amazon-codecatalyst-persistent-storage
- name: PersistentStorageSizeInGiBInteger
  property_count: 0
  slug: amazon-codecatalyst-persistent-storage-size-in-gi-b-integer
- name: ProjectDescription
  property_count: 0
  slug: amazon-codecatalyst-project-description
- name: ProjectDisplayName
  property_count: 0
  slug: amazon-codecatalyst-project-display-name
- name: ProjectInformation
  property_count: 2
  slug: amazon-codecatalyst-project-information
- name: ProjectListFilter
  property_count: 3
  slug: amazon-codecatalyst-project-list-filter
- name: ProjectListFilters
  property_count: 0
  slug: amazon-codecatalyst-project-list-filters
- name: ProjectSummaries
  property_count: 0
  slug: amazon-codecatalyst-project-summaries
- name: ProjectSummary
  property_count: 3
  slug: amazon-codecatalyst-project-summary
- name: RegionString
  property_count: 0
  slug: amazon-codecatalyst-region-string
- name: RepositoriesInput
  property_count: 0
  slug: amazon-codecatalyst-repositories-input
- name: RepositoryInput
  property_count: 2
  slug: amazon-codecatalyst-repository-input
- name: SensitiveString
  property_count: 0
  slug: amazon-codecatalyst-sensitive-string
- name: SourceRepositoryBranchRefString
  property_count: 0
  slug: amazon-codecatalyst-source-repository-branch-ref-string
- name: SourceRepositoryBranchString
  property_count: 0
  slug: amazon-codecatalyst-source-repository-branch-string
- name: SourceRepositoryDescriptionString
  property_count: 0
  slug: amazon-codecatalyst-source-repository-description-string
- name: SourceRepositoryIdString
  property_count: 0
  slug: amazon-codecatalyst-source-repository-id-string
- name: SourceRepositoryNameString
  property_count: 0
  slug: amazon-codecatalyst-source-repository-name-string
- name: SpaceDescription
  property_count: 0
  slug: amazon-codecatalyst-space-description
- name: SpaceSummaries
  property_count: 0
  slug: amazon-codecatalyst-space-summaries
- name: SpaceSummary
  property_count: 4
  slug: amazon-codecatalyst-space-summary
- name: StartDevEnvironmentRequest
  property_count: 3
  slug: amazon-codecatalyst-start-dev-environment-request
- name: StartDevEnvironmentResponse
  property_count: 4
  slug: amazon-codecatalyst-start-dev-environment-response
- name: StartDevEnvironmentSessionRequest
  property_count: 1
  slug: amazon-codecatalyst-start-dev-environment-session-request
- name: StartDevEnvironmentSessionResponse
  property_count: 5
  slug: amazon-codecatalyst-start-dev-environment-session-response
- name: StartDevEnvironmentSessionResponseSessionIdString
  property_count: 0
  slug: amazon-codecatalyst-start-dev-environment-session-response-session-id-string
- name: StatusReason
  property_count: 0
  slug: amazon-codecatalyst-status-reason
- name: StopDevEnvironmentRequest
  property_count: 0
  slug: amazon-codecatalyst-stop-dev-environment-request
- name: StopDevEnvironmentResponse
  property_count: 4
  slug: amazon-codecatalyst-stop-dev-environment-response
- name: StopDevEnvironmentSessionRequest
  property_count: 0
  slug: amazon-codecatalyst-stop-dev-environment-session-request
- name: StopDevEnvironmentSessionRequestSessionIdString
  property_count: 0
  slug: amazon-codecatalyst-stop-dev-environment-session-request-session-id-string
- name: StopDevEnvironmentSessionResponse
  property_count: 4
  slug: amazon-codecatalyst-stop-dev-environment-session-response
- name: StopDevEnvironmentSessionResponseSessionIdString
  property_count: 0
  slug: amazon-codecatalyst-stop-dev-environment-session-response-session-id-string
- name: StringList
  property_count: 0
  slug: amazon-codecatalyst-string-list
- name: String
  property_count: 0
  slug: amazon-codecatalyst-string
- name: SyntheticTimestamp_date_time
  property_count: 0
  slug: amazon-codecatalyst-synthetic-timestamp_date_time
- name: Timestamp
  property_count: 0
  slug: amazon-codecatalyst-timestamp
- name: UpdateDevEnvironmentRequestAliasString
  property_count: 0
  slug: amazon-codecatalyst-update-dev-environment-request-alias-string
- name: UpdateDevEnvironmentRequest
  property_count: 5
  slug: amazon-codecatalyst-update-dev-environment-request
- name: UpdateDevEnvironmentResponseAliasString
  property_count: 0
  slug: amazon-codecatalyst-update-dev-environment-response-alias-string
- name: UpdateDevEnvironmentResponse
  property_count: 8
  slug: amazon-codecatalyst-update-dev-environment-response
- name: UpdateProjectRequest
  property_count: 1
  slug: amazon-codecatalyst-update-project-request
- name: UpdateProjectResponse
  property_count: 4
  slug: amazon-codecatalyst-update-project-response
- name: UpdateSpaceRequest
  property_count: 1
  slug: amazon-codecatalyst-update-space-request
- name: UpdateSpaceResponse
  property_count: 3
  slug: amazon-codecatalyst-update-space-response
- name: UserIdentity
  property_count: 4
  slug: amazon-codecatalyst-user-identity
- name: UserType
  property_count: 0
  slug: amazon-codecatalyst-user-type
- name: Uuid
  property_count: 0
  slug: amazon-codecatalyst-uuid
- name: VerifySessionResponseIdentityString
  property_count: 0
  slug: amazon-codecatalyst-verify-session-response-identity-string
- name: VerifySessionResponse
  property_count: 1
  slug: amazon-codecatalyst-verify-session-response
json_structures:
- name: Amazon Codecatalyst Access Token Id Structure
  property_count: 0
  slug: amazon-codecatalyst-access-token-id-structure
- name: Amazon Codecatalyst Access Token Name Structure
  property_count: 0
  slug: amazon-codecatalyst-access-token-name-structure
- name: Amazon Codecatalyst Access Token Secret Structure
  property_count: 0
  slug: amazon-codecatalyst-access-token-secret-structure
- name: Amazon Codecatalyst Access Token Summaries Structure
  property_count: 0
  slug: amazon-codecatalyst-access-token-summaries-structure
- name: Amazon Codecatalyst Access Token Summary Structure
  property_count: 3
  slug: amazon-codecatalyst-access-token-summary-structure
- name: Amazon Codecatalyst Boolean Structure
  property_count: 0
  slug: amazon-codecatalyst-boolean-structure
- name: Amazon Codecatalyst Client Token Structure
  property_count: 0
  slug: amazon-codecatalyst-client-token-structure
- name: Amazon Codecatalyst Comparison Operator Structure
  property_count: 0
  slug: amazon-codecatalyst-comparison-operator-structure
- name: Amazon Codecatalyst Create Access Token Request Structure
  property_count: 2
  slug: amazon-codecatalyst-create-access-token-request-structure
- name: Amazon Codecatalyst Create Access Token Response Structure
  property_count: 4
  slug: amazon-codecatalyst-create-access-token-response-structure
- name: Amazon Codecatalyst Create Dev Environment Request Alias String Structure
  property_count: 0
  slug: amazon-codecatalyst-create-dev-environment-request-alias-string-structure
- name: Amazon Codecatalyst Create Dev Environment Request Structure
  property_count: 7
  slug: amazon-codecatalyst-create-dev-environment-request-structure
- name: Amazon Codecatalyst Create Dev Environment Response Structure
  property_count: 3
  slug: amazon-codecatalyst-create-dev-environment-response-structure
- name: Amazon Codecatalyst Create Project Request Structure
  property_count: 2
  slug: amazon-codecatalyst-create-project-request-structure
- name: Amazon Codecatalyst Create Project Response Structure
  property_count: 4
  slug: amazon-codecatalyst-create-project-response-structure
- name: Amazon Codecatalyst Create Source Repository Branch Request Structure
  property_count: 1
  slug: amazon-codecatalyst-create-source-repository-branch-request-structure
- name: Amazon Codecatalyst Create Source Repository Branch Response Structure
  property_count: 4
  slug: amazon-codecatalyst-create-source-repository-branch-response-structure
- name: Amazon Codecatalyst Create Source Repository Request Structure
  property_count: 1
  slug: amazon-codecatalyst-create-source-repository-request-structure
- name: Amazon Codecatalyst Create Source Repository Response Structure
  property_count: 4
  slug: amazon-codecatalyst-create-source-repository-response-structure
- name: Amazon Codecatalyst Delete Access Token Request Structure
  property_count: 0
  slug: amazon-codecatalyst-delete-access-token-request-structure
- name: Amazon Codecatalyst Delete Access Token Response Structure
  property_count: 0
  slug: amazon-codecatalyst-delete-access-token-response-structure
- name: Amazon Codecatalyst Delete Dev Environment Request Structure
  property_count: 0
  slug: amazon-codecatalyst-delete-dev-environment-request-structure
- name: Amazon Codecatalyst Delete Dev Environment Response Structure
  property_count: 3
  slug: amazon-codecatalyst-delete-dev-environment-response-structure
- name: Amazon Codecatalyst Delete Project Request Structure
  property_count: 0
  slug: amazon-codecatalyst-delete-project-request-structure
- name: Amazon Codecatalyst Delete Project Response Structure
  property_count: 3
  slug: amazon-codecatalyst-delete-project-response-structure
- name: Amazon Codecatalyst Delete Source Repository Request Structure
  property_count: 0
  slug: amazon-codecatalyst-delete-source-repository-request-structure
- name: Amazon Codecatalyst Delete Source Repository Response Structure
  property_count: 3
  slug: amazon-codecatalyst-delete-source-repository-response-structure
- name: Amazon Codecatalyst Delete Space Request Structure
  property_count: 0
  slug: amazon-codecatalyst-delete-space-request-structure
- name: Amazon Codecatalyst Delete Space Response Structure
  property_count: 2
  slug: amazon-codecatalyst-delete-space-response-structure
- name: Amazon Codecatalyst Dev Environment Access Details Structure
  property_count: 2
  slug: amazon-codecatalyst-dev-environment-access-details-structure
- name: Amazon Codecatalyst Dev Environment Repository Summaries Structure
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-repository-summaries-structure
- name: Amazon Codecatalyst Dev Environment Repository Summary Structure
  property_count: 2
  slug: amazon-codecatalyst-dev-environment-repository-summary-structure
- name: Amazon Codecatalyst Dev Environment Session Configuration Structure
  property_count: 2
  slug: amazon-codecatalyst-dev-environment-session-configuration-structure
- name: Amazon Codecatalyst Dev Environment Session Summary Id String Structure
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-session-summary-id-string-structure
- name: Amazon Codecatalyst Dev Environment Session Summary Structure
  property_count: 5
  slug: amazon-codecatalyst-dev-environment-session-summary-structure
- name: Amazon Codecatalyst Dev Environment Session Type Structure
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-session-type-structure
- name: Amazon Codecatalyst Dev Environment Sessions Summary List Structure
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-sessions-summary-list-structure
- name: Amazon Codecatalyst Dev Environment Status Structure
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-status-structure
- name: Amazon Codecatalyst Dev Environment Summary Alias String Structure
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-summary-alias-string-structure
- name: Amazon Codecatalyst Dev Environment Summary Creator Id String Structure
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-summary-creator-id-string-structure
- name: Amazon Codecatalyst Dev Environment Summary List Structure
  property_count: 0
  slug: amazon-codecatalyst-dev-environment-summary-list-structure
- name: Amazon Codecatalyst Dev Environment Summary Structure
  property_count: 13
  slug: amazon-codecatalyst-dev-environment-summary-structure
- name: Amazon Codecatalyst Email Address Structure
  property_count: 2
  slug: amazon-codecatalyst-email-address-structure
- name: Amazon Codecatalyst Event Log Entries Structure
  property_count: 0
  slug: amazon-codecatalyst-event-log-entries-structure
- name: Amazon Codecatalyst Event Log Entry Structure
  property_count: 15
  slug: amazon-codecatalyst-event-log-entry-structure
- name: Amazon Codecatalyst Event Payload Structure
  property_count: 2
  slug: amazon-codecatalyst-event-payload-structure
- name: Amazon Codecatalyst Execute Command Session Configuration Arguments Member String Structure
  property_count: 0
  slug: amazon-codecatalyst-execute-command-session-configuration-arguments-member-string-structure
- name: Amazon Codecatalyst Execute Command Session Configuration Arguments Structure
  property_count: 0
  slug: amazon-codecatalyst-execute-command-session-configuration-arguments-structure
- name: Amazon Codecatalyst Execute Command Session Configuration Command String Structure
  property_count: 0
  slug: amazon-codecatalyst-execute-command-session-configuration-command-string-structure
- name: Amazon Codecatalyst Execute Command Session Configuration Structure
  property_count: 2
  slug: amazon-codecatalyst-execute-command-session-configuration-structure
- name: Amazon Codecatalyst Filter Key Structure
  property_count: 0
  slug: amazon-codecatalyst-filter-key-structure
- name: Amazon Codecatalyst Filter Structure
  property_count: 3
  slug: amazon-codecatalyst-filter-structure
- name: Amazon Codecatalyst Filters Structure
  property_count: 0
  slug: amazon-codecatalyst-filters-structure
- name: Amazon Codecatalyst Get Dev Environment Request Structure
  property_count: 0
  slug: amazon-codecatalyst-get-dev-environment-request-structure
- name: Amazon Codecatalyst Get Dev Environment Response Alias String Structure
  property_count: 0
  slug: amazon-codecatalyst-get-dev-environment-response-alias-string-structure
- name: Amazon Codecatalyst Get Dev Environment Response Creator Id String Structure
  property_count: 0
  slug: amazon-codecatalyst-get-dev-environment-response-creator-id-string-structure
- name: Amazon Codecatalyst Get Dev Environment Response Structure
  property_count: 13
  slug: amazon-codecatalyst-get-dev-environment-response-structure
- name: Amazon Codecatalyst Get Project Request Structure
  property_count: 0
  slug: amazon-codecatalyst-get-project-request-structure
- name: Amazon Codecatalyst Get Project Response Structure
  property_count: 4
  slug: amazon-codecatalyst-get-project-response-structure
- name: Amazon Codecatalyst Get Source Repository Clone Urls Request Structure
  property_count: 0
  slug: amazon-codecatalyst-get-source-repository-clone-urls-request-structure
- name: Amazon Codecatalyst Get Source Repository Clone Urls Response Structure
  property_count: 1
  slug: amazon-codecatalyst-get-source-repository-clone-urls-response-structure
- name: Amazon Codecatalyst Get Source Repository Request Structure
  property_count: 0
  slug: amazon-codecatalyst-get-source-repository-request-structure
- name: Amazon Codecatalyst Get Source Repository Response Structure
  property_count: 6
  slug: amazon-codecatalyst-get-source-repository-response-structure
- name: Amazon Codecatalyst Get Space Request Structure
  property_count: 0
  slug: amazon-codecatalyst-get-space-request-structure
- name: Amazon Codecatalyst Get Space Response Structure
  property_count: 4
  slug: amazon-codecatalyst-get-space-response-structure
- name: Amazon Codecatalyst Get Subscription Request Structure
  property_count: 0
  slug: amazon-codecatalyst-get-subscription-request-structure
- name: Amazon Codecatalyst Get Subscription Response Structure
  property_count: 2
  slug: amazon-codecatalyst-get-subscription-response-structure
- name: Amazon Codecatalyst Get User Details Request Id String Structure
  property_count: 0
  slug: amazon-codecatalyst-get-user-details-request-id-string-structure
- name: Amazon Codecatalyst Get User Details Request Structure
  property_count: 0
  slug: amazon-codecatalyst-get-user-details-request-structure
- name: Amazon Codecatalyst Get User Details Request User Name String Structure
  property_count: 0
  slug: amazon-codecatalyst-get-user-details-request-user-name-string-structure
- name: Amazon Codecatalyst Get User Details Response Structure
  property_count: 5
  slug: amazon-codecatalyst-get-user-details-response-structure
- name: Amazon Codecatalyst Ide Configuration List Structure
  property_count: 0
  slug: amazon-codecatalyst-ide-configuration-list-structure
- name: Amazon Codecatalyst Ide Configuration Name String Structure
  property_count: 0
  slug: amazon-codecatalyst-ide-configuration-name-string-structure
- name: Amazon Codecatalyst Ide Configuration Runtime String Structure
  property_count: 0
  slug: amazon-codecatalyst-ide-configuration-runtime-string-structure
- name: Amazon Codecatalyst Ide Configuration Structure
  property_count: 2
  slug: amazon-codecatalyst-ide-configuration-structure
- name: Amazon Codecatalyst Ide Name String Structure
  property_count: 0
  slug: amazon-codecatalyst-ide-name-string-structure
- name: Amazon Codecatalyst Ide Runtime String Structure
  property_count: 0
  slug: amazon-codecatalyst-ide-runtime-string-structure
- name: Amazon Codecatalyst Ide Structure
  property_count: 2
  slug: amazon-codecatalyst-ide-structure
- name: Amazon Codecatalyst Ides Structure
  property_count: 0
  slug: amazon-codecatalyst-ides-structure
- name: Amazon Codecatalyst Inactivity Timeout Minutes Structure
  property_count: 0
  slug: amazon-codecatalyst-inactivity-timeout-minutes-structure
- name: Amazon Codecatalyst Instance Type Structure
  property_count: 0
  slug: amazon-codecatalyst-instance-type-structure
- name: Amazon Codecatalyst List Access Tokens Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-list-access-tokens-request-max-results-integer-structure
- name: Amazon Codecatalyst List Access Tokens Request Next Token String Structure
  property_count: 0
  slug: amazon-codecatalyst-list-access-tokens-request-next-token-string-structure
- name: Amazon Codecatalyst List Access Tokens Request Structure
  property_count: 2
  slug: amazon-codecatalyst-list-access-tokens-request-structure
- name: Amazon Codecatalyst List Access Tokens Response Structure
  property_count: 2
  slug: amazon-codecatalyst-list-access-tokens-response-structure
- name: Amazon Codecatalyst List Dev Environment Sessions Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-list-dev-environment-sessions-request-max-results-integer-structure
- name: Amazon Codecatalyst List Dev Environment Sessions Request Next Token String Structure
  property_count: 0
  slug: amazon-codecatalyst-list-dev-environment-sessions-request-next-token-string-structure
- name: Amazon Codecatalyst List Dev Environment Sessions Request Structure
  property_count: 2
  slug: amazon-codecatalyst-list-dev-environment-sessions-request-structure
- name: Amazon Codecatalyst List Dev Environment Sessions Response Structure
  property_count: 2
  slug: amazon-codecatalyst-list-dev-environment-sessions-response-structure
- name: Amazon Codecatalyst List Dev Environments Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-list-dev-environments-request-max-results-integer-structure
- name: Amazon Codecatalyst List Dev Environments Request Next Token String Structure
  property_count: 0
  slug: amazon-codecatalyst-list-dev-environments-request-next-token-string-structure
- name: Amazon Codecatalyst List Dev Environments Request Structure
  property_count: 3
  slug: amazon-codecatalyst-list-dev-environments-request-structure
- name: Amazon Codecatalyst List Dev Environments Response Structure
  property_count: 2
  slug: amazon-codecatalyst-list-dev-environments-response-structure
- name: Amazon Codecatalyst List Event Logs Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-list-event-logs-request-max-results-integer-structure
- name: Amazon Codecatalyst List Event Logs Request Next Token String Structure
  property_count: 0
  slug: amazon-codecatalyst-list-event-logs-request-next-token-string-structure
- name: Amazon Codecatalyst List Event Logs Request Structure
  property_count: 5
  slug: amazon-codecatalyst-list-event-logs-request-structure
- name: Amazon Codecatalyst List Event Logs Response Structure
  property_count: 2
  slug: amazon-codecatalyst-list-event-logs-response-structure
- name: Amazon Codecatalyst List Projects Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-list-projects-request-max-results-integer-structure
- name: Amazon Codecatalyst List Projects Request Next Token String Structure
  property_count: 0
  slug: amazon-codecatalyst-list-projects-request-next-token-string-structure
- name: Amazon Codecatalyst List Projects Request Structure
  property_count: 3
  slug: amazon-codecatalyst-list-projects-request-structure
- name: Amazon Codecatalyst List Projects Response Structure
  property_count: 2
  slug: amazon-codecatalyst-list-projects-response-structure
- name: Amazon Codecatalyst List Source Repositories Item Structure
  property_count: 5
  slug: amazon-codecatalyst-list-source-repositories-item-structure
- name: Amazon Codecatalyst List Source Repositories Items Structure
  property_count: 0
  slug: amazon-codecatalyst-list-source-repositories-items-structure
- name: Amazon Codecatalyst List Source Repositories Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-list-source-repositories-request-max-results-integer-structure
- name: Amazon Codecatalyst List Source Repositories Request Next Token String Structure
  property_count: 0
  slug: amazon-codecatalyst-list-source-repositories-request-next-token-string-structure
- name: Amazon Codecatalyst List Source Repositories Request Structure
  property_count: 2
  slug: amazon-codecatalyst-list-source-repositories-request-structure
- name: Amazon Codecatalyst List Source Repositories Response Structure
  property_count: 2
  slug: amazon-codecatalyst-list-source-repositories-response-structure
- name: Amazon Codecatalyst List Source Repository Branches Item Structure
  property_count: 4
  slug: amazon-codecatalyst-list-source-repository-branches-item-structure
- name: Amazon Codecatalyst List Source Repository Branches Items Structure
  property_count: 0
  slug: amazon-codecatalyst-list-source-repository-branches-items-structure
- name: Amazon Codecatalyst List Source Repository Branches Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-list-source-repository-branches-request-max-results-integer-structure
- name: Amazon Codecatalyst List Source Repository Branches Request Next Token String Structure
  property_count: 0
  slug: amazon-codecatalyst-list-source-repository-branches-request-next-token-string-structure
- name: Amazon Codecatalyst List Source Repository Branches Request Structure
  property_count: 2
  slug: amazon-codecatalyst-list-source-repository-branches-request-structure
- name: Amazon Codecatalyst List Source Repository Branches Response Structure
  property_count: 2
  slug: amazon-codecatalyst-list-source-repository-branches-response-structure
- name: Amazon Codecatalyst List Spaces Request Next Token String Structure
  property_count: 0
  slug: amazon-codecatalyst-list-spaces-request-next-token-string-structure
- name: Amazon Codecatalyst List Spaces Request Structure
  property_count: 1
  slug: amazon-codecatalyst-list-spaces-request-structure
- name: Amazon Codecatalyst List Spaces Response Structure
  property_count: 2
  slug: amazon-codecatalyst-list-spaces-response-structure
- name: Amazon Codecatalyst Name String Structure
  property_count: 0
  slug: amazon-codecatalyst-name-string-structure
- name: Amazon Codecatalyst Operation Type Structure
  property_count: 0
  slug: amazon-codecatalyst-operation-type-structure
- name: Amazon Codecatalyst Persistent Storage Configuration Size In Gi B Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-persistent-storage-configuration-size-in-gi-b-integer-structure
- name: Amazon Codecatalyst Persistent Storage Configuration Structure
  property_count: 1
  slug: amazon-codecatalyst-persistent-storage-configuration-structure
- name: Amazon Codecatalyst Persistent Storage Size In Gi B Integer Structure
  property_count: 0
  slug: amazon-codecatalyst-persistent-storage-size-in-gi-b-integer-structure
- name: Amazon Codecatalyst Persistent Storage Structure
  property_count: 1
  slug: amazon-codecatalyst-persistent-storage-structure
- name: Amazon Codecatalyst Project Description Structure
  property_count: 0
  slug: amazon-codecatalyst-project-description-structure
- name: Amazon Codecatalyst Project Display Name Structure
  property_count: 0
  slug: amazon-codecatalyst-project-display-name-structure
- name: Amazon Codecatalyst Project Information Structure
  property_count: 2
  slug: amazon-codecatalyst-project-information-structure
- name: Amazon Codecatalyst Project List Filter Structure
  property_count: 3
  slug: amazon-codecatalyst-project-list-filter-structure
- name: Amazon Codecatalyst Project List Filters Structure
  property_count: 0
  slug: amazon-codecatalyst-project-list-filters-structure
- name: Amazon Codecatalyst Project Summaries Structure
  property_count: 0
  slug: amazon-codecatalyst-project-summaries-structure
- name: Amazon Codecatalyst Project Summary Structure
  property_count: 3
  slug: amazon-codecatalyst-project-summary-structure
- name: Amazon Codecatalyst Region String Structure
  property_count: 0
  slug: amazon-codecatalyst-region-string-structure
- name: Amazon Codecatalyst Repositories Input Structure
  property_count: 0
  slug: amazon-codecatalyst-repositories-input-structure
- name: Amazon Codecatalyst Repository Input Structure
  property_count: 2
  slug: amazon-codecatalyst-repository-input-structure
- name: Amazon Codecatalyst Sensitive String Structure
  property_count: 0
  slug: amazon-codecatalyst-sensitive-string-structure
- name: Amazon Codecatalyst Source Repository Branch Ref String Structure
  property_count: 0
  slug: amazon-codecatalyst-source-repository-branch-ref-string-structure
- name: Amazon Codecatalyst Source Repository Branch String Structure
  property_count: 0
  slug: amazon-codecatalyst-source-repository-branch-string-structure
- name: Amazon Codecatalyst Source Repository Description String Structure
  property_count: 0
  slug: amazon-codecatalyst-source-repository-description-string-structure
- name: Amazon Codecatalyst Source Repository Id String Structure
  property_count: 0
  slug: amazon-codecatalyst-source-repository-id-string-structure
- name: Amazon Codecatalyst Source Repository Name String Structure
  property_count: 0
  slug: amazon-codecatalyst-source-repository-name-string-structure
- name: Amazon Codecatalyst Space Description Structure
  property_count: 0
  slug: amazon-codecatalyst-space-description-structure
- name: Amazon Codecatalyst Space Summaries Structure
  property_count: 0
  slug: amazon-codecatalyst-space-summaries-structure
- name: Amazon Codecatalyst Space Summary Structure
  property_count: 4
  slug: amazon-codecatalyst-space-summary-structure
- name: Amazon Codecatalyst Start Dev Environment Request Structure
  property_count: 3
  slug: amazon-codecatalyst-start-dev-environment-request-structure
- name: Amazon Codecatalyst Start Dev Environment Response Structure
  property_count: 4
  slug: amazon-codecatalyst-start-dev-environment-response-structure
- name: Amazon Codecatalyst Start Dev Environment Session Request Structure
  property_count: 1
  slug: amazon-codecatalyst-start-dev-environment-session-request-structure
- name: Amazon Codecatalyst Start Dev Environment Session Response Session Id String Structure
  property_count: 0
  slug: amazon-codecatalyst-start-dev-environment-session-response-session-id-string-structure
- name: Amazon Codecatalyst Start Dev Environment Session Response Structure
  property_count: 5
  slug: amazon-codecatalyst-start-dev-environment-session-response-structure
- name: Amazon Codecatalyst Status Reason Structure
  property_count: 0
  slug: amazon-codecatalyst-status-reason-structure
- name: Amazon Codecatalyst Stop Dev Environment Request Structure
  property_count: 0
  slug: amazon-codecatalyst-stop-dev-environment-request-structure
- name: Amazon Codecatalyst Stop Dev Environment Response Structure
  property_count: 4
  slug: amazon-codecatalyst-stop-dev-environment-response-structure
- name: Amazon Codecatalyst Stop Dev Environment Session Request Session Id String Structure
  property_count: 0
  slug: amazon-codecatalyst-stop-dev-environment-session-request-session-id-string-structure
- name: Amazon Codecatalyst Stop Dev Environment Session Request Structure
  property_count: 0
  slug: amazon-codecatalyst-stop-dev-environment-session-request-structure
- name: Amazon Codecatalyst Stop Dev Environment Session Response Session Id String Structure
  property_count: 0
  slug: amazon-codecatalyst-stop-dev-environment-session-response-session-id-string-structure
- name: Amazon Codecatalyst Stop Dev Environment Session Response Structure
  property_count: 4
  slug: amazon-codecatalyst-stop-dev-environment-session-response-structure
- name: Amazon Codecatalyst String List Structure
  property_count: 0
  slug: amazon-codecatalyst-string-list-structure
- name: Amazon Codecatalyst String Structure
  property_count: 0
  slug: amazon-codecatalyst-string-structure
- name: Amazon Codecatalyst Synthetic Timestamp_Date_Time Structure
  property_count: 0
  slug: amazon-codecatalyst-synthetic-timestamp_date_time-structure
- name: Amazon Codecatalyst Timestamp Structure
  property_count: 0
  slug: amazon-codecatalyst-timestamp-structure
- name: Amazon Codecatalyst Update Dev Environment Request Alias String Structure
  property_count: 0
  slug: amazon-codecatalyst-update-dev-environment-request-alias-string-structure
- name: Amazon Codecatalyst Update Dev Environment Request Structure
  property_count: 5
  slug: amazon-codecatalyst-update-dev-environment-request-structure
- name: Amazon Codecatalyst Update Dev Environment Response Alias String Structure
  property_count: 0
  slug: amazon-codecatalyst-update-dev-environment-response-alias-string-structure
- name: Amazon Codecatalyst Update Dev Environment Response Structure
  property_count: 8
  slug: amazon-codecatalyst-update-dev-environment-response-structure
- name: Amazon Codecatalyst Update Project Request Structure
  property_count: 1
  slug: amazon-codecatalyst-update-project-request-structure
- name: Amazon Codecatalyst Update Project Response Structure
  property_count: 4
  slug: amazon-codecatalyst-update-project-response-structure
- name: Amazon Codecatalyst Update Space Request Structure
  property_count: 1
  slug: amazon-codecatalyst-update-space-request-structure
- name: Amazon Codecatalyst Update Space Response Structure
  property_count: 3
  slug: amazon-codecatalyst-update-space-response-structure
- name: Amazon Codecatalyst User Identity Structure
  property_count: 4
  slug: amazon-codecatalyst-user-identity-structure
- name: Amazon Codecatalyst User Type Structure
  property_count: 0
  slug: amazon-codecatalyst-user-type-structure
- name: Amazon Codecatalyst Uuid Structure
  property_count: 0
  slug: amazon-codecatalyst-uuid-structure
- name: Amazon Codecatalyst Verify Session Response Identity String Structure
  property_count: 0
  slug: amazon-codecatalyst-verify-session-response-identity-string-structure
- name: Amazon Codecatalyst Verify Session Response Structure
  property_count: 1
  slug: amazon-codecatalyst-verify-session-response-structure
jsonld:
- class_count: 92
  name: Amazon Codecatalyst Context
  property_count: 74
  slug: amazon-codecatalyst-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon CodeCatalyst MCP Server
  slug: amazon-codecatalyst-mcp-server
modified: '2026-06-20'
name: Amazon CodeCatalyst
nav: Providers
network: true
overview: 'Amazon CodeCatalyst publishes 4 APIs on the [APIs.io](https://apis.io/) network, including AccessTokens API, Session API, Spaces API, and 1 more. Tagged areas include Amazon, Developer Tools, CI/CD, Collaboration, and DevOps.


  The Amazon CodeCatalyst catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CodeCatalyst''s developer surface includes authentication, getting-started guide, pricing, developer console, developer portal, documentation, engineering blog, and 22 more developer resources.'
random_paper: 18
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon CodeCatalyst API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-codecatalyst-jsonschema-spectral-rules
- effective_rule_count: 62
  extends:
  - spectral:oas
  name: Amazon CodeCatalyst API Rules
  rule_count: 21
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 11
  slug: amazon-codecatalyst-spectral-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 57.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 33.3
    contract_quality: 71.4
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 18.4
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-codecatalyst/refs/heads/main/screenshots/amazon-codecatalyst-2026-07-25T195952.png
security:
- kind: authentication
  name: Amazon Codecatalyst Authentication
  slug: amazon-codecatalyst-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Codecatalyst Domain Security
  slug: amazon-codecatalyst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Codecatalyst Vulnerability Disclosure
  slug: amazon-codecatalyst-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Codecatalyst Trust Center
  slug: amazon-codecatalyst-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-codecatalyst
tags:
- Amazon
- Developer Tools
- CI/CD
- Collaboration
- DevOps
- Source Control
use_cases:
- description: Use Dev Environments to eliminate local development setup time, allowing new developers to be productive within minutes on any project.
  name: Rapid Developer Onboarding
- description: Create and enforce consistent build, test, and deployment workflows across all projects in a space, reducing inconsistency and manual pipeline maintenance.
  name: Standardized CI/CD Pipelines
- description: Enable distributed teams to collaborate on source code through integrated repositories, pull requests, and code review workflows.
  name: Collaborative Code Development
website: https://aws.amazon.com/codecatalyst/
---
