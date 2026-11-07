---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Ivoyant API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Ivoyant API
  slug: koodisi-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/koodisi/plans/koodisi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/koodisi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/koodisi/rules/koodisi-rules.yml
  title: ''
  type: Spectral
  url: rules/koodisi-rules.yml
- group: design
  href: https://artifacts.apis.io/koodisi/json-ld/koodisi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/koodisi-context.jsonld
- group: design
  href: https://artifacts.apis.io/koodisi/vocabulary/koodisi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/koodisi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/koodisi/data-model/koodisi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/koodisi-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://koodisi.com/security
- group: auth
  href: https://artifacts.apis.io/koodisi/authentication/koodisi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/koodisi-authentication.yml
- group: operate
  href: https://artifacts.apis.io/koodisi/lifecycle/koodisi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/koodisi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/koodisi/lifecycle/koodisi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/koodisi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/koodisi/conformance/koodisi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/koodisi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/koodisi/llms/koodisi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/koodisi-llms.txt
- group: other
  href: https://artifacts.apis.io/koodisi/hosts/koodisi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/koodisi-hosts.yml
- group: other
  href: https://artifacts.apis.io/koodisi/vendors/koodisi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/koodisi-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://koodisi.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://koodisi.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.koodisi.com/administering-koodisi/configuring-event-notifiers/azure-event-grid-setup-guide
- group: auth
  href: https://artifacts.apis.io/koodisi/security/koodisi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/koodisi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/koodisi/security/koodisi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/koodisi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://koodisi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.koodisi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://koodisi.com/developer-program
- group: commercial
  title: ''
  type: Pricing
  url: https://koodisi.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://koodisi.com/blog
- group: operate
  title: ''
  type: Support
  url: https://koodisi.com/contact
coverage:
  checked: '2026-10-18'
  detail: Documentation site renders via JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.koodisi.com/api-manager/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Ivoyant, operating under the brand Koodisi, provides an enterprise iPaaS and workflow automation platform. It enables businesses to build, deploy, and govern integrations across APIs, MCP tools, and AI agents from a single governed platform. Features include a visual workflow builder, API management, security controls, observability, and AI-ready interfaces, targeting complex integration needs for modern enterprises.
image: https://koodisi.com/og-default.webp
json_schemas:
- name: GetApiV10ChannelsChannelidWebhooksResponse
  property_count: 4
  slug: koodisi-get-api-v10-channels-channelid-webhooks-response
jsonld:
- class_count: 1
  name: Koodisi Context
  property_count: 4
  slug: koodisi-context
layout: provider
modified: '2026-10-18'
name: Ivoyant
nav: Providers
network: true
overview: 'Ivoyant is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Integration Platform, iPaaS, Workflow Automation, Enterprise Integration, and API Management.


  The Ivoyant catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ivoyant''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, support, and 18 more developer resources.'
plans:
- name: Koodisi Plans Pricing
  plan_count: 1
  slug: koodisi-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Ivoyant API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: koodisi-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 55.4
    catalog_earned_first_party: 8.0
    catalog_gap: 59.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 43.4
    contract_governance: 19.7
    contract_quality: 16.4
    developer_ergonomics: 31.0
    discoverability: 64.3
    operational_transparency: 13.2
  previous_composite: 37.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/koodisi/koodisi-2026-11-03T134516.png
security:
- kind: authentication
  name: Koodisi Authentication
  slug: koodisi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Koodisi Domain Security
  slug: koodisi-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Koodisi Trust Center
  slug: koodisi-trust-center
  summary_line: SOC 2, ISO 27001
slug: koodisi
tags:
- Integration Platform
- iPaaS
- Workflow Automation
- Enterprise Integration
- API Management
- Governance
- AI Agents
- Multi-Tenant
website: https://koodisi.com/
---
