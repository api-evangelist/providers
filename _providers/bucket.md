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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Bucket Agentic Access
  operation_count: 12
  slug: bucket-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 1
apis:
- description: JSON-over-HTTP API browsers and backends use at runtime to fetch evaluated and enabled flags, and to send users, companies and feature-usage events. Publishable-key (client) or secret-key (server) bea
  name: Reflag Runtime API
  slug: reflag-runtime-api
- baseURL: https://app.reflag.com/api
  baseurl_source: declared
  description: The Apps API from Bucket — 9 operation(s) for apps.
  name: Bucket Apps API
  slug: bucket-apps-api
artifact_total: 14
collections:
- collection_type: open
  name: Reflag Management Apps API
  slug: open-bucket-apps-api
common:
- group: commercial
  href: https://artifacts.apis.io/bucket/plans/bucket-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bucket-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/bucket/capabilities/bucket-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bucket-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/bucket/overlays/bucket-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bucket-management-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/bucket/security/bucket-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bucket-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://reflag.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reflag.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reflag.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.reflag.com/api/reflag-rest-api/reflag-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reflag.com/welcome/readme
- group: company
  title: ''
  type: Blog
  url: https://reflag.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://reflag.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://reflag.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.reflag.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.reflag.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reflag.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reflag.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reflagcom
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reflag.com
- group: auth
  title: ''
  type: Security
  url: https://reflag.com/legal/security-policy
- group: auth
  title: ''
  type: Compliance
  url: https://reflag.com/security
- group: build
  href: https://artifacts.apis.io/bucket/packages/bucket-packages.yml
  title: ''
  type: Packages
  url: packages/bucket-packages.yml
- group: build
  href: https://artifacts.apis.io/bucket/packages/bucket-packages.yml
  title: ''
  type: SDKs
  url: packages/bucket-packages.yml
- group: build
  href: https://artifacts.apis.io/bucket/cli/bucket-cli.yml
  title: ''
  type: CLI
  url: cli/bucket-cli.yml
- group: agent
  href: https://artifacts.apis.io/bucket/mcp/bucket-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bucket-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bucket/llms/bucket-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bucket-llms.txt
- group: agent
  href: https://artifacts.apis.io/bucket/well-known/bucket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bucket-well-known.yml
- group: auth
  href: https://artifacts.apis.io/bucket/authentication/bucket-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bucket-authentication.yml
- group: design
  href: https://artifacts.apis.io/bucket/conventions/bucket-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bucket-conventions.yml
- group: design
  href: https://artifacts.apis.io/bucket/conformance/bucket-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bucket-conformance.yml
- group: design
  href: https://artifacts.apis.io/bucket/lifecycle/bucket-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bucket-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bucket/components/bucket-components.yml
  title: ''
  type: Components
  url: components/bucket-components.yml
- group: auth
  href: https://artifacts.apis.io/bucket/security/bucket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bucket-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bucket/security/bucket-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bucket-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bucket/agentic-access/bucket-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bucket-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/bucket/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Bucket (rebranded to Reflag in 2026, reflag.com) is a TypeScript-first feature management platform built for B2B SaaS teams. It provides feature flags with self-cleaning lifecycle automation, AI/agent integration via a hosted MCP server, strongly typed SDKs for React, React Native, Vue, Next.js, Node.js and the browser, OpenFeature providers, local flag evaluation for zero-latency and downtime protection, feature entitlements, in-app feedback collection, and deep integrations with Linear, Slack, GitHub, Datadog, Vercel and analytics tools. The platform exposes two APIs — a Runtime API for evaluating flags for users and companies at request time, and a Management API for programmatically managing apps, environments, flags and targeting rules from CI/CD. Backed by 500 Global and Creandum.
finops:
- has_sources: true
  method: derived
  name: Bucket Finops
  primary_unit: subscription
  service_category: ''
  slug: bucket-finops
  template: false
image: https://cdn.prod.website-files.com/68a872edf3df6064de547670/68b8414134c540f12c2928bc_reflag-dynamic-favicon.svg
layout: provider
modified: '2026-07-18'
name: Bucket
nav: Providers
network: true
overview: 'Bucket publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, and 1 more. Tagged areas include Company, Feature Flags, Feature Management, Feature Flagging, and Developer Tools.


  The Bucket catalog on APIs.io includes 1 Spectral governance ruleset.


  Bucket''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Bucket Plans Pricing
  plan_count: 3
  slug: bucket-plans-pricing
- name: Bucket Price Estimates
  plan_count: 0
  slug: bucket-price-estimates
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Bucket API Rules
  rule_count: 66
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 6
  slug: bucket-rules
score:
  band: strong
  composite: 66.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 53.6
    developer_ergonomics: 68.5
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 65.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/bucket/bucket-2026-07-25T204024.png
security:
- kind: authentication
  name: Bucket Authentication
  slug: bucket-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bucket Domain Security
  slug: bucket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bucket Vulnerability Disclosure
  slug: bucket-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Bucket Trust Center
  slug: bucket-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 2
skills:
- name: Create and configure a feature flag
  slug: bucket-create-and-configure-flag
- name: Target a flag to a company or user
  slug: bucket-target-company-and-user
slug: bucket
tags:
- Company
- Feature Flags
- Feature Management
- Feature Flagging
- Developer Tools
- Software-as-a-Service
- Entitlements
- Experimentation
- MCP
- Agent Ready
website: https://reflag.com
---
