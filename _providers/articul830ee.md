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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/articul830ee/refs/heads/main/vendors/articul830ee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/articul830ee-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/articul830ee/refs/heads/main/hosts/articul830ee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/articul830ee-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.articul8.ai/
- group: start
  title: ''
  type: SignUp
  url: https://auth.articul8.ai/signup?redirect_uri=https%3A%2F%2Fapi-docs.articul8.ai%2Fparseauth&response_type=code&client_id=6deln67aomph0q5e3j460jg8e&state=eyJub25jZSI6IjE3OTA0MTAxOTJUNndTdkNlX0huUkdneF93aCIsInJlcXVlc3RlZFVyaSI6Ii8ifQ&scope=phone%20email%20profile%20openid%20aws.cognito.signin.user.admin&code_challenge_method=S256&code_challenge=NQAl3xAFwQzhoGIZ8JtPi2fwEFE718ipYZU98wMEOeU
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.articul8.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.articul8.ai/news
- group: company
  title: ''
  type: Blog
  url: https://www.articul8.ai/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/articul830ee/refs/heads/main/security/articul830ee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/articul830ee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.articul8.ai
coverage:
  checked: 2026-09-26
  detail: The provider's API documentation pages return HTML shells and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 404
    url: https://api.articul8.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Articul830ee (operating as Articul8) provides a domain‑specific Generative AI platform purpose‑built for enterprise data and mission‑critical applications. The platform offers autonomous agents, model orchestration, and traceable outcomes, targeting industries such as semiconductor design, supply‑chain management, and engineering standards. It emphasizes observability, auditability, and personalized AI solutions for complex enterprise missions.
image: https://assets.articul8.ai/Techstack_Aug_2125_1_191cc1f8d9.png
layout: provider
modified: '2026-09-26'
name: Articul830ee
nav: Providers
network: true
overview: 'Articul830ee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Generative AI, Enterprise, and Platform.


  Articul830ee''s developer surface includes signup flow, engineering blog, and 7 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Articul830Ee Domain Security
  slug: articul830ee-domain-security
  summary_line: TLSv1.3 · DMARC
slug: articul830ee
tags:
- Company
- Artificial Intelligence
- Generative AI
- Enterprise
- Platform
- DomainSpecific
website: https://www.articul8.ai
---
