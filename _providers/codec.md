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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://codec.ai
- group: company
  title: ''
  type: Blog
  url: https://codec.ai/insights
- group: operate
  title: ''
  type: Support
  url: https://codec.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codec.ai/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codec-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codec-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Codec sells audience-intelligence consulting delivered through a proprietary internal platform; its public presence is a seven-page Webflow marketing site with no developer, docs, pricing or sign-up path, and the only non-www host that resolves (app.codec.ai, the customer platform login) fails at the origin with a Cloudflare 525 SSL handshake error, so there is no developer program to profile.
  evidence:
  - status: 404
    url: https://codec.ai/openapi.json
  - status: 404
    url: https://codec.ai/.well-known/api-catalog
  - status: 525
    url: https://app.codec.ai/
  - status: 404
    url: https://www.codec.ai/pricing
  - status: 200
    url: https://codec.ai/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Codec (CODEC AI) is an AI-powered audience-intelligence consultancy that helps ambitious global brands identify, understand, and activate high-value cultural communities to accelerate growth. Its work spans marketing strategy, brand and creative, and activation and measurement, powered by an award-winning proprietary AI platform, with case studies for enterprise brands such as Stella Artois, Frank's RedHot, and Moncler. Codec is a B2B consultancy rather than a developer-facing API provider — it publishes no public API, SDKs, or developer documentation. It was surfaced as a 500 Global portfolio company and added to the API Evangelist network for enrichment.
image: https://cdn.prod.website-files.com/65b296cf1c033f89b07ba342/65f48906d951be63c90d1342_open-graph.jpg
layout: provider
modified: '2026-08-13'
name: Codec
nav: Providers
network: true
overview: 'Codec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Audience Intelligence, Marketing, and Community.


  Codec''s developer surface includes engineering blog, support, and 4 more developer resources.'
plans:
- name: Codec Plans Pricing
  plan_count: 0
  slug: codec-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Codec Rate Limits
  slug: codec-rate-limits
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codec/refs/heads/main/screenshots/codec-2026-07-25T205919.png
security:
- kind: domain-security
  name: Codec Domain Security
  slug: codec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codec
tags:
- Company
- Artificial Intelligence
- Audience Intelligence
- Marketing
- Community
- Brand Strategy
- Consulting
website: https://codec.ai
---
