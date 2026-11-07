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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for RequestRocket platform providing access control and security features.
  name: RequestRocket API
  slug: requestrocket-api-2
- baseURL: https://api.requestrocket.com
  baseurl_source: declared
  description: 'RequestRocket API as documented publicly: 38 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: RequestRocket API
  slug: requestrocket-api
artifact_total: 14
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/requestrocket
- group: commercial
  href: https://artifacts.apis.io/requestrocket/plans/requestrocket-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/requestrocket-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/requestrocket/rules/requestrocket-rules.yml
  title: ''
  type: Spectral
  url: rules/requestrocket-rules.yml
- group: design
  href: https://artifacts.apis.io/requestrocket/json-ld/requestrocket-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/requestrocket-context.jsonld
- group: design
  href: https://artifacts.apis.io/requestrocket/vocabulary/requestrocket-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/requestrocket-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/requestrocket/data-model/requestrocket-data-model.yml
  title: ''
  type: DataModel
  url: data-model/requestrocket-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://requestrocket.com/technology/api-security
- group: auth
  href: https://artifacts.apis.io/requestrocket/authentication/requestrocket-authentication.yml
  title: ''
  type: Authentication
  url: authentication/requestrocket-authentication.yml
- group: design
  href: https://artifacts.apis.io/requestrocket/conformance/requestrocket-conformance.yml
  title: ''
  type: Conformance
  url: conformance/requestrocket-conformance.yml
- group: agent
  href: https://artifacts.apis.io/requestrocket/llms/requestrocket-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/requestrocket-llms.txt
- group: agent
  href: https://artifacts.apis.io/requestrocket/well-known/requestrocket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/requestrocket-well-known.yml
- group: other
  href: https://artifacts.apis.io/requestrocket/hosts/requestrocket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/requestrocket-hosts.yml
- group: other
  href: https://artifacts.apis.io/requestrocket/vendors/requestrocket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/requestrocket-vendors.yml
- group: auth
  href: https://artifacts.apis.io/requestrocket/security/requestrocket-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/requestrocket-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/requestrocket/security/requestrocket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/requestrocket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://requestrocket.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.requestrocket.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.requestrocket.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.requestrocket.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://requestrocket.com/contact
- group: company
  title: ''
  type: Blog
  url: https://requestrocket.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://requestrocket.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.requestrocket.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.requestrocket.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.requestrocket.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.requestrocket.com/login
coverage:
  checked: '2026-10-18'
  detail: OpenAPI spec at https://api.requestrocket.com/openapi.json returns 401 Unauthorized, requiring authentication.
  evidence:
  - status: 401
    url: https://api.requestrocket.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-18'
description: RequestRocket provides runtime access control for AI agents and APIs, offering authentication, authorization, rate limiting, data redaction, transformation, and observability. Their SaaS platform secures AI, API, and MCP interactions, enabling developers and security teams to govern, monitor, and protect data across services. With a focus on AI agent security, RequestRocket delivers a control plane for request lifecycle management, compliance, and integration guidance.
image: https://requestrocket.com/images/requestrocket.png
json_schemas:
- name: GetApiUsersResponse
  property_count: 2
  slug: requestrocket-get-api-users-response
- name: PostApiClientsClientidCredentialsCredentialidRulesRequest
  property_count: 4
  slug: requestrocket-post-api-clients-clientid-credentials-credentialid-rules-request
- name: PostApiClientsClientidProxiesProxyidMetersRequest
  property_count: 15
  slug: requestrocket-post-api-clients-clientid-proxies-proxyid-meters-request
- name: PostApiClientsClientidProxiesProxyidRulesRequest
  property_count: 5
  slug: requestrocket-post-api-clients-clientid-proxies-proxyid-rules-request
- name: PostApiClientsClientidTargetsTargetidRulesRequest
  property_count: 5
  slug: requestrocket-post-api-clients-clientid-targets-targetid-rules-request
- name: PutApiClientsClientidProxiesProxyidMetersMeteridRequest
  property_count: 15
  slug: requestrocket-put-api-clients-clientid-proxies-proxyid-meters-meterid-request
jsonld:
- class_count: 30
  name: Requestrocket Context
  property_count: 34
  slug: requestrocket-context
layout: provider
modified: '2026-10-18'
name: RequestRocket
nav: Providers
network: true
overview: 'RequestRocket is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Security, Software-as-a-Service, and Access Control.


  The RequestRocket catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RequestRocket''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Requestrocket Plans Pricing
  plan_count: 6
  slug: requestrocket-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: RequestRocket API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: requestrocket-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 29.8
    discoverability: 73.2
    operational_transparency: 15.8
  previous_composite: 46.4
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
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/requestrocket/requestrocket-2026-11-03T142403.png
security:
- kind: authentication
  name: Requestrocket Authentication
  slug: requestrocket-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Requestrocket Domain Security
  slug: requestrocket-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Requestrocket Trust Center
  slug: requestrocket-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: requestrocket
tags:
- Company
- Artificial Intelligence
- Security
- Software-as-a-Service
- Access Control
website: https://requestrocket.com/
---
