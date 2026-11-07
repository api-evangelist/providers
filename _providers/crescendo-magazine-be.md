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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Crescendo Magazine content and services via MCP.
  name: Crescendo Magazine API
  slug: crescendo-magazine-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/crescendo-magazine-be/llms/crescendo-magazine-be-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crescendo-magazine-be-llms.txt
- group: other
  href: https://artifacts.apis.io/crescendo-magazine-be/hosts/crescendo-magazine-be-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crescendo-magazine-be-hosts.yml
- group: auth
  href: https://artifacts.apis.io/crescendo-magazine-be/security/crescendo-magazine-be-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crescendo-magazine-be-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crescendo-magazine.be/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found; only an MCP endpoint is available.
  evidence:
  - status: 200
    url: https://phono.crescendo-magazine.be/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Crescendo Magazine is a leading French online publication dedicated to classical music, offering news, reviews, artist interviews, concert listings, and in‑depth articles on orchestras, composers, and performances worldwide. The site provides rich editorial content, multimedia features, and a community for classical music enthusiasts, positioning itself as a reference source in the classical music domain.
layout: provider
modified: '2026-11-04'
name: Crescendo Magazine
nav: Providers
network: true
overview: Crescendo Magazine is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Classical, Media, Publication, and France.
random_paper: 19
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crescendo Magazine Be Domain Security
  slug: crescendo-magazine-be-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: crescendo-magazine-be
tags:
- Music
- Classical
- Media
- Publication
- France
website: https://crescendo-magazine.be/
---
