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
  url: security/dermbiont-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dermbiont.com/
- group: company
  title: ''
  type: About
  url: https://www.dermbiont.com/overview
- group: other
  title: ''
  type: Product
  url: https://www.dermbiont.com/platform
- group: other
  title: ''
  type: Platform
  url: https://www.dermbiont.com/dermatology-platform
- group: other
  title: ''
  type: Pipeline
  url: https://www.dermbiont.com/pipeline
- group: other
  title: ''
  type: Leadership
  url: https://www.dermbiont.com/leadership
- group: operate
  title: ''
  type: Contact
  url: https://www.dermbiont.com/contact-us
- group: operate
  title: ''
  type: Support
  url: https://www.dermbiont.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dermbiont
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/dermbiont
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dermbiont-llms.txt
coverage:
  checked: '2026-08-12'
  detail: DermBiont is a clinical-stage dermatology drug developer whose only product is the SM-030 topical candidate; its sole web property is a 30-page Squarespace corporate site with no developer, docs or API section anywhere in its sitemap, every OpenAPI, GraphQL, llms.txt and .well-known path returns 404, api.dermbiont.com does not resolve, and no GitHub organization or first-party package exists on any public registry.
  evidence:
  - status: 404
    url: https://www.dermbiont.com/openapi.json
  - status: 404
    url: https://www.dermbiont.com/graphql
  - status: 404
    url: https://www.dermbiont.com/llms.txt
  - status: 404
    url: https://www.dermbiont.com/.well-known/agent-card.json
  - status: 404
    url: https://www.dermbiont.com/.well-known/agent.json
  - status: 404
    url: https://www.dermbiont.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/dermbiont
  - status: 200
    url: https://www.dermbiont.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'DermBiont, Inc. is a Boston, Massachusetts clinical-stage dermatology therapeutics company founded in 2017 that develops targeted topical treatments addressing the root cause of skin disease rather than its symptoms. Its lead program SM-030 is a first-in-class topical PKC-beta inhibitor in development for melasma and other hyperpigmentation disorders of the skin, targeting excess melanin production; earlier programs included SM-020 for seborrheic keratosis and the live-bacterial DBI-001 and DBI-002 candidates for atopic dermatitis, tinea pedis and onychomycosis. The company describes an in-house discovery platform for microbiome-based therapeutics built on terabytes of DNA sequencing data from human skin samples across healthy individuals and patients, paired with a proprietary computational biology platform that identifies functions gained and lost by the skin microbiome. That computational platform is internal research tooling, not a product: DermBiont sells drug candidates
  and partnering opportunities, publishes no developer program, no public API, no SDK and no machine-readable API contract of any kind, and its website is a Squarespace-hosted corporate site.'
image: https://static1.squarespace.com/static/5be33300f93fd46b40da5761/t/629e316bea93f12ec9cc272d/1654534507403/DM-main-logo.png?format=1500w
layout: provider
modified: '2026-08-12'
name: DermBiont
nav: Providers
network: true
overview: 'DermBiont is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Dermatology, and Therapeutics.


  DermBiont''s developer surface includes support and 11 more developer resources.'
random_paper: 70
score:
  band: minimal
  composite: 6.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Dermbiont Domain Security
  slug: dermbiont-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dermbiont
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Dermatology
- Therapeutics
- Skin Microbiome
- Microbiome
- Drug Discovery
- Clinical Stage
- Life Sciences
- Health
website: https://www.dermbiont.com/
---
