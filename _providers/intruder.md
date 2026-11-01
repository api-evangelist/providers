---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Intruder Agentic Access
  operation_count: 33
  slug: intruder-agentic-access
  summary_line: 33 operations · 18 acting
api_count: 1
apis:
- baseURL: https://api.intruder.io
  baseurl_source: declared
  description: The Health API from Intruder — 1 operation(s) for health.
  name: Intruder Health API
  slug: intruder-health-api
- baseURL: https://api.intruder.io
  baseurl_source: declared
  description: The Issues API from Intruder — 6 operation(s) for issues.
  name: Intruder Issues API
  slug: intruder-issues-api
- baseURL: https://api.intruder.io
  baseurl_source: declared
  description: The Licenses API from Intruder — 1 operation(s) for licenses.
  name: Intruder Licenses API
  slug: intruder-licenses-api
- baseURL: https://api.intruder.io
  baseurl_source: declared
  description: The Occurrences API from Intruder — 1 operation(s) for occurrences.
  name: Intruder Occurrences API
  slug: intruder-occurrences-api
- baseURL: https://api.intruder.io
  baseurl_source: declared
  description: The Scans API from Intruder — 5 operation(s) for scans.
  name: Intruder Scans API
  slug: intruder-scans-api
- baseURL: https://api.intruder.io
  baseurl_source: declared
  description: The Tags API from Intruder — 1 operation(s) for tags.
  name: Intruder Tags API
  slug: intruder-tags-api
- baseURL: https://api.intruder.io
  baseurl_source: declared
  description: The Targets API from Intruder — 9 operation(s) for targets.
  name: Intruder Targets API
  slug: intruder-targets-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/intruder/agentic-access/intruder-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/intruder-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/intruder/rate-limits/intruder-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/intruder-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/intruder/plans/intruder-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/intruder-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/intruder/rules/intruder-rules.yml
  title: ''
  type: Spectral
  url: rules/intruder-rules.yml
- group: design
  href: https://artifacts.apis.io/intruder/json-ld/intruder-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/intruder-context.jsonld
- group: design
  href: https://artifacts.apis.io/intruder/vocabulary/intruder-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/intruder-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/intruder/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/intruder/data-model/intruder-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intruder-data-model.yml
- group: design
  href: https://artifacts.apis.io/intruder/conventions/intruder-conventions.yml
  title: ''
  type: Conventions
  url: conventions/intruder-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.intruder.io/security
- group: auth
  href: https://artifacts.apis.io/intruder/authentication/intruder-authentication.yml
  title: ''
  type: Authentication
  url: authentication/intruder-authentication.yml
- group: design
  href: https://artifacts.apis.io/intruder/errors/intruder-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/intruder-problem-types.yml
- group: design
  href: https://artifacts.apis.io/intruder/conformance/intruder-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intruder-conformance.yml
- group: agent
  href: https://artifacts.apis.io/intruder/llms/intruder-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intruder-llms.txt
- group: auth
  href: https://artifacts.apis.io/intruder/well-known/intruder-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/intruder-help-security.txt
- group: agent
  href: https://artifacts.apis.io/intruder/well-known/intruder-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/intruder-well-known.yml
- group: other
  href: https://artifacts.apis.io/intruder/hosts/intruder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intruder-hosts.yml
- group: other
  href: https://artifacts.apis.io/intruder/vendors/intruder-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intruder-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.intruder.io/?_gl=1*v6z0gl*_ga*MTQwOTAxMDU5NC4xNjgyNTk3MDI0*_ga_ME4CJVYS32*MTY4NTg5MzY1Mi4xMS4xLjE2ODU4OTQyNTAuNTUuMC4w
- group: auth
  title: ''
  type: Security
  url: https://www.intruder.io/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.intruder.io/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.intruder.io/changelog
- group: auth
  href: https://artifacts.apis.io/intruder/security/intruder-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/intruder-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/intruder/security/intruder-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/intruder-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/intruder/security/intruder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intruder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intruder.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.intruder.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.intruder.io/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.intruder.io/docs/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://www.intruder.io/get-demo
- group: operate
  title: ''
  type: Support
  url: https://help.intruder.io/
- group: company
  title: ''
  type: Blog
  url: https://www.intruder.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intruder-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.intruder.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://portal.intruder.io/free_trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intruder.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intruder.io/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/intruder-io/workspace
created: '2026-10-20'
description: Intruder provides an AI‑powered platform that helps organizations stop security breaches before they start. Offering on‑demand cloud security, attack surface management, automated vulnerability scanning, and API security testing, Intruder combines continuous monitoring with actionable insights. Their solutions integrate with existing workflows, support compliance frameworks like SOC 2, ISO, HIPAA, and DORA, and deliver a unified view of multi‑cloud risk, enabling security teams to prioritize and remediate threats efficiently.
image: https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/67a491743aabcda5309e1a8e_Open%20Graph.jpg
json_schemas:
- name: AssessmentSchedulesCreateUpdateRequest
  property_count: 9
  slug: intruder-assessment-schedules-create-update-request
- name: PatchedAssessmentSchedulesCreateUpdateRequest
  property_count: 9
  slug: intruder-patched-assessment-schedules-create-update-request
- name: PatchedTargetAuthenticationsRequest
  property_count: 21
  slug: intruder-patched-target-authentications-request
- name: Scan
  property_count: 11
  slug: intruder-scan
- name: TargetAuthenticationsRequest
  property_count: 21
  slug: intruder-target-authentications-request
- name: Target
  property_count: 12
  slug: intruder-target
jsonld:
- class_count: 56
  name: Intruder Context
  property_count: 109
  slug: intruder-context
layout: provider
modified: '2026-10-20'
name: Intruder
nav: Providers
network: true
overview: 'Intruder publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Issues API, Licenses API, and 4 more. Tagged areas include Company, Security, Cloud, API, and AI.


  The Intruder catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Intruder''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 31 more developer resources.'
plans:
- name: Intruder Plans Pricing
  plan_count: 4
  slug: intruder-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Intruder Rate Limits
  slug: intruder-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Intruder API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: intruder-rules
score:
  band: exemplar
  composite: 69.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 63.0
    developer_ergonomics: 63.7
    discoverability: 67.9
    operational_transparency: 78.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Intruder Authentication
  slug: intruder-authentication
  summary_line: 7 schemes
- kind: domain-security
  name: Intruder Domain Security
  slug: intruder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Intruder Vulnerability Disclosure
  slug: intruder-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Intruder Trust Center
  slug: intruder-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
skill_count: 3
skills:
- name: intruder-create-target-with-auth-and-tag
  slug: intruder-create-target-with-auth-and-tag
- name: intruder-issues-snooze-occurrence
  slug: intruder-issues-snooze-occurrence
- name: intruder-start-scan
  slug: intruder-start-scan
slug: intruder
tags:
- Company
- Security
- Cloud
- API
- AI
- Platform
website: https://intruder.io/
---
