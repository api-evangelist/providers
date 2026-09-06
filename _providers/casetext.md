---
access_model:
  confidence: high
  label: Retired
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://casetext.com/pricing/'', ''status'': 410}'
  - '{''url'': ''https://casetext.com/signin/'', ''status'': 410}'
  - '{''url'': ''https://casetext.com/'', ''status'': 301, ''note'': ''redirects to thomsonreuters.com/en/cocounsel''}'
  - '{''url'': ''https://casetext.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.thomsonreuters.com/en/cocounsel — a different registrable domain (casetext.com -> thomsonreuters.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/casetext-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/casetext-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/casetext-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/casetext-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/casetext-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/casetext-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://casetext.com
- group: other
  title: ''
  type: Successor
  url: https://www.thomsonreuters.com/en/cocounsel
- group: other
  title: ''
  type: ParentCompany
  url: https://www.thomsonreuters.com
- group: other
  title: ''
  type: Acquisition
  url: https://www.thomsonreuters.com/en/press-releases/2023/august/thomson-reuters-completes-acquisition-of-casetext-inc
- group: build
  title: ''
  type: GitHub
  url: https://github.com/casetext
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/casetext
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/casetext
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/casetext
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Casetext
coverage:
  checked: '2026-08-10'
  detail: Casetext was absorbed into Thomson Reuters and the standalone platform was shut down on 2025-04-01; casetext.com now 301s to thomsonreuters.com/en/cocounsel and every other path on the domain — including /pricing/, /blog/, /signin/, /robots.txt and every /.well-known/ path — returns HTTP 410 Gone behind a "This service is no longer available" notice, while api., developer., docs. and app.casetext.com no longer resolve.
  evidence:
  - status: 301
    url: https://casetext.com/
  - status: 410
    url: https://casetext.com/pricing/
  - status: 410
    url: https://casetext.com/graphql
  - status: 410
    url: https://casetext.com/openapi.json
  - status: 410
    url: https://casetext.com/.well-known/agent-card.json
  - status: 410
    url: https://parallelsearch.casetext.com/
  - status: 404
    url: https://compose.law/
  reason: defunct
  state: none
created: '2026-05-25'
description: 'Casetext is a legal technology company founded in 2013 by Jake Heller, Joanna Huey, and Laurence Pfeffer and headquartered in San Francisco, California. The company built one of the earliest neural-search engines for U.S. case law (Parallel Search) and a broader research platform covering federal and state cases, statutes, regulations, and secondary sources, with citator signals delivered through its SmartCite feature. Casetext is best known for CoCounsel, a generative-AI legal assistant released in March 2023 and originally built on top of OpenAI''s GPT-4, that automates document review, deposition preparation, contract analysis, legal research memos, and database queries for law firms and in-house legal teams. Companion products include AllSearch, a private document search tool that lets firms run Parallel Search across their own document collections, and Compose, an automated brief-drafting product. Thomson Reuters acquired Casetext in June 2023 for $650 million in an all-cash
  deal that closed on August 17, 2023, and CoCounsel has since been integrated across Thomson Reuters'' Westlaw, Practical Law, and HighQ product lines as the company''s flagship legal-AI assistant. Casetext is now a RETIRED BRAND rather than an active provider: casetext.com began redirecting to a Thomson Reuters CoCounsel page on February 1, 2025, CoCounsel 1.0 access on the Casetext platform ended March 31, 2025, and the standalone platform was shut down on April 1, 2025. As of August 2026 every path on the domain returns HTTP 410 Gone behind a hand-written retirement notice pointing users to Westlaw, and the developer-facing subdomains do not resolve. Casetext never published a public developer API, SDK, or machine-readable specification of any kind; the casetext GitHub organization holds 79 fully archived repositories — research forks (transformers, ELECTRA, pgvector, FiD) and early JavaScript infrastructure utilities — and the 15 npm packages it published are general-purpose libraries
  rather than API clients, the newest released in June 2018.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/casetext.png
layout: provider
modified: '2026-08-10'
name: Casetext
nav: Providers
network: true
overview: 'Casetext is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Legal Tech, Legal Research, Case Law, and Legal AI.


  Casetext''s developer surface includes GitHub presence and 14 more developer resources.'
plans:
- name: Casetext Plans Pricing
  plan_count: 0
  slug: casetext-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Casetext Rate Limits
  slug: casetext-rate-limits
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 10
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/casetext/refs/heads/main/screenshots/casetext-2026-06-20T174038.png
security:
- kind: domain-security
  name: Casetext Domain Security
  slug: casetext-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: casetext
tags:
- Legal
- Legal Tech
- Legal Research
- Case Law
- Legal AI
- Generative AI
- CoCounsel
- Parallel Search
- AllSearch
- Compose
- SmartCite
- Document Review
- Contract Analysis
- Deposition Preparation
- Thomson Reuters
website: https://casetext.com
---
