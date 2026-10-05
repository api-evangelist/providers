---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-04'
api_count: 5
apis:
- description: REST API for managing Zscaler Internet Access policies, URL filtering, cloud sandbox, DLP, location and user provisioning, and reporting on web traffic and threats across the Zscaler Cloud platform.
  name: Zscaler Internet Access (ZIA) API
  slug: zia-api
- description: REST API for managing Zscaler Private Access (ZPA) configurations including segment groups, application segments, connector groups, SCIM provisioning, policies, and access logs.
  name: Zscaler Private Access (ZPA) API
  slug: zpa-api
- baseURL: https://zsapi.zscaler.net/api/v1
  baseurl_source: declared
  description: The App Views API from Zscaler — 4 operation(s) for app views.
  name: Zscaler App Views API
  slug: zscaler-app-views-api
- baseURL: https://zsapi.zscaler.net/api/v1
  baseurl_source: declared
  description: The Apps API from Zscaler — 3 operation(s) for apps.
  name: Zscaler Apps API
  slug: zscaler-apps-api
- baseURL: https://zsapi.zscaler.net/api/v1
  baseurl_source: declared
  description: The Posture API from Zscaler — 9 operation(s) for posture.
  name: Zscaler Posture API
  slug: zscaler-posture-api
artifact_total: 17
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/rate-limits/zscaler-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zscaler-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/plans/zscaler-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zscaler-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/rules/zscaler-rules.yml
  title: ''
  type: Spectral
  url: rules/zscaler-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/json-ld/zscaler-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zscaler-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/vocabulary/zscaler-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zscaler-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/data-model/zscaler-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zscaler-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/conformance/zscaler-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zscaler-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/llms/zscaler-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zscaler-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/well-known/zscaler-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zscaler-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/hosts/zscaler-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zscaler-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/vendors/zscaler-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zscaler-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.zscaler.com/blogs/cybersecurity-best-practices/webhooks
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.zscaler.com/
- group: auth
  title: ''
  type: Security
  url: https://www.zscaler.com/security/vulnerability-disclosure-program
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zscaler.com/blogs/company-news/privacy-vs-encryption
- group: other
  title: ''
  type: Leadership
  url: https://www.zscaler.com/company/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://help.zscaler.com/secure-ai-apps-infra/about-ai-red-teaming-onboarding-agent
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/security/zscaler-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zscaler-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/security/zscaler-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zscaler-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zscaler
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zscaler
- group: company
  title: ''
  type: Website
  url: https://www.zscaler.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.zscaler.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zscaler.com/pricing-and-plans
- group: start
  title: ''
  type: Signup
  url: https://www.zscaler.com/products/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.zscaler.com/blogs
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://config.private.zscaler.com/mcp
  - status: 200
    url: https://www.zscaler.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-11'
description: Zscaler is a cloud security platform delivering Zero Trust Exchange services including Zscaler Internet Access (ZIA), Zscaler Private Access (ZPA), and Zscaler Digital Experience (ZDX). Zscaler exposes REST APIs across its product suite for configuration, policy management, and reporting, authenticated via API keys, OAuth 2.0, or session-based authentication depending on the product and cloud (zsapi).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zscaler.png
json_schemas:
- name: GetAppViewsListResponse
  property_count: 5
  slug: zscaler-get-app-views-list-response
- name: GetV1AppViewsListResponse
  property_count: 5
  slug: zscaler-get-v1-app-views-list-response
- name: PostPostureControlsRequest
  property_count: 2
  slug: zscaler-post-posture-controls-request
- name: PostV1PostureControlsRequest
  property_count: 2
  slug: zscaler-post-v1-posture-controls-request
- name: PutPostureAssetsStatusRequest
  property_count: 3
  slug: zscaler-put-posture-assets-status-request
- name: PutV1PosturePostureidStatusRequest
  property_count: 3
  slug: zscaler-put-v1-posture-postureid-status-request
jsonld:
- class_count: 21
  name: Zscaler Context
  property_count: 20
  slug: zscaler-context
layout: provider
modified: '2026-05-11'
name: Zscaler
nav: Providers
network: true
overview: 'Zscaler publishes 5 APIs on the [APIs.io](https://apis.io/) network, including App Views API, Apps API, Posture API, and 2 more. Tagged areas include Cloud Security, Zero Trust, SASE, Network Security, and SWG.


  The Zscaler catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zscaler''s developer surface includes getting-started guide, documentation, pricing, signup flow, engineering blog, and 21 more developer resources.'
plans:
- name: Zscaler Plans Pricing
  plan_count: 0
  slug: zscaler-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Zscaler Rate Limits
  slug: zscaler-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Zscaler API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: zscaler-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.1
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 24.2
    developer_ergonomics: 14.3
    discoverability: 80.4
    operational_transparency: 52.6
  previous_composite: 12.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/screenshots/zscaler-2026-06-20T201955.png
security:
- kind: domain-security
  name: Zscaler Domain Security
  slug: zscaler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zscaler Vulnerability Disclosure
  slug: zscaler-vulnerability-disclosure
  summary_line: Bugcrowd
slug: zscaler
tags:
- Cloud Security
- Zero Trust
- SASE
- Network Security
- SWG
website: https://www.zscaler.com/
---
