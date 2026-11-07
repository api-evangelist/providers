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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI-native platform for legal technology offering various services.
  name: Case.dev API
  slug: case-dev-api
- baseURL: https://api.case.dev
  baseurl_source: declared
  description: The AI-native platform for legal technology. Build smarter legal applications with our suite of AI-powered APIs.
  name: Case.dev API API
  slug: case-dev-api-api
artifact_total: 9
asyncapis:
- description: ''
  name: Casedev Webhooks
  slug: casedev-webhooks
common:
- group: design
  href: https://artifacts.apis.io/casedev/rules/casedev-rules.yml
  title: ''
  type: Spectral
  url: rules/casedev-rules.yml
- group: design
  href: https://artifacts.apis.io/casedev/json-ld/casedev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/casedev-context.jsonld
- group: design
  href: https://artifacts.apis.io/casedev/vocabulary/casedev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/casedev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/casedev/conventions/casedev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/casedev-conventions.yml
- group: design
  href: https://artifacts.apis.io/casedev/conventions/casedev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/casedev-conventions.yml
- group: design
  href: https://artifacts.apis.io/casedev/conformance/casedev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/casedev-conformance.yml
- group: design
  href: https://artifacts.apis.io/casedev/asyncapi/casedev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/casedev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/casedev/data-model/casedev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/casedev-data-model.yml
- group: build
  href: https://artifacts.apis.io/casedev/cli/casedev-cli.yml
  title: ''
  type: CLI
  url: cli/casedev-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://case.dev/
- group: auth
  href: https://artifacts.apis.io/casedev/authentication/casedev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/casedev-authentication.yml
- group: design
  href: https://artifacts.apis.io/casedev/errors/casedev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/casedev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/casedev/llms/casedev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/casedev-llms.txt
- group: other
  href: https://artifacts.apis.io/casedev/a2a/casedev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/casedev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/casedev/well-known/casedev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/casedev-well-known.yml
- group: other
  href: https://artifacts.apis.io/casedev/hosts/casedev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/casedev-hosts.yml
- group: other
  href: https://artifacts.apis.io/casedev/vendors/casedev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/casedev-vendors.yml
- group: build
  href: https://artifacts.apis.io/casedev/packages/casedev-packages.yml
  title: ''
  type: SDKs
  url: packages/casedev-packages.yml
- group: build
  href: https://artifacts.apis.io/casedev/packages/casedev-packages.yml
  title: ''
  type: Packages
  url: packages/casedev-packages.yml
- group: auth
  href: https://artifacts.apis.io/casedev/security/casedev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/casedev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/casedev/security/casedev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/casedev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://case.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.case.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.case.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.case.dev/getting-started/index.md
- group: company
  title: ''
  type: Blog
  url: https://casemark.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CaseMark
- group: commercial
  title: ''
  type: TermsOfService
  url: https://case.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://case.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://case.dev/contact
created: '2026-10-29'
description: Case.dev is a legal operating system for the agent era, providing a platform for AI‑driven legal workflows, compliance, jurisdiction, audit, and playbooks. It powers agents that automate case management, document summarization, and structured legal research, serving firms like Curi, Ogletree Deakins, and Nelson Mullins.
image: https://case.dev/og/home
jsonld:
- class_count: 1
  name: Casedev Context
  property_count: 1
  slug: casedev-context
layout: provider
modified: '2026-10-29'
name: Case.dev
nav: Providers
network: true
overview: 'Case.dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, Legal Tech, Artificial Intelligence, Platform, and Automation.


  The Case.dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Case.dev''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, support, and 23 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Casedev Rate Limits
  slug: casedev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Case.dev API Rules
  rule_count: 67
  severity_counts:
    error: 56
    hint: 0
    info: 2
    warn: 9
  slug: casedev-rules
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 48.3
    developer_ergonomics: 44.0
    discoverability: 73.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/casedev/casedev-2026-11-03T123438.png
security:
- kind: authentication
  name: Casedev Authentication
  slug: casedev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Casedev Domain Security
  slug: casedev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Casedev Trust Center
  slug: casedev-trust-center
  summary_line: SOC 2, HIPAA
slug: casedev
tags:
- Company
- Legal Tech
- Artificial Intelligence
- Platform
- Automation
website: https://case.dev/
---
