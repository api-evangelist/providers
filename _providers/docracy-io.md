---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API documented on the Docracy developer portal, but no machine‑readable contract was found.
  name: Docracy API
  slug: docracy-api
- baseURL: https://api.docracy.io
  baseurl_source: declared
  description: 'Docracy API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Docracy API
  slug: docracy-io-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/docracy-io/plans/docracy-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docracy-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docracy-io/rules/docracy-io-rules.yml
  title: ''
  type: Spectral
  url: rules/docracy-io-rules.yml
- group: design
  href: https://artifacts.apis.io/docracy-io/json-ld/docracy-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docracy-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/docracy-io/vocabulary/docracy-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docracy-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/docracy-io/data-model/docracy-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docracy-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docracy.io/trust
- group: auth
  title: ''
  type: Security
  url: https://docracy.io/trust
- group: design
  href: https://artifacts.apis.io/docracy-io/conformance/docracy-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docracy-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docracy-io/llms/docracy-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docracy-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/docracy-io/well-known/docracy-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docracy-io-security.txt
- group: agent
  href: https://artifacts.apis.io/docracy-io/well-known/docracy-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docracy-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/docracy-io/hosts/docracy-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docracy-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/docracy-io/vendors/docracy-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docracy-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docracy.io/terms
- group: operate
  title: ''
  type: Roadmap
  url: https://docracy.io/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docracy.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://docracy.io/pricing
- group: start
  title: ''
  type: Login
  url: https://docracy.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://docracy.io/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docracy.io/developers
- group: company
  title: ''
  type: Blog
  url: https://docracy.io/blog
- group: auth
  href: https://artifacts.apis.io/docracy-io/security/docracy-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/docracy-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/docracy-io/security/docracy-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/docracy-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/docracy-io/security/docracy-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docracy-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docracy.io/
coverage:
  checked: '2026-11-05'
  detail: Docracy developer pages provide documentation but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docracy.io/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Docracy provides free, no‑signup e‑signature services for quick, low‑stakes agreements. Built by RELACON GmbH, it lets users create, send, and sign documents without an account, offering features like WhatsApp payments and a marketplace of templates.
image: https://docracy.io/og-image.png
json_schemas:
- name: PostApiEmbedApiTokenSessionsRequest
  property_count: 5
  slug: docracy-io-post-api-embed-api-token-sessions-request
- name: PostApiEmbedApiTokenSessionsResponse
  property_count: 3
  slug: docracy-io-post-api-embed-api-token-sessions-response
- name: PostApiEmbedSessionsRequest
  property_count: 5
  slug: docracy-io-post-api-embed-sessions-request
- name: PostApiEmbedSessionsResponse
  property_count: 3
  slug: docracy-io-post-api-embed-sessions-response
- name: PostApiZapierDocumentsBulkRequest
  property_count: 4
  slug: docracy-io-post-api-zapier-documents-bulk-request
- name: PostApiZapierDocumentsRequest
  property_count: 2
  slug: docracy-io-post-api-zapier-documents-request
jsonld:
- class_count: 12
  name: Docracy Io Context
  property_count: 22
  slug: docracy-io-context
layout: provider
modified: '2026-11-05'
name: Docracy
nav: Providers
network: true
overview: 'Docracy is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Signature, Free, and Document Automation.


  The Docracy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Docracy''s developer surface includes pricing, documentation, engineering blog, and 22 more developer resources.'
plans:
- name: Docracy Io Plans Pricing
  plan_count: 3
  slug: docracy-io-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Docracy API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: docracy-io-rules
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docracy Io Domain Security
  slug: docracy-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Docracy Io Vulnerability Disclosure
  slug: docracy-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Docracy Io Trust Center
  slug: docracy-io-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: docracy-io
tags:
- Company
- E-Signature
- Free
- Document Automation
website: https://docracy.io/
---
