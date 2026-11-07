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
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP connector allows AI assistants to interact with Traceable Docs data via a remote server.
  name: Traceable Docs MCP
  slug: traceable-docs-mcp
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/traceabledocs-com/rate-limits/traceabledocs-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/traceabledocs-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/traceabledocs-com/plans/traceabledocs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/traceabledocs-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/traceabledocs-com/conventions/traceabledocs-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/traceabledocs-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/traceabledocs-com/conventions/traceabledocs-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/traceabledocs-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://traceabledocs.com/security
- group: auth
  href: https://artifacts.apis.io/traceabledocs-com/authentication/traceabledocs-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/traceabledocs-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/traceabledocs-com/scopes/traceabledocs-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/traceabledocs-com-scopes.yml
- group: agent
  href: https://artifacts.apis.io/traceabledocs-com/llms/traceabledocs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/traceabledocs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/traceabledocs-com/well-known/traceabledocs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/traceabledocs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/traceabledocs-com/hosts/traceabledocs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/traceabledocs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/traceabledocs-com/vendors/traceabledocs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/traceabledocs-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://traceabledocs.com/security
- group: start
  title: ''
  type: GettingStarted
  url: https://traceabledocs.com//get-started
- group: start
  title: ''
  type: SignUp
  url: https://app.traceabledocs.com/signup
- group: auth
  href: https://artifacts.apis.io/traceabledocs-com/security/traceabledocs-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/traceabledocs-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/traceabledocs-com/security/traceabledocs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/traceabledocs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/traceabledocs-com/security/traceabledocs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/traceabledocs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://traceabledocs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://traceabledocs.com/docs
- group: company
  title: ''
  type: Blog
  url: https://traceabledocs.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://traceabledocs.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://traceabledocs.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://traceabledocs.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.traceabledocs.com/legal/privacy
coverage:
  checked: '2026-10-31'
  detail: MCP endpoint requires authentication via login, redirecting spec URLs to a sign‑in page.
  evidence:
  - status: 307
    url: https://app.traceabledocs.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Traceable Docs provides a cloud-based requirements management and document control platform for regulated product teams. It offers live traceability, e‑signatures, audit‑ready evidence, and an AI‑powered connector (MCP) that lets large language models interact with project data. The solution supports compliance with standards such as ISO 13485, IEC 62304, and 21 CFR Part 11, helping companies streamline design control, risk management, and regulatory documentation.
image: https://traceabledocs.com/og-home.png
layout: provider
modified: '2026-10-31'
name: traceabledocs-com
nav: Providers
network: true
overview: 'traceabledocs-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Requirements Management, Document Control, Regulatory Compliance, and AI Integration.


  traceabledocs-com''s developer surface includes authentication, getting-started guide, signup flow, documentation, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Traceabledocs Com Plans Pricing
  plan_count: 5
  slug: traceabledocs-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Traceabledocs Com Rate Limits
  slug: traceabledocs-com-rate-limits
scopes:
- name: Traceabledocs Com Scopes
  scope_count: 2
  slug: traceabledocs-com-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 41.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/traceabledocs-com/traceabledocs-com-2026-11-03T144937.png
security:
- kind: authentication
  name: Traceabledocs Com Authentication
  slug: traceabledocs-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Traceabledocs Com Domain Security
  slug: traceabledocs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Traceabledocs Com Vulnerability Disclosure
  slug: traceabledocs-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Traceabledocs Com Trust Center
  slug: traceabledocs-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: traceabledocs-com
tags:
- Company
- Requirements Management
- Document Control
- Regulatory Compliance
- AI Integration
website: https://traceabledocs.com/
---
