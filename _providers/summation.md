---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 6
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/summation/refs/heads/main/rate-limits/summation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/summation-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.summation.com/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/summation/refs/heads/main/plans/summation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/summation-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.summation.com/resources/articles
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/summation/refs/heads/main/security/summation-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/summation-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/summation/refs/heads/main/security/summation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/summation-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/summation/refs/heads/main/security/summation-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/summation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.summation.com/security
- group: company
  title: ''
  type: Website
  url: https://www.summation.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.summation.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.summation.com/
- group: start
  title: ''
  type: Login
  url: https://app.summation.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.summation.com/try-summation
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.summation.com/legals/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.summation.com/legals/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/summation-hq/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/_summation
- group: company
  title: ''
  type: Careers
  url: https://www.summation.com/careers
created: '2026-07-17'
description: Summation is an enterprise AI analyst platform that automates recurring business work — financial reviews, forecasts, models, and executive-ready decks — by connecting to a company's data sources (ERPs, data warehouses, and spreadsheets) and producing verified, source-traced reports in the format teams already use. Its AI agent "Addison" runs playbooks across finance, operations, and sales, tracing every number back to its source so outputs are audit-ready and SOC 2 Type II compliant. Founded by Ian Wong (CEO) and Ramachandran "RC" Ramarathinam (CTO), formerly of Opendoor, Summation is backed by Battery Ventures. The company operates a customer application, product documentation, and a public Trust Center, but does not currently publish a public developer API surface.
image: https://www.summation.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.summation.com over HTTP.
  name: Summation MCP Server
  slug: summation
modified: '2026-10-06'
name: Summation
nav: Providers
network: true
overview: 'Summation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Analytics, and Finance.


  Summation''s developer surface includes pricing, engineering blog, documentation, signup flow, and 14 more developer resources.'
plans:
- name: Summation Plans Pricing
  plan_count: 4
  slug: summation-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Summation Rate Limits
  slug: summation-rate-limits
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.0
  facets:
    access_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 51.7
    operational_transparency: 10.5
  previous_composite: 19.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/summation/refs/heads/main/screenshots/summation-2026-09-02T161323.png
security:
- kind: domain-security
  name: Summation Domain Security
  slug: summation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Summation Vulnerability Disclosure
  slug: summation-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Summation Trust Center
  slug: summation-trust-center
  summary_line: SOC 2, ISO 27001
slug: summation
tags:
- Company
- Artificial Intelligence
- AI Agents
- Analytics
- Finance
- Business Intelligence
- Data
- Enterprise Software
- Reporting
website: https://www.summation.com/
---
