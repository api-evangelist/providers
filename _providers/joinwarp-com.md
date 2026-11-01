---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/joinwarp-com/rate-limits/joinwarp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/joinwarp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/joinwarp-com/plans/joinwarp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/joinwarp-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.warp.co/security
- group: auth
  href: https://artifacts.apis.io/joinwarp-com/authentication/joinwarp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/joinwarp-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/joinwarp-com/llms/joinwarp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/joinwarp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/joinwarp-com/a2a/joinwarp-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/joinwarp-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/joinwarp-com/well-known/joinwarp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/joinwarp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/joinwarp-com/hosts/joinwarp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joinwarp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joinwarp-com/vendors/joinwarp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joinwarp-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/joinwarp-com/packages/joinwarp-com-packages.yml
  title: ''
  type: SDKs
  url: packages/joinwarp-com-packages.yml
- group: build
  href: https://artifacts.apis.io/joinwarp-com/packages/joinwarp-com-packages.yml
  title: ''
  type: Packages
  url: packages/joinwarp-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.warp.co/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://www.warp.co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.warp.co/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.warp.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.warp.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.warp.co/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://help.joinwarp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.warp.co
- group: auth
  href: https://artifacts.apis.io/joinwarp-com/security/joinwarp-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/joinwarp-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/joinwarp-com/security/joinwarp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joinwarp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.joinwarp.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://help.joinwarp.com/mcp
  - status: 200
    url: https://www.joinwarp.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Warp provides AI‑native payroll, tax compliance, benefits administration, and IT management tools for finance and HR teams at high‑growth companies. The platform automates onboarding, payroll processing, tax registrations, filings and notices across all 50 U.S. states and supports global contractor payments in 150+ countries. It integrates with existing ERP, CRM and finance stacks via native connectors and a public API.
image: https://www.warp.co/og/open-graph.png
layout: provider
modified: '2026-10-25'
name: Warp
nav: Providers
network: true
overview: 'Warp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payroll, Benefits, Tax Compliance, IT Management, and Global Payroll.


  Warp''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 16 more developer resources.'
plans:
- name: Joinwarp Com Plans Pricing
  plan_count: 6
  slug: joinwarp-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Joinwarp Com Rate Limits
  slug: joinwarp-com-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 47.0
    catalog_earned_first_party: 20.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Joinwarp Com Authentication
  slug: joinwarp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Joinwarp Com Domain Security
  slug: joinwarp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Joinwarp Com Trust Center
  slug: joinwarp-com-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: joinwarp-com
tags:
- Payroll
- Benefits
- Tax Compliance
- IT Management
- Global Payroll
- HRIS
- AI Agents
website: https://www.joinwarp.com
---
