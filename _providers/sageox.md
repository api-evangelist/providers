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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 105
  human_in_the_loop: 3
  name: Sageox Agentic Access
  operation_count: 223
  slug: sageox-agentic-access
  summary_line: 223 operations · 105 acting · 3 human-in-the-loop
api_count: 23
apis:
- description: Administrative analytics, session management, and system operations. Includes active session counts, user analytics, and management endpoints restricted to admin roles.
  name: SageOx Admin API
  slug: sageox-admin-api
- description: Multi-tenant telemetry platform for CLI tools and AI agents. Register applications, ingest events via API key authentication, and query analytics through the dashboard API. **Two authentication models
  name: SageOx AgentX API
  slug: sageox-agentx-api
- description: The API Keys API from SageOx — 2 operation(s) for api keys.
  name: SageOx API Keys API
  slug: sageox-api-keys-api
- description: Session management and token lifecycle. Validates JWT tokens issued by Better Auth, returns session details and user identity. Used by both web app and CLI for authentication verification.
  name: SageOx Auth API
  slug: sageox-auth-api
- description: Integration endpoints for the `ox` CLI tool. Includes device flow authentication (code request → polling → token exchange), server-side diagnostics, repository initialization, and friction event track
  name: SageOx CLI API
  slug: sageox-cli-api
- description: The Devices API from SageOx — 7 operation(s) for devices.
  name: SageOx Devices API
  slug: sageox-devices-api
- description: The Firmware Admin API from SageOx — 9 operation(s) for firmware admin.
  name: SageOx Firmware Admin API
  slug: sageox-firmware-admin-api
- description: The Firmware OTA API from SageOx — 1 operation(s) for firmware ota.
  name: SageOx Firmware OTA API
  slug: sageox-firmware-ota-api
- description: Browse repository files, view commits, compare branches, and manage the Ledger. The Ledger stores historical context (decisions, discussions, AI-generated summaries) as version-controlled files in a G
  name: SageOx Git API
  slug: sageox-git-api
- description: AI-generated guidance content and statistics. Provides contextual recommendations, best practices, and insights derived from team context and recording analysis.
  name: SageOx Guidance API
  slug: sageox-guidance-api
- description: Service health and readiness endpoints for orchestration platforms. The `/live` endpoint returns service liveness; `/ready` confirms database connectivity and dependency availability.
  name: SageOx Health API
  slug: sageox-health-api
- description: OpenAI-compatible chat completion endpoints. Proxies requests to configured LLM providers (Bedrock, OpenAI) with model routing, token usage tracking, and streaming support. Follows the OpenAI `/v1/cha
  name: SageOx LLM API
  slug: sageox-llm-api
- description: Collect frontend application logs for centralized error tracking and debugging. Accepts batches of structured log entries from web and CLI clients with severity levels and metadata.
  name: SageOx Logs API
  slug: sageox-logs-api
- description: The Miscellaneous API from SageOx — 12 operation(s) for miscellaneous.
  name: SageOx Miscellaneous API
  slug: sageox-miscellaneous-api
- description: Read, manage, and stream real-time notifications. Supports SSE (Server-Sent Events) for live delivery, bulk operations (mark read, delete), and preference-based filtering. Notifications originate from
  name: SageOx Notifications API
  slug: sageox-notifications-api
- description: Upload and manage photos with automatic OCR text extraction. Photos can be scoped to a repository (linked to recordings/discussions) or a team (shared resources). Uses presigned URLs for direct-to-sto
  name: SageOx Photos API
  slug: sageox-photos-api
- description: Unauthenticated endpoints for public-facing data. Returns team profiles, public recording metadata, shared conventions, and repository status without requiring authentication. Rate limited per IP.
  name: SageOx Public API
  slug: sageox-public-api
- description: 'Full lifecycle management for discussion recordings: chunked upload, transcription, speaker identification, AI-generated summaries, decisions, and action items. Recordings feed into the repository Led'
  name: SageOx Recordings API
  slug: sageox-recordings-api
- description: The Repositories API from SageOx — 6 operation(s) for repositories.
  name: SageOx Repositories API
  slug: sageox-repositories-api
- description: Repository initialization and merge operations. `initRepo` creates or reconnects a repository with SageOx (idempotent). `mergeRepos` combines ledger data when repositories are merged.
  name: SageOx Repository API
  slug: sageox-repository-api
- description: The runs API from SageOx — 7 operation(s) for runs.
  name: SageOx runs API
  slug: sageox-runs-api
- description: Create and manage teams with hierarchical membership (owner, admin, member). Handles invitations via email with role assignment, team-wide conventions and norms, and child-team relationships. Teams ar
  name: SageOx Teams API
  slug: sageox-teams-api
- description: Manage user profiles, preferences, API keys, and account settings. Preferences control notification delivery, theme, and feature opt-ins. API keys authenticate CLI and programmatic access.
  name: SageOx Users API
  slug: sageox-users-api
artifact_total: 28
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sageox-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sageox-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sageox-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sageox.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sageox.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://sageox.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sageox.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://sageox.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://sageox.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sageox
- group: start
  title: ''
  type: SignUp
  url: https://sageox.ai/register
- group: start
  title: ''
  type: Login
  url: https://sageox.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sageox.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sageox.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hi@sageox.ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sageox-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/sageox-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sageox-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sageox-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sageox-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sageox-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sageox-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/sageox-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sageox-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sageox-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sageox-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sageox-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sageox-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: SageOx is a Seattle-based platform that acts as the "hivemind for human-agent teams" — it captures team discussions, decisions, and AI coding-agent work sessions and distills them into a shared, searchable Ledger (per-repo history) and Team Context (team-wide knowledge) so that agents inherit full context instead of starting cold. Developers integrate through the Ox CLI (a Go binary that primes Claude Code, Codex, Cursor, Windsurf, Cline and other agents), the Ox MCP server (a hosted, OAuth-scoped Model Context Protocol endpoint), and a REST API covering repositories, recordings, notifications, teams, users, runs, API keys, and Ox Dot capture devices. SageOx raised a $15M seed round in May 2026 led by Canaan Partners with A.Capital, Pioneer Square Labs, and Founders' Co-op.
image: https://sageox.ai/sageox-wordmark-dark.png
layout: provider
mcp_servers:
- description: ''
  name: sageox-mcp.yml
  slug: sageox-mcpyml
modified: '2026-07-21'
name: SageOx
nav: Providers
network: true
overview: 'SageOx publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Admin API, AgentX API, API Keys API, and 20 more. Tagged areas include Company, AI Agents, Developer Tools, Knowledge Management, and Agent Memory.


  SageOx''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 22 more developer resources.'
random_paper: 35
scopes:
- name: Sageox Scopes
  scope_count: 4
  slug: sageox-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.1
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 48.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sageox Authentication
  slug: sageox-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Sageox Domain Security
  slug: sageox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sageox
tags:
- Company
- AI Agents
- Developer Tools
- Knowledge Management
- Agent Memory
- Model Context Protocol
- MCP
- CLI
- Team Collaboration
- Agentic Engineering
website: https://sageox.ai
---
