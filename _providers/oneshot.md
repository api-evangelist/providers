---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - https://www.oneshot.ai/pricing
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.oneshot.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.oneshot.ai/getting-started-with-oneshot
- group: start
  title: ''
  type: GettingStarted
  url: https://www.oneshot.ai/getting-started-with-oneshot
- group: company
  title: ''
  type: Blog
  url: https://www.oneshot.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oneshot.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.oneshot.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oneshot.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oneshot.ai/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oneshot-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/oneshot-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.oneshot.ai
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oneshot-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oneshot-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/oneshot-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/oneshot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oneshot-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oneshot-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oneshot-llms.txt
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.oneshot.ai/aup
coverage:
  checked: '2026-08-13'
  detail: OneShot ships only an end-user web app and Chrome extension; its own site has no developer, API or docs page (all 404, and none of the 180 URLs in its sitemap is a reference page), api.oneshot.ai has no public DNS record at all, and app.oneshot.ai answers 200 with the same SPA shell for every path including /openapi.json.
  evidence:
  - status: 404
    url: https://www.oneshot.ai/api
  - status: 404
    url: https://www.oneshot.ai/developers
  - status: 404
    url: https://www.oneshot.ai/llms.txt
  - status: 404
    url: https://www.oneshot.ai/.well-known/agent-card.json
  - status: 0
    url: https://api.oneshot.ai/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'OneShot (oneshot.ai) is an autonomous outbound sales prospecting platform that uses generative AI, machine learning, and reinforcement learning to automate the manual work of B2B prospecting. It sources ideal-customer-profile (ICP) leads from 35+ data providers, manages email and domain health, generates hyper-personalized messaging for email and LinkedIn, and can run fully autonomous 24/7 outreach that books qualified meetings. The product ships as a Chrome extension and a web application, and integrates natively with HubSpot, Salesforce, Apollo, Salesloft, and Outreach. Founded in London by Gautam Rishi (CEO) and Venki Pola (CTO), OneShot is backed by 42Cap, Seedcamp, and Addvia Ventures. Commercially it publishes three monthly tiers ($49/$99, $399 and $1,995), all sold through a "Book a Demo" motion with no self-serve checkout, and it operates a Vanta-hosted trust center at security.oneshot.ai alongside published GDPR and data-processing terms. This profile was surfaced
  as a Seedcamp portfolio company and enriched from OneShot''s public surface. OneShot exposes NO public developer API: full contract discovery across www.oneshot.ai, the apex, app.oneshot.ai and every candidate api/docs/mcp subdomain found no OpenAPI, AsyncAPI, GraphQL SDL, MCP server or A2A agent card, and no developer portal or API reference exists. Its only first-party distributed package is an end-user Chrome extension.'
image: https://cdn.prod.website-files.com/64c2dbb9c4026648656ec081/68643037866f61678f86bb47_oneshot_meta_preview_atlas.png
layout: provider
modified: '2026-08-13'
name: OneShot
nav: Providers
network: true
overview: 'OneShot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Sales Automation, Outbound, and Prospecting.


  OneShot''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Oneshot Plans Pricing
  plan_count: 3
  slug: oneshot-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Oneshot Rate Limits
  slug: oneshot-rate-limits
score:
  band: thin
  composite: 28.0
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oneshot/refs/heads/main/screenshots/oneshot-2026-08-07T190434.png
security:
- kind: authentication
  name: Oneshot Authentication
  slug: oneshot-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Oneshot Domain Security
  slug: oneshot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oneshot Vulnerability Disclosure
  slug: oneshot-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Oneshot Trust Center
  slug: oneshot-trust-center
  summary_line: trust center published
slug: oneshot
tags:
- Company
- Sales
- Sales Automation
- Outbound
- Prospecting
- Lead Generation
- Artificial Intelligence
- Go-To-Market
website: https://www.oneshot.ai
---
