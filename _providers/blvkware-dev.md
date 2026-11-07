---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Blvkware Dev Agentic Access
  operation_count: 10
  slug: blvkware-dev-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.blvkware.dev/hallux/v1
  baseurl_source: declared
  description: Resolve identifiers to verdicts.
  name: BlvkWare Check API
  slug: blvkware-dev-check-api
- baseURL: https://api.blvkware.dev/hallux/v1
  baseurl_source: declared
  description: The phantom ledger itself.
  name: BlvkWare Corpus API
  slug: blvkware-dev-corpus-api
- baseURL: https://api.blvkware.dev/hallux/v1
  baseurl_source: declared
  description: Coverage, methodology and our own numbers.
  name: BlvkWare Meta API
  slug: blvkware-dev-meta-api
- baseURL: https://api.blvkware.dev/hallux/v1
  baseurl_source: declared
  description: Be told when a verdict changes.
  name: BlvkWare Watch API
  slug: blvkware-dev-watch-api
artifact_total: 14
common:
- group: docs
  title: ''
  type: Documentation
  url: https://blvkware.dev/guides/
- group: agent
  href: https://artifacts.apis.io/blvkware-dev/agentic-access/blvkware-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blvkware-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/blvkware-dev/plans/blvkware-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blvkware-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blvkware-dev/rules/blvkware-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/blvkware-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/blvkware-dev/json-ld/blvkware-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blvkware-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/blvkware-dev/vocabulary/blvkware-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blvkware-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blvkware-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blvkware-dev/data-model/blvkware-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blvkware-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/blvkware-dev/errors/blvkware-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blvkware-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blvkware-dev/conformance/blvkware-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blvkware-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blvkware-dev/llms/blvkware-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blvkware-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/blvkware-dev/well-known/blvkware-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blvkware-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/blvkware-dev/hosts/blvkware-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blvkware-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/blvkware-dev/vendors/blvkware-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blvkware-dev-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rxslice
- group: auth
  href: https://artifacts.apis.io/blvkware-dev/security/blvkware-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blvkware-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blvkware.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://blvkware.dev/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blvkware.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blvkware.dev/privacy/
created: '2026-11-02'
description: BlvkWare designs AI agents that do real work and sells each as a downloadable kit. The kits include the agent's instructions, tool definitions for OpenAI, Anthropic and MCP formats, workflows, record schemas, autonomy policies, and acceptance tests, all generated from the buyer's answers. Pricing starts at $79 for a single‑job kit and $199 for a full‑function kit.
image: https://blvkware.dev/assets/og/home.png
json_schemas:
- name: CheckRequest
  property_count: 2
  slug: blvkware-dev-check-request
- name: CheckResponse
  property_count: 5
  slug: blvkware-dev-check-response
- name: Result
  property_count: 8
  slug: blvkware-dev-result
- name: WatchRequest
  property_count: 2
  slug: blvkware-dev-watch-request
jsonld:
- class_count: 8
  name: Blvkware Dev Context
  property_count: 35
  slug: blvkware-dev-context
layout: provider
modified: '2026-11-02'
name: BlvkWare
nav: Providers
network: true
overview: 'BlvkWare publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Check API, Corpus API, Meta API, and 1 more. Tagged areas include Artificial Intelligence, Agents, Kit, Automation, and Marketplace.


  The BlvkWare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BlvkWare''s developer surface includes documentation, pricing, and 18 more developer resources.'
plans:
- name: Blvkware Dev Plans Pricing
  plan_count: 7
  slug: blvkware-dev-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: BlvkWare API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: blvkware-dev-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 59.4
    developer_ergonomics: 6.5
    discoverability: 66.1
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blvkware Dev Domain Security
  slug: blvkware-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: blvkware-dev-check-identifiers
  slug: blvkware-dev-check-identifiers
slug: blvkware-dev
tags:
- Artificial Intelligence
- Agents
- Kit
- Automation
- Marketplace
- Company
website: https://blvkware.dev/
---
