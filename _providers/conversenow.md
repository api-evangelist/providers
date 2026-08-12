---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/conversenow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conversenow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conversenow.ai/
- group: company
  title: ''
  type: Blog
  url: https://conversenow.ai/insights.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conversenow
- group: start
  title: ''
  type: SignUp
  url: https://conversenow.ai/book-demo.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conversenow.ai/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conversenow.ai/privacy-policy.html
- group: auth
  title: ''
  type: Security
  url: https://conversenow.ai/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/conversenow-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/conversenow-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conversenow-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conversenow.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conversenow-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conversenow-llms.txt
coverage:
  checked: '2026-08-09'
  detail: ConverseNow markets an "Order Injection API" as a product on its products page and its own status page monitors a component literally named "API Server", but the only route to it is the "Book a Consultation" form — there is no developer portal, no API reference, and the docs.conversenow.ai and app.conversenow.ai hostnames are dangling DNS records with no listener on port 80 or 443.
  evidence:
  - status: 200
    url: https://conversenow.ai/products.html
  - status: 200
    url: https://conversenow.ai/book-demo.html
  - status: 0
    url: https://docs.conversenow.ai/
  - status: 0
    url: https://developer.conversenow.ai/
  - status: 404
    url: https://conversenow.ai/openapi.json
  - status: 200
    url: https://status.conversenow.ai/
  reason: sales-gate
  state: gated
created: '2026-08-09'
description: ConverseNow is an Austin, Texas voice AI company, founded in 2018, that builds conversational AI virtual assistants which automate restaurant order taking across high-volume voice channels — inbound phone, drive-thru, SMS, and kiosk. The platform uses large language models to understand natural-language orders, suggest upsells, and confirm items in real time, and it markets an "Order Injection API" that pushes completed orders into restaurant point-of-sale and order-management systems. ConverseNow lists integrations with Brink POS, Fiserv, Focus, ItsaCheckmate, NCR Aloha, Olo, PAR, Qu, Xpient, Adora POS, and Deliverect, and reports processing more than two million conversations per month across national QSR brands. It publishes no public developer portal, API reference, or machine-readable specification; API access is reached through a sales consultation.
image: https://storage.googleapis.com/conversenow/static/website/conversenow-logo.svg
layout: provider
modified: '2026-08-09'
name: ConverseNow
nav: Providers
network: true
overview: 'ConverseNow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Voice AI, Conversational AI, Restaurants, and Point of Sale.


  ConverseNow''s developer surface includes engineering blog, signup flow, changelog, and 12 more developer resources.'
random_paper: 49
score:
  band: emerging
  composite: 19.2
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 20.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Conversenow Domain Security
  slug: conversenow-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Conversenow Vulnerability Disclosure
  slug: conversenow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: conversenow
tags:
- Company
- Voice AI
- Conversational AI
- Restaurants
- Point of Sale
- Ordering
- Drive-Thru
- Speech Recognition
- Artificial Intelligence
- Food Service
website: https://conversenow.ai/
---
