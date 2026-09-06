---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  url: security/cliffs-natural-resources-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cleveland-cliffs
- group: company
  title: ''
  type: Website
  url: https://www.clevelandcliffs.com
- group: company
  title: ''
  type: Investor Relations
  url: https://www.clevelandcliffs.com/investors
- group: company
  title: ''
  type: Newsroom
  url: https://www.clevelandcliffs.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clevelandcliffs.com/privacy-policy
- group: other
  title: ''
  type: Canonical Profile
  url: https://raw.githubusercontent.com/api-evangelist/cleveland-cliffs/refs/heads/main/apis.yml
- group: company
  title: ''
  type: Blog
  url: https://www.clevelandcliffs.com/news/news-releases/rss
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cliffs-natural-resources-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Cleveland-Cliffs (the current name for Cliffs Natural Resources) runs no developer program at all — developer/api/docs.clevelandcliffs.com do not resolve, the corporate site serves its standard 404 page for every /.well-known/*, /openapi.json and /llms.txt path, and its own "For Suppliers" page routes partners to login-gated web portals (isupplier.cliffssteel.com, cert.cliffssteel.com) and emailed invoices rather than to any documented interface.
  evidence:
  - status: 0
    url: https://developer.clevelandcliffs.com/
  - status: 404
    url: https://www.clevelandcliffs.com/openapi.json
  - status: 404
    url: https://www.clevelandcliffs.com/.well-known/api-catalog
  - status: 404
    url: https://www.clevelandcliffs.com/llms.txt
  - status: 200
    url: https://www.clevelandcliffs.com/doing-business/for-suppliers
  reason: no-developer-program
  state: none
created: '2026-03-23'
description: Cliffs Natural Resources is the legacy corporate name for what is now Cleveland-Cliffs Inc., a major mining and natural resources company that produces iron ore pellets primarily for steelmaking customers in North America. The company was renamed Cleveland-Cliffs in 2017 and the canonical profile lives at the cleveland-cliffs repo. Cliffs Natural Resources / Cleveland-Cliffs does not publish a public developer portal or general-purpose REST API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cliffs-natural-resources.png
layout: provider
modified: '2026-09-05'
name: Cliffs Natural Resources
nav: Providers
network: true
overview: 'Cliffs Natural Resources is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Iron Ore, Manufacturing, Mining, Steel, and Steelmaking.


  Cliffs Natural Resources'' developer surface includes engineering blog and 8 more developer resources.'
press:
- date: '2026-05-25'
  title: Cliffs Natural Resources Inc. Celebrates 170 Years of Mining
  url: https://www.prnewswire.com/news-releases/cliffs-natural-resources-inc-celebrates-170-years-of-mining-300448500.html
- date: '2026-05-25'
  title: 'Cleveland-Cliffs Vs GRAY MEDIA -A: Which is a Better Buy ...'
  url: https://danelfin.com/stocks/CLF-cleveland-cliffs-vs-GTN.A-gray-media-a-compare
- date: '2026-05-25'
  title: Cleveland-Cliffs Reports First-Quarter 2026 Results
  url: https://earningswhispers.com/epsdetails/CLF
- date: '2026-05-25'
  title: Cliffs Natural Resources renames itself Cleveland-Cliffs Inc.
  url: https://www.uppermichiganssource.com/content/news/Cliffs-Natural-Resources-440498943.html
- date: '2026-05-25'
  title: ANNUAL REPORT 2024
  url: https://www.clevelandcliffs.com/investors/sec-filings/annual-reports/content/0000764065-25-000074/0000764065-25-000074.pdf
random_paper: 10
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cliffs-natural-resources/refs/heads/main/screenshots/cliffs-natural-resources-2026-06-20T174519.png
security:
- kind: domain-security
  name: Cliffs Natural Resources Domain Security
  slug: cliffs-natural-resources-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cliffs-natural-resources
tags:
- Iron Ore
- Manufacturing
- Mining
- Steel
- Steelmaking
website: https://www.clevelandcliffs.com
---
