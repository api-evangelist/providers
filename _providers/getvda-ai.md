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
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-09-25'
api_count: 6
apis:
- baseURL: https://witness.getvda.ai
  baseurl_source: declared
  description: Seal governed AI-agent decisions into tamper-evident, Ed25519-signed, independently-verifiable records and verify them offline; issue, check and revoke agent admission credentials; self-serve key mint
  name: VDA Witness API
  slug: vda-witness-api
- baseURL: https://hitl.getvda.ai
  baseurl_source: declared
  description: 'Human decisions on agent actions: register an authority config, raise an escalated decision, read it, record the human resolution (sealed to Witness under customer-managed custody), manage baselines a'
  name: VDA HITL API
  slug: vda-hitl-api
- baseURL: https://acp.getvda.ai
  baseurl_source: declared
  description: 'Agent Control Plane — the governance-aware wrapper on git: load a governance set at a ref, prepare and Compliance-Guard a change, run the governance CI suite, surface it for a non-engineer approver, r'
  name: VDA ACP API
  slug: vda-acp-api
- baseURL: https://c2md.getvda.ai
  baseurl_source: declared
  description: A2A (JSON-RPC at /a2a) and MCP (/mcp) agent that generates EU AI Act, GDPR, NIST SP 800-53 and ISO 42001 governance Markdown (AGENTS.md, SOP.md, SKILL.md, EXCEPTION.md), risk assessments, DPIA/FRIA sc
  name: C2MD Compliance Agent
  slug: c2md-compliance-agent
- baseURL: https://router.getvda.ai
  baseurl_source: declared
  description: 'The GOSCE (GitHub Open-Source Combination Engine) fleet: 98 templated remote MCP + A2A agents at <agent>.getvda.ai, each with two tools (invoke, selftest), an Ed25519-signed agent card verifiable agai'
  name: GOSCE Agent Portfolio and Router
  slug: gosce-agent-portfolio-and-router
- description: 'Admission authority for the suite — an A2A agent (6 skills) that runs holder-binding (DID-auth), intake and gap analysis for a candidate agent and issues a Witness-sealed admission credential against '
  name: VDA Onboarding Agent
  slug: vda-onboarding-agent
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://getvda.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://getvda.ai/governance-cycle.html
- group: start
  title: ''
  type: GettingStarted
  url: https://witness.getvda.ai/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getvda-ai
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@getvda.ai
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/llms/getvda-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getvda-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://getvda.ai/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/a2a/getvda-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getvda-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/mcp/getvda-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getvda-ai-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/mcp/getvda-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/getvda-ai-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/packages/getvda-ai-packages.yml
  title: ''
  type: Packages
  url: packages/getvda-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/packages/getvda-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/getvda-ai-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/well-known/getvda-ai-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/getvda-ai-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/conformance/getvda-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getvda-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/errors/getvda-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getvda-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/lifecycle/getvda-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getvda-ai-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/scopes/getvda-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/getvda-ai-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/authentication/getvda-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getvda-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/security/getvda-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getvda-ai-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/conventions/getvda-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getvda-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/conventions/getvda-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/getvda-ai-conventions.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/regulatory/getvda-ai-regulatory-posture.yml
  title: ''
  type: X-RegulatoryPosture
  url: regulatory/getvda-ai-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/regulatory/getvda-ai-regulatory-posture.yml
  title: ''
  type: DataResidency
  url: regulatory/getvda-ai-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/regulatory/getvda-ai-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/getvda-ai-regulatory-posture.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/sandbox/getvda-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/getvda-ai-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/plans/getvda-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getvda-ai-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://witness.getvda.ai/.well-known/agent-card.json
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/rate-limits/getvda-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getvda-ai-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/data-model/getvda-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getvda-ai-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getvda-ai/refs/heads/main/overlays/getvda-ai-witness-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/getvda-ai-witness-overlay.yaml
- group: other
  title: ''
  type: X-Robots
  url: https://getvda.ai/robots.txt
- group: other
  title: ''
  type: X-Sitemap
  url: https://getvda.ai/sitemap.xml
- group: start
  title: ''
  type: X-Demo
  url: https://getvda.ai/demo
created: '2026-09-19'
description: 'Verified Digital Agents (VDA, getvda.ai) sells governance for AI agents that can be proved after the fact: Witness seals every governed decision into an Ed25519-signed, hash-chained record (anchored to Sigstore Rekor and RFC 3161 TSAs on the paid tier) and produces EU AI Act Article 12 evidence; C2MD turns EU AI Act, GDPR, NIST SP 800-53 and ISO 42001 controls into governance Markdown agents can follow; ACP versions, tests, approves and signs that governance in git and serves it as signed bundles; Onboarding admits agents and issues Witness-sealed admission credentials against did:web identities; HITL routes what exceeds an agent''s authority to a human and seals the decision. Every block publishes a signed A2A agent card, Witness/C2MD/HITL run remote MCP servers, and Witness/HITL/ACP publish OpenAPI 3.1. The same operator runs GOSCE, a 98-server fleet of templated, x402-metered MCP/A2A agents under *.getvda.ai — the "VDA / GOSCE" author that a2aregistry.org counted as 98 agents.'
image: https://getvda.ai/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: Verified Digital Agents (VDA) MCP Server
  slug: verified-digital-agents-vda-mcp-server
- description: ''
  name: Witness MCP endpoint (Streamable HTTP)
  slug: witness-mcp-endpoint-streamable-http
- description: ''
  name: HITL MCP endpoint (Streamable HTTP, bearer required)
  slug: hitl-mcp-endpoint-streamable-http-bearer-required
- description: ''
  name: C2MD MCP endpoint (Streamable HTTP)
  slug: c2md-mcp-endpoint-streamable-http
- description: ''
  name: GOSCE router MCP endpoint (Streamable HTTP)
  slug: gosce-router-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Verified Digital Agents (VDA)
nav: Providers
network: true
overview: 'Verified Digital Agents (VDA) publishes 6 APIs on the [APIs.io](https://apis.io/) network, including VDA Witness API, VDA HITL API, VDA ACP API, and 3 more. Tagged areas include Company, AI Agents, AI Governance, Compliance, and Audit Trail.


  Verified Digital Agents (VDA)''s developer surface includes documentation, getting-started guide, authentication, sandbox, pricing, and 29 more developer resources.'
plans:
- name: Getvda Ai Plans Pricing
  plan_count: 6
  slug: getvda-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 7
  name: Getvda Ai Rate Limits
  slug: getvda-ai-rate-limits
scopes:
- name: Getvda Ai Scopes
  scope_count: 0
  slug: getvda-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 38.1
    developer_ergonomics: 56.5
    discoverability: 80.0
    operational_transparency: 34.2
  previous_composite: 44.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Getvda Ai Authentication
  slug: getvda-ai-authentication
  summary_line: http/oauth2/x402-payment · 7 schemes
- kind: domain-security
  name: Getvda Ai Domain Security
  slug: getvda-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: getvda-ai
tags:
- Company
- AI Agents
- AI Governance
- Compliance
- Audit Trail
- Agent Identity
- A2A
- MCP
- x402
- EU AI Act
- Human-in-the-Loop
website: https://getvda.ai/
---
