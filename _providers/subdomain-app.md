---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Subdomain App Agentic Access
  operation_count: 1
  slug: subdomain-app-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Find the subdomains of a domain name.
  name: Subdomain API
  slug: subdomain-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/subdomain-app/agentic-access/subdomain-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/subdomain-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/subdomain-app/rate-limits/subdomain-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/subdomain-app-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/subdomain-app/rules/subdomain-app-rules.yml
  title: ''
  type: Spectral
  url: rules/subdomain-app-rules.yml
- group: design
  href: https://artifacts.apis.io/subdomain-app/errors/subdomain-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/subdomain-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/subdomain-app/conformance/subdomain-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/subdomain-app-conformance.yml
- group: other
  href: https://artifacts.apis.io/subdomain-app/hosts/subdomain-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/subdomain-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/subdomain-app/vendors/subdomain-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/subdomain-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://subdomain.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://subdomain.app/privacy
- group: auth
  href: https://artifacts.apis.io/subdomain-app/security/subdomain-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/subdomain-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://subdomain.app/
created: '2026-10-31'
description: Subdomain API provides a free, no‑signup JSON API that returns the subdomains associated with any given domain. Leveraging one of the largest publicly available subdomain indexes, the service enables developers and security researchers to automate discovery, enrich threat intelligence, and integrate subdomain enumeration into CI/CD pipelines. The API is publicly accessible via HTTPS GET requests and returns results in a simple JSON array, making it easy to consume in scripts and applications.
image: https://subdomain.app/favicon.svg
layout: provider
modified: '2026-10-31'
name: subdomain-app
nav: Providers
network: true
overview: 'subdomain-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Subdomain, Discovery, API, and Free.


  The subdomain-app catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Subdomain App Plans Pricing
  plan_count: 0
  slug: subdomain-app-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Subdomain App Rate Limits
  slug: subdomain-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: subdomain-app API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: subdomain-app-rules
scopes:
- name: Subdomain App Scopes
  scope_count: 0
  slug: subdomain-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.4
    catalog_earned_first_party: 0.0
    catalog_gap: 54.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 65.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Subdomain App Authentication
  slug: subdomain-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Subdomain App Domain Security
  slug: subdomain-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: subdomain-app
tags:
- Security
- Subdomain
- Discovery
- API
- Free
website: https://subdomain.app/
---
