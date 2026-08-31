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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/multiply-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gomultiply.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gomultiply.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gomultiply.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.gomultiply.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/multiply-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/multiply-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Multiply sells a human-plus-AI managed media service, not software — its own llms.txt enumerates nine marketing pages and eight browser games and names no API, docs host or developer surface, and api./docs./developer./developers.gomultiply.com have no DNS records at all.
  evidence:
  - status: 200
    url: https://www.gomultiply.com/llms.txt
  - status: 200
    url: https://www.gomultiply.com/sitemap.xml
  - status: 404
    url: https://www.gomultiply.com/openapi.json
  - status: 404
    url: https://www.gomultiply.com/.well-known/agent-card.json
  - status: 404
    url: https://app.getkalos.com/login
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Multiply is an AI-native media agency built specifically for B2B companies, pairing human paid-media strategists with a fleet of 25+ specialized AI agents to run and continuously optimize LinkedIn and Google Search advertising. Its "Self-Learning Advertising" platform plugs into a company's own data — sales call recordings (e.g. Gong), CRM closed-won outcomes, case studies, website content, competitive kill sheets and product documentation — and runs hundreds of structured ad experiments that refine audiences, copy and creative from real revenue signals. Multiply is a managed service (not a self-serve API product), founded by Matt Jayson (ex-Google, ex-Brex) and Ashish Warty (ex-HackerOne SVP Engineering, ex-Dropbox), and raised $9.5M led by Mayfield in March 2026. It was added to the API Evangelist network as a Mayfield portfolio company; two enrichment passes confirmed it publishes no public API, developer documentation, SDK, or /.well-known/ discovery surface. It does publish
  an llms.txt and three named service tiers — Growth (from $6K/mo), Scale (from $12K/mo) and Enterprise — priced against monthly ad spend rather than API usage.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/multiply.png
layout: provider
modified: '2026-08-12'
name: Multiply
nav: Providers
network: true
overview: 'Multiply is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, B2B, and Artificial Intelligence.


  Multiply''s developer surface includes pricing, engineering blog, and 5 more developer resources.'
plans:
- name: Multiply Plans Pricing
  plan_count: 3
  slug: multiply-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/multiply/refs/heads/main/screenshots/multiply-2026-08-07T184437.png
security:
- kind: domain-security
  name: Multiply Domain Security
  slug: multiply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: multiply
tags:
- Company
- Advertising
- Marketing
- B2B
- Artificial Intelligence
- Media Agency
- Paid Media
- Marketing Technology
- AI Agents
website: https://www.gomultiply.com/
---
