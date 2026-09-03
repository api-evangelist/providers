---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hungry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryhungry.com/
- group: company
  title: ''
  type: About
  url: https://tryhungry.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://tryhungry.com/contact
- group: start
  title: ''
  type: Login
  url: https://tryhungry.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryhungry.com/terms-and-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryhungry.com/terms-and-privacy
- group: company
  title: ''
  type: Press
  url: https://tryhungry.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tryhungry
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hungry-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://tryhungry.github.io/techreleasenotes/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tryhungry/
- group: company
  title: ''
  type: Careers
  url: https://tryhungry.com/careers
- group: commercial
  title: ''
  type: Plans
  url: plans/hungry-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hungry-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/hungry-well-known.yml
coverage:
  checked: '2026-08-22'
  detail: HUNGRY runs a real engineering org and a private API at api.tryhungry.com behind Cloudflare, but ships software only as an end-user product — the platform is sold as catering, not as a contract; api.tryhungry.com returns a plain-text "404 page not found" on /openapi.json, /swagger.json, /api-docs, /graphql and every /.well-known/ path, and the public github.com/tryhungry org holds only forks of third-party libraries.
  evidence:
  - status: 404
    url: https://api.tryhungry.com/openapi.json
  - status: 404
    url: https://api.tryhungry.com/graphql
  - status: 404
    url: https://api.tryhungry.com/.well-known/agent-card.json
  - status: 404
    url: https://tryhungry.com/llms.txt
  - status: 200
    url: https://tryhungry.com/sitemap.xml
  - status: 200
    url: https://tryhungry.github.io/techreleasenotes/
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'HUNGRY (Hungry Marketplace, Inc.) is an Arlington, Virginia workplace food platform that connects corporate clients to a curated network of independent chefs and local restaurants. Founded in 2016 by Jeff Grass, Eman Pahlavani and Shy Pahlevani, it operates four product lines — office catering, Group Order individual meal pre-ordering, live events and chef pop-ups, and snacks and pantry — plus HUNGRY Last Mile, its own delivery and logistics arm. The platform runs its own admin, chef/food-partner dashboard, client admin dashboard, ops captain app and consumer ordering marketplace across 24 US cities and, following the February 2026 merger with Toronto-based hungerhub, more than ten Canadian markets. Earlier acquisitions include NatureBox and Garten. HUNGRY publishes no public developer program: the backing API at api.tryhungry.com is a private first-party service for its own web and mobile clients, and no OpenAPI, GraphQL SDL, AsyncAPI, SDK or partner API reference is published
  anywhere on its public surface. The company does publish a dated, public engineering release-notes site, which is the only machine-adjacent technical artifact it makes available.'
image: https://tryhungry.com/_astro/hungry-logo.BlRuMDC-.svg
layout: provider
modified: '2026-08-22'
name: HUNGRY
nav: Providers
network: true
overview: 'HUNGRY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Catering, Marketplace, and Logistics.


  HUNGRY''s developer surface includes support, changelog, release notes, and 13 more developer resources.'
plans:
- name: Hungry Plans Pricing
  plan_count: 0
  slug: hungry-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 13.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hungry/refs/heads/main/screenshots/hungry-2026-09-02T145759.png
security:
- kind: domain-security
  name: Hungry Domain Security
  slug: hungry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hungry
tags:
- Company
- Food and Beverage
- Catering
- Marketplace
- Logistics
- Food Delivery
- Workplace
- Hospitality
- Corporate Services
- Last Mile Delivery
website: https://tryhungry.com/
---
