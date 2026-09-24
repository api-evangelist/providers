---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-09-24'
api_count: 16
apis:
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'HumanMirror x402 API v3.2.0: 82 pay-per-call operations settled in USDC on Base through x402 V2 — agent security (secret scanning, safe preflight, execution receipts, sanitize shield), data quality (c'
  name: HumanMirror X402 API
  slug: x402
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Three separately published contracts for the M2M core: Sanitize Shield (indirect prompt-injection quarantine with a signed Cleanliness Proof), M2M Payload Normalizer (canonical JSON + stable SHA-256 d'
  name: HumanMirror M2M Core Services
  slug: m2m-core
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: Structured analysis of text, JSON records and numeric series (data quality, trends, anomalies, recommendations). Bearer hm_oracle_* key; one credit per successful analysis; 100 credits for 4.99 EUR vi
  name: HumanMirror Oracle API
  slug: oracle
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: Five deterministic micro-tools for agent data pipelines — clean_json, dedupe_records, normalize_entity, score_data_quality, detect_anomaly — multiplexed through POST /api/forge/run with a Bearer hm_fo
  name: HumanMirror Forge API
  slug: forge
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Machine-to-machine tool discovery, routing and credit metering: free catalog search, a 100-credit trial key per network origin, Stripe checkout/claim for 5 000-credit packs, routed tool calls, and the'
  name: HumanMirror Nexus API
  slug: nexus
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Deterministic operational utilities billed in Nexus credits under a Bearer hm_nexus_* key: Sentinel output inspection, Trace receipt issue + public verify, Lens schema inference and contract diff, Vau'
  name: HumanMirror AgentOps API
  slug: agentops
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Free outcome-first fallback discovery for blocked agents: resolve a stated outcome to a live Nexus capability or record a sanitized capability gap in a privacy-thresholded public Machine Demand Graph '
  name: HumanMirror Magnet API
  slug: magnet
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Verified outcome execution: quote and verify are free, a successful outcome.run costs 5 Nexus credits and failed execution or failed deterministic verification is refunded. The same three paths are mi'
  name: HumanMirror Outcome API
  slug: outcome
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Single-tool verified-outcome interface (humanmirror_do): dry-run quotes are free, verified execution costs 6 Nexus credits, failures are refunded. The provider''s recommended default MCP surface for ag'
  name: HumanMirror One API
  slug: one
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Verified 2-3 step agent missions billed as one whole transaction: free quote, 12 Nexus credits kept only if every step and the final proof succeed. One MCP tool (humanmirror_flow), registry entry fr.h'
  name: HumanMirror Flow API
  slug: flow
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Non-custodial intent marketplace for autonomous agents: buyers publish a paid intent (0.010 USDC via x402), providers bid for free, the market awards the best admissible bid (0.050 USDC); live state i'
  name: HumanMirror Intent Market API
  slug: market
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Cryptographic Proof-of-State and exact SHA-256 state-continuity drift detection (state-and-trust, 0.050 USDC via x402) plus the HumanMirror Universal Value Protocol (HUVP/1) resolver, policy firewall '
  name: HumanMirror Agent OS API
  slug: agent-os
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Beta (1.0.0-beta) agent-to-human field-verification network: quote and post bounded public-world verification missions, register field workers, claim/submit/verify missions, and confirm the 80/20 buye'
  name: HumanMirror Physical Oracle API
  slug: physical-oracle
- baseURL: https://humanmirror.fr
  baseurl_source: declared
  description: 'Public machine catalog and status for HumanMirror Automata, the family of ~35 operational guard services (renewal, broken-link, chargeback, KYC, invoice, dunning, uptime, webhook dead-letter …) whose '
  name: HumanMirror Automata API
  slug: automata
- description: The OmniDome machine-society hub — registrar, agora, beacon, commons, settlement quotes, trust hall, agent exchange (1 bp fee) — exposed as a remote MCP server whose five discovery tools answer anonym
  name: OmniDome by HumanMirror (MCP)
  slug: omnidome
artifact_total: 37
collections:
- collection_type: postman
  name: HumanMirror AgentOps
  slug: postman-humanmirror-fr-agentops
- collection_type: postman
  name: HumanMirror Forge API
  slug: postman-humanmirror-fr-forge
- collection_type: postman
  name: HumanMirror Magnet
  slug: postman-humanmirror-fr-magnet
- collection_type: postman
  name: HumanMirror Nexus API
  slug: postman-humanmirror-fr-nexus
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/security/humanmirror-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/humanmirror-fr-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/authentication/humanmirror-fr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/humanmirror-fr-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://humanmirror.fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://humanmirror.fr/agents/
- group: start
  title: ''
  type: GettingStarted
  url: https://humanmirror.fr/connect/
- group: docs
  title: ''
  type: Documentation
  url: https://humanmirror.fr/docs/vibecode/
- group: other
  title: ''
  type: Playground
  url: https://humanmirror.fr/playground/
- group: commercial
  title: ''
  type: Pricing
  url: https://humanmirror.fr/products/
- group: operate
  title: ''
  type: Support
  url: https://humanmirror.fr/contact/
- group: start
  title: ''
  type: SignUp
  url: https://humanmirror.fr/dashboard/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://humanmirror.fr/cgv/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://humanmirror.fr/confidentialite/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VibeMirror-coder
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/llms/humanmirror-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/humanmirror-fr-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://humanmirror.fr/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/a2a/humanmirror-fr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/humanmirror-fr-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/mcp/humanmirror-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/humanmirror-fr-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/mcp/humanmirror-fr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/humanmirror-fr-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/well-known/humanmirror-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/humanmirror-fr-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/well-known/humanmirror-fr-ai-plugin.json
  title: ''
  type: PluginManifest
  url: well-known/humanmirror-fr-ai-plugin.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/conformance/humanmirror-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/humanmirror-fr-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/errors/humanmirror-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/humanmirror-fr-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/lifecycle/humanmirror-fr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/humanmirror-fr-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/conventions/humanmirror-fr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/humanmirror-fr-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/rate-limits/humanmirror-fr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/humanmirror-fr-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/plans/humanmirror-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/humanmirror-fr-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/packages/humanmirror-fr-packages.yml
  title: ''
  type: Packages
  url: packages/humanmirror-fr-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/cli/humanmirror-fr-cli.yml
  title: ''
  type: CLI
  url: cli/humanmirror-fr-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/sandbox/humanmirror-fr-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/humanmirror-fr-sandbox.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/regulatory/humanmirror-fr-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/humanmirror-fr-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/security/humanmirror-fr-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/humanmirror-fr-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/security/humanmirror-fr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/humanmirror-fr-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanmirror-fr/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: 'HumanMirror is a Toulouse, France-based agent-infrastructure provider (operated as an entrepreneur individuel) that sells security, verification, data-quality and payment-orchestration services to autonomous agents and the developers who run them. Agents pay per call in USDC on Base through x402 V2 (0.001 / 0.010 / 0.050 USDC tiers, 5 USDC bundles, a 297 USDC 30-day pass) or in Stripe-bought credits (Oracle, Forge, Nexus); humans buy audits, a Pro subscription and Enterprise Guard governance tiers in EUR. The surface is unusually machine-first: 16 OpenAPI 3.1 contracts, seven hosted MCP servers whose tools/list is open, an A2A agent card, llms.txt, an ai-plugin manifest, published JSON Schemas and ~40 vendor /.well-known/ manifests, all on a single host.'
image: https://humanmirror.fr/assets/humanmirror-mark.svg
json_schemas:
- name: HumanMirror Agent OS State & Trust v1
  property_count: 7
  slug: humanmirror-fr-agent-os-v1
- name: Humanmirror Fr Escrow V1 Example
  property_count: 0
  slug: humanmirror-fr-escrow-v1-example
- name: HumanMirror x402 Escrow State v1
  property_count: 12
  slug: humanmirror-fr-escrow-v1
- name: HumanMirror Genesis Manifest
  property_count: 6
  slug: humanmirror-fr-genesis
jsonld:
- class_count: 0
  name: Humanmirror Fr M2M Context
  property_count: 0
  slug: humanmirror-fr-m2m
layout: provider
mcp_servers:
- description: ''
  name: HumanMirror MCP Server
  slug: humanmirror-mcp-server
- description: ''
  name: HumanMirror MCP Server
  slug: humanmirror-mcp-server-2
- description: ''
  name: HumanMirror MCP Server
  slug: humanmirror-mcp-server-3
- description: ''
  name: HumanMirror MCP Server
  slug: humanmirror-mcp-server-4
- description: ''
  name: HumanMirror MCP Server
  slug: humanmirror-mcp-server-5
- description: ''
  name: HumanMirror MCP Server
  slug: humanmirror-mcp-server-6
- description: ''
  name: HumanMirror MCP Server
  slug: humanmirror-mcp-server-7
- description: ''
  name: HumanMirror MCP Server
  slug: humanmirror-mcp-server-8
modified: '2026-09-19'
name: HumanMirror
nav: Providers
network: true
overview: 'HumanMirror publishes 14 APIs on the [APIs.io](https://apis.io/) network, including X402 API, M2M Core Services, Oracle API, and 11 more. Tagged areas include Company, AI Agents, Agent Security, Prompt Injection Defense, and x402.


  The HumanMirror catalog on APIs.io includes 1 JSON-LD context.


  HumanMirror''s developer surface includes authentication, getting-started guide, documentation, pricing, support, signup flow, CLI, and 26 more developer resources.'
plans:
- name: Humanmirror Fr Plans Pricing
  plan_count: 10
  slug: humanmirror-fr-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 6
  name: Humanmirror Fr Rate Limits
  slug: humanmirror-fr-rate-limits
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 79.0
    catalog_earned_first_party: 24.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 52.5
    developer_ergonomics: 68.5
    discoverability: 81.5
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 60.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Humanmirror Fr Authentication
  slug: humanmirror-fr-authentication
  summary_line: http bearer (per-product prefixed API keys)/apiKey in header (X-API-Key, HumanMirror Pro)/x402 payment signature (PAYMENT-SIGNATURE header, not an OpenAPI securityScheme)/none (discovery, quotes, verification, Magnet, MCP tools/list) · 11 schemes
- kind: domain-security
  name: Humanmirror Fr Domain Security
  slug: humanmirror-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Humanmirror Fr Vulnerability Disclosure
  slug: humanmirror-fr-vulnerability-disclosure
  summary_line: Hackerone
slug: humanmirror-fr
tags:
- Company
- AI Agents
- Agent Security
- Prompt Injection Defense
- x402
- Machine Payments
- USDC
- MCP
- A2A
- Data Quality
- Verified Outcomes
- Microtransactions
- France
website: https://humanmirror.fr/
---
