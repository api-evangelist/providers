---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-03'
api_count: 1
apis:
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The AuthenticationMethodKubernetesService API from Bito — 1 operation(s) for authenticationmethodkubernetesservice.
  name: Bito Authentication Method Kubernetes Service API
  slug: bito-authenticationmethodkubernetesservice-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The AuthenticationMethodOIDCService API from Bito — 2 operation(s) for authenticationmethodoidcservice.
  name: Bito Authentication Method OIDC Service API
  slug: bito-authenticationmethodoidcservice-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The AuthenticationMethodTokenService API from Bito — 1 operation(s) for authenticationmethodtokenservice.
  name: Bito Authentication Method Token Service API
  slug: bito-authenticationmethodtokenservice-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The EvaluationService API from Bito — 3 operation(s) for evaluationservice.
  name: Bito Evaluation Service API
  slug: bito-evaluationservice-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Flipt API from Bito — 18 operation(s) for flipt.
  name: Bito Flipt API
  slug: bito-flipt-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The OFREPService API from Bito — 3 operation(s) for ofrepservice.
  name: Bito OFREP Service API
  slug: bito-ofrepservice-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Authentication Service API from Bito — 4 operation(s) for authentication service.
  name: Bito Authentication Service API
  slug: bito-authentication-service-api
artifact_total: 12
asyncapis:
- description: ''
  name: Bito Webhooks
  slug: bito-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/plans/bito-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bito-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/rules/bito-rules.yml
  title: ''
  type: Spectral
  url: rules/bito-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/json-ld/bito-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bito-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/vocabulary/bito-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bito-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/asyncapi/bito-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bito-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/data-model/bito-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bito-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/changelog/bito-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bito-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/conformance/bito-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bito-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/overlays/bito-flipt-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bito-flipt-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/llms/bito-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bito-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/well-known/bito-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bito-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/hosts/bito-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bito-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/vendors/bito-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bito-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/packages/bito-packages.yml
  title: ''
  type: SDKs
  url: packages/bito-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/packages/bito-packages.yml
  title: ''
  type: Packages
  url: packages/bito-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bito.ai/
- group: auth
  title: ''
  type: Security
  url: https://bito.ai/enterprise/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bito.ai/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bito.ai/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bito/refs/heads/main/security/bito-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bito-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bito.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bito.ai
- group: company
  title: ''
  type: Blog
  url: https://bito.ai/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitbito
- group: commercial
  title: ''
  type: Pricing
  url: https://bito.ai/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bito.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bito.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://status.bito.ai
coverage:
  checked: '2026-09-28'
  detail: Documentation at https://docs.bito.ai is rendered via Gitbook and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.bito.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bito.ai provides an AI model routing platform that helps developers select and integrate large language models like Claude, Code, Cursor, and Codex. Their suite includes context engineering, autonomous agents, design and scoping tools, grounded coding, and AI code review agents. Bito aims to reduce development costs by optimizing model selection and offering a unified interface for AI-powered software engineering tasks.
image: https://bito.ai/wp-content/uploads/2026/08/Option-A-1-2-1.webp
jsonld:
- class_count: 57
  name: Bito Context
  property_count: 69
  slug: bito-context
layout: provider
modified: '2026-09-28'
name: Bito
nav: Providers
network: true
overview: 'Bito publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication Method Kubernetes Service API, Authentication Method OIDC Service API, Authentication Method Token Service API, and 4 more. Tagged areas include Company, Artificial Intelligence, Developer Tools, Software-as-a-Service, and Machine Learning.


  The Bito catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bito''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, support, and 22 more developer resources.'
plans:
- name: Bito Plans Pricing
  plan_count: 4
  slug: bito-plans-pricing
random_paper: 12
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bito API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: bito-rules
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.8
    catalog_earned_first_party: 12.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 54.4
    developer_ergonomics: 35.7
    discoverability: 55.4
    operational_transparency: 39.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Bito Domain Security
  slug: bito-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bito
tags:
- Company
- Artificial Intelligence
- Developer Tools
- Software-as-a-Service
- Machine Learning
website: https://bito.ai
---
