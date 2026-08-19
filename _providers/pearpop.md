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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pearpop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pearpop.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pearpop.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pearpop.ai/privacy
- group: other
  title: ''
  type: SignIn
  url: https://pearpop.ai/signin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pearpop
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/pearpop/
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/pearpop_stock/
coverage:
  checked: '2026-08-04'
  detail: Pearpop ships no developer surface at all — pearpop.com is a 15-page Framer marketing site whose sitemap contains no docs or developer page, api.pearpop.com is a dangling CNAME to a deleted AWS API Gateway custom domain, and the only live API namespace (pearpop.ai/api/*) 302s every anonymous call to the Pearpop.AI sign-in page.
  evidence:
  - status: 404
    url: https://www.pearpop.com/developers
  - status: 404
    url: https://www.pearpop.com/openapi.json
  - status: 200
    url: https://www.pearpop.com/sitemap.xml
  - status: 302
    url: https://pearpop.ai/api/health
  - status: 404
    url: https://pearpop.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: Pearpop, Inc. is a Los Angeles-based creator marketing company founded in October 2020 by Cole Mason and Guy Oseary. It began as a two-sided social collaboration marketplace where brands could book social-media creators on demand under a performance-based, pay-per-placement model, and has since grown into a full-service creator marketing partner running campaigns for brands including Netflix, Microsoft, Chipotle, Klarna and Activision. Its current product line is marketed at pearpop.com (brand campaigns, creator representation and events) plus Pearpop.AI at pearpop.ai — described in Pearpop's own terms of service as an AI-powered email platform for content creators and influencers that handles brand-deal inboxes, contract review, rate recommendations and payments. Pearpop publishes no public developer program, API documentation, SDKs or machine-readable API specification; the only live API namespace, pearpop.ai/api/*, redirects unauthenticated callers to the application sign-in
  page.
image: https://framerusercontent.com/assets/ao2KsbBYtXXhJYI7gchP67vlJaI.png
layout: provider
modified: '2026-08-04'
name: PearPop
nav: Providers
network: true
overview: PearPop is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, Influencer Marketing, Social Media, and Marketing.
random_paper: 14
score:
  band: minimal
  composite: 9.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Pearpop Domain Security
  slug: pearpop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pearpop
tags:
- Company
- Creator Economy
- Influencer Marketing
- Social Media
- Marketing
- Marketplace
- Talent Management
- Artificial Intelligence
website: https://www.pearpop.com/
---
