---
access_model:
  confidence: high
  label: Free tier, self-service sign-up
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.yesware.com/plans-and-pricing
  - https://www.yesware.com/sign-up
  trial: true
  try_now: true
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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.yesware.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yesware.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yesware.com/docs/getting-started-with-yesware
- group: operate
  title: ''
  type: Support
  url: mailto:support@yesware.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.yesware.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://www.yesware.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yesware.com/plans-and-pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/yesware-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yesware-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yesware-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yesware.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.yesware.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.yesware.com/user/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yesware.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yesware.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Yesware
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yesware-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yesware-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/yesware-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yesware-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.yesware.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.yesware.com/security/
coverage:
  checked: '2026-08-13'
  detail: Yesware ships only an end-user product — every one of the 81 pages in docs.yesware.com's sitemap is Gmail/Outlook product help, no API host resolves (api.yesware.com does not exist in DNS), and Yesware's own retired help-center article "Does Yesware have a public-facing API instead of a Google extension?" answered no.
  evidence:
  - status: 200
    url: https://docs.yesware.com/sitemap.xml
  - status: 404
    url: https://www.yesware.com/.well-known/agent-card.json
  - status: 404
    url: https://www.yesware.com/.well-known/api-catalog
  - status: 301
    url: https://support.yesware.com/hc/en-us/articles/15420545065623-How-many-API-calls-does-Yesware-use
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Yesware is a sales engagement and email productivity platform that lives inside Gmail and Outlook, helping sales teams track email opens, link clicks, and attachment views in real time, run multi-touch outreach campaigns and sequences, use shared email templates, schedule meetings, and prospect from a database of 100M+ B2B contacts. It provides bi-directional Salesforce sync to log activities automatically and reporting dashboards on template and team performance. Yesware has been part of Vendasta since October 2022. It does not expose a public developer REST API, GraphQL endpoint, webhook catalog, MCP server or agent card — its own help center answered "does Yesware have a public-facing API" with no, and its entire documentation set at docs.yesware.com is end-user product help. The integration surface is delivered through Salesforce sync, native Gmail/Outlook inbox extensions, LinkedIn, Zoom, Google Meet and Microsoft Teams connectors, and third-party iPaaS platforms. The most
  machine-readable surface Yesware operates is its Atlassian Statuspage. It was surfaced as a portfolio company of Battery Ventures and GV and profiled in the API Evangelist network.
image: https://cdn.prod.website-files.com/6036bf3265493cd8d57a7527/62aa0d96e8c9ac7fb2d2528b_882b3fdf09a3292fea8075d218f74d92_yesware-featured-image.png
layout: provider
modified: '2026-08-13'
name: Yesware
nav: Providers
network: true
overview: 'Yesware is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Engagement, Email Tracking, Sales Productivity, and CRM.


  Yesware''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Yesware Plans Pricing
  plan_count: 4
  slug: yesware-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Yesware Rate Limits
  slug: yesware-rate-limits
score:
  band: thin
  composite: 28.4
  delta: -5.1
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 33.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: domain-security
  name: Yesware Domain Security
  slug: yesware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yesware Vulnerability Disclosure
  slug: yesware-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Yesware Trust Center
  slug: yesware-trust-center
  summary_line: SOC 2 Type II, Skyhigh CloudTrust Enterprise-Ready, GDPR, Salesforce Security Review
slug: yesware
tags:
- Company
- Sales Engagement
- Email Tracking
- Sales Productivity
- CRM
- Salesforce
- Outreach
- Email Marketing
- Sales Enablement
- Gmail
- Outlook
website: https://www.yesware.com
---
