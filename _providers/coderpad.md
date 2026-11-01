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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Coderpad Agentic Access
  operation_count: 47
  slug: coderpad-agentic-access
  summary_line: 47 operations · 18 acting
api_count: 2
apis:
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: Information about the account the API key belongs to.
  name: CoderPad Account API
  slug: coderpad-account-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The Campaigns API from CoderPad — 4 operation(s) for campaigns.
  name: CoderPad Campaigns API
  slug: coderpad-campaigns-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The Me API from CoderPad — 1 operation(s) for me.
  name: CoderPad Me API
  slug: coderpad-me-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: Information about your organization, its users and its usage. Requires an organization account.
  name: CoderPad Organization API
  slug: coderpad-organization-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: The language environments of a pad, including their files.
  name: CoderPad Pad environments API
  slug: coderpad-pad-environments-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: A pad is a live interview or take-home session.
  name: CoderPad Pads API
  slug: coderpad-pads-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: The starter code of a question that can be taken in several languages or project templates. A question with variants has no language of its own; each variant carries one.
  name: CoderPad Question variants API
  slug: coderpad-question-variants-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: Questions from your question bank, which you can use to start pads.
  name: CoderPad Questions API
  slug: coderpad-questions-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The TemporaryFile API from CoderPad — 1 operation(s) for temporaryfile.
  name: CoderPad Temporary File API
  slug: coderpad-temporaryfile-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The Tests API from CoderPad — 8 operation(s) for tests.
  name: CoderPad Tests API
  slug: coderpad-tests-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The Webhook API from CoderPad — 1 operation(s) for webhook.
  name: CoderPad Webhook API
  slug: coderpad-webhook-api
artifact_total: 23
asyncapis:
- description: ''
  name: Coderpad Webhooks
  slug: coderpad-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/coderpad/agentic-access/coderpad-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coderpad-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/coderpad/plans/coderpad-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coderpad-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coderpad/rules/coderpad-rules.yml
  title: ''
  type: Spectral
  url: rules/coderpad-rules.yml
- group: design
  href: https://artifacts.apis.io/coderpad/json-ld/coderpad-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coderpad-context.jsonld
- group: design
  href: https://artifacts.apis.io/coderpad/vocabulary/coderpad-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coderpad-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coderpad/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coderpad/asyncapi/coderpad-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coderpad-webhooks.yml
- group: design
  href: https://artifacts.apis.io/coderpad/data-model/coderpad-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coderpad-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://coderpad.io/security/
- group: design
  href: https://artifacts.apis.io/coderpad/errors/coderpad-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coderpad-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coderpad/conformance/coderpad-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coderpad-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coderpad/llms/coderpad-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coderpad-llms.txt
- group: auth
  href: https://artifacts.apis.io/coderpad/well-known/coderpad-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coderpad-status-security.txt
- group: auth
  href: https://artifacts.apis.io/coderpad/well-known/coderpad-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coderpad-security.txt
- group: agent
  href: https://artifacts.apis.io/coderpad/well-known/coderpad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coderpad-well-known.yml
- group: other
  href: https://artifacts.apis.io/coderpad/hosts/coderpad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coderpad-hosts.yml
- group: other
  href: https://artifacts.apis.io/coderpad/vendors/coderpad-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coderpad-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coderpad.io
- group: auth
  title: ''
  type: Security
  url: https://coderpad.io/security/
- group: start
  title: ''
  type: Sandbox
  url: https://app.coderpad.io/sandbox
- group: company
  title: ''
  type: Newsroom
  url: https://coderpad.io/press/
- group: start
  title: ''
  type: Login
  url: https://app.coderpad.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://coderpad.io/resources/docs/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://coderpad.io/resources/docs/screen/recruiters-quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoderPad
- group: auth
  href: https://artifacts.apis.io/coderpad/authentication/coderpad-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coderpad-authentication.yml
- group: auth
  href: https://artifacts.apis.io/coderpad/security/coderpad-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coderpad-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/coderpad/security/coderpad-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coderpad-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coderpad/security/coderpad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coderpad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coderpad.io/
- group: docs
  title: ''
  type: Documentation
  url: https://coderpad.io/resources/docs/
- group: company
  title: ''
  type: Blog
  url: https://coderpad.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://coderpad.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coderpad.io/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coderpad.io/privacy/
- group: operate
  title: ''
  type: Support
  url: https://coderpad.io/contact/support/
created: '2026-10-27'
description: CoderPad provides an AI‑ready technical assessment platform that enables companies to create, conduct, and evaluate coding interviews and screening tests. It supports real‑time collaborative coding, AI‑assisted candidate assistance, and integrates with hiring workflows. The service offers features such as interview templates, automated scoring, and detailed analytics to help technical hiring teams evaluate candidates efficiently and fairly across all stages of the hiring process.
image: https://coderpad.io/wp-content/uploads/2024/01/coderpad-hire-better-candidates-faster-opengraph-image.png
jsonld:
- class_count: 120
  name: Coderpad Context
  property_count: 317
  slug: coderpad-context
layout: provider
modified: '2026-10-27'
name: CoderPad
nav: Providers
network: true
overview: 'CoderPad publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Campaigns API, Me API, and 8 more. Tagged areas include Company, AI, Hiring, TechnicalAssessment, and InterviewPlatform.


  The CoderPad catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CoderPad''s developer surface includes sandbox, changelog, getting-started guide, authentication, documentation, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Coderpad Plans Pricing
  plan_count: 7
  slug: coderpad-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: CoderPad API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: coderpad-rules
score:
  band: strong
  composite: 64.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 64.4
    developer_ergonomics: 49.4
    discoverability: 58.9
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
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
  name: Coderpad Authentication
  slug: coderpad-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Coderpad Domain Security
  slug: coderpad-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coderpad Vulnerability Disclosure
  slug: coderpad-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Coderpad Trust Center
  slug: coderpad-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: coderpad-create-and-retrieve-question
  slug: coderpad-create-and-retrieve-question
- name: coderpad-manage-question-variants
  slug: coderpad-manage-question-variants
- name: coderpad-pads-create-and-retrieve
  slug: coderpad-pads-create-and-retrieve
slug: coderpad
tags:
- Company
- AI
- Hiring
- TechnicalAssessment
- InterviewPlatform
website: https://coderpad.io/
---
