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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kintra-fibers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kintrafibers.com/
- group: company
  title: ''
  type: About
  url: https://www.kintrafibers.com/about-us
- group: other
  title: ''
  type: Sustainability
  url: https://www.kintrafibers.com/sustainability
- group: operate
  title: ''
  type: Contact
  url: https://www.kintrafibers.com/contact
- group: operate
  title: ''
  type: Support
  url: https://www.kintrafibers.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kintrafibers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kintra-fibers-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Kintra Fibers manufactures a bio-based PBS polyester substitute sold as resin, staple fiber, 75D/72F yarn and fabric to extruders, spinners, mills and apparel brands; its only web property is a Webflow marketing site built on the off-the-shelf GENTLE e-commerce template whose /blog, /careers and /privacy-policy routes still return the vendor's lorem-ipsum placeholder copy, and every OpenAPI, GraphQL, MCP, llms.txt and agent-card path on it returns 404 while api.kintrafibers.com does not resolve at all.
  evidence:
  - status: 200
    url: https://www.kintrafibers.com/
  - status: 404
    url: https://www.kintrafibers.com/openapi.json
  - status: 404
    url: https://www.kintrafibers.com/graphql
  - status: 404
    url: https://www.kintrafibers.com/llms.txt
  - status: 404
    url: https://www.kintrafibers.com/.well-known/agent-card.json
  - status: 404
    url: https://www.kintrafibers.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/kintrafibers
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Kintra Fibers is a Brooklyn, New York materials-science company that has developed a proprietary bio-based and biodegradable synthetic yarn as an alternative to conventional petroleum polyester. Its polymer is a novel form of polybutylene succinate (PBS) made from renewable corn- and wheat-derived sugar feedstocks, melt-spun on the same commercial equipment already used for polyester so that mills, spinners and extruders can adopt it without re-tooling. The company sells four physical products into the apparel supply chain — resin for extruders, staple fiber for spinners, 75D/72F multifilament yarn in FDY, ATY and DTY forms for mills, and finished performance fabric for brands. Co-founded by Billy McCall and Alissa Baier-Lentz, Kintra runs an in-house resin and fiber science lab in Brooklyn, launched a Fashion for Good consortium with Inditex, Bestseller and Reformation, and closed a funding round led by H&M Group. Kintra is a manufacturer of physical materials, not a software
  company: it operates no developer program, publishes no public API, SDK, webhook or machine-readable API contract, and its only web property is a Webflow marketing and contact site.'
image: https://cdn.prod.website-files.com/686faf8e945540977b7e15ab/68c03021964251e1fb786fdd_Screenshot%202025-09-09%20at%203.48.06%E2%80%AFPM.png
layout: provider
modified: '2026-08-23'
name: Kintra Fibers
nav: Providers
network: true
overview: 'Kintra Fibers is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Materials Science, Textiles, Apparel, and Fashion.


  Kintra Fibers'' developer surface includes support and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kintra-fibers/refs/heads/main/screenshots/kintra-fibers-2026-09-02T150043.png
security:
- kind: domain-security
  name: Kintra Fibers Domain Security
  slug: kintra-fibers-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kintra-fibers
tags:
- Company
- Materials Science
- Textiles
- Apparel
- Fashion
- Biomaterials
- Sustainability
- Manufacturing
- Supply Chain
- Climate Tech
website: https://www.kintrafibers.com/
---
