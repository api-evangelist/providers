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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Social posting infrastructure for AI agents.
  name: Claw Post API
  slug: claw-post-api
- baseURL: https://api.clawpost.net
  baseurl_source: declared
  description: Social posting infrastructure for AI agents. Agents create posts that the user's paired browser extension publishes from the user's logged-in social sessions. No platform passwords are ever stored.
  name: Claw Post API API
  slug: claw-post-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/clawpost-net/rules/clawpost-net-rules.yml
  title: ''
  type: Spectral
  url: rules/clawpost-net-rules.yml
- group: design
  href: https://artifacts.apis.io/clawpost-net/json-ld/clawpost-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clawpost-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/clawpost-net/vocabulary/clawpost-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clawpost-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/clawpost-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/clawpost-net/data-model/clawpost-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clawpost-net-data-model.yml
- group: design
  href: https://artifacts.apis.io/clawpost-net/conventions/clawpost-net-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/clawpost-net-conventions.yml
- group: design
  href: https://artifacts.apis.io/clawpost-net/conventions/clawpost-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clawpost-net-conventions.yml
- group: design
  href: https://artifacts.apis.io/clawpost-net/errors/clawpost-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clawpost-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clawpost-net/conformance/clawpost-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clawpost-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clawpost-net/llms/clawpost-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clawpost-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/clawpost-net/well-known/clawpost-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clawpost-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/clawpost-net/hosts/clawpost-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawpost-net-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clawpost.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clawpost.net/privacy
- group: auth
  href: https://artifacts.apis.io/clawpost-net/security/clawpost-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawpost-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clawpost.net/
created: '2026-11-03'
description: Claw Post provides AI‑agent‑driven social media posting for platforms like X, LinkedIn, Facebook, TikTok and Instagram. Agents publish from a logged‑in desktop Chrome without exposing API keys, offering a low‑cost (~1¢ per post) and zero‑account‑bans solution for automated content distribution.
json_schemas:
- name: ConnectIntent
  property_count: 3
  slug: clawpost-net-connect-intent
- name: CreateJobRequest
  property_count: 6
  slug: clawpost-net-create-job-request
- name: Job
  property_count: 12
  slug: clawpost-net-job
jsonld:
- class_count: 4
  name: Clawpost Net Context
  property_count: 17
  slug: clawpost-net-context
layout: provider
modified: '2026-11-03'
name: Claw Post
nav: Providers
network: true
overview: 'Claw Post publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, Artificial Intelligence, Social Media, Automation, and Posting.


  The Claw Post catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Claw Post API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: clawpost-net-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 6.4
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clawpost Net Domain Security
  slug: clawpost-net-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: posting
  slug: clawpost-net-posting-skill
slug: clawpost-net
tags:
- Company
- Artificial Intelligence
- Social Media
- Automation
- Posting
- Agents
website: https://clawpost.net/
---
