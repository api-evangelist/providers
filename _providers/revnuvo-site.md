---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Revnuvo Site Agentic Access
  operation_count: 2
  slug: revnuvo-site-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://dns.revnuvo.site
  baseurl_source: declared
  description: The Domain API from revnuvo-site — 2 operation(s) for domain.
  name: revnuvo-site Domain API
  slug: revnuvo-site-domain-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/revnuvo-site/agentic-access/revnuvo-site-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/revnuvo-site-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/revnuvo-site/rules/revnuvo-site-rules.yml
  title: ''
  type: Spectral
  url: rules/revnuvo-site-rules.yml
- group: design
  href: https://artifacts.apis.io/revnuvo-site/errors/revnuvo-site-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/revnuvo-site-problem-types.yml
- group: design
  href: https://artifacts.apis.io/revnuvo-site/conformance/revnuvo-site-conformance.yml
  title: ''
  type: Conformance
  url: conformance/revnuvo-site-conformance.yml
- group: agent
  href: https://artifacts.apis.io/revnuvo-site/llms/revnuvo-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/revnuvo-site-llms.txt
- group: other
  href: https://artifacts.apis.io/revnuvo-site/hosts/revnuvo-site-hosts.yml
  title: ''
  type: Hosts
  url: hosts/revnuvo-site-hosts.yml
- group: other
  href: https://artifacts.apis.io/revnuvo-site/vendors/revnuvo-site-vendors.yml
  title: ''
  type: Vendors
  url: vendors/revnuvo-site-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://revnuvo.site/products/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://revnuvo.site/terms/
- group: auth
  title: ''
  type: Security
  url: https://revnuvo.site/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://revnuvo.site/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://revnuvo.site/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.revnuvo.site/login
- group: company
  title: ''
  type: Blog
  url: https://revnuvo.site/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.revnuvo.site/
- group: auth
  href: https://artifacts.apis.io/revnuvo-site/security/revnuvo-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/revnuvo-site-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://revnuvo.site/
created: '2026-10-30'
description: Revnuvo provides a modern platform for managing revenue operations, offering tools for subscription billing, invoicing, and financial analytics. The company focuses on simplifying complex revenue workflows for SaaS businesses, integrating with popular payment gateways and ERP systems. Their solution aims to improve cash flow visibility and automate recurring revenue processes, supporting growth and compliance for enterprises.
layout: provider
modified: '2026-10-30'
name: revnuvo-site
nav: Providers
network: true
overview: 'revnuvo-site publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Domain API. Tagged areas include Company, Revenue, Software-as-a-Service, Billing, and Finance.


  The revnuvo-site catalog on APIs.io includes 1 Spectral governance ruleset.


  revnuvo-site''s developer surface includes pricing, engineering blog, documentation, and 14 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: revnuvo-site API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: revnuvo-site-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 39.8
    developer_ergonomics: 6.0
    discoverability: 69.6
    operational_transparency: 5.3
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/revnuvo-site/revnuvo-site-2026-11-03T142237.png
security:
- kind: domain-security
  name: Revnuvo Site Domain Security
  slug: revnuvo-site-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: revnuvo-site
tags:
- Company
- Revenue
- Software-as-a-Service
- Billing
- Finance
website: https://revnuvo.site/
---
