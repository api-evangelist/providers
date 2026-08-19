---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 84.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 56
  human_in_the_loop: 56
  name: Xquik Agentic Access
  operation_count: 127
  slug: xquik-agentic-access
  summary_line: 127 operations · 56 acting · 56 human-in-the-loop
api_count: 3
apis:
- description: OpenAPI 3.1 REST API for public X data, connected-account write actions, monitoring, signed webhooks, exports, account management, and billing.
  name: Xquik REST API
  slug: xquik-rest-api
- description: Hosted MCP server for the Xquik API with OAuth 2.1 and API-key access.
  name: Xquik API MCP Server
  slug: xquik-api-mcp-server
- description: Read-only hosted MCP server for searching Xquik documentation.
  name: Xquik Docs MCP Server
  slug: xquik-docs-mcp-server
artifact_total: 21
asyncapis:
- description: ''
  name: Xquik Asyncapi Provenance
  slug: xquik-asyncapi-provenance
- description: Xquik sends signed monitor events to customer-managed HTTPS webhook endpoints. Xquik is not affiliated with or endorsed by X Corp.
  name: Xquik Monitor Webhooks
  slug: xquik-asyncapi
collections:
- collection_type: open
  name: Xquik API
  slug: open-xquik-rest-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xquik-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xquik-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xquik-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://xquik.com/en
- group: other
  title: ''
  type: APIsJSON
  url: https://xquik.com/apis.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.xquik.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xquik.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.xquik.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.xquik.com/x-api-quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.xquik.com/api-reference/authentication
- group: design
  title: ''
  type: Idempotency
  url: https://docs.xquik.com/api-reference/x-write/create-tweet
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-typescript
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-python
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-go
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-ruby
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-java
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-kotlin
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-csharp
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-php
- group: build
  title: ''
  type: CLI
  url: https://github.com/Xquik-dev/x-twitter-scraper-cli
- group: start
  title: ''
  type: Sandbox
  url: https://docs.xquik.com/mcp/tools
- group: build
  title: ''
  type: Postman
  url: collections/xquik.postman_collection.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xquik-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@xquik.com
- group: company
  title: ''
  type: Blog
  url: blogs/xquik-developer-updates.md
- group: commercial
  title: ''
  type: Plans
  url: plans/xquik-plans.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://xquik.com/en#pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.xquik.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.xquik.com/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xquik.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xquik.com/en/privacy
- group: commercial
  title: ''
  type: FinOps
  url: finops/xquik-finops.yml
- group: auth
  title: ''
  type: Compliance
  url: security/xquik-compliance.md
- group: auth
  title: ''
  type: TrustCenter
  url: security/xquik-trust-center.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.xquik.com/changelog
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xquik-rate-limits.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/xquik-deprecation-policy.md
- group: auth
  title: ''
  type: Security
  url: https://docs.xquik.com/security
- group: design
  title: ''
  type: Webhooks
  url: https://docs.xquik.com/webhooks/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Xquik-dev
- group: operate
  title: ''
  type: RoadMap
  url: roadmap/xquik-roadmap.md
- group: design
  title: ''
  type: ErrorCatalog
  url: https://docs.xquik.com/guides/error-handling
- group: agent
  title: ''
  type: WellKnown
  url: well-known/xquik-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://xquik.com/.well-known/security.txt
- group: other
  title: ''
  type: HTTPMessageSignatures
  url: https://xquik.com/.well-known/http-message-signatures-directory
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xquik-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/xquik-api-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xquik-agentic-access.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/xquik-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/xquik-vocabulary.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/xquik-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/xquik-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/xquik-asyncapi.yaml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/xquik-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/xquik-webhook-event.schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/xquik-webhook-endpoint.schema.json
- group: build
  title: ''
  type: Packages
  url: packages/xquik-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/xquik-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xquik-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/xquik-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xquik-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xquik-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/xquik-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/xquik-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/xquik-sandbox.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xquik-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xquik-lifecycle.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/xquik-security.txt
created: '2026-04-14'
description: Xquik is an independent third-party X data and automation platform. It provides public data reads, connected-account write actions, monitoring, signed webhooks, exports, hosted MCP servers, OAuth 2.1, API keys, 8 SDKs, a CLI, Agent Skills, and an OpenAPI 3.1 contract. Not affiliated with X Corp.
finops:
- name: Xquik Finops
  service_category: Social Media Data
  slug: xquik-finops
image: https://xquik.com/logo-square.png
json_schemas:
- name: Xquik Webhook Endpoint
  property_count: 8
  slug: xquik-webhook-endpoint.schema
- name: Xquik Webhook Event
  property_count: 8
  slug: xquik-webhook-event.schema
jsonld:
- class_count: 18
  name: Xquik Context
  property_count: 4
  slug: xquik-context
layout: provider
mcp_servers:
- description: ''
  name: xquik-mcp.yml
  slug: xquik-mcpyml
- description: ''
  name: mcp
  slug: mcp
- description: ''
  name: xquik-docs-mcp.yml
  slug: xquik-docs-mcpyml
modified: '2026-08-13'
name: Xquik
nav: Providers
network: true
overview: 'Xquik publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include social media data, X / Twitter, social listening, data extraction, and automation.


  The Xquik catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Xquik''s developer surface includes authentication, documentation, API reference, getting-started guide, SDKs, CLI, sandbox, and 62 more developer resources.'
plans:
- name: Xquik Plans
  plan_count: 4
  slug: xquik-plans
random_paper: 27
rate_limits:
- limit_count: 7
  name: Xquik Rate Limits
  slug: xquik-rate-limits
rules:
- effective_rule_count: 20
  extends: []
  name: Xquik API Rules
  rule_count: 20
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 3
  slug: xquik-rules
scopes:
- name: Xquik Scopes
  scope_count: 1
  slug: xquik-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 92.8
  delta: 3.1
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 100.0
    contract_quality: 80.9
    developer_ergonomics: 100.0
    discoverability: 100.0
    governance: 100.0
    operational_transparency: 81.6
  previous_composite: 89.7
  provenance:
    agentic_access: unknown
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/screenshots/xquik-api-2026-08-17T075407.png
security:
- kind: authentication
  name: Xquik Api Authentication
  slug: xquik-api-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Xquik Api Domain Security
  slug: xquik-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Xquik Api Vulnerability Disclosure
  slug: xquik-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: xquik-api
tags:
- social media data
- X / Twitter
- social listening
- data extraction
- automation
- webhooks
- MCP
- developer API
website: https://xquik.com/en
---
