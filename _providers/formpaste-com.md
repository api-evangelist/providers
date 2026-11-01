---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Formpaste provides a free contact form API for submitting forms via https://api.formpaste.com/submit and related endpoints.
  name: Formpaste API
  slug: formpaste-api
artifact_total: 6
asyncapis:
- description: ''
  name: Formpaste Com Webhooks
  slug: formpaste-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/formpaste-com/plans/formpaste-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/formpaste-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/formpaste-com/asyncapi/formpaste-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/formpaste-com-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/formpaste-com/authentication/formpaste-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/formpaste-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/formpaste-com/llms/formpaste-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/formpaste-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/formpaste-com/mcp/formpaste-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/formpaste-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/formpaste-com/hosts/formpaste-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/formpaste-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/formpaste-com/vendors/formpaste-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/formpaste-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/formpaste-com/security/formpaste-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/formpaste-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://formpaste.com/
- group: docs
  title: ''
  type: Documentation
  url: https://formpaste.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://formpaste.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://formpaste.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://formpaste.com/help
- group: company
  title: ''
  type: Blog
  url: https://formpaste.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://formpaste.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://formpaste.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://formpaste.com/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript and block direct spec discovery.
  evidence:
  - status: 200
    url: https://formpaste.com/docs/reference/options
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Formpaste provides a free contact form API that developers can integrate into HTML, Astro, React, Next.js, and other web projects. It offers spam filtering without CAPTCHAs, supports up to 250 submissions per month for free, and includes features like AI assistance, customizable templates, and a dashboard for managing submissions. The service aims to simplify form handling for developers and AI agents, providing a ready-to-use endpoint and documentation for quick integration.
image: https://formpaste.com/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.formpaste.com requiring an API key.
  name: formpaste-com MCP Server
  slug: formpaste-com-mcp-yml
modified: '2026-10-30'
name: formpaste-com
nav: Providers
network: true
overview: 'formpaste-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Form, Contact, and Free.


  The formpaste-com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  formpaste-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Formpaste Com Plans Pricing
  plan_count: 2
  slug: formpaste-com-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.2
    catalog_earned_first_party: 0.0
    catalog_gap: 70.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.5
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 47.6
    discoverability: 65.0
    operational_transparency: 7.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Formpaste Com Authentication
  slug: formpaste-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Formpaste Com Domain Security
  slug: formpaste-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: formpaste-com
tags:
- Company
- API
- Form
- Contact
- Free
website: https://formpaste.com/
---
