---
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 227
  human_in_the_loop: 29
  name: Pipeshub Agentic Access
  operation_count: 381
  slug: pipeshub-agentic-access
  summary_line: 381 operations · 227 acting · 29 human-in-the-loop
api_count: 2
apis:
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Custom AI agents with specialized capabilities and tool integrations
  name: PipesHub Agents API
  slug: pipeshub-agents-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Manage individual AI model providers - add, update, delete, and set defaults.
  name: PipesHub AI Models Providers API
  slug: pipeshub-ai-models-providers-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Configure authentication providers including Azure AD, Microsoft, Google OAuth, SAML SSO, and custom OAuth 2.0.
  name: PipesHub Authentication Configuration API
  slug: pipeshub-authentication-configuration-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Manage organization-level configuration including Slack bot integration, AI models, and metrics collection.
  name: PipesHub Configuration Manager API
  slug: pipeshub-configuration-manager-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Connector-related operations
  name: PipesHub Connector API
  slug: pipeshub-connector-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Configure authentication, sync settings, and filters for connectors
  name: PipesHub Connector Configuration API
  slug: pipeshub-connector-configuration-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Enable/disable connectors for sync or agent functionality
  name: PipesHub Connector Control API
  slug: pipeshub-connector-control-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Dynamic filter options for selecting which data to sync
  name: PipesHub Connector Filters API
  slug: pipeshub-connector-filters-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Create, manage, and delete connector instances for your organization
  name: PipesHub Connector Instances API
  slug: pipeshub-connector-instances-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: OAuth 2.0 authorization flow for connectors requiring user consent
  name: PipesHub Connector OAuth API
  slug: pipeshub-connector-oauth-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Browse available connector types and their configuration schemas
  name: PipesHub Connector Registry API
  slug: pipeshub-connector-registry-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: The Connectors API from PipesHub — 1 operation(s) for connectors.
  name: PipesHub Connectors API
  slug: pipeshub-connectors-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Server-backed Speech-to-Text (STT) and Text-to-Speech (TTS) for the chat UI. These endpoints are used by the chat frontend when an admin has configured a TTS/STT provider under the AI Models configura
  name: PipesHub Conversational Speech API
  slug: pipeshub-conversational-speech-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: AI-powered conversational chat management with citations and follow-up questions
  name: PipesHub Conversations API
  slug: pipeshub-conversations-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Endpoints for scheduling, managing, and monitoring data crawling jobs for enterprise connectors. The Crawling Manager uses BullMQ (Redis-based queue) to schedule and execute crawling jobs that sync da
  name: PipesHub Crawling Jobs API
  slug: pipeshub-crawling-jobs-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Service-to-service storage endpoints, authenticated with the storage scoped token rather than a signed-in user's session, so these are **not** callable by API clients or the browser. Storage checks on
  name: PipesHub Internal Storage API
  slug: pipeshub-internal-storage-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Knowledge base management operations
  name: PipesHub Knowledge Base API
  slug: pipeshub-knowledge-base-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Unified browse API for root and child nodes (apps, record groups, folders, records) with filtering and search
  name: PipesHub Knowledge Hub API
  slug: pipeshub-knowledge-hub-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Model Context Protocol (MCP) endpoints for AI tool integration. PipesHub exposes a Streamable HTTP MCP server that allows MCP-compatible clients (such as Claude Desktop, Cursor, or custom agents) to i
  name: PipesHub MCP API
  slug: pipeshub-mcp-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Configure telemetry and metrics collection for application monitoring and analytics. PipesHub collects anonymized usage metrics to help improve the product. Metrics are pushed to a configurable remote
  name: PipesHub Metrics Collection API
  slug: pipeshub-metrics-collection-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: In-app notifications for the signed-in user (connector errors, warnings, and related alerts)
  name: PipesHub Notifications API
  slug: pipeshub-notifications-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: OAuth 2.0 token exchange for third-party authentication providers
  name: PipesHub OAuth API
  slug: pipeshub-oauth-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: 'Manage OAuth 2.0 client applications registered with PipesHub. OAuth apps allow third-party applications to access PipesHub APIs on behalf of users or organizations. Each app receives a client ID and '
  name: PipesHub OAuth Apps API
  slug: pipeshub-oauth-apps-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Admin management of OAuth credentials for connector types
  name: PipesHub OAuth Configuration API
  slug: pipeshub-oauth-configuration-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: PipesHub OAuth 2.0 Authorization Server implementing RFC 6749, RFC 7636 (PKCE), and OpenID Connect. **Supported Grant Types:** - `authorization_code` - Standard OAuth flow with PKCE support - `client_
  name: PipesHub OAuth Provider API
  slug: pipeshub-oauth-provider-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: OpenID Connect 1.0 endpoints for identity federation and discovery. **Discovery:** - `/.well-known/openid-configuration` - Authorization server metadata - `/.well-known/oauth-authorization-server` - A
  name: PipesHub OpenID Connect API
  slug: pipeshub-openid-connect-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Admin configuration of authentication methods including MFA steps and allowed providers
  name: PipesHub Organization Auth Config API
  slug: pipeshub-organization-auth-config-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Organization management operations
  name: PipesHub Organizations API
  slug: pipeshub-organizations-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Permission management for knowledge bases
  name: PipesHub Permissions API
  slug: pipeshub-permissions-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Self-service, long-lived, scoped, revocable credentials that act as their creator — unlike an OAuth app's `client_credentials` flow, which acts as the app. **Who can create one** - **Any authenticated
  name: PipesHub Personal Access Tokens API
  slug: pipeshub-personal-access-tokens-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Platform-wide settings including file upload limits, feature flags, and custom system prompts.
  name: PipesHub Platform Settings API
  slug: pipeshub-platform-settings-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Workspaces that group related assistant and agent conversations under a shared name, custom instructions, a knowledge scope, and reference files. Projects can be shared with teammates; project members
  name: PipesHub Projects API
  slug: pipeshub-projects-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Configure public URLs for frontend application and connector callbacks.
  name: PipesHub Public URLs API
  slug: pipeshub-public-urls-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Record management and operations
  name: PipesHub Records API
  slug: pipeshub-records-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: SAML 2.0 Single Sign-On integration with enterprise Identity Providers
  name: PipesHub SAML API
  slug: pipeshub-saml-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Enterprise semantic search across all indexed knowledge with relevance scoring
  name: PipesHub Semantic Search API
  slug: pipeshub-semantic-search-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: 'Machine identities that automation authenticates as, so a script reads with its own permissions rather than borrowing a person''s. A service account is an ordinary user record with `kind: "service"`. I'
  name: PipesHub Service Accounts API
  slug: pipeshub-service-accounts-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: The credential a service account authenticates with. A service token is an OAuth access token, so signing, hashing, revocation and the `/mcp` path are the same machinery personal access tokens use. Wh
  name: PipesHub Service Tokens API
  slug: pipeshub-service-tokens-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: 'Beta: Skills (SKILL.md packages) that agents load on demand — CRUD, versioning, resources, import (npm/URL/upload), and learning-loop candidate review. Gated by the ENABLE_SKILLS platform feature flag'
  name: PipesHub Skills API
  slug: pipeshub-skills-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Configure SMTP email server for sending notifications and invitations.
  name: PipesHub SMTP Configuration API
  slug: pipeshub-smtp-configuration-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Configure storage backend for file uploads and documents. Supports AWS S3, Azure Blob Storage, or local filesystem.
  name: PipesHub Storage Configuration API
  slug: pipeshub-storage-configuration-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Team management operations
  name: PipesHub Teams API
  slug: pipeshub-teams-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: The Toolset API from PipesHub — 1 operation(s) for toolset.
  name: PipesHub Toolset API
  slug: pipeshub-toolset-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Configure authentication and settings for toolset instances
  name: PipesHub Toolset Configuration API
  slug: pipeshub-toolset-configuration-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Create, manage, and configure toolset instances for your organization
  name: PipesHub Toolset Instances API
  slug: pipeshub-toolset-instances-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: OAuth 2.0 authorization flow for toolsets requiring user consent
  name: PipesHub Toolset OAuth API
  slug: pipeshub-toolset-oauth-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Browse available toolsets and their configuration schemas for agent integrations
  name: PipesHub Toolset Registry API
  slug: pipeshub-toolset-registry-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: User authentication including multi-step MFA, password reset, OTP login, and token management
  name: PipesHub User Account API
  slug: pipeshub-user-account-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: User group management operations
  name: PipesHub User Groups API
  slug: pipeshub-user-groups-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: User management operations
  name: PipesHub Users API
  slug: pipeshub-users-api
- baseURL: https://app.pipeshub.com/api/v1
  baseurl_source: declared
  description: Manage web search providers (DuckDuckGo, Serper, Tavily, Exa) and settings for internet search.
  name: PipesHub Web Search API
  slug: pipeshub-web-search-api
artifact_total: 68
asyncapis:
- description: ''
  name: Pipeshub Webhooks
  slug: pipeshub-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/agentic-access/pipeshub-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pipeshub-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/rate-limits/pipeshub-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pipeshub-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/plans/pipeshub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pipeshub-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/rules/pipeshub-rules.yml
  title: ''
  type: Spectral
  url: rules/pipeshub-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/rules/pipeshub-pipeshub-ai-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/pipeshub-pipeshub-ai-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/json-ld/pipeshub-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pipeshub-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/vocabulary/pipeshub-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pipeshub-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/asyncapi/pipeshub-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pipeshub-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/data-model/pipeshub-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pipeshub-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/changelog/pipeshub-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pipeshub-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/conventions/pipeshub-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pipeshub-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/sandbox/pipeshub-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pipeshub-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/lifecycle/pipeshub-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/pipeshub-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/lifecycle/pipeshub-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pipeshub-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/errors/pipeshub-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pipeshub-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/conformance/pipeshub-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pipeshub-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/overlays/pipeshub-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pipeshub-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/llms/pipeshub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pipeshub-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/a2a/pipeshub-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pipeshub-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/mcp/pipeshub-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pipeshub-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/mcp/pipeshub-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pipeshub-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/well-known/pipeshub-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeshub-platform-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/well-known/pipeshub-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pipeshub-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/hosts/pipeshub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pipeshub-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/vendors/pipeshub-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pipeshub-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/packages/pipeshub-packages.yml
  title: ''
  type: SDKs
  url: packages/pipeshub-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/packages/pipeshub-packages.yml
  title: ''
  type: Packages
  url: packages/pipeshub-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/scopes/pipeshub-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/pipeshub-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/authentication/pipeshub-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pipeshub-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/security/pipeshub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pipeshub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pipeshub.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/pipeshub-ai/pipeshub-ai/blob/a883af6d0f5d31f57d07d88dfcb1e9c483343e38/.spectral.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pipeshub.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pipeshub.com/developer/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pipeshub.com/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pipeshub.com/additional-resources/changelog
- group: company
  title: ''
  type: Blog
  url: https://pipeshub.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pipeshub-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://pipeshub.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.pipeshub.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.pipeshub.com/
- group: auth
  title: ''
  type: Security
  url: https://pipeshub.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pipeshub.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pipeshub.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/K5RskzJBm2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pipeshub
- group: other
  title: ''
  type: X
  url: https://x.com/PipesHub
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@PipesHub-GenAI
created: '2026-10-09'
description: PipesHub is an open-source, enterprise-ready workplace AI platform positioned as an open-source alternative to Glean. It unifies scattered business data by connecting to business and enterprise apps, provides explainable, permission-aware enterprise search across them, and powers AI agents that get work done. It can be self-hosted from its public GitHub repository (pipeshub-ai/pipeshub-ai) or used as a hosted app, and documents a developer API reference for building on its enterprise context layer.
image: https://framerusercontent.com/images/87N6FTaGQx1IeB0Klbo9hPHAOus.png
json_schemas:
- name: AgentCreateConversationRequest
  property_count: 17
  slug: pipeshub-agent-create-conversation-request
- name: Conversation
  property_count: 26
  slug: pipeshub-conversation
- name: CreateConversationRequest
  property_count: 17
  slug: pipeshub-create-conversation-request
- name: GetRecordByIdResponseSchema
  property_count: 5
  slug: pipeshub-get-record-by-id-response-schema
- name: KnowledgeHubNodesResponse
  property_count: 11
  slug: pipeshub-knowledge-hub-nodes-response
- name: Record
  property_count: 32
  slug: pipeshub-record
jsonld:
- class_count: 120
  name: Pipeshub Context
  property_count: 279
  slug: pipeshub-context
layout: provider
mcp_servers:
- description: PipesHub exposes a remote MCP endpoint over Streamable HTTP at {PIPESHUB_INSTANCE_URL}/mcp ("no local npm packages or stdio processes needed"), plus an optional local stdio bridge published as the npm
  name: PipesHub MCP Server
  slug: pipeshub-mcp-server
modified: '2026-10-09'
name: PipesHub
nav: Providers
network: true
overview: 'PipesHub publishes 51 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, AI Models Providers API, Authentication Configuration API, and 48 more. Tagged areas include Company, Artificial Intelligence, Enterprise Search, AI Agents, and Open Source.


  The PipesHub catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  PipesHub''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, engineering blog, and 42 more developer resources.'
plans:
- name: Pipeshub Plans Pricing
  plan_count: 2
  slug: pipeshub-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Pipeshub Rate Limits
  slug: pipeshub-rate-limits
rules:
- authorship: provider
  effective_rule_count: 44
  extends:
  - spectral:oas
  name: PipesHub — pipeshub ai rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 1
    info: 0
    warn: 2
  slug: pipeshub-pipeshub-ai-spectral-rules
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: PipesHub API Rules
  rule_count: 19
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 6
  slug: pipeshub-rules
scopes:
- name: Pipeshub Scopes
  scope_count: 43
  slug: pipeshub-scopes
  summary_line: 43 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 72.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 87.3
    catalog_earned_first_party: 26.0
    catalog_gap: 27.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 65.8
    contract_governance: 76.5
    contract_quality: 68.6
    developer_ergonomics: 63.7
    discoverability: 75.0
    operational_transparency: 55.3
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 51
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/pipeshub/refs/heads/main/screenshots/pipeshub-2026-10-11T112606.png
security:
- kind: authentication
  name: Pipeshub Authentication
  slug: pipeshub-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Pipeshub Domain Security
  slug: pipeshub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pipeshub
tags:
- Company
- Artificial Intelligence
- Enterprise Search
- AI Agents
- Open Source
- Knowledge Management
- Workplace AI
website: https://pipeshub.com/
---
