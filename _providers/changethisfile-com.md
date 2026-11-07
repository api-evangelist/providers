---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Changethisfile Com Agentic Access
  operation_count: 9
  slug: changethisfile-com-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 1
apis:
- baseURL: https://changethisfile.com
  baseurl_source: declared
  description: API keys and usage reporting.
  name: ChangeThisFile Account API
  slug: changethisfile-com-account-api
- baseURL: https://changethisfile.com
  baseurl_source: declared
  description: Stripe Checkout and customer portal.
  name: ChangeThisFile Billing API
  slug: changethisfile-com-billing-api
- baseURL: https://changethisfile.com
  baseurl_source: declared
  description: Synchronous and asynchronous file conversions.
  name: ChangeThisFile Conversions API
  slug: changethisfile-com-conversions-api
- baseURL: https://changethisfile.com
  baseurl_source: declared
  description: Async-only conversion jobs. Use these for long-running operations or when you want to poll instead of holding the request open.
  name: ChangeThisFile Jobs API
  slug: changethisfile-com-jobs-api
artifact_total: 21
asyncapis:
- description: ''
  name: Changethisfile Com Webhooks
  slug: changethisfile-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/changethisfile-com/agentic-access/changethisfile-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/changethisfile-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/changethisfile-com/plans/changethisfile-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/changethisfile-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/changethisfile-com/rules/changethisfile-com-rules.yml
  title: ''
  type: Spectral
  url: rules/changethisfile-com-rules.yml
- group: design
  href: https://artifacts.apis.io/changethisfile-com/json-ld/changethisfile-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/changethisfile-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/changethisfile-com/vocabulary/changethisfile-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/changethisfile-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/changethisfile-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/changethisfile-com/asyncapi/changethisfile-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/changethisfile-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/changethisfile-com/data-model/changethisfile-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/changethisfile-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/changethisfile-com/changelog/changethisfile-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/changethisfile-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/changethisfile-com/conventions/changethisfile-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/changethisfile-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/changethisfile-com/conventions/changethisfile-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/changethisfile-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://changethisfile.com/security
- group: auth
  href: https://artifacts.apis.io/changethisfile-com/authentication/changethisfile-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/changethisfile-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/changethisfile-com/errors/changethisfile-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/changethisfile-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/changethisfile-com/conformance/changethisfile-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/changethisfile-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/changethisfile-com/llms/changethisfile-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/changethisfile-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/changethisfile-com/well-known/changethisfile-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/changethisfile-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/changethisfile-com/hosts/changethisfile-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/changethisfile-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/changethisfile-com/vendors/changethisfile-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/changethisfile-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://changethisfile.com/status
- group: auth
  title: ''
  type: Security
  url: https://changethisfile.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://changethisfile.com/api/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://changethisfile.com/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://changethisfile.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://changethisfile.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/changethisfile-com/security/changethisfile-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/changethisfile-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/changethisfile-com/security/changethisfile-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/changethisfile-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/changethisfile-com/security/changethisfile-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changethisfile-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://changethisfile.com/
- group: docs
  title: ''
  type: Documentation
  url: https://changethisfile.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://changethisfile.com/docs/api-reference
- group: docs
  title: ''
  type: OpenAPISpec
  url: https://changethisfile.com/docs/openapi.yaml
- group: commercial
  title: ''
  type: Pricing
  url: https://changethisfile.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://changethisfile.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://changethisfile.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://changethisfile.com/contact
created: '2026-11-03'
description: 'ChangeThisFile is a free online file conversion service offering over 500 conversion routes for images, video, audio, documents, data, ebooks, fonts, and archives. It operates with a privacy‑first architecture: most conversions run client‑side in the browser, while server‑side processing is used only when necessary and files are deleted immediately after conversion. Built and operated by Sovereign Firm, the platform provides a public API for developers to integrate conversion capabilities into their applications.'
image: https://changethisfile.com/images/og-default.png
json_schemas:
- name: ConversionRequest
  property_count: 4
  slug: changethisfile-com-conversion-request
- name: ConversionResponse
  property_count: 5
  slug: changethisfile-com-conversion-response
- name: Job
  property_count: 3
  slug: changethisfile-com-job
- name: JobStatus
  property_count: 6
  slug: changethisfile-com-job-status
- name: Plan
  property_count: 8
  slug: changethisfile-com-plan
- name: Usage
  property_count: 6
  slug: changethisfile-com-usage
jsonld:
- class_count: 8
  name: Changethisfile Com Context
  property_count: 28
  slug: changethisfile-com-context
layout: provider
modified: '2026-11-03'
name: ChangeThisFile
nav: Providers
network: true
overview: 'ChangeThisFile publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Conversions API, and 1 more. Tagged areas include File Conversion, Free, Privacy, and Software-as-a-Service.


  The ChangeThisFile catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ChangeThisFile''s developer surface includes changelog, authentication, sandbox, engineering blog, getting-started guide, documentation, API reference, and 29 more developer resources.'
plans:
- name: Changethisfile Com Plans Pricing
  plan_count: 6
  slug: changethisfile-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: ChangeThisFile API Rules
  rule_count: 71
  severity_counts:
    error: 67
    hint: 0
    info: 3
    warn: 1
  slug: changethisfile-com-rules
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 72.5
    developer_ergonomics: 35.1
    discoverability: 57.1
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Changethisfile Com Authentication
  slug: changethisfile-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Changethisfile Com Domain Security
  slug: changethisfile-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Changethisfile Com Vulnerability Disclosure
  slug: changethisfile-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Changethisfile Com Trust Center
  slug: changethisfile-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 2
skills:
- name: changethisfile-com-billing-checkout
  slug: changethisfile-com-billing-checkout
- name: changethisfile-com-create-and-poll-job
  slug: changethisfile-com-create-and-poll-job
slug: changethisfile-com
tags:
- File Conversion
- Free
- Privacy
- Software-as-a-Service
website: https://changethisfile.com/
---
