---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.chronoloq.com
  baseurl_source: spec
  description: Chronoloq API provides AI risk assessment and security scoring endpoints as documented.
  name: Chronoloq API
  slug: chronoloq-api
- baseURL: https://api.chronoloq.com
  baseurl_source: declared
  description: The Scans API from Chronoloq — 1 operation(s) for scans.
  name: Chronoloq Scans API
  slug: chronoloq-scans-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/chronoloq/plans/chronoloq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chronoloq-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chronoloq/rules/chronoloq-rules.yml
  title: ''
  type: Spectral
  url: rules/chronoloq-rules.yml
- group: design
  href: https://artifacts.apis.io/chronoloq/json-ld/chronoloq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chronoloq-context.jsonld
- group: design
  href: https://artifacts.apis.io/chronoloq/vocabulary/chronoloq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chronoloq-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chronoloq/data-model/chronoloq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chronoloq-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://chronoloq.com/trust
- group: design
  href: https://artifacts.apis.io/chronoloq/conformance/chronoloq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chronoloq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chronoloq/llms/chronoloq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chronoloq-llms.txt
- group: other
  href: https://artifacts.apis.io/chronoloq/a2a/chronoloq-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chronoloq-a2a.yml
- group: other
  href: https://artifacts.apis.io/chronoloq/hosts/chronoloq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chronoloq-hosts.yml
- group: other
  href: https://artifacts.apis.io/chronoloq/vendors/chronoloq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chronoloq-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://chronoloq.com/security
- group: auth
  href: https://artifacts.apis.io/chronoloq/security/chronoloq-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chronoloq-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/chronoloq/security/chronoloq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chronoloq-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chronoloq/security/chronoloq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chronoloq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chronoloq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://chronoloq.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://chronoloq.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://chronoloq.com/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://chronoloq.com/contact
- group: company
  title: ''
  type: Blog
  url: https://chronoloq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://chronoloq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://chronoloq.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chronoloq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chronoloq.com/privacy
coverage:
  checked: '2026-10-16'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 525
    url: https://api.chronoloq.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Chronoloq provides AI risk assessment and security scoring for enterprises, offering a free AI security audit, detailed risk reports, and compliance guidance across finance, healthcare, education, and e‑commerce sectors. Their platform helps organizations understand and mitigate AI‑related security risks with actionable insights and a proprietary Chronoloq Score.
finops:
- has_sources: true
  method: derived
  name: Chronoloq Finops
  primary_unit: ''
  service_category: ''
  slug: chronoloq-finops
  template: true
image: https://chronoloq.com/og-banner.png
json_schemas:
- name: PostV1ScansRequest
  property_count: 1
  slug: chronoloq-post-v1-scans-request
jsonld:
- class_count: 1
  name: Chronoloq Context
  property_count: 1
  slug: chronoloq-context
layout: provider
modified: '2026-10-16'
name: Chronoloq
nav: Providers
network: true
overview: 'Chronoloq is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Scans API, and 1 more. Tagged areas include Company, Artificial Intelligence, Security, Risk Assessment, and Enterprise.


  The Chronoloq catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chronoloq''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Chronoloq Plans Pricing
  plan_count: 1
  slug: chronoloq-plans-pricing
- name: Chronoloq Price Estimates
  plan_count: 0
  slug: chronoloq-price-estimates
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Chronoloq API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: chronoloq-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 17.9
    discoverability: 64.3
    operational_transparency: 5.3
  previous_composite: 39.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
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
screenshot: https://apis.io/screenshots/chronoloq/chronoloq-2026-11-03T124118.png
security:
- kind: domain-security
  name: Chronoloq Domain Security
  slug: chronoloq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chronoloq Vulnerability Disclosure
  slug: chronoloq-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Chronoloq Trust Center
  slug: chronoloq-trust-center
  summary_line: PCI DSS, HIPAA
slug: chronoloq
tags:
- Company
- Artificial Intelligence
- Security
- Risk Assessment
- Enterprise
website: https://chronoloq.com/
---
