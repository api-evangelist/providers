---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Affiliatespy Io Agentic Access
  operation_count: 2
  slug: affiliatespy-io-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: AffiliateSpy REST API mirroring the MCP surface
  name: AffiliateSpy API
  slug: affiliatespy-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/affiliatespy-io/agentic-access/affiliatespy-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/affiliatespy-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/affiliatespy-io/plans/affiliatespy-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affiliatespy-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/affiliatespy-io/rules/affiliatespy-io-rules.yml
  title: ''
  type: Spectral
  url: rules/affiliatespy-io-rules.yml
- group: design
  href: https://artifacts.apis.io/affiliatespy-io/vocabulary/affiliatespy-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/affiliatespy-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/affiliatespy-io/errors/affiliatespy-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/affiliatespy-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/affiliatespy-io/conformance/affiliatespy-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affiliatespy-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/affiliatespy-io/well-known/affiliatespy-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/affiliatespy-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/affiliatespy-io/hosts/affiliatespy-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/affiliatespy-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/affiliatespy-io/vendors/affiliatespy-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/affiliatespy-io-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.affiliatespy.io/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/affiliatespy-io/authentication/affiliatespy-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/affiliatespy-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/affiliatespy-io/security/affiliatespy-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affiliatespy-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://affiliatespy.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.affiliatespy.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.affiliatespy.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.affiliatespy.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.affiliatespy.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.affiliatespy.io/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://affiliatespy.io/openapi.json
  - status: null
    url: https://www.affiliatespy.io/openapi.json
  - status: 401
    url: https://www.affiliatespy.io/api/mcp
  - status: 200
    url: https://affiliatespy.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: AffiliateSpy is an affiliate marketing intelligence platform that reveals which creators and sites promote competitor mobile apps. It provides verified contact details, AI‑driven outreach, and receipt data to help businesses recruit affiliates and monitor competitor promotions. The tool aggregates affiliate activity, offers insights into payouts, and enables targeted partnership strategies.
layout: provider
modified: '2026-10-31'
name: AffiliateSpy
nav: Providers
network: true
overview: 'AffiliateSpy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Affiliate Marketing, Intelligence, Artificial Intelligence, and Software-as-a-Service.


  The AffiliateSpy catalog on APIs.io includes 1 Spectral governance ruleset.


  AffiliateSpy''s developer surface includes API reference, authentication, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Affiliatespy Io Plans Pricing
  plan_count: 3
  slug: affiliatespy-io-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AffiliateSpy API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: affiliatespy-io-rules
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Affiliatespy Io Authentication
  slug: affiliatespy-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Affiliatespy Io Domain Security
  slug: affiliatespy-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: affiliatespy-io
tags:
- Company
- Affiliate Marketing
- Intelligence
- Artificial Intelligence
- Software-as-a-Service
website: https://affiliatespy.io/
---
