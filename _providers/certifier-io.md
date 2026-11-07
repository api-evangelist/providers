---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Certifier Io Agentic Access
  operation_count: 19
  slug: certifier-io-agentic-access
  summary_line: 19 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.certifier.io
  baseurl_source: declared
  description: Endpoints for tracking and managing credential interaction events
  name: Certifier Credential Interactions API
  slug: certifier-io-credential-interactions-api
- baseURL: https://api.certifier.io
  baseurl_source: declared
  description: Endpoints for managing credential templates (groups)
  name: Certifier Credential Templates API
  slug: certifier-io-credential-templates-api
- baseURL: https://api.certifier.io
  baseurl_source: declared
  description: Endpoints for creating, managing, issuing, and sending credentials
  name: Certifier Credentials API
  slug: certifier-io-credentials-api
- baseURL: https://api.certifier.io
  baseurl_source: declared
  description: Endpoints for managing certificate and badge design templates
  name: Certifier Design Templates API
  slug: certifier-io-design-templates-api
artifact_total: 18
asyncapis:
- description: ''
  name: Certifier Io Webhooks
  slug: certifier-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/certifier-io/agentic-access/certifier-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/certifier-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/certifier-io/rate-limits/certifier-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/certifier-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/certifier-io/plans/certifier-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/certifier-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/certifier-io/rules/certifier-io-rules.yml
  title: ''
  type: Spectral
  url: rules/certifier-io-rules.yml
- group: design
  href: https://artifacts.apis.io/certifier-io/json-ld/certifier-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/certifier-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/certifier-io/vocabulary/certifier-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/certifier-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/certifier-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/certifier-io/asyncapi/certifier-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/certifier-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/certifier-io/data-model/certifier-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/certifier-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/certifier-io/changelog/certifier-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/certifier-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/certifier-io/conventions/certifier-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/certifier-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/certifier-io/authentication/certifier-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/certifier-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/certifier-io/lifecycle/certifier-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/certifier-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/certifier-io/errors/certifier-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/certifier-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/certifier-io/conformance/certifier-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/certifier-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/certifier-io/llms/certifier-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/certifier-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/certifier-io/well-known/certifier-io-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/certifier-io-support-security.txt
- group: agent
  href: https://artifacts.apis.io/certifier-io/well-known/certifier-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/certifier-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/certifier-io/hosts/certifier-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/certifier-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/certifier-io/vendors/certifier-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/certifier-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://certifier.io/terms
- group: operate
  title: ''
  type: Support
  url: https://support.certifier.io/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.certifier.io/
- group: start
  title: ''
  type: SignUp
  url: https://app.certifier.io/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://certifier.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://certifier.io/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://certifier.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://certifier.io/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.certifier.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.certifier.io/docs/api-reference/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.certifier.io/
- group: auth
  href: https://artifacts.apis.io/certifier-io/security/certifier-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certifier-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://certifier.io/
created: '2026-11-03'
description: Certifier is the leading software to create, issue, and verify certificates in bulk. An AI‑powered platform for managing digital certificates, credentials, and badges. It offers templates, mass email delivery, and a user‑friendly interface for organizations to automate credential issuance and verification at scale.
image: https://res.cloudinary.com/certifier/image/upload/v1745403347/Certifier_-_Create_distribute_and_manage_digital_credentials_OpenGraph_dvkn5i.jpg
json_schemas:
- name: CreateCredential
  property_count: 5
  slug: certifier-io-create-credential
- name: CreateIssueSendCredential
  property_count: 5
  slug: certifier-io-create-issue-send-credential
- name: CredentialInteraction
  property_count: 5
  slug: certifier-io-credential-interaction
- name: Credential
  property_count: 11
  slug: certifier-io-credential
- name: Group
  property_count: 8
  slug: certifier-io-group
- name: UpdateCredential
  property_count: 4
  slug: certifier-io-update-credential
jsonld:
- class_count: 16
  name: Certifier Io Context
  property_count: 32
  slug: certifier-io-context
layout: provider
modified: '2026-11-03'
name: Certifier
nav: Providers
network: true
overview: 'Certifier publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Credential Interactions API, Credential Templates API, Credentials API, and 1 more. Tagged areas include Company, Certificate, Artificial Intelligence, Automation, and Credentials.


  The Certifier catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Certifier''s developer surface includes changelog, authentication, support, signup flow, pricing, engineering blog, API reference, and 26 more developer resources.'
plans:
- name: Certifier Io Plans Pricing
  plan_count: 3
  slug: certifier-io-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Certifier Io Rate Limits
  slug: certifier-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Certifier API Rules
  rule_count: 56
  severity_counts:
    error: 51
    hint: 0
    info: 3
    warn: 2
  slug: certifier-io-rules
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 72.7
    developer_ergonomics: 36.2
    discoverability: 66.1
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Certifier Io Authentication
  slug: certifier-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Certifier Io Domain Security
  slug: certifier-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: certifier-io
tags:
- Company
- Certificate
- Artificial Intelligence
- Automation
- Credentials
website: https://certifier.io/
---
