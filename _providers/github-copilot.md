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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Github Copilot Agentic Access
  operation_count: 19
  slug: github-copilot-agentic-access
  summary_line: 19 operations · 5 acting
api_count: 12
apis:
- description: API for GitHub Copilot Chat interactions and conversations.
  name: GitHub Copilot Chat API
  slug: github-copilot-chat-api
- description: Platform for building Copilot Extensions that integrate third-party tools, services, and custom agents into GitHub Copilot Chat, using GitHub Apps with agent or skillset configurations.
  name: GitHub Copilot Extensions API
  slug: github-copilot-extensions-api
- description: Autonomous coding agent that works in the background to complete tasks, spinning up secure development environments powered by GitHub Actions to explore code, make changes, run tests, and open pull re
  name: GitHub Copilot Coding Agent
  slug: github-copilot-coding-agent
- description: AI-powered code review agent that analyzes pull requests for issues, suggests fixes, and provides feedback across any programming language with agentic context gathering capabilities.
  name: GitHub Copilot Code Review
  slug: github-copilot-code-review
- description: GitHub official Model Context Protocol server that enables AI tools to interact with GitHub repositories, issues, pull requests, and other resources through a standardized protocol.
  name: GitHub MCP Server
  slug: github-mcp-server
- description: Configuration system for providing repository-level, path-specific, and organization-level custom instructions to guide Copilot behavior, code style, and response formatting.
  name: GitHub Copilot Custom Instructions
  slug: github-copilot-custom-instructions
- description: Organization-level Copilot billing and subscription information
  name: GitHub Copilot Copilot Billing API
  slug: github-copilot-copilot-billing-api
- description: Manage content exclusion path rules for organizations
  name: GitHub Copilot Copilot Content Exclusion API
  slug: github-copilot-copilot-content-exclusion-api
- description: Aggregated Copilot usage metrics by organization and team
  name: GitHub Copilot Copilot Metrics API
  slug: github-copilot-copilot-metrics-api
- description: Seat assignment management for organizations
  name: GitHub Copilot Copilot Seats API
  slug: github-copilot-copilot-seats-api
- description: Downloadable usage metrics reports for enterprises and organizations
  name: GitHub Copilot Copilot Usage Reports API
  slug: github-copilot-copilot-usage-reports-api
- description: Add and remove individual users and teams from Copilot subscriptions
  name: GitHub Copilot Copilot User Management API
  slug: github-copilot-copilot-user-management-api
arazzos:
- description: List all Copilot seat assignments for an organization and drill into the first seat's details.
  name: GitHub Copilot Audit Seat Assignments
  slug: github-copilot-audit-seats-workflow
- description: List current seats, set seats to pending cancellation for selected users, and confirm the updated billing breakdown.
  name: GitHub Copilot Deprovision Seats for Users
  slug: github-copilot-deprovision-users-workflow
- description: Fetch the latest 28-day enterprise usage report, then the daily enterprise and user-level usage reports for a specific day.
  name: GitHub Copilot Enterprise Metrics Report
  slug: github-copilot-enterprise-metrics-report-workflow
- description: Pull aggregated organization Copilot metrics, then fetch the latest 28-day org and user-level usage report links.
  name: GitHub Copilot Organization Metrics Report
  slug: github-copilot-org-metrics-report-workflow
- description: Confirm organization billing capacity, assign Copilot seats to whole teams, and read back the updated seat breakdown.
  name: GitHub Copilot Provision Seats for Teams
  slug: github-copilot-provision-teams-workflow
- description: Check organization billing capacity, assign Copilot seats to selected users, and verify a seat was granted.
  name: GitHub Copilot Provision Seats for Users
  slug: github-copilot-provision-users-workflow
- description: Pull organization-wide Copilot metrics, then drill into a specific team's aggregated metrics.
  name: GitHub Copilot Team Metrics Report
  slug: github-copilot-team-metrics-report-workflow
artifact_total: 192
collections:
- collection_type: postman
  name: GitHub Copilot REST API
  slug: postman-github-copilot
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GitHub Copilot REST Copilot Billing API
  slug: open-github-copilot-copilot-billing-api
- collection_type: open
  name: GitHub Copilot REST Copilot Billing Copilot Content Exclusion API
  slug: open-github-copilot-copilot-content-exclusion-api
- collection_type: open
  name: GitHub Copilot REST Copilot Billing Copilot Metrics API
  slug: open-github-copilot-copilot-metrics-api
- collection_type: open
  name: GitHub Copilot REST Copilot Billing Copilot Seats API
  slug: open-github-copilot-copilot-seats-api
- collection_type: open
  name: GitHub Copilot REST Copilot Billing Copilot Usage Reports API
  slug: open-github-copilot-copilot-usage-reports-api
- collection_type: open
  name: GitHub Copilot REST Copilot Billing Copilot User Management API
  slug: open-github-copilot-copilot-user-management-api
- collection_type: open
  name: GitHub Copilot REST API
  slug: open-github-copilot
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/github/github-mcp-server/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/github/github-mcp-server/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/github/github-mcp-server/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/github/github-mcp-server/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/github/github-mcp-server/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/github/github-mcp-server/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/github-copilot-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/github-copilot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/github-copilot-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/github-copilot-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/github-copilot-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/github-copilot-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/github-copilot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/github-copilot-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/github-copilot-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/github-copilot-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/github-copilot-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/github-copilot-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/github-copilot-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/github-copilot-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/github-copilot-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/github-copilot-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/github-copilot-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/github-copilot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/github-copilot-trust-center.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/github-copilot/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-copilot-audit-seats-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-copilot-deprovision-users-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-copilot-enterprise-metrics-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-copilot-org-metrics-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-copilot-provision-teams-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-copilot-provision-users-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-copilot-team-metrics-report-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://github.com/features/copilot
- group: operate
  title: ''
  type: StatusPage
  url: https://www.githubstatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/copilot/quickstart
- group: company
  title: ''
  type: Blog
  url: https://github.blog/tag/github-copilot/
- group: start
  title: ''
  type: Signup
  url: https://github.com/github-copilot/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/features/copilot/plans
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.blog/changelog/label/copilot/
- group: operate
  title: ''
  type: Support
  url: https://support.github.com
- group: build
  title: ''
  type: SDKs
  url: https://github.com/github/copilot-sdk
- group: auth
  title: ''
  type: TrustCenter
  url: https://copilot.github.trust.page/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
- group: auth
  title: ''
  type: Authentication
  url: https://docs.github.com/en/rest/authentication
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/github/rest-api-description
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/en/copilot
- group: other
  title: ''
  type: Marketplace
  url: https://github.com/marketplace?type=apps&copilot_app=true
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.github.com/llms.txt
created: '2024'
description: APIs and resources for GitHub Copilot, an AI pair programmer that helps you write code faster.
examples:
- key_count: 6
  name: Github Copilot Addteamstocopilotsubscription Example
  slug: github-copilot-addteamstocopilotsubscription-example
- key_count: 6
  name: Github Copilot Adduserstocopilotsubscription Example
  slug: github-copilot-adduserstocopilotsubscription-example
- key_count: 3
  name: Github Copilot Code Completions Editor Example
  slug: github-copilot-code-completions-editor-example
- key_count: 6
  name: Github Copilot Code Completions Language Metrics Example
  slug: github-copilot-code-completions-language-metrics-example
- key_count: 5
  name: Github Copilot Code Completions Model Example
  slug: github-copilot-code-completions-model-example
- key_count: 0
  name: Github Copilot Content Exclusion Rules Example
  slug: github-copilot-content-exclusion-rules-example
- key_count: 6
  name: Github Copilot Copilot Billing Info Example
  slug: github-copilot-copilot-billing-info-example
- key_count: 2
  name: Github Copilot Copilot Dotcom Chat Example
  slug: github-copilot-copilot-dotcom-chat-example
- key_count: 2
  name: Github Copilot Copilot Dotcom Pull Requests Example
  slug: github-copilot-copilot-dotcom-pull-requests-example
- key_count: 2
  name: Github Copilot Copilot Ide Chat Example
  slug: github-copilot-copilot-ide-chat-example
- key_count: 3
  name: Github Copilot Copilot Ide Code Completions Example
  slug: github-copilot-copilot-ide-code-completions-example
- key_count: 7
  name: Github Copilot Copilot Metrics Day Example
  slug: github-copilot-copilot-metrics-day-example
- key_count: 9
  name: Github Copilot Copilot Seat Detail Example
  slug: github-copilot-copilot-seat-detail-example
- key_count: 2
  name: Github Copilot Copilot Seats Response Example
  slug: github-copilot-copilot-seats-response-example
- key_count: 5
  name: Github Copilot Dotcom Chat Model Example
  slug: github-copilot-dotcom-chat-model-example
- key_count: 2
  name: Github Copilot Error Example
  slug: github-copilot-error-example
- key_count: 6
  name: Github Copilot Getcopilotbillingfororganization Example
  slug: github-copilot-getcopilotbillingfororganization-example
- key_count: 6
  name: Github Copilot Getcopilotcontentexclusionrules Example
  slug: github-copilot-getcopilotcontentexclusionrules-example
- key_count: 6
  name: Github Copilot Getcopilotmetricsfororganization Example
  slug: github-copilot-getcopilotmetricsfororganization-example
- key_count: 6
  name: Github Copilot Getcopilotmetricsforteam Example
  slug: github-copilot-getcopilotmetricsforteam-example
- key_count: 6
  name: Github Copilot Getcopilotseatforuser Example
  slug: github-copilot-getcopilotseatforuser-example
- key_count: 6
  name: Github Copilot Getenterprisecopilotusage28Day Example
  slug: github-copilot-getenterprisecopilotusage28day-example
- key_count: 6
  name: Github Copilot Getenterprisecopilotusagedaily Example
  slug: github-copilot-getenterprisecopilotusagedaily-example
- key_count: 6
  name: Github Copilot Getenterpriseuserscopilotusage28Day Example
  slug: github-copilot-getenterpriseuserscopilotusage28day-example
- key_count: 6
  name: Github Copilot Getenterpriseuserscopilotusagedaily Example
  slug: github-copilot-getenterpriseuserscopilotusagedaily-example
- key_count: 6
  name: Github Copilot Getorganizationcopilotusage28Day Example
  slug: github-copilot-getorganizationcopilotusage28day-example
- key_count: 6
  name: Github Copilot Getorganizationcopilotusagedaily Example
  slug: github-copilot-getorganizationcopilotusagedaily-example
- key_count: 6
  name: Github Copilot Getorganizationuserscopilotusage28Day Example
  slug: github-copilot-getorganizationuserscopilotusage28day-example
- key_count: 6
  name: Github Copilot Getorganizationuserscopilotusagedaily Example
  slug: github-copilot-getorganizationuserscopilotusagedaily-example
- key_count: 3
  name: Github Copilot Ide Chat Editor Example
  slug: github-copilot-ide-chat-editor-example
- key_count: 7
  name: Github Copilot Ide Chat Model Example
  slug: github-copilot-ide-chat-model-example
- key_count: 6
  name: Github Copilot Listcopilotseats Example
  slug: github-copilot-listcopilotseats-example
- key_count: 2
  name: Github Copilot Metrics Language Summary Example
  slug: github-copilot-metrics-language-summary-example
- key_count: 5
  name: Github Copilot Pull Request Model Example
  slug: github-copilot-pull-request-model-example
- key_count: 3
  name: Github Copilot Pull Request Repository Example
  slug: github-copilot-pull-request-repository-example
- key_count: 6
  name: Github Copilot Removeteamsfromcopilotsubscription Example
  slug: github-copilot-removeteamsfromcopilotsubscription-example
- key_count: 6
  name: Github Copilot Removeusersfromcopilotsubscription Example
  slug: github-copilot-removeusersfromcopilotsubscription-example
- key_count: 6
  name: Github Copilot Seat Breakdown Example
  slug: github-copilot-seat-breakdown-example
- key_count: 1
  name: Github Copilot Seats Cancelled Response Example
  slug: github-copilot-seats-cancelled-response-example
- key_count: 1
  name: Github Copilot Seats Created Response Example
  slug: github-copilot-seats-created-response-example
- key_count: 1
  name: Github Copilot Selected Teams Request Example
  slug: github-copilot-selected-teams-request-example
- key_count: 1
  name: Github Copilot Selected Users Request Example
  slug: github-copilot-selected-users-request-example
- key_count: 6
  name: Github Copilot Setcopilotcontentexclusionrules Example
  slug: github-copilot-setcopilotcontentexclusionrules-example
- key_count: 18
  name: Github Copilot Simple User Example
  slug: github-copilot-simple-user-example
- key_count: 12
  name: Github Copilot Team Example
  slug: github-copilot-team-example
- key_count: 2
  name: Github Copilot Usage Report Daily Example
  slug: github-copilot-usage-report-daily-example
- key_count: 3
  name: Github Copilot Usage Report28 Day Example
  slug: github-copilot-usage-report28-day-example
features:
- description: AI-powered inline code suggestions that complete lines, functions, and entire blocks as you type in your IDE.
  name: Code Completion
- description: Conversational AI assistant for asking questions about code, generating solutions, and debugging directly in your editor.
  name: Chat
- description: Autonomous agent that explores code, makes changes, runs tests, and opens pull requests from issue assignments.
  name: Coding Agent
- description: AI-powered pull request review that analyzes changes, identifies issues, and suggests fixes across any language.
  name: Code Review
- description: Third-party integrations that extend Copilot Chat with custom tools, services, and domain-specific agents.
  name: Extensions
- description: Repository-level and organization-level configuration to guide Copilot behavior, code style, and conventions.
  name: Custom Instructions
- description: Model Context Protocol server enabling AI tools to interact with GitHub repositories, issues, and pull requests.
  name: MCP Server
- description: Governance controls to specify which files and repositories Copilot can access at organization and enterprise level.
  name: Content Exclusion
- description: Detailed analytics on Copilot adoption, usage patterns, and productivity impact across organizations and enterprises.
  name: Usage Metrics
- description: Programmatic management of Copilot seat assignments, billing, and subscription details for organizations and teams.
  name: Seat Management
finops:
- name: Github Copilot Finops
  service_category: Developer Tools / AI
  slug: github-copilot-finops
image: https://github.githubassets.com/images/modules/site/copilot/copilot-logo.png
integrations:
- description: Full Copilot integration in VS Code including code completion, chat, code review, and MCP support.
  name: Visual Studio Code
- description: Copilot code completion and chat support across IntelliJ, PyCharm, WebStorm, and other JetBrains IDEs.
  name: JetBrains IDEs
- description: Copilot Chat, code review, and coding agent capabilities directly in the GitHub web interface.
  name: GitHub.com
- description: Copilot coding agent uses GitHub Actions to spin up secure environments for autonomous coding tasks.
  name: GitHub Actions
- description: Standard protocol integration enabling AI tools to access GitHub data through the official MCP server.
  name: Model Context Protocol
json_schemas:
- name: CodeCompletionsEditor
  property_count: 3
  slug: github-copilot-code-completions-editor
- name: CodeCompletionsLanguageMetrics
  property_count: 6
  slug: github-copilot-code-completions-language-metrics
- name: CodeCompletionsModel
  property_count: 5
  slug: github-copilot-code-completions-model
- name: CodeCompletionsEditor
  property_count: 3
  slug: github-copilot-codecompletionseditor
- name: CodeCompletionsLanguageMetrics
  property_count: 6
  slug: github-copilot-codecompletionslanguagemetrics
- name: CodeCompletionsModel
  property_count: 5
  slug: github-copilot-codecompletionsmodel
- name: ContentExclusionRules
  property_count: 0
  slug: github-copilot-content-exclusion-rules
- name: ContentExclusionRules
  property_count: 0
  slug: github-copilot-contentexclusionrules
- name: CopilotBillingInfo
  property_count: 6
  slug: github-copilot-copilot-billing-info
- name: CopilotDotcomChat
  property_count: 2
  slug: github-copilot-copilot-dotcom-chat
- name: CopilotDotcomPullRequests
  property_count: 2
  slug: github-copilot-copilot-dotcom-pull-requests
- name: CopilotIdeChat
  property_count: 2
  slug: github-copilot-copilot-ide-chat
- name: CopilotIdeCodeCompletions
  property_count: 3
  slug: github-copilot-copilot-ide-code-completions
- name: CopilotMetricsDay
  property_count: 7
  slug: github-copilot-copilot-metrics-day
- name: CopilotSeatDetail
  property_count: 9
  slug: github-copilot-copilot-seat-detail
- name: CopilotSeatsResponse
  property_count: 2
  slug: github-copilot-copilot-seats-response
- name: CopilotBillingInfo
  property_count: 7
  slug: github-copilot-copilotbillinginfo
- name: CopilotDotcomChat
  property_count: 2
  slug: github-copilot-copilotdotcomchat
- name: CopilotDotcomPullRequests
  property_count: 2
  slug: github-copilot-copilotdotcompullrequests
- name: CopilotIdeChat
  property_count: 2
  slug: github-copilot-copilotidechat
- name: CopilotIdeCodeCompletions
  property_count: 3
  slug: github-copilot-copilotidecodecompletions
- name: CopilotMetricsDay
  property_count: 7
  slug: github-copilot-copilotmetricsday
- name: CopilotSeatDetail
  property_count: 9
  slug: github-copilot-copilotseatdetail
- name: CopilotSeatsResponse
  property_count: 2
  slug: github-copilot-copilotseatsresponse
- name: DotcomChatModel
  property_count: 5
  slug: github-copilot-dotcom-chat-model
- name: DotcomChatModel
  property_count: 5
  slug: github-copilot-dotcomchatmodel
- name: Error
  property_count: 2
  slug: github-copilot-error
- name: IdeChatEditor
  property_count: 3
  slug: github-copilot-ide-chat-editor
- name: IdeChatModel
  property_count: 7
  slug: github-copilot-ide-chat-model
- name: IdeChatEditor
  property_count: 3
  slug: github-copilot-idechateditor
- name: IdeChatModel
  property_count: 7
  slug: github-copilot-idechatmodel
- name: MetricsLanguageSummary
  property_count: 2
  slug: github-copilot-metrics-language-summary
- name: GitHub Copilot Metrics Schema
  property_count: 0
  slug: github-copilot-metrics
- name: MetricsLanguageSummary
  property_count: 2
  slug: github-copilot-metricslanguagesummary
- name: PullRequestModel
  property_count: 5
  slug: github-copilot-pull-request-model
- name: PullRequestRepository
  property_count: 3
  slug: github-copilot-pull-request-repository
- name: PullRequestModel
  property_count: 5
  slug: github-copilot-pullrequestmodel
- name: PullRequestRepository
  property_count: 3
  slug: github-copilot-pullrequestrepository
- name: SeatBreakdown
  property_count: 6
  slug: github-copilot-seat-breakdown
- name: GitHub Copilot Seat Management Schema
  property_count: 0
  slug: github-copilot-seat
- name: SeatBreakdown
  property_count: 6
  slug: github-copilot-seatbreakdown
- name: SeatsCancelledResponse
  property_count: 1
  slug: github-copilot-seats-cancelled-response
- name: SeatsCreatedResponse
  property_count: 1
  slug: github-copilot-seats-created-response
- name: SeatsCancelledResponse
  property_count: 1
  slug: github-copilot-seatscancelledresponse
- name: SeatsCreatedResponse
  property_count: 1
  slug: github-copilot-seatscreatedresponse
- name: SelectedTeamsRequest
  property_count: 1
  slug: github-copilot-selected-teams-request
- name: SelectedUsersRequest
  property_count: 1
  slug: github-copilot-selected-users-request
- name: SelectedTeamsRequest
  property_count: 1
  slug: github-copilot-selectedteamsrequest
- name: SelectedUsersRequest
  property_count: 1
  slug: github-copilot-selectedusersrequest
- name: SimpleUser
  property_count: 18
  slug: github-copilot-simple-user
- name: SimpleUser
  property_count: 18
  slug: github-copilot-simpleuser
- name: Team
  property_count: 12
  slug: github-copilot-team
- name: UsageReportDaily
  property_count: 2
  slug: github-copilot-usage-report-daily
- name: UsageReport28Day
  property_count: 3
  slug: github-copilot-usage-report28-day
- name: UsageReport28Day
  property_count: 3
  slug: github-copilot-usagereport28day
- name: UsageReportDaily
  property_count: 2
  slug: github-copilot-usagereportdaily
json_structures:
- name: Github Copilot Code Completions Editor Structure
  property_count: 3
  slug: github-copilot-code-completions-editor-structure
- name: Github Copilot Code Completions Language Metrics Structure
  property_count: 6
  slug: github-copilot-code-completions-language-metrics-structure
- name: Github Copilot Code Completions Model Structure
  property_count: 5
  slug: github-copilot-code-completions-model-structure
- name: Github Copilot Content Exclusion Rules Structure
  property_count: 0
  slug: github-copilot-content-exclusion-rules-structure
- name: Github Copilot Copilot Billing Info Structure
  property_count: 6
  slug: github-copilot-copilot-billing-info-structure
- name: Github Copilot Copilot Dotcom Chat Structure
  property_count: 2
  slug: github-copilot-copilot-dotcom-chat-structure
- name: Github Copilot Copilot Dotcom Pull Requests Structure
  property_count: 2
  slug: github-copilot-copilot-dotcom-pull-requests-structure
- name: Github Copilot Copilot Ide Chat Structure
  property_count: 2
  slug: github-copilot-copilot-ide-chat-structure
- name: Github Copilot Copilot Ide Code Completions Structure
  property_count: 3
  slug: github-copilot-copilot-ide-code-completions-structure
- name: Github Copilot Copilot Metrics Day Structure
  property_count: 7
  slug: github-copilot-copilot-metrics-day-structure
- name: Github Copilot Copilot Seat Detail Structure
  property_count: 9
  slug: github-copilot-copilot-seat-detail-structure
- name: Github Copilot Copilot Seats Response Structure
  property_count: 2
  slug: github-copilot-copilot-seats-response-structure
- name: Github Copilot Dotcom Chat Model Structure
  property_count: 5
  slug: github-copilot-dotcom-chat-model-structure
- name: Github Copilot Error Structure
  property_count: 2
  slug: github-copilot-error-structure
- name: Github Copilot Ide Chat Editor Structure
  property_count: 3
  slug: github-copilot-ide-chat-editor-structure
- name: Github Copilot Ide Chat Model Structure
  property_count: 7
  slug: github-copilot-ide-chat-model-structure
- name: Github Copilot Metrics Language Summary Structure
  property_count: 2
  slug: github-copilot-metrics-language-summary-structure
- name: Github Copilot Pull Request Model Structure
  property_count: 5
  slug: github-copilot-pull-request-model-structure
- name: Github Copilot Pull Request Repository Structure
  property_count: 3
  slug: github-copilot-pull-request-repository-structure
- name: Github Copilot Seat Breakdown Structure
  property_count: 6
  slug: github-copilot-seat-breakdown-structure
- name: Github Copilot Seats Cancelled Response Structure
  property_count: 1
  slug: github-copilot-seats-cancelled-response-structure
- name: Github Copilot Seats Created Response Structure
  property_count: 1
  slug: github-copilot-seats-created-response-structure
- name: Github Copilot Selected Teams Request Structure
  property_count: 1
  slug: github-copilot-selected-teams-request-structure
- name: Github Copilot Selected Users Request Structure
  property_count: 1
  slug: github-copilot-selected-users-request-structure
- name: Github Copilot Simple User Structure
  property_count: 18
  slug: github-copilot-simple-user-structure
- name: Github Copilot Structure
  property_count: 0
  slug: github-copilot-structure
- name: Github Copilot Team Structure
  property_count: 12
  slug: github-copilot-team-structure
- name: Github Copilot Usage Report Daily Structure
  property_count: 2
  slug: github-copilot-usage-report-daily-structure
- name: Github Copilot Usage Report28 Day Structure
  property_count: 3
  slug: github-copilot-usage-report28-day-structure
jsonld:
- class_count: 0
  name: Github Copilot Context
  property_count: 0
  slug: github-copilot-context
layout: provider
mcp_servers:
- description: The GitHub MCP server exposes GitHub itself (repositories, issues, pull requests, Actions, code security, etc.) to MCP-capable agents including GitHub Copilot. Tools are organized into configurable to
  name: GitHub Copilot MCP Server
  slug: github-copilot-mcp-server
modified: '2026-06-20'
name: GitHub Copilot
nav: Providers
network: true
overview: 'GitHub Copilot publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Copilot Billing API, Copilot Content Exclusion API, Copilot Metrics API, and 3 more. Tagged areas include Agents, Artificial Intelligence, Code Generation, Code Review, and Coding Agents.


  The GitHub Copilot catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  GitHub Copilot''s developer surface includes authentication, changelog, CLI, developer portal, getting-started guide, engineering blog, signup flow, and 44 more developer resources.'
plans:
- name: Github Copilot Plans Pricing
  plan_count: 5
  slug: github-copilot-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 11
  name: Github Copilot Rate Limits
  slug: github-copilot-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: GitHub Copilot API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: github-copilot-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: GitHub Copilot API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 12
  slug: github-copilot-spectral-rules
scopes:
- name: Github Copilot Scopes
  scope_count: 5
  slug: github-copilot-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 64.2
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 30.3
    contract_quality: 73.1
    developer_ergonomics: 69.0
    discoverability: 83.3
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 64.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/github-copilot/refs/heads/main/screenshots/github-copilot-2026-06-20T181939.png
security:
- kind: authentication
  name: Github Copilot Authentication
  slug: github-copilot-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Github Copilot Domain Security
  slug: github-copilot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Github Copilot Vulnerability Disclosure
  slug: github-copilot-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Github Copilot Trust Center
  slug: github-copilot-trust-center
  summary_line: trust center published
slug: github-copilot
tags:
- Agents
- Artificial Intelligence
- Code Generation
- Code Review
- Coding Agents
- Custom Instructions
- Developer Tools
- Extensions
- IDE
- Machine-Learning
- MCP
- Metrics
- Productivity
use_cases:
- description: Accelerate software development with AI-powered code completions, chat assistance, and automated code review.
  name: Developer Productivity
- description: Manage Copilot deployments at scale with seat management, content exclusion, usage metrics, and compliance controls.
  name: Enterprise Copilot Governance
- description: Build domain-specific Copilot Extensions and agents that integrate third-party tools and services into the developer workflow.
  name: Custom AI Tooling
- description: Automate code review, identify potential issues, and enforce coding standards using the Copilot Code Review agent.
  name: Code Quality Automation
---
