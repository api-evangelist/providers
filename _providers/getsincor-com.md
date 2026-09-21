---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: 'A2A 1.0.1 agent surface over JSON-RPC 2.0 exposing sixteen skills. Discover via the agent card, quote a skill (price, fee split, free-quota state, input/output JSON Schema) without side effects, then '
  name: SINCOR Agent Swarm A2A API
  slug: sincor-agent-swarm-a2a-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://getsincor.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/a2a/getsincor-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getsincor-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/well-known/getsincor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getsincor-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/authentication/getsincor-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getsincor-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/conventions/getsincor-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getsincor-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/errors/getsincor-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getsincor-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/conformance/getsincor-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getsincor-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/lifecycle/getsincor-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getsincor-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/changelog/getsincor-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getsincor-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/OrderofChaos33/SINCOR2/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/OrderofChaos33/SINCOR2/blob/main/ROADMAP.md
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/plans/getsincor-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getsincor-com-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://getsincor.com/buy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/rate-limits/getsincor-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getsincor-com-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/sandbox/getsincor-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/getsincor-com-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/packages/getsincor-com-packages.yml
  title: ''
  type: Packages
  url: packages/getsincor-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/packages/getsincor-com-packages.yml
  title: ''
  type: SDKs
  url: packages/getsincor-com-packages.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/OrderofChaos33/SINCOR2
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OrderofChaos33
- group: auth
  title: ''
  type: Security
  url: https://github.com/OrderofChaos33/SINCOR2/blob/main/SECURITY.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/security/getsincor-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getsincor-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/security/getsincor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getsincor-com-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/regulatory/getsincor-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/getsincor-com-regulatory-posture.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getsincor-com/refs/heads/main/llms/getsincor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getsincor-com-llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://getsincor.com/signup
- group: other
  title: ''
  type: Whitepaper
  url: https://getsincor.com/static/docs/SINCOR_whitepaper.md
- group: operate
  title: ''
  type: Community
  url: https://t.me/getsincor
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/getsincor
- group: auth
  title: ''
  type: X-TokenList
  url: https://getsincor.com/tokenlists/sincor.tokenlist.json
created: '2026-09-19'
description: 'SINCOR operates an autonomous AI "agent swarm" on Base mainnet that sells sixteen skills — lead enrichment, competitor intelligence, outbound sequences, healthcare credential checks, dental billing scrubs, compliance SBOMs, market forecasts, deal scoring, content, cash-flow recovery, local-business site building, TOA strategic decisions, contract negotiation, quality audits, agent lifecycle and AXIOM payment verification — to other agents over the A2A protocol (1.0.1, JSON-RPC 2.0 at https://getsincor.com/api/a2a). Payment is on-chain: paid skills are quoted in the AXM token and settled to a treasury on Base with a 500 bps platform fee, six skills are free for the first five calls per caller, and human subscriptions (Starter $297/month) are paid in USDC on Base. The machine-readable contract is the A2A Agent Card at /.well-known/agent-card.json (graded conformant), backed by per-skill JSON Schemas from the quote endpoint; there is no OpenAPI, no MCP server and no rate-limit
  signal. The runtime is open source (MIT) at github.com/OrderofChaos33/SINCOR2, which also carries the API reference, changelog, roadmap and security policy.'
image: https://getsincor.com/static/sincor_og.jpg
layout: provider
modified: '2026-09-19'
name: SINCOR
nav: Providers
network: true
overview: 'SINCOR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, A2A, Agentic Commerce, and Agentic Payments.


  SINCOR''s developer surface includes authentication, changelog, pricing, sandbox, signup flow, and 24 more developer resources.'
plans:
- name: Getsincor Com Plans Pricing
  plan_count: 3
  slug: getsincor-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Getsincor Com Rate Limits
  slug: getsincor-com-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 35.5
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 68.5
    operational_transparency: 36.8
  previous_composite: 2.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Getsincor Com Authentication
  slug: getsincor-com-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Getsincor Com Domain Security
  slug: getsincor-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Getsincor Com Vulnerability Disclosure
  slug: getsincor-com-vulnerability-disclosure
  summary_line: Hackerone
slug: getsincor-com
tags:
- Company
- AI Agents
- A2A
- Agentic Commerce
- Agentic Payments
- x402
- Base
- Crypto
- Lead Generation
- Healthcare
- Compliance
- Market Intelligence
- agent-native
website: https://getsincor.com/
---
