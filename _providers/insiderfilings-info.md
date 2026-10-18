---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Public Beta REST API for normalized SEC ownership transaction line items from Forms 3, 4 and 5.
  name: InsiderFilings API
  slug: insiderfilings-api
- baseURL: https://insiderfilings.info/api/v1
  baseurl_source: declared
  description: The InsiderFilings API V1 — Public Beta API from insiderfilings.info — 1 operation(s) for insiderfilings api v1 — public beta.
  name: insiderfilings.info InsiderFilings API V1 — Public Beta API
  slug: insiderfilings-info-insiderfilings-api-v1-public-beta-api
- baseURL: https://insiderfilings.info/api/v1
  baseurl_source: declared
  description: The Transactions API from insiderfilings.info — 1 operation(s) for transactions.
  name: insiderfilings.info Transactions API
  slug: insiderfilings-info-transactions-api
artifact_total: 4
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/insiderfilings-info/refs/heads/main/conformance/insiderfilings-info-conformance.yml
  title: ''
  type: Conformance
  url: conformance/insiderfilings-info-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/insiderfilings-info/refs/heads/main/llms/insiderfilings-info-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/insiderfilings-info-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/insiderfilings-info/refs/heads/main/hosts/insiderfilings-info-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insiderfilings-info-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/insiderfilings-info/refs/heads/main/vendors/insiderfilings-info-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insiderfilings-info-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insiderfilings.info/privacy.php
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/insiderfilings-info/refs/heads/main/security/insiderfilings-info-domain-security.yml
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
created: '2026-10-11'
description: InsiderFilings.info provides a public beta REST API delivering normalized SEC ownership transaction line items from Forms 3, 4, and 5, including amendments. The service aggregates data from the SEC EDGAR system, updates filings roughly every five minutes, and offers free 7‑day trial access with rate limits of 100 requests per day. It aims to cover all SEC filings from 2025 onward, though historical coverage may be incomplete. Users can query recent insider purchases and sales, explore detailed filing data, and integrate this information into compliance, research, or investment workflows.
image: https://insiderfilings.info/assets/social/preview.png
layout: provider
modified: '2026-10-11'
name: insiderfilings.info
nav: Providers
network: true
overview: 'insiderfilings.info publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including InsiderFilings API V1 — Public Beta API, Transactions API, and 1 more. Tagged areas include Insider Trading, SEC Filings, Financial Data, Research Tools, and Market Data.


  insiderfilings.info''s developer surface includes documentation and 7 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 45.9
    developer_ergonomics: 9.5
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
