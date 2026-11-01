---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hanria Ai Agentic Access
  operation_count: 1
  slug: hanria-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Check a proposed agent action against an operator-authored mandate.
  name: Check
  slug: check
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/hanria-ai/agentic-access/hanria-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hanria-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hanria-ai/rules/hanria-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/hanria-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/hanria-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hanria-ai/conformance/hanria-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hanria-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hanria-ai/llms/hanria-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hanria-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/hanria-ai/a2a/hanria-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hanria-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hanria-ai/well-known/hanria-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hanria-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/hanria-ai/hosts/hanria-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hanria-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/hanria-ai/vendors/hanria-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hanria-ai-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://hanria.ai/guides/
- group: auth
  href: https://artifacts.apis.io/hanria-ai/security/hanria-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hanria-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hanria.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://hanria.ai/developers/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hanria.ai/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://hanria.ai/how-it-works/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hanria.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hanria.ai/privacy/
created: '2026-10-30'
description: HANRIA provides a decision point for agent commerce, enabling verification of AI agents' identities, mandates, and payment eligibility before actions are taken. It offers a mandate check, runtime enforcement, independent review, and record carrying to ensure accountability and compliance. The platform protects users from unauthorized agent actions and maintains transparent audit trails.
image: https://hanria.ai/brand/hanria-h.svg
layout: provider
modified: '2026-10-30'
name: hanria-ai
nav: Providers
network: true
overview: 'hanria-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Agent, Identity, Verification, and Payments.


  The hanria-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  hanria-ai''s developer surface includes API reference, documentation, getting-started guide, and 14 more developer resources.'
plans:
- name: Hanria Ai Plans Pricing
  plan_count: 0
  slug: hanria-ai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Hanria Ai Rate Limits
  slug: hanria-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: hanria-ai API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: hanria-ai-rules
scopes:
- name: Hanria Ai Scopes
  scope_count: 0
  slug: hanria-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 44.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hanria Ai Authentication
  slug: hanria-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hanria Ai Domain Security
  slug: hanria-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: check-action
  slug: hanria-ai-check-action
slug: hanria-ai
tags:
- AI
- Agent
- Identity
- Verification
- Payments
- Compliance
- Company
website: https://hanria.ai/
---
