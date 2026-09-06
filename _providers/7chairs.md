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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://circlesup.com/
- group: company
  title: ''
  type: About
  url: https://circlesup.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://circlesup.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://circlesup.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://circlesup.typeform.com/to/e5q9ZYmq
- group: start
  title: ''
  type: Login
  url: https://circlesup.com/app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://circlesup.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circlesup.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/7chairs
- group: auth
  title: ''
  type: DomainSecurity
  url: security/7chairs-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/7chairs-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Circles is a direct-to-consumer subscription mental-health app with no developer program at all - circlesup.com/developers/ and circlesup.com/api/ are soft-404s from the WordPress catch-all, and the api.circlesup.com host that does exist answers every path, including its root, with an nginx 503 page rather than any documented surface.
  evidence:
  - status: 200
    url: https://circlesup.com/developers/
  - status: 200
    url: https://circlesup.com/api/
  - status: 503
    url: https://api.circlesup.com/openapi.json
  - status: 200
    url: https://app.circlesup.com/openapi.json
  - status: 200
    url: https://circlesup.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 'Circles (legal entity 7Chairs Ltd, founded 2020 by Irad Eichler and Guy Winch) is a consumer digital mental-health company operating an online emotional support platform at circlesup.com. It runs live, facilitator-led audio and video support groups plus peer chat for people working through narcissistic abuse, toxic relationships, breakups, divorce, grief, anxiety and stress, delivered through iOS and Android apps and a web app at app.circlesup.com. It is a direct-to-consumer subscription service, not a developer platform: as of the 2026-09-05 enrichment pass the company publishes no developer portal, no API documentation and no machine-readable contract, and its api.circlesup.com host answers every request with an HTTP 503 edge page.'
image: https://circlesup.com/wp-content/uploads/2023/03/image-96.png
layout: provider
modified: '2026-09-05'
name: Circles - Online Group Support
nav: Providers
network: true
overview: 'Circles - Online Group Support is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Health Care, Wellness, and Consumer Applications.


  Circles - Online Group Support''s developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 7Chairs Domain Security
  slug: 7chairs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 7chairs
tags:
- Company
- Mental Health
- Health Care
- Wellness
- Consumer Applications
- Support Groups
- Mobile Applications
- Subscription
website: https://circlesup.com/
---
