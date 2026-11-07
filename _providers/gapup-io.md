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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Gapup platform (no machine-readable contract discovered)
  name: Gapup API
  slug: gapup-api
- description: 'gapup-io API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: gapup-io API
  slug: gapup-io-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/gapup-io/plans/gapup-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gapup-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gapup-io/rules/gapup-io-rules.yml
  title: ''
  type: Spectral
  url: rules/gapup-io-rules.yml
- group: design
  href: https://artifacts.apis.io/gapup-io/json-ld/gapup-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gapup-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/gapup-io/vocabulary/gapup-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gapup-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gapup-io/data-model/gapup-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gapup-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/gapup-io/changelog/gapup-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gapup-io-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gapup.io/security
- group: design
  href: https://artifacts.apis.io/gapup-io/conformance/gapup-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gapup-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gapup-io/llms/gapup-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gapup-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/gapup-io/well-known/gapup-io-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gapup-io-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/gapup-io/well-known/gapup-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gapup-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/gapup-io/hosts/gapup-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gapup-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/gapup-io/vendors/gapup-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gapup-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://hub.gapup.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://mcp.gapup.io/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://hub.gapup.io/blog
- group: auth
  href: https://artifacts.apis.io/gapup-io/security/gapup-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gapup-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gapup-io/security/gapup-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gapup-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gapup-io/security/gapup-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gapup-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gapup.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gapup.io/x402
- group: docs
  title: ''
  type: APIReference
  url: https://www.gapup.io/x402
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gapup.io/promesse
- group: operate
  title: ''
  type: Support
  url: https://www.gapup.io/aide/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gapup.io/pricing/launch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gapup.io/legal/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gapup.io/legal/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation is public but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL spec was found.
  evidence:
  - status: 0
    url: https://api.gapup.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Gapup.io provides an AI‑powered hub that helps businesses understand and optimise their costs and revenues. The platform offers modular expert agents for finance, operations, compliance and more, delivering actionable insights, automated reporting and ROI‑focused recommendations. It targets enterprises seeking data‑driven decision‑making and flexible, scalable AI solutions across multiple departments.
image: https://image.pollinations.ai/prompt/gapup%20hub%20saas%20banner%20tech%20modern%20purple%20gold%20gradient%20cinematic?width=1200&height=630&nologo=true&seed=905
json_schemas:
- name: PostMcpRequest
  property_count: 6
  slug: gapup-io-post-mcp-request
jsonld:
- class_count: 1
  name: Gapup Io Context
  property_count: 6
  slug: gapup-io-context
layout: provider
modified: '2026-10-30'
name: gapup-io
nav: Providers
network: true
overview: 'gapup-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Finance, Compliance, and Enterprise.


  The gapup-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  gapup-io''s developer surface includes changelog, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 20 more developer resources.'
plans:
- name: Gapup Io Plans Pricing
  plan_count: 7
  slug: gapup-io-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: gapup-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: gapup-io-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.2
    catalog_earned_first_party: 12.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 59.2
    contract_governance: 35.6
    contract_quality: 17.4
    developer_ergonomics: 17.9
    discoverability: 55.4
    operational_transparency: 13.2
  previous_composite: 42.5
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
      standard: ccpa
    jurisdictions_satisfied: 2
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
screenshot: https://apis.io/screenshots/gapup-io/gapup-io-2026-11-03T132522.png
security:
- kind: domain-security
  name: Gapup Io Domain Security
  slug: gapup-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gapup Io Vulnerability Disclosure
  slug: gapup-io-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Gapup Io Trust Center
  slug: gapup-io-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR
slug: gapup-io
tags:
- Artificial Intelligence
- Finance
- Compliance
- Enterprise
website: https://www.gapup.io/
---
