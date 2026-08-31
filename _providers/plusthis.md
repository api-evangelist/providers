---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Plusthis Webhooks
  slug: plusthis-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://plusthis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.plusthis.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.plusthis.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.plusthis.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.plusthis.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plusthis.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.plusthis.com/register
- group: start
  title: ''
  type: Login
  url: https://www.plusthis.com/app-login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plusthis.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plusthis.com/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/plusthis-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plusthis-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plusthis-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/plusthis-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plusthis-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: PlusThis is a no-code CRM add-on sold entirely through its own web app — there is no developer portal, no API reference and no signup for API credentials anywhere on plusthis.com, kb.plusthis.com or help.plusthis.com, and the host named api.plusthis.com is the application login rather than an API (it 404s every spec path and answers /v1 with a bare "OK").
  evidence:
  - status: 404
    url: https://api.plusthis.com/openapi.json
  - status: 200
    url: https://api.plusthis.com/v1
  - status: 0
    url: https://developer.plusthis.com/
  - status: 0
    url: https://docs.plusthis.com/
  - status: 404
    url: https://www.plusthis.com/.well-known/api-catalog
  - status: 200
    url: https://help.plusthis.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: PlusThis is an Arizona-based marketing automation add-on company, founded in 2011, that sells a toolkit of roughly seventy no-code "tools" which bolt extra behaviour onto a CRM a business already runs — Keap (Infusionsoft), ActiveCampaign, Ontraport, HubSpot, Drip and HighLevel (GHL). The tools cover action links and smart links, countdown and evergreen-date scarcity, webinar and meeting connections (Zoom, GoToWebinar, WebinarJam, EverWebinar), scheduling connections (Calendly, Acuity), SMS sequences, field math and text formatting, contact validation and deduplication, Google Sheets and Drive export, Slack and DocuSign connections, and a Webhook Catcher that writes inbound third-party webhook payloads onto a CRM contact record. PlusThis is metered commercially on Active Tools and monthly Tool Runs rather than API calls, and it publishes no public developer API, no OpenAPI or other machine-readable contract, and no client SDKs — it is a consumer of other vendors' APIs rather
  than a producer of one.
image: https://d60ayi9p2ljnr.cloudfront.net/cms/assets/plusthis-icon-lg.png
layout: provider
modified: '2026-08-12'
name: PlusThis
nav: Providers
network: true
overview: 'PlusThis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing Automation, Marketing, CRM, and Sales.


  The PlusThis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PlusThis'' developer surface includes documentation, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Plusthis Plans Pricing
  plan_count: 7
  slug: plusthis-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Plusthis Rate Limits
  slug: plusthis-rate-limits
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 33.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Plusthis Domain Security
  slug: plusthis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plusthis
tags:
- Company
- Marketing Automation
- Marketing
- CRM
- Sales
- No Code
- Automation
- Integration
- Webhook
- Email Marketing
- SMS
- Small Business
website: https://plusthis.com/
---
