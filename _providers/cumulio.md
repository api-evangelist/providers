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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: The Authorize API from Cumulio — 1 operation(s) for authorize.
  name: Cumulio Authorize API
  slug: cumulio-authorize-api
- description: The Datasets API from Cumulio — 1 operation(s) for datasets.
  name: Cumulio Datasets API
  slug: cumulio-datasets-api
- description: The Exchange API from Cumulio — 1 operation(s) for exchange.
  name: Cumulio Exchange API
  slug: cumulio-exchange-api
- description: The Query API from Cumulio — 1 operation(s) for query.
  name: Cumulio Query API
  slug: cumulio-query-api
artifact_total: 10
asyncapis:
- description: ''
  name: Cumulio Webhooks
  slug: cumulio-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/rate-limits/cumulio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cumulio-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/plans/cumulio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cumulio-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/rules/cumulio-rules.yml
  title: ''
  type: Spectral
  url: rules/cumulio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/asyncapi/cumulio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cumulio-webhooks.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.luzmo.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/conformance/cumulio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cumulio-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/llms/cumulio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cumulio-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/well-known/cumulio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cumulio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/hosts/cumulio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cumulio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/vendors/cumulio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cumulio-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/packages/cumulio-packages.yml
  title: ''
  type: SDKs
  url: packages/cumulio-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/packages/cumulio-packages.yml
  title: ''
  type: Packages
  url: packages/cumulio-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.luzmo.com/information-pages/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.luzmo.com/signup
- group: auth
  title: ''
  type: Security
  url: https://www.luzmo.com/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.luzmo.com/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.luzmo.com/information-pages/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.luzmo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.luzmo.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developer.luzmo.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/security/cumulio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cumulio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cumulio/refs/heads/main/security/cumulio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cumulio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.luzmo.com
coverage:
  checked: '2026-10-12'
  detail: Developer documentation at https://developer.luzmo.com renders via JavaScript and provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 404
    url: https://developer.luzmo.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: 'Cumulio is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: https://www.luzmo.com/assets/og/default.en.png
layout: provider
modified: '2026-10-12'
name: Cumulio
nav: Providers
network: true
overview: 'Cumulio is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Authorize API, Datasets API, Exchange API, and 1 more. Tagged areas include Company.


  The Cumulio catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cumulio''s developer surface includes signup flow, pricing, engineering blog, documentation, and 19 more developer resources.'
plans:
- name: Cumulio Plans Pricing
  plan_count: 1
  slug: cumulio-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Cumulio Rate Limits
  slug: cumulio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Cumulio API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: cumulio-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.5
    catalog_earned_first_party: 16.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 17.3
    developer_ergonomics: 19.0
    discoverability: 51.8
    operational_transparency: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Cumulio Domain Security
  slug: cumulio-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Cumulio Trust Center
  slug: cumulio-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: cumulio
tags:
- Company
website: https://www.luzmo.com
---
