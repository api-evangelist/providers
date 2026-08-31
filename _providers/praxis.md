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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/praxis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.praxisnation.com/
- group: company
  title: ''
  type: Blog
  url: https://www.praxisnation.com/news
- group: start
  title: ''
  type: SignUp
  url: https://www.praxisnation.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.praxisnation.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.praxisnation.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsletter
  url: https://praxisnation.substack.com
- group: company
  title: ''
  type: Twitter
  url: https://x.com/praxisnation
coverage:
  checked: '2026-08-26'
  detail: Praxis is a membership community and city-development venture whose only software surface is a members-only account portal at portal.praxisnation.com; its internal Next.js routes under /api/ answer 401 with a null body to anonymous callers, and the company publishes no developer portal, documentation or machine-readable contract on any host it controls.
  evidence:
  - status: 404
    url: https://www.praxisnation.com/openapi.json
  - status: 404
    url: https://www.praxisnation.com/.well-known/agent-card.json
  - status: 404
    url: https://www.praxisnation.com/llms.txt
  - status: 401
    url: https://portal.praxisnation.com/api/openapi.json
  - status: 200
    url: https://www.praxisnation.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Praxis is a New York-based company building an internet-native community and city-development venture — "an online community starting a new city" — founded in 2019 by Dryden Brown and Charlie Callinan. It operates a membership community at praxisnation.com whose stated purpose is to create a new culture and a resident-owned physical city, and a members-only account portal at portal.praxisnation.com where members view their PRAX holdings and manage their account. In October 2024 Praxis announced $525M in financing toward development of its first city. Praxis is a real-estate, community and smart-cities company, not a software vendor: it publishes no developer program, no API documentation, and no machine-readable API contract on any host it controls.'
image: https://d3b16n6zj6onqf.cloudfront.net/images/og-image.png
layout: provider
modified: '2026-08-26'
name: Praxis
nav: Providers
network: true
overview: 'Praxis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, Smart Cities, Communities, and Membership.


  Praxis'' developer surface includes engineering blog, signup flow, and 6 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Praxis Domain Security
  slug: praxis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: praxis
tags:
- Company
- Real-Estate
- Smart Cities
- Communities
- Membership
- Urban Development
- Network State
website: https://www.praxisnation.com/
---
