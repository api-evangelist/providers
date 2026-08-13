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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calysta-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/calysta-llms.txt
- group: company
  title: ''
  type: Website
  url: https://calysta.com/
- group: company
  title: ''
  type: About
  url: https://calysta.com/who-we-are/
- group: company
  title: ''
  type: Blog
  url: https://calysta.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://calysta.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://calysta.com/contacts/
- group: company
  title: ''
  type: Careers
  url: https://calysta.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calysta.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calysta.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/calysta-energy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/feedkind
coverage:
  checked: '2026-08-09'
  detail: Calysta sells single-cell protein ingredients (FeedKind, Positive Protein) manufactured by an industrial gas-fermentation process; its complete 33-page WordPress sitemap has no developer, docs or API page, and the only machine-readable surface on the host is the stock WordPress REST API at /wp-json/ whose 273 routes are all core or third-party plugin namespaces with no first-party Calysta namespace.
  evidence:
  - status: 200
    url: https://calysta.com/wp-sitemap.xml
  - status: 404
    url: https://calysta.com/llms.txt
  - status: 404
    url: https://calysta.com/.well-known/security.txt
  - status: 200
    url: https://calysta.com/zzz-api-evangelist-control.json
  - status: 200
    url: https://calysta.com/.well-known/agent-card.json
  - status: 0
    url: https://api.calysta.com/
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: Calysta, Inc. is a cellular agriculture company founded in 2012 and headquartered in San Mateo, California, with operations in Memphis, Tennessee (NouriTech), Wilton/Teesside in the United Kingdom (Calysta UK Ltd.) and Singapore (Calysta Asia Pte Ltd.). It produces protein ingredients through a patented gas-fermentation platform in which a naturally-occurring microorganism converts carbon and energy into a non-GMO single-cell protein, using no arable land and no plant or animal inputs. Its product family includes FeedKind for aquaculture and livestock, FeedKind Pet, FeedKind Net Zero and Positive Protein for human food ingredients; FeedKind Aqua is sold globally through Calysseo, a 50/50 joint venture with Adisseo whose first production plant in China manufactures thousands of tonnes per year. Calysta sells physical protein ingredients to feed and food manufacturers — its fermentation platform is industrial process technology, not commercial software — and it publishes no public
  API, developer portal, SDK, or machine-readable specification.
image: https://calysta.com/wp-content/uploads/2022/03/calystalogo-1.png
layout: provider
modified: '2026-08-09'
name: Calysta
nav: Providers
network: true
overview: 'Calysta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cellular Agriculture, Fermentation, and Alternative Protein.


  Calysta''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 33
score:
  band: minimal
  composite: 11.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Calysta Domain Security
  slug: calysta-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calysta
tags:
- Company
- Biotechnology
- Cellular Agriculture
- Fermentation
- Alternative Protein
- Animal Feed
- Aquaculture
- Food Ingredients
- Sustainability
- Pet Nutrition
website: https://calysta.com/
---
