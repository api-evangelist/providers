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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://community.tracebit.com
  baseurl_source: declared
  description: The Alerts API from Tracebit — 2 operation(s) for alerts.
  name: Tracebit Alerts API
  slug: tracebit-alerts-api
- baseURL: https://community.tracebit.com
  baseurl_source: declared
  description: The Canary Credentials API from Tracebit — 2 operation(s) for canary credentials.
  name: Tracebit Canary Credentials API
  slug: tracebit-canary-credentials-api
artifact_total: 14
collections:
- collection_type: open
  name: Tracebit Alerts API
  slug: open-tracebit-alerts-api
- collection_type: open
  name: Tracebit Alerts Canary Credentials API
  slug: open-tracebit-canary-credentials-api
common:
- group: commercial
  href: https://artifacts.apis.io/tracebit/plans/tracebit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tracebit-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/tracebit/capabilities/tracebit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tracebit-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://tracebit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://community.tracebit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://community.tracebit.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://community.tracebit.com/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/tracebit-com/tracebit-community-cli#getting-started
- group: operate
  title: ''
  type: Support
  url: https://tracebit.com/contact
- group: company
  title: ''
  type: Blog
  url: https://tracebit.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tracebit-com
- group: commercial
  title: ''
  type: Pricing
  url: https://tracebit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://community.tracebit.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tracebit.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tracebit.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tracebit.com/
- group: auth
  href: https://artifacts.apis.io/tracebit/security/tracebit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tracebit-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tracebit/security/tracebit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tracebit-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tracebit/authentication/tracebit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tracebit-authentication.yml
- group: design
  href: https://artifacts.apis.io/tracebit/conventions/tracebit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tracebit-conventions.yml
- group: design
  href: https://artifacts.apis.io/tracebit/errors/tracebit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tracebit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tracebit/conformance/tracebit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tracebit-conformance.yml
- group: design
  href: https://artifacts.apis.io/tracebit/lifecycle/tracebit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tracebit-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/tracebit/changelog/tracebit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tracebit-changelog.yml
- group: build
  href: https://artifacts.apis.io/tracebit/cli/tracebit-cli.yml
  title: ''
  type: CLI
  url: cli/tracebit-cli.yml
- group: build
  href: https://artifacts.apis.io/tracebit/packages/tracebit-packages.yml
  title: ''
  type: Packages
  url: packages/tracebit-packages.yml
- group: agent
  href: https://artifacts.apis.io/tracebit/well-known/tracebit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tracebit-well-known.yml
- group: design
  href: https://artifacts.apis.io/tracebit/data-model/tracebit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tracebit-data-model.yml
- group: other
  href: https://artifacts.apis.io/tracebit/overlays/tracebit-community-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tracebit-community-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/tracebit/mcp/tracebit-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tracebit-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tracebit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/tracebit/llms/tracebit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tracebit-llms.txt
created: '2026-07-17'
description: Tracebit is a security-canary (deception) platform backed by Accel. It deploys realistic decoy credentials, secrets, and identities — canaries — across AWS, Azure, Google Cloud, Okta, Kubernetes, CI/CD pipelines, and workstations, and raises high-fidelity alerts the moment an attacker touches one during lateral movement or credential access. The free Community Edition exposes a public REST API (OpenAPI 3.1) for issuing and confirming canary credentials and reading alerts and their logs, alongside an open-source CLI, a GitHub Action, and a provider-published Agent Skill.
finops:
- has_sources: true
  method: derived
  name: Tracebit Finops
  primary_unit: subscription
  service_category: ''
  slug: tracebit-finops
  template: false
image: https://cdn.prod.website-files.com/663e4960fd682070c6a1bfdc/6a16ecb79f26e0be2459ffbd_tracebit-opengraph-home.jpg
layout: provider
modified: '2026-07-21'
name: Tracebit
nav: Providers
network: true
overview: 'Tracebit publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Alerts API and Canary Credentials API. Tagged areas include Company, Cloud Saas, Security, Deception, and Canary Tokens.


  The Tracebit catalog on APIs.io includes 1 Spectral governance ruleset.


  Tracebit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Tracebit Plans Pricing
  plan_count: 3
  slug: tracebit-plans-pricing
- name: Tracebit Price Estimates
  plan_count: 0
  slug: tracebit-price-estimates
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Tracebit API Rules
  rule_count: 47
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 2
  slug: tracebit-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 56.5
    developer_ergonomics: 61.9
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 55.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tracebit/tracebit-2026-08-17T082426.png
security:
- kind: authentication
  name: Tracebit Authentication
  slug: tracebit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tracebit Domain Security
  slug: tracebit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tracebit Trust Center
  slug: tracebit-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: tracebit-canaries
  slug: tracebit-canary-honeytokens-skill
- name: Deploy Tracebit canary credentials
  slug: tracebit-deploy-canary-credentials
- name: Monitor Tracebit canary alerts
  slug: tracebit-monitor-canary-alerts
slug: tracebit
tags:
- Company
- Cloud Saas
- Security
- Deception
- Canary Tokens
- Threat Detection
- Cloud Security
- Incident Response
website: https://tracebit.com/
---
