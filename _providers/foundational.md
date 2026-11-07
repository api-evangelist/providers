---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Foundational Agentic Access
  operation_count: 34
  slug: foundational-agentic-access
  summary_line: 34 operations · 19 acting
api_count: 1
apis:
- baseURL: /api/v1
  baseurl_source: spec
  description: The Auth API from Foundational — 1 operation(s) for auth.
  name: Foundational Auth API
  slug: foundational-auth-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The Lineage API from Foundational — 14 operation(s) for lineage.
  name: Foundational Lineage API
  slug: foundational-lineage-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The Manual Lineage API from Foundational — 3 operation(s) for manual lineage.
  name: Foundational Manual Lineage API
  slug: foundational-manual-lineage-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The Monitors API from Foundational — 2 operation(s) for monitors.
  name: Foundational Monitors API
  slug: foundational-monitors-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The Onboarding API from Foundational — 5 operation(s) for onboarding.
  name: Foundational Onboarding API
  slug: foundational-onboarding-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The Policies API from Foundational — 3 operation(s) for policies.
  name: Foundational Policies API
  slug: foundational-policies-api
artifact_total: 20
asyncapis:
- description: ''
  name: Foundational Webhooks
  slug: foundational-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/foundational/agentic-access/foundational-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/foundational-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/foundational/rules/foundational-rules.yml
  title: ''
  type: Spectral
  url: rules/foundational-rules.yml
- group: design
  href: https://artifacts.apis.io/foundational/json-ld/foundational-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/foundational-context.jsonld
- group: design
  href: https://artifacts.apis.io/foundational/vocabulary/foundational-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/foundational-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/foundational/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/foundational/asyncapi/foundational-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/foundational-webhooks.yml
- group: design
  href: https://artifacts.apis.io/foundational/data-model/foundational-data-model.yml
  title: ''
  type: DataModel
  url: data-model/foundational-data-model.yml
- group: design
  href: https://artifacts.apis.io/foundational/errors/foundational-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/foundational-problem-types.yml
- group: design
  href: https://artifacts.apis.io/foundational/conformance/foundational-conformance.yml
  title: ''
  type: Conformance
  url: conformance/foundational-conformance.yml
- group: other
  href: https://artifacts.apis.io/foundational/overlays/foundational-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/foundational-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/foundational/llms/foundational-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/foundational-llms.txt
- group: auth
  href: https://artifacts.apis.io/foundational/well-known/foundational-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/foundational-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/foundational/well-known/foundational-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/foundational-well-known.yml
- group: other
  href: https://artifacts.apis.io/foundational/hosts/foundational-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foundational-hosts.yml
- group: other
  href: https://artifacts.apis.io/foundational/vendors/foundational-vendors.yml
  title: ''
  type: Vendors
  url: vendors/foundational-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.foundational.io/team
- group: auth
  href: https://artifacts.apis.io/foundational/security/foundational-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foundational-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.foundational.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.foundational.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.foundational.io/en/collections/10497184-ai-and-api-connectivity
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.foundational.io/en/collections/6125551-get-started
- group: company
  title: ''
  type: Blog
  url: https://www.foundational.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.foundational.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.foundational.io/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.foundational.io/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.foundational.io/demo
created: '2026-10-29'
description: Foundational is a Data Management Platform that automates pre‑deploy impact analysis, lineage, and data contracts, enabling proactive data governance for AI‑driven enterprises. It helps teams find, fix, and prevent data incidents before code merges, reducing risk and protecting trust across the data lifecycle.
image: https://cdn.prod.website-files.com/64889d1417f36c1e9731bb2c/66139de567673391dd1c4658_Foundational%20%20OG.png
json_schemas:
- name: AppGraphNeighborsResponse
  property_count: 5
  slug: foundational-app-graph-neighbors-response
- name: DashboardUsageRankingResponse
  property_count: 11
  slug: foundational-dashboard-usage-ranking-response
- name: EdgeProvenanceResponse
  property_count: 8
  slug: foundational-edge-provenance-response
- name: LineageEntitiesResponse
  property_count: 3
  slug: foundational-lineage-entities-response
- name: LineageEntityResponse
  property_count: 11
  slug: foundational-lineage-entity-response
- name: PublicPolicyResponse
  property_count: 9
  slug: foundational-public-policy-response
jsonld:
- class_count: 120
  name: Foundational Context
  property_count: 323
  slug: foundational-context
layout: provider
modified: '2026-10-29'
name: Foundational
nav: Providers
network: true
overview: 'Foundational publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Lineage API, Manual Lineage API, and 3 more. Tagged areas include Company, Data Governance, Artificial Intelligence, Data Management, and Data Lineage.


  The Foundational catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Foundational''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Foundational Plans Pricing
  plan_count: 0
  slug: foundational-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Foundational API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: foundational-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 63.7
    developer_ergonomics: 21.9
    discoverability: 65.2
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/foundational/foundational-2026-11-03T132309.png
security:
- kind: domain-security
  name: Foundational Domain Security
  slug: foundational-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: entity-tags
  slug: foundational-entity-tags
- name: lineage-search
  slug: foundational-lineage-search
slug: foundational
tags:
- Company
- Data Governance
- Artificial Intelligence
- Data Management
- Data Lineage
website: https://www.foundational.io/
---
