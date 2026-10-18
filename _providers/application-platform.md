---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: API for MainPath platform providing low‑code development and deployment services.
  name: MainPath API
  slug: mainpath-api
- baseURL: https://api.mainpath.ai
  baseurl_source: declared
  description: The Doppelt.digital API API from doppelt.digital — 1 operation(s) for doppelt.digital api.
  name: doppelt.digital Doppelt.digital API
  slug: application-platform-doppelt-digital-api-api
- baseURL: https://api.mainpath.ai
  baseurl_source: declared
  description: The Install API from doppelt.digital — 1 operation(s) for install.
  name: doppelt.digital Install API
  slug: application-platform-install-api
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/plans/application-platform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/application-platform-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/rules/application-platform-rules.yml
  title: ''
  type: Spectral
  url: rules/application-platform-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/cli/application-platform-cli.yml
  title: ''
  type: CLI
  url: cli/application-platform-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/authentication/application-platform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/application-platform-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/conformance/application-platform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/application-platform-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/llms/application-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/application-platform-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/well-known/application-platform-login-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/application-platform-login-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/well-known/application-platform-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/application-platform-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/hosts/application-platform-hosts.yml
  title: ''
  type: Hosts
  url: hosts/application-platform-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/vendors/application-platform-vendors.yml
  title: ''
  type: Vendors
  url: vendors/application-platform-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mainpath.ai/en/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/application-platform/refs/heads/main/security/application-platform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/application-platform-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://application-platform.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mainpath.ai/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mainpath.ai/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.mainpath.ai/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mainpath.ai/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mainpath.ai/en/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.mainpath.ai/en/support
coverage:
  checked: '2026-10-16'
  detail: Documentation pages exist but no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 404
    url: https://api.mainpath.ai/openapi.json
  - status: 404
    url: https://api.application-platform.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Doppelt.digital is a product listed on the MainPath platform, offering a comprehensive low‑code development and deployment environment for building, hosting, and managing modern applications. It provides templates, CI/CD pipelines, cloud‑native infrastructure, and integrated monitoring, targeting small to medium teams seeking rapid project bootstrapping and scalable operations across Europe. The service emphasizes data privacy, European hosting, and a modular toolbox for developers and DevOps engineers.
image: https://www.mainpath.ai/img/og/mainpath.png
layout: provider
modified: '2026-10-15'
name: doppelt.digital
nav: Providers
network: true
overview: 'doppelt.digital is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Doppelt.digital API, Install API, and 1 more. Tagged areas include Low-code, Development Platform, Cloud Hosting, European SaaS, and Automation.


  The doppelt.digital catalog on APIs.io includes 1 Spectral governance ruleset.


  doppelt.digital''s developer surface includes CLI, authentication, changelog, documentation, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Application Platform Plans Pricing
  plan_count: 4
  slug: application-platform-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: doppelt.digital API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: application-platform-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 12.9
    developer_ergonomics: 35.7
    discoverability: 78.6
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Application Platform Authentication
  slug: application-platform-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Application Platform Domain Security
  slug: application-platform-domain-security
  summary_line: TLSv1.3
slug: application-platform
tags:
- Low-code
- Development Platform
- Cloud Hosting
- European SaaS
- Automation
website: https://application-platform.com/
---
