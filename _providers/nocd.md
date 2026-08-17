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
  url: security/nocd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.treatmyocd.com/
- group: company
  title: ''
  type: Blog
  url: https://www.treatmyocd.com/learn/blog
- group: operate
  title: ''
  type: Support
  url: https://www.treatmyocd.com/about-us/contact-us
- group: start
  title: ''
  type: Login
  url: https://app.treatmyocd.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.treatmyocd.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.treatmyocd.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/treatmyocd
- group: company
  title: ''
  type: About
  url: https://www.treatmyocd.com/about-us/our-story
- group: company
  title: ''
  type: Careers
  url: https://www.treatmyocd.com/about-us/careers
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/nocd_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nocd-llms.txt
coverage:
  checked: '2026-08-04'
  detail: NOCD ships a consumer teletherapy app; its backend at api.treatmyocd.com answers a plain-text 404 for /openapi.json, /openapi.yaml and /docs and 302s every other path to the marketing site, and there is no developer.treatmyocd.com (NXDOMAIN) or developer section anywhere on treatmyocd.com.
  evidence:
  - status: 404
    url: https://api.treatmyocd.com/openapi.json
  - status: 302
    url: https://api.treatmyocd.com/.well-known/agent-card.json
  - status: 404
    url: https://www.treatmyocd.com/llms.txt
  - status: 404
    url: https://docs.treatmyocd.com/
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: NOCD is a virtual mental-health provider specializing in the treatment of obsessive-compulsive disorder. Through its web and mobile applications the company matches members with licensed therapists trained in Exposure and Response Prevention (ERP) therapy, delivers live video sessions, and provides between-session messaging, a peer community, and in-app therapeutic tools. NOCD is in-network with a large number of US health plans and serves children, adolescents, and adults. The product is delivered as an end-user clinical service — the company operates a private mobile/web application backend at api.treatmyocd.com but publishes no public developer program, API reference, or machine-readable specification.
image: https://www.treatmyocd.com/images/meta-image.png
layout: provider
modified: '2026-08-04'
name: NOCD
nav: Providers
network: true
overview: 'NOCD is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Mental Health, Telehealth, and Digital Health.


  NOCD''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 122
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
    operational_transparency: 5.3
  previous_composite: 15.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nocd/refs/heads/main/screenshots/nocd-2026-08-07T185408.png
security:
- kind: domain-security
  name: Nocd Domain Security
  slug: nocd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nocd
tags:
- Company
- Health Care
- Mental Health
- Telehealth
- Digital Health
- Therapy
- Behavioral Health
- Consumer Application
website: https://www.treatmyocd.com/
---
