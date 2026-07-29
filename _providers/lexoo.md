---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
api_count: 2
apis:
- description: The Lexoo website is built on WordPress and exposes the standard WordPress REST API at /wp-json/, serving JSON representations of the site's pages, media, taxonomies and settings. The live discovery d
  name: Lexoo WordPress REST API
  slug: wordpress-rest-api
- description: Lexoo's WordPress site publishes a standard RSS 2.0 feed at /feed/ for its main content stream. The feed is well-formed and reachable but currently carries no items, because the site publishes pages o
  name: Lexoo RSS Feed
  slug: rss-feed
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lexoo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lexoo-llms.txt
- group: company
  title: ''
  type: Website
  url: https://lexoo.com/
- group: company
  title: ''
  type: About
  url: https://lexoo.com/team/
- group: operate
  title: ''
  type: Contact
  url: mailto:team@lexoo.com
- group: other
  title: ''
  type: Product
  url: https://lexoo.com/contract-review/
- group: other
  title: ''
  type: Product
  url: https://lexoo.com/multi-country-projects/
- group: other
  title: ''
  type: Product
  url: https://lexoo.com/scale-ups-start-ups/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lexoolimited
created: '2026-07-17'
description: 'Lexoo is a commercial legal services provider that operates as an outsourced in-house legal team for businesses, concentrating on commercial contract review and negotiation. The company handles routine contract work at fixed rates per agreement with a stated maximum two-day turnaround, so internal legal and sales teams are freed for more strategic work. Alongside contract review, Lexoo runs multi-country projects that engage local counsel across more than 70 countries for work such as terms and conditions localisation and regulatory research, and it builds playbooks and training materials that let client teams handle standard agreements independently. The practice is led by Nathalie Lambert and serves scale-ups and start-ups, with published client references including Trustpilot, Nielsen, ComplyAdvantage, Xeneta, Chattermill and Jokr. Lexoo is not an API-first company: it publishes no developer portal, documentation or SDKs, and its only machine-readable surfaces are the standard
  WordPress REST API and RSS feed exposed by its marketing site.'
image: https://lexoo.com/wp-content/uploads/2024/10/cropped-lexoo-logo-IN-Copy-192x192.png
layout: provider
modified: '2026-07-19'
name: Lexoo
nav: Providers
network: true
overview: Lexoo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Legal Services, Contract Review, Compliance, and Professional Services.
random_paper: 77
score:
  band: minimal
  composite: 7.6
  delta: -1.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lexoo/refs/heads/main/screenshots/lexoo-2026-07-25T225002.png
security:
- kind: domain-security
  name: Lexoo Domain Security
  slug: lexoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lexoo
tags:
- Legal
- Legal Services
- Contract Review
- Compliance
- Professional Services
- Legal Technology
- Consulting
website: https://lexoo.com/
---
