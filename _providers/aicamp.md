---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Aicamp Agentic Access
  operation_count: 3
  slug: aicamp-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: AICamp provides AI workspace APIs as documented in their markdown docs. No machine‑readable OpenAPI spec belonging to AICamp was found.
  name: AICamp API
  slug: aicamp-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/aicamp/agentic-access/aicamp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aicamp-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aicamp/plans/aicamp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aicamp-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aicamp/rules/aicamp-rules.yml
  title: ''
  type: Spectral
  url: rules/aicamp-rules.yml
- group: design
  href: https://artifacts.apis.io/aicamp/json-ld/aicamp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aicamp-context.jsonld
- group: design
  href: https://artifacts.apis.io/aicamp/vocabulary/aicamp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aicamp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aicamp/data-model/aicamp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aicamp-data-model.yml
- group: design
  href: https://artifacts.apis.io/aicamp/errors/aicamp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aicamp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aicamp/conformance/aicamp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicamp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aicamp/llms/aicamp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicamp-llms.txt
- group: other
  href: https://artifacts.apis.io/aicamp/a2a/aicamp-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aicamp-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aicamp/well-known/aicamp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aicamp-well-known.yml
- group: other
  href: https://artifacts.apis.io/aicamp/hosts/aicamp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aicamp-hosts.yml
- group: other
  href: https://artifacts.apis.io/aicamp/vendors/aicamp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aicamp-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aicamp.so/legal/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://app.aicamp.so/auth/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicamp.so/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aicamp.so/changelog
- group: company
  title: ''
  type: Blog
  url: https://aicamp.so/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aicamp.so/chat/chat-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aicamp.so/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aicamp.so/llms.txt
- group: auth
  href: https://artifacts.apis.io/aicamp/authentication/aicamp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aicamp-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aicamp/security/aicamp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicamp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aicamp.so/
- group: commercial
  title: ''
  type: Pricing
  url: https://aicamp.so/pricing
- group: company
  title: ''
  type: About
  url: https://aicamp.so/about
- group: company
  title: ''
  type: Careers
  url: https://aicamp.so/careers
coverage:
  checked: '2026-10-19'
  detail: Documentation is markdown but no OpenAPI or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 200
    url: https://docs.aicamp.so/introduction.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: AICamp provides a collaborative AI workspace designed for modern teams to centralize and manage AI-driven projects. It enables teams to build custom agents, share prompts, and collaborate across leading large language models without the complexity typically associated with enterprise AI solutions. The platform focuses on security, ease of use, and integration, allowing organizations to streamline AI workflows, enhance productivity, and foster innovation within a secure, shared environment.
image: https://uploads-ssl.webflow.com/662f95ccea47268446f3337d/6679230f45627b3f87af6aae_opengraph-image.png
jsonld:
- class_count: 2
  name: Aicamp Context
  property_count: 4
  slug: aicamp-context
layout: provider
modified: '2026-10-19'
name: AICamp
nav: Providers
network: true
overview: 'AICamp publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Collaboration, Workspace, and Team.


  The AICamp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AICamp''s developer surface includes signup flow, changelog, engineering blog, getting-started guide, documentation, API reference, authentication, and 20 more developer resources.'
plans:
- name: Aicamp Plans Pricing
  plan_count: 4
  slug: aicamp-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: AICamp API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: aicamp-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 13.4
    developer_ergonomics: 27.4
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 37.1
  provenance:
    agentic_access: derived
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aicamp/aicamp-2026-11-03T120445.png
security:
- kind: authentication
  name: Aicamp Authentication
  slug: aicamp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aicamp Domain Security
  slug: aicamp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aicamp
tags:
- Company
- Artificial Intelligence
- Collaboration
- Workspace
- Team
- Platform
website: https://aicamp.so/
---
