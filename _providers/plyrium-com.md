---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Plyrium Com Agentic Access
  operation_count: 8
  slug: plyrium-com-agentic-access
  summary_line: 8 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://vouchspec.plyrium.com
  baseurl_source: declared
  description: Free, anonymous machine-readable service metadata.
  name: Plyrium Discovery API
  slug: plyrium-com-discovery-api
- baseURL: https://vouchspec.plyrium.com
  baseurl_source: declared
  description: x402-paid exact-commit validation intake.
  name: Plyrium Purchase API
  slug: plyrium-com-purchase-api
- baseURL: https://vouchspec.plyrium.com
  baseurl_source: declared
  description: Public receipt bytes, status, and issuer key.
  name: Plyrium Verification API
  slug: plyrium-com-verification-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/plyrium-com/agentic-access/plyrium-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/plyrium-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/plyrium-com/security/plyrium-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plyrium-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plyrium.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plyrium.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plyrium.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plyrium.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.plyrium.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.plyrium.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.plyrium.com/kb
- group: start
  title: ''
  type: Login
  url: https://www.plyrium.com/login
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mordiaky
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plyrium
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/plyrium
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/plyrium
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/plyrium
- group: agent
  href: https://artifacts.apis.io/plyrium-com/well-known/plyrium-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/plyrium-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/plyrium-com/well-known/plyrium-com-ai-catalog.json
  title: ''
  type: AICatalog
  url: well-known/plyrium-com-ai-catalog.json
- group: agent
  href: https://artifacts.apis.io/plyrium-com/llms/plyrium-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plyrium-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/plyrium-com/mcp/plyrium-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/plyrium-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/plyrium-com/a2a/plyrium-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/plyrium-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/plyrium-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/plyrium-com/packages/plyrium-com-packages.yml
  title: ''
  type: Packages
  url: packages/plyrium-com-packages.yml
- group: build
  href: https://artifacts.apis.io/plyrium-com/cli/plyrium-com-cli.yml
  title: ''
  type: CLI
  url: cli/plyrium-com-cli.yml
- group: design
  href: https://artifacts.apis.io/plyrium-com/conformance/plyrium-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plyrium-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/plyrium-com/errors/plyrium-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plyrium-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/plyrium-com/lifecycle/plyrium-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/plyrium-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/plyrium-com/changelog/plyrium-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plyrium-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/mordiaky/vouchspec/blob/main/CHANGELOG.md
- group: design
  href: https://artifacts.apis.io/plyrium-com/conventions/plyrium-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/plyrium-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/plyrium-com/conventions/plyrium-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/plyrium-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/plyrium-com/sandbox/plyrium-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/plyrium-com-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/plyrium-com/plans/plyrium-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/plyrium-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/plyrium-com/rate-limits/plyrium-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/plyrium-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/plyrium-com/data-model/plyrium-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plyrium-com-data-model.yml
- group: other
  href: https://artifacts.apis.io/plyrium-com/overlays/plyrium-com-vouchspec-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/plyrium-com-vouchspec-overlay.yaml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.plyrium.com/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://www.plyrium.com/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://www.plyrium.com/privacy
- group: operate
  title: ''
  type: IncidentNotification
  url: https://www.plyrium.com/privacy
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://www.plyrium.com/privacy
- group: other
  title: ''
  type: ExitAssistance
  url: https://www.plyrium.com/terms
- group: other
  title: ''
  type: AITransparency
  url: https://www.plyrium.com/privacy
created: '2026-09-19'
description: Plyrium is a contractor operating system for home-service businesses (HVAC, plumbing, electrical, roofing) built in Coolidge, Arizona - AI phone answering, scheduling, quotes, invoicing with Stripe payments and Google Business Profile automation. Its public API surface is VouchSpec, an agent-only service on vouchspec.plyrium.com that sells fresh static validation and Ed25519-signed DSSE evidence for one exact public GitHub Agent Skill commit, paid per request in USDC over x402 on Base, and discoverable through an OpenAPI 3.1 contract, llms.txt, an A2A agent card, a remote MCP server, an installable Agent Skill and an ARD ai-catalog.
finops:
- has_sources: true
  method: derived
  name: Plyrium Com Finops
  primary_unit: subscription
  service_category: ''
  slug: plyrium-com-finops
  template: false
image: https://www.plyrium.com/brand/plyrium-icon-rounded-1024.png
layout: provider
mcp_servers:
- description: Remote MCP server at vouchspec.plyrium.com over streamable HTTP; 1 tool listed.
  name: Plyrium MCP Server
  slug: vouchspec-agent-skill-evidence
modified: '2026-09-19'
name: Plyrium
nav: Providers
network: true
overview: 'Plyrium publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API, Purchase API, and Verification API. Tagged areas include Company, Agent Skills, Supply Chain Security, Software Provenance, and x402.


  The Plyrium catalog on APIs.io includes 1 Spectral governance ruleset.


  Plyrium''s developer surface includes pricing, engineering blog, support, GitHub presence, CLI, changelog, sandbox, and 35 more developer resources.'
plans:
- name: Plyrium Com Plans Pricing
  plan_count: 5
  slug: plyrium-com-plans-pricing
- name: Plyrium Com Price Estimates
  plan_count: 0
  slug: plyrium-com-price-estimates
random_paper: 22
rate_limits:
- limit_count: 0
  name: Plyrium Com Rate Limits
  slug: plyrium-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Plyrium API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: plyrium-com-rules
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 46.0
    developer_ergonomics: 45.2
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/plyrium-com/plyrium-com-2026-10-11T112643.png
security:
- kind: authentication
  name: Plyrium Com Authentication
  slug: plyrium-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Plyrium Com Domain Security
  slug: plyrium-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: plyrium-com-verify-shared-receipt
  slug: plyrium-com-verify-shared-receipt
- name: vouchspec-verify-before-install
  slug: plyrium-com-vouchspec-verify-before-install
slug: plyrium-com
tags:
- Company
- Agent Skills
- Supply Chain Security
- Software Provenance
- x402
- Agentic Commerce
- A2A
- MCP
- Field Service Management
- Home Services
website: https://plyrium.com/
---
