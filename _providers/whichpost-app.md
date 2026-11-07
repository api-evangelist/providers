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
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Whichpost App Agentic Access
  operation_count: 3
  slug: whichpost-app-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: 'Practical guides for apps, clipping buyers and agencies that pay creators: what to pay, how to measure posts, and when to rebook or pause.'
  name: WhichPost API
  slug: whichpost-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/whichpost-app/agentic-access/whichpost-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/whichpost-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/whichpost-app/plans/whichpost-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/whichpost-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/whichpost-app/rules/whichpost-app-rules.yml
  title: ''
  type: Spectral
  url: rules/whichpost-app-rules.yml
- group: design
  href: https://artifacts.apis.io/whichpost-app/json-ld/whichpost-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/whichpost-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/whichpost-app/vocabulary/whichpost-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/whichpost-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/whichpost-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/whichpost-app/data-model/whichpost-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whichpost-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/whichpost-app/security/whichpost-app-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/whichpost-app-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/whichpost-app/errors/whichpost-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whichpost-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/whichpost-app/conformance/whichpost-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whichpost-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/whichpost-app/llms/whichpost-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whichpost-app-llms.txt
- group: build
  href: https://artifacts.apis.io/whichpost-app/mcp/whichpost-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/whichpost-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/whichpost-app/mcp/whichpost-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/whichpost-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/whichpost-app/well-known/whichpost-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/whichpost-app-security.txt
- group: agent
  href: https://artifacts.apis.io/whichpost-app/well-known/whichpost-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whichpost-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/whichpost-app/hosts/whichpost-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whichpost-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/whichpost-app/vendors/whichpost-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whichpost-app-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://whichpost.app/guides
- group: docs
  title: ''
  type: APIReference
  url: https://whichpost.app/llms.txt
- group: auth
  href: https://artifacts.apis.io/whichpost-app/security/whichpost-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/whichpost-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/whichpost-app/security/whichpost-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whichpost-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whichpost.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://whichpost.app/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whichpost.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whichpost.app/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://whichpost.app/analyze
- group: start
  title: ''
  type: SignUp
  url: https://whichpost.app/signin
created: '2026-10-30'
description: WhichPost is a SaaS platform that helps creators and brands understand which of their social media posts generate paying customers. By connecting a read‑only Stripe or RevenueCat key, the service reads checkout, trial, subscription and refund events and applies in‑house statistical models to estimate the number of paying customers attributable to each post. The platform offers a free analyzer that works without an account, and a paid workspace for ongoing campaign tracking. It emphasizes privacy by not storing personal identifiers and provides a clear pricing page. The service is hosted at whichpost.app.
image: https://whichpost.app/assets/og/default.png?v=5afd54ed77
jsonld:
- class_count: 1
  name: Whichpost App Context
  property_count: 1
  slug: whichpost-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at whichpost.app.
  name: whichpost-app MCP Server
  slug: whichpost-app-mcp-yml
modified: '2026-10-30'
name: whichpost-app
nav: Providers
network: true
overview: 'whichpost-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Creator Economy, Revenue, and Software-as-a-Service.


  The whichpost-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  whichpost-app''s developer surface includes documentation, API reference, pricing, getting-started guide, signup flow, and 22 more developer resources.'
plans:
- name: Whichpost App Plans Pricing
  plan_count: 4
  slug: whichpost-app-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: whichpost-app API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: whichpost-app-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 20.7
    discoverability: 75.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/whichpost-app/whichpost-app-2026-11-03T150147.png
security:
- kind: domain-security
  name: Whichpost App Domain Security
  slug: whichpost-app-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Whichpost App Vulnerability Disclosure
  slug: whichpost-app-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: whichpost-app-locales-skill
  slug: whichpost-app-locales-skill
- name: whichpost-app-pricing-skill
  slug: whichpost-app-pricing-skill
- name: whichpost-app-waitlist-skill
  slug: whichpost-app-waitlist-skill
slug: whichpost-app
tags:
- Company
- Analytics
- Creator Economy
- Revenue
- Software-as-a-Service
- Marketing
website: https://whichpost.app/
---
