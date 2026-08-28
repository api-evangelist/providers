---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.4
  scored_at: '2026-08-26'
api_count: 10
apis:
- description: A Model Context Protocol server endpoint advertised in the nusano.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The endpoint is live b
  name: Nusano MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: News releases, event notices and Nu Blog posts from nusano.com, served as JSON by the WordPress content REST API. 109 posts were readable anonymously on 2026-08-26.
  name: Nusano Posts API
  slug: posts
- description: Marketing, company, technology and HALEU Knowledge Center pages from nusano.com, served as JSON. 47 pages were readable anonymously on 2026-08-26.
  name: Nusano Pages API
  slug: pages
- description: The nusano.com media library — facility photography, logos, media-kit assets and documents — served as JSON. 1,127 media items were readable anonymously on 2026-08-26.
  name: Nusano Media API
  slug: media
- description: The category taxonomy applied to Nusano news and blog content (14 categories on 2026-08-26).
  name: Nusano Categories API
  slug: categories
- description: The tag taxonomy applied to Nusano news and blog content (310 tags on 2026-08-26).
  name: Nusano Tags API
  slug: tags
- description: Publicly listed content authors on nusano.com (2 on 2026-08-26). Write routes and the application-password routes on this collection are authentication-gated.
  name: Nusano Users API
  slug: users
- description: The comment collection for nusano.com. The route is live and anonymously readable but returns an empty set — comments are closed across the site.
  name: Nusano Comments API
  slug: comments
- description: Site-wide search across nusano.com posts and pages, returning 156 searchable objects on 2026-08-26.
  name: Nusano Search API
  slug: search
- description: Type, taxonomy and status descriptors that describe the shape of the nusano.com content collections — the self-describing layer of the WordPress REST API.
  name: Nusano Discovery API
  slug: discovery
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://nusano.com/
- group: company
  title: ''
  type: About
  url: https://nusano.com/company/
- group: other
  title: ''
  type: Technology
  url: https://nusano.com/technology/
- group: company
  title: ''
  type: Blog
  url: https://nusano.com/news/nu-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://nusano.com/feed/
- group: company
  title: ''
  type: News
  url: https://nusano.com/news/
- group: operate
  title: ''
  type: Support
  url: https://nusano.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://nusano.com/careers/
- group: other
  title: ''
  type: MediaKit
  url: https://nusano.com/news/nusano-media-kit/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nusano
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nusano/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@nusano
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nusano.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nusano.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/nusano_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nusano-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nusano-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nusano-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nusano-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nusano-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nusano-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nusano-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nusano-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nusano-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nusano-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/nusano-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/nusano-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nusano-content-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: 'Nusano is a privately held physics company headquartered in West Valley City, Utah, that is rebuilding radioisotope production around a proprietary high-current ion source and linear accelerator platform. Founded by nuclear cardiologist Dr. Howard Lewin and nuclear physicist Dr. Glenn Rosenthal and led by CEO Chris Lowe, the company cut the ribbon in August 2025 on a custom-built 190,000-square-foot production facility capable of producing more than 40 different radioisotopes, and has raised over $115M in a Series C to commercialize them. Its platform can generate up to twelve isotopes simultaneously and serves three markets: medical radioisotopes as active pharmaceutical ingredients for radiotherapeutic and diagnostic oncology (with multi-isotope supply agreements signed with Ratio Therapeutics, Ariceum Therapeutics and Clarity Pharmaceuticals), high-assay low-enriched uranium (HALEU) for next-generation nuclear fuel, and long-lived radioisotope nuclear batteries for aerospace,
  maritime and terrestrial use, alongside mass-separation work on North American critical mineral refining. Nusano is a manufacturer of physical radioisotope products, not a software vendor: it operates no developer program, publishes no product API, SDK or developer portal, and the only machine-readable surfaces on nusano.com are a published llms.txt and the WordPress content REST API (wp/v2) that serves the newsroom, Nu Blog, pages and media library as JSON, plus a WordPress MCP Adapter endpoint that is live but authentication-gated.'
image: https://nusano.com/wp-content/uploads/2025/07/logo-graphic-full-color.jpeg
layout: provider
mcp_servers:
- description: 'The nusano.com WordPress REST route index advertises an "mcp" namespace with a single MCP server route at /wp-json/mcp/mcp-adapter-default-server accepting POST, GET and DELETE. This is the WordPress '
  name: Nusano MCP Server (WordPress MCP Adapter)
  slug: nusano-mcp-server-wordpress-mcp-adapter
modified: '2026-08-26'
name: Nusano
nav: Providers
network: true
overview: 'Nusano publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 6 more. Tagged areas include Company, Radioisotopes, Nuclear Medicine, Life Sciences, and Healthcare.


  Nusano''s developer surface includes engineering blog, product news, support, YouTube channel, authentication, code examples, and 23 more developer resources.'
plans:
- name: Nusano Plans Pricing
  plan_count: 0
  slug: nusano-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Nusano Rate Limits
  slug: nusano-rate-limits
score:
  band: emerging
  composite: 26.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 17.1
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Nusano Authentication
  slug: nusano-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nusano Domain Security
  slug: nusano-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nusano
tags:
- Company
- Radioisotopes
- Nuclear Medicine
- Life Sciences
- Healthcare
- Oncology
- Radiopharmaceuticals
- Physics
- Advanced Manufacturing
- Nuclear Energy
- HALEU
- Critical Minerals
- Content
website: https://nusano.com/
---
