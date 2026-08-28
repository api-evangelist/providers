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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Fantasy Sports APIs provide URIs used to access fantasy sports data. Currently the APIs support retrieval of Fantasy Football, Baseball, Basketball, and Hockey data including game, league, team, a
  name: Yahoo
  slug: yahoo
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yahoo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yahoo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yahoo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yahoo
created: '2025-02-08'
description: The Fantasy Sports APIs provide URIs used to access fantasy sports data. Currently the APIs support retrieval of Fantasy Football, Baseball, Basketball, and Hockey data including game, league, team, and player information. The APIs are based on a RESTful model. Therefore, resources like game, league, team, player etc. and collections like games, leagues, teams, players form the building blocks for these APIs.
finops:
- name: Yahoo Finops
  service_category: API
  slug: yahoo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yahoo.png
layout: provider
modified: '2026-03-16'
name: Yahoo
nav: Providers
network: true
overview: Yahoo publishes 1 API on the [APIs.io](https://apis.io/) network.
plans:
- name: Yahoo Plans Pricing
  plan_count: 3
  slug: yahoo-plans-pricing
press:
- date: '2026-05-25'
  title: Artificial intelligence
  url: https://finance.yahoo.com/topic/artificial-intelligence/
- date: '2026-05-25'
  title: AI News, Updates, Products and Reviews
  url: https://tech.yahoo.com/ai/
- date: '2026-05-25'
  title: Yahoo - The rapid growth of cloud computing and artificial ...
  url: https://www.facebook.com/yahoofinance/photos/the-rapid-growth-of-cloud-computing-and-artificial-intelligence-has-fueled-deman/1084123300249114/
- date: '2026-05-25'
  title: Introducing Yahoo Scout, a New AI Answer Engine
  url: https://www.yahooinc.com/press/introducing-yahoo-scout-a-new-ai-answer-engine
- date: '2026-05-25'
  title: How to Structure Press Releases for Maximum AI Visibility
  url: https://finance.yahoo.com/news/structure-press-releases-maximum-ai-091000311.html
random_paper: 19
rate_limits:
- limit_count: 5
  name: Yahoo Rate Limits
  slug: yahoo-rate-limits
score:
  band: emerging
  composite: 11.4
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 9.5
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yahoo/refs/heads/main/screenshots/yahoo-2026-06-20T201726.png
security:
- kind: domain-security
  name: Yahoo Domain Security
  slug: yahoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yahoo Vulnerability Disclosure
  slug: yahoo-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: yahoo
---
