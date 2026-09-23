---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Quiver Quantitative Agentic Access
  operation_count: 53
  slug: quiver-quantitative-agentic-access
  summary_line: 53 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.quiverquant.com
  baseurl_source: declared
  description: The Beta API from Quiver Quantitative — 2 operation(s) for beta.
  name: Quiver Quantitative Beta API
  slug: quiver-quantitative-beta-api
- baseURL: https://api.quiverquant.com
  baseurl_source: declared
  description: tier 1 endpoint
  name: Quiver Quantitative Tier 1 API
  slug: quiver-quantitative-tier-1-api
- baseURL: https://api.quiverquant.com
  baseurl_source: declared
  description: tier 2 endpoint
  name: Quiver Quantitative Tier 2 API
  slug: quiver-quantitative-tier-2-api
- baseURL: https://api.quiverquant.com
  baseurl_source: declared
  description: The Tier New Constructs Ratings API from Quiver Quantitative — 1 operation(s) for tier new constructs ratings.
  name: Quiver Quantitative Tier New Constructs Ratings API
  slug: quiver-quantitative-tier-new-constructs-ratings-api
artifact_total: 7
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quiverquant.com/termsofservice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quiverquant.com/privacypolicy/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quiver-quantitative/refs/heads/main/agentic-access/quiver-quantitative-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quiver-quantitative-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quiver-quantitative/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quiver-quantitative/refs/heads/main/data-model/quiver-quantitative-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quiver-quantitative-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quiver-quantitative/refs/heads/main/conformance/quiver-quantitative-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quiver-quantitative-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quiver-quantitative/refs/heads/main/overlays/quiver-quantitative-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/quiver-quantitative-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quiver-quantitative/refs/heads/main/llms/quiver-quantitative-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quiver-quantitative-llms.txt
- group: company
  title: ''
  type: Newsroom
  url: https://www.quiverquant.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quiver-quantitative/refs/heads/main/authentication/quiver-quantitative-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quiver-quantitative-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quiver-quantitative/refs/heads/main/security/quiver-quantitative-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quiver-quantitative-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quiverquant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.quiverquant.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.quiverquant.com/api/
- group: company
  title: ''
  type: Blog
  url: https://www.quiverquant.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quiverquant.com/register/?next=pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.quiverquant.com/register/
created: '2026-09-21'
description: Quiver Quantitative provides comprehensive political and financial data APIs, delivering real‑time and historical datasets on congressional trading, insider transactions, lobbying, government contracts, election fundraising, and market‑moving events. Users can query datasets on politicians, stocks, bills, and economic indicators, with subscription plans for analysts, journalists, and fintech developers.
image: https://www.quiverquant.com/static/images/site_preview.png
layout: provider
modified: '2026-09-21'
name: Quiver Quantitative
nav: Providers
network: true
overview: 'Quiver Quantitative publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Beta API, Tier 1 API, Tier 2 API, and 1 more. Tagged areas include Company, Data, Finance, and Politics.


  Quiver Quantitative''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 32.7
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Quiver Quantitative Authentication
  slug: quiver-quantitative-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quiver Quantitative Domain Security
  slug: quiver-quantitative-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quiver-quantitative
tags:
- Company
- Data
- Finance
- Politics
website: https://www.quiverquant.com/
---
