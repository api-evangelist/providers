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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Draftly AI Blog Writer service
  name: Draftly Blog API
  slug: draftly-blog-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/draftly-blog/plans/draftly-blog-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/draftly-blog-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/draftly-blog/llms/draftly-blog-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/draftly-blog-llms.txt
- group: other
  href: https://artifacts.apis.io/draftly-blog/hosts/draftly-blog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/draftly-blog-hosts.yml
- group: other
  href: https://artifacts.apis.io/draftly-blog/vendors/draftly-blog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/draftly-blog-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.draftly.blog/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.draftly.blog/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.draftly.blog/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.draftly.blog/blog
- group: auth
  href: https://artifacts.apis.io/draftly-blog/security/draftly-blog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/draftly-blog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://draftly.blog/
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered despite probing known API hosts.
  evidence:
  - status: 0
    url: https://api.draftly.blog/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Draftly provides an AI-powered blog writing service that generates SEO‑ready posts in a user’s brand voice. It reads a website, selects timely industry topics, writes a draft with meta data, and can publish directly to platforms such as WordPress, Shopify, Webflow, Ghost, Squarespace, or HubSpot. The tool is aimed at small businesses and marketing teams that need regular, on‑brand blog content without manual research or editing.
image: https://www.draftly.blog/opengraph-image.jpg?opengraph-image.3lh0gr9-nzvdi.jpg
layout: provider
modified: '2026-11-05'
name: Draftly
nav: Providers
network: true
overview: 'Draftly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Writing, SEO, and Content Marketing.


  Draftly''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Draftly Blog Plans Pricing
  plan_count: 4
  slug: draftly-blog-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Draftly Blog Domain Security
  slug: draftly-blog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: draftly-blog
tags:
- AI Writing
- SEO
- Content Marketing
website: https://draftly.blog/
---
