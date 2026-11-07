---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
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
  score: 8.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Match Candidate Platform (MCP) API documentation.
  name: DevMatch MCP
  slug: devmatch-mcp
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dev-match-xyz/plans/dev-match-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dev-match-xyz-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dev-match-xyz/llms/dev-match-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dev-match-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/dev-match-xyz/a2a/dev-match-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dev-match-xyz-a2a.yml
- group: other
  href: https://artifacts.apis.io/dev-match-xyz/hosts/dev-match-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dev-match-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/dev-match-xyz/vendors/dev-match-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dev-match-xyz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dev-match-xyz/security/dev-match-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dev-match-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dev-match.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://dev-match.xyz/docs/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://dev-match.xyz/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev-match.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dev-match.xyz/privacy
- group: operate
  title: ''
  type: Contact
  url: https://dev-match.xyz/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://dev-match.xyz/how-it-works
coverage:
  checked: '2026-11-05'
  detail: Documentation is served as JavaScript‑rendered pages, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://dev-match.xyz/docs/mcp
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DevMatch helps deep‑tech teams hire engineers and scientists by searching public work such as papers, open‑source contributions and patents. The platform matches job descriptions to real‑world evidence, providing evidence‑backed candidate profiles and fraud‑risk scores. It also offers an MCP server for AI assistants to query candidate data directly.
image: https://dev-match.xyz/opengraph-image?038246dc359968f4
layout: provider
modified: '2026-11-05'
name: DevMatch
nav: Providers
network: true
overview: 'DevMatch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Engineering, Hiring, Deep Tech, Artificial Intelligence, and Platform.


  DevMatch''s developer surface includes documentation, pricing, getting-started guide, and 10 more developer resources.'
plans:
- name: Dev Match Xyz Plans Pricing
  plan_count: 3
  slug: dev-match-xyz-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dev Match Xyz Domain Security
  slug: dev-match-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dev-match-xyz
tags:
- Engineering
- Hiring
- Deep Tech
- Artificial Intelligence
- Platform
website: https://dev-match.xyz/
---
