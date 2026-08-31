---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Audit API from Gleeful AI — 3 operation(s) for audit.
  name: Gleeful AI Audit API
  slug: gleefulai-audit-api
- description: The Bots API from Gleeful AI — 1 operation(s) for bots.
  name: Gleeful AI Bots API
  slug: gleefulai-bots-api
- description: The Capabilities API from Gleeful AI — 1 operation(s) for capabilities.
  name: Gleeful AI Capabilities API
  slug: gleefulai-capabilities-api
- description: The Catalog API from Gleeful AI — 1 operation(s) for catalog.
  name: Gleeful AI Catalog API
  slug: gleefulai-catalog-api
- description: The Cite API from Gleeful AI — 2 operation(s) for cite.
  name: Gleeful AI Cite API
  slug: gleefulai-cite-api
- description: The Compare API from Gleeful AI — 2 operation(s) for compare.
  name: Gleeful AI Compare API
  slug: gleefulai-compare-api
- description: The Content API from Gleeful AI — 1 operation(s) for content.
  name: Gleeful AI Content API
  slug: gleefulai-content-api
- description: The Examples API from Gleeful AI — 1 operation(s) for examples.
  name: Gleeful AI Examples API
  slug: gleefulai-examples-api
- description: The Fixes API from Gleeful AI — 1 operation(s) for fixes.
  name: Gleeful AI Fixes API
  slug: gleefulai-fixes-api
- description: The Health API from Gleeful AI — 1 operation(s) for health.
  name: Gleeful AI Health API
  slug: gleefulai-health-api
- description: The Llms API from Gleeful AI — 1 operation(s) for llms.
  name: Gleeful AI Llms API
  slug: gleefulai-llms-api
- description: The Meta API from Gleeful AI — 1 operation(s) for meta.
  name: Gleeful AI Meta API
  slug: gleefulai-meta-api
- description: The Preview API from Gleeful AI — 2 operation(s) for preview.
  name: Gleeful AI Preview API
  slug: gleefulai-preview-api
- description: The Pricing API from Gleeful AI — 1 operation(s) for pricing.
  name: Gleeful AI Pricing API
  slug: gleefulai-pricing-api
- description: The Probe API from Gleeful AI — 1 operation(s) for probe.
  name: Gleeful AI Probe API
  slug: gleefulai-probe-api
- description: The Schema API from Gleeful AI — 1 operation(s) for schema.
  name: Gleeful AI Schema API
  slug: gleefulai-schema-api
- description: The Status API from Gleeful AI — 1 operation(s) for status.
  name: Gleeful AI Status API
  slug: gleefulai-status-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Visibility AI Audit API
  slug: open-gleefulai-audit-api
- collection_type: open
  name: Visibility AI Audit Bots API
  slug: open-gleefulai-bots-api
- collection_type: open
  name: Visibility AI Audit Capabilities API
  slug: open-gleefulai-capabilities-api
- collection_type: open
  name: Visibility AI Audit Catalog API
  slug: open-gleefulai-catalog-api
- collection_type: open
  name: Visibility AI Audit Cite API
  slug: open-gleefulai-cite-api
- collection_type: open
  name: Visibility AI Audit Compare API
  slug: open-gleefulai-compare-api
- collection_type: open
  name: Visibility AI Audit Content API
  slug: open-gleefulai-content-api
- collection_type: open
  name: Visibility AI Audit Examples API
  slug: open-gleefulai-examples-api
- collection_type: open
  name: Visibility AI Audit Fixes API
  slug: open-gleefulai-fixes-api
- collection_type: open
  name: Visibility AI Audit Health API
  slug: open-gleefulai-health-api
- collection_type: open
  name: Visibility AI Audit Llms API
  slug: open-gleefulai-llms-api
- collection_type: open
  name: Visibility AI Audit Meta API
  slug: open-gleefulai-meta-api
- collection_type: open
  name: Visibility AI Audit Pricing API
  slug: open-gleefulai-pricing-api
- collection_type: open
  name: Visibility AI Audit Probe API
  slug: open-gleefulai-probe-api
- collection_type: open
  name: Visibility AI Audit Schema API
  slug: open-gleefulai-schema-api
- collection_type: open
  name: Visibility AI Audit Status API
  slug: open-gleefulai-status-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gleefulai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://visibility.gleefulai.com
- group: docs
  title: ''
  type: Documentation
  url: https://visibility.gleefulai.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://visibility.gleefulai.com/api/pricing
- group: agent
  title: ''
  type: LlmsText
  url: llms/gleefulai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/gleefulai-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gleefulai-plans.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gleefulai-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gleefulai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gleefulai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gleefulai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/gleefulai-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gleefulai-rate-limits.yml
coverage:
  checked: '2026-08-13'
  detail: gleefulai.com was moved to the GoDaddy/Afternic aftermarket on 2026-08-07 and is now a domain listed for sale — the API host visibility.gleefulai.com fails the TLS handshake for its own hostname, every /api/* path 404s from the parking origin, and the wildcard even serves a generated /llms.txt whose text advertises the domain for sale, so the entire surface captured live on 2026-08-03 is gone.
  evidence:
  - status: 0
    url: https://visibility.gleefulai.com/api/pricing
  - status: 404
    url: http://visibility.gleefulai.com/api/pricing
  - status: 404
    url: http://visibility.gleefulai.com/api/health
  - status: 403
    url: https://gleefulai.com/lander
  - status: 200
    url: http://visibility.gleefulai.com/llms.txt
  reason: defunct
  state: none
created: '2026-08-03'
description: 'Gleeful AI publishes Visibility, an AI-visibility and answer-engine-optimization audit API: it scores how visible and understandable a website is to AI assistants and agents, audits AI crawler access (GPTBot, ClaudeBot and others), generates a production-ready llms.txt and schema.org markup, checks brand citation across assistants, and runs competitor gap analysis. The access model is the notable part — there are no API keys. Every priced endpoint answers an unauthenticated request with HTTP 402 and an x402 v2 challenge in a Payment-Required header, settled in USDC on Base at prices from $0.06 to $0.55 a call, published machine-readably at /api/pricing alongside /api/capabilities and /api/catalog. Discovery, pricing and two preview endpoints are free. It is an agent-native API in both directions: built to be paid for and called by an agent, and built to measure whether agents can read you.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gleefulai.png
layout: provider
modified: '2026-08-13'
name: Gleeful AI
nav: Providers
network: true
overview: 'Gleeful AI publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Bots API, Capabilities API, and 14 more. Tagged areas include Artificial Intelligence, Agents, x402, Micropayments, and SEO.


  Gleeful AI''s developer surface includes documentation, pricing, authentication, and 10 more developer resources.'
plans:
- name: Gleefulai Plans
  plan_count: 0
  slug: gleefulai-plans
random_paper: 18
rate_limits:
- limit_count: 0
  name: Gleefulai Rate Limits
  slug: gleefulai-rate-limits
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 39.9
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 23.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gleefulai/refs/heads/main/screenshots/gleefulai-2026-08-07T165729.png
security:
- kind: authentication
  name: Gleefulai Authentication
  slug: gleefulai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gleefulai Domain Security
  slug: gleefulai-domain-security
  summary_line: no transport/DNS hardening detected
slug: gleefulai
tags:
- Artificial Intelligence
- Agents
- x402
- Micropayments
- SEO
- Audit
- Website
- Content
- Crawlers
- Monetization
website: https://visibility.gleefulai.com
---
