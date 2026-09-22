---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-21'
api_count: 2
apis:
- description: 'Token-based REST API for managing first-party data, building and editing audience segments, activating audiences, and retrieving behavior and audience analytics on the Lotame Spherical platform. JSON '
  name: Lotame Admin Services API
  slug: lotame-admin-services-api
- description: 'Real-time server-side API that returns the assigned Panorama ID for an IP address and user-agent (web) or Mobile Advertiser ID / MAID (mobile app). JSON POST to sid.crwdcntrl.net/sid, identified by a '
  name: Panorama ID Server-Side API
  slug: panorama-id-server-side-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.lotame.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.lotame.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.lotame.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://my.lotame.com/category/administrative-api
- group: operate
  title: ''
  type: Support
  url: https://www.cognitoforms.com/LotameSolutionsInc/SupportTicketForm
- group: start
  title: ''
  type: SignUp
  url: https://my.lotame.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.lotame.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lotame.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lotame.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lotame.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/authentication/lotame-solutions-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lotame-solutions-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/conventions/lotame-solutions-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lotame-solutions-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/errors/lotame-solutions-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lotame-solutions-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/lifecycle/lotame-solutions-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lotame-solutions-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/conformance/lotame-solutions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lotame-solutions-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/security/lotame-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lotame-solutions-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/mcp/lotame-solutions-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lotame-solutions-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/llms/lotame-solutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lotame-solutions-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/packages/lotame-solutions-packages.yml
  title: ''
  type: Packages
  url: packages/lotame-solutions-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/packages/lotame-solutions-packages.yml
  title: ''
  type: SDKs
  url: packages/lotame-solutions-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/components/lotame-solutions-components.yml
  title: ''
  type: Components
  url: components/lotame-solutions-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/data-model/lotame-solutions-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lotame-solutions-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/plans/lotame-solutions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lotame-solutions-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/rate-limits/lotame-solutions-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lotame-solutions-rate-limits.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lotame.com/legal/eu-privacy-consent-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lotame
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Lotame/api-examples
created: '2026-07-17'
description: Lotame Solutions is a data collaboration and identity company for digital marketing and advertising. Its Spherical platform lets marketers, agencies, and publishers connect, enrich, and activate first- and third-party audience data, while Panorama ID delivers a privacy-first, cookieless identity for addressability across web, mobile app, and CTV. Lotame exposes a token-based Admin Services REST API (api.lotame.com/2/) for managing first-party data, building audiences, and pulling behavior and audience statistics, plus a server-side Panorama ID resolution API on sid.crwdcntrl.net for web and mobile (MAID) identity lookups. Lotame operates across 24 countries and was acquired by Publicis Groupe.
image: https://cdn-ilbibgp.nitrocdn.com/eakWUVxgVLoymIJUurpQZcwTweYHDeju/assets/images/optimized/rev-6d2d189/www.lotame.com/wp-content/uploads/2025/05/lotame-website-favicon-300x300.png
layout: provider
modified: '2026-08-13'
name: Lotame Solutions
nav: Providers
network: true
overview: 'Lotame Solutions publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Management Platform, Identity, Advertising, and Marketing.


  Lotame Solutions'' developer surface includes documentation, API reference, support, signup flow, engineering blog, authentication, and 21 more developer resources.'
plans:
- name: Lotame Solutions Plans Pricing
  plan_count: 0
  slug: lotame-solutions-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Lotame Solutions Rate Limits
  slug: lotame-solutions-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    operational_transparency: 2.6
  previous_composite: 26.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/screenshots/lotame-solutions-2026-07-25T225550.png
security:
- kind: authentication
  name: Lotame Solutions Authentication
  slug: lotame-solutions-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lotame Solutions Domain Security
  slug: lotame-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lotame-solutions
tags:
- Company
- Data Management Platform
- Identity
- Advertising
- Marketing
- Audience Data
- Data Collaboration
- AdTech
website: https://www.lotame.com/
---
