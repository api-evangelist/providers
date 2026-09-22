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
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-09-21'
api_count: 2
apis:
- baseURL: https://allagents.app
  baseurl_source: declared
  description: Search, browse and read agent cards, and manage your own — register, update, claim a harvested card, recover a lost token, delist. JSON over HTTPS rooted at the domain, documented by the provider in a
  name: allagents Directory API
  slug: allagents-directory-api
- description: 'The directory as an A2A agent. POST a JSON-RPC 2.0 message/send stating a need ("I need a translation agent") and the operator answers with ranked matching agents and a card link for each. Discovered '
  name: allagents Operator (A2A Agent)
  slug: allagents-operator-a2a-agent
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://allagents.app/
- group: docs
  title: ''
  type: Documentation
  url: https://allagents.app/api
- group: docs
  title: ''
  type: APIReference
  url: https://allagents.app/api
- group: start
  title: ''
  type: GettingStarted
  url: https://allagents.app/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://allagents.app/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/llms/allagents-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allagents-app-llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:allagents.contact@proton.me
- group: other
  title: ''
  type: Sitemap
  url: https://allagents.app/sitemap.xml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/a2a/allagents-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/allagents-app-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/well-known/allagents-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allagents-app-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/conformance/allagents-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allagents-app-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/errors/allagents-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allagents-app-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/lifecycle/allagents-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/allagents-app-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/authentication/allagents-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allagents-app-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/conventions/allagents-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/allagents-app-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/security/allagents-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allagents-app-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/plans/allagents-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allagents-app-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/rate-limits/allagents-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/allagents-app-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/packages/allagents-app-packages.yml
  title: ''
  type: Packages
  url: packages/allagents-app-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allagents-app/refs/heads/main/regulatory/allagents-app-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/allagents-app-regulatory-posture.yml
created: '2026-09-19'
description: 'allagents (allagents.app) is a public directory of AI agents by specialty, operated from Switzerland. It lists 811 agents across specialties such as trading, research, coding, memory, automation, legal, commerce, identity and security, each card carrying the agent''s name, address, protocols and how to reach it. Listing is free, instant and account-less — one POST returns an edit token and a recovery phrase — and withdrawal is instant and permanent. The directory exposes a small JSON API (search, browse by page or specialty, one card, register, update, claim, recover, delist), publishes an llms.txt, and is itself an A2A agent: its conformant agent card at /.well-known/agent-card.json points at a JSON-RPC message/send operator that answers a plain-language need with matching agents.'
image: https://allagents.app/logo.png
layout: provider
mcp_servers:
- description: ''
  name: MCP candidate only (deployment mode none — the provider ships no MCP server)
  slug: mcp-candidate-only-deployment-mode-none-the-provider-ships-no-mcp-server
modified: '2026-09-19'
name: allagents
nav: Providers
network: true
overview: 'allagents publishes 1 API on the [APIs.io](https://apis.io/) network: Directory API. Tagged areas include Company, AI Agents, Agent Directory, A2A, and Discovery.


  allagents'' developer surface includes documentation, API reference, getting-started guide, support, authentication, and 16 more developer resources.'
plans:
- name: Allagents App Plans Pricing
  plan_count: 1
  slug: allagents-app-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Allagents App Rate Limits
  slug: allagents-app-rate-limits
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 12.0
    developer_ergonomics: 47.0
    discoverability: 75.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 25.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Allagents App Authentication
  slug: allagents-app-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Allagents App Domain Security
  slug: allagents-app-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: allagents-app
tags:
- Company
- AI Agents
- Agent Directory
- A2A
- Discovery
- Search
- Registry
- Switzerland
website: https://allagents.app/
---
