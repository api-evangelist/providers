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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Appllama provides a platform to discover app designs via its documentation and pricing pages.
  name: Appllama API
  slug: appllama-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/appllama-io/plans/appllama-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appllama-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/appllama-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/appllama-io/llms/appllama-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appllama-io-llms.txt
- group: other
  href: https://artifacts.apis.io/appllama-io/hosts/appllama-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appllama-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/appllama-io/vendors/appllama-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appllama-io-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://appllama.io/flows/news
- group: other
  title: ''
  type: Leadership
  url: https://appllama.io/flows/team
- group: docs
  title: ''
  type: Documentation
  url: https://appllama.io/flows/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://appllama.io/flows/onboarding
- group: auth
  href: https://artifacts.apis.io/appllama-io/security/appllama-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appllama-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appllama.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://appllama.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appllama.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appllama.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://appllama.io/support
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found despite documentation pages.
  evidence:
  - status: 404
    url: https://api.appllama.io/openapi.json
  - status: 404
    url: https://appllama.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Appllama provides a platform to discover winning app designs and build your own applications. It offers access to over 82,900 screens from more than 1,800 top-grossing iOS apps, covering categories such as Health & Fitness, Productivity, Education, and Entertainment. Users can explore pricing, screens, flows, UI elements, and leverage the MCP (Mobile Component Platform) to integrate designs into their products. The service includes a free tier, Pro Studio subscription, and extensive resources like documentation, pricing details, terms, privacy policy, and support.
image: https://appllama.io/og.png
layout: provider
modified: '2026-11-01'
name: Appllama
nav: Providers
network: true
overview: 'Appllama is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design, UI/UX, Mobile, Screens, and Marketplace.


  Appllama''s developer surface includes documentation, getting-started guide, pricing, support, and 11 more developer resources.'
plans:
- name: Appllama Io Plans Pricing
  plan_count: 4
  slug: appllama-io-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.5
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 25.0
  provenance:
    mcp: derived
    skills: unknown
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
security:
- kind: domain-security
  name: Appllama Io Domain Security
  slug: appllama-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: appllama-io
tags:
- Design
- UI/UX
- Mobile
- Screens
- Marketplace
website: https://appllama.io/
---
