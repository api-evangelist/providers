---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
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
- description: API for Aiqbee MCP integration, providing access to team knowledge via MCP servers.
  name: Aiqbee MCP API
  slug: aiqbee-mcp-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aiqbee-com/plans/aiqbee-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiqbee-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aiqbee-com/llms/aiqbee-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiqbee-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aiqbee-com/hosts/aiqbee-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiqbee-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiqbee-com/vendors/aiqbee-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiqbee-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.aiqbee.com/press/teams-app-launch
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiqbee
- group: auth
  href: https://artifacts.apis.io/aiqbee-com/security/aiqbee-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiqbee-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiqbee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aiqbee.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://aiqbee.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://aiqbee.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://aiqbee.com/about
coverage:
  checked: '2026-11-01'
  detail: Developers page is a JavaScript-rendered site with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://aiqbee.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Aiqbee offers an enterprise AI memory platform that lets organizations centralize documents, URLs and institutional knowledge into AI‑ready “Brains” that can be accessed from IDEs, Microsoft Teams and any MCP‑compatible application. The service includes governance controls, audit trails and data protection features, and is sold on a per‑user subscription starting at $15 per user per month.
image: https://www.aiqbee.com/og-image.png
layout: provider
modified: '2026-11-01'
name: Aiqbee
nav: Providers
network: true
overview: 'Aiqbee is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI memory, Enterprise Knowledge, LLM Governance, Teams Integration, and Developer Tools.


  Aiqbee''s developer surface includes documentation, pricing, engineering blog, getting-started guide, and 8 more developer resources.'
plans:
- name: Aiqbee Com Plans Pricing
  plan_count: 6
  slug: aiqbee-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 18.4
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiqbee Com Domain Security
  slug: aiqbee-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiqbee-com
tags:
- AI memory
- Enterprise Knowledge
- LLM Governance
- Teams Integration
- Developer Tools
- AI Marketplace
website: https://aiqbee.com/
---
