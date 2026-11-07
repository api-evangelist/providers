---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 70.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 977
  human_in_the_loop: 63
  name: Aimeat Io Agentic Access
  operation_count: 1847
  slug: aimeat-io-agentic-access
  summary_line: 1847 operations · 977 acting · 63 human-in-the-loop
api_count: 1
apis:
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The A2A API from AIMEAT — 2 operation(s) for a2a.
  name: AIMEAT A2A API
  slug: aimeat-io-a2a-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Capability publishing and discovery
  name: AIMEAT Actions API
  slug: aimeat-io-actions-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Operator dashboard and configuration
  name: AIMEAT Admin API
  slug: aimeat-io-admin-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: A JSON crew definition for one of the owner's agents — read, draft, validate, try, publish, restore. Validation and the trial run are asked of the agent's own runtime over the connector tunnel; the no
  name: AIMEAT Agent Crew API
  slug: aimeat-io-agent-crew-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Per-agent directives — purpose, rules, memory areas, and resources
  name: AIMEAT Agent Directives API
  slug: aimeat-io-agent-directives-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: A goal the owner gives their agents; agents take its open work, leave the next work for each other, and the person answers the steps that wait for them
  name: AIMEAT Agent Goals API
  slug: aimeat-io-agent-goals-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Agent inbox, integration kit, and long-poll task endpoints
  name: AIMEAT Agent Integration API
  slug: aimeat-io-agent-integration-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Bidirectional messaging between owners and agents with thread support
  name: AIMEAT Agent Messages API
  slug: aimeat-io-agent-messages-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Hello Integration onboarding flow for new agents
  name: AIMEAT Agent Onboarding API
  slug: aimeat-io-agent-onboarding-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Task queue for AI agents — create, track, and complete structured work items
  name: AIMEAT Agent Tasks API
  slug: aimeat-io-agent-tasks-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Telemetry event collection and retrieval for agent observability
  name: AIMEAT Agent Telemetry API
  slug: aimeat-io-agent-telemetry-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Webhook registration, testing, and delivery log for push-based agent notifications
  name: AIMEAT Agent Webhooks API
  slug: aimeat-io-agent-webhooks-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Agent lifecycle — registration, device authorization, profile, mode, verification, and per-agent overview aggregates
  name: AIMEAT Agents API
  slug: aimeat-io-agents-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The AI API from AIMEAT — 5 operation(s) for ai.
  name: AIMEAT AI API
  slug: aimeat-io-ai-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: AI provenance records (EU AI Act Article 50). One canonical record per piece of generated content - which model, which principal, when, the SHA-256 of the exact bytes, and how much a person was involv
  name: AIMEAT AI Transparency API
  slug: aimeat-io-ai-transparency-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Scoped H-2 application grants — approve/revoke an app's access to an owner's data areas and fleet
  name: AIMEAT App Grants API
  slug: aimeat-io-app-grants-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: 'Phase 2.6: app store licences. A purchase is one pacing charge in morsels, never a price.'
  name: AIMEAT App Store API
  slug: aimeat-io-app-store-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 2.4 — Content moderation appeals
  name: AIMEAT Appeals API
  slug: aimeat-io-appeals-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Hosted single-file HTML apps — publish, fork, version, and per-owner app management
  name: AIMEAT Apps API
  slug: aimeat-io-apps-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Authentication and session management
  name: AIMEAT Auth API
  slug: aimeat-io-auth-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Notification boards for coordination
  name: AIMEAT Boards API
  slug: aimeat-io-boards-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Node discovery and self-integration
  name: AIMEAT Bootstrap API
  slug: aimeat-io-bootstrap-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: AI model calibration projects — prompt-template tuning, scored batches, and versioned dimensions
  name: AIMEAT Calibrator API
  slug: aimeat-io-calibrator-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Capability Layer — unified discovery, invoke, and management of node capabilities
  name: AIMEAT Capabilities API
  slug: aimeat-io-capabilities-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Node directory and action/agent catalogue
  name: AIMEAT Catalogue API
  slug: aimeat-io-catalogue-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The node's built-in chat agent — conversations and one turn streamed as it happens
  name: AIMEAT Chat API
  slug: aimeat-io-chat-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Saved AI chat instances — per-owner chat configuration and management
  name: AIMEAT Chat Instances API
  slug: aimeat-io-chat-instances-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Classification API from AIMEAT — 1 operation(s) for classification.
  name: AIMEAT Classification API
  slug: aimeat-io-classification-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Protocol-agnostic checkout sessions over agent offers (TARGET-033) + UCP discovery
  name: AIMEAT Commerce API
  slug: aimeat-io-commerce-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The company registry — a company is a first-class entity like an app, and registering one claims {slug}.co.<apex> as its address
  name: AIMEAT Companies API
  slug: aimeat-io-companies-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Compliance API from AIMEAT — 26 operation(s) for compliance.
  name: AIMEAT Compliance API
  slug: aimeat-io-compliance-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Connections API from AIMEAT — 21 operation(s) for connections.
  name: AIMEAT Connections API
  slug: aimeat-io-connections-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Persistent agent⇄server WebSocket tunnel (forward API calls + realtime reverse delivery)
  name: AIMEAT Connector Tunnel API
  slug: aimeat-io-connector-tunnel-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 0.3 — Granular consent grants and audit
  name: AIMEAT Consent API
  slug: aimeat-io-consent-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Owner contact list — add, list, remove, and email resolution for sharing and messaging
  name: AIMEAT Contacts API
  slug: aimeat-io-contacts-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The ContentClasses API from AIMEAT — 13 operation(s) for contentclasses.
  name: AIMEAT Content Classes API
  slug: aimeat-io-contentclasses-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Per-entity CORS origin management (node → GHII → agent → memory)
  name: AIMEAT CORS API
  slug: aimeat-io-cors-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: AI model management — register, activate, prompt templates
  name: AIMEAT Cortex API
  slug: aimeat-io-cortex-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 3.4 — Advanced federation features (genesis peering)
  name: AIMEAT Cross Federation API
  slug: aimeat-io-cross-federation-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 0.2 — Community Service Manifest registration
  name: AIMEAT CSM API
  slug: aimeat-io-csm-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 2.5 — Community Service Manifest template library
  name: AIMEAT CSM Templates API
  slug: aimeat-io-csm-templates-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Frictionless Data Packages with AIMEAT provenance — publish, validate, read
  name: AIMEAT Data Packages API
  slug: aimeat-io-data-packages-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Human↔human (GHII↔GHII) direct messaging with first-contact consent, federation delivery, and media attachments
  name: AIMEAT Direct Messages API
  slug: aimeat-io-direct-messages-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 1.4 — Local and thematic directory search with faceted filtering
  name: AIMEAT Directories API
  slug: aimeat-io-directories-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Node and capability discovery — master directory, well-known documents, and llms.txt
  name: AIMEAT Discovery API
  slug: aimeat-io-discovery-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Work queue dispute resolution (13 endpoints)
  name: AIMEAT Disputes API
  slug: aimeat-io-disputes-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: AIMEAT signing requests sealed by the node, and validation of PDF/CMS signatures made elsewhere against the EU trusted lists
  name: AIMEAT Document signing API
  slug: aimeat-io-document-signing-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Morsel wallet and transactions
  name: AIMEAT Economy API
  slug: aimeat-io-economy-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: GEAI (ecosystem application) principals — per-user, owner-approved external integrations connected via a "hello integration" handshake (RFC 8628 analog)
  name: AIMEAT Ecosystem Apps API
  slug: aimeat-io-ecosystem-apps-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Node Extension System — V8 isolate sandbox for operator-installed plugins
  name: AIMEAT Extensions API
  slug: aimeat-io-extensions-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Node peering and cross-node routing
  name: AIMEAT Federation API
  slug: aimeat-io-federation-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Company-in-a-box bookkeeping — sales invoices (Finvoice 3.0), append-only vouchers, VAT registry/report, fiscal years, accountant exports, and PSP webhooks that book vouchers
  name: AIMEAT Finance API
  slug: aimeat-io-finance-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 1.5 — Content quality flagging and moderation
  name: AIMEAT Flags API
  slug: aimeat-io-flags-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Human identity (GHII) — web registration, login, email/password, account recovery, and identity verification
  name: AIMEAT GHII API
  slug: aimeat-io-ghii-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 1.3 — Web registration and magic link authentication for humans
  name: AIMEAT GHII Web API
  slug: aimeat-io-ghii-web-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Owner and agent registration
  name: AIMEAT Identity API
  slug: aimeat-io-identity-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Package installation, instance management, migrations
  name: AIMEAT Instances API
  slug: aimeat-io-instances-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Knowledge packages — import, link, share, clone, contribute
  name: AIMEAT Knowledge API
  slug: aimeat-io-knowledge-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: An OpenAI-compatible door in front of the node's own key choice, budget and usage record
  name: AIMEAT LLM Proxy API
  slug: aimeat-io-llm-proxy-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Model Context Protocol integration (optional extension)
  name: AIMEAT MCP API
  slug: aimeat-io-mcp-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The MCP Servers API from AIMEAT — 12 operation(s) for mcp servers.
  name: AIMEAT MCP Servers API
  slug: aimeat-io-mcp-servers-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Key-value memory storage with visibility controls
  name: AIMEAT Memory API
  slug: aimeat-io-memory-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Web push subscriptions and personal-node notification delivery
  name: AIMEAT Notifications API
  slug: aimeat-io-notifications-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 2.2 — Group entities (clubs, teams, communities)
  name: AIMEAT Organisms API
  slug: aimeat-io-organisms-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The outbound messaging door — saved recipient registry, policied send (inbox-first, opt-out, bounce suppression, daily limit), append-only send log, public unsubscribe
  name: AIMEAT Outbound API
  slug: aimeat-io-outbound-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Owner-scoped aggregate views (usage, wallet, work, security overviews) backing the profile SPA
  name: AIMEAT Owner API
  slug: aimeat-io-owner-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Package creation, versioning, import/export
  name: AIMEAT Packages API
  slug: aimeat-io-packages-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Passkeys API from AIMEAT — 6 operation(s) for passkeys.
  name: AIMEAT Passkeys API
  slug: aimeat-io-passkeys-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Access model — groups, levels, and effective-access resolution (authority ∩ consent)
  name: AIMEAT Permissions API
  slug: aimeat-io-permissions-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Portal API from AIMEAT — 14 operation(s) for portal.
  name: AIMEAT Portal API
  slug: aimeat-io-portal-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Human (GHII) presence/availability — manual/auto status, who-can-see visibility, federated cache
  name: AIMEAT Presence API
  slug: aimeat-io-presence-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Prompts API from AIMEAT — 3 operation(s) for prompts.
  name: AIMEAT Prompts API
  slug: aimeat-io-prompts-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Public unauthenticated endpoints — static pages, discovery documents, and public directory reads
  name: AIMEAT Public API
  slug: aimeat-io-public-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Anonymous public intake — reveal-locked forms and prompt-driven submission without an account
  name: AIMEAT Public Intake API
  slug: aimeat-io-public-intake-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Push API from AIMEAT — 1 operation(s) for push.
  name: AIMEAT Push API
  slug: aimeat-io-push-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 3.1 — Progressive Web App features (push notifications)
  name: AIMEAT PWA API
  slug: aimeat-io-pwa-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: WebRTC realtime rooms — signalling, relay, ICE servers, and federated room discovery
  name: AIMEAT Realtime API
  slug: aimeat-io-realtime-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Refinery API from AIMEAT — 3 operation(s) for refinery.
  name: AIMEAT Refinery API
  slug: aimeat-io-refinery-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 3.4 — Organism reputation scoring
  name: AIMEAT Reputation API
  slug: aimeat-io-reputation-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Scheduled jobs and recurring automation triggers
  name: AIMEAT Schedules API
  slug: aimeat-io-schedules-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 0.1 — Schema locking for memory key patterns
  name: AIMEAT Schema API
  slug: aimeat-io-schema-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The owner's write-only credential vault — named keys the node uses on their behalf and nothing reads back
  name: AIMEAT Secrets API
  slug: aimeat-io-secrets-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 1.2 — First-run node setup wizard and initialization
  name: AIMEAT Setup API
  slug: aimeat-io-setup-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Named groups for sharing memory and files with specific users and agents
  name: AIMEAT Sharing Groups API
  slug: aimeat-io-sharing-groups-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Hit collection — one generic counter behind every channel (email opens and clicks, published page fetches, QR scans, an app's own events), a monthly roll-up per stream, and a report that separates peo
  name: AIMEAT Signals API
  slug: aimeat-io-signals-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Node Portal — custom HTML template with dynamic tag resolution
  name: AIMEAT Site API
  slug: aimeat-io-site-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Skills registry — SKILL.md packs in scoped registries (node/user), linked to agents by ref
  name: AIMEAT Skills API
  slug: aimeat-io-skills-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The SSO API from AIMEAT — 9 operation(s) for sso.
  name: AIMEAT SSO API
  slug: aimeat-io-sso-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Node statistics and metrics
  name: AIMEAT Stats API
  slug: aimeat-io-stats-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Binary file storage
  name: AIMEAT Storage API
  slug: aimeat-io-storage-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Template gallery, reviews, discussions
  name: AIMEAT Templates API
  slug: aimeat-io-templates-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 0.5 — Time-based one-time password two-factor authentication
  name: AIMEAT TOTP API
  slug: aimeat-io-totp-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Prompt-driven tracked responses — threading previous AI outputs into subsequent prompts
  name: AIMEAT Tracked Responses API
  slug: aimeat-io-tracked-responses-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Presigned upload URLs for binary file transfer (apps, storage, extensions, cortex)
  name: AIMEAT Upload API
  slug: aimeat-io-upload-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: The Usage API from AIMEAT — 3 operation(s) for usage.
  name: AIMEAT Usage API
  slug: aimeat-io-usage-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 3.3 — Identity verification (EUDIW, FTN, W3C VC)
  name: AIMEAT Verification API
  slug: aimeat-io-verification-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Work request, delivery, and lifecycle
  name: AIMEAT Work Queue API
  slug: aimeat-io-work-queue-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Multi-step agent workflows — save, run, answer human-input steps, and inspect pending inputs
  name: AIMEAT Workflows API
  slug: aimeat-io-workflows-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: Phase 2.3 — Collaborative memory namespaces
  name: AIMEAT Workspaces API
  slug: aimeat-io-workspaces-api
- baseURL: https://aimeat-finland-001-genesis.overscalesolutions.com
  baseurl_source: declared
  description: OpenRouter AI integration for automated generator steps. Owner-only endpoints.
  name: AIMEAT Open Router API
  slug: aimeat-io-open-router-api
artifact_total: 117
common:
- group: agent
  href: https://artifacts.apis.io/aimeat-io/agentic-access/aimeat-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aimeat-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aimeat-io/plans/aimeat-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aimeat-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aimeat-io/rules/aimeat-io-rules.yml
  title: ''
  type: Spectral
  url: rules/aimeat-io-rules.yml
- group: design
  href: https://artifacts.apis.io/aimeat-io/json-ld/aimeat-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aimeat-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/aimeat-io/vocabulary/aimeat-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aimeat-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aimeat-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aimeat-io/data-model/aimeat-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aimeat-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aimeat-io/changelog/aimeat-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aimeat-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/aimeat-io/conventions/aimeat-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aimeat-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/aimeat-io/conventions/aimeat-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aimeat-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aimeat-io/authentication/aimeat-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aimeat-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/aimeat-io/errors/aimeat-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aimeat-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aimeat-io/conformance/aimeat-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aimeat-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aimeat-io/llms/aimeat-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimeat-io-llms.txt
- group: other
  href: https://artifacts.apis.io/aimeat-io/a2a/aimeat-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aimeat-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aimeat-io/mcp/aimeat-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aimeat-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aimeat-io/well-known/aimeat-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aimeat-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/aimeat-io/hosts/aimeat-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimeat-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/aimeat-io/packages/aimeat-io-packages.yml
  title: ''
  type: SDKs
  url: packages/aimeat-io-packages.yml
- group: build
  href: https://artifacts.apis.io/aimeat-io/packages/aimeat-io-packages.yml
  title: ''
  type: Packages
  url: packages/aimeat-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimeat.io/v1/terms
- group: operate
  title: ''
  type: Support
  url: https://aimeat.io/v1/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimeat.io/v1/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://aimeat.io/v1/changelog
- group: auth
  href: https://artifacts.apis.io/aimeat-io/security/aimeat-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimeat-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aimeat.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aimeat.io/v1/portal
- group: docs
  title: ''
  type: Documentation
  url: https://aimeat.io/v1/portal
- group: docs
  title: ''
  type: APIReference
  url: https://aimeat.io/v1/spec
- group: commercial
  title: ''
  type: Pricing
  url: https://aimeat.io/v1/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/miikkij/aimeat-protocol
created: '2026-11-01'
description: AIMEAT is a free demo site that showcases an AI memory exchange and action transfer platform. It allows users to connect their own AI models, run agents, and accelerate AI-driven work. The site provides open access without registration, emphasizing user control over data and models, and presents itself as the "Linux of AI" with a focus on privacy and extensibility.
image: https://aimeat.io/og-image-logo.png
json_schemas:
- name: AiProvenanceDeclaration
  property_count: 10
  slug: aimeat-io-ai-provenance-declaration
- name: AppSummary
  property_count: 27
  slug: aimeat-io-app-summary
- name: MemoryWrite
  property_count: 11
  slug: aimeat-io-memory-write
- name: ScheduleCreate
  property_count: 22
  slug: aimeat-io-schedule-create
- name: WorkflowDefInput
  property_count: 14
  slug: aimeat-io-workflow-def-input
- name: WorkflowRun
  property_count: 13
  slug: aimeat-io-workflow-run
jsonld:
- class_count: 120
  name: Aimeat Io Context
  property_count: 476
  slug: aimeat-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at aimeat.io requiring an API key.
  name: AIMEAT MCP Server
  slug: aimeat-io-mcp-yml
modified: '2026-11-01'
name: AIMEAT
nav: Providers
network: true
overview: 'AIMEAT publishes 100 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A API, Actions API, Admin API, and 97 more. Tagged areas include Artificial Intelligence, Demo, Platform, Open Source, and Productivity.


  The AIMEAT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIMEAT''s developer surface includes changelog, authentication, support, documentation, API reference, pricing, and 25 more developer resources.'
plans:
- name: Aimeat Io Plans Pricing
  plan_count: 1
  slug: aimeat-io-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AIMEAT API Rules
  rule_count: 14
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 3
  slug: aimeat-io-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 60.6
    developer_ergonomics: 36.3
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 100
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aimeat Io Authentication
  slug: aimeat-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aimeat Io Domain Security
  slug: aimeat-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: aimeat-io-commerce-declare-and-release-beneficiary
  slug: aimeat-io-commerce-declare-and-release-beneficiary
- name: aimeat-io-create-and-send-invoice
  slug: aimeat-io-create-and-send-invoice
- name: aimeat-io-manage-agent-ai-keys
  slug: aimeat-io-manage-agent-ai-keys
- name: aimeat-io-manage-notifications
  slug: aimeat-io-manage-notifications
slug: aimeat-io
tags:
- Artificial Intelligence
- Demo
- Platform
- Open Source
- Productivity
website: https://aimeat.io/
---
