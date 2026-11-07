---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - rate-limits
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.cogentco.com/
- group: company
  title: ''
  type: About
  url: https://www.cogentco.com/en/about-cogent
- group: other
  title: ''
  type: Services
  url: https://www.cogentco.com/en/products-and-services
- group: operate
  title: ''
  type: Support
  url: https://www.cogentco.com/en/customer-service
- group: operate
  title: ''
  type: FAQ
  url: https://www.cogentco.com/faq
- group: start
  title: ''
  type: Login
  url: https://ecogent.cogentco.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.cogentco.com/en/contact/sales-inquiry
- group: company
  title: ''
  type: Blog
  url: https://www.cogentco.com/en/cogent-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cogentco.com/en/?format=feed&type=rss
- group: operate
  title: ''
  type: PressReleases
  url: https://www.cogentco.com/en/about-cogent/press-releases
- group: company
  title: ''
  type: Careers
  url: https://www.cogentco.com/en/about-cogent/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.cogentco.com/en/about-cogent/investor-relations
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.cogentco.com/files/docs/network/performance/global_sla.pdf
- group: design
  href: https://artifacts.apis.io/cogent-communications/lifecycle/cogent-communications-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cogent-communications-lifecycle.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cogentco.com/privacy-policy
- group: commercial
  href: https://artifacts.apis.io/cogent-communications/plans/cogent-communications-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cogent-communications-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cogent-communications/rate-limits/cogent-communications-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cogent-communications-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cogent-communications/finops/cogent-communications-finops.yml
  title: ''
  type: FinOps
  url: finops/cogent-communications-finops.yml
- group: auth
  href: https://artifacts.apis.io/cogent-communications/security/cogent-communications-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cogent-communications-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/cogent-communications/llms/cogent-communications-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cogent-communications-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cogent-communications
- group: other
  title: ''
  type: X
  url: https://twitter.com/cogentco
coverage:
  checked: '2026-09-14'
  detail: Cogent sells network transport, not software, and runs no developer program at all — the cogentco.com sitemap has no developer, API or docs section, api.cogentco.com and developer.cogentco.com are NXDOMAIN, and the only two interactive surfaces (eCogent at ecogent.cogentco.com and the Global Peer Exchange portal) are catch-all login apps that answer HTTP 200 with the same HTML page for every path probed, including a random control path that cannot exist.
  evidence:
  - status: 0
    url: https://developer.cogentco.com/
  - status: 0
    url: https://api.cogentco.com/
  - status: 404
    url: https://www.cogentco.com/openapi.json
  - status: 404
    url: https://www.cogentco.com/llms.txt
  - status: 404
    url: https://www.cogentco.com/.well-known/agent-card.json
  - status: 200
    url: https://ecogent.cogentco.com/.well-known/cogent-communications-negative-control-7f3ab91c.json
  - status: 200
    url: https://www.cogentco.com/en/sitemap
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'Cogent Communications Holdings, Inc. (NASDAQ: CCOI, AS174) is a facilities-based Tier 1 internet service provider headquartered in Washington, DC, selling Dedicated Internet Access, IP Transit, Ethernet, MPLS IP-VPN, SD-WAN, optical wavelength transport, Global Peer Connect peering ports and colocation across its own global fiber network. Cogent publishes no public API, developer portal or machine-readable contract: a full probe on 2026-09-14 found no OpenAPI, AsyncAPI, GraphQL, MCP server or agent card on any host it operates, and the api.cogentco.com and developer.cogentco.com names a prior scaffold recorded do not exist in DNS. Its programmatic-adjacent surfaces are two login-gated portals — eCogent for billing, orders, tickets, DNS changes and IP/BGP requests, and the Global Peer Exchange portal for peering ports. What it does publish openly is a dated Network Services SLA with quantified latency, jitter and packet-delivery commitments, plus monthly network performance
  statistics.'
finops:
- has_sources: true
  method: generated
  name: Cogent Communications Finops
  primary_unit: ''
  service_category: Networking
  slug: cogent-communications-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cogent-communications.png
layout: provider
modified: '2026-09-14'
name: Cogent Communications
nav: Providers
network: true
overview: 'Cogent Communications is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Internet, Networks, Data Center, Telecommunications, and Colocation.


  Cogent Communications'' developer surface includes support, FAQ, engineering blog, and 19 more developer resources.'
plans:
- name: Cogent Communications Plans Pricing
  plan_count: 1
  slug: cogent-communications-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Cogent Communications Rate Limits
  slug: cogent-communications-rate-limits
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cogent-communications/cogent-communications-2026-06-20T174711.png
security:
- kind: domain-security
  name: Cogent Communications Domain Security
  slug: cogent-communications-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cogent-communications
tags:
- Internet
- Networks
- Data Center
- Telecommunications
- Colocation
- Bandwidth
- Ethernet
- Peering
- Fiber
- Internet Service Provider
website: https://www.cogentco.com/
---
