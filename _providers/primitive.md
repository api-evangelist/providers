---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-03'
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
artifact_total: 27
asyncapis:
- description: ''
  name: Primitive Webhooks
  slug: primitive-webhooks
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/primitive-a2a.yml
created: '2026-07-17'
description: Primitive is a company surfaced as a portfolio company of y-combinator and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
modified: '2026-07-17'
name: Primitive
nav: Providers
network: true
overview: 'Primitive publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agent API, CLI API, and 19 more. Tagged areas include Company.


  The Primitive catalog on APIs.io includes 1 event-driven AsyncAPI specification.'
random_paper: 35
score:
  band: emerging
  composite: 27.0
  delta: 0.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 77.3
    developer_ergonomics: 0.0
    discoverability: 51.9
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
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
- Company
---
