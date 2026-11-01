---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Lifx Agentic Access
  operation_count: 19
  slug: lifx-agentic-access
  summary_line: 19 operations · 16 acting
api_count: 1
apis:
- baseURL: https://api.lifx.com/v1
  baseurl_source: declared
  description: The Color API from LIFX — 1 operation(s) for color.
  name: LIFX Color API
  slug: lifx-color-api
- baseURL: https://api.lifx.com/v1
  baseurl_source: declared
  description: The Lights API from LIFX — 16 operation(s) for lights.
  name: LIFX Lights API
  slug: lifx-lights-api
- baseURL: https://api.lifx.com/v1
  baseurl_source: declared
  description: The Scenes API from LIFX — 2 operation(s) for scenes.
  name: LIFX Scenes API
  slug: lifx-scenes-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/lifx/well-known/lifx-lifx-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lifx-lifx-security.txt
- group: agent
  href: https://artifacts.apis.io/lifx/agentic-access/lifx-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lifx-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/lifx/rate-limits/lifx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lifx-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/lifx/rules/lifx-rules.yml
  title: ''
  type: Spectral
  url: rules/lifx-rules.yml
- group: agent
  href: https://artifacts.apis.io/lifx/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lifx.com/pages/privacy-security-responsible-disclosure-of-security-vulnerabilities
- group: auth
  href: https://artifacts.apis.io/lifx/authentication/lifx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lifx-authentication.yml
- group: design
  href: https://artifacts.apis.io/lifx/errors/lifx-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lifx-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lifx/conformance/lifx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lifx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lifx/llms/lifx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lifx-llms.txt
- group: auth
  href: https://artifacts.apis.io/lifx/well-known/lifx-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lifx-www-security.txt
- group: auth
  href: https://artifacts.apis.io/lifx/well-known/lifx-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lifx-status-security.txt
- group: auth
  href: https://artifacts.apis.io/lifx/well-known/lifx-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lifx-security.txt
- group: auth
  href: https://artifacts.apis.io/lifx/well-known/lifx-security-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lifx-security-security.txt
- group: auth
  href: https://artifacts.apis.io/lifx/well-known/lifx-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lifx-app-security.txt
- group: agent
  href: https://artifacts.apis.io/lifx/well-known/lifx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lifx-well-known.yml
- group: other
  href: https://artifacts.apis.io/lifx/hosts/lifx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lifx-hosts.yml
- group: other
  href: https://artifacts.apis.io/lifx/vendors/lifx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lifx-vendors.yml
- group: build
  href: https://artifacts.apis.io/lifx/packages/lifx-packages.yml
  title: ''
  type: SDKs
  url: packages/lifx-packages.yml
- group: build
  href: https://artifacts.apis.io/lifx/packages/lifx-packages.yml
  title: ''
  type: Packages
  url: packages/lifx-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lifx.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.lifx.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lifx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lifx.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.lifx.com/pages/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LIFX
- group: auth
  href: https://artifacts.apis.io/lifx/security/lifx-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lifx-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lifx/security/lifx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lifx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lifx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.developer.lifx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.developer.lifx.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://api.developer.lifx.com/reference/introduction.md
created: '2026-10-28'
description: LIFX designs and manufactures smart lighting products that can be controlled via Wi‑Fi without a hub. Their platform includes an HTTP Remote Control API for developers to integrate lighting control into applications, automations, and services. The API provides endpoints for listing lights, setting states, applying effects, and managing scenes, with authentication, rate‑limit, and error handling documentation.
image: http://www.lifx.com/cdn/shop/files/LIFX_BrandImage_T1-logo.jpg?v=1773807872
layout: provider
modified: '2026-10-28'
name: LIFX
nav: Providers
network: true
overview: 'LIFX publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Color API, Lights API, and Scenes API. Tagged areas include Smart Lighting, Wi‑Fi Bulbs, Home Automation, and Lighting Fixtures.


  The LIFX catalog on APIs.io includes 1 Spectral governance ruleset.


  LIFX''s developer surface includes authentication, support, documentation, API reference, and 28 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 1
  name: Lifx Rate Limits
  slug: lifx-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: LIFX API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: lifx-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.5
    catalog_earned_first_party: 8.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 47.3
    developer_ergonomics: 51.8
    discoverability: 58.9
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lifx Authentication
  slug: lifx-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Lifx Domain Security
  slug: lifx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lifx Vulnerability Disclosure
  slug: lifx-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: lifx-set-light-state
  slug: lifx-set-light-state
slug: lifx
tags:
- Smart Lighting
- Wi‑Fi Bulbs
- Home Automation
- Lighting Fixtures
website: https://lifx.com/
---
