---
access_model:
  confidence: medium
  label: Subscription requested through the Cat Digital Marketplace
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 20.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The Cat Digital Marketplace publishes a catalog of Caterpillar APIs spanning asset telematics, fleet management, fuel data, utilization, hours/odometer, and geofencing. Developers subscribe via the Ca
  name: Cat Digital Marketplace API
  slug: cat-digital-marketplace-api
- description: Caterpillar's implementation of the ISO 15143-3 (AEMP 2.0) mixed-fleet telematics standard. Publishes Fleet Snapshot (/fleet/{pageNumber}), Equipment Snapshot (/equipment/{equipmentId}) and Timeseries
  name: ISO 15143-3 (AEMP 2.0) API
  slug: iso-15143-3-aemp-api
- description: 'The next-generation VisionLink APIs let dealers and customers pull the fleet data VisionLink reports without mining it out of the application — Assets Operation, Assets Summary, Faults History, Asset '
  name: VisionLink APIs
  slug: visionlink-apis
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caterpillar-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/caterpillar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/caterpillar
- group: auth
  title: ''
  type: Authentication
  url: authentication/caterpillar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/caterpillar-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/caterpillar-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/caterpillar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caterpillar-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/caterpillar-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caterpillar-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/caterpillar-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/caterpillar-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/caterpillar-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/caterpillar-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/caterpillar-openid-configuration.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caterpillar-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/caterpillar-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/caterpillar-mcp.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caterpillar-inc
- group: company
  title: ''
  type: Website
  url: https://www.caterpillar.com/
- group: start
  title: ''
  type: Portal
  url: https://digital.cat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://digital.cat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://digital.cat.com/api-catalog-overview
- group: docs
  title: ''
  type: APIReference
  url: https://digital.cat.com/development-guidelines
- group: start
  title: ''
  type: GettingStarted
  url: https://digital.cat.com/knowledge-hub/documentation/develop-cat-apis-getting-started
- group: build
  title: ''
  type: Postman
  url: https://digital.cat.com/knowledge-hub/document/iso-15143-3-aemp-20-api-postman-collection
- group: operate
  title: ''
  type: ChangeLog
  url: https://digital.cat.com/release-notes-manager
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CaterpillarInc
- group: company
  title: ''
  type: About
  url: https://www.caterpillar.com/en/company.html
- group: company
  title: ''
  type: Careers
  url: https://www.caterpillar.com/en/careers.html
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.caterpillar.com/en/investors.html
- group: operate
  title: ''
  type: PressReleases
  url: https://www.caterpillar.com/en/news.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.caterpillar.com/en/news.html
- group: operate
  title: ''
  type: Support
  url: https://digital.cat.com/knowledge-hub/faq
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.caterpillar.com/en/support.html
- group: operate
  title: ''
  type: Contact
  url: https://www.caterpillar.com/en/support/contact-us.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://digital.cat.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://digital.cat.com/privacy
- group: other
  title: ''
  type: Sitemap
  url: https://www.caterpillar.com/en/sitemap.html
created: '2026-03-21'
description: 'Caterpillar Inc. (NYSE: CAT) is the world''s leading manufacturer of construction and mining equipment, off-highway diesel and natural gas engines, industrial gas turbines, and diesel-electric locomotives. Its digital arm, Cat Digital, publishes developer APIs through the Cat Digital Marketplace (digital.cat.com) covering fleet, asset, fuel, and worksite telematics built on top of the Cat Connect and VisionLink data platforms. The callable surface runs on an Apigee gateway at services.cat.com (mirrored at api.cat.com) and is authorized by a PingFederate OAuth 2.0 / OpenID Connect authorization server at fedlogin.cat.com. Caterpillar implements the ISO 15143-3 (AEMP 2.0) mixed-fleet telematics standard, so a consumer that already speaks AEMP can read Cat machine data with no bespoke connector.'
finops:
- name: Caterpillar Finops
  service_category: Equipment Telematics + Fleet Data
  slug: caterpillar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caterpillar.png
layout: provider
modified: '2026-09-05'
name: Caterpillar
nav: Providers
network: true
overview: 'Caterpillar publishes 2 APIs on the [APIs.io](https://apis.io/) network: ISO 15143-3 (AEMP 2.0) API and VisionLink APIs. Tagged areas include Construction, Engines, Fortune 500, Heavy Equipment, and Locomotives.


  Caterpillar''s developer surface includes authentication, changelog, developer portal, documentation, API reference, getting-started guide, support, and 32 more developer resources.'
plans:
- name: Caterpillar Plans Pricing
  plan_count: 1
  slug: caterpillar-plans-pricing
press:
- date: '2026-05-25'
  title: Caterpillar Teams With NVIDIA to Revolutionize Heavy ...
  url: https://www.prnewswire.com/news-releases/caterpillar-teams-with-nvidia-to-revolutionize-heavy-industry-with-physical-ai-and-robotics-302655427.html
- date: '2026-05-25'
  title: Caterpillar isn't just adapting to the future, we're actively ...
  url: https://www.facebook.com/caterpillarinc/posts/caterpillar-isnt-just-adapting-to-the-future-were-actively-building-it-solving-o/1322800776550953/
- date: '2026-05-25'
  title: 'Artificial Intelligence: Transforming the Way We Help Our ...'
  url: https://www.caterpillar.com/en/news/caterpillarNews/2026/ai-transforming-way-we-help-customers.html
- date: '2026-05-25'
  title: Caterpillar pledges $100M to upskill workforce in AI era
  url: https://www.manufacturingdive.com/news/caterpillar-pledges-100-million-to-upskill-workforce-ai-era-centennial/746046/
- date: '2026-05-25'
  title: Corporate Press Releases
  url: https://www.caterpillar.com/en/news/corporate-press-releases.html
random_paper: 16
rate_limits:
- limit_count: 4
  name: Caterpillar Rate Limits
  slug: caterpillar-rate-limits
scopes:
- name: Caterpillar Scopes
  scope_count: 13
  slug: caterpillar-scopes
  summary_line: 13 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.0
    catalog_earned_first_party: 20.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 21.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 19.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/caterpillar/refs/heads/main/screenshots/caterpillar-2026-06-20T174051.png
security:
- kind: authentication
  name: Caterpillar Authentication
  slug: caterpillar-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Caterpillar Domain Security
  slug: caterpillar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Caterpillar Vulnerability Disclosure
  slug: caterpillar-vulnerability-disclosure
  summary_line: Hackerone
slug: caterpillar
tags:
- Construction
- Engines
- Fortune 500
- Heavy Equipment
- Locomotives
- Manufacturing
- Mining
- Telematics
- Fleet Management
- ISO 15143-3
- AEMP
website: https://www.caterpillar.com/
---
