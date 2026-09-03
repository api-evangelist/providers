---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 2
  name: Xiaomi Agentic Access
  operation_count: 23
  slug: xiaomi-agentic-access
  summary_line: 23 operations · 14 acting · 2 human-in-the-loop
api_count: 3
apis:
- baseURL: https://open.account.xiaomi.com
  baseurl_source: declared
  description: The Access Control API from Xiaomi — 1 operation(s) for access control.
  name: Xiaomi Access Control API
  slug: xiaomi-access-control-api
- baseURL: https://open.account.xiaomi.com
  baseurl_source: declared
  description: The Authentication API from Xiaomi — 1 operation(s) for authentication.
  name: Xiaomi Authentication API
  slug: xiaomi-authentication-api
- baseURL: https://open.account.xiaomi.com
  baseurl_source: declared
  description: The CDN API from Xiaomi — 2 operation(s) for cdn.
  name: Xiaomi CDN API
  slug: xiaomi-cdn-api
- baseURL: https://open.account.xiaomi.com
  baseurl_source: declared
  description: The Chat API from Xiaomi — 1 operation(s) for chat.
  name: Xiaomi Chat API
  slug: xiaomi-chat-api
- baseURL: https://open.account.xiaomi.com
  baseurl_source: declared
  description: The Models API from Xiaomi — 1 operation(s) for models.
  name: Xiaomi Models API
  slug: xiaomi-models-api
- baseURL: https://open.account.xiaomi.com
  baseurl_source: declared
  description: The Multipart Upload API from Xiaomi — 3 operation(s) for multipart upload.
  name: Xiaomi Multipart Upload API
  slug: xiaomi-multipart-upload-api
- baseURL: https://open.account.xiaomi.com
  baseurl_source: declared
  description: The Objects API from Xiaomi — 4 operation(s) for objects.
  name: Xiaomi Objects API
  slug: xiaomi-objects-api
- baseURL: https://open.account.xiaomi.com
  baseurl_source: declared
  description: The User API from Xiaomi — 4 operation(s) for user.
  name: Xiaomi User API
  slug: xiaomi-user-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Xiaomi Galaxy FDS Access Control API
  slug: open-xiaomi-access-control-api
- collection_type: open
  name: Xiaomi Galaxy FDS Access Control Authentication API
  slug: open-xiaomi-authentication-api
- collection_type: open
  name: Xiaomi Galaxy FDS Access Control CDN API
  slug: open-xiaomi-cdn-api
- collection_type: open
  name: Xiaomi Galaxy FDS Access Control Chat API
  slug: open-xiaomi-chat-api
- collection_type: open
  name: Xiaomi Galaxy FDS API
  slug: open-xiaomi-galaxy-fds
- collection_type: open
  name: Xiaomi MiMo AI API
  slug: open-xiaomi-mimo-api
- collection_type: open
  name: Xiaomi Galaxy FDS Access Control Models API
  slug: open-xiaomi-models-api
- collection_type: open
  name: Xiaomi Galaxy FDS Access Control Multipart Upload API
  slug: open-xiaomi-multipart-upload-api
- collection_type: open
  name: Xiaomi Galaxy FDS Access Control Objects API
  slug: open-xiaomi-objects-api
- collection_type: open
  name: Xiaomi Open API
  slug: open-xiaomi-open-api
- collection_type: open
  name: Xiaomi Galaxy FDS Access Control User API
  slug: open-xiaomi-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xiaomi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/xiaomi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xiaomi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xiaomi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xiaomi-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xiaomi-technology
- group: company
  title: ''
  type: Website
  url: https://www.mi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.mi.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XiaoMi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/XiaoMi/galaxy-fds-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/XiaoMi/cloud-ml-sdk
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/json-schema/xiaomi-user-profile-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/json-schema/xiaomi-chat-completion-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/json-ld/xiaomi-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/vocabulary/xiaomi-vocabulary.yml
created: '2025-02-25'
description: Xiaomi is a multinational technology company headquartered in Beijing, China, that designs, develops, and sells a wide range of consumer electronics and related software services. The company is known for its smartphones, laptops, smart home devices, and other innovative products. Xiaomi offers developer APIs for IoT device control, cloud storage (Galaxy FDS), account/identity (Open API), machine learning (Cloud-ML), and AI language models (MiMo).
examples:
- key_count: 2
  name: Xiaomi Create Chat Completion Example
  slug: xiaomi-create-chat-completion-example
- key_count: 2
  name: Xiaomi Get User Profile Example
  slug: xiaomi-get-user-profile-example
finops:
- name: Xiaomi Finops
  service_category: Consumer Electronics / IoT
  slug: xiaomi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xiaomi.png
json_schemas:
- name: Xiaomi MiMo Chat Completion
  property_count: 6
  slug: xiaomi-chat-completion
- name: Xiaomi User Profile
  property_count: 3
  slug: xiaomi-user-profile
json_structures:
- name: Xiaomi User Profile Structure
  property_count: 0
  slug: xiaomi-user-profile-structure
jsonld:
- class_count: 20
  name: Xiaomi Context
  property_count: 2
  slug: xiaomi-context
layout: provider
modified: '2026-05-19'
name: Xiaomi
nav: Providers
network: true
overview: 'Xiaomi publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Access Control API, Authentication API, CDN API, and 5 more. Tagged areas include Consumer Electronics, IoT, Smart Home, Mobile, and Artificial Intelligence.


  The Xiaomi catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Xiaomi''s developer surface includes authentication and 14 more developer resources.'
plans:
- name: Xiaomi Plans Pricing
  plan_count: 1
  slug: xiaomi-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Xiaomi Rate Limits
  slug: xiaomi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Xiaomi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: xiaomi-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Xiaomi API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 5
  slug: xiaomi-rules
scopes:
- name: Xiaomi Scopes
  scope_count: 5
  slug: xiaomi-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 28.8
    contract_quality: 60.2
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/screenshots/xiaomi-2026-06-20T201705.png
security:
- kind: authentication
  name: Xiaomi Authentication
  slug: xiaomi-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Xiaomi Domain Security
  slug: xiaomi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Xiaomi Trust Center
  slug: xiaomi-trust-center
  summary_line: GDPR
slug: xiaomi
tags:
- Consumer Electronics
- IoT
- Smart Home
- Mobile
- Artificial Intelligence
- Cloud Storage
- Machine-Learning
website: https://www.mi.com
---
