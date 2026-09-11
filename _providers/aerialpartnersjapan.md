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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.aerial-p.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aerial-p.com/media
- group: operate
  title: ''
  type: Support
  url: https://www.aerial-p.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aerial-p.com/document/regulation.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerial-p.com/document/privacypolicy.html
- group: commercial
  title: ''
  type: Plans
  url: plans/aerialpartnersjapan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aerialpartnersjapan-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aerialpartnersjapan-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerialpartnersjapan-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aerialpartnersjapan-llms.txt
coverage:
  checked: '2026-09-10'
  detail: 'The only API Aerial Partners markets — the "Gtax Network API" on its Gtax Network page — has no reference, no spec and no signup: the page ends by directing every enquiry to the corporate contact form, and ADM and AWA are sold the same way, so nothing about the contract is readable without a sales conversation.'
  evidence:
  - status: 200
    url: https://www.aerial-p.com/others/gtax_network.html
  - status: 200
    url: https://www.aerial-p.com/service
  - status: 404
    url: https://www.aerial-p.com/openapi.json
  - status: 404
    url: https://www.aerial-p.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-10'
description: 'Aerial Partners (株式会社Aerial Partners, Roppongi, Minato-ku, Tokyo) builds digital-asset accounting, tax and data-management software for the Japanese market. Its current product line is AWA (Aerial Web3 Accounting), an accounting-support tool for Web3 businesses handling crypto assets and NFTs, and ADM (Aerial Data Management), a management-accounting and statutory-ledger data platform for crypto-asset exchange operators and Type I financial instruments business operators. The company also resells Lukka Insights, the crypto data platform of its parent, Lukka, which acquired Aerial Partners in January 2025. Aerial Partners originated Gtax, the consumer and tax-accountant crypto profit-and-loss calculator, and Guardian, its tax-filing support service; both moved to 株式会社Gtax, which pafin acquired in July 2026 and is folding into Cryptact on 5 October 2026. Aerial Partners publishes no public developer portal, API reference or machine-readable contract: the only API it markets is
  the "Gtax Network API", a joint-development BtoBtoC offering for exchange operators reachable only through the corporate inquiry form.'
image: https://www.aerial-p.com/wp-content/uploads/2023/10/aerial_p_OGP-–-2.png
layout: provider
modified: '2026-09-10'
name: Aerial Partners
nav: Providers
network: true
overview: 'Aerial Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Digital Assets, Accounting, and Tax.


  Aerial Partners'' developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Aerialpartnersjapan Plans Pricing
  plan_count: 0
  slug: aerialpartnersjapan-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Aerialpartnersjapan Rate Limits
  slug: aerialpartnersjapan-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerialpartnersjapan Domain Security
  slug: aerialpartnersjapan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aerialpartnersjapan
tags:
- Company
- Cryptocurrency
- Digital Assets
- Accounting
- Tax
- Web3
- Financial Services
- Japan
- Data Management
- Blockchain
website: https://www.aerial-p.com/
---
