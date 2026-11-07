---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Com.Bot API provides messaging automation across WhatsApp, Instagram Direct, Facebook Messenger, Google RCS, and SMS via a unified platform.
  name: Com.Bot API
  slug: com-bot-api
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/com-bot/vendors/com-bot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/com-bot-vendors.yml
- group: operate
  href: https://artifacts.apis.io/com-bot/rate-limits/com-bot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/com-bot-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/com-bot/plans/com-bot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/com-bot-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/com-bot/llms/com-bot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/com-bot-llms.txt
- group: other
  href: https://artifacts.apis.io/com-bot/hosts/com-bot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/com-bot-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.com.bot/
- group: auth
  href: https://artifacts.apis.io/com-bot/security/com-bot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/com-bot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://com.bot/
- group: docs
  title: ''
  type: APIReference
  url: https://com.bot/whatsapp/
- group: start
  title: ''
  type: GettingStarted
  url: https://v3.com.bot/register
- group: commercial
  title: ''
  type: Pricing
  url: https://com.bot/pricing/
- group: operate
  title: ''
  type: Support
  url: https://com.bot/contact/
- group: company
  title: ''
  type: Blog
  url: https://blog.com.bot/
- group: start
  title: ''
  type: SignUp
  url: https://v3.com.bot/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://com.bot/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://com.bot/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/com-bot/mcp/com-bot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/com-bot-mcp.yml
created: '2026-10-30'
description: Com.Bot is a messaging automation platform founded in 2021 by Akshay Sharda and owned by Com Bot AI Limited in Surat, India. It offers an official Meta Business Partner solution for WhatsApp Business API, Instagram Direct Messaging, Facebook Messenger, Google RCS, and bulk SMS, providing a shared inbox, AI chatbot builder, broadcast capabilities, and payment integration. The service supports over 50,000 active customers across more than 50 countries, including 100+ government bodies, processing over 100 million messages daily. Com.Bot enables businesses to automate customer engagement across multiple channels from a single platform.
image: https://com.bot/wp-content/themes/combot/assets/img/combot-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at com.bot.
  name: com-bot MCP Server
  slug: com-bot-mcp-yml
modified: '2026-10-30'
name: com-bot
nav: Providers
network: true
overview: 'com-bot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Automation, WhatsApp, Software-as-a-Service, and India.


  com-bot''s developer surface includes documentation, API reference, getting-started guide, pricing, support, engineering blog, signup flow, and 10 more developer resources.'
plans:
- name: Com Bot Plans Pricing
  plan_count: 3
  slug: com-bot-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Com Bot Rate Limits
  slug: com-bot-rate-limits
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 32.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/com-bot/com-bot-2026-11-03T124910.png
security:
- kind: domain-security
  name: Com Bot Domain Security
  slug: com-bot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: com-bot
tags:
- Messaging
- Automation
- WhatsApp
- Software-as-a-Service
- India
website: https://com.bot/
---
