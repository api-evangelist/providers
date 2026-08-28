---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://grotto.ai/
- group: company
  title: ''
  type: Blog
  url: https://grotto.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grotto.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grotto.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/grotto-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.grotto.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grotto-ai-domain-security.yml
- group: company
  title: ''
  type: About
  url: https://grotto.ai/about-us
- group: company
  title: ''
  type: Press
  url: https://grotto.ai/press
- group: other
  title: ''
  type: CaseStudies
  url: https://grotto.ai/use-cases/weidner
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/grotto
- group: operate
  title: ''
  type: Contact
  url: mailto:info@grotto.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/grotto-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/grotto-ai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/grotto-ai-llms.txt
coverage:
  checked: '2026-08-14'
  detail: Grotto sells a demo-led leasing-coaching product with no developer surface at all — its own sitemap.xml lists twelve marketing pages and nothing else, /docs, /api, /developers and /pricing all 404, no api./docs./developer. subdomain resolves in DNS, and the product itself runs as per-customer web-app tenants (demo.grotto.ai, a Solara Python app) that publish no endpoints, spec or webhook catalog.
  evidence:
  - status: 200
    url: https://grotto.ai/sitemap.xml
  - status: 404
    url: https://grotto.ai/developers
  - status: 404
    url: https://grotto.ai/openapi.json
  - status: 404
    url: https://grotto.ai/.well-known/agent-card.json
  - status: 404
    url: https://demo.grotto.ai/openapi.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Grotto AI is an AI sales-coaching platform purpose-built for the multifamily apartment leasing industry. Founded by former EvolutionIQ leaders Nick Deveau (CEO) and Ben Epstein (CTO), Grotto delivers real-time call guidance, tour and call coaching, and prospect-lifecycle support across email and text that help leasing agents handle objections, book tours, and convert more leads to recover net operating income and asset value. The platform works alongside multifamily systems such as Entrata, Funnel, and Yardi and is used by operators including Weidner Apartment Homes and Hillpointe. Grotto is SOC 2 Type II and ISO 27701 certified and Fair Housing compliant. It is backed by ICONIQ. Grotto does not publish a public developer API, SDK, or documentation surface; it is a demo-led enterprise SaaS product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grotto-ai.png
layout: provider
modified: '2026-08-14'
name: Grotto AI
nav: Providers
network: true
overview: 'Grotto AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Multifamily, Leasing, and Sales Coaching.


  Grotto AI''s developer surface includes engineering blog and 14 more developer resources.'
plans:
- name: Grotto Ai Plans Pricing
  plan_count: 0
  slug: grotto-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Grotto Ai Rate Limits
  slug: grotto-ai-rate-limits
score:
  band: emerging
  composite: 12.8
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grotto-ai/refs/heads/main/screenshots/grotto-ai-2026-07-25T220338.png
security:
- kind: domain-security
  name: Grotto Ai Domain Security
  slug: grotto-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Grotto Ai Trust Center
  slug: grotto-ai-trust-center
  summary_line: SOC 2 Type II, ISO 27701
slug: grotto-ai
tags:
- Company
- Artificial Intelligence
- Multifamily
- Leasing
- Sales Coaching
- PropTech
- Real-Estate
- Conversation Intelligence
website: https://grotto.ai/
---
