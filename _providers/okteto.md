---
access_model:
  confidence: high
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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Okteto Agentic Access
  operation_count: 2
  slug: okteto-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://{oktetoURL}/api/v0
  baseurl_source: declared
  description: Operations about applications
  name: Okteto Applications API
  slug: okteto-applications-api
- baseURL: https://{oktetoURL}/api/v0
  baseurl_source: declared
  description: Operations about namespaces (Development or Preview)
  name: Okteto Namespaces API
  slug: okteto-namespaces-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/okteto/agentic-access/okteto-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/okteto-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/okteto/plans/okteto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/okteto-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/okteto/rules/okteto-rules.yml
  title: ''
  type: Spectral
  url: rules/okteto-rules.yml
- group: design
  href: https://artifacts.apis.io/okteto/json-ld/okteto-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/okteto-context.jsonld
- group: design
  href: https://artifacts.apis.io/okteto/vocabulary/okteto-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/okteto-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/okteto/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/okteto/data-model/okteto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/okteto-data-model.yml
- group: build
  href: https://artifacts.apis.io/okteto/cli/okteto-cli.yml
  title: ''
  type: CLI
  url: cli/okteto-cli.yml
- group: operate
  href: https://artifacts.apis.io/okteto/changelog/okteto-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/okteto-changelog.yml
- group: design
  href: https://artifacts.apis.io/okteto/conventions/okteto-conventions.yml
  title: ''
  type: Conventions
  url: conventions/okteto-conventions.yml
- group: start
  href: https://artifacts.apis.io/okteto/sandbox/okteto-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/okteto-sandbox.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.okteto.com/docs/release-notes/
- group: design
  href: https://artifacts.apis.io/okteto/lifecycle/okteto-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/okteto-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/okteto/errors/okteto-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/okteto-problem-types.yml
- group: design
  href: https://artifacts.apis.io/okteto/conformance/okteto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/okteto-conformance.yml
- group: other
  href: https://artifacts.apis.io/okteto/overlays/okteto-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/okteto-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/okteto/llms/okteto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/okteto-llms.txt
- group: auth
  href: https://artifacts.apis.io/okteto/well-known/okteto-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/okteto-security.txt
- group: auth
  href: https://artifacts.apis.io/okteto/well-known/okteto-okteto-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/okteto-okteto-security.txt
- group: agent
  href: https://artifacts.apis.io/okteto/well-known/okteto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/okteto-well-known.yml
- group: other
  href: https://artifacts.apis.io/okteto/hosts/okteto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/okteto-hosts.yml
- group: other
  href: https://artifacts.apis.io/okteto/vendors/okteto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/okteto-vendors.yml
- group: build
  href: https://artifacts.apis.io/okteto/packages/okteto-packages.yml
  title: ''
  type: SDKs
  url: packages/okteto-packages.yml
- group: build
  href: https://artifacts.apis.io/okteto/packages/okteto-packages.yml
  title: ''
  type: Packages
  url: packages/okteto-packages.yml
- group: auth
  href: https://artifacts.apis.io/okteto/authentication/okteto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/okteto-authentication.yml
- group: auth
  href: https://artifacts.apis.io/okteto/security/okteto-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/okteto-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/okteto/security/okteto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/okteto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://okteto.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.okteto.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.okteto.com/docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.okteto.com/docs/get-started/install/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.okteto.com/docs/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.okteto.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/okteto
- group: commercial
  title: ''
  type: Pricing
  url: https://www.okteto.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.okteto.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.okteto.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://community.okteto.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.okteto.com/contact/
- group: auth
  title: ''
  type: Security
  url: https://www.okteto.com/security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.okteto.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.okteto.com/privacy-policy/
created: '2026-10-18'
description: 'Okteto is a development-environment platform built on Kubernetes. Its site says it "gives coding agents production-like environments to verify their work": isolated, full-stack environments that run on your own infrastructure. Teams use it for Kubernetes development environments, preview environments and testing of cloud-native applications. Okteto publishes an open-source CLI (github.com/okteto/okteto), reference documentation, release notes and a community forum.'
image: https://www.okteto.com/okteto-meta-image.png
json_schemas:
- name: Application
  property_count: 8
  slug: okteto-application
- name: Namespace
  property_count: 8
  slug: okteto-namespace
jsonld:
- class_count: 3
  name: Okteto Context
  property_count: 12
  slug: okteto-context
layout: provider
modified: '2026-10-18'
name: Okteto
nav: Providers
network: true
overview: 'Okteto publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Applications API and Namespaces API. Tagged areas include Company, Kubernetes, Developer Environments, Cloud-Native, and Developer Tools.


  The Okteto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Okteto''s developer surface includes CLI, changelog, sandbox, authentication, documentation, API reference, getting-started guide, and 35 more developer resources.'
plans:
- name: Okteto Plans Pricing
  plan_count: 3
  slug: okteto-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Okteto Rate Limits
  slug: okteto-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Okteto API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: okteto-rules
scopes:
- name: Okteto Scopes
  scope_count: 0
  slug: okteto-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 58.7
    developer_ergonomics: 58.3
    discoverability: 73.2
    operational_transparency: 19.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 65.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/okteto/okteto-2026-11-03T140509.png
security:
- kind: authentication
  name: Okteto Authentication
  slug: okteto-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Okteto Domain Security
  slug: okteto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Okteto Vulnerability Disclosure
  slug: okteto-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: okteto-debugging
  slug: okteto-debugging
- name: okteto-manifest-optimizer
  slug: okteto-manifest-optimizer
- name: okteto-onboarding
  slug: okteto-onboarding
- name: okteto-preview
  slug: okteto-preview
- name: okteto
  slug: okteto
slug: okteto
tags:
- Company
- Kubernetes
- Developer Environments
- Cloud-Native
- Developer Tools
- Preview Environments
- AI Agents
- CLI
website: https://okteto.com
---
