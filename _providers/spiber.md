---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The read-only WordPress REST API that backs spiber.inc. The service names itself "Spiber API" in its own discovery document and is referenced from spiber.inc/robots.txt as the origin of the site sitem
  name: Spiber Content API (WordPress REST)
  slug: spiber-content-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://spiber.inc/en
- group: company
  title: ''
  type: About
  url: https://spiber.inc/en/about
- group: company
  title: ''
  type: Blog
  url: https://spiber.inc/en/news
- group: company
  title: ''
  type: BlogRSS
  url: https://spiber.inc/en/news/feed
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spiber.inc/en/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://spiber.inc/en/cookie-policy
- group: company
  title: ''
  type: Careers
  url: https://spiber.inc/en/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Spiber
- group: other
  title: ''
  type: Sustainability
  url: https://spiber.inc/en/sustainability
- group: other
  title: ''
  type: Research
  url: https://spiber.inc/en/academic-papers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spiber-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spiber-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spiber-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spiber-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spiber-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/spiber-packages.yml
coverage:
  checked: '2026-08-29'
  detail: Spiber manufactures Brewed Protein fiber, resin and film by precision fermentation and sells it to apparel and automotive brands under supply agreements, so it publishes no developer program at all; the only machine-readable HTTP surface on any Spiber host is the unadvertised read-only WordPress REST backend that renders spiber.inc, which serves every response with X-Robots-Tag noindex and has no reference documentation.
  evidence:
  - status: 404
    url: https://spiber.inc/developers
  - status: 404
    url: https://spiber.inc/openapi.json
  - status: 404
    url: https://spiber.inc/.well-known/agent-card.json
  - status: 200
    url: https://spiber.xsrv.jp/api/wp-json/
  - status: 200
    url: https://api.github.com/orgs/Spiber
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: Spiber Inc. is a Japanese biotechnology and advanced-materials company founded in 2007 and headquartered in Tsuruoka, Yamagata Prefecture, Japan. Spiber develops Brewed Protein materials — structural proteins produced by precision fermentation of plant-derived sugars using engineered microbes, then spun into fibers, resins, and films as animal-free, petroleum-free alternatives to silk, wool, cashmere, leather, and synthetic polymers. The company operates fermentation plants in Japan, Thailand, and the United States and supplies apparel, outdoor, automotive, and consumer brands, alongside a research program in synthetic biology, polymer science, and life-cycle assessment. Spiber is a materials manufacturer rather than a software vendor and publishes no developer program, developer portal, SDKs, or product API; the only machine-readable HTTP surface it serves is the read-only WordPress REST content API behind its corporate website.
image: https://spiber.inc/en/opengraph-image.jpeg
layout: provider
mcp_servers:
- description: ''
  name: Spiber MCP Server
  slug: spiber-mcp-server
modified: '2026-08-29'
name: Spiber
nav: Providers
network: true
overview: 'Spiber publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Materials Science, Synthetic Biology, and Manufacturing.


  Spiber''s developer surface includes engineering blog and 15 more developer resources.'
plans:
- name: Spiber Plans Pricing
  plan_count: 0
  slug: spiber-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Spiber Rate Limits
  slug: spiber-rate-limits
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 15.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Spiber Authentication
  slug: spiber-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Spiber Domain Security
  slug: spiber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spiber
tags:
- Company
- Biotechnology
- Materials Science
- Synthetic Biology
- Manufacturing
- Sustainability
- Textiles
- Precision Fermentation
- Japan
- Content
website: https://spiber.inc/en
---
