---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Inbound custom webhook triggers that start Rewst workflows. An external system sends an HTTP request (method configured per trigger) to a per-trigger URL; the normalized payload ({body, headers, metho
  name: Rewst Webhook Triggers
  slug: rewst-webhook-triggers
artifact_total: 9
asyncapis:
- description: ''
  name: Rewst Webhooks
  slug: rewst-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/rewst/plans/rewst-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rewst-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://rewst.io/resources/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://rewst.io/resources/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://rewst.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rewst.help/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rewst.help/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rewst.help/readme.md
- group: operate
  title: ''
  type: Support
  url: https://rewst.io/support/community
- group: company
  title: ''
  type: Blog
  url: https://rewst.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RewstApp
- group: commercial
  title: ''
  type: Pricing
  url: https://rewst.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.rewst.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rewst.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rewst.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rewst.io/
- group: auth
  href: https://artifacts.apis.io/rewst/security/rewst-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rewst-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://rewst.io/trust-center
- group: auth
  title: ''
  type: Security
  url: https://rewst.io/vulnerability-disclosure
- group: auth
  href: https://artifacts.apis.io/rewst/security/rewst-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rewst-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rewst/security/rewst-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rewst-domain-security.yml
- group: design
  href: https://artifacts.apis.io/rewst/asyncapi/rewst-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rewst-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/rewst/authentication/rewst-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rewst-authentication.yml
- group: operate
  href: https://artifacts.apis.io/rewst/rate-limits/rewst-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rewst-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/rewst/conventions/rewst-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rewst-conventions.yml
- group: design
  href: https://artifacts.apis.io/rewst/errors/rewst-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rewst-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rewst/lifecycle/rewst-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rewst-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rewst/conformance/rewst-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rewst-conformance.yml
- group: build
  href: https://artifacts.apis.io/rewst/packages/rewst-packages.yml
  title: ''
  type: Packages
  url: packages/rewst-packages.yml
- group: design
  href: https://artifacts.apis.io/rewst/components/rewst-components.yml
  title: ''
  type: Components
  url: components/rewst-components.yml
- group: agent
  href: https://artifacts.apis.io/rewst/well-known/rewst-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rewst-well-known.yml
- group: agent
  href: https://artifacts.apis.io/rewst/llms/rewst-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rewst-llms.txt
created: '2026-07-17'
description: Rewst is a workflow automation and integration (iPaaS/RPA) platform built specifically for managed service providers (MSPs). It combines a visual workflow builder, a form builder, an app builder, 90+ managed MSP integrations (PSA, RMM, Microsoft 365, security tools), reusable automation packages called Crates, and RoboRewsty, an AI assistant, so MSP teams can automate repetitive operational tasks. Rewst's primary programmatic surface is inbound custom webhook triggers that start workflows, authenticated with an optional x-rewst-secret header and rate limited per trigger; it also offers a Generic GraphQL request action for calling external APIs from within workflows. Rewst is SOC 2 Type 2 compliant, publishes a live status page, and runs a Bugcrowd vulnerability-disclosure program. Backed by Sapphire Ventures.
finops:
- has_sources: true
  method: derived
  name: Rewst Finops
  primary_unit: ''
  service_category: ''
  slug: rewst-finops
  template: true
image: https://avatars.githubusercontent.com/u/75550907?v=4
layout: provider
modified: '2026-10-06'
name: Rewst
nav: Providers
network: true
overview: 'Rewst is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Automation, iPaaS, and RPA.


  The Rewst catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rewst''s developer surface includes engineering blog, documentation, getting-started guide, support, pricing, authentication, and 25 more developer resources.'
plans:
- name: Rewst Plans Pricing
  plan_count: 0
  slug: rewst-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Rewst Rate Limits
  slug: rewst-rate-limits
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 50.0
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 49.6
  provenance:
    conformance: first-party
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rewst/rewst-2026-08-17T081551.png
security:
- kind: authentication
  name: Rewst Authentication
  slug: rewst-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Rewst Domain Security
  slug: rewst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rewst Vulnerability Disclosure
  slug: rewst-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Rewst Trust Center
  slug: rewst-trust-center
  summary_line: SOC 2, GDPR
slug: rewst
tags:
- Company
- DevOps
- Automation
- iPaaS
- RPA
- Workflow Automation
- MSP
- Integration
- Webhook
website: https://rewst.io/
---
