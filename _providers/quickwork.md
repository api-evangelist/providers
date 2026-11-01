---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Quickwork Agentic Access
  operation_count: 28
  slug: quickwork-agentic-access
  summary_line: 28 operations · 16 acting · 2 human-in-the-loop
api_count: 24
apis:
- baseURL: https://automation.quickwork.co
  baseurl_source: declared
  description: The Embedded API from Quickwork — 27 operation(s) for embedded.
  name: Quickwork Embedded API
  slug: quickwork-embedded-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/quickwork/agentic-access/quickwork-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quickwork-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/quickwork/rate-limits/quickwork-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quickwork-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/quickwork/rules/quickwork-rules.yml
  title: ''
  type: Spectral
  url: rules/quickwork-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.quickwork.co/security
- group: auth
  href: https://artifacts.apis.io/quickwork/authentication/quickwork-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quickwork-authentication.yml
- group: design
  href: https://artifacts.apis.io/quickwork/errors/quickwork-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/quickwork-problem-types.yml
- group: design
  href: https://artifacts.apis.io/quickwork/conformance/quickwork-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quickwork-conformance.yml
- group: agent
  href: https://artifacts.apis.io/quickwork/llms/quickwork-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quickwork-llms.txt
- group: auth
  href: https://artifacts.apis.io/quickwork/well-known/quickwork-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quickwork-status-security.txt
- group: auth
  href: https://artifacts.apis.io/quickwork/well-known/quickwork-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quickwork-security.txt
- group: auth
  href: https://artifacts.apis.io/quickwork/well-known/quickwork-quickwork-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quickwork-quickwork-security.txt
- group: auth
  href: https://artifacts.apis.io/quickwork/well-known/quickwork-automation-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quickwork-automation-security.txt
- group: agent
  href: https://artifacts.apis.io/quickwork/well-known/quickwork-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quickwork-well-known.yml
- group: other
  href: https://artifacts.apis.io/quickwork/hosts/quickwork-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quickwork-hosts.yml
- group: other
  href: https://artifacts.apis.io/quickwork/vendors/quickwork-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quickwork-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.quickwork.co/
- group: auth
  title: ''
  type: Security
  url: https://www.quickwork.co/security
- group: auth
  href: https://artifacts.apis.io/quickwork/security/quickwork-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/quickwork-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/quickwork/security/quickwork-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/quickwork-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/quickwork/security/quickwork-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quickwork-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quickwork.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quickwork.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://automation.quickwork.co/
- group: company
  title: ''
  type: Blog
  url: https://blog.quickwork.co/
- group: operate
  title: ''
  type: Support
  url: https://support.quickwork.co/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quickwork.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quickwork.co/privacy-policy
created: '2026-10-21'
description: Quickwork is an API integration and workflow automation platform that enables enterprises to connect, automate, and orchestrate applications, APIs, data, events, and AI agents on a unified platform. It offers low‑latency, high‑concurrency processing, on‑premise deployment, and robust security, serving a wide range of use cases from data integration to AI‑driven workflows. The platform is recognized for high usability and performance, supporting real‑time mission‑critical workflows with sub‑15ms latency and zero‑downtime deployments.
layout: provider
modified: '2026-10-21'
name: Quickwork
nav: Providers
network: true
overview: 'Quickwork publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Embedded API. Tagged areas include Integration, Automation, Workflows, API Platform, and Enterprise.


  The Quickwork catalog on APIs.io includes 1 Spectral governance ruleset.


  Quickwork''s developer surface includes authentication, documentation, engineering blog, support, and 23 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 1
  name: Quickwork Rate Limits
  slug: quickwork-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Quickwork API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: quickwork-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 50.5
    catalog_earned_first_party: 8.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 47.1
    developer_ergonomics: 38.1
    discoverability: 67.9
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Quickwork Authentication
  slug: quickwork-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Quickwork Domain Security
  slug: quickwork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quickwork Vulnerability Disclosure
  slug: quickwork-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Quickwork Trust Center
  slug: quickwork-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: quickwork
tags:
- Integration
- Automation
- Workflows
- API Platform
- Enterprise
website: https://quickwork.co/
---
