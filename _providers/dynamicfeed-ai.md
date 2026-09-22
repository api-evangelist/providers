---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-09-21'
api_count: 2
apis:
- baseURL: https://dynamicfeed.ai
  baseurl_source: declared
  description: 'The full REST surface: 158 operations on https://dynamicfeed.ai — the keyless POST /v1/batch tool dispatcher (up to 20 calls per request, each result Ed25519-signed with provenance and freshness), leg'
  name: Dynamic Feed REST API
  slug: dynamic-feed-rest-api
- description: Hosted, keyless Model Context Protocol server at https://dynamicfeed.ai/mcp (Streamable HTTP with legacy HTTP+SSE auto-detected; explicit SSE at /sse) exposing all 94 read-only live-data tools with re
  name: Dynamic Feed MCP Server
  slug: dynamic-feed-mcp-server
- description: A2A 1.0 JSON-RPC agent at https://dynamicfeed.ai/a2a with a JWS-signed agent card (graded conformant) declaring eight keyless skills — live weather, natural hazards, macro and rates, security intel, c
  name: Dynamic Feed A2A Agent
  slug: dynamic-feed-a2a-agent
- description: 'Push-on-change webhooks registered per key at POST /v1/webhooks (SSRF-validated URL, one-time secret, HMAC-SHA256 X-DynamicFeed-Signature on every delivery) and a keyless Server-Sent Events stream at '
  name: Dynamic Feed Webhooks and Live Stream
  slug: dynamic-feed-webhooks-and-stream
artifact_total: 29
asyncapis:
- description: ''
  name: Dynamicfeed Ai Webhooks
  slug: dynamicfeed-ai-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/security/dynamicfeed-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dynamicfeed-ai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/security/dynamicfeed-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dynamicfeed-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/security/dynamicfeed-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamicfeed-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dynamicfeed.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://dynamicfeed.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dynamicfeed.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dynamicfeed.ai/connect
- group: start
  title: ''
  type: GettingStarted
  url: https://dynamicfeed.ai/connect
- group: other
  title: ''
  type: Playground
  url: https://dynamicfeed.ai/playground
- group: start
  title: ''
  type: Console
  url: https://dynamicfeed.ai/dashboard
- group: start
  title: ''
  type: SignUp
  url: https://dynamicfeed.ai/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://dynamicfeed.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dynamicfeed.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dynamicfeed.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://dynamicfeed.ai/uptime
- group: operate
  title: ''
  type: StatusPage
  url: https://dynamicfeed.ai/status.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fluxdyne
- group: auth
  title: ''
  type: TrustCenter
  url: https://dynamicfeed.ai/trust
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://dynamicfeed.ai/security/advisories
- group: other
  title: ''
  type: ParentCompany
  url: https://fluxdyne.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/llms/dynamicfeed-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dynamicfeed-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dynamicfeed.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/well-known/dynamicfeed-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dynamicfeed-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/well-known/dynamicfeed-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dynamicfeed-ai-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://dynamicfeed.ai/.well-known/security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/well-known/dynamicfeed-ai-ai-catalog.json
  title: ''
  type: AICatalog
  url: well-known/dynamicfeed-ai-ai-catalog.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/well-known/dynamicfeed-ai-ai-plugin.json
  title: ''
  type: AIPlugin
  url: well-known/dynamicfeed-ai-ai-plugin.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/packages/dynamicfeed-ai-packages.yml
  title: ''
  type: Packages
  url: packages/dynamicfeed-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/packages/dynamicfeed-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/dynamicfeed-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/cli/dynamicfeed-ai-cli.yml
  title: ''
  type: CLI
  url: cli/dynamicfeed-ai-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/conformance/dynamicfeed-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dynamicfeed-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/lifecycle/dynamicfeed-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dynamicfeed-ai-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/plans/dynamicfeed-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynamicfeed-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/components/dynamicfeed-ai-components.yml
  title: ''
  type: Components
  url: components/dynamicfeed-ai-components.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://dynamicfeed.ai/privacy
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://dynamicfeed.ai/privacy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/regulatory/dynamicfeed-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/dynamicfeed-ai-regulatory-posture.yml
- group: other
  title: ''
  type: OpenDataset
  url: https://dynamicfeed.ai/dataset
- group: other
  title: ''
  type: X402
  url: https://dynamicfeed.ai/v1/pro/catalog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/authentication/dynamicfeed-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynamicfeed-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamicfeed-ai/refs/heads/main/security/dynamicfeed-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dynamicfeed-ai-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'Dynamic Feed, a product of Fluxdyne Pty Ltd (Australia), is a live-data and machine-evidence layer for AI agents and robots: 94 read-only tools across 20 domains (weather and air quality, natural hazards, space weather and satellite positions, CVEs and actively-exploited vulnerabilities, software versions and EOL, sanctions and Federal Register, shipping, macro and rates, AI-model pricing and provider latency) drawn from named public sources such as NASA, NOAA, USGS, CISA, OFAC and the World Bank plus its own measurements. Every response carries a provenance and freshness envelope and a detached Ed25519 signature (DF-VERIFY/1) verifiable offline against published keys. The same tool registry is served three ways from one host: a keyless MCP server at /mcp (Streamable HTTP, protocol 2025-06-18), an A2A 1.0 agent at /a2a with a conformant signed agent card, and a REST API published as OpenAPI 3.1 with a keyless 20-call batch endpoint. A /v1 surface adds robot go/caution/no-go
  awareness verdicts, RFC 3161 anchoring, signed transaction/inference/robot/eval receipts on an append-only notary log with daily checkpoints, per-key watchlists, HMAC-signed change webhooks and an SSE stream. Paid access is machine-native via x402 (HTTP 402, USDC on Base, 0.001 USDC per call).'
image: https://dynamicfeed.ai/df-logo.png
json_schemas:
- name: DF-VERIFY/1 — attestation/v1 profile (parametric trigger)
  property_count: 8
  slug: dynamicfeed-ai-attestation-v1
- name: DF-VERIFY/1 — awareness/v1 profile
  property_count: 13
  slug: dynamicfeed-ai-awareness-v1
- name: DF-VERIFY/1 — delivery-receipt/v1 (proof of delivery for agent commerce)
  property_count: 15
  slug: dynamicfeed-ai-delivery-receipt-v1
- name: Dynamic Feed eval-receipt/v1
  property_count: 6
  slug: dynamicfeed-ai-eval-receipt-v1
- name: DF-VERIFY/1 — GroundTruthReceipt Verifiable Credential profile
  property_count: 7
  slug: dynamicfeed-ai-ground-truth-vc-v1
- name: Dynamic Feed — inference-receipt/v1
  property_count: 6
  slug: dynamicfeed-ai-inference-receipt-v1
- name: DF-VERIFY/1 — intensity/v1 profile (parametric intensity-at-location)
  property_count: 14
  slug: dynamicfeed-ai-intensity-v1
- name: OKF reliability object (v1 draft)
  property_count: 12
  slug: dynamicfeed-ai-okf-reliability-v1
- name: DF-VERIFY/1 — proxy-witness/v1 profile (receipts for any API)
  property_count: 8
  slug: dynamicfeed-ai-proxy-witness-v1
- name: DF-VERIFY/1 — receipt/v1 profile
  property_count: 6
  slug: dynamicfeed-ai-receipt-v1
- name: Dynamic Feed — robot-receipt/v1
  property_count: 6
  slug: dynamicfeed-ai-robot-receipt-v1
- name: Dynamicfeed Ai Schemas Index
  property_count: 0
  slug: dynamicfeed-ai-schemas-index
- name: DF-VERIFY/1 — station-receipt/v1 profile (We Sign Your Station)
  property_count: 9
  slug: dynamicfeed-ai-station-receipt-v1
- name: DF-VERIFY/1 — trigger-receipt/v1 profile (parametric catastrophe settlement)
  property_count: 11
  slug: dynamicfeed-ai-trigger-receipt-v1
- name: Dynamic Feed Trust Receipt v1 envelope
  property_count: 3
  slug: dynamicfeed-ai-trust-receipt-v1
- name: Dynamic Feed txn-receipt/v1
  property_count: 6
  slug: dynamicfeed-ai-txn-receipt-v1
layout: provider
mcp_servers:
- description: ''
  name: Dynamic Feed MCP Server
  slug: dynamic-feed-mcp-server
- description: ''
  name: Dynamic Feed MCP Server
  slug: dynamic-feed-mcp-server-2
modified: '2026-09-19'
name: Dynamic Feed
nav: Providers
network: true
overview: 'Dynamic Feed publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Live Data, AI Agents, MCP, A2A, and agent-native.


  The Dynamic Feed catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dynamic Feed''s developer surface includes documentation, API reference, getting-started guide, developer console, signup flow, pricing, CLI, and 34 more developer resources.'
plans:
- name: Dynamicfeed Ai Plans Pricing
  plan_count: 4
  slug: dynamicfeed-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Dynamicfeed Ai Rate Limits
  slug: dynamicfeed-ai-rate-limits
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 71.0
    catalog_earned_first_party: 24.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 61.1
    developer_ergonomics: 73.2
    discoverability: 87.0
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 66.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Dynamicfeed Ai Authentication
  slug: dynamicfeed-ai-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Dynamicfeed Ai Domain Security
  slug: dynamicfeed-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dynamicfeed Ai Vulnerability Disclosure
  slug: dynamicfeed-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Dynamicfeed Ai Trust Center
  slug: dynamicfeed-ai-trust-center
  summary_line: trust center published
slug: dynamicfeed-ai
tags:
- Live Data
- AI Agents
- MCP
- A2A
- agent-native
- Provenance
- Weather
- Natural Hazards
- Vulnerabilities
- Sanctions
- Space
- Robotics
- x402
- Receipts
- Notary
- Australia
website: https://dynamicfeed.ai/
---
