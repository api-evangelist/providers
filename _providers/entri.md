---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Entri provides a domain lifecycle platform with APIs for activation, purchasing, monitoring, and security of domains.
  name: Entri API
  slug: entri-api-2
- description: 'Entri API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Entri API
  slug: entri-api
artifact_total: 14
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.entri.com/getting-started
- group: commercial
  href: https://artifacts.apis.io/entri/plans/entri-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/entri-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/entri/rules/entri-rules.yml
  title: ''
  type: Spectral
  url: rules/entri-rules.yml
- group: design
  href: https://artifacts.apis.io/entri/json-ld/entri-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/entri-context.jsonld
- group: design
  href: https://artifacts.apis.io/entri/vocabulary/entri-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/entri-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/entri/data-model/entri-data-model.yml
  title: ''
  type: DataModel
  url: data-model/entri-data-model.yml
- group: design
  href: https://artifacts.apis.io/entri/conventions/entri-conventions.yml
  title: ''
  type: Conventions
  url: conventions/entri-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.entri.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/entri/authentication/entri-authentication.yml
  title: ''
  type: Authentication
  url: authentication/entri-authentication.yml
- group: design
  href: https://artifacts.apis.io/entri/conformance/entri-conformance.yml
  title: ''
  type: Conformance
  url: conformance/entri-conformance.yml
- group: agent
  href: https://artifacts.apis.io/entri/llms/entri-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/entri-llms.txt
- group: other
  href: https://artifacts.apis.io/entri/a2a/entri-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/entri-a2a.yml
- group: auth
  href: https://artifacts.apis.io/entri/well-known/entri-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/entri-security.txt
- group: auth
  href: https://artifacts.apis.io/entri/well-known/entri-entri-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/entri-entri-security.txt
- group: agent
  href: https://artifacts.apis.io/entri/well-known/entri-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/entri-well-known.yml
- group: other
  href: https://artifacts.apis.io/entri/hosts/entri-hosts.yml
  title: ''
  type: Hosts
  url: hosts/entri-hosts.yml
- group: other
  href: https://artifacts.apis.io/entri/vendors/entri-vendors.yml
  title: ''
  type: Vendors
  url: vendors/entri-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.entri.com/
- group: auth
  href: https://artifacts.apis.io/entri/security/entri-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/entri-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/entri/security/entri-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/entri-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://entri.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.entri.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.entri.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.entri.com/
- group: operate
  title: ''
  type: Support
  url: https://contact.entri.com/
- group: company
  title: ''
  type: Blog
  url: https://www.entri.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.entri.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://onboarding.entri.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.entri.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.entri.com/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/entri/workspace
coverage:
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://developers.entri.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Entri provides a domain lifecycle platform that enables developers to connect, buy, sell, and monitor domains via APIs. Their suite includes Entri Activate, Connect, Sell, Monitor, Secure, and Power, offering seamless integration of domain management into products. The company focuses on simplifying domain operations for developers and businesses, offering APIs for activation, purchasing, monitoring, and security, with detailed documentation and support resources.
image: https://framerusercontent.com/assets/LHPe9Ei5uvTjH5lABqkGDrExZw.png
json_schemas:
- name: GetMonitorDomainsDomainnameResponse
  property_count: 14
  slug: entri-get-monitor-domains-domainname-response
- name: GetSellDomainsResponse
  property_count: 8
  slug: entri-get-sell-domains-response
- name: GetSellJobidStatusResponse
  property_count: 5
  slug: entri-get-sell-jobid-status-response
- name: PostCheckdomainResponse
  property_count: 13
  slug: entri-post-checkdomain-response
- name: PostConnectAsyncRequest
  property_count: 5
  slug: entri-post-connect-async-request
- name: PostSslRequest
  property_count: 3
  slug: entri-post-ssl-request
jsonld:
- class_count: 40
  name: Entri Context
  property_count: 58
  slug: entri-context
layout: provider
modified: '2026-10-20'
name: Entri
nav: Providers
network: true
overview: 'Entri is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Domain, Integration, and Software-as-a-Service.


  The Entri catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Entri''s developer surface includes getting-started guide, authentication, documentation, API reference, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Entri Plans Pricing
  plan_count: 4
  slug: entri-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Entri API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: entri-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 29.6
    developer_ergonomics: 36.9
    discoverability: 55.4
    operational_transparency: 13.2
  previous_composite: 48.2
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/entri/entri-2026-11-03T131537.png
security:
- kind: authentication
  name: Entri Authentication
  slug: entri-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Entri Domain Security
  slug: entri-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Entri Vulnerability Disclosure
  slug: entri-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: entri
tags:
- Company
- Domain
- Integration
- Software-as-a-Service
website: https://entri.com/
---
