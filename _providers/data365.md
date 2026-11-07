---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 8.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/data365/rate-limits/data365-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/data365-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/data365/plans/data365-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/data365-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/data365/authentication/data365-authentication.yml
  title: ''
  type: Authentication
  url: authentication/data365-authentication.yml
- group: agent
  href: https://artifacts.apis.io/data365/llms/data365-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/data365-llms.txt
- group: other
  href: https://artifacts.apis.io/data365/hosts/data365-hosts.yml
  title: ''
  type: Hosts
  url: hosts/data365-hosts.yml
- group: other
  href: https://artifacts.apis.io/data365/vendors/data365-vendors.yml
  title: ''
  type: Vendors
  url: vendors/data365-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data365.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://data365.co/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://data365.co/guides/callback-guide
- group: auth
  href: https://artifacts.apis.io/data365/security/data365-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/data365-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data365.co
- group: company
  title: ''
  type: Blog
  url: https://data365.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://data365.co/pricing
- group: operate
  title: ''
  type: Support
  url: https://data365.co/contact
coverage:
  checked: '2026-11-04'
  detail: Provider homepage returns HTML for typical spec URLs and no machine‑readable OpenAPI document was found.
  evidence:
  - status: 200
    url: https://data365.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Data365 provides real-time social media search APIs, delivering reliable data from major platforms such as Twitter, Facebook, Instagram, and TikTok. Developers can integrate these APIs to monitor trends, sentiment, and public conversations, enabling data-driven insights for marketing, research, and analytics applications.
image: https://cdn.prod.website-files.com/64d9f528c6b6445ddaf33590/684977ca7dd80bcd4c51a6cf_Opengraph.webp
layout: provider
modified: '2026-11-04'
name: Data365
nav: Providers
network: true
overview: 'Data365 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Media, Real-Time Data, and Developers.


  Data365''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Data365 Plans Pricing
  plan_count: 3
  slug: data365-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Data365 Rate Limits
  slug: data365-rate-limits
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 42.0
    catalog_earned_first_party: 20.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 39.3
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Data365 Authentication
  slug: data365-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Data365 Domain Security
  slug: data365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: data365
tags:
- Company
- Social Media
- Real-Time Data
- Developers
website: https://data365.co
---
