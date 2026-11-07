---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_PROXY_HOST:YOUR_PORT
  baseurl_source: declared
  description: The RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) API API from RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) — 1 operation(s) for rapidproxy (rapid terminal uk network limited) api.
  name: RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) API
  slug: rapidproxy-rapidproxy-rapid-terminal-uk-network-limited-api-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/rapidproxy/plans/rapidproxy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rapidproxy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rapidproxy/rules/rapidproxy-rules.yml
  title: ''
  type: Spectral
  url: rules/rapidproxy-rules.yml
- group: design
  href: https://artifacts.apis.io/rapidproxy/conformance/rapidproxy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rapidproxy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rapidproxy/llms/rapidproxy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rapidproxy-llms.txt
- group: agent
  href: https://artifacts.apis.io/rapidproxy/well-known/rapidproxy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rapidproxy-well-known.yml
- group: other
  href: https://artifacts.apis.io/rapidproxy/hosts/rapidproxy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rapidproxy-hosts.yml
- group: other
  href: https://artifacts.apis.io/rapidproxy/vendors/rapidproxy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rapidproxy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rapidproxy.io/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rapidproxy.io/privacy_policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rapidproxy.io/residential-proxies/pricing
- group: start
  title: ''
  type: Login
  url: https://www.rapidproxy.io/user/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rapidproxy.io/proxies/getting-started
- group: auth
  href: https://artifacts.apis.io/rapidproxy/security/rapidproxy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rapidproxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rapidproxy.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rapidproxy.io/proxies/integration-guide
- group: company
  title: ''
  type: Blog
  url: https://www.rapidproxy.io/blog
coverage:
  checked: '2026-10-12'
  detail: Documentation is served via Gitbook with JavaScript-rendered pages, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://docs.rapidproxy.io/proxies/integration-guide
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) provides a large residential proxy network with over 70 million IP addresses, enabling scalable web scraping, data collection, and ad verification. The service offers rotating and static residential proxies across global locations, with flexible pricing and an affiliate program. RapidProxy targets developers and enterprises needing reliable, high‑volume proxy solutions while emphasizing privacy and compliance.
layout: provider
modified: '2026-10-12'
name: RapidProxy (RAPID TERMINAL UK NETWORK LIMITED)
nav: Providers
network: true
overview: 'RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) is listed with 1 API on the [APIs.io](https://apis.io/) network: RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) API. Tagged areas include Proxy, Residential, Web Scraping, and Data Collection.


  The RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) catalog on APIs.io includes 1 Spectral governance ruleset.


  RapidProxy (RAPID TERMINAL UK NETWORK LIMITED)''s developer surface includes pricing, getting-started guide, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Rapidproxy Plans Pricing
  plan_count: 3
  slug: rapidproxy-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: RapidProxy (RAPID TERMINAL UK NETWORK LIMITED) API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: rapidproxy-rules
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 9.9
    developer_ergonomics: 11.9
    discoverability: 60.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 31.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/rapidproxy/rapidproxy-2026-11-03T141932.png
security:
- kind: domain-security
  name: Rapidproxy Domain Security
  slug: rapidproxy-domain-security
  summary_line: TLSv1.3
slug: rapidproxy
tags:
- Proxy
- Residential
- Web Scraping
- Data Collection
website: https://www.rapidproxy.io/
---
