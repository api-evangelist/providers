---
access_model:
  confidence: high
  label: No public API · Partner/agent-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - review
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brown-brown-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bbrown.com/
- group: company
  title: ''
  type: Website
  url: https://us.bbrown.com/
- group: company
  title: ''
  type: Blog
  url: https://us.bbrown.com/blog/
- group: company
  title: ''
  type: BlogFeeds
  url: https://us.bbrown.com/blog/rss.xml
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.bbrown.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://investor.bbrown.com/rss/news-releases.xml
- group: company
  title: ''
  type: About
  url: https://us.bbrown.com/about/
- group: operate
  title: ''
  type: Support
  url: https://us.bbrown.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://us.bbrown.com/customer-logins
- group: company
  title: ''
  type: Careers
  url: https://us.bbrown.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.bbrown.com/general-terms-of-business
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.bbrown.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brown-brown-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brown-brown-insurance
created: '2026-07-25'
description: 'Brown & Brown, Inc. (NYSE: BRO) is a Daytona Beach, Florida headquartered insurance brokerage and risk-management intermediary founded in 1939, and one of the largest independent brokers in the United States. Following the 2025 acquisition of Accession Risk Management Group (Risk Strategies and One80 Intermediaries), it reports through two segments: Retail — property and casualty insurance, employee benefits, private client, captive solutions and financial/wealth services — and Specialty Distribution — programs, wholesale brokerage and MGA/binding-authority businesses including Arrowhead. As a distributor rather than a carrier, Brown & Brown places risk with insurers instead of underwriting it, and its US home market has no federal insurance regulator and no open-insurance mandate. Its API posture reflects that honestly: Brown & Brown publishes no public developer portal and no self-serve API. developer.bbrown.com, developers.bbrown.com, docs.bbrown.com and api.bbrown.com do
  not resolve, and every /developers, /api, /partners and /integrations path returns 404. Every discoverable application subdomain is a login wall — agent, client and vendor portals behind Microsoft Entra ID SSO or third-party sign-in. The only real programmatic surface is partner-gated: the Arrowhead Programs "Enterprise API" (EAPI), a quoting integration distributed through comparative raters and aggregators such as CoverHound, Tarmika, Semsee and DAIS, with no public documentation, base URL or specification. No ACORD, AL3, ACORD XML or NGDS reference is published on any Brown & Brown first-party property; carrier data exchange runs, as it does across US retail brokerage, through the agency management system layer — Brown & Brown is a publicly referenced Vertafore AMS360 agency — and IVANS agency download rather than through any API Brown & Brown itself exposes. In July 2026 the company announced an AI-first transformation with Anthropic, McKinsey and Accenture, deploying Claude across
  23,000 teammates and Claude Code across its software engineering organization; that is internal adoption and has so far produced no external API, developer portal or agent-facing surface. The only machine-readable documents Brown & Brown publishes are two RSS feeds — the blog and investor news releases.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Brown & Brown
nav: Providers
network: true
overview: 'Brown & Brown is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Broker, Property and Casualty, and Employee Benefits.


  Brown & Brown''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 106
score:
  band: emerging
  composite: 15.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brown-brown/refs/heads/main/screenshots/brown-brown-2026-07-25T203954.png
security:
- kind: domain-security
  name: Brown Brown Domain Security
  slug: brown-brown-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brown-brown
tags:
- Insurance
- United States
- Broker
- Property and Casualty
- Employee Benefits
- Wholesale Brokerage
- Managing General Agent
- Risk Management
- Agency Management
- Partner Gated
website: https://www.bbrown.com/
---
