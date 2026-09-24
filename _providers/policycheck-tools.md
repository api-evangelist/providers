---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Policycheck Tools Agentic Access
  operation_count: 2
  slug: policycheck-tools-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://policycheck.tools
  baseurl_source: declared
  description: Anonymous JSON REST API on policycheck.tools. The provider-published OpenAPI (verbatim in openapi/) describes two live legacy ChatGPT-plugin operations, analyzeLegalDocument (POST /api/chatgpt/analyze
  name: PolicyCheck API
  slug: policycheck-api
- description: 'JSON-RPC 2.0 Agent-to-Agent endpoint at https://policycheck.tools/api/a2a, discovered through an A2A agent card served at the legacy /.well-known/agent.json path (protocolVersion 0.2.0, seven skills: '
  name: PolicyCheck A2A Agent
  slug: policycheck-a2a-agent
- description: The policycheck-mcp npm package (1.0.2, published 2026-02-13, MIT) is a stdio Model Context Protocol server installed with `npx -y policycheck-mcp`. It exposes three tools — analyze_seller (policy pag
  name: PolicyCheck MCP Server
  slug: policycheck-mcp-server
- description: 'Pay-per-request analysis over the x402 protocol: POST https://policycheck.tools/api/x402/analyze answers HTTP 402 with a PAYMENT-REQUIRED header carrying an x402Version 2 envelope — $0.03 (30000 atomi'
  name: PolicyCheck x402 Analysis API
  slug: policycheck-x402-analysis-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://policycheck.tools/
- group: docs
  title: ''
  type: Documentation
  url: https://policycheck.tools/docs
- group: docs
  title: ''
  type: APIReference
  url: https://policycheck.tools/docs#endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://policycheck.tools/docs#quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://policycheck.tools/docs#rate-limits
- group: company
  title: ''
  type: Blog
  url: https://policycheck.tools/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@policycheck.tools
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policycheck.tools/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policycheck.tools/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vibegpt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/vibegpt/T-C-Widget
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/llms/policycheck-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/policycheck-tools-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://policycheck.tools/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/a2a/policycheck-tools-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/policycheck-tools-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/well-known/policycheck-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/policycheck-tools-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/mcp/policycheck-tools-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/policycheck-tools-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/mcp/policycheck-tools-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/policycheck-tools-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/packages/policycheck-tools-packages.yml
  title: ''
  type: Packages
  url: packages/policycheck-tools-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/x402/policycheck-tools-x402.yml
  title: ''
  type: X-X402
  url: x402/policycheck-tools-x402.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/authentication/policycheck-tools-authentication.yml
  title: ''
  type: Authentication
  url: authentication/policycheck-tools-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/conventions/policycheck-tools-conventions.yml
  title: ''
  type: Conventions
  url: conventions/policycheck-tools-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/errors/policycheck-tools-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/policycheck-tools-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/lifecycle/policycheck-tools-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/policycheck-tools-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/conformance/policycheck-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/policycheck-tools-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/data-model/policycheck-tools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/policycheck-tools-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/overlays/policycheck-tools-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/policycheck-tools-openapi-overlay.yaml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/rate-limits/policycheck-tools-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/policycheck-tools-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/plans/policycheck-tools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/policycheck-tools-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/agentic-access/policycheck-tools-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/policycheck-tools-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/security/policycheck-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/policycheck-tools-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/regulatory/policycheck-tools-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/policycheck-tools-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/regulatory/policycheck-tools-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/policycheck-tools-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/policycheck-tools/refs/heads/main/regulatory/policycheck-tools-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/policycheck-tools-regulatory-posture.yml
created: '2026-09-19'
description: PolicyCheck (formerly LegalEasy) is a seller-policy risk intelligence service built for AI purchasing agents. Given a store URL or raw policy text it extracts structured facts from return, shipping, warranty, terms and privacy policies — return window, restocking fees, binding arbitration, class-action waivers, data selling — scores them deterministically into a 0-10 risk score and a 0-100 buyer protection score, labels standard boilerplate separately from unusual restrictions, and can return the result as an Ed25519-signed assessment an agent presents at checkout and a merchant verifies against a public JWKS. The surface is anonymous REST at policycheck.tools/api/check, an A2A JSON-RPC agent with a published agent card, a stdio MCP server on npm, an x402 pay-per-analysis endpoint settled in USDC on Base, a versioned clause registry, and a keyed audit log and compliance report. The published OpenAPI covers only the two legacy ChatGPT-plugin operations.
image: https://policycheck.tools/logo.png
layout: provider
mcp_servers:
- description: ''
  name: PolicyCheck MCP Server
  slug: policycheck-mcp-server
modified: '2026-09-19'
name: PolicyCheck
nav: Providers
network: true
overview: 'PolicyCheck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Policy Analysis, Consumer Protection, E-Commerce, and Agentic Commerce.


  PolicyCheck''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, authentication, and 27 more developer resources.'
plans:
- name: Policycheck Tools Plans Pricing
  plan_count: 2
  slug: policycheck-tools-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Policycheck Tools Rate Limits
  slug: policycheck-tools-rate-limits
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 46.9
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Policycheck Tools Authentication
  slug: policycheck-tools-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Policycheck Tools Domain Security
  slug: policycheck-tools-domain-security
  summary_line: TLSv1.3 · HSTS
slug: policycheck-tools
tags:
- Company
- Policy Analysis
- Consumer Protection
- E-Commerce
- Agentic Commerce
- Risk Assessment
- AI Agents
- A2A
- MCP
- x402
- Legal
- Returns
website: https://policycheck.tools/
---
