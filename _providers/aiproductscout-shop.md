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
- description: 'Endpoints for merchants and AI developers: connect agents over MCP, publish a product feed, and check AI visibility programmatically.'
  name: Shop2LLM API
  slug: shop2llm-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aiproductscout-shop/plans/aiproductscout-shop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiproductscout-shop-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aiproductscout-shop/conformance/aiproductscout-shop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiproductscout-shop-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiproductscout-shop/llms/aiproductscout-shop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiproductscout-shop-llms.txt
- group: other
  href: https://artifacts.apis.io/aiproductscout-shop/hosts/aiproductscout-shop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiproductscout-shop-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiproductscout-shop/vendors/aiproductscout-shop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiproductscout-shop-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aiproductscout-shop/security/aiproductscout-shop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiproductscout-shop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiproductscout.shop/
- group: docs
  title: ''
  type: Documentation
  url: https://aiproductscout.shop/fincore/v1/page/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aiproductscout.shop/fincore/v1/page/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://aiproductscout.shop/fincore/v1/page/prolanding
- group: company
  title: ''
  type: Blog
  url: https://aiproductscout.shop/fincore/v1/page/blog/index
- group: commercial
  title: ''
  type: Pricing
  url: https://aiproductscout.shop/fincore/v1/page/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiproductscout.shop/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiproductscout.shop/privacy
coverage:
  checked: '2026-11-01'
  detail: Provider documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://aiproductscout.shop/fincore/v1/page/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Shop2LLM provides a SaaS solution that makes e‑commerce stores discoverable to AI assistants such as ChatGPT, Claude, Gemini and Perplexity. It offers automatic llms.txt generation, JSON‑LD product schema, AI crawler detection, and analytics on AI‑driven traffic. The platform supports WordPress, Shopify, Magento and other platforms, with a free tier and a Pro tier at $9/month offering multi‑platform AI visibility, advanced tools, and MCP API access.
layout: provider
modified: '2026-11-01'
name: Shop2LLM
nav: Providers
network: true
overview: 'Shop2LLM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Software-as-a-Service, E-Commerce, Marketing, and Visibility.


  Shop2LLM''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Aiproductscout Shop Plans Pricing
  plan_count: 3
  slug: aiproductscout-shop-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 26.7
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiproductscout Shop Domain Security
  slug: aiproductscout-shop-domain-security
  summary_line: TLSv1.3
slug: aiproductscout-shop
tags:
- Artificial Intelligence
- Software-as-a-Service
- E-Commerce
- Marketing
- Visibility
website: https://aiproductscout.shop/
---
