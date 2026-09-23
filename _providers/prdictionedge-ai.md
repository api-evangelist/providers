---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://api.aux.prdictionedge.ai
  baseurl_source: declared
  description: REST API (23 operations, OpenAPI 3.1) for durable business-counterparty certification attempts, evidence resolution (GLEIF business identity, OFAC sanctions, RDAP domain identity, private-source attes
  name: AUX Evidence and Certification API
  slug: aux-evidence-and-certification-api
- description: A2A 1.0 JSON-RPC interface for the AUX Evidence and Certification agent, exposing twelve bounded skills (business identity evidence, OFAC sanctions evidence, domain identity evidence, source attestati
  name: AUX A2A Agent (JSON-RPC)
  slug: aux-a2a-agent-json-rpc
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://prdictionedge.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aux.prdictionedge.ai/agents
- group: docs
  title: ''
  type: Documentation
  url: https://aux.prdictionedge.ai/agents
- group: docs
  title: ''
  type: APIReference
  url: https://api.aux.prdictionedge.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://aux.prdictionedge.ai/agents/quickstart
- group: operate
  title: ''
  type: Roadmap
  url: https://aux.prdictionedge.ai/roadmap
- group: operate
  title: ''
  type: Support
  url: https://aux.prdictionedge.ai/demo?product=aux
- group: company
  title: ''
  type: Blog
  url: https://aux.prdictionedge.ai/news/agentic-payments-owner-control
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aux.prdictionedge.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aux.prdictionedge.ai/privacy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/a2a/prdictionedge-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/prdictionedge-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/llms/prdictionedge-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prdictionedge-ai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/well-known/prdictionedge-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prdictionedge-ai-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/mcp/prdictionedge-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/prdictionedge-ai-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/mcp/prdictionedge-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/prdictionedge-ai-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/packages/prdictionedge-ai-packages.yml
  title: ''
  type: Packages
  url: packages/prdictionedge-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/packages/prdictionedge-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/prdictionedge-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/cli/prdictionedge-ai-cli.yml
  title: ''
  type: CLI
  url: cli/prdictionedge-ai-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/authentication/prdictionedge-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prdictionedge-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/conventions/prdictionedge-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/prdictionedge-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/conventions/prdictionedge-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/prdictionedge-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/errors/prdictionedge-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prdictionedge-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/lifecycle/prdictionedge-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/prdictionedge-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/conformance/prdictionedge-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prdictionedge-ai-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/security/prdictionedge-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prdictionedge-ai-domain-security.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/sandbox/prdictionedge-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/prdictionedge-ai-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/data-model/prdictionedge-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prdictionedge-ai-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/overlays/prdictionedge-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/prdictionedge-ai-openapi-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/plans/prdictionedge-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prdictionedge-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/rate-limits/prdictionedge-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prdictionedge-ai-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/regulatory/prdictionedge-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/prdictionedge-ai-regulatory-posture.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/prdictionedge-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: 'AUX by PrdictionEdge is a machine-native, non-executing pre-action trust layer for AI agents: before an agent onboards, contracts with or pays a business counterparty, AUX independently resolves live GLEIF legal-entity evidence, bounded exact-name OFAC screening and IANA RDAP domain identity, verifies signed private-source attestations, and returns ES256-signed certification receipts that any downstream system can verify offline against a published JWKS. The public counterparty check needs no account, API key or payment. The surface is published as OpenAPI 3.1, an A2A 1.0 JSON-RPC agent with a well-known Agent Card, an ARD manifest and llms.txt. PrdictionEdge (Chino Hills, California; founder John Bruner) has refocused its public work entirely on AUX.'
image: https://aux.prdictionedge.ai/og.png
layout: provider
mcp_servers:
- description: ''
  name: AUX by PrdictionEdge MCP Server
  slug: aux-by-prdictionedge-mcp-server
modified: '2026-09-19'
name: AUX by PrdictionEdge
nav: Providers
network: true
overview: 'AUX by PrdictionEdge publishes 1 API on the [APIs.io](https://apis.io/) network: AUX Evidence and Certification API. Tagged areas include Company, Counterparty Verification, Sanctions Screening, Legal Entity Identifier, and Know Your Business.


  AUX by PrdictionEdge''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 25 more developer resources.'
plans:
- name: Prdictionedge Ai Plans Pricing
  plan_count: 0
  slug: prdictionedge-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Prdictionedge Ai Rate Limits
  slug: prdictionedge-ai-rate-limits
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 42.9
    developer_ergonomics: 80.4
    discoverability: 75.9
    operational_transparency: 5.3
  previous_composite: 40.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Prdictionedge Ai Authentication
  slug: prdictionedge-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Prdictionedge Ai Domain Security
  slug: prdictionedge-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prdictionedge-ai
tags:
- Company
- Counterparty Verification
- Sanctions Screening
- Legal Entity Identifier
- Know Your Business
- Agent Infrastructure
- Trust and Safety
- Signed Receipts
- Agentic Payments
- A2A
- Agent-Native
website: https://prdictionedge.ai/
---
