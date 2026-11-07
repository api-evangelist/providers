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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.2
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Machine-readable filing data for the post-merger company is published by the U.S. Securities and Exchange Commission, not by the company itself. CIK 0001710366 is the CONSOL Energy Inc. registrant, re
  name: SEC EDGAR Filings (Core Natural Resources, CIK 1710366)
  slug: sec-edgar-filings
- description: 'The public WordPress REST API (wp-json) of the CONSOL Energy website at corenaturalresources.com: the route index of the site''s content management system, catalogued as one site surface rather than as'
  name: CONSOL Energy Website (WordPress REST)
  slug: corenaturalresources-com-website-wordpress-rest
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/consol-energy/finops/consol-energy-finops.yml
  title: ''
  type: FinOps
  url: finops/consol-energy-finops.yml
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
  href: https://artifacts.apis.io/consol-energy/authentication/consol-energy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consol-energy-authentication.yml
- group: design
  href: https://artifacts.apis.io/consol-energy/conventions/consol-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/consol-energy-conventions.yml
- group: design
  href: https://artifacts.apis.io/consol-energy/errors/consol-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/consol-energy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/consol-energy/lifecycle/consol-energy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/consol-energy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/consol-energy/conformance/consol-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consol-energy-conformance.yml
- group: design
  href: https://artifacts.apis.io/consol-energy/data-model/consol-energy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/consol-energy-data-model.yml
- group: auth
  href: https://artifacts.apis.io/consol-energy/security/consol-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consol-energy-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/consol-energy/llms/consol-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consol-energy-llms.txt
- group: agent
  href: https://artifacts.apis.io/consol-energy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/consol-energy/mcp/consol-energy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/consol-energy-mcp.yml
- group: commercial
  href: https://artifacts.apis.io/consol-energy/plans/consol-energy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consol-energy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/consol-energy/rate-limits/consol-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/consol-energy-rate-limits.yml
created: '2026-03-23'
description: 'CONSOL Energy was a Pittsburgh-based bituminous coal producer serving electric utilities, steelmakers and industrial customers. In January 2025 it merged with Arch Resources to form Core Natural Resources, Inc. (NYSE: CNR), and consolenergy.com now 301-redirects to corenaturalresources.com. The company publishes no developer portal, no API documentation, no SDKs and no GitHub organization — but it runs its corporate site on WordPress and serves the WordPress REST API anonymously at https://corenaturalresources.com/wp-json/, a real machine-readable read surface with custom post types for mines (11, with an East/West taxonomy), leadership (16) and news releases (40), plus pages and a 173-item media library holding the supplier terms, Supplier Code of Conduct and sustainability PDFs. Each endpoint was called anonymously on 2026-09-05; writes and admin routes are authenticated (401). Financial data stays third-party, via the SEC EDGAR APIs. See arch-coal for the other merger half.'
finops:
- has_sources: true
  method: generated
  name: Consol Energy Finops
  primary_unit: ''
  service_category: Energy / Coal Mining
  slug: consol-energy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/consol-energy.png
layout: provider
modified: '2026-09-05'
name: CONSOL Energy
nav: Providers
network: true
overview: 'CONSOL Energy publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Bituminous Coal, Coal Mining, Core Natural Resources, Energy, and Investor Relations.


  The CONSOL Energy catalog on APIs.io includes 1 Spectral governance ruleset.


  CONSOL Energy''s developer surface includes authentication and 23 more developer resources.'
plans:
- name: Consol Energy Plans Pricing
  plan_count: 0
  slug: consol-energy-plans-pricing
press:
- date: ''
  title: Core Natural Resources bets on AI data center power ...
  url: https://www.bizjournals.com/pittsburgh/news/2026/02/12/core-natural-resources-artificial-intelligence.html
- date: ''
  title: Arch, Consol to Combine Into $5.2 Billion Coal Giant
  url: https://www.wsj.com/business/energy-oil/coal-miners-arch-consol-agree-to-merger-of-equals-5f9ea0e9
- date: ''
  title: Core Natural Resources –
  url: https://filecache.investorroom.com/mr5ir_consolmining/204/download/CONSOL%20%26%20Arch%20Merger%20Announcement%20Conference%20Call%20Presentation.pdf
- date: ''
  title: Arch Resources and CONSOL Energy to Combine in All- ...
  url: https://www.prnewswire.com/news-releases/arch-resources-and-consol-energy-to-combine-in-all-stock-merger-of-equals-to-create-core-natural-resources-a-premier-north-american-natural-resource-company-focused-on-global-markets-302227383.html
- date: ''
  title: 'Earnings call: CONSOL Energy reported a net income of $58 ...'
  url: https://www.investing.com/news/stock-market-news/earnings-call-consol-energy-reported-a-net-income-of-58-million-93CH-3562829
random_paper: 5
rate_limits:
- limit_count: 0
  name: Consol Energy Rate Limits
  slug: consol-energy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: CONSOL Energy API Rules
  rule_count: 57
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 3
  slug: consol-energy-rules
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 1.7
    developer_ergonomics: 30.4
    discoverability: 63.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/consol-energy/consol-energy-2026-06-20T174910.png
security:
- kind: authentication
  name: Consol Energy Authentication
  slug: consol-energy-authentication
  summary_line: none/cookie-nonce/http-basic · 3 schemes
- kind: domain-security
  name: Consol Energy Domain Security
  slug: consol-energy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: consol-energy-mine-roster
  slug: consol-energy-mine-roster
- name: consol-energy-news-and-disclosures
  slug: consol-energy-news-and-disclosures
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
