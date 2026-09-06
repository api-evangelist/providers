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
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 37
  human_in_the_loop: 3
  name: Anthropic Agentic Access
  operation_count: 71
  slug: anthropic-agentic-access
  summary_line: 71 operations · 37 acting · 3 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation. The Messages API supports text, images, tool use, extended th
  name: Anthropic Messages API
  slug: anthropic-messages-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: List and inspect Claude models including Opus 4.7, Sonnet 4.6, and Haiku 4.5. The response includes max_input_tokens, max_tokens, and a capabilities object for every model so clients can discover mode
  name: Anthropic Models API
  slug: anthropic-models-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: 'The Files API lets you upload and manage files for reuse across Messages, Batches, code execution, and Managed Agents without re-uploading content. 500 MB request limit; supports PDFs, images, Office '
  name: Anthropic Files API
  slug: anthropic-files-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Create and manage custom Agent Skills. Skills are filesystem-based directories of instructions, scripts, and resources that Claude loads on demand via progressive disclosure. Workspace-wide sharing. T
  name: Anthropic Skills API
  slug: anthropic-skills-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Reusable, versioned agent configurations
  name: Anthropic Agents API
  slug: anthropic-agents-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Monitor and manage API keys
  name: Anthropic Api Keys API
  slug: anthropic-api-keys-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Service-level cost reporting
  name: Anthropic Cost API
  slug: anthropic-cost-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Container configuration for agent sessions
  name: Anthropic Environments API
  slug: anthropic-environments-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: User messages and tool results sent to a session
  name: Anthropic Events API
  slug: anthropic-events-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Retrieve organization information and settings
  name: Anthropic Organization API
  slug: anthropic-organization-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Create and manage organization invitations
  name: Anthropic Organization Invites API
  slug: anthropic-organization-invites-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Manage organization members and their roles
  name: Anthropic Organization Members API
  slug: anthropic-organization-members-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: APIs for generating well-written prompts for specified tasks
  name: Anthropic Prompt Generation API
  slug: anthropic-prompt-generation-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: APIs for enhancing existing prompts with feedback
  name: Anthropic Prompt Improvement API
  slug: anthropic-prompt-improvement-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: APIs for converting prompts into reusable templates with variables
  name: Anthropic Prompt Templatization API
  slug: anthropic-prompt-templatization-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Stateful agent execution instances
  name: Anthropic Sessions API
  slug: anthropic-sessions-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Token usage and consumption reporting
  name: Anthropic Usage API
  slug: anthropic-usage-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Manage workspace membership and roles
  name: Anthropic Workspace Members API
  slug: anthropic-workspace-members-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Create and manage workspaces within an organization
  name: Anthropic Workspaces API
  slug: anthropic-workspaces-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Agents?beta=true API from Anthropic — 1 operation(s) for agents?beta=true.
  name: Anthropic Agents?beta=true API
  slug: anthropic-agents-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Anthropic API API from Anthropic — 0 operation(s) for anthropic api.
  name: Anthropic Anthropic API
  slug: anthropic-anthropic-api-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Complete API from Anthropic — 1 operation(s) for complete.
  name: Anthropic Complete API
  slug: anthropic-complete-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Deployment Runs API from Anthropic — 1 operation(s) for deployment runs.
  name: Anthropic Deployment Runs API
  slug: anthropic-deployment-runs-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Deployment Runs?beta=true API from Anthropic — 1 operation(s) for deployment runs?beta=true.
  name: Anthropic Deployment Runs?beta=true API
  slug: anthropic-deployment-runs-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Deployments API from Anthropic — 5 operation(s) for deployments.
  name: Anthropic Deployments API
  slug: anthropic-deployments-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Deployments?beta=true API from Anthropic — 1 operation(s) for deployments?beta=true.
  name: Anthropic Deployments?beta=true API
  slug: anthropic-deployments-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Dreams API from Anthropic — 3 operation(s) for dreams.
  name: Anthropic Dreams API
  slug: anthropic-dreams-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Dreams?beta=true API from Anthropic — 1 operation(s) for dreams?beta=true.
  name: Anthropic Dreams?beta=true API
  slug: anthropic-dreams-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Environments?beta=true API from Anthropic — 1 operation(s) for environments?beta=true.
  name: Anthropic Environments?beta=true API
  slug: anthropic-environments-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Files?beta=true API from Anthropic — 1 operation(s) for files?beta=true.
  name: Anthropic Files?beta=true API
  slug: anthropic-files-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Memory Stores API from Anthropic — 7 operation(s) for memory stores.
  name: Anthropic Memory Stores API
  slug: anthropic-memory-stores-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Memory Stores?beta=true API from Anthropic — 1 operation(s) for memory stores?beta=true.
  name: Anthropic Memory Stores?beta=true API
  slug: anthropic-memory-stores-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Messages?beta=true API from Anthropic — 1 operation(s) for messages?beta=true.
  name: Anthropic Messages?beta=true API
  slug: anthropic-messages-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Models?beta=true API from Anthropic — 1 operation(s) for models?beta=true.
  name: Anthropic Models?beta=true API
  slug: anthropic-models-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Organizations API from Anthropic — 43 operation(s) for organizations.
  name: Anthropic Organizations API
  slug: anthropic-organizations-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Sessions?beta=true API from Anthropic — 1 operation(s) for sessions?beta=true.
  name: Anthropic Sessions?beta=true API
  slug: anthropic-sessions-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Skills?beta=true API from Anthropic — 1 operation(s) for skills?beta=true.
  name: Anthropic Skills?beta=true API
  slug: anthropic-skills-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Tunnels API from Anthropic — 7 operation(s) for tunnels.
  name: Anthropic Tunnels API
  slug: anthropic-tunnels-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Tunnels?beta=true API from Anthropic — 1 operation(s) for tunnels?beta=true.
  name: Anthropic Tunnels?beta=true API
  slug: anthropic-tunnels-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The User Profiles API from Anthropic — 2 operation(s) for user profiles.
  name: Anthropic User Profiles API
  slug: anthropic-user-profiles-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The User Profiles?beta=true API from Anthropic — 1 operation(s) for user profiles?beta=true.
  name: Anthropic User Profiles?beta=true API
  slug: anthropic-user-profiles-beta-true-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Vaults API from Anthropic — 6 operation(s) for vaults.
  name: Anthropic Vaults API
  slug: anthropic-vaults-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Vaults?beta=true API from Anthropic — 1 operation(s) for vaults?beta=true.
  name: Anthropic Vaults?beta=true API
  slug: anthropic-vaults-beta-true-api
arazzos:
- description: Create a batch, request cancellation, then poll until it leaves the canceling state.
  name: Anthropic Cancel a Message Batch and Confirm
  slug: anthropic-batch-cancel-and-confirm-workflow
- description: Submit a message batch, poll until processing ends, then fetch the JSONL results.
  name: Anthropic Create Batch, Poll, and Retrieve Results
  slug: anthropic-batch-create-poll-results-workflow
- description: Estimate input token usage for a prompt, then send the message only when it fits a budget.
  name: Anthropic Count Tokens Then Create Message
  slug: anthropic-count-tokens-then-message-workflow
- description: Create a workspace, add a user to it, then confirm the member appears in the roster.
  name: Anthropic Create Workspace and Add a Member
  slug: anthropic-create-workspace-and-add-member-workflow
- description: List available models, confirm a chosen model exists, then create a message with it.
  name: Anthropic Discover a Model and Send a Message
  slug: anthropic-discover-model-and-message-workflow
- description: Send an organization invite, then read it back and branch on whether it is still pending.
  name: Anthropic Invite an Org Member and Confirm
  slug: anthropic-invite-org-member-and-confirm-workflow
- description: List message batches, inspect the most recent one, and pull its results if it has ended.
  name: Anthropic List Batches and Fetch Latest Results
  slug: anthropic-list-batches-and-fetch-latest-results-workflow
- description: Find an org member by email, create a workspace, and add that member to it.
  name: Anthropic Onboard an Org Member into a Workspace
  slug: anthropic-onboard-member-to-workspace-workflow
- description: Create a workspace, add a member as a developer, then promote them to workspace admin.
  name: Anthropic Provision and Promote a Workspace Member
  slug: anthropic-provision-and-promote-workspace-member-workflow
- description: Upload a file, confirm it appears in the file list, then delete it to clean up.
  name: Anthropic Upload, List, and Clean Up a File
  slug: anthropic-upload-list-and-cleanup-file-workflow
- description: Upload a file, read back its metadata, and download its content when it is downloadable.
  name: Anthropic Upload, Verify, and Download a File
  slug: anthropic-upload-verify-download-file-workflow
artifact_total: 136
asyncapis:
- description: 'AsyncAPI specification modeling the Server-Sent Events (SSE) stream produced by Anthropic''s Messages API when `"stream": true` is set on a POST to `/v1/messages`. Transport: HTTP/1.1 with `Content-Typ'
  name: Anthropic Messages Streaming API
  slug: anthropic-asyncapi
- description: ''
  name: Anthropic Webhooks
  slug: anthropic-webhooks
collections:
- collection_type: postman
  name: Anthropic Admin API
  slug: postman-anthropic-admin-api
- collection_type: postman
  name: Anthropic Claude Code Analytics API
  slug: postman-anthropic-claude-code-analytics-api
- collection_type: postman
  name: Anthropic Files API
  slug: postman-anthropic-files-api
- collection_type: postman
  name: Anthropic Managed Agents API
  slug: postman-anthropic-managed-agents-api
- collection_type: postman
  name: Anthropic Message Batches API
  slug: postman-anthropic-message-batches-api
- collection_type: postman
  name: Anthropic Messages API
  slug: postman-anthropic-messages-api
- collection_type: postman
  name: Anthropic Models API
  slug: postman-anthropic-models-api
- collection_type: postman
  name: Anthropic Prompt Tools API
  slug: postman-anthropic-prompts-api
- collection_type: postman
  name: Anthropic Skills API
  slug: postman-anthropic-skills-api
- collection_type: postman
  name: Anthropic Token Counting API
  slug: postman-anthropic-token-counting-api
- collection_type: postman
  name: Anthropic Usage and Cost API
  slug: postman-anthropic-usage-cost-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Anthropic Admin API
  slug: open-anthropic-admin-api
- collection_type: open
  name: Anthropic Admin Agents API
  slug: open-anthropic-agents-api
- collection_type: open
  name: Anthropic Admin Agents Api Keys API
  slug: open-anthropic-api-keys-api
- collection_type: open
  name: Anthropic Admin Agents Claude Code Analytics API
  slug: open-anthropic-claude-code-analytics-api
- collection_type: open
  name: Anthropic Admin Agents Cost API
  slug: open-anthropic-cost-api
- collection_type: open
  name: Anthropic Admin Agents Environments API
  slug: open-anthropic-environments-api
- collection_type: open
  name: Anthropic Admin Agents Events API
  slug: open-anthropic-events-api
- collection_type: open
  name: Anthropic Admin Agents Files API
  slug: open-anthropic-files-api
- collection_type: open
  name: Anthropic Managed Agents API
  slug: open-anthropic-managed-agents-api
- collection_type: open
  name: Anthropic Admin Agents Message Batches API
  slug: open-anthropic-message-batches-api
- collection_type: open
  name: Anthropic Admin Agents Messages API
  slug: open-anthropic-messages-api
- collection_type: open
  name: Anthropic Admin Agents Models API
  slug: open-anthropic-models-api
- collection_type: open
  name: Anthropic Admin Agents Organization API
  slug: open-anthropic-organization-api
- collection_type: open
  name: Anthropic Admin Agents Organization Invites API
  slug: open-anthropic-organization-invites-api
- collection_type: open
  name: Anthropic Admin Agents Organization Members API
  slug: open-anthropic-organization-members-api
- collection_type: open
  name: Anthropic Admin Agents Prompt Generation API
  slug: open-anthropic-prompt-generation-api
- collection_type: open
  name: Anthropic Admin Agents Prompt Improvement API
  slug: open-anthropic-prompt-improvement-api
- collection_type: open
  name: Anthropic Admin Agents Prompt Templatization API
  slug: open-anthropic-prompt-templatization-api
- collection_type: open
  name: Anthropic Prompt Tools API
  slug: open-anthropic-prompts-api
- collection_type: open
  name: Anthropic Admin Agents Sessions API
  slug: open-anthropic-sessions-api
- collection_type: open
  name: Anthropic Admin Agents Skill Versions API
  slug: open-anthropic-skill-versions-api
- collection_type: open
  name: Anthropic Admin Agents Skills API
  slug: open-anthropic-skills-api
- collection_type: open
  name: Anthropic Admin Agents Token Counting API
  slug: open-anthropic-token-counting-api
- collection_type: open
  name: Anthropic Admin Agents Tokens API
  slug: open-anthropic-tokens-api
- collection_type: open
  name: Anthropic Admin Agents Usage API
  slug: open-anthropic-usage-api
- collection_type: open
  name: Anthropic Usage and Cost API
  slug: open-anthropic-usage-cost-api
- collection_type: open
  name: Anthropic Admin Agents Workspace Members API
  slug: open-anthropic-workspace-members-api
- collection_type: open
  name: Anthropic Admin Agents Workspaces API
  slug: open-anthropic-workspaces-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/anthropic-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anthropic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anthropic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anthropic-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/anthropic-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anthropic-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/anthropic-security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/anthropic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anthropic-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/anthropic-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anthropic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anthropic-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anthropic-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anthropic-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/anthropic-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anthropic-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anthropic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/anthropic-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-messages-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-models-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-message-batches-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-files-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-admin-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-prompts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-token-counting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-skills-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-usage-cost-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-claude-code-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anthropic-managed-agents-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/anthropic/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-batch-cancel-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-batch-create-poll-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-count-tokens-then-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-create-workspace-and-add-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-discover-model-and-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-invite-org-member-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-list-batches-and-fetch-latest-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-onboard-member-to-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-provision-and-promote-workspace-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-upload-list-and-cleanup-file-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anthropic-upload-verify-download-file-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anthropicresearch
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/anthropics/anthropic-quickstarts
- group: start
  title: ''
  type: Portal
  url: https://platform.claude.com/docs/en/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/messages
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anthropic.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://platform.claude.com/docs/en/release-notes/overview
- group: docs
  title: ''
  type: Documentation
  url: https://platform.claude.com/login
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.anthropic.com/en/api/rate-limits
- group: other
  title: ''
  type: Tiers
  url: https://docs.anthropic.com/en/api/service-tiers
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.anthropic.com/en/api/errors
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/client-sdks
- group: design
  title: ''
  type: Versioning
  url: https://docs.anthropic.com/en/api/versioning
- group: other
  title: ''
  type: Regions
  url: https://docs.anthropic.com/en/api/supported-regions
- group: operate
  title: ''
  type: Support
  url: https://support.claude.com/en/collections/4078531-api
- group: commercial
  title: ''
  type: Plans
  url: https://www.anthropic.com/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anthropic.com/pricing#api
- group: start
  title: ''
  type: Portal
  url: https://www.anthropic.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anthropic.com/en/docs/get-started
- group: other
  title: ''
  type: Glossary
  url: https://docs.anthropic.com/en/docs/about-claude/glossary
- group: docs
  title: ''
  type: Documentation
  url: https://www.anthropic.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anthropic.com/legal/privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.claude.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anthropic.com
- group: company
  title: ''
  type: Blog
  url: https://www.anthropic.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.anthropic.com/engineering
- group: start
  title: ''
  type: Signup
  url: https://console.anthropic.com/
- group: start
  title: ''
  type: Signup
  url: https://platform.claude.com/
- group: start
  title: ''
  type: Sandbox
  url: https://platform.claude.com/playground
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/beta-headers
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.anthropic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anthropic.com/legal/aup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/administration-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/usage-cost-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/claude-code-analytics-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anthropics
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-csharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/claude-agent-sdk-python
- group: build
  title: ''
  type: Tools
  url: https://github.com/anthropics/claude-code
- group: build
  title: ''
  type: Tools
  url: https://github.com/anthropics/claude-code-action
- group: build
  title: ''
  type: Tools
  url: https://github.com/anthropics/skills
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/anthropics/claude-cookbooks
- group: learn
  title: ''
  type: Courses
  url: https://github.com/anthropics/courses
- group: learn
  title: ''
  type: Courses
  url: https://github.com/anthropics/prompt-eng-interactive-tutorial
- group: build
  title: ''
  type: Plugins
  url: https://github.com/anthropics/claude-plugins-official
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/anthropics/financial-services
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/anthropics/claude-for-legal
- group: build
  title: ''
  type: Plugins
  url: https://github.com/anthropics/knowledge-work-plugins
- group: learn
  title: ''
  type: Training
  url: https://www.anthropic.com/learn
- group: operate
  title: ''
  type: Forums
  url: https://discord.com/invite/6PPFFzqPDZ
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/postman/anthropic-apis/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/token-counting
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/data-residency
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/messages-streaming
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/agents-and-tools/computer-use
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/citations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/batch-processing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/build-with-claude/compaction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/agents-and-tools/agent-skills/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/agents-and-tools/tool-use/memory-tool
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/openai-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/claude-on-amazon-bedrock
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/claude-on-vertex-ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/build-with-claude/claude-platform-on-aws
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/build-with-claude/claude-in-microsoft-foundry
- group: other
  title: ''
  type: Models
  url: https://docs.anthropic.com/en/docs/about-claude/models/all-models
- group: build
  title: ''
  type: SDKs
  url: https://docs.anthropic.com/en/docs/claude-code/sdk
- group: build
  title: ''
  type: SDKs
  url: https://docs.anthropic.com/en/api/sdks/cli
- group: docs
  title: ''
  type: Documentation
  url: https://modelcontextprotocol.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modelcontextprotocol
- group: docs
  title: ''
  type: Documentation
  url: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- group: start
  title: ''
  type: Portal
  url: https://www.anthropic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.claude.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anthropic.com/en/api/getting-started
- group: commercial
  title: ''
  type: Plans
  url: plans/anthropic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anthropic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/anthropic-finops.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/anthropic-tool-crosswalk.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/anthropic-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/anthropic-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.anthropic.com/llms.txt
- group: auth
  title: ''
  type: Security
  url: security/anthropic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: security/anthropic-trust-center.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/anthropic-lifecycle.yml
- group: docs
  title: ''
  type: APIReference
  url: https://platform.claude.com/docs/en/api/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.claude.com/docs/en/home
created: '2025-08-14T00:00:00.000Z'
description: 'Anthropic is an AI safety company and the creator of the Claude family of large language models (Opus, Sonnet, Haiku, and the Fable/Mythos frontier line). The Claude Developer Platform exposes them through a single REST API at api.anthropic.com: the Messages API for text, vision, tool use, thinking, streaming and structured outputs; Message Batches for asynchronous work at half price; Files, Token Counting, Models, and experimental Prompt Tools; Managed Agents with sessions, environments, memory stores, vaults and scheduled deployments; a Skills API; and an Admin API for organizations, workspaces, members, invites and API keys. Authentication is x-api-key with a required anthropic-version date header and dated anthropic-beta opt-ins. Anthropic also authors two of the open standards the agent ecosystem runs on — the Model Context Protocol and the Agent Skills specification — and ships Claude Code, the terminal agentic coding tool, which doubles as a first-party stdio MCP server.'
features:
- Claude Opus 4.7 — most capable generally available model for complex reasoning and agentic coding
- Claude Sonnet 4.6 — balanced model combining speed and intelligence with 1M context window
- Claude Haiku 4.5 — fastest model with near-frontier intelligence
- Messages API with text, vision, tool use, extended thinking, streaming, structured outputs
- Prompt caching with automatic and manual breakpoints, 5-minute and 1-hour TTLs, cache reads at 10% of input price
- Server-side compaction API for effectively infinite conversations on Opus 4.6/4.7 and Sonnet 4.6
- Memory tool (client-side) for cross-conversation persistence with ZDR support
- Message Batches API with 50% discount on both input and output tokens
- Files API for upload-once / reuse-many content across Messages and Managed Agents
- Agent Skills API (beta) — packaged domain expertise with progressive disclosure
- Claude Managed Agents (beta) — Agents, Sessions, Environments with SSE streaming and managed sandboxes
- Web Search tool ($10/1,000 searches) and Web Fetch tool (free)
- Code Execution tool — Python + Bash + filesystem in sandbox; 1,550 free container-hours/month
- Computer Use tool for browser and desktop automation (beta)
- Advisor tool (beta) for pairing executor and high-intelligence advisor models
- Tool Search tool and Programmatic Tool Calling
- Token-bucket rate limiting with cache-aware ITPM (cache reads excluded on most models)
- Five usage tiers (Tier 1-4 plus Monthly Invoicing) with automatic advancement
- Usage & Cost Admin API and Claude Code Analytics Admin API for FinOps reporting
- Rate Limits API for programmatic limit inspection
- Workload Identity Federation for short-lived bearer tokens
- Data residency controls (US-only inference at 1.1x pricing for models after Feb 2026)
- Available via Claude API, Claude Platform on AWS, Microsoft Foundry, AWS Bedrock, and Google Vertex AI
- Official SDKs: Python, TypeScript, Java, Go, Ruby, C#, PHP plus the `ant` CLI
- Claude Code (terminal agent) and Claude Code GitHub Action
- Open MCP specification stewardship via modelcontextprotocol.io
finops:
- name: Anthropic Finops
  service_category: AI and Machine Learning
  slug: anthropic-finops
graphqls:
- description: This GraphQL schema is a conceptual representation of the Anthropic Claude API derived from the REST API surface. The Anthropic API provides access to Claude large language models for text generation,
  name: Anthropic GraphQL Schema
  slug: anthropic-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anthropic.png
json_schemas:
- name: Anthropic Message
  property_count: 0
  slug: anthropic-message
- name: Anthropic Tool Use
  property_count: 0
  slug: anthropic-tool-use
jsonld:
- class_count: 0
  name: Anthropic Context
  property_count: 18
  slug: anthropic-context
layout: provider
modified: '2026-08-27'
name: Anthropic
nav: Providers
network: true
overview: 'Anthropic publishes 43 APIs on the [APIs.io](https://apis.io/) network, including Messages API, Models API, Files API, and 40 more. Tagged areas include Artificial Intelligence, Claude, Foundation Models, Large Language Models, and Machine-Learning.


  The Anthropic catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Anthropic''s developer surface includes authentication, changelog, CLI, documentation, developer portal, support, pricing, and 131 more developer resources.'
plans:
- name: Anthropic Plans Pricing
  plan_count: 5
  slug: anthropic-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 12
  name: Anthropic Rate Limits
  slug: anthropic-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Anthropic API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: anthropic-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Anthropic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: anthropic-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 74.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 77.6
    developer_ergonomics: 96.4
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 71.1
  previous_composite: 74.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/screenshots/anthropic-2026-06-20T172029.png
security:
- kind: authentication
  name: Anthropic Authentication
  slug: anthropic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Anthropic Domain Security
  slug: anthropic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anthropic Vulnerability Disclosure
  slug: anthropic-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Anthropic Trust Center
  slug: anthropic-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001:2022, ISO/IEC 42001:2023, HIPAA
slug: anthropic
tags:
- Artificial Intelligence
- Claude
- Foundation Models
- Large Language Models
- Machine-Learning
- MCP
- Agents
website: https://platform.claude.com/docs/en/home
---
