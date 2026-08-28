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
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://rankscience.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rankscience.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.rankscience.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rankscience.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rankscience.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rankscience
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rankscience-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rankscience-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rankscience-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rankscience-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rankscience-rate-limits.yml
coverage:
  checked: '2026-08-13'
  detail: RankScience is now an SEO/AI-visibility services agency on a Webflow marketing site with no developer program; the platform-era hosts api.rankscience.com and dashboard.rankscience.com still resolve to Cloudflare but return 530 origin errors, and status.rankscience.com redirects to an inactive Statuspage.
  evidence:
  - status: 530
    url: https://api.rankscience.com/openapi.json
  - status: 404
    url: https://www.rankscience.com/openapi.json
  - status: 404
    url: https://www.rankscience.com/.well-known/agent-card.json
  - status: 200
    url: https://status.rankscience.com/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: RankScience is a San Francisco based SEO and AI-visibility agency (RankScience LLC) that helps startups, SaaS companies, and enterprises grow search traffic through foundational and technical SEO, strategic content, and link building, alongside next-generation AI-search optimization services (Generative Engine Optimization, Large Language Model Optimization, and Answer Engine Optimization) for platforms like ChatGPT, Claude, and Perplexity. It began as a YC-backed SEO A/B testing platform and now operates as a services agency. RankScience does not currently publish a public developer API, SDKs, or API documentation; this profile captures its public web and AI-discovery surface (a published /llms.txt and domain security posture).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rankscience.png
layout: provider
modified: '2026-08-13'
name: RankScience
nav: Providers
network: true
overview: 'RankScience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, SEO, AI Visibility, and Generative Engine Optimization.


  RankScience''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Rankscience Plans Pricing
  plan_count: 0
  slug: rankscience-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Rankscience Rate Limits
  slug: rankscience-rate-limits
score:
  band: emerging
  composite: 11.7
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Rankscience Domain Security
  slug: rankscience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rankscience
tags:
- Company
- Enterprise Saas
- SEO
- AI Visibility
- Generative Engine Optimization
- Content Marketing
- Marketing Agency
website: https://rankscience.com/
---
