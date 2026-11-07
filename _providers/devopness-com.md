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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Devopness Com Agentic Access
  operation_count: 1
  slug: devopness-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Devopness API - Painless essential DevOps to everyone
  name: Devopness API
  slug: devopness-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/devopness-com/agentic-access/devopness-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/devopness-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/devopness-com/plans/devopness-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/devopness-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/devopness-com/rules/devopness-com-rules.yml
  title: ''
  type: Spectral
  url: rules/devopness-com-rules.yml
- group: design
  href: https://artifacts.apis.io/devopness-com/vocabulary/devopness-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/devopness-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/devopness-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/devopness-com/changelog/devopness-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/devopness-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/devopness-com/conformance/devopness-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/devopness-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/devopness-com/llms/devopness-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/devopness-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/devopness-com/well-known/devopness-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/devopness-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/devopness-com/hosts/devopness-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devopness-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/devopness-com/vendors/devopness-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devopness-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devopness.com/docs/legal/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://github.com/devopness/devopness/discussions/categories/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devopness.com/docs/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://devopness.com/changelog/
- group: auth
  href: https://artifacts.apis.io/devopness-com/security/devopness-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devopness-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devopness.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devopness.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://devopness.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://devopness.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://devopness.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://devopness.com/pricing/
- group: agent
  title: ''
  type: MCP
  url: https://devopness.com/mcp/
created: '2026-11-05'
description: Devopness offers a self‑service platform that lets developers and teams deploy applications and provision infrastructure directly in their own AWS, Azure, Google Cloud, DigitalOcean, Hetzner, and other accounts. Users connect a cloud provider, link a GitHub, GitLab or Bitbucket repository, and deploy apps or self‑hosted tools with zero downtime via a web UI, API, MCP, or git push. The service includes server provisioning, SSL certificates, DNS, firewalls, cronjobs, and fine‑grained access controls, enabling teams to ship without a dedicated DevOps engineer.
image: https://assets.devopness.com/images/logo.png
layout: provider
modified: '2026-11-05'
name: Devopness
nav: Providers
network: true
overview: 'Devopness is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Platform-as-a-Service, DevOps, Self-Hosted, and Infrastructure.


  The Devopness catalog on APIs.io includes 1 Spectral governance ruleset.


  Devopness'' developer surface includes changelog, support, documentation, API reference, getting-started guide, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Devopness Com Plans Pricing
  plan_count: 4
  slug: devopness-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Devopness API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: devopness-com-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 15.8
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devopness Com Domain Security
  slug: devopness-com-domain-security
  summary_line: TLSv1.3
slug: devopness-com
tags:
- Cloud
- Platform-as-a-Service
- DevOps
- Self-Hosted
- Infrastructure
website: https://devopness.com/
---
