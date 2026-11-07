---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The Audible Magic Content API is a lightweight method to obtain media files from Audible Magic''s Fulfillment services - an HTTP GET (with a cookie) taking a RetailerID, a ComponentID and an AssetType '
  name: Audible Magic Fulfillment Content API
  slug: fulfillment-content-api
- description: The Audible Magic Toolkit is a package of command-line programs (identify, analyze, identifyStream) for Linux, Windows and Mac that fingerprint unknown media files, package the fingerprints into an ID
  name: Audible Magic Identification Toolkit
  slug: identification-toolkit
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/audible-magic/rate-limits/audible-magic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/audible-magic-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/audible-magic/cli/audible-magic-cli.yml
  title: ''
  type: CLI
  url: cli/audible-magic-cli.yml
- group: design
  href: https://artifacts.apis.io/audible-magic/conventions/audible-magic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/audible-magic-conventions.yml
- group: auth
  href: https://artifacts.apis.io/audible-magic/authentication/audible-magic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audible-magic-authentication.yml
- group: design
  href: https://artifacts.apis.io/audible-magic/lifecycle/audible-magic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/audible-magic-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/audible-magic/errors/audible-magic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audible-magic-problem-types.yml
- group: other
  href: https://artifacts.apis.io/audible-magic/hosts/audible-magic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audible-magic-hosts.yml
- group: build
  href: https://artifacts.apis.io/audible-magic/integrations/audible-magic-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/audible-magic-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/audible-magic/vendors/audible-magic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audible-magic-vendors.yml
- group: auth
  href: https://artifacts.apis.io/audible-magic/security/audible-magic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audible-magic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.audiblemagic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.audiblemagic.com/implementing-audible-magic-services
- group: start
  title: ''
  type: GettingStarted
  url: https://support.audiblemagic.com/onboarding-overview-id-services
- group: operate
  title: ''
  type: Support
  url: https://support.audiblemagic.com/
- group: start
  title: ''
  type: Login
  url: https://support.audiblemagic.com/_hcms/mem/login
- group: company
  title: ''
  type: Blog
  url: https://www.audiblemagic.com/newsroom/news/
- group: company
  title: ''
  type: Newsroom
  url: https://www.audiblemagic.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.audiblemagic.com/company/leadership/
- group: operate
  title: ''
  type: Contact
  url: https://www.audiblemagic.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.audiblemagic.com/privacy-policy/
- group: commercial
  title: ''
  type: LicenseAgreement
  url: https://www.audiblemagic.com/software-license-agreement/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/audible-magic
created: '2026-10-18'
description: Audible Magic is an automatic content recognition (ACR) and rights administration company whose content identification technology is used by platforms such as Twitch, SoundCloud and Dailymotion. Its products include identification services (ID360, Social Check, Article 17 compliance), rights management and licensing (Rights360, RightsRX, Admin360) and music fulfillment (Fulfillment360, the Fulfillment Content API and Cleared Catalog data feed), with an Audible Magic Toolkit and help-desk documentation for implementing its services.
image: https://www.audiblemagic.com/wp-content/uploads/2019/08/AM-Logo.png
layout: provider
modified: '2026-10-18'
name: Audible Magic
nav: Providers
network: true
overview: 'Audible Magic is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automatic Content Recognition, Content Identification, Rights Management, and Music Licensing.


  Audible Magic''s developer surface includes CLI, authentication, documentation, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Audible Magic Plans Pricing
  plan_count: 0
  slug: audible-magic-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Audible Magic Rate Limits
  slug: audible-magic-rate-limits
scopes:
- name: Audible Magic Scopes
  scope_count: 0
  slug: audible-magic-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 58.9
    operational_transparency: 36.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/audible-magic/audible-magic-2026-11-03T121308.png
security:
- kind: authentication
  name: Audible Magic Authentication
  slug: audible-magic-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Audible Magic Domain Security
  slug: audible-magic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: audible-magic
tags:
- Company
- Automatic Content Recognition
- Content Identification
- Rights Management
- Music Licensing
- Copyright Compliance
- Audio Fingerprinting
website: https://www.audiblemagic.com/
---
