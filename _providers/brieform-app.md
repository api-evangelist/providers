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
    event_surface_described: unknown
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
  score: 26.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/brieform-app/plans/brieform-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brieform-app-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/brieform-app/changelog/brieform-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brieform-app-changelog.yml
- group: agent
  href: https://artifacts.apis.io/brieform-app/llms/brieform-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brieform-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/brieform-app/mcp/brieform-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brieform-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/brieform-app/well-known/brieform-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brieform-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/brieform-app/hosts/brieform-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brieform-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/brieform-app/vendors/brieform-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brieform-app-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://brieform.app/features/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brieform.app/terms
- group: start
  title: ''
  type: SignUp
  url: https://brieform.app/register
- group: auth
  title: ''
  type: Security
  url: https://brieform.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brieform.app/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://brieform.app/changelog
- group: auth
  href: https://artifacts.apis.io/brieform-app/security/brieform-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brieform-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brieform.app/
- group: docs
  title: ''
  type: Documentation
  url: https://brieform.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://brieform.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://brieform.app/blog
- group: other
  title: ''
  type: SignIn
  url: https://brieform.app/login
coverage:
  checked: '2026-11-03'
  detail: Documentation is HTML only and no OpenAPI/AsyncAPI/GraphQL spec was found on the provider's hosts.
  evidence:
  - status: 200
    url: https://brieform.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Brieform is an AI‑powered form builder that lets you describe a form to your favorite large language model (Claude, ChatGPT, Cursor, etc.) and automatically creates a shareable web form. The form works like any normal web page, and responses can be read back into the AI for further processing. It offers a free tier to get started and integrates with multiple AI platforms.
image: https://brieform.app/opengraph-image?ac8f4f79061d0914
layout: provider
mcp_servers:
- description: Remote MCP server at brieform.app requiring OAuth.
  name: Brieform MCP Server
  slug: brieform-app-mcp-yml
modified: '2026-11-03'
name: Brieform
nav: Providers
network: true
overview: 'Brieform is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Form Builder, Freelancers, Agencies, Web Forms, and No-Code.


  Brieform''s developer surface includes changelog, signup flow, documentation, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Brieform App Plans Pricing
  plan_count: 3
  slug: brieform-app-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.3
    operational_transparency: 17.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brieform App Domain Security
  slug: brieform-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: brieform-app
tags:
- Form Builder
- Freelancers
- Agencies
- Web Forms
- No-Code
website: https://brieform.app/
---
