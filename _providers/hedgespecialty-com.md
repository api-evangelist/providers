---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Hedgespecialty Com Agentic Access
  operation_count: 75
  slug: hedgespecialty-com-agentic-access
  summary_line: 75 operations · 29 acting
api_count: 1
apis:
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Account API from Hedge — 1 operation(s) for account.
  name: Hedge Account API
  slug: hedgespecialty-com-account-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Appetite API from Hedge — 7 operation(s) for appetite.
  name: Hedge Appetite API
  slug: hedgespecialty-com-appetite-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Auth API from Hedge — 4 operation(s) for auth.
  name: Hedge Auth API
  slug: hedgespecialty-com-auth-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Binding API from Hedge — 5 operation(s) for binding.
  name: Hedge Binding API
  slug: hedgespecialty-com-binding-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Carrier quotes API from Hedge — 14 operation(s) for carrier quotes.
  name: Hedge Carrier quotes API
  slug: hedgespecialty-com-carrier-quotes-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Documents API from Hedge — 5 operation(s) for documents.
  name: Hedge Documents API
  slug: hedgespecialty-com-documents-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Market access API from Hedge — 5 operation(s) for market access.
  name: Hedge Market access API
  slug: hedgespecialty-com-market-access-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Payments API from Hedge — 1 operation(s) for payments.
  name: Hedge Payments API
  slug: hedgespecialty-com-payments-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Policies API from Hedge — 3 operation(s) for policies.
  name: Hedge Policies API
  slug: hedgespecialty-com-policies-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Programs API from Hedge — 2 operation(s) for programs.
  name: Hedge Programs API
  slug: hedgespecialty-com-programs-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Requirements API from Hedge — 12 operation(s) for requirements.
  name: Hedge Requirements API
  slug: hedgespecialty-com-requirements-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Submissions API from Hedge — 11 operation(s) for submissions.
  name: Hedge Submissions API
  slug: hedgespecialty-com-submissions-api
- baseURL: https://api.hedgespecialty.com/api/v1
  baseurl_source: declared
  description: The Webhooks API from Hedge — 0 operation(s) for webhooks.
  name: Hedge Webhooks API
  slug: hedgespecialty-com-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Hedgespecialty Com Webhooks
  slug: hedgespecialty-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/hedgespecialty-com/agentic-access/hedgespecialty-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hedgespecialty-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/rules/hedgespecialty-com-rules.yml
  title: ''
  type: Spectral
  url: rules/hedgespecialty-com-rules.yml
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/json-ld/hedgespecialty-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hedgespecialty-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/vocabulary/hedgespecialty-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hedgespecialty-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hedgespecialty-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/asyncapi/hedgespecialty-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hedgespecialty-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/data-model/hedgespecialty-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hedgespecialty-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/conventions/hedgespecialty-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hedgespecialty-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/conventions/hedgespecialty-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hedgespecialty-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/hedgespecialty-com/security/hedgespecialty-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/hedgespecialty-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hedgespecialty-com/authentication/hedgespecialty-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hedgespecialty-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/errors/hedgespecialty-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hedgespecialty-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hedgespecialty-com/conformance/hedgespecialty-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hedgespecialty-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hedgespecialty-com/llms/hedgespecialty-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hedgespecialty-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/hedgespecialty-com/well-known/hedgespecialty-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hedgespecialty-com-security.txt
- group: auth
  href: https://artifacts.apis.io/hedgespecialty-com/well-known/hedgespecialty-com-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hedgespecialty-com-portal-security.txt
- group: auth
  href: https://artifacts.apis.io/hedgespecialty-com/well-known/hedgespecialty-com-brokers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hedgespecialty-com-brokers-security.txt
- group: agent
  href: https://artifacts.apis.io/hedgespecialty-com/well-known/hedgespecialty-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hedgespecialty-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hedgespecialty-com/hosts/hedgespecialty-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hedgespecialty-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hedgespecialty-com/vendors/hedgespecialty-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hedgespecialty-com-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.hedgespecialty.com/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hedgespecialty.com/quickstart/
- group: auth
  href: https://artifacts.apis.io/hedgespecialty-com/scopes/hedgespecialty-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hedgespecialty-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/hedgespecialty-com/security/hedgespecialty-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hedgespecialty-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hedgespecialty-com/security/hedgespecialty-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hedgespecialty-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hedgespecialty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hedgespecialty.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hedgespecialty.com/agents
- group: operate
  title: ''
  type: Support
  url: https://www.hedgespecialty.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hedgespecialty.com/legal-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hedgespecialty.com/legal-privacy
created: '2026-10-29'
description: Hedge Specialty provides wholesale insurance solutions for retail brokers, focusing on hard-to-place commercial risks. The platform offers structured intake, broker support, and a guided submission process, enabling agents to submit accounts for market review without initial login. Hedge streamlines specialty coverage placement, offering tools for agents and software integrations, and aims to simplify complex risk underwriting for the insurance market.
image: https://www.hedgespecialty.com/og-image.png
json_schemas:
- name: ApplicationSection
  property_count: 30
  slug: hedgespecialty-com-application-section
- name: CatalogResult
  property_count: 5
  slug: hedgespecialty-com-catalog-result
- name: IntakeCreated
  property_count: 9
  slug: hedgespecialty-com-intake-created
- name: Requirements
  property_count: 14
  slug: hedgespecialty-com-requirements
- name: SharedQuestion
  property_count: 14
  slug: hedgespecialty-com-shared-question
- name: SubmissionCreate
  property_count: 19
  slug: hedgespecialty-com-submission-create
jsonld:
- class_count: 49
  name: Hedgespecialty Com Context
  property_count: 270
  slug: hedgespecialty-com-context
layout: provider
modified: '2026-10-29'
name: Hedge
nav: Providers
network: true
overview: 'Hedge publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Appetite API, Auth API, and 10 more. Tagged areas include Company, Insurance, Wholesale, Brokerage, and Specialty.


  The Hedge catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Hedge''s developer surface includes authentication, getting-started guide, documentation, support, and 27 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Hedge API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 1
  slug: hedgespecialty-com-rules
scopes:
- name: Hedgespecialty Com Scopes
  scope_count: 2
  slug: hedgespecialty-com-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 69.7
    developer_ergonomics: 31.5
    discoverability: 74.1
    operational_transparency: 18.4
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 38.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hedgespecialty-com/hedgespecialty-com-2026-11-03T133324.png
security:
- kind: authentication
  name: Hedgespecialty Com Authentication
  slug: hedgespecialty-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hedgespecialty Com Domain Security
  slug: hedgespecialty-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hedgespecialty Com Vulnerability Disclosure
  slug: hedgespecialty-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: hedgespecialty-com-bind-quote
  slug: hedgespecialty-com-bind-quote
- name: hedgespecialty-com-carrier-quotes-workflow
  slug: hedgespecialty-com-carrier-quotes-workflow
- name: hedgespecialty-com-download-submission-documents
  slug: hedgespecialty-com-download-submission-documents
- name: hedgespecialty-com-oauth-flow
  slug: hedgespecialty-com-oauth-flow
- name: hedgespecialty-com-submit-risk
  slug: hedgespecialty-com-submit-risk
slug: hedgespecialty-com
tags:
- Company
- Insurance
- Wholesale
- Brokerage
- Specialty
website: https://www.hedgespecialty.com/
---
