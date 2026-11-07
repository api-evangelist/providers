---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Codescene Agentic Access
  operation_count: 73
  slug: codescene-agentic-access
  summary_line: 73 operations · 17 acting
api_count: 1
apis:
- description: Public API documentation for CodeScene.
  name: CodeScene REST API
  slug: codescene-rest-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/codescene/llms/codescene-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/codescene-llms.txt
- group: other
  href: https://artifacts.apis.io/codescene/hosts/codescene-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codescene-hosts.yml
- group: other
  href: https://artifacts.apis.io/codescene/vendors/codescene-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codescene-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.codescene.com/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.enterprise.codescene.io/latest/
- group: auth
  href: https://artifacts.apis.io/codescene/security/codescene-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codescene-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codescene.com/
- group: docs
  title: ''
  type: Documentation
  url: https://codescene.io/docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://codescene.io/docs/integrations/rest-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://codescene.io/docs/getting-started/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://codescene.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://codescene.com/blog
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.codescene.com/en/help
- group: start
  title: ''
  type: SignUp
  url: https://codescene.com/product/free-trial
coverage:
  checked: '2026-10-27'
  detail: Documentation provides HTML reference but no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://codescene.io/docs/integrations/rest-api.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: CodeScene provides AI‑enhanced code analysis tools that help software teams visualize technical debt, prioritize refactoring, and ensure safe AI‑assisted coding. Their platform combines behavioral code analysis, CodeHealth metrics, and integrations with IDEs, CI pipelines, and popular version‑control systems to deliver actionable insights and guardrails that improve code quality and reduce defect risk.
image: https://codescene.com/hubfs/Featured%20image%20-%20Product.png
layout: provider
modified: '2026-10-26'
name: CodeScene
nav: Providers
network: true
overview: 'CodeScene publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Code Analysis, Technical Debt, and DevOps.


  The CodeScene catalog on APIs.io includes 1 Spectral governance ruleset.


  CodeScene''s developer surface includes changelog, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 7 more developer resources.'
plans:
- name: Codescene Plans Pricing
  plan_count: 3
  slug: codescene-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: CodeScene API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: codescene-rules
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/codescene/codescene-2026-11-03T124728.png
security:
- kind: authentication
  name: Codescene Authentication
  slug: codescene-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Codescene Domain Security
  slug: codescene-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codescene
tags:
- Company
- Artificial Intelligence
- Code Analysis
- Technical Debt
- DevOps
website: https://codescene.com/
---
