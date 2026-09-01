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
- group: company
  title: ''
  type: Website
  url: https://newneek.co
- group: start
  title: ''
  type: SignUp
  url: https://newneek.co/subscribe
- group: operate
  title: ''
  type: Support
  url: https://newneek.co/help
- group: company
  title: ''
  type: Blog
  url: https://blog.naver.com/newneek_official
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newneek.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newneek.co/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newneek-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newneek
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newneek-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Newneek is a Korean consumer newsletter and media app with no developer program at all — 26 discovery paths across five hosts all returned honest 404s, and its one live API origin (api.newneek.co, nginx, answers /health/) is an undocumented internal backend for the mobile and web apps that 404s every conventional spec path.
  evidence:
  - status: 404
    url: https://api.newneek.co/openapi.json
  - status: 404
    url: https://api.newneek.co/.well-known/agent-card.json
  - status: 404
    url: https://newneek.co/.well-known/security.txt
  - status: 404
    url: https://newneek.co/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Newneek (뉴닉) is a South Korean knowledge and media platform that makes news and current events easy and fun to follow. Founded by Kim So-yeon and operated by Newneek Co., Ltd. from Seoul''s Mapo district, the company is best known for its conversational email newsletter delivered by the mascot "Gosuni," alongside a mobile app, a Slack news bot, and active social channels. Newneek is a consumer content brand rather than an API producer: it publishes no public developer portal, API documentation, or machine-readable API surface. It appears in the API Evangelist network as a 500 Global portfolio company, and this profile captures its identity and domain-security posture. Enrichment probes found no OpenAPI, well-known, OAuth, MCP, or webhook surface to harvest.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newneek.png
layout: provider
modified: '2026-08-13'
name: Newneek
nav: Providers
network: true
overview: 'Newneek is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Newsletter, News, and Content.


  Newneek''s developer surface includes signup flow, support, engineering blog, and 6 more developer resources.'
plans:
- name: Newneek Plans Pricing
  plan_count: 0
  slug: newneek-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Newneek Rate Limits
  slug: newneek-rate-limits
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newneek/refs/heads/main/screenshots/newneek-2026-08-07T185122.png
security:
- kind: domain-security
  name: Newneek Domain Security
  slug: newneek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: newneek
tags:
- Company
- Media
- Newsletter
- News
- Content
- Consumer
- South Korea
website: https://newneek.co
---
