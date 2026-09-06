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
  url: security/good-meat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goodmeat.co/
- group: company
  title: ''
  type: About
  url: https://www.goodmeat.co/about
- group: operate
  title: ''
  type: Contact
  url: https://www.goodmeat.co/contact
- group: company
  title: ''
  type: Careers
  url: https://www.goodmeat.co/careers
- group: company
  title: ''
  type: Blog
  url: https://www.goodmeat.co/stories
- group: company
  title: ''
  type: Newsroom
  url: https://www.goodmeat.co/newsroom
- group: operate
  title: ''
  type: FAQ
  url: https://www.goodmeat.co/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodmeat.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodmeat.co/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EatJust
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/goodmeat/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.ju.st/
coverage:
  checked: '2026-08-22'
  detail: GOOD Meat sells cultivated chicken as a physical food product through restaurants and grocers; its entire published surface — enumerated from its own sitemap-us-en.xml.gz — is marketing, stories, news, careers and legal pages, with no developer, docs or API path anywhere, and parent Eat Just's GitHub organization (github.com/EatJust) has zero public repositories.
  evidence:
  - status: 200
    url: https://www.goodmeat.co/
  - status: 404
    url: https://www.goodmeat.co/openapi.json
  - status: 404
    url: https://www.goodmeat.co/graphql
  - status: 404
    url: https://www.goodmeat.co/llms.txt
  - status: 404
    url: https://www.goodmeat.co/.well-known/agent-card.json
  - status: 404
    url: https://www.goodmeat.co/developers
  - status: 404
    url: https://www.ju.st/openapi.json
  - status: 200
    url: https://api.github.com/orgs/eatjust
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'GOOD Meat is the cultivated-meat division of Eat Just, Inc., a San Francisco food technology company. It grows real chicken from animal cells in production bioreactors rather than by raising and slaughtering birds, and it was the first company in the world cleared to sell cultivated meat to consumers — approved in Singapore in December 2020, then cleared by the U.S. FDA in March 2023 and granted USDA label approval and grant of inspection in June 2023. Its products have been served at 1880 and Huber''s Butchery in Singapore and at José Andrés'' China Chilcano in Washington, D.C., and in May 2024 it became the first cultivated meat sold at retail. GOOD Meat is a consumer packaged-food and foodservice brand: it sells meat, not software. It operates no developer program, publishes no API, SDK, webhook or machine-readable specification, and its parent''s GitHub organization carries no public repositories.'
image: https://assets.goodmeat.co/cdn/f/168369/1920x1080/ce40305d2e/gm_logo4.png
layout: provider
modified: '2026-08-22'
name: GOOD Meat
nav: Providers
network: true
overview: 'GOOD Meat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Cultivated Meat, Agriculture Technology, and Consumer Packaged Goods.


  GOOD Meat''s developer surface includes engineering blog, FAQ, and 11 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/good-meat/refs/heads/main/screenshots/good-meat-2026-09-02T145620.png
security:
- kind: domain-security
  name: Good Meat Domain Security
  slug: good-meat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: good-meat
tags:
- Company
- Food and Beverage
- Cultivated Meat
- Agriculture Technology
- Consumer Packaged Goods
- Biotechnology
- Food Technology
- Sustainability
website: https://www.goodmeat.co/
---
