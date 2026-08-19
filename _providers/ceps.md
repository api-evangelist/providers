---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: CEPS exposes its publications and news stream as RSS/Atom feeds that aggregators, knowledge management tools, and policy-monitoring platforms can consume to track CEPS working papers, policy insights,
  name: CEPS Publications RSS / Content Feeds
  slug: ceps-publications-feed
- description: CEPS maintains a calendar of policy events, conferences, task force meetings, and webinars that can be embedded or syndicated via the public events listing pages.
  name: CEPS Events Listings
  slug: ceps-events
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ceps-domain-security.yml
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
  url: https://www.ceps.eu/news/
- group: other
  title: ''
  type: Events
  url: https://www.ceps.eu/events/
- group: other
  title: ''
  type: RSS
  url: https://www.ceps.eu/feed/
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
  url: https://www.ceps.eu/privacy-policy/
created: '2026-01-02'
description: Founded in Brussels in 1983, the Centre for European Policy Studies (CEPS) is a leading independent think tank and forum for debate on EU affairs, with an exceptionally strong in-house research capacity and an extensive network of partner institutes. CEPS conducts rigorous, evidence-based policy research on European and global issues (Data Governance Act, Data Act, AI Act, climate, migration, financial markets) and disseminates its findings primarily through publications, events, and podcasts rather than a commercial API; programmatic access to CEPS output is primarily via public RSS, OPML feeds, and structured publication pages on ceps.eu.
finops:
- name: Ceps Finops
  service_category: API
  slug: ceps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ceps.png
layout: provider
modified: '2026-04-23'
name: CEPS (Centre for European Policy Studies)
nav: Providers
network: true
overview: 'CEPS (Centre for European Policy Studies) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Brussels, Data Governance, EU Policy, European Union, and Policy Research.


  CEPS (Centre for European Policy Studies)''s developer surface includes product news and 10 more developer resources.'
plans:
- name: Ceps Plans Pricing
  plan_count: 3
  slug: ceps-plans-pricing
random_paper: 129
rate_limits:
- limit_count: 5
  name: Ceps Rate Limits
  slug: ceps-rate-limits
score:
  band: minimal
  composite: 7.4
  delta: -5.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
- RSS
- Research
- Think Tank
website: https://www.ceps.eu/
---
