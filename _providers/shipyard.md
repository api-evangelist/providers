---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Shipyard provides managed, ephemeral development environments via its API. Documentation is hosted at the developer portal.
  name: Shipyard API
  slug: shipyard-api-2
- baseURL: https://shipyard.build
  baseurl_source: declared
  description: 'Shipyard API as documented publicly: 33 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Shipyard API
  slug: shipyard-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/shipyard/plans/shipyard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shipyard-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/shipyard/rules/shipyard-rules.yml
  title: ''
  type: Spectral
  url: rules/shipyard-rules.yml
- group: design
  href: https://artifacts.apis.io/shipyard/json-ld/shipyard-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shipyard-context.jsonld
- group: design
  href: https://artifacts.apis.io/shipyard/vocabulary/shipyard-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shipyard-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/shipyard/data-model/shipyard-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shipyard-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://shipyard.build/security/
- group: auth
  href: https://artifacts.apis.io/shipyard/authentication/shipyard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shipyard-authentication.yml
- group: design
  href: https://artifacts.apis.io/shipyard/conformance/shipyard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shipyard-conformance.yml
- group: other
  href: https://artifacts.apis.io/shipyard/hosts/shipyard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shipyard-hosts.yml
- group: other
  href: https://artifacts.apis.io/shipyard/vendors/shipyard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shipyard-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://shipyard.build/security
- group: company
  title: ''
  type: Newsroom
  url: https://shipyard.build/press
- group: start
  title: ''
  type: Login
  url: https://shipyard.build/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jnl
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackgen.com/docs/release-notes/aiden/2026/august/v2026-8-8
- group: auth
  href: https://artifacts.apis.io/shipyard/security/shipyard-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/shipyard-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/shipyard/security/shipyard-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/shipyard-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/shipyard/security/shipyard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shipyard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipyard.build
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shipyard.build/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shipyard.build/
- group: company
  title: ''
  type: Blog
  url: https://shipyard.build/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://shipyard.build/pricing
- group: operate
  title: ''
  type: Support
  url: https://shipyard.build/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shipyard.build/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shipyard.build/privacy
coverage:
  detail: Documentation pages are served as JavaScript-rendered HTML, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.shipyard.build/
  - status: 200
    url: https://docs.stackgen.com/shipyard/getting-started/quickstart
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Shipyard provides managed, ephemeral development environments that spin up full-stack, isolated copies of applications for each pull request or feature branch. Integrated with CI/CD pipelines, it supports AI agents, DevOps teams, QA, and product teams, offering rapid testing, cost savings, and automated teardown. Now part of StackGen, Shipyard enables developers to test code changes safely without impacting production, accelerating delivery and reducing cloud spend.
image: https://sy-marketing.netlify.app/images/shipyard-by-stackgen-share.png
json_schemas:
- name: GetApiV1EnvironmentAppUuidEnvVarsResponse
  property_count: 2
  slug: shipyard-get-api-v1-environment-app-uuid-env-vars-response
- name: GetApiV1EnvironmentResponse
  property_count: 4
  slug: shipyard-get-api-v1-environment-response
- name: PostApiV1EnvironmentAppUuidCancelResponse
  property_count: 2
  slug: shipyard-post-api-v1-environment-app-uuid-cancel-response
- name: PostApiV1EnvironmentAppUuidRebuildResponse
  property_count: 2
  slug: shipyard-post-api-v1-environment-app-uuid-rebuild-response
- name: PostApiV1EnvironmentAppUuidReviveResponse
  property_count: 2
  slug: shipyard-post-api-v1-environment-app-uuid-revive-response
- name: PostAppcdApiV1AuthPairedapikeyResponse
  property_count: 6
  slug: shipyard-post-appcd-api-v1-auth-pairedapikey-response
jsonld:
- class_count: 36
  name: Shipyard Context
  property_count: 31
  slug: shipyard-context
layout: provider
modified: '2026-10-29'
name: Shipyard
nav: Providers
network: true
overview: 'Shipyard is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ephemeral Environments, CI/CD, DevOps, and AI Agents.


  The Shipyard catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shipyard''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, support, and 20 more developer resources.'
plans:
- name: Shipyard Plans Pricing
  plan_count: 3
  slug: shipyard-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Shipyard API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: shipyard-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.1
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 31.0
    discoverability: 58.0
    operational_transparency: 7.9
  previous_composite: 49.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shipyard/shipyard-2026-11-03T143131.png
security:
- kind: authentication
  name: Shipyard Authentication
  slug: shipyard-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Shipyard Domain Security
  slug: shipyard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shipyard Vulnerability Disclosure
  slug: shipyard-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Shipyard Trust Center
  slug: shipyard-trust-center
  summary_line: ISO 27001, HIPAA, FedRAMP
slug: shipyard
tags:
- Company
- Ephemeral Environments
- CI/CD
- DevOps
- AI Agents
website: https://www.shipyard.build
---
