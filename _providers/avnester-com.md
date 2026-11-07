---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Avnester Com Agentic Access
  operation_count: 1
  slug: avnester-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.avnester.com
  baseurl_source: declared
  description: The public API from AVnester — 1 operation(s) for public.
  name: AVnester Public API
  slug: avnester-com-public-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/avnester-com/agentic-access/avnester-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avnester-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/avnester-com/plans/avnester-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avnester-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/avnester-com/rules/avnester-com-rules.yml
  title: ''
  type: Spectral
  url: rules/avnester-com-rules.yml
- group: design
  href: https://artifacts.apis.io/avnester-com/vocabulary/avnester-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avnester-com-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://avnester.com/trust
- group: auth
  href: https://artifacts.apis.io/avnester-com/authentication/avnester-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avnester-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/avnester-com/conformance/avnester-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avnester-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avnester-com/llms/avnester-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avnester-com-llms.txt
- group: other
  href: https://artifacts.apis.io/avnester-com/a2a/avnester-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/avnester-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/avnester-com/well-known/avnester-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avnester-com-security.txt
- group: auth
  href: https://artifacts.apis.io/avnester-com/well-known/avnester-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avnester-com-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/avnester-com/well-known/avnester-com-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avnester-com-developers-security.txt
- group: auth
  href: https://artifacts.apis.io/avnester-com/well-known/avnester-com-auth-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avnester-com-auth-security.txt
- group: auth
  href: https://artifacts.apis.io/avnester-com/well-known/avnester-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avnester-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/avnester-com/well-known/avnester-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avnester-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/avnester-com/hosts/avnester-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avnester-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/avnester-com/vendors/avnester-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avnester-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://avnester.com/status
- group: auth
  title: ''
  type: Security
  url: https://avnester.com/legal/security
- group: start
  title: ''
  type: Login
  url: https://avnester.com/login/developer?mode=login&src=devsite-header
- group: docs
  title: ''
  type: APIReference
  url: https://developers.avnester.com/
- group: auth
  href: https://artifacts.apis.io/avnester-com/scopes/avnester-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/avnester-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/avnester-com/security/avnester-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avnester-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/avnester-com/security/avnester-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avnester-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/avnester-com/security/avnester-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avnester-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avnester.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://avnester.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avnester.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avnester.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://avnester.com/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://avnester.com/api/mcp
  - status: 401
    url: https://api.avnester.com/api/mcp
  - status: 401
    url: https://auth.avnester.com/api/mcp
  - status: 401
    url: https://mcp.avnester.com/api/mcp
  - status: 200
    url: https://avnester.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: AVnester is an Indian AI‑powered real‑estate platform that helps users find verified resale properties, explore new builder projects, compare localities, track price trends, and make confident buying decisions across Tamil Nadu. It offers property listings in over 600 cities, AI tools, calculators, and market intelligence to streamline the home‑buying process.
image: https://avnester.com/og-image.png
layout: provider
modified: '2026-11-02'
name: AVnester
nav: Providers
network: true
overview: 'AVnester publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Real Estate, Artificial Intelligence, Property Listings, India, and Marketplace.


  The AVnester catalog on APIs.io includes 1 Spectral governance ruleset.


  AVnester''s developer surface includes authentication, API reference, pricing, support, and 26 more developer resources.'
plans:
- name: Avnester Com Plans Pricing
  plan_count: 6
  slug: avnester-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Avnester Com Rate Limits
  slug: avnester-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: AVnester API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: avnester-com-rules
scopes:
- name: Avnester Com Scopes
  scope_count: 3
  slug: avnester-com-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 66.8
    catalog_earned_first_party: 24.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.9
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 45.9
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avnester Com Authentication
  slug: avnester-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Avnester Com Domain Security
  slug: avnester-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avnester Com Vulnerability Disclosure
  slug: avnester-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Avnester Com Trust Center
  slug: avnester-com-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 3
skills:
- name: compare-properties
  slug: avnester-com-compare-properties
- name: get-property-details
  slug: avnester-com-get-property-details
- name: search-properties
  slug: avnester-com-search-properties
slug: avnester-com
tags:
- Real Estate
- Artificial Intelligence
- Property Listings
- India
- Marketplace
website: https://avnester.com/
---
