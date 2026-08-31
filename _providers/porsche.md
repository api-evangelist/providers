---
access_model:
  confidence: high
  label: Partner Only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.porsche.com/faq
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'The Porsche ID API Portal is where Porsche AG publishes and manages the APIs that integrate Porsche ID, its customer identity platform. It is not a public API programme: the portal''s own FAQ states "W'
  name: Porsche
  slug: porsche
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.porsche.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/porsche-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/porsche-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/porscheofficial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/porsche-ag
- group: start
  title: ''
  type: Portal
  url: https://developer.porsche.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.porsche.com/terms
- group: agent
  title: ''
  type: WellKnown
  url: well-known/porsche-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/porsche-security.txt
- group: auth
  title: ''
  type: Security
  url: security/porsche-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/porsche-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/porsche-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/porsche-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/porsche-packages.yml
- group: design
  title: ''
  type: Components
  url: components/porsche-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/porsche-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/porsche-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/porsche-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/porsche-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/porsche-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/porsche-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/porsche-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://designsystem.porsche.com/v4/
- group: operate
  title: ''
  type: Support
  url: https://developer.porsche.com/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.porsche.com/privacy-policy
created: '2025-02-25'
description: Porsche is a luxury car manufacturer known for producing high-performance sports cars, sedans, and SUVs. Founded in 1931 by Ferdinand Porsche, the brand has a long history of engineering excellence and precision craftsmanship. Porsche vehicles are renowned for their sleek design, exceptional handling, and powerful engines, making them a favorite among driving enthusiasts around the world.
finops:
- name: Porsche Finops
  service_category: API
  slug: porsche-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/porsche.png
layout: provider
modified: '2026-08-27'
name: Porsche
nav: Providers
network: true
overview: 'Porsche publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Cars, Vehicles, Automotive, and Connected Car.


  Porsche''s developer surface includes developer portal, authentication, changelog, documentation, support, and 21 more developer resources.'
plans:
- name: Porsche Plans Pricing
  plan_count: 0
  slug: porsche-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Porsche Rate Limits
  slug: porsche-rate-limits
scopes:
- name: Porsche Scopes
  scope_count: 0
  slug: porsche-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 36.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 28.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/porsche/refs/heads/main/screenshots/porsche-2026-06-20T191922.png
security:
- kind: authentication
  name: Porsche Authentication
  slug: porsche-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Porsche Domain Security
  slug: porsche-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Porsche Vulnerability Disclosure
  slug: porsche-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: porsche
tags:
- Automobiles
- Cars
- Vehicles
- Automotive
- Connected Car
- Identity
- OpenID Connect
- Design System
- Open-Source
- Germany
website: https://www.porsche.com/
---
