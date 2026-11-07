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
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Factory Agentic Access
  operation_count: 8
  slug: factory-agentic-access
  summary_line: 8 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://docs.factory.com
  baseurl_source: declared
  description: The Automations API from Factory — 6 operation(s) for automations.
  name: Factory Automations API
  slug: factory-automations-api
- baseURL: https://docs.factory.com
  baseurl_source: declared
  description: The Computers API from Factory — 1 operation(s) for computers.
  name: Factory Computers API
  slug: factory-computers-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/factory/data-model/factory-data-model.yml
  title: ''
  type: DataModel
  url: data-model/factory-data-model.yml
- group: agent
  href: https://artifacts.apis.io/factory/agentic-access/factory-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/factory-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/factory/plans/factory-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/factory-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/factory/rules/factory-rules.yml
  title: ''
  type: Spectral
  url: rules/factory-rules.yml
- group: design
  href: https://artifacts.apis.io/factory/vocabulary/factory-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/factory-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/factory/cli/factory-cli.yml
  title: ''
  type: CLI
  url: cli/factory-cli.yml
- group: operate
  href: https://artifacts.apis.io/factory/changelog/factory-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/factory-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://factory.com/security
- group: design
  href: https://artifacts.apis.io/factory/errors/factory-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/factory-problem-types.yml
- group: design
  href: https://artifacts.apis.io/factory/conformance/factory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/factory-conformance.yml
- group: agent
  href: https://artifacts.apis.io/factory/llms/factory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/factory-llms.txt
- group: other
  href: https://artifacts.apis.io/factory/hosts/factory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/factory-hosts.yml
- group: other
  href: https://artifacts.apis.io/factory/vendors/factory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/factory-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://factory.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://factory.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://factory.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.factory.com/docs/changelog/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.factory.com/factory-app/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.factory.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.factory.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/factory/security/factory-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/factory-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/factory/security/factory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/factory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://factory.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.factory.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://factory.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://factory.com/terms
- group: operate
  title: ''
  type: Support
  url: https://factory.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Factory-AI
created: '2026-10-22'
description: Factory provides a cloud‑based manufacturing operations platform that connects factories, suppliers, and customers through real‑time data integration, workflow automation, and analytics. The solution enables manufacturers to digitize production lines, monitor equipment health, manage inventory, and optimize supply‑chain logistics, delivering increased efficiency and transparency across the entire manufacturing ecosystem.
image: https://factory.com/og-v3.png
json_schemas:
- name: CreateComputerRequestBody
  property_count: 0
  slug: factory-create-computer-request-body
- name: GetListCiAutomationJobs200ResponseBody
  property_count: 0
  slug: factory-get-list-ci-automation-jobs200-response-body
- name: GetListCiEligibleRepositories200ResponseBody
  property_count: 0
  slug: factory-get-list-ci-eligible-repositories200-response-body
- name: GetListCiRepositoryOwners200ResponseBody
  property_count: 0
  slug: factory-get-list-ci-repository-owners200-response-body
- name: GetListGithubActionsRunsForCiAutomationWorkflows200ResponseBody
  property_count: 0
  slug: factory-get-list-github-actions-runs-for-ci-automation-workflows200-response-body
- name: GetScanRepositoriesForCiWorkflows200ResponseBody
  property_count: 0
  slug: factory-get-scan-repositories-for-ci-workflows200-response-body
layout: provider
modified: '2026-10-22'
name: Factory
nav: Providers
network: true
overview: 'Factory publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Automations API and Computers API. Tagged areas include Manufacturing, Software-as-a-Service, Cloud, Automation, and Supply Chain.


  The Factory catalog on APIs.io includes 1 Spectral governance ruleset.


  Factory''s developer surface includes CLI, changelog, getting-started guide, API reference, documentation, pricing, support, and 21 more developer resources.'
plans:
- name: Factory Plans Pricing
  plan_count: 6
  slug: factory-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Factory API Rules
  rule_count: 12
  severity_counts:
    error: 6
    hint: 0
    info: 5
    warn: 1
  slug: factory-rules
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 43.8
    developer_ergonomics: 28.6
    discoverability: 74.1
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/factory/factory-2026-11-03T131812.png
security:
- kind: domain-security
  name: Factory Domain Security
  slug: factory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Factory Trust Center
  slug: factory-trust-center
  summary_line: SOC 2
slug: factory
tags:
- Manufacturing
- Software-as-a-Service
- Cloud
- Automation
- Supply Chain
- Company
website: https://factory.com
---
