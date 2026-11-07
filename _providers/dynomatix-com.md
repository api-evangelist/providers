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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dynomatix-com/well-known/dynomatix-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dynomatix-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dynomatix-com/hosts/dynomatix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynomatix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dynomatix-com/vendors/dynomatix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynomatix-com-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://dynomatix.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dynomatix
- group: auth
  href: https://artifacts.apis.io/dynomatix-com/security/dynomatix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynomatix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dynomatix.com/
coverage:
  checked: '2026-11-06'
  detail: The provider's MCP endpoint only allows POST, returning 405 on GET, and no OpenAPI or docs were found.
  evidence:
  - status: 405
    url: https://dynomatix.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Dynamatix builds and operates AI agent systems for businesses, moving agents from pilot to production and maintaining them. It offers managed hosting for the open-source OpenClaw assistant, a website chat button (FindWise) that answers from a company's own material, and a Slack social‑bookmarking tool (Prosvita). The company has been building software since 2012 and focuses on agent infrastructure, retrieval over existing pages, and taking over failing software.
image: https://dynomatix.com/assets/og.png
layout: provider
modified: '2026-11-06'
name: Dynamatix
nav: Providers
network: true
overview: 'Dynamatix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Managed Hosting, Retrieval, and Software migration.


  Dynamatix''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 5.3
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
  name: Dynomatix Com Domain Security
  slug: dynomatix-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: dynomatix-com
tags:
- AI Agents
- Managed Hosting
- Retrieval
- Software migration
website: https://dynomatix.com/
---
