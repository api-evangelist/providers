---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Thehive Ai Agentic Access
  operation_count: 4
  slug: thehive-ai-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.thehive.ai/api/
  baseurl_source: declared
  description: The Task API from Hive — 4 operation(s) for task.
  name: Hive Task API
  slug: thehive-ai-task-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/thehive-ai/vocabulary/thehive-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thehive-ai-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/thehive-ai/well-known/thehive-ai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thehive-ai-status-security.txt
- group: start
  title: ''
  type: Login
  url: https://thehive.ai/login
- group: agent
  href: https://artifacts.apis.io/thehive-ai/agentic-access/thehive-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thehive-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/thehive-ai/plans/thehive-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thehive-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/thehive-ai/rules/thehive-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/thehive-ai-rules.yml
- group: auth
  href: https://artifacts.apis.io/thehive-ai/authentication/thehive-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thehive-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/thehive-ai/errors/thehive-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thehive-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thehive-ai/conformance/thehive-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thehive-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/thehive-ai/llms/thehive-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thehive-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/thehive-ai/well-known/thehive-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thehive-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/thehive-ai/hosts/thehive-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thehive-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/thehive-ai/vendors/thehive-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thehive-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thehive.ai/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thehive.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thehive.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://thehive.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://thehive.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thehive.ai/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thehive.ai/
- group: auth
  href: https://artifacts.apis.io/thehive-ai/security/thehive-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thehive-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thehive.ai
created: '2026-10-25'
description: Hive provides enterprise‑grade AI solutions, offering cloud‑based machine‑learning models, computer‑vision services, and data‑labeling platforms. Trusted by large innovators, Hive enables organizations to integrate advanced AI into products at scale, with a focus on security, compliance, and rapid deployment.
image: https://thehive.ai/_next/static/images/thumbnail-e2a49944225d8e3f443794a8a866114a.jpg
layout: provider
modified: '2026-10-25'
name: Hive
nav: Providers
network: true
overview: 'Hive publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Task API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Data Labeling, and Enterprise.


  The Hive catalog on APIs.io includes 1 Spectral governance ruleset.


  Hive''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Thehive Ai Plans Pricing
  plan_count: 2
  slug: thehive-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Thehive Ai Rate Limits
  slug: thehive-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Hive API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: thehive-ai-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 53.1
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
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
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thehive-ai/thehive-ai-2026-11-03T144621.png
security:
- kind: authentication
  name: Thehive Ai Authentication
  slug: thehive-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thehive Ai Domain Security
  slug: thehive-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thehive-ai
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Data Labeling
- Enterprise
website: https://thehive.ai
---
