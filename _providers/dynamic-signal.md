---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Employee communication platform API (details not publicly documented)
  name: Dynamic Signal API
  slug: dynamic-signal-api-2
- description: 'Dynamic Signal API as documented publicly: 94 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Dynamic Signal API
  slug: dynamic-signal-api
artifact_total: 8
asyncapis:
- description: ''
  name: Dynamic Signal Webhooks
  slug: dynamic-signal-webhooks
common:
- group: design
  href: https://artifacts.apis.io/dynamic-signal/rules/dynamic-signal-rules.yml
  title: ''
  type: Spectral
  url: rules/dynamic-signal-rules.yml
- group: design
  href: https://artifacts.apis.io/dynamic-signal/vocabulary/dynamic-signal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dynamic-signal-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dynamic-signal/asyncapi/dynamic-signal-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dynamic-signal-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/dynamic-signal/changelog/dynamic-signal-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dynamic-signal-changelog.yml
- group: design
  href: https://artifacts.apis.io/dynamic-signal/conventions/dynamic-signal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dynamic-signal-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://firstup.io/legal/information-security-guidelines/
- group: auth
  href: https://artifacts.apis.io/dynamic-signal/authentication/dynamic-signal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynamic-signal-authentication.yml
- group: design
  href: https://artifacts.apis.io/dynamic-signal/conformance/dynamic-signal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dynamic-signal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dynamic-signal/llms/dynamic-signal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dynamic-signal-llms.txt
- group: other
  href: https://artifacts.apis.io/dynamic-signal/a2a/dynamic-signal-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dynamic-signal-a2a.yml
- group: auth
  href: https://artifacts.apis.io/dynamic-signal/well-known/dynamic-signal-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dynamic-signal-status-security.txt
- group: auth
  href: https://artifacts.apis.io/dynamic-signal/well-known/dynamic-signal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dynamic-signal-security.txt
- group: auth
  href: https://artifacts.apis.io/dynamic-signal/well-known/dynamic-signal-library-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dynamic-signal-library-security.txt
- group: agent
  href: https://artifacts.apis.io/dynamic-signal/well-known/dynamic-signal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dynamic-signal-well-known.yml
- group: other
  href: https://artifacts.apis.io/dynamic-signal/hosts/dynamic-signal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynamic-signal-hosts.yml
- group: other
  href: https://artifacts.apis.io/dynamic-signal/vendors/dynamic-signal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynamic-signal-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firstup.io/legal/terms-of-service-2020/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.firstup.io/
- group: auth
  title: ''
  type: Security
  url: https://firstup.io/company/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firstup.io/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://firstup.io/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://firstup.io/company/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.firstup.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.firstup.io/versionchange/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.firstup.io/endpoints/openapi
- group: auth
  href: https://artifacts.apis.io/dynamic-signal/security/dynamic-signal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dynamic-signal-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dynamic-signal/security/dynamic-signal-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dynamic-signal-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dynamic-signal/security/dynamic-signal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamic-signal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://firstup.io
- group: docs
  title: ''
  type: Documentation
  url: https://firstup.io/platform/integrations-apis/
- group: company
  title: ''
  type: Blog
  url: https://firstup.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://firstup.io/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.firstup.io/hc/en-us
- group: other
  title: ''
  type: Company
  url: https://firstup.io/company/
coverage:
  checked: '2026-10-24'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://firstup.io/platform/integrations-apis/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Dynamic Signal, now operating as Firstup, provides an intelligent employee communication platform that helps enterprises deliver personalized messages across the employee journey. The solution supports onboarding, promotions, life events, performance reviews, and global mobility, aiming to improve engagement, reduce attrition, and drive business outcomes through targeted communications and actionable insights.
image: https://firstup.io/og-image.jpg
layout: provider
modified: '2026-10-24'
name: Dynamic Signal
nav: Providers
network: true
overview: 'Dynamic Signal is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Communication, Enterprise Software, SaaS, and HR Tech.


  The Dynamic Signal catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Dynamic Signal''s developer surface includes changelog, authentication, API reference, documentation, engineering blog, pricing, support, and 27 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Dynamic Signal API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: dynamic-signal-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 18.4
    developer_ergonomics: 45.2
    discoverability: 60.7
    operational_transparency: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 15
      marker_coverage: 100.0
      total: 15
    mcp: unknown
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
  name: Dynamic Signal Authentication
  slug: dynamic-signal-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Dynamic Signal Domain Security
  slug: dynamic-signal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dynamic Signal Vulnerability Disclosure
  slug: dynamic-signal-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dynamic Signal Trust Center
  slug: dynamic-signal-trust-center
  summary_line: SOC 2, ISO 27001
slug: dynamic-signal
tags:
- Company
- Employee Communication
- Enterprise Software
- SaaS
- HR Tech
website: https://firstup.io
---
