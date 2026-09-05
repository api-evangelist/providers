---
access_model:
  confidence: medium
  label: Demo-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://joinground.com/book-a-demo
  - https://apps.shopify.com/ground
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
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ground-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinground.com/
- group: start
  title: ''
  type: Login
  url: https://app.joinground.com/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinground.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinground.com/legal/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://joinground.com/documentation/what-is-ground
- group: company
  title: ''
  type: Blog
  url: https://joinground.com/blog
- group: operate
  title: ''
  type: Support
  url: https://joinground.com/faq
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ground-ai-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/ground-ai-robots.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ground-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ground-ai-rate-limits.yml
coverage:
  checked: '2026-08-14'
  detail: 'Ground ships its AI revenue agents as managed connectors into Shopify, Klaviyo, Attentive and Mailchimp and markets a "no dev time" setup, so there is nothing to call: joinground.com/api, /docs, /developers and /openapi.json all return 404, no api. or docs. subdomain resolves, and the only machine-readable documents on the domain are llms.txt, robots.txt and sitemap.xml.'
  evidence:
  - status: 404
    url: https://joinground.com/developers
  - status: 404
    url: https://joinground.com/openapi.json
  - status: 404
    url: https://joinground.com/api-docs
  - status: 404
    url: https://joinground.com/.well-known/agent-card.json
  - status: 200
    url: https://joinground.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Ground — legally Cheres, Inc (dba Ground), 20 Exchange Place, New York — is an AI-native revenue platform for consumer and e-commerce brands, delivering autonomous "AI revenue agents" that work across the customer lifecycle. Its named agents are Greet AI for first-touch conversion of new visitors, ReCartify for identity resolution, ReBeat AI for repeat purchase and winback, and Terra for repetitive marketer tasks. Ground positions itself as Growth-as-a-Service, plugging into a brand''s existing stack — Shopify, Adobe Commerce, WooCommerce, Klaviyo, Mailchimp, Attentive, Postscript, Yotpo, Meta Ads and Amped — with a stated 15-minute, no-developer setup. It is Techstars-backed and ships a free Shopify App Store listing. Ground publishes product documentation, a blog, an FAQ and a machine-readable llms.txt, and its robots.txt carries an explicit Cloudflare Content Signals AI-use reservation (search=yes, ai-train=no, use=reference). It publishes no public API, OpenAPI, MCP server,
  SDK, webhook catalog or developer portal: the platform is delivered as managed connectors into the tools a brand already runs, and every commercial path terminates in a demo booking.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ground-ai.png
layout: provider
modified: '2026-08-14'
name: Ground AI
nav: Providers
network: true
overview: 'Ground AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Artificial Intelligence, Commerce, and Revenue.


  Ground AI''s developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
plans:
- name: Ground Ai Plans Pricing
  plan_count: 1
  slug: ground-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Ground Ai Rate Limits
  slug: ground-ai-rate-limits
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ground-ai/refs/heads/main/screenshots/ground-ai-2026-07-25T220342.png
security:
- kind: domain-security
  name: Ground Ai Domain Security
  slug: ground-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ground-ai
tags:
- Company
- E-Commerce
- Artificial Intelligence
- Commerce
- Revenue
- Retention
- Marketing Automation
- AI Agents
- Growth
- Shopify
- Agentic Commerce
website: https://joinground.com/
---
