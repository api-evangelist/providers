---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Bynn Com Agentic Access
  operation_count: 54
  slug: bynn-com-agentic-access
  summary_line: 54 operations · 29 acting
api_count: 1
apis:
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about age_verifications
  name: Bynn Intelligence Age Verification API
  slug: bynn-com-age-verification-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about amls
  name: Bynn Intelligence Aml API
  slug: bynn-com-aml-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about api_keys
  name: Bynn Intelligence API Keys API
  slug: bynn-com-api-keys-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about autodocs
  name: Bynn Intelligence Autodoc API
  slug: bynn-com-autodoc-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about documents
  name: Bynn Intelligence Documents API
  slug: bynn-com-documents-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about dossiers
  name: Bynn Intelligence Dossiers API
  slug: bynn-com-dossiers-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about Face Collections
  name: Bynn Intelligence Face Collections API
  slug: bynn-com-face-collections-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about Face Enrollments
  name: Bynn Intelligence Face Enrollment API
  slug: bynn-com-face-enrollment-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about Face Searches
  name: Bynn Intelligence Face Search API
  slug: bynn-com-face-search-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about moderations
  name: Bynn Intelligence Moderation API
  slug: bynn-com-moderation-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about nfcs
  name: Bynn Intelligence Nfc API
  slug: bynn-com-nfc-api
- baseURL: https://api.bynn.com/v1
  baseurl_source: declared
  description: Operations about sessions
  name: Bynn Intelligence Sessions API
  slug: bynn-com-sessions-api
artifact_total: 28
common:
- group: auth
  href: https://artifacts.apis.io/bynn-com/well-known/bynn-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bynn-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/bynn-com/agentic-access/bynn-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bynn-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bynn-com/rules/bynn-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bynn-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bynn-com/json-ld/bynn-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bynn-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bynn-com/vocabulary/bynn-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bynn-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bynn-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bynn-com/data-model/bynn-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bynn-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bynn-com/conventions/bynn-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bynn-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/bynn-com/conventions/bynn-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bynn-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bynn.com/company/trust
- group: design
  href: https://artifacts.apis.io/bynn-com/errors/bynn-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bynn-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bynn-com/conformance/bynn-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bynn-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bynn-com/llms/bynn-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bynn-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bynn-com/well-known/bynn-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bynn-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bynn-com/hosts/bynn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bynn-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bynn-com/vendors/bynn-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bynn-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bynn.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bynn.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bynn.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Bynn-Intelligence/bynn-cli/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bynn.com/docs/bynn-onboarding-process
- group: auth
  href: https://artifacts.apis.io/bynn-com/authentication/bynn-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bynn-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bynn-com/security/bynn-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bynn-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bynn-com/security/bynn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bynn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bynn.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bynn.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bynn.com/docs/bynn-mcp
- group: docs
  title: ''
  type: APIReference
  url: https://api.bynn.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://bynn.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://bynn.com/blog
created: '2026-11-03'
description: Bynn Intelligence builds enterprise AI through frontier research, proprietary models, autonomous systems, and AI development and integration. The company offers advanced AI solutions for enterprises, focusing on cutting‑edge research, scalable models, and integration services to accelerate digital transformation across industries.
image: https://bynn.com/open-graph.jpg
json_schemas:
- name: Bynn_V1_Entities_AgeVerificationResult
  property_count: 13
  slug: bynn-com-bynn-v1-entities-age-verification-result
- name: Bynn_V1_Entities_AutoDocInvitation
  property_count: 16
  slug: bynn-com-bynn-v1-entities-auto-doc-invitation
- name: Bynn_V1_Entities_DossierEntity
  property_count: 21
  slug: bynn-com-bynn-v1-entities-dossier-entity
- name: Bynn_V1_Entities_ModerationModelEntity
  property_count: 26
  slug: bynn-com-bynn-v1-entities-moderation-model-entity
- name: postDocuments
  property_count: 5
  slug: bynn-com-post-documents
- name: postNfc
  property_count: 35
  slug: bynn-com-post-nfc
jsonld:
- class_count: 64
  name: Bynn Com Context
  property_count: 263
  slug: bynn-com-context
layout: provider
modified: '2026-11-03'
name: Bynn Intelligence
nav: Providers
network: true
overview: 'Bynn Intelligence publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Age Verification API, Aml API, API Keys API, and 9 more. Tagged areas include Artificial Intelligence, Enterprise, Frontier Research, Identity Verification, and Digital Trust.


  The Bynn Intelligence catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bynn Intelligence''s developer surface includes changelog, getting-started guide, authentication, documentation, API reference, pricing, engineering blog, and 23 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Bynn Intelligence API Rules
  rule_count: 71
  severity_counts:
    error: 61
    hint: 0
    info: 3
    warn: 7
  slug: bynn-com-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 64.7
    developer_ergonomics: 33.9
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bynn Com Authentication
  slug: bynn-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bynn Com Domain Security
  slug: bynn-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Bynn Com Trust Center
  slug: bynn-com-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 4
skills:
- name: bynn-com-create-and-retrieve-document
  slug: bynn-com-create-and-retrieve-document
- name: bynn-com-create-and-retrieve-dossier
  slug: bynn-com-create-and-retrieve-dossier
- name: bynn-com-face-collection-management
  slug: bynn-com-face-collection-management
- name: bynn-com-face-enrollment-workflow
  slug: bynn-com-face-enrollment-workflow
slug: bynn-com
tags:
- Artificial Intelligence
- Enterprise
- Frontier Research
- Identity Verification
- Digital Trust
website: https://bynn.com/
---
