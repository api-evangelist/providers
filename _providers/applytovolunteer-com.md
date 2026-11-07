---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Applytovolunteer Com Agentic Access
  operation_count: 26
  slug: applytovolunteer-com-agentic-access
  summary_line: 26 operations · 14 acting
api_count: 1
apis:
- baseURL: https://applytovolunteer.com
  baseurl_source: declared
  description: The Applications API from ApplyToVolunteer — 1 operation(s) for applications.
  name: ApplyToVolunteer Applications API
  slug: applytovolunteer-com-applications-api
- baseURL: https://applytovolunteer.com
  baseurl_source: declared
  description: The Auth API from ApplyToVolunteer — 2 operation(s) for auth.
  name: ApplyToVolunteer Auth API
  slug: applytovolunteer-com-auth-api
- baseURL: https://applytovolunteer.com
  baseurl_source: declared
  description: The Conversions API from ApplyToVolunteer — 2 operation(s) for conversions.
  name: ApplyToVolunteer Conversions API
  slug: applytovolunteer-com-conversions-api
- baseURL: https://applytovolunteer.com
  baseurl_source: declared
  description: The Demos API from ApplyToVolunteer — 1 operation(s) for demos.
  name: ApplyToVolunteer Demos API
  slug: applytovolunteer-com-demos-api
- baseURL: https://applytovolunteer.com
  baseurl_source: declared
  description: The Forms API from ApplyToVolunteer — 7 operation(s) for forms.
  name: ApplyToVolunteer Forms API
  slug: applytovolunteer-com-forms-api
- baseURL: https://applytovolunteer.com
  baseurl_source: declared
  description: The Me API from ApplyToVolunteer — 1 operation(s) for me.
  name: ApplyToVolunteer Me API
  slug: applytovolunteer-com-me-api
- baseURL: https://applytovolunteer.com
  baseurl_source: declared
  description: The Public API from ApplyToVolunteer — 2 operation(s) for public.
  name: ApplyToVolunteer Public API
  slug: applytovolunteer-com-public-api
- baseURL: https://applytovolunteer.com
  baseurl_source: declared
  description: The Tools API from ApplyToVolunteer — 5 operation(s) for tools.
  name: ApplyToVolunteer Tools API
  slug: applytovolunteer-com-tools-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/applytovolunteer-com/agentic-access/applytovolunteer-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/applytovolunteer-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/applytovolunteer-com/rules/applytovolunteer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/applytovolunteer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/applytovolunteer-com/json-ld/applytovolunteer-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/applytovolunteer-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/applytovolunteer-com/vocabulary/applytovolunteer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/applytovolunteer-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/applytovolunteer-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/applytovolunteer-com/data-model/applytovolunteer-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/applytovolunteer-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/applytovolunteer-com/security/applytovolunteer-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/applytovolunteer-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/applytovolunteer-com/authentication/applytovolunteer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/applytovolunteer-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/applytovolunteer-com/scopes/applytovolunteer-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/applytovolunteer-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/applytovolunteer-com/errors/applytovolunteer-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/applytovolunteer-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/applytovolunteer-com/conformance/applytovolunteer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/applytovolunteer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/applytovolunteer-com/llms/applytovolunteer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applytovolunteer-com-llms.txt
- group: other
  href: https://artifacts.apis.io/applytovolunteer-com/a2a/applytovolunteer-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/applytovolunteer-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/applytovolunteer-com/well-known/applytovolunteer-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/applytovolunteer-com-security.txt
- group: agent
  href: https://artifacts.apis.io/applytovolunteer-com/well-known/applytovolunteer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applytovolunteer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/applytovolunteer-com/hosts/applytovolunteer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applytovolunteer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/applytovolunteer-com/vendors/applytovolunteer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applytovolunteer-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://applytovolunteer.com/login
- group: auth
  href: https://artifacts.apis.io/applytovolunteer-com/security/applytovolunteer-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/applytovolunteer-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/applytovolunteer-com/security/applytovolunteer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applytovolunteer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://applytovolunteer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://applytovolunteer.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://applytovolunteer.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://applytovolunteer.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://applytovolunteer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://applytovolunteer.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:help@apply2volunteer.com
created: '2026-11-01'
description: ApplyToVolunteer provides a platform that transforms existing PDF volunteer application forms into short, mobile‑friendly online forms. Users can upload their current forms, customize questions, and publish them as hosted forms or embed them on their own websites, enabling volunteers to apply easily from their phones. The service includes free tools such as a form grader and PDF‑to‑online converter, with paid plans announced for future features. It aims to streamline volunteer recruitment for organizations by reducing paperwork and improving the applicant experience.
jsonld:
- class_count: 1
  name: Applytovolunteer Com Context
  property_count: 4
  slug: applytovolunteer-com-context
layout: provider
modified: '2026-11-01'
name: ApplyToVolunteer
nav: Providers
network: true
overview: 'ApplyToVolunteer publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Auth API, Conversions API, and 5 more. Tagged areas include Volunteer, Forms, Software-as-a-Service, Non-Profit, and Platform.


  The ApplyToVolunteer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ApplyToVolunteer''s developer surface includes authentication, documentation, API reference, pricing, support, and 22 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 0
  name: Applytovolunteer Com Rate Limits
  slug: applytovolunteer-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: ApplyToVolunteer API Rules
  rule_count: 60
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 6
  slug: applytovolunteer-com-rules
scopes:
- name: Applytovolunteer Com Scopes
  scope_count: 4
  slug: applytovolunteer-com-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 52.1
    developer_ergonomics: 26.8
    discoverability: 62.5
    operational_transparency: 10.5
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Applytovolunteer Com Authentication
  slug: applytovolunteer-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Applytovolunteer Com Domain Security
  slug: applytovolunteer-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Applytovolunteer Com Vulnerability Disclosure
  slug: applytovolunteer-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: applytovolunteer-com-create-and-publish-form
  slug: applytovolunteer-com-create-and-publish-form
slug: applytovolunteer-com
tags:
- Volunteer
- Forms
- Software-as-a-Service
- Non-Profit
- Platform
website: https://applytovolunteer.com/
---
