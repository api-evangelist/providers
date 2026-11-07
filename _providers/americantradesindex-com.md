---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: American Trades Index helps you find and win more business. Find the projects being built, the companies around them, and the markets where demand is growing.
  name: American Trades Index API
  slug: american-trades-index-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/americantradesindex-com/rules/americantradesindex-com-rules.yml
  title: ''
  type: Spectral
  url: rules/americantradesindex-com-rules.yml
- group: design
  href: https://artifacts.apis.io/americantradesindex-com/conformance/americantradesindex-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/americantradesindex-com-conformance.yml
- group: operate
  href: https://artifacts.apis.io/americantradesindex-com/rate-limits/americantradesindex-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/americantradesindex-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/americantradesindex-com/plans/americantradesindex-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/americantradesindex-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/americantradesindex-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://americantradesindex.com/trust
- group: design
  href: https://artifacts.apis.io/americantradesindex-com/errors/americantradesindex-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/americantradesindex-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/americantradesindex-com/llms/americantradesindex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/americantradesindex-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/americantradesindex-com/well-known/americantradesindex-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/americantradesindex-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/americantradesindex-com/hosts/americantradesindex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/americantradesindex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/americantradesindex-com/vendors/americantradesindex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/americantradesindex-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://americantradesindex.com/signin
- group: auth
  href: https://artifacts.apis.io/americantradesindex-com/security/americantradesindex-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/americantradesindex-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/americantradesindex-com/security/americantradesindex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/americantradesindex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://americantradesindex.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://americantradesindex.com/settings/connect
- group: docs
  title: ''
  type: APIReference
  url: https://api.americantradesindex.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://americantradesindex.com/onboarding
- group: commercial
  title: ''
  type: Pricing
  url: https://americantradesindex.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://americantradesindex.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://americantradesindex.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://americantradesindex.com/contact
created: '2026-11-01'
description: American Trades Index aggregates daily public construction permits, bids, and award data across the United States to provide sales professionals with actionable leads. By scanning city, county, state and federal records, the service delivers the 25 most relevant new projects in a user’s territory each week via email, including project details, dates, and contact information for contractors, bidders and awardees. A free 14‑day trial lets users explore the data before subscribing to the Pro plan at $199 per month.
image: https://americantradesindex.com/ati-icon.png
layout: provider
modified: '2026-11-01'
name: American Trades Index
nav: Providers
network: true
overview: 'American Trades Index publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Leads, Permits, Bids, and Awards.


  The American Trades Index catalog on APIs.io includes 1 Spectral governance ruleset.


  American Trades Index''s developer surface includes API reference, getting-started guide, pricing, support, and 18 more developer resources.'
plans:
- name: Americantradesindex Com Plans Pricing
  plan_count: 3
  slug: americantradesindex-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Americantradesindex Com Rate Limits
  slug: americantradesindex-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: American Trades Index API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 5
  slug: americantradesindex-com-rules
scopes:
- name: Americantradesindex Com Scopes
  scope_count: 0
  slug: americantradesindex-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 41.5
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Americantradesindex Com Authentication
  slug: americantradesindex-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Americantradesindex Com Domain Security
  slug: americantradesindex-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Americantradesindex Com Trust Center
  slug: americantradesindex-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: americantradesindex-com
tags:
- Construction
- Leads
- Permits
- Bids
- Awards
website: https://americantradesindex.com/
---
