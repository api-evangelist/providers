---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Patchmon Agentic Access
  operation_count: 1
  slug: patchmon-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.patchmon.net/api/v1
  baseurl_source: declared
  description: Endpoints using scoped credentials (Basic Auth, integration_type api)
  name: PatchMon Scoped API - Hosts API
  slug: patchmon-scoped-api-hosts-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/patchmon/agentic-access/patchmon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/patchmon-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/patchmon/rate-limits/patchmon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/patchmon-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/patchmon/plans/patchmon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/patchmon-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/patchmon/rules/patchmon-rules.yml
  title: ''
  type: Spectral
  url: rules/patchmon-rules.yml
- group: design
  href: https://artifacts.apis.io/patchmon/vocabulary/patchmon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/patchmon-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.patchmon.net/
- group: auth
  href: https://artifacts.apis.io/patchmon/authentication/patchmon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/patchmon-authentication.yml
- group: design
  href: https://artifacts.apis.io/patchmon/errors/patchmon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/patchmon-problem-types.yml
- group: design
  href: https://artifacts.apis.io/patchmon/conformance/patchmon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/patchmon-conformance.yml
- group: other
  href: https://artifacts.apis.io/patchmon/overlays/patchmon-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/patchmon-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/patchmon/well-known/patchmon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/patchmon-security.txt
- group: agent
  href: https://artifacts.apis.io/patchmon/well-known/patchmon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/patchmon-well-known.yml
- group: other
  href: https://artifacts.apis.io/patchmon/hosts/patchmon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/patchmon-hosts.yml
- group: other
  href: https://artifacts.apis.io/patchmon/vendors/patchmon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/patchmon-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://patchmon.net/integrations/webhooks
- group: auth
  title: ''
  type: Security
  url: https://patchmon.net/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.patchmon.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://patchmon.net/docs/patchmon-operator-guide/first-time-admin-setup
- group: auth
  href: https://artifacts.apis.io/patchmon/security/patchmon-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/patchmon-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/patchmon/security/patchmon-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/patchmon-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/patchmon/security/patchmon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/patchmon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://patchmon.net/
- group: docs
  title: ''
  type: Documentation
  url: https://patchmon.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://patchmon.net/docs/api-reference
- group: company
  title: ''
  type: Blog
  url: https://patchmon.net/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/patchmon
- group: commercial
  title: ''
  type: Pricing
  url: https://patchmon.net/pricing
- group: start
  title: ''
  type: Login
  url: https://patchmon.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://patchmon.net/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://patchmon.net/legal/privacy-policy
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.patchmon.net/roadmap
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/patchmon
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://feedback.patchmon.net/api/mcp
  - status: 401
    url: https://portal.patchmon.net/mcp
  - status: 200
    url: https://patchmon.net/
  reason: partner-login
  state: gated
created: '2026-10-28'
description: PatchMon provides a patch management platform for Linux, FreeBSD, and Windows servers. It offers a web dashboard, REST API, and integrations to automate update deployment, compliance reporting, and audit trails. Available as a cloud service or self‑hosted open‑source edition under AGPL‑v3.
image: https://patchmon.net/assets/logo_square_default.svg
layout: provider
modified: '2026-10-28'
name: PatchMon
nav: Providers
network: true
overview: 'PatchMon publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Scoped API - Hosts API. Tagged areas include Company, Patch Management, Linux, FreeBSD, and Windows.


  The PatchMon catalog on APIs.io includes 1 Spectral governance ruleset.


  PatchMon''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Patchmon Plans Pricing
  plan_count: 3
  slug: patchmon-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Patchmon Rate Limits
  slug: patchmon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: PatchMon API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: patchmon-rules
scopes:
- name: Patchmon Scopes
  scope_count: 0
  slug: patchmon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 46.5
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Patchmon Authentication
  slug: patchmon-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Patchmon Domain Security
  slug: patchmon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Patchmon Vulnerability Disclosure
  slug: patchmon-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Patchmon Trust Center
  slug: patchmon-trust-center
  summary_line: ISO 27001
slug: patchmon
tags:
- Company
- Patch Management
- Linux
- FreeBSD
- Windows
- Open Source
website: https://patchmon.net/
---
