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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cortica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cortica.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cortica.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cortica.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cortica/
coverage:
  checked: '2026-08-11'
  detail: Cortica Ltd is an Israeli Autonomous AI venture builder whose technology reaches the market only through spin-outs and joint ventures (Autobrains, Corsight, Corsound, SeeTrue, CordiGuide, Qualisense), and cortica.com is a three-page WordPress marketing site — its full sitemap is the homepage, a privacy policy, a terms page, 24 reposted press mentions and 6 portfolio pages, with no developer portal, no docs host and no api./docs./developer. subdomain resolving in DNS; the only 200-returning JSON API on the domain is the stock WordPress CMS backend at /wp-json/ (namespaces wp/v2, oembed/1.0, contact-form-7/v1, objectcache/v1, wp-site-health/v1, wp-block-editor/v1, wp-abilities/v1 — all core or plugin, none a product API), and every OpenAPI, GraphQL, llms.txt and /.well-known/ probe returned 404.
  evidence:
  - status: 404
    url: https://cortica.com/openapi.json
  - status: 404
    url: https://cortica.com/swagger.json
  - status: 404
    url: https://cortica.com/graphql
  - status: 404
    url: https://cortica.com/llms.txt
  - status: 404
    url: https://cortica.com/.well-known/agent-card.json
  - status: 404
    url: https://cortica.com/.well-known/agent.json
  - status: 404
    url: https://cortica.com/.well-known/security.txt
  - status: 200
    url: https://cortica.com/wp-json/
  - status: 200
    url: https://api.github.com/users/cortica-inc
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: 'Cortica is a Tel Aviv, Israel based Autonomous AI company founded in 2007 that builds and spins out category-leading AI companies. Its self-learning, unsupervised "Autonomous AI" is modelled on the mammalian cortex — signatures instead of labels, adaptive architecture, and self-learning neural networks that index high volumes of visual, audio, radar and time-series signal on low-compute platforms. Cortica states it has invested more than $250M over 15 years and holds 300+ patents, and it operates as a venture builder rather than a product vendor: its technology reaches the market through partner joint ventures and spin-outs including Autobrains (autonomous driving), Corsight AI (facial recognition), Corsound AI (voice), SeeTrue (airport security screening), CordiGuide (medical imaging) and Lean AI / Qualisense (industrial quality inspection, with Johnson Electric). Cortica itself publishes no developer program, API, SDK or machine-readable specification on its own domain.'
image: https://cortica.com/wp-content/uploads/2023/05/Favicon.png
layout: provider
modified: '2026-08-11'
name: Cortica
nav: Providers
network: true
overview: Cortica is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer-Vision, Machine-Learning, and Autonomous Systems.
random_paper: 6
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cortica/refs/heads/main/screenshots/cortica-2026-09-02T145148.png
security:
- kind: domain-security
  name: Cortica Domain Security
  slug: cortica-domain-security
  summary_line: TLSv1.3
slug: cortica
tags:
- Company
- Artificial Intelligence
- Computer-Vision
- Machine-Learning
- Autonomous Systems
- Venture Builder
- Israel
- Deep Tech
website: https://cortica.com/
---
