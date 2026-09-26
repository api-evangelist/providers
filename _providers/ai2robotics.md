---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: API documentation is provided at https://docs.ai2robotics.com but no machine‑readable contract was found.
  name: Ai²robotics API
  slug: ai-robotics-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ai2robotics/refs/heads/main/changelog/ai2robotics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ai2robotics-changelog.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ai2robotics.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ai2robotics
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai2robotics/refs/heads/main/security/ai2robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai2robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai2robotics.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ai2robotics.com
- group: company
  title: ''
  type: Blog
  url: https://ai2robotics.com/news
- group: operate
  title: ''
  type: Support
  url: https://ai2robotics.com/contact
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ai2robotics.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ai2robotics.com/start/product-introduction/
- group: start
  title: ''
  type: SignUp
  url: https://ai2robotics.com/joinus
coverage:
  checked: 2026-09-22
  detail: Docs site returns HTML shells for spec URLs, no machine‑readable OpenAPI found.
  evidence:
  - status: 200
    url: https://docs.ai2robotics.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: Ai²robotics (智平方科技) is a global leader in the research, development, manufacturing, and services of general‑purpose intelligent robots. Founded in April 2023 and headquartered in Shenzhen, the company accelerates the adoption of AGI robots, aiming to make them as ubiquitous as smartphones. It offers the AlphaBrain Platform and other AI‑driven robotics solutions for industrial and commercial applications, with a focus on safety, scalability, and real‑world AI integration.
image: https://ai2robotics.com/wp-content/uploads/2023/11/cropped-fav.png
layout: provider
modified: '2026-09-22'
name: Ai²robotics
nav: Providers
network: true
overview: 'Ai²robotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Artificial Intelligence, AGI, Manufacturing, and Shenzhen.


  Ai²robotics'' developer surface includes changelog, documentation, engineering blog, support, API reference, getting-started guide, signup flow, and 4 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 58.9
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 18.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai2Robotics Domain Security
  slug: ai2robotics-domain-security
  summary_line: TLSv1.3
slug: ai2robotics
tags:
- Robotics
- Artificial Intelligence
- AGI
- Manufacturing
- Shenzhen
website: https://ai2robotics.com
---
