---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-08-17'
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
  name: Sageox Admin API
  slug: sageox-admin-api
- description: Multi-tenant telemetry platform for CLI tools and AI agents. Register applications, ingest events via API key authentication, and query analytics through the dashboard API. **Two authentication models
  name: Sageox AgentX API
  slug: sageox-agentx-api
- description: The API Keys API from Sageox — 2 operation(s) for api keys.
  name: Sageox API Keys API
  slug: sageox-api-keys-api
- description: Session management and token lifecycle. Validates JWT tokens issued by Better Auth, returns session details and user identity. Used by both web app and CLI for authentication verification.
  name: Sageox Auth API
  slug: sageox-auth-api
- description: Integration endpoints for the `ox` CLI tool. Includes device flow authentication (code request → polling → token exchange), server-side diagnostics, repository initialization, and friction event track
  name: Sageox CLI API
  slug: sageox-cli-api
- description: The Devices API from Sageox — 7 operation(s) for devices.
  name: Sageox Devices API
  slug: sageox-devices-api
- description: The Firmware Admin API from Sageox — 9 operation(s) for firmware admin.
  name: Sageox Firmware Admin API
  slug: sageox-firmware-admin-api
- description: The Firmware OTA API from Sageox — 1 operation(s) for firmware ota.
  name: Sageox Firmware OTA API
  slug: sageox-firmware-ota-api
- description: Browse repository files, view commits, compare branches, and manage the Ledger. The Ledger stores historical context (decisions, discussions, AI-generated summaries) as version-controlled files in a G
  name: Sageox Git API
  slug: sageox-git-api
- description: AI-generated guidance content and statistics. Provides contextual recommendations, best practices, and insights derived from team context and recording analysis.
  name: Sageox Guidance API
  slug: sageox-guidance-api
- description: Service health and readiness endpoints for orchestration platforms. The `/live` endpoint returns service liveness; `/ready` confirms database connectivity and dependency availability.
  name: Sageox Health API
  slug: sageox-health-api
- description: OpenAI-compatible chat completion endpoints. Proxies requests to configured LLM providers (Bedrock, OpenAI) with model routing, token usage tracking, and streaming support. Follows the OpenAI `/v1/cha
  name: Sageox LLM API
  slug: sageox-llm-api
- description: Collect frontend application logs for centralized error tracking and debugging. Accepts batches of structured log entries from web and CLI clients with severity levels and metadata.
  name: Sageox Logs API
  slug: sageox-logs-api
- description: The Miscellaneous API from Sageox — 12 operation(s) for miscellaneous.
  name: Sageox Miscellaneous API
  slug: sageox-miscellaneous-api
- description: Read, manage, and stream real-time notifications. Supports SSE (Server-Sent Events) for live delivery, bulk operations (mark read, delete), and preference-based filtering. Notifications originate from
  name: Sageox Notifications API
  slug: sageox-notifications-api
- description: Upload and manage photos with automatic OCR text extraction. Photos can be scoped to a repository (linked to recordings/discussions) or a team (shared resources). Uses presigned URLs for direct-to-sto
  name: Sageox Photos API
  slug: sageox-photos-api
- description: Unauthenticated endpoints for public-facing data. Returns team profiles, public recording metadata, shared conventions, and repository status without requiring authentication. Rate limited per IP.
  name: Sageox Public API
  slug: sageox-public-api
- description: 'Full lifecycle management for discussion recordings: chunked upload, transcription, speaker identification, AI-generated summaries, decisions, and action items. Recordings feed into the repository Led'
  name: Sageox Recordings API
  slug: sageox-recordings-api
- description: The Repositories API from Sageox — 6 operation(s) for repositories.
  name: Sageox Repositories API
  slug: sageox-repositories-api
- description: Repository initialization and merge operations. `initRepo` creates or reconnects a repository with SageOx (idempotent). `mergeRepos` combines ledger data when repositories are merged.
  name: Sageox Repository API
  slug: sageox-repository-api
- description: The runs API from Sageox — 7 operation(s) for runs.
  name: Sageox runs API
  slug: sageox-runs-api
- description: Create and manage teams with hierarchical membership (owner, admin, member). Handles invitations via email with role assignment, team-wide conventions and norms, and child-team relationships. Teams ar
  name: Sageox Teams API
  slug: sageox-teams-api
- description: Manage user profiles, preferences, API keys, and account settings. Preferences control notification delivery, theme, and feature opt-ins. API keys authenticate CLI and programmatic access.
  name: Sageox Users API
  slug: sageox-users-api
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SageOx Admin API
  slug: open-sageox-admin-api
- collection_type: open
  name: SageOx Admin AgentX API
  slug: open-sageox-agentx-api
- collection_type: open
  name: SageOx Admin API Keys API
  slug: open-sageox-api-keys-api
- collection_type: open
  name: SageOx Admin Auth API
  slug: open-sageox-auth-api
- collection_type: open
  name: SageOx Admin CLI API
  slug: open-sageox-cli-api
- collection_type: open
  name: SageOx Admin Devices API
  slug: open-sageox-devices-api
- collection_type: open
  name: SageOx Admin Firmware Admin API
  slug: open-sageox-firmware-admin-api
- collection_type: open
  name: SageOx Admin Firmware OTA API
  slug: open-sageox-firmware-ota-api
- collection_type: open
  name: SageOx Admin Git API
  slug: open-sageox-git-api
- collection_type: open
  name: SageOx Admin Guidance API
  slug: open-sageox-guidance-api
- collection_type: open
  name: SageOx Admin Health API
  slug: open-sageox-health-api
- collection_type: open
  name: SageOx Admin LLM API
  slug: open-sageox-llm-api
- collection_type: open
  name: SageOx Admin Logs API
  slug: open-sageox-logs-api
- collection_type: open
  name: SageOx Admin Miscellaneous API
  slug: open-sageox-miscellaneous-api
- collection_type: open
  name: SageOx Admin Notifications API
  slug: open-sageox-notifications-api
- collection_type: open
  name: SageOx Admin Photos API
  slug: open-sageox-photos-api
- collection_type: open
  name: SageOx Admin Public API
  slug: open-sageox-public-api
- collection_type: open
  name: SageOx Admin Recordings API
  slug: open-sageox-recordings-api
- collection_type: open
  name: SageOx Admin Repositories API
  slug: open-sageox-repositories-api
- collection_type: open
  name: SageOx Admin Repository API
  slug: open-sageox-repository-api
- collection_type: open
  name: SageOx Admin runs API
  slug: open-sageox-runs-api
- collection_type: open
  name: SageOx Admin Teams API
  slug: open-sageox-teams-api
- collection_type: open
  name: SageOx Admin Users API
  slug: open-sageox-users-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sageox-capture-a-recording.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sageox-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sageox-openapi-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/sageox-a2a.yml
created: '2026-07-17'
description: Sageox is a company surfaced as a portfolio company of canaan-partners and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: ''
  name: sageox-mcp.yml
  slug: sageox-mcpyml
modified: '2026-07-17'
name: Sageox
nav: Providers
network: true
overview: Sageox publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Admin API, AgentX API, API Keys API, and 20 more. Tagged areas include Company.
random_paper: 51
scopes:
- name: Sageox Scopes
  scope_count: 4
  slug: sageox-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 23.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 62.1
    developer_ergonomics: 10.3
    discoverability: 40.7
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 23.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
---
