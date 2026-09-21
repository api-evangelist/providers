---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-09-20'
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
  description: Agent-only API for purchasing fresh, isolated static validation and signed evidence for one exact immutable public GitHub Agent Skill commit. Free anonymous discovery and verification operations (heal
  name: VouchSpec Agent Skill Evidence API
  slug: vouchspec-agent-skill-evidence-api
artifact_total: 7
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/agentic-access/plyrium-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/plyrium-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/security/plyrium-com-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/well-known/plyrium-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/plyrium-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/well-known/plyrium-com-ai-catalog.json
  title: ''
  type: AICatalog
  url: well-known/plyrium-com-ai-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/llms/plyrium-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plyrium-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/mcp/plyrium-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/plyrium-com-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/a2a/plyrium-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/plyrium-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/packages/plyrium-com-packages.yml
  title: ''
  type: Packages
  url: packages/plyrium-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/cli/plyrium-com-cli.yml
  title: ''
  type: CLI
  url: cli/plyrium-com-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/conformance/plyrium-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plyrium-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/errors/plyrium-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plyrium-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/lifecycle/plyrium-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/plyrium-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/changelog/plyrium-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plyrium-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/mordiaky/vouchspec/blob/main/CHANGELOG.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/conventions/plyrium-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/plyrium-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/conventions/plyrium-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/plyrium-com-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/sandbox/plyrium-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/plyrium-com-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/plans/plyrium-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/plyrium-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/rate-limits/plyrium-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/plyrium-com-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/data-model/plyrium-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plyrium-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plyrium-com/refs/heads/main/overlays/plyrium-com-vouchspec-overlay.yaml
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
image: https://www.plyrium.com/brand/plyrium-icon-rounded-1024.png
layout: provider
mcp_servers:
- description: ''
  name: Plyrium MCP Server
  slug: plyrium-mcp-server
modified: '2026-09-19'
name: Plyrium
nav: Providers
network: true
overview: 'Plyrium publishes 1 API on the [APIs.io](https://apis.io/) network: VouchSpec Agent Skill Evidence API. Tagged areas include Company, Agent Skills, Supply Chain Security, Software Provenance, and x402.


  Plyrium''s developer surface includes pricing, engineering blog, support, GitHub presence, CLI, changelog, sandbox, and 35 more developer resources.'
plans:
- name: Plyrium Com Plans Pricing
  plan_count: 2
  slug: plyrium-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Plyrium Com Rate Limits
  slug: plyrium-com-rate-limits
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 45.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 57.1
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 2.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Plyrium Com Authentication
  slug: plyrium-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Plyrium Com Domain Security
  slug: plyrium-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- Field Service
- Home Services
website: https://plyrium.com/
---
