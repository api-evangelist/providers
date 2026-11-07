---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/tryspansa-com/security/tryspansa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tryspansa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryspansa.com/
coverage:
  checked: '2026-09-19'
  detail: The only public API claim is TrySpansa's own a2aregistry.org listing; its agent card at tryspansa.com/.well-known/agent-card.json — like every path on the domain since a 2026-09-16 deployment, including /features, /pricing and /developers — returns HTTP 200 with a 141-byte blank noindex HTML shell, the registry's own 2026-09-14 check recorded NO_TRANSPORTS for that card, and api./docs./mcp.tryspansa.com answer Vercel DEPLOYMENT_NOT_FOUND, so no contract, docs, SDK or portal exists to read.
  evidence:
  - note: blank HTML shell, not JSON
    status: 200
    url: https://tryspansa.com/.well-known/agent-card.json
  - note: blank HTML shell
    status: 200
    url: https://tryspansa.com/features
  - note: blank HTML shell
    status: 200
    url: https://tryspansa.com/developers
  - note: Vercel DEPLOYMENT_NOT_FOUND
    status: 404
    url: https://api.tryspansa.com/
  - note: Vercel DEPLOYMENT_NOT_FOUND
    status: 404
    url: https://docs.tryspansa.com/
  - note: 'registry record (terminal 200 after 2 redirects from the slash-less URL): protocolVersion unknown, task_conformance NO_TRANSPORTS checked 2026-09-14'
    status: 200
    url: https://a2aregistry.org/agents/c235a802-ed05-49e6-8c0d-94db05b8d324/
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: TrySpansa is a YouTube sponsorship and influencer marketplace that lets brands discover and qualify YouTube channels by niche, audience size and engagement (144K+ channels across 30 niches, per its own listing), see CPM-based estimated sponsorship rates, send campaign briefs to creators, and fund deals through escrow on a commission-only model. It listed itself on a2aregistry.org as a 'YouTube sponsorship marketplace API' (discovery-only in v1), but as of 2026-09-19 tryspansa.com serves only a blank HTML shell on every path including its agent card, and no public API contract, documentation, SDK or developer portal is published anywhere.
layout: provider
modified: '2026-09-19'
name: TrySpansa
nav: Providers
network: true
overview: TrySpansa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, YouTube, Sponsorship, Influencer Marketing, and Creator Economy.
random_paper: 17
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tryspansa-com/tryspansa-com-2026-11-03T145203.png
security:
- kind: domain-security
  name: Tryspansa Com Domain Security
  slug: tryspansa-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tryspansa-com
tags:
- Company
- YouTube
- Sponsorship
- Influencer Marketing
- Creator Economy
- Marketplace
- Advertising
- Agents
website: https://tryspansa.com/
---
