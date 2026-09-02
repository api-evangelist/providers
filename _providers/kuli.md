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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kuli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kuli.one
- group: company
  title: ''
  type: About
  url: https://kuli.one/about
- group: company
  title: ''
  type: Blog
  url: https://kuli.one/blog
- group: operate
  title: ''
  type: Contact
  url: https://kuli.one/contact
- group: operate
  title: ''
  type: Support
  url: https://kuli.one/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kuli.one/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kuli.one/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kuliai
- group: other
  title: ''
  type: Glossary
  url: https://kuli.one/glossary
- group: build
  title: ''
  type: Tools
  url: https://kuli.one/tools
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kuli-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Kuli ships only an end-user application — its sitemap's 66 URLs are marketing, blog, glossary and calculator pages with no developer, API or documentation entry, and the api/developer/developers/docs/mcp subdomains of kuli.one do not resolve at all; the one real HTTP API found, the Kuli Discovery app's own FastAPI backend, has its automatic /openapi.json and /docs deliberately disabled in production and answers 401 to anyone without an app session.
  evidence:
  - status: 200
    url: https://kuli.one/openapi.json
  - status: 200
    url: https://kuli.one/sitemap.xml
  - status: 404
    url: https://kuli-discovery-backend-prod.livelyocean-00d2887a.westeurope.azurecontainerapps.io/openapi.json
  - status: 401
    url: https://kuli-discovery-backend-prod.livelyocean-00d2887a.westeurope.azurecontainerapps.io/api/settings/profile
  - status: 200
    url: https://kuli.one/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Kuli is an AI agent for influencer marketing, built for consumer brands. It runs the full creator marketing lifecycle end to end — discovery, vetting, outreach, and reporting — so a small marketing team ships like a much larger one. Unlike platforms that filter creators on metadata such as follower counts and engagement rates, Kuli's agent watches actual creator videos frame by frame across TikTok and Instagram, assessing brand safety, content style, audience signals, and brand fit, then drafts personalized outreach in the brand's own voice and reports campaign ROI on a schedule. Founded in 2025 and headquartered in Levallois-Perret, Paris, Kuli is a Y Combinator company. As of this profile Kuli publishes no public API, developer portal, or SDKs — its only machine-readable surface is an llms.txt.
image: https://framerusercontent.com/assets/aUo3Rkr9XBqPsT5tjDnjU2NPzI.png
layout: provider
modified: '2026-08-13'
name: Kuli
nav: Providers
network: true
overview: 'Kuli is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Marketing, Artificial Intelligence, and Creator Economy.


  Kuli''s developer surface includes engineering blog, support, tooling, and 9 more developer resources.'
plans:
- name: Kuli Plans Pricing
  plan_count: 0
  slug: kuli-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Kuli Rate Limits
  slug: kuli-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kuli/refs/heads/main/screenshots/kuli-2026-07-25T224328.png
security:
- kind: domain-security
  name: Kuli Domain Security
  slug: kuli-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kuli
tags:
- Company
- Influencer Marketing
- Marketing
- Artificial Intelligence
- Creator Economy
- Brand Safety
- Video Analysis
- Social-Media
website: https://kuli.one
---
