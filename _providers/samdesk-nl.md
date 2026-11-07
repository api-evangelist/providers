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
    mcp_server: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Customer service API for e‑commerce teams, providing ticketing, multilingual support, and AI‑drafted replies.
  name: SamDesk API
  slug: samdesk-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/samdesk-nl/plans/samdesk-nl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/samdesk-nl-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/samdesk-nl/changelog/samdesk-nl-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/samdesk-nl-changelog.yml
- group: agent
  href: https://artifacts.apis.io/samdesk-nl/llms/samdesk-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/samdesk-nl-llms.txt
- group: agent
  href: https://artifacts.apis.io/samdesk-nl/mcp/samdesk-nl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/samdesk-nl-mcp.yml
- group: agent
  href: https://artifacts.apis.io/samdesk-nl/well-known/samdesk-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/samdesk-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/samdesk-nl/hosts/samdesk-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/samdesk-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/samdesk-nl/vendors/samdesk-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/samdesk-nl-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://samdesk.nl/nl/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://samdesk.nl/nl/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://samdesk.nl/en/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://samdesk.nl/en/guides/
- group: operate
  title: ''
  type: ChangeLog
  url: https://samdesk.nl/nl/help/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://samdesk.nl/nl/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://samdesk.nl/nl/help/getting-started/
- group: auth
  href: https://artifacts.apis.io/samdesk-nl/security/samdesk-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/samdesk-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://samdesk.nl/
- group: start
  title: ''
  type: SignUp
  url: https://samdesk.nl/accounts/signup/
- group: operate
  title: ''
  type: Support
  url: https://samdesk.nl/en/contact/
coverage:
  checked: '2026-10-30'
  detail: Public documentation exists but no machine‑readable OpenAPI or other spec is published.
  evidence:
  - status: 200
    url: https://samdesk.nl/en/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: SamDesk provides AI-powered customer service software for e‑commerce teams, combining CRM, help‑desk ticketing, multilingual support, and AI‑drafted replies in a unified inbox. The platform integrates email, chat, and order data, enabling faster, language‑agnostic support across channels.
image: https://samdesk.nl/static/marketing/screenshots/dashboard-thread.32b860f53a36.png
layout: provider
mcp_servers:
- description: Remote MCP server at samdesk.nl requiring OAuth.
  name: samdesk-nl MCP Server
  slug: samdesk-nl-mcp-yml
modified: '2026-10-30'
name: samdesk-nl
nav: Providers
network: true
overview: 'samdesk-nl is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Help Desk, E-Commerce, and Artificial Intelligence.


  samdesk-nl''s developer surface includes changelog, pricing, documentation, engineering blog, getting-started guide, signup flow, support, and 11 more developer resources.'
plans:
- name: Samdesk Nl Plans Pricing
  plan_count: 3
  slug: samdesk-nl-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 29.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/samdesk-nl/samdesk-nl-2026-11-03T142655.png
security:
- kind: domain-security
  name: Samdesk Nl Domain Security
  slug: samdesk-nl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: samdesk-nl
tags:
- Company
- CRM
- Help Desk
- E-Commerce
- Artificial Intelligence
website: https://samdesk.nl/
---
