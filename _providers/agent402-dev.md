---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Agent402 Dev Agentic Access
  operation_count: 12
  slug: agent402-dev-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://agent402.dev
  baseurl_source: spec
  description: The Developer tools API from agent402.dev — 9 operation(s) for developer tools.
  name: agent402.dev Developer tools API
  slug: agent402-dev-developer-tools-api
- baseURL: https://agent402.dev
  baseurl_source: spec
  description: The Downloads API from agent402.dev — 2 operation(s) for downloads.
  name: agent402.dev Downloads API
  slug: agent402-dev-downloads-api
- baseURL: https://agent402.dev
  baseurl_source: spec
  description: The Productivity API from agent402.dev — 1 operation(s) for productivity.
  name: agent402.dev Productivity API
  slug: agent402-dev-productivity-api
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/agent402-dev/overlays/agent402-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agent402-dev-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://agent402.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://agent402.dev/
- group: agent
  href: https://artifacts.apis.io/agent402-dev/llms/agent402-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent402-dev-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agent402.dev/llms.txt
- group: other
  href: https://artifacts.apis.io/agent402-dev/a2a/agent402-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agent402-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agent402-dev/well-known/agent402-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent402-dev-well-known.yml
- group: agent
  href: https://artifacts.apis.io/agent402-dev/mcp/agent402-dev-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/agent402-dev-mcp.yml
- group: build
  href: https://artifacts.apis.io/agent402-dev/packages/agent402-dev-packages.yml
  title: ''
  type: Packages
  url: packages/agent402-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/agent402-dev/authentication/agent402-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agent402-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/agent402-dev/conventions/agent402-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agent402-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/agent402-dev/errors/agent402-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent402-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agent402-dev/lifecycle/agent402-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agent402-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agent402-dev/conformance/agent402-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent402-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/agent402-dev/data-model/agent402-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agent402-dev-data-model.yml
- group: start
  href: https://artifacts.apis.io/agent402-dev/sandbox/agent402-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agent402-dev-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/agent402-dev/plans/agent402-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agent402-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/agent402-dev/rate-limits/agent402-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agent402-dev-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/agent402-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/agent402-dev/regulatory/agent402-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/agent402-dev-regulatory-posture.yml
- group: auth
  href: https://artifacts.apis.io/agent402-dev/security/agent402-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent402-dev-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/agent402-dev/agentic-access/agent402-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agent402-dev-agentic-access.yml
created: '2026-09-19'
description: 'agent402.dev is a pay-per-call agent-commerce service that sells website release evidence and offline tools to AI agents over the x402 v2 protocol, settled in USDC on Base (eip155:8453) with no accounts, sign-up or API keys — payment is the authorization. Its primary product is a 5.00 USDC AI Discovery Site Audit: 22 deterministic technical SEO / AEO / GEO checks on one public HTTPS page plus five evidence-derived remediation slots for JSON-LD, metadata, robots.txt, llms.txt and sitemap.xml, with a free exact-body eligibility check, a live sample report and a machine-readable methodology published beside it. Seven auxiliary direct HTTP resources are priced from 0.01 to 5.99 USDC: a Verified URL Evidence Snapshot, a HEAD-only website preflight, an x402 endpoint health check and launch-readiness audit, a deterministic task-priority day scheduler, and two downloadable ZIP packs. The whole surface is published machine-first — an OpenAPI 3.1 contract at /openapi.json, an x402 v2
  manifest at /.well-known/x402, a conformant A2A agent card, llms.txt and a JSON endpoint map at /meta.json — while the operator is not named anywhere on the site. An earlier MCP surface has been deliberately retired (410 Gone).'
examples:
- key_count: 14
  name: Agent402 Dev Site Release Audit Sample
  slug: agent402-dev-site-release-audit-sample
- key_count: 5
  name: Agent402 Dev Url Evidence 402 Challenge
  slug: agent402-dev-url-evidence-402-challenge
image: https://agent402.dev/favicon.ico
layout: provider
modified: '2026-09-19'
name: agent402.dev
nav: Providers
network: true
overview: 'agent402.dev publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Developer tools API, Downloads API, and Productivity API. Tagged areas include Company, x402, Agentic Payments, Agentic Commerce, and AI Agents.


  The agent402.dev catalog on APIs.io includes 1 Spectral governance ruleset.


  agent402.dev''s developer surface includes pricing, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Agent402 Dev Plans Pricing
  plan_count: 1
  slug: agent402-dev-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Agent402 Dev Rate Limits
  slug: agent402-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: agent402.dev API Rules
  rule_count: 51
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 1
  slug: agent402-dev-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.5
    catalog_earned_first_party: 16.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 56.5
    developer_ergonomics: 35.1
    discoverability: 64.3
    operational_transparency: 21.1
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agent402-dev/agent402-dev-2026-10-11T093045.png
security:
- kind: authentication
  name: Agent402 Dev Authentication
  slug: agent402-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agent402 Dev Domain Security
  slug: agent402-dev-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: capture-url-evidence
  slug: agent402-dev-capture-url-evidence
- name: check-x402-endpoint
  slug: agent402-dev-check-x402-endpoint
- name: run-ai-discovery-site-audit
  slug: agent402-dev-run-ai-discovery-site-audit
slug: agent402-dev
tags:
- Company
- x402
- Agentic Payments
- Agentic Commerce
- AI Agents
- A2A
- Technical SEO
- Website Audits
- URL Evidence
- Developer Tools
- Base
website: https://agent402.dev/
---
