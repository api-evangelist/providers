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
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://your-instance.c15t.dev
  baseurl_source: declared
  description: Search the public c15t documentation corpus.
  name: Inth Documentation API
  slug: inth-documentation-api
- baseURL: https://your-instance.c15t.dev
  baseurl_source: declared
  description: Check whether the c15t documentation application is available.
  name: Inth Operations API
  slug: inth-operations-api
artifact_total: 14
collections:
- collection_type: open
  name: c15t Backend Consent API
  slug: open-inth-consent-api
- collection_type: open
  name: c15t Backend Consent Init API
  slug: open-inth-init-api
- collection_type: open
  name: c15t Backend Consent Legal Documents API
  slug: open-inth-legal-documents-api
- collection_type: open
  name: c15t Backend Consent Status API
  slug: open-inth-status-api
- collection_type: open
  name: c15t Backend Consent Subjects API
  slug: open-inth-subjects-api
common:
- group: commercial
  href: https://artifacts.apis.io/inth/plans/inth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inth-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/inth/capabilities/inth-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/inth-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/inth/overlays/inth-c15t-consent-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/inth-c15t-consent-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/inth/a2a/inth-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/inth-a2a.yml
- group: auth
  href: https://artifacts.apis.io/inth/security/inth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inth-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://c15t.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://c15t.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://c15t.com/docs/self-host
- group: start
  title: ''
  type: Quickstart
  url: https://c15t.com/docs/frameworks/react/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/c15t
- group: commercial
  title: ''
  type: Pricing
  url: https://inth.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://inth.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://inth.com/dashboard/sign-up
- group: operate
  title: ''
  type: Support
  url: https://github.com/c15t/c15t/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://c15t.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inth.com
- group: operate
  href: https://artifacts.apis.io/inth/lifecycle/inth-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/inth-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/inth/lifecycle/inth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/inth-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/inth/packages/inth-packages.yml
  title: ''
  type: Packages
  url: packages/inth-packages.yml
- group: build
  href: https://artifacts.apis.io/inth/packages/inth-packages.yml
  title: ''
  type: SDKs
  url: packages/inth-packages.yml
- group: build
  href: https://artifacts.apis.io/inth/cli/inth-cli.yml
  title: ''
  type: CLI
  url: cli/inth-cli.yml
- group: design
  href: https://artifacts.apis.io/inth/components/inth-components.yml
  title: ''
  type: Components
  url: components/inth-components.yml
- group: design
  href: https://artifacts.apis.io/inth/conventions/inth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/inth-conventions.yml
- group: auth
  href: https://artifacts.apis.io/inth/authentication/inth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inth-authentication.yml
- group: design
  href: https://artifacts.apis.io/inth/errors/inth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inth-problem-types.yml
- group: design
  href: https://artifacts.apis.io/inth/conformance/inth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inth-conformance.yml
- group: auth
  href: https://artifacts.apis.io/inth/conformance/inth-conformance.yml
  title: ''
  type: Compliance
  url: conformance/inth-conformance.yml
- group: design
  href: https://artifacts.apis.io/inth/data-model/inth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inth-data-model.yml
- group: operate
  href: https://artifacts.apis.io/inth/changelog/inth-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/inth-changelog.yml
- group: agent
  href: https://artifacts.apis.io/inth/mcp/inth-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/inth-mcp.yml
- group: agent
  href: https://artifacts.apis.io/inth/llms/inth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inth-llms.txt
- group: agent
  href: https://artifacts.apis.io/inth/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/inth/well-known/inth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inth-well-known.yml
- group: start
  href: https://artifacts.apis.io/inth/sandbox/inth-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/inth-sandbox.yml
created: '2026-07-17'
description: Inth is a San Francisco, Y Combinator-backed company building enterprise privacy governance for teams that ship fast, making consent programmable, observable, and compliant by default. Its foundation is c15t (github.com/c15t), an open-source, developer-first consent management platform with 3M+ npm downloads used by teams like Zed, Expo, Infisical, and Unkey. c15t provides a headless, composable cookie banner, consent manager, and preference center for JavaScript, React, and Next.js, plus a self-hostable consent backend and REST API (@c15t/backend) that also runs as the inth.com managed service. It supports GDPR, CCPA, LGPD, IAB TCF 2.3, Google Consent Mode v2, and Global Privacy Control, with regional policy packs, audit-ready consent records, script and iframe gating, and first-party SDKs and CLI.
finops:
- has_sources: true
  method: derived
  name: Inth Finops
  primary_unit: ai credit
  service_category: ''
  slug: inth-finops
  template: false
image: https://inth.com/opengraph-image.png
layout: provider
modified: '2026-07-19'
name: Inth
nav: Providers
network: true
overview: 'Inth publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Documentation API and Operations API. Tagged areas include Company, Consent Management, Privacy, Cookie Consent, and GDPR.


  The Inth catalog on APIs.io includes 1 Spectral governance ruleset.


  Inth''s developer surface includes documentation, API reference, quickstart, pricing, engineering blog, signup flow, support, and 27 more developer resources.'
plans:
- name: Inth Plans Pricing
  plan_count: 10
  slug: inth-plans-pricing
- name: Inth Price Estimates
  plan_count: 0
  slug: inth-price-estimates
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Inth API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: inth-rules
score:
  band: strong
  composite: 60.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 48.8
    developer_ergonomics: 85.7
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 60.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 25.0
      total: 8
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: BR
      standard: lgpd
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 3
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/inth/inth-2026-07-25T222721.png
security:
- kind: authentication
  name: Inth Authentication
  slug: inth-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Inth Domain Security
  slug: inth-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: c15t
  slug: inth-c15t
slug: inth
tags:
- Company
- Consent Management
- Privacy
- Cookie Consent
- GDPR
- CCPA
- Compliance
- Consent
- Developer Tools
- Open Source
- A2A
website: https://c15t.com/docs
---
