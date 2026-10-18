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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Isbusinessemail Agentic Access
  operation_count: 6
  slug: isbusinessemail-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.isbusinessemail.com
  baseurl_source: declared
  description: The Check API from isBusinessEmail — 2 operation(s) for check.
  name: isBusinessEmail Check API
  slug: isbusinessemail-check-api
- baseURL: https://api.isbusinessemail.com
  baseurl_source: declared
  description: The Feedback API from isBusinessEmail — 1 operation(s) for feedback.
  name: isBusinessEmail Feedback API
  slug: isbusinessemail-feedback-api
- baseURL: https://api.isbusinessemail.com
  baseurl_source: declared
  description: The Health API from isBusinessEmail — 1 operation(s) for health.
  name: isBusinessEmail Health API
  slug: isbusinessemail-health-api
- baseURL: https://api.isbusinessemail.com
  baseurl_source: declared
  description: The Usage API from isBusinessEmail — 1 operation(s) for usage.
  name: isBusinessEmail Usage API
  slug: isbusinessemail-usage-api
artifact_total: 12
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/agentic-access/isbusinessemail-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/isbusinessemail-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/rate-limits/isbusinessemail-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/isbusinessemail-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/rules/isbusinessemail-rules.yml
  title: ''
  type: Spectral
  url: rules/isbusinessemail-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/json-ld/isbusinessemail-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/isbusinessemail-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/vocabulary/isbusinessemail-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/isbusinessemail-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/data-model/isbusinessemail-data-model.yml
  title: ''
  type: DataModel
  url: data-model/isbusinessemail-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/lifecycle/isbusinessemail-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/isbusinessemail-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/lifecycle/isbusinessemail-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/isbusinessemail-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/errors/isbusinessemail-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/isbusinessemail-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/conformance/isbusinessemail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/isbusinessemail-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/llms/isbusinessemail-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/isbusinessemail-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/well-known/isbusinessemail-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/isbusinessemail-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/well-known/isbusinessemail-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/isbusinessemail-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/hosts/isbusinessemail-hosts.yml
  title: ''
  type: Hosts
  url: hosts/isbusinessemail-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/vendors/isbusinessemail-vendors.yml
  title: ''
  type: Vendors
  url: vendors/isbusinessemail-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.isbusinessemail.com
- group: auth
  title: ''
  type: Security
  url: https://isbusinessemail.com/security
- group: start
  title: ''
  type: Login
  url: https://isbusinessemail.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://isbusinessemail.com/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/authentication/isbusinessemail-authentication.yml
  title: ''
  type: Authentication
  url: authentication/isbusinessemail-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/security/isbusinessemail-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/isbusinessemail-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/isbusinessemail/refs/heads/main/security/isbusinessemail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/isbusinessemail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://isbusinessemail.com
- group: docs
  title: ''
  type: Documentation
  url: https://isbusinessemail.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://isbusinessemail.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://isbusinessemail.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://isbusinessemail.com/contact
- group: company
  title: ''
  type: Blog
  url: https://isbusinessemail.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://isbusinessemail.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://isbusinessemail.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.isbusinessemail.com/openapi.json
  - status: 401
    url: https://api.isbusinessemail.com/mcp
  - status: 200
    url: https://isbusinessemail.com
  reason: partner-login
  state: gated
created: '2026-10-05'
description: isBusinessEmail provides a free API to determine whether an email address or domain belongs to a business, detecting Google Workspace and Microsoft 365 usage. The service offers up to 100 free checks per day, stores no email data, and is EU‑hosted, making it suitable for privacy‑focused applications. Users can obtain an API key instantly without a credit card, and the platform includes tools, lists, and integrations for developers.
image: https://isbusinessemail.com/og/default.png
json_schemas:
- name: CheckResult
  property_count: 29
  slug: isbusinessemail-check-result
jsonld:
- class_count: 2
  name: Isbusinessemail Context
  property_count: 35
  slug: isbusinessemail-context
layout: provider
modified: '2026-10-05'
name: isBusinessEmail
nav: Providers
network: true
overview: 'isBusinessEmail publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Check API, Feedback API, Health API, and 1 more. Tagged areas include Company, EmailVerification, BusinessTools, and EUHosted.


  The isBusinessEmail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  isBusinessEmail''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 23 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 2
  name: Isbusinessemail Rate Limits
  slug: isbusinessemail-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: isBusinessEmail API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: isbusinessemail-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.2
    catalog_earned_first_party: 8.0
    catalog_gap: 55.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 47.6
    discoverability: 64.3
    operational_transparency: 71.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Isbusinessemail Authentication
  slug: isbusinessemail-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Isbusinessemail Domain Security
  slug: isbusinessemail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Isbusinessemail Vulnerability Disclosure
  slug: isbusinessemail-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: isbusinessemail
tags:
- Company
- EmailVerification
- BusinessTools
- EUHosted
website: https://isbusinessemail.com
---
