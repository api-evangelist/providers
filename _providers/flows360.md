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
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.1
  scored_at: '2026-11-06'
api_count: 4
apis:
- baseURL: https://your-metabase-instance.com
  baseurl_source: spec
  description: Integration documentation for Flows360 provides technical references and guides to implement connected workflows.
  name: Flows360 API
  slug: flows360-api
- baseURL: https://your-metabase-instance.com
  baseurl_source: declared
  description: The Purchase Orders API from Flows360 — 1 operation(s) for purchase orders.
  name: Flows360 Purchase Orders API
  slug: flows360-purchase-orders-api
- baseURL: https://your-metabase-instance.com
  baseurl_source: declared
  description: The Session API from Flows360 — 1 operation(s) for session.
  name: Flows360 Session API
  slug: flows360-session-api
- baseURL: https://your-metabase-instance.com
  baseurl_source: declared
  description: The Suppliers API from Flows360 — 1 operation(s) for suppliers.
  name: Flows360 Suppliers API
  slug: flows360-suppliers-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/flows360/plans/flows360-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flows360-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flows360/rules/flows360-rules.yml
  title: ''
  type: Spectral
  url: rules/flows360-rules.yml
- group: design
  href: https://artifacts.apis.io/flows360/json-ld/flows360-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flows360-context.jsonld
- group: design
  href: https://artifacts.apis.io/flows360/vocabulary/flows360-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flows360-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/flows360/data-model/flows360-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flows360-data-model.yml
- group: operate
  href: https://artifacts.apis.io/flows360/changelog/flows360-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flows360-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.flows360.co/platform/security-governance/
- group: design
  href: https://artifacts.apis.io/flows360/conformance/flows360-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flows360-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flows360/llms/flows360-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flows360-llms.txt
- group: agent
  href: https://artifacts.apis.io/flows360/well-known/flows360-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flows360-well-known.yml
- group: other
  href: https://artifacts.apis.io/flows360/hosts/flows360-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flows360-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.flows360.co/integrations/webhook/
- group: operate
  title: ''
  type: Support
  url: https://support.flows360.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.flows360.co/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flows360
- group: auth
  href: https://artifacts.apis.io/flows360/security/flows360-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flows360-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/flows360/security/flows360-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flows360-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flows360.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flows360.co/docs/
- group: company
  title: ''
  type: Blog
  url: https://www.flows360.co/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flows360.co/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flows360.co/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flows360.co/terms-of-service/
coverage:
  checked: '2026-10-16'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.flows360.co/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Flows360 provides a comprehensive workflow automation platform that enables businesses to design, execute, and monitor complex processes across multiple systems. The solution offers a visual builder, extensive integrations, real-time analytics, and robust security features, helping organizations streamline operations, reduce manual effort, and improve efficiency. With a focus on scalability and flexibility, Flows360 serves enterprises across various industries, delivering customizable automation capabilities and enterprise-grade support.
finops:
- has_sources: true
  method: derived
  name: Flows360 Finops
  primary_unit: seat
  service_category: ''
  slug: flows360-finops
  template: false
image: https://www.flows360.co/wp-content/uploads/2026/03/cropped-1c.-Full-Colour-Logo-2000pxl-NoBackGround-PNG-300x88.png
json_schemas:
- name: PostApiSessionRequest
  property_count: 2
  slug: flows360-post-api-session-request
- name: PostApiSessionResponse
  property_count: 1
  slug: flows360-post-api-session-response
jsonld:
- class_count: 2
  name: Flows360 Context
  property_count: 3
  slug: flows360-context
layout: provider
modified: '2026-10-16'
name: Flows360
nav: Providers
network: true
overview: 'Flows360 is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Purchase Orders API, Session API, and 2 more. Tagged areas include Company, Automation, Workflows, Integration, and Software-as-a-Service.


  The Flows360 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Flows360''s developer surface includes changelog, support, getting-started guide, documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Flows360 Plans Pricing
  plan_count: 3
  slug: flows360-plans-pricing
- name: Flows360 Price Estimates
  plan_count: 0
  slug: flows360-price-estimates
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Flows360 API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: flows360-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 67.1
    contract_governance: 22.0
    contract_quality: 19.4
    developer_ergonomics: 14.3
    discoverability: 69.6
    operational_transparency: 22.4
  previous_composite: 42.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/flows360/flows360-2026-11-03T132201.png
security:
- kind: domain-security
  name: Flows360 Domain Security
  slug: flows360-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Flows360 Trust Center
  slug: flows360-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: flows360
tags:
- Company
- Automation
- Workflows
- Integration
- Software-as-a-Service
website: https://www.flows360.co/
---
