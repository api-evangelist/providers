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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/razor-group-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/razor-group-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.razor-group.com/
- group: company
  title: ''
  type: Blog
  url: https://www.razor-group.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/razor-group
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.razor-group.com/privacy-policy
- group: other
  title: ''
  type: Imprint
  url: https://www.razor-group.com/imprint
- group: operate
  title: ''
  type: Contact
  url: https://www.razor-group.com/contact-us
- group: company
  title: ''
  type: About
  url: https://www.razor-group.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.razor-group.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://de.linkedin.com/company/razor-brands
- group: company
  title: ''
  type: Twitter
  url: https://mobile.twitter.com/razorgroup
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/razor-group_stock/
coverage:
  checked: '2026-08-05'
  detail: razor-group.com is a Webflow marketing site with no developer section of any kind, and the only two API endpoints Razor operates are private — api.razor-group.com resolves in DNS but refuses public TCP connections on 443 and 80, and the internal "Ava" operator portal fronts an AWS API Gateway that answers MissingAuthenticationToken to anonymous callers.
  evidence:
  - status: 404
    url: https://www.razor-group.com/openapi.json
  - status: 404
    url: https://www.razor-group.com/.well-known/agent-card.json
  - status: 404
    url: https://www.razor-group.com/llms.txt
  - status: 403
    url: https://portal.razor-group.com/api/health
  - status: 0
    url: https://api.razor-group.com/
  - status: 200
    url: https://api.github.com/orgs/razor-group/repos
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Razor Group (Whele LLC) is a Berlin- and Boston-headquartered consumer goods holding company that acquires, consolidates and scales profitable e-commerce brands selling on Amazon FBA, Walmart, Target, Chewy and other online marketplaces. Founded in 2020, the company has raised over $1 billion, employs 450+ people across five offices in Europe, North America and Asia, and operates more than 40,000 SKUs across brands including GymKeg, POWRX, Tranquil Spa and Porto Vino. In August 2025 Razor merged with Infinite Commerce to form the largest consolidator in the FBA aggregator space, operating a unified internal technology platform for demand forecasting, pricing and advertising. Razor Group is a buyer and operator of physical consumer products, not a software vendor: it publishes no public API, SDK, webhook surface or developer portal.'
image: https://cdn.prod.website-files.com/659bd12259ec13f287424e42/659bd12259ec13f28742502c_razor%20logo-blu-01.svg
layout: provider
modified: '2026-08-05'
name: Razor Group
nav: Providers
network: true
overview: 'Razor Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Consumer Goods, Marketplace, and Retail.


  Razor Group''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 30
score:
  band: minimal
  composite: 10.1
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Razor Group Domain Security
  slug: razor-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: razor-group
tags:
- Company
- E-Commerce
- Consumer Goods
- Marketplace
- Retail
- Amazon FBA
- Aggregator
- Brand Acquisition
- Germany
website: https://www.razor-group.com/
---
