---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Procter And Gamble Agentic Access
  operation_count: 3
  slug: procter-and-gamble-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://developer.pg.com
  baseurl_source: declared
  description: Manage and track orders.
  name: Procter & Gamble Orders API
  slug: procter-and-gamble-orders-api
- baseURL: https://developer.pg.com
  baseurl_source: declared
  description: Access P&G product catalog and data.
  name: Procter & Gamble Products API
  slug: procter-and-gamble-products-api
- baseURL: https://developer.pg.com
  baseurl_source: declared
  description: Integration with P&G supply chain operations.
  name: Procter & Gamble Supply Chain API
  slug: procter-and-gamble-supply-chain-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Procter & Gamble API Marketplace
  slug: open-procter-and-gamble-api-marketplace
- collection_type: open
  name: Procter & Gamble API Marketplace Orders API
  slug: open-procter-and-gamble-orders-api
- collection_type: open
  name: Procter & Gamble API Marketplace Orders Products API
  slug: open-procter-and-gamble-products-api
- collection_type: open
  name: Procter & Gamble API Marketplace Orders Supply Chain API
  slug: open-procter-and-gamble-supply-chain-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/procter-and-gamble-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/procter-and-gamble-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/procter-and-gamble-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/procter-and-gamble-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/procter-and-gamble-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/procter-gamble
created: '2026-03-21'
description: Procter & Gamble (P&G) is one of the world's largest consumer goods companies, with a portfolio of trusted brands across beauty, grooming, health care, fabric and home care, and baby, feminine, and family care. P&G operates an API Marketplace at developer.pg.com that provides partners, suppliers, and developers with programmatic access to P&G systems for integrating with the company's supply chain, product data, and business operations.
finops:
- name: Procter And Gamble Finops
  service_category: Consumer Goods
  slug: procter-and-gamble-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/procter-and-gamble.png
layout: provider
modified: '2026-05-19'
name: Procter & Gamble
nav: Providers
network: true
overview: 'Procter & Gamble publishes 3 APIs on the [APIs.io](https://apis.io/) network: Orders API, Products API, and Supply Chain API. Tagged areas include Consumer Goods, Manufacturing, Retail, Supply Chain, and Fortune 100.


  Procter & Gamble''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Procter And Gamble Plans Pricing
  plan_count: 1
  slug: procter-and-gamble-plans-pricing
press:
- date: '2026-05-25'
  title: How P&G Transforms Business Through Technology
  url: https://us.pg.com/blogs/innovation-at-scale-transforming-business-through-technology/
- date: '2026-05-25'
  title: How Procter & Gamble Uses AI to Unlock New Insights ...
  url: https://sloanreview.mit.edu/article/how-procter-gamble-uses-ai-to-unlock-new-insights-from-data/
- date: '2026-05-25'
  title: 'Procter & Gamble Uses AI Agents: 10 Ways to ...'
  url: https://www.klover.ai/procter-gamble-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025/
- date: '2026-05-25'
  title: Google Cloud Helps Power More Personalized Experience ...
  url: https://www.googlecloudpresscorner.com/2020-07-14-Google-Cloud-Helps-Power-More-Personalized-Experience-for-Procter-Gamble-Consumers
- date: '2026-05-25'
  title: How Procter & Gamble is Leveraging AI to Democratize ...
  url: https://www.youtube.com/watch?v=DjxguIe1tqc
random_paper: 16
rate_limits:
- limit_count: 1
  name: Procter And Gamble Rate Limits
  slug: procter-and-gamble-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/procter-and-gamble/refs/heads/main/screenshots/procter-and-gamble-2026-06-20T192133.png
security:
- kind: authentication
  name: Procter And Gamble Authentication
  slug: procter-and-gamble-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Procter And Gamble Domain Security
  slug: procter-and-gamble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Procter And Gamble Vulnerability Disclosure
  slug: procter-and-gamble-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: procter-and-gamble
tags:
- Consumer Goods
- Manufacturing
- Retail
- Supply Chain
- Fortune 100
---
