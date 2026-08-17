---
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
- group: company
  title: ''
  type: Website
  url: https://groupboss.io/
- group: operate
  title: ''
  type: Support
  url: https://groupboss.io/help/
- group: company
  title: ''
  type: Blog
  url: https://groupboss.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://groupboss.io/blog/rss/
- group: commercial
  title: ''
  type: Pricing
  url: https://groupboss.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.groupboss.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://groupboss.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://groupboss.io/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://groupboss.io/faq
- group: other
  title: ''
  type: Download
  url: https://chromewebstore.google.com/detail/groupboss/gakcpcoikgklfbajjkdaomcfkpeiobfl
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/groupboss-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/groupboss-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/groupboss-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groupboss-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groupboss-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://groupboss.io/llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groupboss-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: Groupboss is a Chrome-extension SaaS that consumes ~30 other providers' APIs using the customer's own API keys and publishes none of its own — groupboss.io /api and /developers both return an untitled catch-all shell byte-identical to a nonsense path, and no spec answered on groupboss.io, app.groupboss.io, api.groupboss.com or support.groupboss.io.
  evidence:
  - status: 200
    url: https://groupboss.io/api
  - status: 200
    url: https://groupboss.io/developers
  - status: 200
    url: https://api.groupboss.com/openapi.json
  - status: 404
    url: https://support.groupboss.io/openapi.json
  - status: 404
    url: https://groupboss.io/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: Groupboss is a Facebook Group lead-generation and member-onboarding tool sold as a Chrome extension paired with a hosted web app. When someone requests to join a Facebook Group, Groupboss captures the answers to the group's membership questions — including the email address — approves or declines the member automatically against rules the admin sets, and pushes the captured lead into Google Sheets and into the admin's email marketing platform or CRM. It ships connectors for roughly thirty destinations including Mailchimp, ActiveCampaign, Klaviyo, Brevo, GetResponse, Kit, Drip, MailerLite, Omnisend, HubSpot, Zoho CRM, GoHighLevel, Airtable, FluentCRM, ClickFunnels and Systeme.io. Those connectors are one-directional and consume the customer's own API key for each destination platform; Groupboss itself publishes no public API, no webhooks and no developer program, so it is a pure API consumer rather than an API producer.
image: https://d3lonve0ytqgeg.cloudfront.net/media/logo.png
layout: provider
modified: '2026-08-12'
name: Groupboss
nav: Providers
network: true
overview: 'Groupboss is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lead Generation, Marketing, Marketing Automation, and Email Marketing.


  Groupboss'' developer surface includes support, engineering blog, pricing, FAQ, changelog, and 12 more developer resources.'
plans:
- name: Groupboss Plans Pricing
  plan_count: 3
  slug: groupboss-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 0
  name: Groupboss Rate Limits
  slug: groupboss-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 24.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Groupboss Domain Security
  slug: groupboss-domain-security
  summary_line: TLSv1.3 · DMARC
slug: groupboss
tags:
- Company
- Lead Generation
- Marketing
- Marketing Automation
- Email Marketing
- CRM
- Social Media
- Community
- Browser Extension
- SaaS
website: https://groupboss.io/
---
