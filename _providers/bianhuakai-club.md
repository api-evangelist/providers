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
    error_semantics: false
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
  score: 10.8
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: 'A2A agent operated by Lei Zhang: you provide a Google Maps link or coordinates of any place in China and a real local goes there and films ~10 minutes of genuine, unscripted everyday footage (streets,'
  name: China On-Site Video Service (A2A agent)
  slug: china-on-site-video-service-a2a-agent
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://bianhuakai.club/
- group: commercial
  title: ''
  type: Pricing
  url: https://bianhuakai.club/lei/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/a2a/bianhuakai-club-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bianhuakai-club-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/well-known/bianhuakai-club-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bianhuakai-club-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/llms/bianhuakai-club-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bianhuakai-club-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/authentication/bianhuakai-club-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bianhuakai-club-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/conventions/bianhuakai-club-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bianhuakai-club-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/conformance/bianhuakai-club-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bianhuakai-club-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/plans/bianhuakai-club-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bianhuakai-club-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/rate-limits/bianhuakai-club-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bianhuakai-club-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/security/bianhuakai-club-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bianhuakai-club-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bianhuakai-club/refs/heads/main/regulatory/bianhuakai-club-regulatory-posture.yml
  title: ''
  type: X-RegulatoryPosture
  url: regulatory/bianhuakai-club-regulatory-posture.yml
created: '2026-09-19'
description: 'OPC / 彼岸花开 is a one-person company (OPC) operated by Lei Zhang in Hangzhou, China. Its agent-facing surface is a single A2A agent, "China On-Site Video Service": an agent (or a person) supplies a Google Maps link or coordinates for any place in China and Lei travels there and films about ten minutes of genuine, unscripted footage - streets, markets, temples, a family''s old neighborhood - delivered by email as an MP4 for a fixed $50 USD (other requests at $50/hour, paid by Wise, Panda Remit or Remitly). The A2A agent card is served from the company''s own domain at the legacy /.well-known/agent.json path and grades conformant against A2A 1.0.0; the JSON-RPC endpoint at /a2a/ is anonymous and live. It is an agent card in front of a human fulfilment service, not a software API: there is no OpenAPI, MCP server, SDK, developer documentation or developer signup. The site root hosts a separate login-gated Chinese consumer chat app (彼岸花开 · 花灵).'
layout: provider
modified: '2026-09-19'
name: OPC / 彼岸花开
nav: Providers
network: true
overview: 'OPC / 彼岸花开 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agents, A2A, Video, and Video Production.


  OPC / 彼岸花开''s developer surface includes pricing, authentication, and 10 more developer resources.'
plans:
- name: Bianhuakai Club Plans Pricing
  plan_count: 0
  slug: bianhuakai-club-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Bianhuakai Club Rate Limits
  slug: bianhuakai-club-rate-limits
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 13.1
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bianhuakai Club Authentication
  slug: bianhuakai-club-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bianhuakai Club Domain Security
  slug: bianhuakai-club-domain-security
  summary_line: TLSv1.3
slug: bianhuakai-club
tags:
- Company
- Agents
- A2A
- Video
- Video Production
- China
- Hangzhou
- Travel
- Genealogy
- Real-Estate
- Documentary
- Local Services
- One-Person Company
website: https://bianhuakai.club/
---
