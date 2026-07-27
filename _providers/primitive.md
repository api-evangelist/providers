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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 86.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 76
  human_in_the_loop: 1
  name: Primitive Agentic Access
  operation_count: 129
  slug: primitive-agentic-access
  summary_line: 129 operations · 76 acting · 1 human-in-the-loop
api_count: 22
apis:
- description: Manage your account settings, storage, and webhook secret
  name: Primitive Account API
  slug: primitive-account-api
- description: Agent signup and authentication
  name: Primitive Agent API
  slug: primitive-agent-api
- description: Browser-assisted CLI authentication
  name: Primitive CLI API
  slug: primitive-cli-api
- description: Public, no-account sandbox operations that mirror authenticated endpoints with synthetic data so an agent can learn the request and response shapes before signing up.
  name: Primitive Demo API
  slug: primitive-demo-api
- description: Unauthenticated entry point that lists the API base URL, how to obtain credentials, and the operations callable without a token.
  name: Primitive Discovery API
  slug: primitive-discovery-api
- description: Claim, verify, and manage email domains
  name: Primitive Domains API
  slug: primitive-domains-api
- description: List, inspect, and manage received emails
  name: Primitive Emails API
  slug: primitive-emails-api
- description: Manage webhook endpoints that receive email events
  name: Primitive Endpoints API
  slug: primitive-endpoints-api
- description: Manage whitelist and blocklist filter rules
  name: Primitive Filters API
  slug: primitive-filters-api
- description: 'Deploy JavaScript handlers that run on inbound mail. Each function is a single ESM module whose default export is an object with an async `fetch(request, env)` method, in the shape of a Workers-style '
  name: Primitive Functions API
  slug: primitive-functions-api
- description: Check inbound email setup and processing readiness
  name: Primitive Inbox API
  slug: primitive-inbox-api
- description: Durable org-scoped or function-scoped JSON key-value storage for agents and functions. Keys are caller-defined. Function scope is always addressed by the function id UUID, not by function name.
  name: Primitive Memories API
  slug: primitive-memories-api
- description: 'Collect and pay stablecoin (USDC) payments with x402. Settlement is non-custodial: funds move directly from payer to payee on-chain via an EIP-3009 authorization the payer signs with their own key, an'
  name: Primitive Payments API
  slug: primitive-payments-api
- description: 'The Agent Registry: ownable directories of agents, addressable by a registry-scoped handle. A registry''s publish policy (owner_only, request, or open) decides whether a publish lists immediately or pe'
  name: Primitive Registries API
  slug: primitive-registries-api
- description: 'Recipient routing: route inbound mail to a single destination per recipient address. Rules bind an address pattern (exact or wildcard) to an endpoint; `function_id` routes an address to a function, mi'
  name: Primitive Routes API
  slug: primitive-routes-api
- description: Semantic and hybrid search across received and sent mail
  name: Primitive Search API
  slug: primitive-search-api
- description: Send outbound emails through the Primitive API
  name: Primitive Sending API
  slug: primitive-sending-api
- description: Operational endpoints such as the unauthenticated health/liveness probe.
  name: Primitive Service API
  slug: primitive-service-api
- description: Public Function template registry reads used to browse installable agent templates.
  name: Primitive Templates API
  slug: primitive-templates-api
- description: Conversation threads spanning received and sent emails
  name: Primitive Threads API
  slug: primitive-threads-api
- description: 'Wake scheduling: schedule and send typed wake commands to your own functions over real DKIM-signed email on a cron cadence, and manage the per-target allowlist that authorizes which senders may wake a'
  name: Primitive Wake API
  slug: primitive-wake-api
- description: View and replay webhook delivery attempts
  name: Primitive Webhook Deliveries API
  slug: primitive-webhook-deliveries-api
artifact_total: 28
asyncapis:
- description: ''
  name: Primitive Webhooks
  slug: primitive-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.primitive.dev/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.primitive.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.primitive.dev/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.primitive.dev/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://www.primitive.dev/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.primitive.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.primitive.dev/blog
- group: operate
  title: ''
  type: Support
  url: https://www.primitive.dev/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.primitive.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.primitive.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/primitivedotdev
- group: build
  title: ''
  type: Packages
  url: packages/primitive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/primitive-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/primitive-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/primitive-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/primitive-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/primitive-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/primitive-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/primitive-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/primitive-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/primitive-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/primitive-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/primitive-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/primitive-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/primitive-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/primitive-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/primitive-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/primitive-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/primitive-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/primitive-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/primitive-openapi-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/primitive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/primitive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/primitive-domain-security.yml
created: '2026-07-17'
description: Primitive is email infrastructure built for AI agents. It lets an agent send and receive email with a single authenticated HTTP call — no SMTP credentials, DNS, or mail servers — and hosts each agent at a managed *.primitive.email address that runs a JavaScript handler on every inbound message. The `primitive chat` verb sends a message and returns the threaded reply in one round trip. The v1 REST API (96 paths, 129 operations) covers domains, sending, inbound emails, threads, search, webhook endpoints, filters, routing, hosted Functions, durable Memories, an agent registry, wake scheduling, and non-custodial x402 USDC payments over email. Primitive ships a published hosted MCP server, an A2A agent card, a read-only GraphQL surface, official Node/Python/Go SDKs and a CLI, and a rich agent-native discovery surface (llms.txt, /.well-known/*, packaged Agent Skills). Backed by Y Combinator (Spring 2026).
image: https://www.primitive.dev/web-app-manifest-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: primitive-mcp.yml
  slug: primitive-mcpyml
modified: '2026-07-20'
name: Primitive
nav: Providers
network: true
overview: 'Primitive publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agent API, CLI API, and 19 more. Tagged areas include Email, Email Infrastructure, AI Agents, Agent Infrastructure, and Messaging.


  The Primitive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Primitive''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 28 more developer resources.'
random_paper: 33
score:
  band: developing
  composite: 58.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 71.1
    developer_ergonomics: 87.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 58.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Primitive Authentication
  slug: primitive-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Primitive Domain Security
  slug: primitive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Primitive Vulnerability Disclosure
  slug: primitive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: primitive
tags:
- Email
- Email Infrastructure
- AI Agents
- Agent Infrastructure
- Messaging
- Webhooks
- MCP
- Developer Tools
- API
website: https://www.primitive.dev/developers
---
