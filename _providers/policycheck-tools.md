---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Policycheck Tools Agentic Access
  operation_count: 2
  slug: policycheck-tools-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: 'JSON-RPC 2.0 Agent-to-Agent endpoint at https://policycheck.tools/api/a2a, discovered through an A2A agent card served at the legacy /.well-known/agent.json path (protocolVersion 0.2.0, seven skills: '
  name: PolicyCheck A2A Agent
  slug: policycheck-a2a-agent
- description: The policycheck-mcp npm package (1.0.2, published 2026-02-13, MIT) is a stdio Model Context Protocol server installed with `npx -y policycheck-mcp`. It exposes three tools — analyze_seller (policy pag
  name: PolicyCheck MCP Server
  slug: policycheck-mcp-server
- description: 'Pay-per-request analysis over the x402 protocol: POST https://policycheck.tools/api/x402/analyze answers HTTP 402 with a PAYMENT-REQUIRED header carrying an x402Version 2 envelope — $0.03 (30000 atomi'
  name: PolicyCheck x402 Analysis API
  slug: policycheck-x402-analysis-api
- baseURL: https://policycheck.tools/api/a2a
  baseurl_source: declared
  description: The Chatgpt API from PolicyCheck — 2 operation(s) for chatgpt.
  name: PolicyCheck Chatgpt API
  slug: policycheck-tools-chatgpt-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/policycheck-tools/capabilities/policycheck-tools-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/policycheck-tools-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/policycheck-tools/skills/policycheck-tools-analyze-a-legal-document.md
  title: ''
  type: AgentSkill
  url: skills/policycheck-tools-analyze-a-legal-document.md
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
  href: https://artifacts.apis.io/policycheck-tools/llms/policycheck-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/policycheck-tools-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://policycheck.tools/llms.txt
- group: other
  href: https://artifacts.apis.io/policycheck-tools/a2a/policycheck-tools-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/policycheck-tools-a2a.yml
- group: agent
  href: https://artifacts.apis.io/policycheck-tools/well-known/policycheck-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/policycheck-tools-well-known.yml
- group: agent
  href: https://artifacts.apis.io/policycheck-tools/mcp/policycheck-tools-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/policycheck-tools-mcp.yml
- group: build
  href: https://artifacts.apis.io/policycheck-tools/mcp/policycheck-tools-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/policycheck-tools-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/policycheck-tools/packages/policycheck-tools-packages.yml
  title: ''
  type: Packages
  url: packages/policycheck-tools-packages.yml
- group: other
  href: https://artifacts.apis.io/policycheck-tools/x402/policycheck-tools-x402.yml
  title: ''
  type: X-X402
  url: x402/policycheck-tools-x402.yml
- group: auth
  href: https://artifacts.apis.io/policycheck-tools/authentication/policycheck-tools-authentication.yml
  title: ''
  type: Authentication
  url: authentication/policycheck-tools-authentication.yml
- group: design
  href: https://artifacts.apis.io/policycheck-tools/conventions/policycheck-tools-conventions.yml
  title: ''
  type: Conventions
  url: conventions/policycheck-tools-conventions.yml
- group: design
  href: https://artifacts.apis.io/policycheck-tools/errors/policycheck-tools-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/policycheck-tools-problem-types.yml
- group: design
  href: https://artifacts.apis.io/policycheck-tools/lifecycle/policycheck-tools-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/policycheck-tools-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/policycheck-tools/conformance/policycheck-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/policycheck-tools-conformance.yml
- group: design
  href: https://artifacts.apis.io/policycheck-tools/data-model/policycheck-tools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/policycheck-tools-data-model.yml
- group: other
  href: https://artifacts.apis.io/policycheck-tools/overlays/policycheck-tools-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/policycheck-tools-openapi-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/policycheck-tools/rate-limits/policycheck-tools-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/policycheck-tools-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/policycheck-tools/plans/policycheck-tools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/policycheck-tools-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/policycheck-tools/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/policycheck-tools/agentic-access/policycheck-tools-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/policycheck-tools-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/policycheck-tools/security/policycheck-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/policycheck-tools-domain-security.yml
- group: other
  href: https://artifacts.apis.io/policycheck-tools/regulatory/policycheck-tools-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/policycheck-tools-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/policycheck-tools/regulatory/policycheck-tools-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/policycheck-tools-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/policycheck-tools/regulatory/policycheck-tools-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/policycheck-tools-regulatory-posture.yml
created: '2026-09-19'
description: PolicyCheck (formerly LegalEasy) is a seller-policy risk intelligence service built for AI purchasing agents. Given a store URL or raw policy text it extracts structured facts from return, shipping, warranty, terms and privacy policies — return window, restocking fees, binding arbitration, class-action waivers, data selling — scores them deterministically into a 0-10 risk score and a 0-100 buyer protection score, labels standard boilerplate separately from unusual restrictions, and can return the result as an Ed25519-signed assessment an agent presents at checkout and a merchant verifies against a public JWKS. The surface is anonymous REST at policycheck.tools/api/check, an A2A JSON-RPC agent with a published agent card, a stdio MCP server on npm, an x402 pay-per-analysis endpoint settled in USDC on Base, a versioned clause registry, and a keyed audit log and compliance report. The published OpenAPI covers only the two legacy ChatGPT-plugin operations.
finops:
- has_sources: true
  method: derived
  name: Policycheck Tools Finops
  primary_unit: analysis
  service_category: ''
  slug: policycheck-tools-finops
  template: false
image: https://policycheck.tools/logo.png
layout: provider
mcp_servers:
- description: 'PolicyCheck ships ONE MCP server: the policycheck-mcp npm package, a stdio server a human installs with `npx -y policycheck-mcp`. It exposes three tools and implements each one as a JSON-RPC 2.0 messa'
  name: PolicyCheck MCP Server
  slug: policycheck-mcp
modified: '2026-09-19'
name: PolicyCheck
nav: Providers
network: true
overview: 'PolicyCheck publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chatgpt API, and 3 more. Tagged areas include Company, Policy Analysis, Consumer Protection, E-Commerce, and Agentic Commerce.


  The PolicyCheck catalog on APIs.io includes 1 Spectral governance ruleset.


  PolicyCheck''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, authentication, and 29 more developer resources.'
plans:
- name: Policycheck Tools Plans Pricing
  plan_count: 2
  slug: policycheck-tools-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Policycheck Tools Rate Limits
  slug: policycheck-tools-rate-limits
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: PolicyCheck API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: policycheck-tools-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 55.5
    catalog_earned_first_party: 16.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 44.7
    developer_ergonomics: 33.9
    discoverability: 63.3
    operational_transparency: 23.7
  previous_composite: 48.6
  provenance:
    agentic_access: derived
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
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/policycheck-tools/policycheck-tools-2026-10-11T112650.png
security:
- kind: authentication
  name: Policycheck Tools Authentication
  slug: policycheck-tools-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Policycheck Tools Domain Security
  slug: policycheck-tools-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: Analyze a seller's legal document for buyer risk
  slug: policycheck-tools-analyze-a-legal-document
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
