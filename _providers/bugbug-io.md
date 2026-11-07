---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 2
  name: Bugbug Io Agentic Access
  operation_count: 96
  slug: bugbug-io-agentic-access
  summary_line: 96 operations · 49 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Retrieving components
  name: BugBug Components API
  slug: bugbug-io-components-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Config
  name: BugBug Config API
  slug: bugbug-io-config-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: The Folders API from BugBug — 3 operation(s) for folders.
  name: BugBug Folders API
  slug: bugbug-io-folders-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Managing test groups
  name: BugBug Groups API
  slug: bugbug-io-groups-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Importing and exporting YAML and ZIP files
  name: BugBug Import / Export API
  slug: bugbug-io-import-export-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: The Organizations API from BugBug — 1 operation(s) for organizations.
  name: BugBug Organizations API
  slug: bugbug-io-organizations-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Profiles
  name: BugBug Profiles API
  slug: bugbug-io-profiles-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Retrieving projects
  name: BugBug Projects API
  slug: bugbug-io-projects-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Project settings
  name: BugBug Settings API
  slug: bugbug-io-settings-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: The Step runs API from BugBug — 1 operation(s) for step runs.
  name: BugBug Step runs API
  slug: bugbug-io-step-runs-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Managing test steps
  name: BugBug Steps API
  slug: bugbug-io-steps-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Executing and getting result
  name: BugBug Suite runs API
  slug: bugbug-io-suite-runs-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Retrieving suites
  name: BugBug Suites API
  slug: bugbug-io-suites-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: The Tags API from BugBug — 2 operation(s) for tags.
  name: BugBug Tags API
  slug: bugbug-io-tags-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Executing tests and getting result
  name: BugBug Test runs API
  slug: bugbug-io-test-runs-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Retrieving tests
  name: BugBug Tests API
  slug: bugbug-io-tests-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: The Variables API from BugBug — 2 operation(s) for variables.
  name: BugBug Variables API
  slug: bugbug-io-variables-api
- baseURL: https://api.bugbug.io
  baseurl_source: declared
  description: Visual regression reference screenshots
  name: BugBug Visual regression API
  slug: bugbug-io-visual-regression-api
artifact_total: 36
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bugbug.io/quick-start/setup-bugbug
- group: agent
  href: https://artifacts.apis.io/bugbug-io/agentic-access/bugbug-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bugbug-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bugbug-io/plans/bugbug-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bugbug-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bugbug-io/rules/bugbug-io-rules.yml
  title: ''
  type: Spectral
  url: rules/bugbug-io-rules.yml
- group: design
  href: https://artifacts.apis.io/bugbug-io/json-ld/bugbug-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bugbug-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/bugbug-io/vocabulary/bugbug-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bugbug-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bugbug-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bugbug-io/data-model/bugbug-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bugbug-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bugbug-io/security/bugbug-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bugbug-io-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/bugbug-io/errors/bugbug-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bugbug-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bugbug-io/conformance/bugbug-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bugbug-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bugbug-io/llms/bugbug-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bugbug-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/bugbug-io/well-known/bugbug-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bugbug-io-security.txt
- group: auth
  href: https://artifacts.apis.io/bugbug-io/well-known/bugbug-io-develop-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bugbug-io-develop-security.txt
- group: auth
  href: https://artifacts.apis.io/bugbug-io/well-known/bugbug-io-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bugbug-io-app-security.txt
- group: agent
  href: https://artifacts.apis.io/bugbug-io/well-known/bugbug-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bugbug-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/bugbug-io/hosts/bugbug-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bugbug-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/bugbug-io/vendors/bugbug-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bugbug-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/bugbug-io/packages/bugbug-io-packages.yml
  title: ''
  type: SDKs
  url: packages/bugbug-io-packages.yml
- group: build
  href: https://artifacts.apis.io/bugbug-io/packages/bugbug-io-packages.yml
  title: ''
  type: Packages
  url: packages/bugbug-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bugbug.io/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bugbug.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bugbug.io/privacy-policy/
- group: docs
  title: ''
  type: APIReference
  url: https://api.bugbug.io/docs/swagger/
- group: auth
  href: https://artifacts.apis.io/bugbug-io/authentication/bugbug-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bugbug-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bugbug-io/security/bugbug-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bugbug-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bugbug-io/security/bugbug-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bugbug-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bugbug.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bugbug.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://bugbug.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://bugbug.io/blog/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 403
    url: https://app.bugbug.io/mcp
  - status: 200
    url: https://bugbug.io/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: BugBug is a low-code, no‑code end‑to‑end test automation platform for SaaS teams. It lets users record, edit and run regression tests without writing code, speeding delivery and reducing QA overhead. The service offers free, core and pro plans, integrates with CI pipelines, and provides a visual test recorder and MCP automation engine.
image: https://bugbug-homepage.s3.eu-central-1.amazonaws.com/opengraph_image_76fdb81af4.png
json_schemas:
- name: PatchedStepResponse
  property_count: 0
  slug: bugbug-io-patched-step-response
- name: StepResponse
  property_count: 0
  slug: bugbug-io-step-response
- name: V2ProjectSettings
  property_count: 23
  slug: bugbug-io-v2-project-settings
- name: V2StepRunDetail
  property_count: 44
  slug: bugbug-io-v2-step-run-detail
- name: V2SuiteRun
  property_count: 22
  slug: bugbug-io-v2-suite-run
- name: V2TestRun
  property_count: 30
  slug: bugbug-io-v2-test-run
jsonld:
- class_count: 120
  name: Bugbug Io Context
  property_count: 142
  slug: bugbug-io-context
layout: provider
modified: '2026-11-03'
name: BugBug
nav: Providers
network: true
overview: 'BugBug publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Components API, Config API, Folders API, and 15 more. Tagged areas include Company, Testing, Automation, Software-as-a-Service, and Low-Code.


  The BugBug catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BugBug''s developer surface includes getting-started guide, API reference, authentication, documentation, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Bugbug Io Plans Pricing
  plan_count: 4
  slug: bugbug-io-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: BugBug API Rules
  rule_count: 56
  severity_counts:
    error: 42
    hint: 0
    info: 3
    warn: 11
  slug: bugbug-io-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 60.6
    developer_ergonomics: 36.3
    discoverability: 66.1
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bugbug Io Authentication
  slug: bugbug-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bugbug Io Domain Security
  slug: bugbug-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bugbug Io Vulnerability Disclosure
  slug: bugbug-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: bugbug-io-components-workflow
  slug: bugbug-io-components-workflow
- name: bugbug-io-create-test-with-component-and-tags
  slug: bugbug-io-create-test-with-component-and-tags
- name: bugbug-io-execute-suite-run
  slug: bugbug-io-execute-suite-run
- name: bugbug-io-suite-lifecycle
  slug: bugbug-io-suite-lifecycle
- name: bugbug-io-test-run-execute-and-fetch
  slug: bugbug-io-test-run-execute-and-fetch
slug: bugbug-io
tags:
- Company
- Testing
- Automation
- Software-as-a-Service
- Low-Code
- No-Code
website: https://bugbug.io/
---
