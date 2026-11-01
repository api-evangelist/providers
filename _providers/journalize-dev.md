---
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Journalize Dev Agentic Access
  operation_count: 21
  slug: journalize-dev-agentic-access
  summary_line: 21 operations · 4 acting
api_count: 1
apis:
- description: The Accounts API from journalize-dev — 2 operation(s) for accounts.
  name: journalize-dev Accounts API
  slug: journalize-dev-accounts-api
- description: The Export API from journalize-dev — 1 operation(s) for export.
  name: journalize-dev Export API
  slug: journalize-dev-export-api
- description: The Health API from journalize-dev — 1 operation(s) for health.
  name: journalize-dev Health API
  slug: journalize-dev-health-api
- description: The Journal API from journalize-dev — 3 operation(s) for journal.
  name: journalize-dev Journal API
  slug: journalize-dev-journal-api
- description: The Journalize API from journalize-dev — 1 operation(s) for journalize.
  name: journalize-dev Journalize API
  slug: journalize-dev-journalize-api
- description: The Llms.txt API from journalize-dev — 1 operation(s) for llms.txt.
  name: journalize-dev Llms.txt API
  slug: journalize-dev-llms-txt-api
- description: The Privacy API from journalize-dev — 1 operation(s) for privacy.
  name: journalize-dev Privacy API
  slug: journalize-dev-privacy-api
- description: The Register API from journalize-dev — 1 operation(s) for register.
  name: journalize-dev Register API
  slug: journalize-dev-register-api
- description: The Reports API from journalize-dev — 3 operation(s) for reports.
  name: journalize-dev Reports API
  slug: journalize-dev-reports-api
- description: The Robots.txt API from journalize-dev — 1 operation(s) for robots.txt.
  name: journalize-dev Robots.txt API
  slug: journalize-dev-robots-txt-api
- description: The Security.txt API from journalize-dev — 1 operation(s) for security.txt.
  name: journalize-dev Security.txt API
  slug: journalize-dev-security-txt-api
- description: The SKILL.md API from journalize-dev — 1 operation(s) for skill.md.
  name: journalize-dev SKILL.md API
  slug: journalize-dev-skill-md-api
- description: The Terms API from journalize-dev — 1 operation(s) for terms.
  name: journalize-dev Terms API
  slug: journalize-dev-terms-api
- description: The .well Known API from journalize-dev — 2 operation(s) for .well known.
  name: journalize-dev .well Known API
  slug: journalize-dev-well-known-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/journalize-dev/agentic-access/journalize-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/journalize-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/journalize-dev/rules/journalize-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/journalize-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/journalize-dev/json-ld/journalize-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/journalize-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/journalize-dev/vocabulary/journalize-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/journalize-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/journalize-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/journalize-dev/data-model/journalize-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/journalize-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/journalize-dev/security/journalize-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/journalize-dev-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/journalize-dev/errors/journalize-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/journalize-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/journalize-dev/conformance/journalize-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/journalize-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/journalize-dev/llms/journalize-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/journalize-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/journalize-dev/well-known/journalize-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/journalize-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/journalize-dev/well-known/journalize-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/journalize-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/journalize-dev/hosts/journalize-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/journalize-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/journalize-dev/vendors/journalize-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/journalize-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://journalize.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://journalize.dev/privacy
- group: auth
  href: https://artifacts.apis.io/journalize-dev/security/journalize-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/journalize-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/journalize-dev/security/journalize-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/journalize-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://journalize.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://journalize.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://journalize.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://journalize.dev/openapi.json
created: '2026-10-30'
description: 'Journalize — bookkeeping your AI agent can run on its own. Give an AI agent a real double-entry ledger: an account it opens once, transactions validated by real Beancount rules, and balance sheets/income statements it can pull on demand. REST and MCP, priced per call via x402. The service offers endpoints to register keys, submit and validate accounting directives, list accounts, and retrieve balances, all secured with Ed25519 signatures. Built by Chris Dunn in Singapore, Journalize enables AI agents to perform accurate financial bookkeeping without manual intervention.'
image: https://journalize.dev/favicon.ico
json_schemas:
- name: BalanceSheetResponse
  property_count: 4
  slug: journalize-dev-balance-sheet-response
- name: DirectiveBatchRequest
  property_count: 1
  slug: journalize-dev-directive-batch-request
- name: DirectiveWriteResponse
  property_count: 5
  slug: journalize-dev-directive-write-response
- name: IncomeStatementResponse
  property_count: 4
  slug: journalize-dev-income-statement-response
- name: RegisterResponse
  property_count: 2
  slug: journalize-dev-register-response
- name: TrialBalanceResponse
  property_count: 4
  slug: journalize-dev-trial-balance-response
jsonld:
- class_count: 22
  name: Journalize Dev Context
  property_count: 33
  slug: journalize-dev-context
layout: provider
modified: '2026-10-30'
name: journalize-dev
nav: Providers
network: true
overview: 'journalize-dev publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Export API, Health API, and 11 more. Tagged areas include Company, Accounting, AI, FinTech, and Ledger.


  The journalize-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  journalize-dev''s developer surface includes documentation, API reference, and 20 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: journalize-dev API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: journalize-dev-rules
scopes:
- name: Journalize Dev Scopes
  scope_count: 0
  slug: journalize-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 49.4
    developer_ergonomics: 32.6
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Journalize Dev Authentication
  slug: journalize-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Journalize Dev Domain Security
  slug: journalize-dev-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Journalize Dev Vulnerability Disclosure
  slug: journalize-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: journalize-dev-basic
  slug: journalize-dev-basic
slug: journalize-dev
tags:
- Company
- Accounting
- AI
- FinTech
- Ledger
website: https://journalize.dev/
---
