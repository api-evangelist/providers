---
access_model:
  confidence: medium
  label: Public, anonymous, unmetered read access — not sold and not documented
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: Machine-readable filing data for the post-merger company is published by the U.S. Securities and Exchange Commission, not by the company itself. CIK 0001710366 is the CONSOL Energy Inc. registrant, re
  name: SEC EDGAR Filings (Core Natural Resources, CIK 1710366)
  slug: sec-edgar-filings
- baseURL: https://corenaturalresources.com/wp-json
  baseurl_source: declared
  description: 'The "mine" custom post type on the company''s own WordPress host: profiles for 11 mines — Bailey, Enlow Fork, Harvey (the former CONSOL Pennsylvania Mining Complex), Beckley, Itmann, Mountain Laurel, L'
  name: Core Natural Resources Mines Content API
  slug: mines-content-api
- baseURL: https://corenaturalresources.com/wp-json
  baseurl_source: declared
  description: 'The "leader" custom post type: 16 executive leadership and board-member profiles, with a leader-category taxonomy separating the board of directors from executive leadership. Served anonymously by the'
  name: Core Natural Resources Leadership Content API
  slug: leadership-content-api
- baseURL: https://corenaturalresources.com/wp-json
  baseurl_source: declared
  description: 'The "article" custom post type: 40 news releases and corporate articles, grouped by the news-series-title taxonomy (9 terms), alongside the core WordPress post, category and tag types. This is the mac'
  name: Core Natural Resources News Content API
  slug: news-content-api
- baseURL: https://corenaturalresources.com/wp-json
  baseurl_source: declared
  description: Corporate pages (22, including investors, suppliers, sustainability, careers and contact) and the 173-item media library, which is where the supplier terms and conditions, the Supplier Code of Conduct
  name: Core Natural Resources Site Content API
  slug: site-content-api
- baseURL: https://corenaturalresources.com/wp-json
  baseurl_source: declared
  description: 'Self-describing metadata for the host: registered content types and taxonomies, post statuses, cross-type search across all 89 published items, and oEmbed 1.0. This is the surface that makes the rest '
  name: Core Natural Resources Discovery API
  slug: discovery-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://corenaturalresources.com/
- group: company
  title: ''
  type: X-LegacyWebsite
  url: https://consolenergy.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/consol-energy
- group: other
  title: ''
  type: X-Suppliers
  url: https://corenaturalresources.com/suppliers/
- group: company
  title: ''
  type: InvestorRelations
  url: https://corenaturalresources.com/investors/
- group: company
  title: ''
  type: Newsroom
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
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corenaturalresources.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corenaturalresources.com/arch-terms-and-conditions/
- group: auth
  title: ''
  type: Authentication
  url: authentication/consol-energy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/consol-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/consol-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/consol-energy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/consol-energy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/consol-energy-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/consol-energy-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/consol-energy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/consol-energy-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/consol-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/consol-energy-rate-limits.yml
created: '2026-03-23'
description: 'CONSOL Energy was a Pittsburgh-based bituminous coal producer serving electric utilities, steelmakers and industrial customers. In January 2025 it merged with Arch Resources to form Core Natural Resources, Inc. (NYSE: CNR), and consolenergy.com now 301-redirects to corenaturalresources.com. The company publishes no developer portal, no API documentation, no SDKs and no GitHub organization — but it runs its corporate site on WordPress and serves the WordPress REST API anonymously at https://corenaturalresources.com/wp-json/, a real machine-readable read surface with custom post types for mines (11, with an East/West taxonomy), leadership (16) and news releases (40), plus pages and a 173-item media library holding the supplier terms, Supplier Code of Conduct and sustainability PDFs. Each endpoint was called anonymously on 2026-09-05; writes and admin routes are authenticated (401). Financial data stays third-party, via the SEC EDGAR APIs. See arch-coal for the other merger half.'
examples:
- key_count: 15
  name: Consol Energy Content Types
  slug: consol-energy-content-types
finops:
- name: Consol Energy Finops
  service_category: Energy / Coal Mining
  slug: consol-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/consol-energy.png
layout: provider
modified: '2026-09-05'
name: CONSOL Energy
nav: Providers
network: true
overview: 'CONSOL Energy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Core Natural Resources Mines Content API, Core Natural Resources Leadership Content API, Core Natural Resources News Content API, and 2 more. Tagged areas include Bituminous Coal, Coal Mining, Core Natural Resources, Energy, and Investor Relations.


  CONSOL Energy''s developer surface includes authentication and 22 more developer resources.'
plans:
- name: Consol Energy Plans Pricing
  plan_count: 0
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
- limit_count: 0
  name: Consol Energy Rate Limits
  slug: consol-energy-rate-limits
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 15.8
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/consol-energy/refs/heads/main/screenshots/consol-energy-2026-06-20T174910.png
security:
- kind: authentication
  name: Consol Energy Authentication
  slug: consol-energy-authentication
  summary_line: none/cookie-nonce/http-basic · 3 schemes
- kind: domain-security
  name: Consol Energy Domain Security
  slug: consol-energy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
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
