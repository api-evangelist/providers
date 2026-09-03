---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The authentication, session, organization and admin API behind the Nickelytics / R-Ads Ad Manager. It is a Better Auth instance whose auto-generated OpenAPI 3.1.1 document is served publicly at /api/a
  name: Nickelytics R-Ads Platform Authentication API
  slug: nickelytics-r-ads-platform-authentication-api
artifact_total: 5
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/kiwibot/
- group: company
  title: ''
  type: Website
  url: https://nickelytics.com/
- group: operate
  title: ''
  type: Support
  url: https://www.robot.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.robot.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.robot.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://admanager.robot.com/
- group: company
  title: ''
  type: Blog
  url: https://robots.nickelytics.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nickelytics
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nickelytics-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nickelytics-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nickelytics-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/nickelytics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nickelytics-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/nickelytics-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nickelytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nickelytics-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Nickelytics is a data-driven out-of-home (OOH) and digital-out-of-home (DOOH) advertising platform that turns moving assets into measurable media. It wraps gig-economy and rideshare vehicles, autonomous sidewalk delivery robots, and e-scooters with brand campaigns, then layers geo-targeting, programmatic DOOH buying, route verification, proof-of-play, and performance reporting into a single campaign dashboard. Nickelytics was acquired by Kiwibot for roughly $25M in September 2024; Kiwibot rebranded to Robot.com in 2025 and Nickelytics now ships as the "R-Ads" advertising product, a self-serve suite covering robot media (RDOOH), vehicle wraps (MOOH) and digital screens (DOOH), bought through the R-Ads Ad Manager at admanager.robot.com. Nickelytics publishes no developer portal, API reference or SDKs. The only machine-readable contract it serves is the platform authentication API — a Better Auth instance whose OpenAPI 3.1.1 document is public at api.nickelytics.com and api-ads.robot.com
  — while the campaign/reporting surface behind /v1 is authenticated and undocumented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nickelytics.png
layout: provider
modified: '2026-08-12'
name: Nickelytics
nav: Providers
network: true
overview: 'Nickelytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, OOH, DOOH, and Programmatic Advertising.


  Nickelytics'' developer surface includes support, signup flow, engineering blog, and 14 more developer resources.'
plans:
- name: Nickelytics Plans Pricing
  plan_count: 0
  slug: nickelytics-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Nickelytics Rate Limits
  slug: nickelytics-rate-limits
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 19.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nickelytics/refs/heads/main/screenshots/nickelytics-2026-08-07T185252.png
security:
- kind: authentication
  name: Nickelytics Authentication
  slug: nickelytics-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Nickelytics Domain Security
  slug: nickelytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nickelytics
tags:
- Company
- Advertising
- OOH
- DOOH
- Programmatic Advertising
- Mobility
- Robotics
- Rideshare
- AdTech
- Authentication
website: https://nickelytics.com/
---
