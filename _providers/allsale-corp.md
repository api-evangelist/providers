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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allsale-corp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allsale.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://allsale.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://brand.allsale.ai/signup
- group: start
  title: ''
  type: Login
  url: https://brand.allsale.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allsale.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allsale.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:sale@allsale.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ALLSALE-Corp
- group: commercial
  title: ''
  type: Plans
  url: plans/allsale-corp-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allsale-corp-llms.txt
coverage:
  checked: '2026-08-13'
  detail: ALLSALE sells API access only as an unpriced bullet inside its custom-priced Enterprise tier ("White-label / API / custom workflows", "Custom API integrations") with no developer portal, reference or spec anywhere — allsale.ai/docs and allsale.ai/api both 404, and every /openapi.json, /graphql, /mcp and /.well-known/* path on all six ALLSALE-operated hosts 404s.
  evidence:
  - status: 200
    url: https://allsale.ai/#pricing
  - status: 404
    url: https://allsale.ai/docs
  - status: 404
    url: https://allsale.ai/api
  - status: 404
    url: https://www.allsale.ai/openapi.json
  - status: 404
    url: https://brand.allsale.ai/api/openapi.json
  - status: 404
    url: https://www.allsale.ai/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: ALLSALE Corp. operates ALLSALE, a TikTok Shop growth and creator-marketing automation platform for consumer brands. It runs three AI agents — a Creator Discovery Agent that finds and engages relevant TikTok creators, a Budget Optimization Agent that recommends budget allocation and commission adjustments, and a Performance Analyst Agent that tracks GMV and predicts results — automating the full workflow from creator discovery and outreach through performance tracking and ROI analysis. The company is a 500 Global portfolio company and reports 100K+ creators engaged and $50M+ in customer revenue generated across its brand clients. Plans run from a $399/month Starter tier to a $599/month Pro tier, with custom Enterprise pricing offering unlimited messaging, multi-brand support, and white-label options.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allsale-corp.png
layout: provider
modified: '2026-08-13'
name: ALLSALE Corp.
nav: Providers
network: true
overview: 'ALLSALE Corp. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, TikTok Shop, Creator Marketing, Influencer Marketing, and Social Commerce.


  ALLSALE Corp.''s developer surface includes pricing, signup flow, support, and 8 more developer resources.'
plans:
- name: Allsale Corp Plans Pricing
  plan_count: 3
  slug: allsale-corp-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Allsale Corp Rate Limits
  slug: allsale-corp-rate-limits
score:
  band: emerging
  composite: 22.5
  delta: 7.7
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/allsale-corp/refs/heads/main/screenshots/allsale-corp-2026-07-25T195716.png
security:
- kind: domain-security
  name: Allsale Corp Domain Security
  slug: allsale-corp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allsale-corp
tags:
- Company
- TikTok Shop
- Creator Marketing
- Influencer Marketing
- Social Commerce
- E-commerce
- Marketing Automation
- AI Agents
website: https://allsale.ai
---
