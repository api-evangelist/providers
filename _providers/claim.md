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
  url: security/claim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.claim.co/
- group: company
  title: ''
  type: Blog
  url: https://www.claim.co/blog
- group: operate
  title: ''
  type: Support
  url: https://help.claim.co/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claim.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claim.co/privacy-policy
coverage:
  checked: '2026-08-09'
  detail: 'Claim is a consumer cash-back app whose merchant pitch is explicitly the absence of an integration — "no integrations, no setup, no training, no fees" on claim.co/merchants — so there is nothing for a developer to call: claim.co is a Webflow marketing site that 404s /openapi.json, /llms.txt, /graphql and every /.well-known/ path, api.claim.co, docs.claim.co, developer.claim.co and app.claim.co do not resolve in DNS, help.claim.co is an Intercom FAQ for diners with no API section, and there is no public GitHub org or npm package under any Claim name.'
  evidence:
  - status: 404
    url: https://www.claim.co/openapi.json
  - status: 404
    url: https://www.claim.co/llms.txt
  - status: 404
    url: https://www.claim.co/graphql
  - status: 404
    url: https://www.claim.co/.well-known/security.txt
  - status: 404
    url: https://www.claim.co/.well-known/agent-card.json
  - status: 404
    url: https://www.claim.co/.well-known/agent.json
  - status: 404
    url: https://www.claim.co/.well-known/api-catalog
  - status: 404
    url: https://api.github.com/orgs/claim
  - status: 200
    url: https://help.claim.co/en/
  - status: 200
    url: https://www.claim.co/merchants
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: Claim — legally Claim Digital Assets, Inc. — is a New York consumer rewards app that pays people cash back for showing up in person at restaurants and retailers. Every Thursday its "Drop" matches a user with three nearby merchants; the user picks one, pays with a card linked through Plaid, and Claim reimburses them automatically over Venmo. Users can also trade Claims with friends, the social mechanic behind its "Benefits with Friends" positioning. Merchants buy performance-based customer acquisition instead of impressions, and Claim markets the program as turnkey — "no integrations, no setup, no training, no fees" — paying only when a guest transacts. Claim raised a $12M Series A led by VMG Technology in October 2024 ($20M raised in total, with Sequoia Capital and Susa Ventures) and was acquired by Wonder Group, Inc. in January 2026, where it now scales inside Grubhub and Seamless. Claim publishes no developer program, no API reference, and no machine-readable contract of any
  kind.
image: https://cdn.prod.website-files.com/671663e3283d42df61362740/6973e237337e7a6d15f9fc25_og-image-home-new.png
layout: provider
modified: '2026-08-09'
name: Claim
nav: Providers
network: true
overview: 'Claim is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Apps, Rewards, Loyalty, and Cash Back.


  Claim''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Claim Domain Security
  slug: claim-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: claim
tags:
- Company
- Consumer Apps
- Rewards
- Loyalty
- Cash Back
- Restaurant
- Food and Beverage
- Social Network
- Brand Marketing
- Mobile Apps
website: https://www.claim.co/
---
