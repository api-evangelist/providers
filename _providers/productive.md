---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Productive platform providing agency management and professional services automation.
  name: Productive API
  slug: productive-api
artifact_total: 6
asyncapis:
- description: ''
  name: Productive Webhooks
  slug: productive-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/rate-limits/productive-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/productive-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/plans/productive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/productive-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/asyncapi/productive-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/productive-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/conventions/productive-conventions.yml
  title: ''
  type: Conventions
  url: conventions/productive-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/sandbox/productive-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/productive-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://productive.io/trust/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/conformance/productive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/productive-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/llms/productive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/productive-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/well-known/productive-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/productive-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/well-known/productive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/productive-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/hosts/productive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/productive-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/vendors/productive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/productive-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.productive.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://productive.io/trust/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.productive.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://productive.io/whats-new/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.productive.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.productive.io/en/articles/2179614-quickbooks-integration-setup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/security/productive-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/productive-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/productive/refs/heads/main/security/productive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/productive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://productive.io
- group: docs
  title: ''
  type: Documentation
  url: https://productive.io/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://productive.io/pricing/
- group: operate
  title: ''
  type: Roadmap
  url: https://productive.io/roadmap/
- group: company
  title: ''
  type: Blog
  url: https://productive.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.productive.io/en/
created: '2026-10-14'
description: Productive provides an integrated agency management and professional services automation platform. It offers resource planning, time tracking, project management, billing, forecasting, and AI-powered tools to help agencies and consulting firms run projects, manage budgets, and collaborate across teams. The solution combines CRM, financials, and workflow automation in a single SaaS product, delivering real-time insights and customizable reporting for improved profitability and client satisfaction.
image: https://website-assets.productive.io/wf/69273e1d1bd1fcfcff2fe0d4/69724044686ecf3c6b20e7c1_og-productive-product-2.png
layout: provider
modified: '2026-10-14'
name: Productive
nav: Providers
network: true
overview: 'Productive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agency Management, Professional Services Automation, Software-as-a-Service, and Resource Planning.


  The Productive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Productive''s developer surface includes sandbox, changelog, API reference, getting-started guide, documentation, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Productive Plans Pricing
  plan_count: 3
  slug: productive-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Productive Rate Limits
  slug: productive-rate-limits
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 52.4
    discoverability: 73.2
    operational_transparency: 76.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Productive Domain Security
  slug: productive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Productive Trust Center
  slug: productive-trust-center
  summary_line: GDPR
slug: productive
tags:
- Company
- Agency Management
- Professional Services Automation
- Software-as-a-Service
- Resource Planning
website: https://productive.io
---
