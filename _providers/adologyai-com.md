---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Adologyai Com Agentic Access
  operation_count: 1
  slug: adologyai-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Adology API — 1 operation.
  name: Adology API
  slug: adology-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/adologyai-com/vocabulary/adologyai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adologyai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/adologyai-com/errors/adologyai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adologyai-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/adologyai-com/agentic-access/adologyai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adologyai-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adologyai-com/rules/adologyai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/adologyai-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/adologyai-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/adologyai-com/authentication/adologyai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adologyai-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/adologyai-com/conformance/adologyai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adologyai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adologyai-com/llms/adologyai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adologyai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/adologyai-com/hosts/adologyai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adologyai-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://dash.adologyai.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adologyai
- group: auth
  href: https://artifacts.apis.io/adologyai-com/security/adologyai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adologyai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adologyai.com/
- group: operate
  title: ''
  type: Support
  url: https://adologyai.com/support
- group: company
  title: ''
  type: Blog
  url: https://adologyai.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adologyai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adologyai.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://adologyai.com/about
created: '2026-10-31'
description: Adology connects intelligence across categories, competitors, culture, creators, and customers, analyzing the content frame‑by‑frame to help your team decide what to make next. All backed by evidence. Adology is creative intelligence for agencies and brands, built by expert agency and media executives.
image: https://framerusercontent.com/assets/QsnWw7MGuRxtUqovciUBZCACLA.png
layout: provider
modified: '2026-10-31'
name: Adology
nav: Providers
network: true
overview: 'Adology publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Intelligence, Creative, and Analytics.


  The Adology catalog on APIs.io includes 1 Spectral governance ruleset.


  Adology''s developer surface includes authentication, support, engineering blog, getting-started guide, and 14 more developer resources.'
plans:
- name: Adologyai Com Plans Pricing
  plan_count: 0
  slug: adologyai-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Adologyai Com Rate Limits
  slug: adologyai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Adology API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: adologyai-com-rules
scopes:
- name: Adologyai Com Scopes
  scope_count: 0
  slug: adologyai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 27.9
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adologyai Com Authentication
  slug: adologyai-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adologyai Com Domain Security
  slug: adologyai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: debug-auth
  slug: adologyai-com-debug-auth
slug: adologyai-com
tags:
- Artificial Intelligence
- Marketing
- Intelligence
- Creative
- Analytics
website: https://adologyai.com/
---
