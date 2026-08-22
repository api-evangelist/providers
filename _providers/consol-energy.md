---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
api_count: 1
apis:
- description: Machine-readable filing data for the post-merger company is published by the U.S. Securities and Exchange Commission, not by the company itself. CIK 0001710366 is the CONSOL Energy Inc. registrant, re
  name: SEC EDGAR Filings (Core Natural Resources, CIK 1710366)
  slug: sec-edgar-filings
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/consol-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/consol-energy
- group: company
  title: ''
  type: Website
  url: https://corenaturalresources.com/
- group: company
  title: ''
  type: Legacy Website
  url: https://www.consol-energy.com
- group: other
  title: ''
  type: Suppliers
  url: https://corenaturalresources.com/suppliers/
- group: company
  title: ''
  type: Investors
  url: https://corenaturalresources.com/investors/
- group: company
  title: ''
  type: News
  url: https://corenaturalresources.com/news-media/
- group: other
  title: ''
  type: Sustainability
  url: https://corenaturalresources.com/sustainability/
- group: company
  title: ''
  type: Careers
  url: https://corenaturalresources.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://corenaturalresources.com/contact-us/
created: '2026-03-23'
description: CONSOL Energy was a Pittsburgh-based coal mining company that produced high-quality bituminous coal from underground mines for sale to electric utilities, steelmakers, and industrial customers. In 2025 CONSOL Energy merged with Arch Resources to form Core Natural Resources, and the consolenergy.com domain now redirects to corenaturalresources.com. The combined company does not publish public developer APIs; its external digital surface is organized around an investor relations site, a suppliers page (with downloadable terms, conditions, and a Supplier Code of Conduct), and corporate sustainability/safety disclosures — all HTML and PDF, with no documented endpoints and no XML feeds (probed 2026-07-25). Those pages are listed below as website surfaces, not as APIs. The only verified programmatic access to this company's data is the SEC's own EDGAR APIs. See the sibling profile arch-coal for the other half of the merger.
finops:
- name: Consol Energy Finops
  service_category: Energy / Coal Mining
  slug: consol-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/consol-energy.png
layout: provider
modified: '2026-04-28'
name: CONSOL Energy
nav: Providers
network: true
overview: 'CONSOL Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bituminous Coal, Coal Mining, Core Natural Resources, Energy, and Investor Relations.


  CONSOL Energy''s developer surface includes product news and 9 more developer resources.'
plans:
- name: Consol Energy Plans Pricing
  plan_count: 1
  slug: consol-energy-plans-pricing
press:
- date: '2026-05-25'
  title: Core Natural Resources bets on AI data center power ...
  url: https://www.bizjournals.com/pittsburgh/news/2026/02/12/core-natural-resources-artificial-intelligence.html
- date: '2026-05-25'
  title: Arch, Consol to Combine Into $5.2 Billion Coal Giant
  url: https://www.wsj.com/business/energy-oil/coal-miners-arch-consol-agree-to-merger-of-equals-5f9ea0e9
- date: '2026-05-25'
  title: Core Natural Resources –
  url: https://filecache.investorroom.com/mr5ir_consolmining/204/download/CONSOL%20%26%20Arch%20Merger%20Announcement%20Conference%20Call%20Presentation.pdf
- date: '2026-05-25'
  title: Arch Resources and CONSOL Energy to Combine in All- ...
  url: https://www.prnewswire.com/news-releases/arch-resources-and-consol-energy-to-combine-in-all-stock-merger-of-equals-to-create-core-natural-resources-a-premier-north-american-natural-resource-company-focused-on-global-markets-302227383.html
- date: '2026-05-25'
  title: 'Earnings call: CONSOL Energy reported a net income of $58 ...'
  url: https://www.investing.com/news/stock-market-news/earnings-call-consol-energy-reported-a-net-income-of-58-million-93CH-3562829
random_paper: 5
rate_limits:
- limit_count: 1
  name: Consol Energy Rate Limits
  slug: consol-energy-rate-limits
score:
  band: minimal
  composite: 7.6
  delta: -1.5
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/consol-energy/refs/heads/main/screenshots/consol-energy-2026-06-20T174910.png
security:
- kind: domain-security
  name: Consol Energy Domain Security
  slug: consol-energy-domain-security
  summary_line: TLSv1.3
slug: consol-energy
tags:
- Bituminous Coal
- Coal Mining
- Core Natural Resources
- Energy
- Investor Relations
- Mining
- Suppliers
- Sustainability
- Fortune 1000
website: https://corenaturalresources.com/
---
