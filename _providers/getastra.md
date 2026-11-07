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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Astra Pentest API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Astra Pentest API
  slug: getastra-api
artifact_total: 9
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getastra.com/legal/terms
- group: commercial
  href: https://artifacts.apis.io/getastra/plans/getastra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getastra-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/getastra/rules/getastra-rules.yml
  title: ''
  type: Spectral
  url: rules/getastra-rules.yml
- group: design
  href: https://artifacts.apis.io/getastra/json-ld/getastra-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getastra-context.jsonld
- group: design
  href: https://artifacts.apis.io/getastra/vocabulary/getastra-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getastra-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getastra/data-model/getastra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getastra-data-model.yml
- group: auth
  href: https://artifacts.apis.io/getastra/security/getastra-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/getastra-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getastra/authentication/getastra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getastra-authentication.yml
- group: design
  href: https://artifacts.apis.io/getastra/conformance/getastra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getastra-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getastra/llms/getastra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getastra-llms.txt
- group: auth
  href: https://artifacts.apis.io/getastra/well-known/getastra-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getastra-security.txt
- group: auth
  href: https://artifacts.apis.io/getastra/well-known/getastra-my-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getastra-my-security.txt
- group: auth
  href: https://artifacts.apis.io/getastra/well-known/getastra-getastra-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getastra-getastra-security.txt
- group: auth
  href: https://artifacts.apis.io/getastra/well-known/getastra-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getastra-api-security.txt
- group: agent
  href: https://artifacts.apis.io/getastra/well-known/getastra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getastra-well-known.yml
- group: other
  href: https://artifacts.apis.io/getastra/hosts/getastra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getastra-hosts.yml
- group: other
  href: https://artifacts.apis.io/getastra/vendors/getastra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getastra-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getastra.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.getastra.com/articles/1929955147-integrate-slack-with-astra-s-orbitx
- group: docs
  title: ''
  type: Documentation
  url: https://help.getastra.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getastra
- group: auth
  href: https://artifacts.apis.io/getastra/security/getastra-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getastra-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getastra/security/getastra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getastra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getastra.com/
- group: operate
  title: ''
  type: Support
  url: https://help.getastra.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.getastra.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getastra.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.getastra.com/checkout
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getastra.com/privacy-policy
coverage:
  checked: '2026-10-18'
  detail: No machine‑readable OpenAPI, AsyncAPI, GraphQL or gRPC spec was found on the API host; attempts at common spec URLs returned 403 or 404.
  evidence:
  - status: 403
    url: https://api.getastra.com/openapi.json
  - status: 403
    url: https://api.getastra.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Astra Pentest provides an AI‑powered continuous penetration testing platform, offering PTaaS, DAST, API security scanning, and cloud vulnerability assessment. Their solutions scale with development velocity, covering web, mobile, API, cloud, and network applications across industries such as healthcare, SaaS, fintech, and insurance. The company emphasizes autonomous pentesting, detailed reporting, and integration capabilities for modern DevSecOps pipelines.
image: https://cdn.prod.website-files.com/5f80230f2eb0ba0ee5a95589/67766d0c625dd23855cd09eb_home%20dast.png
json_schemas:
- name: PostUsersRequest
  property_count: 4
  slug: getastra-post-users-request
- name: PostUsersResponse
  property_count: 5
  slug: getastra-post-users-response
jsonld:
- class_count: 2
  name: Getastra Context
  property_count: 7
  slug: getastra-context
layout: provider
modified: '2026-10-17'
name: Astra Pentest
nav: Providers
network: true
overview: 'Astra Pentest is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Penetration Testing, and Cloud.


  The Astra Pentest catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Astra Pentest''s developer surface includes authentication, getting-started guide, documentation, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Getastra Plans Pricing
  plan_count: 8
  slug: getastra-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Astra Pentest API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: getastra-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.8
    catalog_earned_first_party: 12.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 20.1
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 21.1
  previous_composite: 43.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/getastra/getastra-2026-11-03T132649.png
security:
- kind: authentication
  name: Getastra Authentication
  slug: getastra-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Getastra Domain Security
  slug: getastra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Getastra Vulnerability Disclosure
  slug: getastra-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: getastra
tags:
- Company
- Security
- Penetration Testing
- Cloud
website: https://www.getastra.com/
---
