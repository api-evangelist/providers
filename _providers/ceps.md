---
access_model:
  confidence: high
  label: Free public web content, no programmatic access
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - probe
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
api_count: 2
apis:
- description: CEPS publishes roughly 150 working papers, policy insights, reports and commentaries a year across some 20 policy topics, listed on the public publications page and filterable by topic. This entry was
  name: CEPS Publications RSS / Content Feeds
  slug: ceps-publications-feed
- description: CEPS maintains a public calendar of policy events, conferences, task force meetings, roundtables and webinars at /ceps-events/, filterable by event type and by upcoming/past state through query parame
  name: CEPS Events Listings
  slug: ceps-events
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ceps-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ceps-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ceps-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ceps
- group: company
  title: ''
  type: Website
  url: https://www.ceps.eu/
- group: company
  title: ''
  type: About
  url: https://www.ceps.eu/about-ceps/
- group: other
  title: ''
  type: Publications
  url: https://www.ceps.eu/ceps-publications/
- group: company
  title: ''
  type: News
  url: https://www.ceps.eu/ceps-news/
- group: other
  title: ''
  type: Events
  url: https://www.ceps.eu/ceps-events/
- group: company
  title: ''
  type: Blog
  url: https://www.ceps.eu/ceps-latest/
- group: operate
  title: ''
  type: Support
  url: https://www.ceps.eu/contact/
- group: other
  title: ''
  type: Knowledge4Policy
  url: https://knowledge4policy.ec.europa.eu/organisation/ceps-centre-european-policy-studies_en
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Centre_for_European_Policy_Studies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ceps.eu/about-ceps/data-privacy-policy/
coverage:
  checked: '2026-09-05'
  detail: 'CEPS is a Brussels policy research institute whose product is publications and events, not software: it runs no developer program, and the one machine-readable surface it used to serve — the site-wide WordPress RSS feed at /feed/ — now answers HTTP 500 "No feed available" and is Disallow''d in robots.txt, leaving the WordPress REST root the site itself declares at /wp-json/ (also robots-disallowed, and honored unprobed) as the only programmatic thing on the domain.'
  evidence:
  - status: 500
    url: https://www.ceps.eu/feed/
  - status: 404
    url: https://www.ceps.eu/llms.txt
  - status: 404
    url: https://www.ceps.eu/.well-known/agent-card.json
  - status: 200
    url: https://www.ceps.eu/robots.txt
  reason: not-a-software-company
  state: none
created: '2026-01-02'
description: 'Founded in Brussels in 1983, the Centre for European Policy Studies (CEPS) is a leading independent think tank and forum for debate on EU affairs, with strong in-house research capacity and an extensive network of partner institutes. CEPS conducts evidence-based policy research on European and global issues (Data Governance Act, Data Act, AI Act, climate, energy, migration, trade, defence, financial markets) and disseminates it through publications, events, task forces and podcasts rather than through any programmatic interface. CEPS publishes no API, SDK or developer program, and as of 2026-09-05 has no working machine-readable surface: the RSS feed this record once pointed at returns HTTP 500 ("No feed available") and is robots-disallowed, and no OpenAPI, AsyncAPI, GraphQL SDL, MCP server, A2A agent card or /.well-known/ document exists on any ceps.eu host. Following CEPS now means the newsletter or the HTML listings on ceps.eu.'
finops:
- name: Ceps Finops
  service_category: API
  slug: ceps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ceps.png
layout: provider
modified: '2026-09-05'
name: CEPS (Centre for European Policy Studies)
nav: Providers
network: true
overview: 'CEPS (Centre for European Policy Studies) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Brussels, Data Governance, EU Policy, European Union, and Policy Research.


  CEPS (Centre for European Policy Studies)''s developer surface includes product news, engineering blog, support, and 11 more developer resources.'
plans:
- name: Ceps Plans Pricing
  plan_count: 0
  slug: ceps-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Ceps Rate Limits
  slug: ceps-rate-limits
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ceps/refs/heads/main/screenshots/ceps-2026-06-20T174141.png
security:
- kind: domain-security
  name: Ceps Domain Security
  slug: ceps-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ceps
tags:
- Brussels
- Data Governance
- EU Policy
- European Union
- Policy Research
- Publications
- Research
- Think Tank
website: https://www.ceps.eu/
---
