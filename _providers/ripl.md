---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.ripl.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ripl.com/features-and-price
- group: company
  title: ''
  type: Blog
  url: https://www.ripl.com/blog
- group: operate
  title: ''
  type: Support
  url: http://help.ripl.com/support/home
- group: operate
  title: ''
  type: HelpCenter
  url: http://help.ripl.com/support/home
- group: start
  title: ''
  type: SignUp
  url: https://app.ripl.com/login?a=firstRun
- group: start
  title: ''
  type: Login
  url: https://app.ripl.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ripl.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ripl.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ripl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ripl-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ripl-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ripl.com/support/solutions/16000060995
- group: commercial
  title: ''
  type: Plans
  url: plans/ripl-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: Ripl ships a consumer/SMB social-posting app and no developer program at all — ripl.com/api and ripl.com/developers are 404, the Freshdesk help center has no API, webhook or integration section, and api.ripl.com is a private Rails/Heroku backend whose root 301s to the marketing site and which 404s every spec, docs and /.well-known path; the only machine-readable surface on the domain is the generic Wix Site MCP server Wix mounts at /_api/mcp for every site it hosts.
  evidence:
  - status: 404
    url: https://www.ripl.com/api
  - status: 404
    url: https://www.ripl.com/developers
  - status: 404
    url: https://api.ripl.com/openapi.json
  - status: 301
    url: https://api.ripl.com/
  - status: 400
    url: https://www.ripl.com/.well-known/agent-card.json
  - status: 200
    url: https://www.ripl.com/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Ripl is a social media marketing platform for small businesses, helping owners create, schedule, and publish engaging content across Instagram, Facebook, TikTok, YouTube, and other channels from customizable, industry-specific templates. It bundles branded post design, stock media, royalty-free music, scheduling, multi-account management, team collaboration, and an AI caption writer so restaurants, retailers, real estate agents, nonprofits, and other small businesses can maintain a consistent, professional online presence without a dedicated marketing team. Ripl is a Techstars portfolio company. Its public website (ripl.com) is built on Wix and exposes no first-party developer API; the app at app.ripl.com is the primary consumer product.
image: https://static.wixstatic.com/ficons/d8d800_48a04f46042747328480b7d817dc73f2~mv2.ico
layout: provider
mcp_servers:
- description: ''
  name: Ripl (Wix Site MCP)
  slug: ripl-wix-site-mcp
modified: '2026-08-13'
name: Ripl
nav: Providers
network: true
overview: 'Ripl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Media Marketing, Small Business, Content Scheduling, and Marketing.


  Ripl''s developer surface includes pricing, engineering blog, support, signup flow, getting-started guide, and 9 more developer resources.'
plans:
- name: Ripl Plans Pricing
  plan_count: 2
  slug: ripl-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Ripl Rate Limits
  slug: ripl-rate-limits
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.4
  provenance:
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ripl/refs/heads/main/screenshots/ripl-2026-09-02T153845.png
security:
- kind: domain-security
  name: Ripl Domain Security
  slug: ripl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ripl
tags:
- Company
- Social Media Marketing
- Small Business
- Content Scheduling
- Marketing
- Software-as-a-Service
- Social Media Management
website: https://www.ripl.com/
---
