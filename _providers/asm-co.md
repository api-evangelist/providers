---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.assembly.com
  baseurl_source: declared
  description: 'Assembly API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Assembly API
  slug: asm-co-api
artifact_total: 9
asyncapis:
- description: ''
  name: Asm Co Webhooks
  slug: asm-co-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/asm-co/rate-limits/asm-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/asm-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/asm-co/plans/asm-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asm-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asm-co/rules/asm-co-rules.yml
  title: ''
  type: Spectral
  url: rules/asm-co-rules.yml
- group: design
  href: https://artifacts.apis.io/asm-co/json-ld/asm-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asm-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/asm-co/vocabulary/asm-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asm-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/asm-co/asyncapi/asm-co-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/asm-co-webhooks.yml
- group: design
  href: https://artifacts.apis.io/asm-co/data-model/asm-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asm-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/asm-co/conventions/asm-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/asm-co-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.assembly.com/
- group: design
  href: https://artifacts.apis.io/asm-co/conformance/asm-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asm-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asm-co/llms/asm-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asm-co-llms.txt
- group: other
  href: https://artifacts.apis.io/asm-co/a2a/asm-co-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/asm-co-a2a.yml
- group: other
  href: https://artifacts.apis.io/asm-co/hosts/asm-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asm-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/asm-co/vendors/asm-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asm-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assembly.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.assembly.com
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.assembly.com/signup?referrer=studio-pricing
- group: auth
  title: ''
  type: Security
  url: https://assembly.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://assembly.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/assemblycom
- group: company
  title: ''
  type: Blog
  url: https://assembly.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://assembly.com/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://assembly.com/docs/getting-started/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.assembly.com/
- group: auth
  href: https://artifacts.apis.io/asm-co/security/asm-co-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/asm-co-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/asm-co/security/asm-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asm-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assembly.com/
created: '2026-10-24'
description: Assembly provides a low-code platform that enables firms to build client portals, CRM systems, and AI‑enhanced applications without extensive coding. Their solution combines customizable templates, integrated payment processing, and robust security features, allowing businesses to streamline client onboarding, collaboration, and billing within a single branded experience. Backed by Y Combinator, Assembly targets professional services firms seeking rapid digital transformation.
image: https://assembly.com/og.jpg
json_schemas:
- name: GetV1InvoicesResponse
  property_count: 25
  slug: asm-co-get-v1-invoices-response
jsonld:
- class_count: 1
  name: Asm Co Context
  property_count: 25
  slug: asm-co-context
layout: provider
modified: '2026-10-24'
name: Assembly
nav: Providers
network: true
overview: 'Assembly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Low-Code, CRM, Artificial Intelligence, and Software-as-a-Service.


  The Assembly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Assembly''s developer surface includes signup flow, pricing, engineering blog, API reference, getting-started guide, documentation, and 21 more developer resources.'
plans:
- name: Asm Co Plans Pricing
  plan_count: 1
  slug: asm-co-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Asm Co Rate Limits
  slug: asm-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Assembly API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: asm-co-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 76.2
    catalog_earned_first_party: 20.0
    catalog_gap: 38.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 28.8
    developer_ergonomics: 15.5
    discoverability: 73.2
    operational_transparency: 55.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.3
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
    score: 14.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/asm-co/asm-co-2026-11-03T121204.png
security:
- kind: domain-security
  name: Asm Co Domain Security
  slug: asm-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Asm Co Trust Center
  slug: asm-co-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: asm-co
tags:
- Company
- Low-Code
- CRM
- Artificial Intelligence
- Software-as-a-Service
website: https://assembly.com/
---
