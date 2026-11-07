---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Goodflag API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Goodflag API
  slug: goodflag-api
artifact_total: 11
asyncapis:
- description: ''
  name: Goodflag Webhooks
  slug: goodflag-webhooks
common:
- group: operate
  title: ''
  type: Support
  url: https://help.goodflag.com/portal/fr/myarea
- group: docs
  title: ''
  type: Documentation
  url: https://docs.goodflag.com/
- group: design
  href: https://artifacts.apis.io/goodflag/rules/goodflag-rules.yml
  title: ''
  type: Spectral
  url: rules/goodflag-rules.yml
- group: design
  href: https://artifacts.apis.io/goodflag/json-ld/goodflag-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/goodflag-context.jsonld
- group: design
  href: https://artifacts.apis.io/goodflag/vocabulary/goodflag-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/goodflag-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/goodflag/asyncapi/goodflag-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/goodflag-webhooks.yml
- group: design
  href: https://artifacts.apis.io/goodflag/data-model/goodflag-data-model.yml
  title: ''
  type: DataModel
  url: data-model/goodflag-data-model.yml
- group: operate
  href: https://artifacts.apis.io/goodflag/changelog/goodflag-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/goodflag-changelog.yml
- group: design
  href: https://artifacts.apis.io/goodflag/conventions/goodflag-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/goodflag-conventions.yml
- group: design
  href: https://artifacts.apis.io/goodflag/conventions/goodflag-conventions.yml
  title: ''
  type: Conventions
  url: conventions/goodflag-conventions.yml
- group: design
  href: https://artifacts.apis.io/goodflag/conformance/goodflag-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goodflag-conformance.yml
- group: agent
  href: https://artifacts.apis.io/goodflag/llms/goodflag-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goodflag-llms.txt
- group: agent
  href: https://artifacts.apis.io/goodflag/well-known/goodflag-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/goodflag-well-known.yml
- group: other
  href: https://artifacts.apis.io/goodflag/hosts/goodflag-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goodflag-hosts.yml
- group: other
  href: https://artifacts.apis.io/goodflag/vendors/goodflag-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goodflag-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goodflag.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.goodflag.com/accueil/changelog
- group: auth
  href: https://artifacts.apis.io/goodflag/security/goodflag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goodflag-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goodflag.com/
- group: docs
  title: ''
  type: APIReference
  url: https://goodflag.com/api
- group: company
  title: ''
  type: Blog
  url: https://goodflag.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://goodflag.com/tarifs-signature-electronique
- group: start
  title: ''
  type: SignUp
  url: https://goodflag.com/demande-renseignement
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/goodflag/workspace
coverage:
  checked: '2026-10-20'
  detail: The provider's API reference page https://goodflag.com/api returns HTML with no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://goodflag.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Goodflag provides certified electronic signature solutions approved by ANSSI, offering simple, advanced, and qualified e‑signatures, electronic seals, timestamps, and 2D‑Doc capabilities. Their platform integrates with Microsoft Power Automate and offers APIs for signature and seal services, targeting sectors such as education, public, industry, health, real estate, and finance. Goodflag aims to help businesses embed secure electronic signing into their workflows with flexible deployment options.
image: https://goodflag.com/hubfs/Images/Site%20web/solution-de-signature-electronique-securisee.webp
json_schemas:
- name: PostApiLogsExportsResponse
  property_count: 16
  slug: goodflag-post-api-logs-exports-response
- name: PostLp7SignboxPkiCreatecertificateResponse
  property_count: 6
  slug: goodflag-post-lp7-signbox-pki-createcertificate-response
- name: PostLp7SignboxPkiSendmessageResponse
  property_count: 3
  slug: goodflag-post-lp7-signbox-pki-sendmessage-response
- name: PostLp7SignboxPkiSendotpResponse
  property_count: 3
  slug: goodflag-post-lp7-signbox-pki-sendotp-response
- name: PostLp7SignboxRequest
  property_count: 5
  slug: goodflag-post-lp7-signbox-request
- name: PostLp7SignboxResponse
  property_count: 4
  slug: goodflag-post-lp7-signbox-response
jsonld:
- class_count: 13
  name: Goodflag Context
  property_count: 8
  slug: goodflag-context
layout: provider
modified: '2026-10-20'
name: Goodflag
nav: Providers
network: true
overview: 'Goodflag is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Signature, Security, and Integration.


  The Goodflag catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Goodflag''s developer surface includes support, documentation, changelog, API reference, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Goodflag API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: goodflag-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 30.9
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/goodflag/goodflag-2026-11-03T132929.png
security:
- kind: domain-security
  name: Goodflag Domain Security
  slug: goodflag-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodflag
tags:
- Company
- E-Signature
- Security
- Integration
website: https://goodflag.com/
---
