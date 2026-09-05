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
  - sandbox
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
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: The ad-request surface Doceree publisher partners call to fetch an HCP-targeted advertisement. It is the endpoint behind the Doceree Publisher Tag, the first-party Prebid.js header-bidding adapter (bi
  name: Doceree Bidder / Ad Request API
  slug: bidder
- description: Doceree's measurement and beacon endpoint. The Prebid.js adapter fires GET /v1/hbTimeout and GET /v1/hbBidWon with a base64-encoded, URI-encoded JSON payload on the `data` query parameter and an `adp`
  name: Doceree Tracking API
  slug: tracking
- description: 'The current mobile ad-serving, identity and clinical-session surface, used by the Doceree iOS SDK 6.x. Discovered 2026-08-12 by reading Doceree''s own MIT-licensed first-party SDK (HTTPSupport.swift), '
  name: Doceree DAI Mobile Ad + Identity API
  slug: dai
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/doceree-trust-center.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/prebid/Prebid.js/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/prebid/Prebid.js/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/prebid/Prebid.js/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/prebid/Prebid.js/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doceree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doceree.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doceree.com/publishers
- group: docs
  title: ''
  type: Documentation
  url: https://support.doceree.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prebid.org/dev-docs/bidders/doceree.html
- group: operate
  title: ''
  type: Support
  url: https://support.doceree.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.doceree.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doceree
- group: start
  title: ''
  type: Login
  url: https://exchange.doceree.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doceree.com/us-terms-of-service-advertiser
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doceree.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://doceree.com/trust
- group: operate
  title: ''
  type: Contact
  url: https://doceree.com/contact
- group: build
  title: ''
  type: Packages
  url: packages/doceree-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/doceree-packages.yml
- group: design
  title: ''
  type: Components
  url: components/doceree-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/doceree-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doceree-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/doceree-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doceree-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doceree-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/doceree-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doceree-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/doceree-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/doceree-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/doceree-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/doceree-sandbox.yml
created: '2026-08-04'
description: 'Doceree Inc. is a US healthcare marketing technology company (Short Hills, New Jersey) operating a global network of physician-only platforms for programmatic messaging and point-of-care advertising to healthcare professionals. Its platform spans HCP programmatic, point-of-care, EHR, email, SMS, co-pay/affordability and account-based messaging channels, backed by a proprietary HCP identity-resolution graph. Doceree''s public, machine-readable surface is an advertising-technology one rather than a general-purpose developer API: a versioned ad-request/bidder endpoint (bidder.doceree.com/v1/adrequest), a tracking/beacon endpoint (tracking.doceree.com), a hosted publisher tag (the Doceree Publisher Tag, servedbydoceree.doceree.com/script/render-header.js), a first-party Prebid.js header-bidding adapter (bidder code "doceree", IAB Europe GVL ID 1063), and first-party mobile ad SDKs for iOS (CocoaPods) and Android (JitPack). A second, newer ad-serving generation runs concurrently
  on dai.doceree.com (POST /drs/* and /dop/*, unversioned) and is used by the iOS SDK 6.x; it carries clinical session, patient, prescription and action-event attributes onto the ad request itself. Doceree publishes no OpenAPI, AsyncAPI, GraphQL schema, MCP server or A2A agent card at any probed host as of August 2026, and no /.well-known/ document on any host.'
image: https://doceree.com/images/doceree-logo.svg
layout: provider
modified: '2026-08-12'
name: Doceree
nav: Providers
network: true
overview: 'Doceree publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Healthcare, Marketing, AdTech, and Programmatic.


  Doceree''s developer surface includes documentation, API reference, support, engineering blog, authentication, changelog, sandbox, and 25 more developer resources.'
plans:
- name: Doceree Plans Pricing
  plan_count: 0
  slug: doceree-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Doceree Rate Limits
  slug: doceree-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 50.0
  previous_composite: 38.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doceree/refs/heads/main/screenshots/doceree-2026-08-07T164451.png
security:
- kind: authentication
  name: Doceree Authentication
  slug: doceree-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Doceree Domain Security
  slug: doceree-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Doceree Trust Center
  slug: doceree-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: doceree
tags:
- Advertising
- Healthcare
- Marketing
- AdTech
- Programmatic
- Header Bidding
- Life Sciences
- Pharmaceuticals
- Point of Care
- Identity Resolution
- Electronic Health Records
- Company
website: https://doceree.com/
---
