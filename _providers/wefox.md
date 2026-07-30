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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wefox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wefox.com
- group: company
  title: ''
  type: About
  url: https://www.wefox.com/about
- group: other
  title: ''
  type: Leadership
  url: https://www.wefox.com/about/leadership
- group: company
  title: ''
  type: Newsroom
  url: https://www.wefox.com/newsroom
- group: other
  title: ''
  type: Austria
  url: https://www.wefox.com/wefox-austria
- group: other
  title: ''
  type: Switzerland
  url: https://www.wefox.com/wefox-switzerland
- group: other
  title: ''
  type: Germany
  url: https://www.wefox.com/de-de
- group: other
  title: ''
  type: Imprint
  url: https://www.wefox.com/imprint
- group: commercial
  title: ''
  type: Privacy
  url: https://www.wefox.com/privacy
- group: commercial
  title: ''
  type: Terms
  url: https://www.wefox.com/taf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wefox
created: '2026-05-25'
description: wefox is a Berlin-headquartered digital insurance distribution platform that connects insurance carriers, brokers, and end customers through a single technology stack. Founded in 2014 and originally known as FinanceFox, the company operates across Germany, Austria, Switzerland, Italy, the Netherlands, Spain, and France, selling personal-lines products such as motor, home, liability, life, and commercial insurance via its in-house carrier (wefox Insurance) and a network of independent brokers. wefox positions itself as an "indirect" insurtech — meaning it distributes through human advisors augmented by software rather than selling direct-to-consumer — and has historically been one of Europe's most highly funded insurtech companies, with backing from Mubadala, Target Global, Salesforce Ventures, OMERS Ventures, Eurazeo, Mountain Partners, and others. The platform itself is a multi-tenant SaaS used by brokers and agents to manage customer relationships, quote and bind policies
  across multiple carriers, handle claims, and trigger commissions. wefox does not publish a public developer portal, OpenAPI specifications, SDKs, or a github.com/wefox organization; integration with the wefox platform is carrier-, broker-, and partner-mediated rather than self-service, and there is no Tier-1 developer surface to document. This repo profiles wefox as an insurance distribution business and tracks any future move toward a public API program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wefox.png
layout: provider
modified: '2026-05-25'
name: wefox
nav: Providers
network: true
overview: 'wefox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Insurtech, Digital Insurance, Insurance Distribution, and Broker Platform.


  wefox''s developer surface includes privacy policy, terms of service, and 10 more developer resources.'
random_paper: 61
score:
  band: minimal
  composite: 8.3
  delta: -2.5
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wefox/refs/heads/main/screenshots/wefox-2026-06-20T201342.png
security:
- kind: domain-security
  name: Wefox Domain Security
  slug: wefox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wefox
tags:
- Insurance
- Insurtech
- Digital Insurance
- Insurance Distribution
- Broker Platform
- Motor Insurance
- Home Insurance
- Liability Insurance
- Life Insurance
- Commercial Insurance
- Europe
- Germany
- Berlin
- Financial Services
website: https://www.wefox.com
---
