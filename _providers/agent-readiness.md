---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 15
apis:
- description: An open JSON-RPC protocol that lets AI agents talk to tools, resources, and prompts through a uniform server surface. MCP is the most direct expression of "an API designed for an agent" — every API su
  name: Model Context Protocol (MCP)
  slug: model-context-protocol
- description: The dominant machine-readable contract for HTTP APIs. Presence of a public OpenAPI document — with examples, error schemas, security schemes, and rate-limit headers — is the single highest-leverage ag
  name: OpenAPI Specification
  slug: openapi-initiative
- description: Machine-readable contract for event-driven APIs (webhooks, message brokers, streaming). Agent-readiness for event surfaces depends on whether the provider ships an AsyncAPI document so agents can subs
  name: AsyncAPI Specification
  slug: asyncapi-initiative
- description: 'The vocabulary that lets an agent validate request and response bodies against typed contracts. Published JSON Schemas (independent of, or embedded in, an OpenAPI) are a strong agent-readiness signal '
  name: JSON Schema
  slug: json-schema
- description: A community schema for publishing operational instructions an agent should follow when using a site or API. A provider that ships a `/skills/` directory with a skill index is signalling that it has th
  name: Agent Skills
  slug: agent-skills
- description: RFC 9727 defines `/.well-known/api-catalog` as the canonical machine entrypoint for discovering an organization's APIs, formatted as an RFC 9264 linkset. Presence of a catalog at this path is one of t
  name: /.well-known/api-catalog (RFC 9727)
  slug: well-known-api-catalog
- description: A cryptographic signature scheme for HTTP messages, used by the emerging web-bot-auth profile to let agents authenticate themselves to origins. Provider support for verifying or surfacing RFC 9421 sig
  name: HTTP Message Signatures (RFC 9421)
  slug: rfc-9421-http-message-signatures
- description: 'IETF draft layering an "identified bot" profile on top of RFC 9421. A provider that publishes a directory of verified agent identities — or surfaces Web Bot Auth verdicts in its responses — is making '
  name: Web Bot Auth (draft)
  slug: web-bot-auth
- description: 'The IETF AIPREF working group''s effort to standardise machine-readable AI usage preferences (e.g. `Content-Usage: ai-input=y, ai-train=n`). A provider that publishes explicit AIPREF signals is making '
  name: Content-Usage / AIPREF (IETF AIPREF WG)
  slug: content-usage-aipref
- description: Cloudflare's `Content-Signal` robots.txt directive, complementing the AIPREF drafts. Together they let an origin separate "crawl for search" from "use for AI input" from "use for AI training" — a conc
  name: Cloudflare Content Signals
  slug: cloudflare-content-signals
- description: The APIs.json format describes a provider's API portfolio in one machine-readable document. Publishing `/apis.json` (or `/apis.yml`) at the site root is the agent-readiness equivalent of a site identi
  name: APIs.json
  slug: apis-json
- description: Identity layer on top of OAuth 2.0. Agent-readiness for authenticated APIs depends on clear, discoverable OIDC metadata (`/.well-known/openid-configuration`) so agents can negotiate auth without readi
  name: OpenID Connect
  slug: openid-connect
- description: Reference provider for the agent-readiness signal set. Stripe publishes its full OpenAPI, ships idempotency keys, surfaces rate-limit headers, has a consistent error envelope, and exposes a status pag
  name: Stripe API (reference provider)
  slug: stripe-api
- description: Reference provider with arguably the most extensively-tooled developer surface on the web. Public OpenAPI, GraphQL schema, webhooks, conditional requests, explicit `X-RateLimit-*` headers, status page
  name: GitHub REST + GraphQL API (reference provider)
  slug: github-rest-api
- description: Reference provider with strong agent-readiness signals on the messaging side — published OpenAPI, idempotency on resource creation, structured error codes, signed webhooks, status page, and SDKs in ev
  name: Twilio API (reference provider)
  slug: twilio-api
artifact_total: 43
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agent-readiness-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agent-readiness-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/api-evangelist/agent-readiness
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/api-evangelist/agent-readiness/blob/main/README.md
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/agent-readiness-signal-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/agent-readiness-provider-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/agent-readiness-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agent-readiness-vocabulary.yaml
created: '2026-05-22'
description: A topic index covering the operational practices, signals, and patterns that make an API surface safely usable by autonomous AI agents rather than only by humans. Catalogs the specifications, identity layers, agent skill formats, and edge-layer signals that combine into a coherent agent-readiness posture, with a dimension model, JSON Schema, JSON-LD context, vocabulary, and example signal records for representative providers.
examples:
- key_count: 10
  name: Agent Readiness Provider Stripe Example
  slug: agent-readiness-provider-stripe-example
- key_count: 12
  name: Agent Readiness Signal Cloudflare Well Known Catalog Example
  slug: agent-readiness-signal-cloudflare-well-known-catalog-example
- key_count: 12
  name: Agent Readiness Signal Github Example
  slug: agent-readiness-signal-github-example
- key_count: 12
  name: Agent Readiness Signal Github Mcp Example
  slug: agent-readiness-signal-github-mcp-example
- key_count: 12
  name: Agent Readiness Signal Memesio Well Known Catalog Example
  slug: agent-readiness-signal-memesio-well-known-catalog-example
- key_count: 12
  name: Agent Readiness Signal Merge Well Known Catalog Example
  slug: agent-readiness-signal-merge-well-known-catalog-example
- key_count: 12
  name: Agent Readiness Signal Stripe Example
  slug: agent-readiness-signal-stripe-example
- key_count: 12
  name: Agent Readiness Signal Stripe Idempotency Example
  slug: agent-readiness-signal-stripe-idempotency-example
- key_count: 12
  name: Agent Readiness Signal Twilio Example
  slug: agent-readiness-signal-twilio-example
- key_count: 12
  name: Agent Readiness Signal Zuplo Well Known Catalog Example
  slug: agent-readiness-signal-zuplo-well-known-catalog-example
features:
- description: A nine-dimension scoring model covering specs, auth, idempotency, error semantics, rate-limit headers, dry-run, examples, MCP, and event contracts
  name: Dimension Model
- description: JSON Schema describing a single agent-readiness signal (provider, dimension, score, evidence URL)
  name: Signal Schema
- description: JSON Schema for a provider-level aggregate of signals across dimensions
  name: Provider Aggregate
- description: A JSON-LD context aligning agent-readiness signals with schema.org and common API vocabularies
  name: JSON-LD Context
- description: Example signal records for Stripe, Twilio, and GitHub illustrating how the model is applied in practice
  name: Reference Examples
- description: Controlled vocabulary of agent-readiness terms across operational and capability dimensions
  name: Vocabulary
graphqls:
- description: Reference provider with arguably the most extensively-tooled developer surface on the web. Public OpenAPI, GraphQL schema, webhooks, conditional requests, explicit `X-RateLimit-*` headers, status page
  name: Agent Readiness GraphQL API
  slug: agent-readiness-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agent-readiness.png
json_schemas:
- name: AgentReadinessProvider
  property_count: 10
  slug: agent-readiness-provider
- name: AgentReadinessSignal
  property_count: 12
  slug: agent-readiness-signal
jsonld:
- class_count: 5
  name: Agent Readiness Context
  property_count: 14
  slug: agent-readiness-context
layout: provider
modified: '2026-05-22'
name: Agent Readiness
nav: Providers
network: true
overview: 'Agent Readiness publishes 3 APIs on the [APIs.io](https://apis.io/) network: Stripe API (reference provider), GitHub REST + GraphQL API (reference provider), and Twilio API (reference provider). Tagged areas include Agent Readiness, AI Agents, API Discovery, API Governance, and Machine-Readable APIs.


  The Agent Readiness catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent Readiness'' developer surface includes documentation and 8 more developer resources.'
random_paper: 10
rules:
- name: Agent Readiness API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agent-readiness-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.0
  delta: -7.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 59.7
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 40.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/agent-readiness/refs/heads/main/screenshots/agent-readiness-2026-06-20T165921.png
security:
- kind: domain-security
  name: Agent Readiness Domain Security
  slug: agent-readiness-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agent Readiness Vulnerability Disclosure
  slug: agent-readiness-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agent-readiness
tags:
- Agent Readiness
- AI Agents
- API Discovery
- API Governance
- Machine-Readable APIs
- MCP
- OpenAPI
- AsyncAPI
use_cases:
- description: A team auditing their own API surface against a checklist of agent-readiness dimensions
  name: Provider Self-Assessment
- description: An engineering team evaluating whether a third-party API can be driven by an autonomous agent before committing to integration
  name: Consumer Pre-Integration Review
- description: A buyer scoring vendor APIs on a normalized agent-readiness rubric during procurement
  name: Procurement and RFP Scoring
- description: A directory or marketplace ranking listed APIs by agent-readiness score to help agent developers pick safe surfaces
  name: Aggregator Indexes
- description: Mapping where each standard (OpenAPI, AsyncAPI, MCP, AIPREF, RFC 9727, RFC 9421) contributes to which dimension
  name: Standards Coverage Map
---
