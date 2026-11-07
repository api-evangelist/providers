---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 779
  human_in_the_loop: 18
  name: Agentstack Tech Agentic Access
  operation_count: 1541
  slug: agentstack-tech-agentic-access
  summary_line: 1541 operations · 779 acting · 18 human-in-the-loop
api_count: 1
apis:
- description: '8DNA API: GET/POST /api/dna/data — key-value access to project.data.* and user.data.* (alternative to many CRUD routes). See docs/architecture/DNA_KEY_VALUE_API.md.'
  name: AgentStack 8DNA API
  slug: agentstack-tech-8dna-api-api
- description: 'Project admin: status, security, agents. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).'
  name: AgentStack Admin API
  slug: agentstack-tech-admin-api
- description: The admin-drain API from AgentStack — 2 operation(s) for admin-drain.
  name: AgentStack Admin Drain API
  slug: agentstack-tech-admin-drain-api
- description: AgentNet ledger (append-only double-entry SoT in Postgres; 8DNA mirror for UX). See docs/adr/AGENTCOIN_LEDGER_L0_AND_PUBLIC_ANCHORING.md. REST compatibility surface; for new integrations prefer MCP ac
  name: AgentStack Agent Net API
  slug: agentstack-tech-agentnet-api
- description: AgentNet Arbitrum attestation. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack AgentNet Arbitrum API
  slug: agentstack-tech-agentnet-arbitrum-api
- description: AgentNet BNB chain attestation. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack AgentNet BNB API
  slug: agentstack-tech-agentnet-bnb-api
- description: AgentNet chain control (authenticated). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack AgentNet Chain Control API
  slug: agentstack-tech-agentnet-chain-control-api
- description: AgentNet chain control (public). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack AgentNet Chain Control Public API
  slug: agentstack-tech-agentnet-chain-control-public-api
- description: AgentNet PTR proof rails. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack AgentNet PTR API
  slug: agentstack-tech-agentnet-ptr-api
- description: AgentNet Solana attestation. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack AgentNet Solana API
  slug: agentstack-tech-agentnet-solana-api
- description: 'Agents Fleet: templates, runs, promotion gates, traces. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PR'
  name: AgentStack Agents Fleet API
  slug: agentstack-tech-agents-fleet-api
- description: AgentSocial chat, channels, and social graph. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md
  name: AgentStack Agent Social API
  slug: agentstack-tech-agentsocial-api
- description: AI Builder build and generation. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack AI Builder API
  slug: agentstack-tech-ai-builder-api
- description: Analytics and events. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Analytics API
  slug: agentstack-tech-analytics-api
- description: Project API key management. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack API Keys API
  slug: agentstack-tech-api-keys-api
- description: Project digital assets / inventory catalog. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Assets API
  slug: agentstack-tech-assets-api
- description: The auth API from AgentStack — 1 operation(s) for auth.
  name: AgentStack Auth API
  slug: agentstack-tech-auth-api
- description: Login, registration, tokens, OAuth. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Authentication API
  slug: agentstack-tech-authentication-api
- description: Avatars. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Avatars API
  slug: agentstack-tech-avatars-api
- description: Backup management. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Backup Management API
  slug: agentstack-tech-backup-management-api
- description: Batch requests. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Batch API
  slug: agentstack-tech-batch-api
- description: Billing and subscription surfaces. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Billing API
  slug: agentstack-tech-billing-api
- description: 'Bots Fleet: inbound channels, brain router, outbound delivery. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS'
  name: AgentStack Bots API
  slug: agentstack-tech-bots-api
- description: Buffs and subscriptions. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Buffs API
  slug: agentstack-tech-buffs-api
- description: Build queue. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Build Queue API
  slug: agentstack-tech-build-queue-api
- description: 'Business organism: org tree, command snapshot, tariff gates (project-scoped). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see do'
  name: AgentStack Business API
  slug: agentstack-tech-business-api
- description: Capability matrix and fabric capability probes. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.
  name: AgentStack Capabilities API
  slug: agentstack-tech-capabilities-api
- description: Cardgame bootstrap BFF. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Cardgame API
  slug: agentstack-tech-cardgame-api
- description: 'Protein commands: POST /api/commands/execute, batch, dna/{entity}/{op}. Same execution stack as MCP tools commands.execute / commands.execute_batch. Logic Engine client commands may appear here too.'
  name: AgentStack Commands API
  slug: agentstack-tech-commands-api
- description: 'Commerce surfaces: checkout, storefront, seller activation bridges. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHA'
  name: AgentStack Commerce API
  slug: agentstack-tech-commerce-api
- description: The commerce-iap API from AgentStack — 13 operation(s) for commerce-iap.
  name: AgentStack Commerce Iap API
  slug: agentstack-tech-commerce-iap-api
- description: Merchant listings, orders, shelf tools. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Commerce Merchant API
  slug: agentstack-tech-commerce-merchant-api
- description: Buyer-facing shop catalog, cart, coupons. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Commerce Shop API
  slug: agentstack-tech-commerce-shop-api
- description: CRM contacts, deals, pipeline, and contact 360 (project-scoped). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNE
  name: AgentStack CRM API
  slug: agentstack-tech-crm-api
- description: Project dashboard overview. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Dashboard API
  slug: agentstack-tech-dashboard-api
- description: 'Field Access Policy (FAP): /api/data-access/* — declarative field policy, triggers, templates.'
  name: AgentStack Data Access API
  slug: agentstack-tech-dataaccess-api
- description: Public capability discovery. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Discovery API
  slug: agentstack-tech-discovery-api
- description: Ecosystem-scoped project helpers. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Ecosystem API
  slug: agentstack-tech-ecosystem-api
- description: Energy (resources). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Energy API
  slug: agentstack-tech-energy-api
- description: 'Managed fabric: context, capabilities, federation, ops, triggers. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANN'
  name: AgentStack Fabric API
  slug: agentstack-tech-fabric-api
- description: Files and storage. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Files API
  slug: agentstack-tech-files-api
- description: Finance BFF and treasury helpers. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Finance API
  slug: agentstack-tech-finance-api
- description: Global asset registry. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Global Assets API
  slug: agentstack-tech-global-assets-api
- description: In-product guidance / compass hints. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Guidance API
  slug: agentstack-tech-guidance-api
- description: Service health and metrics.
  name: AgentStack Health & Metrics API
  slug: agentstack-tech-health-metrics-api
- description: 'Hosted static sites: publish, promote, rollback, /s/ URLs. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND'
  name: AgentStack Hosting API
  slug: agentstack-tech-hosting-api
- description: 'Integration Hub: recipes, inbound hooks, outbound connectors. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_'
  name: AgentStack Integrations API
  slug: agentstack-tech-integrations-api
- description: Invoices. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Invoices API
  slug: agentstack-tech-invoices-api
- description: The Knowledge API from AgentStack — 50 operation(s) for knowledge.
  name: AgentStack Knowledge API
  slug: agentstack-tech-knowledge-api
- description: Rules engine (logic rules). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Logic Engine API
  slug: agentstack-tech-logic-engine-api
- description: Logic templates. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Logic Templates API
  slug: agentstack-tech-logic-templates-api
- description: Marketplace listings and discovery. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Marketplace API
  slug: agentstack-tech-marketplace-api
- description: Matchmaking. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Matchmaking API
  slug: agentstack-tech-matchmaking-api
- description: 'Model Context Protocol: POST /mcp (agentstack.execute), GET /mcp/actions (action catalog), GET /mcp/discovery. Preferred entry for AI agents (Cursor, Claude, VS Code, …).'
  name: AgentStack MCP API
  slug: agentstack-tech-mcp-api
- description: Neural Architecture API. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Neural Architecture API
  slug: agentstack-tech-neural-architecture-api
- description: Notifications and settings. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Notifications API
  slug: agentstack-tech-notifications-api
- description: OAuth 2.1 admin. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack OAuth 2.1 Admin API
  slug: agentstack-tech-oauth-2-1-admin-api
- description: OAuth 2.1. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack OAuth 2.1 API
  slug: agentstack-tech-oauth-2-1-api
- description: CSP reports, OpTrace, and ops telemetry. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Observability API
  slug: agentstack-tech-observability-api
- description: OpTrace metrics and spans. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Op Trace API
  slug: agentstack-tech-optrace-api
- description: Payments and transactions (SDK list; source of truth — data_projects_transaction). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (s
  name: AgentStack Payments API
  slug: agentstack-tech-payments-api
- description: Permissions. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Permissions API
  slug: agentstack-tech-permissions-api
- description: Platform feature flags and meta. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Platform API
  slug: agentstack-tech-platform-api
- description: Principal access policy helpers. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Principal Access API
  slug: agentstack-tech-principalaccess-api
- description: Profile, wallets, avatars, convenience aliases. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.
  name: AgentStack Profile API
  slug: agentstack-tech-profile-api
- description: 'Current project: API keys, wallets, notifications, members. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AN'
  name: AgentStack Project API
  slug: agentstack-tech-project-api
- description: Project files. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Project Files API
  slug: agentstack-tech-project-files-api
- description: The project-orchestrator API from AgentStack — 20 operation(s) for project-orchestrator.
  name: AgentStack Project Orchestrator API
  slug: agentstack-tech-project-orchestrator-api
- description: 'Projects: list, settings, members. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).'
  name: AgentStack Projects API
  slug: agentstack-tech-projects-api
- description: Proxy to external services. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Proxy API
  slug: agentstack-tech-proxy-api
- description: Public commerce lite endpoints. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Public commerce lite API
  slug: agentstack-tech-public-commerce-lite-api
- description: Demo hosting claim and try flows. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Public demo hosting API
  slug: agentstack-tech-public-demo-hosting-api
- description: The Public form intake API from AgentStack — 1 operation(s) for public form intake.
  name: AgentStack Public form intake API
  slug: agentstack-tech-public-form-intake-api
- description: Public grants demo surfaces. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Public grants API
  slug: agentstack-tech-public-grants-api
- description: Unauthenticated hosting surfaces. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Public hosting API
  slug: agentstack-tech-public-hosting-api
- description: The Public services offers API from AgentStack — 4 operation(s) for public services offers.
  name: AgentStack Public services offers API
  slug: agentstack-tech-public-services-offers-api
- description: Public showcase catalogs. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Public showcase API
  slug: agentstack-tech-public-showcase-api
- description: RAG collections, documents, semantic search, and long-term memory. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHAN
  name: AgentStack RAG API
  slug: agentstack-tech-rag-api
- description: Roles and access (RBAC). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack RBAC API
  slug: agentstack-tech-rbac-api
- description: Sandbox and playground APIs. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Sandbox API
  slug: agentstack-tech-sandbox-api
- description: Scheduler tasks. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Scheduler API
  slug: agentstack-tech-scheduler-api
- description: SEO and metadata. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack SEO API
  slug: agentstack-tech-seo-api
- description: User and project sessions. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Sessions API
  slug: agentstack-tech-sessions-api
- description: Shell hub bootstrap for dual-shell SPA. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Shell Hub API
  slug: agentstack-tech-shell-hub-api
- description: Stream/Relay. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Stream/Relay API
  slug: agentstack-tech-stream-relay-api
- description: Project support channels, staff inbox, tickets (psup). REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PRO
  name: AgentStack Support API
  slug: agentstack-tech-support-api
- description: Unified webhooks and client API. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack Unified API
  slug: agentstack-tech-unified-api-api
- description: User AI settings. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack User AI Settings API
  slug: agentstack-tech-user-ai-settings-api
- description: User profile, sessions, user API keys. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCOLS.md).
  name: AgentStack User API
  slug: agentstack-tech-user-api
- description: Outbound webhook registration and delivery status. REST compatibility surface; for new integrations prefer MCP actions, GET/POST /api/dna/data, or POST /api/commands (see docs/API_CHANNELS_AND_PROTOCO
  name: AgentStack Webhooks API
  slug: agentstack-tech-webhooks-api
artifact_total: 106
asyncapis:
- description: ''
  name: Agentstack Tech Webhooks
  slug: agentstack-tech-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/agentstack-tech/agentic-access/agentstack-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentstack-tech-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentstack-tech/rules/agentstack-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/agentstack-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/agentstack-tech/json-ld/agentstack-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentstack-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentstack-tech/vocabulary/agentstack-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentstack-tech-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentstack-tech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentstack-tech/asyncapi/agentstack-tech-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agentstack-tech-webhooks.yml
- group: design
  href: https://artifacts.apis.io/agentstack-tech/data-model/agentstack-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentstack-tech-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentstack-tech/conventions/agentstack-tech-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentstack-tech-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentstack-tech/conventions/agentstack-tech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentstack-tech-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agentstack.tech/trust
- group: auth
  href: https://artifacts.apis.io/agentstack-tech/security/agentstack-tech-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentstack-tech-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/agentstack-tech/errors/agentstack-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentstack-tech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentstack-tech/conformance/agentstack-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentstack-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentstack-tech/llms/agentstack-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentstack-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentstack-tech/mcp/agentstack-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentstack-tech-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentstack-tech/well-known/agentstack-tech-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentstack-tech-security.txt
- group: auth
  href: https://artifacts.apis.io/agentstack-tech/well-known/agentstack-tech-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentstack-tech-api-security.txt
- group: agent
  href: https://artifacts.apis.io/agentstack-tech/well-known/agentstack-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentstack-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentstack-tech/hosts/agentstack-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentstack-tech-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentstack.tech/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentstack.tech/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://agentstack.tech/pricing
- group: start
  title: ''
  type: Login
  url: https://agentstack.tech/login
- group: auth
  href: https://artifacts.apis.io/agentstack-tech/authentication/agentstack-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentstack-tech-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agentstack-tech/security/agentstack-tech-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agentstack-tech-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agentstack-tech/security/agentstack-tech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentstack-tech-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentstack-tech/security/agentstack-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentstack-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentstack.tech/
created: '2026-11-01'
description: 'agentstack-tech is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://agentstack.tech/og/acquisition.png
json_schemas:
- name: ContentMetadataPatch
  property_count: 17
  slug: agentstack-tech-content-metadata-patch
- name: CreatePaymentRequest
  property_count: 23
  slug: agentstack-tech-create-payment-request
- name: GenerationSettingsPatch
  property_count: 16
  slug: agentstack-tech-generation-settings-patch
- name: KnowledgeConfigPatch
  property_count: 38
  slug: agentstack-tech-knowledge-config-patch
- name: PlanClaimResponse
  property_count: 22
  slug: agentstack-tech-plan-claim-response
- name: ProjectDataPatchBody
  property_count: 12
  slug: agentstack-tech-project-data-patch-body
jsonld:
- class_count: 120
  name: Agentstack Tech Context
  property_count: 292
  slug: agentstack-tech-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentstack.tech requiring an API key.
  name: AgentStack MCP Server
  slug: agentstack-tech-mcp-yml
modified: '2026-11-01'
name: AgentStack
nav: Providers
network: true
overview: 'AgentStack publishes 90 API contracts indexed on the [APIs.io](https://apis.io/) network, including 8DNA API, Admin API, Admin Drain API, and 87 more. Tagged areas include Company.


  The AgentStack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AgentStack''s developer surface includes pricing, authentication, and 26 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AgentStack API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: agentstack-tech-rules
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 65.6
    developer_ergonomics: 18.3
    discoverability: 40.0
    operational_transparency: 18.4
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 90
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentstack Tech Authentication
  slug: agentstack-tech-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Agentstack Tech Domain Security
  slug: agentstack-tech-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agentstack Tech Vulnerability Disclosure
  slug: agentstack-tech-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Agentstack Tech Trust Center
  slug: agentstack-tech-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: billing-health
  slug: agentstack-tech-billing-health
slug: agentstack-tech
tags:
- Company
website: https://agentstack.tech/
---
