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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Axiomatics Agentic Access
  operation_count: 1
  slug: axiomatics-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: /
  baseurl_source: spec
  description: The authorize API from Axiomatics — 1 operation(s) for authorize.
  name: Axiomatics Authorize API
  slug: axiomatics-authorize-api
artifact_total: 7
common:
- group: other
  href: https://artifacts.apis.io/axiomatics/vendors/axiomatics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axiomatics-vendors.yml
- group: agent
  href: https://artifacts.apis.io/axiomatics/agentic-access/axiomatics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/axiomatics-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/axiomatics/rules/axiomatics-rules.yml
  title: ''
  type: Spectral
  url: rules/axiomatics-rules.yml
- group: design
  href: https://artifacts.apis.io/axiomatics/json-ld/axiomatics-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/axiomatics-context.jsonld
- group: design
  href: https://artifacts.apis.io/axiomatics/vocabulary/axiomatics-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/axiomatics-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/axiomatics/data-model/axiomatics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axiomatics-data-model.yml
- group: auth
  href: https://artifacts.apis.io/axiomatics/security/axiomatics-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/axiomatics-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/axiomatics/errors/axiomatics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/axiomatics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/axiomatics/conformance/axiomatics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axiomatics-conformance.yml
- group: agent
  href: https://artifacts.apis.io/axiomatics/llms/axiomatics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axiomatics-llms.txt
- group: agent
  href: https://artifacts.apis.io/axiomatics/well-known/axiomatics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axiomatics-well-known.yml
- group: other
  href: https://artifacts.apis.io/axiomatics/hosts/axiomatics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axiomatics-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.axiomatics.com/_hcms/mem/login?redirect_url=https%3A%2F%2Fsupport.axiomatics.com%2F
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axiomatics.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://axiomatics.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axiomatics
- group: company
  title: ''
  type: Blog
  url: https://axiomatics.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axiomatics.com/
- group: auth
  href: https://artifacts.apis.io/axiomatics/authentication/axiomatics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/axiomatics-authentication.yml
- group: auth
  href: https://artifacts.apis.io/axiomatics/security/axiomatics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/axiomatics-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/axiomatics/security/axiomatics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiomatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axiomatics.com/
created: '2026-10-27'
description: Axiomatics provides dynamic authorization solutions for applications, APIs, data and AI. Their platform enables fine-grained, policy-based access control across enterprise environments, supporting use cases in finance, healthcare, government, manufacturing and more. The company offers an Authorization Hub, Access Decision Services, and tools for policy authoring, enforcement, and governance, helping organizations implement zero‑trust and compliance frameworks.
image: https://axiomatics.com/wp-content/uploads/2026/09/axiomatics-logo.png
jsonld:
- class_count: 10
  name: Axiomatics Context
  property_count: 16
  slug: axiomatics-context
layout: provider
modified: '2026-10-27'
name: Axiomatics
nav: Providers
network: true
overview: 'Axiomatics publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Authorize API. Tagged areas include Company, Authorization, Policy, Zero Trust, and Compliance.


  The Axiomatics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Axiomatics'' developer surface includes support, engineering blog, documentation, authentication, and 18 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Axiomatics API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: axiomatics-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 20.2
    discoverability: 56.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/axiomatics/axiomatics-2026-11-03T121437.png
security:
- kind: authentication
  name: Axiomatics Authentication
  slug: axiomatics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Axiomatics Domain Security
  slug: axiomatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Axiomatics Vulnerability Disclosure
  slug: axiomatics-vulnerability-disclosure
  summary_line: no policy recorded
slug: axiomatics
tags:
- Company
- Authorization
- Policy
- Zero Trust
- Compliance
- Enterprise
website: https://axiomatics.com/
---
