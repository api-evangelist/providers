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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL endpoint for analytics data and admin operations.
  name: Caybl AI GraphQL API
  slug: caybl-ai-graphql-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/caybl-ai/plans/caybl-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/caybl-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/caybl-ai/llms/caybl-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caybl-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/caybl-ai/well-known/caybl-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caybl-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/caybl-ai/hosts/caybl-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caybl-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/caybl-ai/vendors/caybl-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caybl-ai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://caybl.ai/support
- group: auth
  title: ''
  type: Security
  url: https://caybl.ai/security
- group: start
  title: ''
  type: Login
  url: https://caybl.ai/login
- group: company
  title: ''
  type: Blog
  url: https://caybl.ai/blog
- group: auth
  href: https://artifacts.apis.io/caybl-ai/security/caybl-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caybl-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caybl.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://caybl.ai/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://caybl.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caybl.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caybl.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.caybl.ai/graphql
  - status: 401
    url: https://api.caybl.ai/mcp
  - status: 403
    url: https://caybl.ai/mcp
  - status: 200
    url: https://caybl.ai/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: Caybl.ai provides a hosted MCP server that connects Google Analytics, Google Ads, Search Console, Bing, Microsoft Advertising, Tag Manager, and YouTube to AI assistants like Claude, ChatGPT, and Gemini. Users can ask natural‑language questions about their analytics data without needing tokens or exports, leveraging a simple login with Google. The service offers a free starter tier and paid plans for higher query volumes, targeting marketers and developers integrating analytics insights into AI workflows.
image: https://caybl.ai/og.png
layout: provider
modified: '2026-11-04'
name: Caybl.ai
nav: Providers
network: true
overview: 'Caybl.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Artificial Intelligence, Marketing, MCP, and Google.


  Caybl.ai''s developer surface includes support, engineering blog, documentation, pricing, and 11 more developer resources.'
plans:
- name: Caybl Ai Plans Pricing
  plan_count: 3
  slug: caybl-ai-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caybl Ai Domain Security
  slug: caybl-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caybl-ai
tags:
- Analytics
- Artificial Intelligence
- Marketing
- MCP
- Google
website: https://caybl.ai/
---
