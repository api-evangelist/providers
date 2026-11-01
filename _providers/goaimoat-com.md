---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Model Context Protocol (MCP) servers providing AI agents data tools such as decision-maker lookup, company intel, search, scrape, and more.
  name: GoAI Moat MCP API
  slug: goai-moat-mcp-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/goaimoat-com/plans/goaimoat-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goaimoat-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/goaimoat-com/llms/goaimoat-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goaimoat-com-llms.txt
- group: other
  href: https://artifacts.apis.io/goaimoat-com/hosts/goaimoat-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goaimoat-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/goaimoat-com/security/goaimoat-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goaimoat-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goaimoat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.goaimoat.com
- group: docs
  title: ''
  type: Documentation
  url: https://goaimoat.com/blog/developers.html
- group: docs
  title: ''
  type: APIReference
  url: https://goaimoat.com/blog/developers.html
- group: start
  title: ''
  type: GettingStarted
  url: https://goaimoat.com/blog/developers.html
- group: company
  title: ''
  type: Blog
  url: https://goaimoat.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://goaimoat.com/blog/developers.html
- group: start
  title: ''
  type: SignUp
  url: https://goaimoat.gumroad.com/l/njpksu
- group: operate
  title: ''
  type: Support
  url: mailto:bd@hezhongth.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jayniebingyu-cyber
coverage:
  checked: '2026-10-29'
  detail: Documentation lists MCP endpoints but provides no machine‑readable OpenAPI, GraphQL, or AsyncAPI specifications.
  evidence:
  - status: 200
    url: https://mcp.goaimoat.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: GoAI Moat provides an AI‑visibility audit service that helps brands understand how they appear in AI‑generated answers across platforms like ChatGPT, Perplexity, Gemini and Google AI Overviews. Through a Model Context Protocol (MCP) server, developers can programmatically request audits, retrieve checklists, get fix‑priority recommendations and monitor usage. The service offers a free tier with one audit per email and a paid developer tier at $49 / month for unlimited access. Documentation, pricing, and a quick‑start guide are published on the company’s website.
image: https://placehold.co/600x400?text=GoAI+Moat
layout: provider
modified: '2026-10-29'
name: goaimoat-com
nav: Providers
network: true
overview: 'goaimoat-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Visibility, MCP, and SEO.


  goaimoat-com''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 7 more developer resources.'
plans:
- name: Goaimoat Com Plans Pricing
  plan_count: 2
  slug: goaimoat-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Goaimoat Com Rate Limits
  slug: goaimoat-com-rate-limits
scopes:
- name: Goaimoat Com Scopes
  scope_count: 0
  slug: goaimoat-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Goaimoat Com Authentication
  slug: goaimoat-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Goaimoat Com Domain Security
  slug: goaimoat-com-domain-security
  summary_line: TLSv1.3
slug: goaimoat-com
tags:
- Company
- AI
- Visibility
- MCP
- SEO
- Audit
website: https://goaimoat.com/
---
