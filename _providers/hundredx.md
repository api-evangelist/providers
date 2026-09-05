---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Two HundredX-operated Model Context Protocol servers reachable on the public internet — "HX BigQuery MCP Server" 2.0.0 at hx-bigquery-mcp.hundredx.com and "Jupyter MCP Server" 2.0.0 at jupyter-mcp.hun
  name: HundredX MCP Servers
  slug: hundredx-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: Security
  url: security/hundredx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hundredx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hundredx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hundredx.com/
- group: company
  title: ''
  type: About
  url: https://hundredx.com/aboutus
- group: operate
  title: ''
  type: Support
  url: https://help.hundredx.com/
- group: start
  title: ''
  type: Login
  url: https://portal.hundredx.com/
- group: company
  title: ''
  type: Blog
  url: https://hundredx.com/news-and-insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hundredx.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hundredx.com/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hundredx-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hundredx-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/hundredx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hundredx-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hundredx-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hundredx-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hundredx-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hundredx-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hundredx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hundredx-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hundredx-llms.txt
created: '2026-08-22'
description: 'HundredX is a Dallas/Addison, Texas data and insights company founded in 2012 that measures customer experience at scale and links it to future business performance. Its "data for good" model collects double-blind, ethically sourced feedback through HundredX Causes programs — contributing funding to nonprofits for every qualifying response — and has accumulated tens of millions of pieces of first-party consumer feedback across 80+ industries covering roughly two-thirds of the US economy. The company packages that corpus as the HundredX GO Score (Growth Outlook), a leading indicator of revenue growth and market performance 6-12 months ahead, and licenses it to enterprises, institutional investors and AI platforms through a sales-led motion and partner alliances with Deloitte and Goldman Sachs. HundredX operates no public developer program: delivery is through a customer portal, negotiated data feeds and partner channels, and no API documentation, OpenAPI description or pricing
  is published.'
layout: provider
mcp_servers:
- description: ''
  name: HundredX MCP Servers
  slug: hundredx-mcp-servers
modified: '2026-08-22'
name: HundredX
nav: Providers
network: true
overview: 'HundredX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Experience, Consumer Insights, Market Research, Alternative Data, and Investment Research.


  HundredX''s developer surface includes support, engineering blog, authentication, and 18 more developer resources.'
plans:
- name: Hundredx Plans Pricing
  plan_count: 0
  slug: hundredx-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Hundredx Rate Limits
  slug: hundredx-rate-limits
scopes:
- name: Hundredx Scopes
  scope_count: 0
  slug: hundredx-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 20.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hundredx/refs/heads/main/screenshots/hundredx-2026-09-02T145756.png
security:
- kind: authentication
  name: Hundredx Authentication
  slug: hundredx-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Hundredx Domain Security
  slug: hundredx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hundredx Vulnerability Disclosure
  slug: hundredx-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hundredx
tags:
- Customer Experience
- Consumer Insights
- Market Research
- Alternative Data
- Investment Research
- Data Licensing
website: https://hundredx.com/
---
