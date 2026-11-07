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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.ipwho.org
  baseurl_source: declared
  description: 'IPWho.org API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: IPWho.org API
  slug: ipwho-org-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/ipwho-org/rate-limits/ipwho-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ipwho-org-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ipwho-org/plans/ipwho-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ipwho-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ipwho-org/rules/ipwho-org-rules.yml
  title: ''
  type: Spectral
  url: rules/ipwho-org-rules.yml
- group: design
  href: https://artifacts.apis.io/ipwho-org/vocabulary/ipwho-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ipwho-org-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/ipwho-org/authentication/ipwho-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ipwho-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/ipwho-org/conformance/ipwho-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ipwho-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ipwho-org/llms/ipwho-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ipwho-org-llms.txt
- group: other
  href: https://artifacts.apis.io/ipwho-org/hosts/ipwho-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ipwho-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/ipwho-org/vendors/ipwho-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ipwho-org-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.ipwho.org/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/ipwho-org/security/ipwho-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ipwho-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ipwho.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.ipwho.org/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ipwho.org/docs/gettingstarted/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ipwho.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.ipwho.org/signup
- group: operate
  title: ''
  type: Contact
  url: https://www.ipwho.org/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lavrox.com/legal/privacy-policy
coverage:
  checked: '2026-10-22'
  detail: Documentation pages return HTML shells and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 404
    url: https://www.ipwho.org/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: IPWho.org provides a fast, accurate, developer‑friendly IP geolocation REST API hosted at api.ipwho.org. It offers single‑IP lookup, bulk lookup, and a self‑lookup (/me) endpoint, returning detailed data on location, timezone, currency, flag, connection, security and user‑agent. The service runs on the independent Lavrox network, delivering low latency and high uptime, with a generous free tier and paid plans. Documentation, pricing, and SDKs for TypeScript, PHP and Python are available.
image: https://www.ipwho.org/og-image.png
layout: provider
modified: '2026-10-22'
name: IPWho.org
nav: Providers
network: true
overview: 'IPWho.org is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IP Geolocation, and Free Tier.


  The IPWho.org catalog on APIs.io includes 1 Spectral governance ruleset.


  IPWho.org''s developer surface includes authentication, API reference, documentation, getting-started guide, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Ipwho Org Plans Pricing
  plan_count: 4
  slug: ipwho-org-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Ipwho Org Rate Limits
  slug: ipwho-org-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: IPWho.org API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ipwho-org-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.8
    catalog_earned_first_party: 24.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 11.4
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 31.6
  previous_composite: 38.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ipwho-org/ipwho-org-2026-11-03T134029.png
security:
- kind: authentication
  name: Ipwho Org Authentication
  slug: ipwho-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ipwho Org Domain Security
  slug: ipwho-org-domain-security
  summary_line: TLSv1.3
slug: ipwho-org
tags:
- Company
- IP Geolocation
- Free Tier
website: https://www.ipwho.org
---
