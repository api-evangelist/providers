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
  url: security/brightloom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightloom.com/
- group: company
  title: ''
  type: Press
  url: https://www.brightloom.com/press/
- group: company
  title: ''
  type: Careers
  url: https://www.brightloom.com/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.brightloom.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brightloom
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Brightloom
coverage:
  checked: '2026-08-14'
  detail: Brightloom's operating estate has been decommissioned — Certificate Transparency shows it ran api.brightloom.com, api-prd/api-dev, the cgp.brightloom.com Customer Growth Platform app, an auth0-cgp Auth0 tenant, and status/support/knowledgebase hosts, and all sixteen of those hostnames now return NXDOMAIN while brightloom.com carries no MX record, leaving only a marketing site frozen at its December 2022 press release whose own nav links (/how-it-works/, /integrations/, /sign-up/) 404 and whose /about/ page serves injected Indonesian gambling search-spam.
  evidence:
  - status: 200
    url: https://www.brightloom.com/
  - status: 404
    url: https://www.brightloom.com/integrations/
  - status: 404
    url: https://www.brightloom.com/sign-up/
  - status: 404
    url: https://www.brightloom.com/openapi.json
  - status: 404
    url: https://www.brightloom.com/graphql
  - status: 404
    url: https://www.brightloom.com/.well-known/agent-card.json
  - status: 404
    url: https://www.brightloom.com/.well-known/api-catalog
  - note: status 0 = no HTTP response at all; curl exits 6 (could not resolve host) because api.brightloom.com is NXDOMAIN. Not a 404 — the host itself is gone.
    status: 0
    url: https://api.brightloom.com/openapi.json
  - status: 200
    url: https://crt.sh/?q=%25.brightloom.com
  reason: defunct
  state: none
created: '2026-08-08'
description: 'Brightloom is a San Francisco customer data and customer intelligence platform for restaurant and retail brands. It began as Eatsa, the automated quinoa-bowl restaurant chain, and rebranded to Brightloom in 2019 when Starbucks licensed select components of its Digital Flywheel customer engagement software to the company, took an equity stake and a board seat alongside a $30M round. The product unifies point-of-sale, loyalty, ecommerce and marketing data into a single customer view, reports on data health, runs AI-driven hyper-segmentation and anomaly detection over that data, and recommends the next campaign and audience a brand should target. Brightloom was sold as an end-user SaaS with prebuilt connectors to common POS, loyalty and marketing platforms rather than as a developer platform, and it published no public API reference, developer portal, SDK or machine-readable specification. The company now appears defunct: the last dated item on its own press page is December 2022,
  the entire operating estate it once held TLS certificates for is gone from DNS — api.brightloom.com, api-prd/api-dev, the cgp.brightloom.com application, its auth0-cgp Auth0 tenant, and the status, support and knowledgebase hosts all NXDOMAIN — brightloom.com publishes no MX record, and only the frozen marketing site remains, with its /about/ page defaced by injected search-spam.'
image: https://www.brightloom.com/assets/components/axl.theme/site/media/fav/apple-touch-icon_v-2.2.png
layout: provider
modified: '2026-08-14'
name: Brightloom
nav: Providers
network: true
overview: Brightloom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Data Platform, Customer Intelligence, Restaurant, and Retail.
random_paper: 8
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brightloom/refs/heads/main/screenshots/brightloom-2026-09-02T144958.png
security:
- kind: domain-security
  name: Brightloom Domain Security
  slug: brightloom-domain-security
  summary_line: TLSv1.3
slug: brightloom
tags:
- Company
- Customer Data Platform
- Customer Intelligence
- Restaurant
- Retail
- Marketing
- Loyalty
- Segmentation
- Point-of-Sale
- Analytics
website: https://www.brightloom.com/
---
