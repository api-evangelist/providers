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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Apheris Agentic Access
  operation_count: 9
  slug: apheris-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 8
apis:
- description: API reference for ApherisFold platform
  name: ApherisFold API
  slug: apherisfold-api
- description: The Apheris API API from Apheris — 1 operation(s) for apheris api.
  name: Apheris Apheris API
  slug: apheris-apheris-api-api
- description: The Health API from Apheris — 1 operation(s) for health.
  name: Apheris Health API
  slug: apheris-health-api
- description: The Predict Async API from Apheris — 2 operation(s) for predict async.
  name: Apheris Predict Async API
  slug: apheris-predict-async-api
- description: The Results API from Apheris — 1 operation(s) for results.
  name: Apheris Results API
  slug: apheris-results-api
- description: The Schema API from Apheris — 1 operation(s) for schema.
  name: Apheris Schema API
  slug: apheris-schema-api
- description: The Ticket API from Apheris — 2 operation(s) for ticket.
  name: Apheris Ticket API
  slug: apheris-ticket-api
- description: The Weights API from Apheris — 1 operation(s) for weights.
  name: Apheris Weights API
  slug: apheris-weights-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/apheris/agentic-access/apheris-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apheris-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/apheris/well-known/apheris-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apheris-clarity-security.txt
- group: build
  href: https://artifacts.apis.io/apheris/integrations/apheris-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/apheris-integration-edges.yml
- group: design
  href: https://artifacts.apis.io/apheris/rules/apheris-rules.yml
  title: ''
  type: Spectral
  url: rules/apheris-rules.yml
- group: design
  href: https://artifacts.apis.io/apheris/json-ld/apheris-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apheris-context.jsonld
- group: design
  href: https://artifacts.apis.io/apheris/vocabulary/apheris-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apheris-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apheris/data-model/apheris-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apheris-data-model.yml
- group: operate
  href: https://artifacts.apis.io/apheris/changelog/apheris-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apheris-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: auth
  href: https://artifacts.apis.io/apheris/authentication/apheris-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apheris-authentication.yml
- group: design
  href: https://artifacts.apis.io/apheris/conformance/apheris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apheris-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apheris/well-known/apheris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apheris-well-known.yml
- group: other
  href: https://artifacts.apis.io/apheris/hosts/apheris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apheris-hosts.yml
- group: other
  href: https://artifacts.apis.io/apheris/vendors/apheris-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apheris-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.apheris.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apheris.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://www.apheris.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apheris.com/docs/hub/nim-msa-server-setup.html
- group: auth
  href: https://artifacts.apis.io/apheris/security/apheris-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apheris-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/apheris/security/apheris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apheris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apheris.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Apheris provides federated AI platforms for drug discovery, enabling superior models through federated data networks. The company focuses on leveraging distributed datasets to train high‑performing predictive models for pharmaceutical research, offering tools that integrate securely across institutions.
json_schemas:
- name: GetApiV1PredictAsyncJobidIdResponse
  property_count: 4
  slug: apheris-get-api-v1-predict-async-jobid-id-response
- name: GetWeightsResponse
  property_count: 1
  slug: apheris-get-weights-response
- name: PostApiV1PredictAsyncRequest
  property_count: 5
  slug: apheris-post-api-v1-predict-async-request
- name: PostApiV1PredictAsyncResponse
  property_count: 2
  slug: apheris-post-api-v1-predict-async-response
jsonld:
- class_count: 4
  name: Apheris Context
  property_count: 10
  slug: apheris-context
layout: provider
modified: '2026-09-25'
name: Apheris
nav: Providers
network: true
overview: 'Apheris is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Apheris API, Health API, Predict Async API, and 5 more. Tagged areas include Company, Artificial Intelligence, Drug Discovery, Federated Learning, and Biotechnology.


  The Apheris catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apheris'' developer surface includes changelog, authentication, documentation, getting-started guide, and 17 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Apheris API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: apheris-rules
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 9.2
    contract_governance: 22.0
    contract_quality: 21.0
    developer_ergonomics: 22.6
    discoverability: 58.9
    operational_transparency: 21.1
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apheris/apheris-2026-10-11T100109.png
security:
- kind: authentication
  name: Apheris Authentication
  slug: apheris-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apheris Domain Security
  slug: apheris-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Apheris Vulnerability Disclosure
  slug: apheris-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apheris
tags:
- Company
- Artificial Intelligence
- Drug Discovery
- Federated Learning
- Biotechnology
website: https://www.apheris.com/
---
