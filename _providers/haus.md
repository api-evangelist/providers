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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/haus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/haus-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: security/haus-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.haus.io/
- group: company
  title: ''
  type: About
  url: https://www.haus.io/about
- group: company
  title: ''
  type: Blog
  url: https://www.haus.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.haus.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.haus.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.haus.io/
- group: start
  title: ''
  type: Login
  url: https://app.haus.io/login
- group: start
  title: ''
  type: SignUp
  url: https://www.haus.io/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://haus.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://haus.io/legal/privacy-policy
- group: auth
  title: ''
  type: SecurityContact
  url: mailto:security@haus.io
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/haus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/haus-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/haus-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/haus-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/haus-lifecycle.yml
coverage:
  checked: '2026-08-12'
  detail: Haus ships only a login-gated SaaS app at app.haus.io — there is no API host in DNS at all (api, developer, docs, graph, gateway, public-api and six more candidate subdomains are all NXDOMAIN), the 40-URL sitemap contains no developer or reference page, the four published pricing tiers offer no API access, and Haus's own llms.txt indexes 45 marketing, blog and case-study pages without naming a single developer resource.
  evidence:
  - status: 200
    url: https://www.haus.io/llms.txt
  - status: 200
    url: https://www.haus.io/pricing
  - status: 404
    url: https://www.haus.io/openapi.json
  - status: 404
    url: https://app.haus.io/openapi.json
  - status: 404
    url: https://www.haus.io/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Haus is an AI-powered causal marketing measurement platform that helps enterprise brands quantify the true incrementality of their advertising spend. The platform runs on-demand geo-based incrementality experiments (treatment vs. holdout groups), causal media mix modeling (MMM) grounded in experimental data, and daily causal attribution reporting, so marketers can see which channels actually drive revenue. Haus reports running thousands of experiments annually across tens of billions of dollars in optimized ad spend for customers such as FanDuel, Intuit, Wayfair, and Coursera. Founded by former Google economists, Haus is backed by Insight Partners.
image: https://cdn.prod.website-files.com/636c27cea6bf2a38e9eea317/698cc912d640157690a26208_og%20image%20-%20home%20-%201600.jpg
layout: provider
modified: '2026-08-12'
name: Haus
nav: Providers
network: true
overview: 'Haus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Analytics, Incrementality, and Measurement.


  Haus'' developer surface includes engineering blog, pricing, support, signup flow, and 15 more developer resources.'
plans:
- name: Haus Plans Pricing
  plan_count: 4
  slug: haus-plans-pricing
random_paper: 135
score:
  band: thin
  composite: 30.1
  delta: 0.1
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/haus/refs/heads/main/screenshots/haus-2026-07-25T220755.png
security:
- kind: domain-security
  name: Haus Domain Security
  slug: haus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Haus Vulnerability Disclosure
  slug: haus-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Haus Trust Center
  slug: haus-trust-center
  summary_line: SOC 2, ISO 27001
slug: haus
tags:
- Company
- Marketing
- Analytics
- Incrementality
- Measurement
- Attribution
- Media Mix Modeling
- Causal Inference
- Advertising
- MarTech
website: https://www.haus.io/
---
