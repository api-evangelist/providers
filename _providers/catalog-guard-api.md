---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Catalog API from Catalog Guard API — 2 operation(s) for catalog.
  name: Catalog Guard API Catalog API
  slug: catalog-guard-api-catalog-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Guard Catalog API
  slug: open-catalog-guard-api-catalog-api
common:
- group: docs
  title: ''
  type: Documentation
  url: https://catalogguard.noahcortezj-c.workers.dev/api/v1/catalog/docs
- group: docs
  title: ''
  type: APIReference
  url: https://catalogguard.noahcortezj-c.workers.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://catalogguard.noahcortezj-c.workers.dev/api/v1/catalog/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://catalogguard.noahcortezj-c.workers.dev/diagnostic
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catalogguard.noahcortezj-c.workers.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catalogguard.noahcortezj-c.workers.dev/privacy
- group: other
  title: ''
  type: APIsJson
  url: https://catalogguard.noahcortezj-c.workers.dev/apis.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/catalog-guard-api-catalog-check-openapi.json
- group: docs
  title: ''
  type: OpenAPIOverlay
  url: overlays/catalog-guard-api-catalog-check-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/catalog-guard-api-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/catalog-guard-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/catalog-guard-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/catalog-guard-api-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/catalog-guard-api-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/catalog-guard-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/catalog-guard-api-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/catalog-guard-api-examples.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/catalog-guard-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/catalog-guard-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/catalog-guard-api-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catalog-guard-api-domain-security.yml
created: '2026-07-31'
description: 'A bounded, fail-closed catalog preflight and validation service for Shopify-shaped supplier product CSVs. Exposes an unauthenticated JSON HTTP API that validates raw CSV text or normalized product rows and returns a deterministic result: safe rows, blockers and warnings, each finding carrying a row index, field, stable code and message. Ambiguous input is refused rather than guessed — unclosed quotes, malformed rows, duplicate headers, duplicate normalized SKUs and incomplete variant pairs all become blockers, and supplier categories are treated as audit-only rather than mapped to a Shopify taxonomy. The service does not accept file uploads, credentials, payment data or store connections, holds no storage, and never imports or modifies a catalog; every successful response repeats those disclosures inline as machine-readable fields. Access is controlled by input bounds and a best-effort rate limit rather than by identity. Commercially it is fronted by a free in-browser CSV preflight,
  a $149 bounded human CSV Diagnostic, and a separate free Shopify store-launch referral path.'
image: https://catalogguard.noahcortezj-c.workers.dev/og.png
layout: provider
mcp_servers:
- description: ''
  name: catalog-guard-api-mcp.yml
  slug: catalog-guard-api-mcpyml
modified: '2026-08-09'
name: Catalog Guard API
nav: Providers
network: true
overview: 'Catalog Guard API publishes 1 API on the [APIs.io](https://apis.io/) network: Catalog API. Tagged areas include ecommerce, catalog-validation, shopify, data-quality, and csv-validation.


  Catalog Guard API''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, code examples, and 16 more developer resources.'
random_paper: 27
rate_limits:
- limit_count: 1
  name: Catalog Guard Api Rate Limits
  slug: catalog-guard-api-rate-limits
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 47.0
    developer_ergonomics: 40.8
    discoverability: 70.4
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 37.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Catalog Guard Api Authentication
  slug: catalog-guard-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Catalog Guard Api Domain Security
  slug: catalog-guard-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: catalog-guard-api
tags:
- ecommerce
- catalog-validation
- shopify
- data-quality
- csv-validation
- product-data-qa
- data-preflight
- data-validation
- retail
---
