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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://insiderfilings.info/api/v1
  baseurl_source: declared
  description: 'Public Beta REST API for normalized SEC ownership transaction line items from Forms 3, 4 and 5, including amendments. Two GET operations: API status (/) and transactions (/transactions).'
  name: InsiderFilings API
  slug: insiderfilings-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/insiderfilings-info/conformance/insiderfilings-info-conformance.yml
  title: ''
  type: Conformance
  url: conformance/insiderfilings-info-conformance.yml
- group: agent
  href: https://artifacts.apis.io/insiderfilings-info/llms/insiderfilings-info-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/insiderfilings-info-llms.txt
- group: other
  href: https://artifacts.apis.io/insiderfilings-info/hosts/insiderfilings-info-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insiderfilings-info-hosts.yml
- group: other
  href: https://artifacts.apis.io/insiderfilings-info/vendors/insiderfilings-info-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insiderfilings-info-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insiderfilings.info/privacy.php
- group: auth
  href: https://artifacts.apis.io/insiderfilings-info/security/insiderfilings-info-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insiderfilings-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://insiderfilings.info/
- group: docs
  title: ''
  type: Documentation
  url: https://insiderfilings.info/api/v1/docs/
- group: other
  title: ''
  type: Playground
  url: https://playground.insiderfilings.info/
created: '2026-10-11'
description: InsiderFilings.info provides a public beta REST API delivering normalized SEC ownership transaction line items from Forms 3, 4 and 5, including amendments, aggregated from SEC EDGAR and checked for new filings roughly every five minutes. Coverage from 2025 onward is intended to be complete; older historical coverage may be incomplete. A free 7-day trial covers filings accepted by the SEC within the last 30 days, with 100 requests per UTC day, 10 per minute and up to 100 results per request; the trial window is separate from the database's historical coverage. Users can query recent insider purchases and sales, explore detailed filing data, and integrate this information into compliance, research, or investment workflows.
image: https://insiderfilings.info/assets/social/preview.png
layout: provider
modified: '2026-10-21'
name: insiderfilings.info
nav: Providers
network: true
overview: 'insiderfilings.info publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: InsiderFilings API. Tagged areas include Insider Trading, SEC Filings, Financial Data, Research Tools, and Market Data.


  insiderfilings.info''s developer surface includes documentation and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 8.3
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 23.5
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 12.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/insiderfilings-info/insiderfilings-info-2026-11-03T133827.png
security:
- kind: domain-security
  name: Insiderfilings Info Domain Security
  slug: insiderfilings-info-domain-security
  summary_line: TLSv1.3 · HSTS
slug: insiderfilings-info
tags:
- Insider Trading
- SEC Filings
- Financial Data
- Research Tools
- Market Data
website: https://insiderfilings.info/
---
