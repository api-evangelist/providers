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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: API documentation and developer resources for Laserfiche platform
  name: Laserfiche API
  slug: laserfiche-api
- baseURL: https://api.laserfiche.com
  baseurl_source: declared
  description: The Oauth API from Laserfiche — 2 operation(s) for oauth.
  name: Laserfiche OAuth API
  slug: laserfiche-oauth-api
- baseURL: https://api.laserfiche.com
  baseurl_source: declared
  description: The Odata4 API from Laserfiche — 2 operation(s) for odata4.
  name: Laserfiche Odata4 API
  slug: laserfiche-odata4-api
- baseURL: https://api.laserfiche.com
  baseurl_source: declared
  description: The Repositories API from Laserfiche — 1 operation(s) for repositories.
  name: Laserfiche Repositories API
  slug: laserfiche-repositories-api
- baseURL: https://api.laserfiche.com
  baseurl_source: declared
  description: The Repository API from Laserfiche — 13 operation(s) for repository.
  name: Laserfiche Repository API
  slug: laserfiche-repository-api
artifact_total: 25
common:
- group: auth
  href: https://artifacts.apis.io/laserfiche/well-known/laserfiche-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/laserfiche-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/laserfiche/plans/laserfiche-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/laserfiche-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/laserfiche/rules/laserfiche-rules.yml
  title: ''
  type: Spectral
  url: rules/laserfiche-rules.yml
- group: design
  href: https://artifacts.apis.io/laserfiche/json-ld/laserfiche-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/laserfiche-context.jsonld
- group: design
  href: https://artifacts.apis.io/laserfiche/vocabulary/laserfiche-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/laserfiche-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/laserfiche/data-model/laserfiche-data-model.yml
  title: ''
  type: DataModel
  url: data-model/laserfiche-data-model.yml
- group: build
  href: https://artifacts.apis.io/laserfiche/cli/laserfiche-cli.yml
  title: ''
  type: CLI
  url: cli/laserfiche-cli.yml
- group: auth
  href: https://artifacts.apis.io/laserfiche/authentication/laserfiche-authentication.yml
  title: ''
  type: Authentication
  url: authentication/laserfiche-authentication.yml
- group: design
  href: https://artifacts.apis.io/laserfiche/conformance/laserfiche-conformance.yml
  title: ''
  type: Conformance
  url: conformance/laserfiche-conformance.yml
- group: agent
  href: https://artifacts.apis.io/laserfiche/llms/laserfiche-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/laserfiche-llms.txt
- group: auth
  href: https://artifacts.apis.io/laserfiche/well-known/laserfiche-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/laserfiche-security.txt
- group: agent
  href: https://artifacts.apis.io/laserfiche/well-known/laserfiche-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/laserfiche-well-known.yml
- group: other
  href: https://artifacts.apis.io/laserfiche/hosts/laserfiche-hosts.yml
  title: ''
  type: Hosts
  url: hosts/laserfiche-hosts.yml
- group: other
  href: https://artifacts.apis.io/laserfiche/vendors/laserfiche-vendors.yml
  title: ''
  type: Vendors
  url: vendors/laserfiche-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.laserfiche.com/legal/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.laserfiche.com/
- group: auth
  title: ''
  type: Security
  url: https://www.laserfiche.com/products/trust-security/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.laserfiche.com/legal/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.laserfiche.com/resources/press-center/press/enterprise-security-launch/
- group: other
  title: ''
  type: Leadership
  url: https://www.laserfiche.com/leadership/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.laserfiche.com/products/whats-new/
- group: auth
  href: https://artifacts.apis.io/laserfiche/security/laserfiche-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/laserfiche-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/laserfiche/security/laserfiche-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/laserfiche-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.laserfiche.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.laserfiche.com/learn-support/developer-center/
- group: docs
  title: ''
  type: Documentation
  url: https://www.laserfiche.com/learn-support/developer-center/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.laserfiche.com/learn-support/developer-center/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.laserfiche.com/products/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.laserfiche.com/learn-support/
- group: company
  title: ''
  type: Blog
  url: https://www.laserfiche.com/blog/
coverage:
  checked: '2026-10-15'
  detail: Developer portal returns HTML rendered by JavaScript with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://developer.laserfiche.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Laserfiche delivers enterprise content management, document management, and process automation solutions that help organizations capture, manage, and secure information across people, processes, and systems. Their platform combines AI-powered data capture, workflow automation, records management, and compliance tools to improve productivity and governance for businesses of all sizes.
finops:
- has_sources: true
  method: derived
  name: Laserfiche Finops
  primary_unit: ''
  service_category: ''
  slug: laserfiche-finops
  template: true
image: https://www.laserfiche.com/wp-content/uploads/2024/12/hero-workflow-1024x720-2412.png
json_schemas:
- name: GetRepositoryV1RepositoriesRepoidTasksOperationtokenResponse
  property_count: 5
  slug: laserfiche-get-repository-v1-repositories-repoid-tasks-operationtoken-response
- name: GetRepositoryV1RepositoriesResponse
  property_count: 1
  slug: laserfiche-get-repository-v1-repositories-response
- name: GetRepositoryV2RepositoriesRepositoryidIdResponse
  property_count: 3
  slug: laserfiche-get-repository-v2-repositories-repositoryid-id-response
- name: PostOauthTokenRequest
  property_count: 6
  slug: laserfiche-post-oauth-token-request
- name: PostOauthTokenResponse
  property_count: 6
  slug: laserfiche-post-oauth-token-response
- name: PostRepositoryV1RepositoriesRepoidEntriesDestinationentryidL
  property_count: 2
  slug: laserfiche-post-repository-v1-repositories-repoid-entries-destinationentryid-l
- name: PostRepositoryV1RepositoriesRepoidEntriesDestinationentryidL2
  property_count: 1
  slug: laserfiche-post-repository-v1-repositories-repoid-entries-destinationentryid-l2
- name: PostRepositoryV2RepositoriesRAbcd1234UserareasRequest
  property_count: 3
  slug: laserfiche-post-repository-v2-repositories-rabcd1234-userareas-request
- name: PostRepositoryV2RepositoriesRAbcd1234UserareasResponse
  property_count: 4
  slug: laserfiche-post-repository-v2-repositories-rabcd1234-userareas-response
- name: PostRepositoryV2RepositoriesRepositoryidIdResponse
  property_count: 18
  slug: laserfiche-post-repository-v2-repositories-repositoryid-id-response
- name: PutRepositoryV2RepositoriesRAbc123EntriesEntrieidLinksReques
  property_count: 5
  slug: laserfiche-put-repository-v2-repositories-rabc123-entries-entrieid-links-reques
- name: PutRepositoryV2RepositoriesRAbc123EntriesEntrieidLinksRespon
  property_count: 14
  slug: laserfiche-put-repository-v2-repositories-rabc123-entries-entrieid-links-respon
jsonld:
- class_count: 20
  name: Laserfiche Context
  property_count: 43
  slug: laserfiche-context
layout: provider
modified: '2026-10-14'
name: Laserfiche
nav: Providers
network: true
overview: 'Laserfiche is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including OAuth API, Odata4 API, Repositories API, and 2 more. Tagged areas include Company, Enterprise Content Management, Document Management, Process Automation, and Artificial Intelligence.


  The Laserfiche catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Laserfiche''s developer surface includes CLI, authentication, changelog, documentation, getting-started guide, pricing, support, and 23 more developer resources.'
plans:
- name: Laserfiche Plans Pricing
  plan_count: 3
  slug: laserfiche-plans-pricing
- name: Laserfiche Price Estimates
  plan_count: 0
  slug: laserfiche-price-estimates
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Laserfiche API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: laserfiche-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 38.1
    discoverability: 71.4
    operational_transparency: 21.1
  previous_composite: 47.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/laserfiche/laserfiche-2026-11-03T134645.png
security:
- kind: authentication
  name: Laserfiche Authentication
  slug: laserfiche-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Laserfiche Domain Security
  slug: laserfiche-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Laserfiche Vulnerability Disclosure
  slug: laserfiche-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: laserfiche
tags:
- Company
- Enterprise Content Management
- Document Management
- Process Automation
- Artificial Intelligence
website: https://www.laserfiche.com
---
