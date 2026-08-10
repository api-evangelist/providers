---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lendis Agentic Access
  operation_count: 28
  slug: lendis-agentic-access
  summary_line: 28 operations
api_count: 10
apis:
- description: Customer case studies
  name: Lendis case-study API
  slug: lendis-case-study-api
- description: Route, type and taxonomy discovery plus site-wide search
  name: Lendis discovery API
  slug: lendis-discovery-api
- description: Kataloge (downloadable product catalogs)
  name: Lendis kataloge API
  slug: lendis-kataloge-api
- description: Medien (media library items)
  name: Lendis media API
  slug: lendis-media-api
- description: Seiten (site pages)
  name: Lendis pages API
  slug: lendis-pages-api
- description: Beitraege (blog posts from the Lendis Magazin)
  name: Lendis posts API
  slug: lendis-posts-api
- description: Ratgeber (buyer's guides)
  name: Lendis ratgeber API
  slug: lendis-ratgeber-api
- description: 'Taxonomy terms: categories, tags, wiki letters, Ratgeber categories'
  name: Lendis taxonomies API
  slug: lendis-taxonomies-api
- description: Customer testimonials
  name: Lendis testimonial API
  slug: lendis-testimonial-api
- description: Wiki glossary entries
  name: Lendis wiki API
  slug: lendis-wiki-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lendis-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.lendis.io
- group: company
  title: ''
  type: Blog
  url: https://www.lendis.io/magazin/
- group: operate
  title: ''
  type: Support
  url: https://www.lendis.io/kontakt/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lendis.io/faq/
- group: start
  title: ''
  type: Login
  url: https://app.lendis.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lendis.io/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lendis.io/datenschutz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lendis-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lendis/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@lendis_io
- group: company
  title: ''
  type: Careers
  url: https://www.lendis.io/karriere/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lendis-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lendis-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/lendis-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lendis-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendis-domain-security.yml
created: '2026-07-17'
description: Lendis GmbH is a Berlin-based B2B technology company, founded in 2018, that rents IT hardware to German small and mid-sized businesses under a Device-as-a-Service (DaaS) model. Lendis bundles hardware procurement, configuration and staging, delivery logistics, financing, IT support, lifecycle management and device offboarding into a single monthly rental rate, and manages the whole estate through LendisOS, a web platform covering a self-service shop, order tracking, asset inventory and contract management. The company targets organisations of roughly 50 to 500 employees that want to avoid tying up capital in laptops, smartphones, monitors and accessories. Lendis publishes no public developer program; its commercial platform runs on a private AWS API Gateway at api.lendis.io. Its marketing site does expose a public read-only WordPress REST content API, and Lendis publishes a machine-readable llms.txt for AI agents.
image: https://res.cloudinary.com/lendis-gmbh/images/f_svg,q_auto/fl_sanitize/v1774942862/www.lendis.io/lendis-logo-it/lendis-logo-it.svg
layout: provider
modified: '2026-07-19'
name: Lendis
nav: Providers
network: true
overview: 'Lendis publishes 10 APIs on the [APIs.io](https://apis.io/) network, including case-study API, discovery API, kataloge API, and 7 more. Tagged areas include Company, Ai Enterprise Software, Device As A Service, IT Hardware, and Leasing.


  Lendis'' developer surface includes engineering blog, support, YouTube channel, and 14 more developer resources.'
random_paper: 59
score:
  band: emerging
  composite: 23.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 15.6
    developer_ergonomics: 6.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 23.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lendis/refs/heads/main/screenshots/lendis-2026-07-25T224902.png
security:
- kind: authentication
  name: Lendis Authentication
  slug: lendis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Lendis Domain Security
  slug: lendis-domain-security
  summary_line: TLSv1.3
slug: lendis
tags:
- Company
- Ai Enterprise Software
- Device As A Service
- IT Hardware
- Leasing
- Asset Management
- Workplace Technology
- Procurement
- Germany
- SaaS
website: https://www.lendis.io
---
