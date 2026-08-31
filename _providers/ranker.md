---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ranker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ranker.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ranker.com/terms
created: '2026-07-17'
description: Ranker is a consumer internet company that runs ranker.com, a crowdsourced ranking and voting platform where users vote on and create rankings across pop culture, entertainment, film, TV, music, food, sports, and other consumer topics. Its business arm licenses "Ranker Insights" audience-intelligence and opinion-graph data - drawn from more than 1.5 billion votes, 115 million voters, and 260,000 rankings - to brands, agencies, publishers, and for AI/LLM training. Ranker does not publish a public, self-serve developer API; a private api.ranker.com powers the site and its robots.txt prohibits automated scraping and AI/LLM training use. Data access is sales-led via business.ranker.com. Backed by Bullpen Capital and DCVC.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ranker.png
layout: provider
modified: '2026-07-20'
name: Ranker
nav: Providers
network: true
overview: Ranker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Entertainment, Media, and Rankings.
random_paper: 13
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Ranker Domain Security
  slug: ranker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ranker
tags:
- Company
- Consumer
- Entertainment
- Media
- Rankings
- Audience Intelligence
- Data Licensing
- Market Research
website: https://www.ranker.com
---
