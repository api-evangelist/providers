---
access_model:
  confidence: medium
  label: Sales-Gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://support.disconetwork.com/hc/en-us/articles/15854633791003-Disco-Pricing-Billing
  - https://disconetwork.com/reporting-api
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Disconetwork Agentic Access
  operation_count: 6
  slug: disconetwork-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- description: The channel-partner management API behind DiscoBeat. Lists ad categories and subcategories, reads channel details, manages channel-wide and publisher-specific subcategory exclusions, and lists, inspec
  name: DiscoBeat Channel API
  slug: disconetwork-discobeat-channel-api
- description: 'The server-to-server conversion intake used by advertisers who cannot run the Web SDK. A POST carries an event name, the publisher account id and one of three customer identifiers (raw email, SHA-256 '
  name: Disco Event API
  slug: disconetwork-event-api
- baseURL: https://partners.disconetwork.com
  baseurl_source: declared
  description: The Discobeat API from Disconetwork — 3 operation(s) for discobeat.
  name: Disconetwork Discobeat API
  slug: disconetwork-discobeat-api
- baseURL: https://partners.disconetwork.com
  baseurl_source: declared
  description: The Events API from Disconetwork — 2 operation(s) for events.
  name: Disconetwork Events API
  slug: disconetwork-events-api
- baseURL: https://partners.disconetwork.com
  baseurl_source: declared
  description: The Recommendations API from Disconetwork — 1 operation(s) for recommendations.
  name: Disconetwork Recommendations API
  slug: disconetwork-recommendations-api
artifact_total: 16
asyncapis:
- description: ''
  name: Disconetwork Event Surface
  slug: disconetwork-event-surface
collections:
- collection_type: postman
  name: Disco Reporting API
  slug: postman-disconetwork-reporting-v1
- collection_type: postman
  name: Disco Reporting API V2
  slug: postman-disconetwork-reporting-v2
- collection_type: open
  name: External API for Disco Integration Partners
  slug: open-disconetwork-partner-api
- collection_type: open
  name: Disco Reporting API
  slug: open-disconetwork-reporting-api-v1
- collection_type: open
  name: Disco Reporting API V2
  slug: open-disconetwork-reporting-api-v2
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/disconetwork-partner-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/disconetwork-reporting-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/disconetwork-reporting-api-v2-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/disconetwork-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://disconetwork.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://disconetwork.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.disconetwork.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.disconetwork.com/docs/api-ref/external-api-for-disco-integration-partners
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.disconetwork.com/docs/publish-discofeed
- group: build
  title: ''
  type: Postman
  url: postman/disconetwork-reporting-v2.postman_collection.json
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.disconetwork.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://support.disconetwork.com/hc/en-us/articles/15854633791003-Disco-Pricing-Billing
- group: commercial
  title: ''
  type: Plans
  url: plans/disconetwork-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/disconetwork-rate-limits.yml
- group: start
  title: ''
  type: SignUp
  url: https://disconetwork.com/book-a-demo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.disconetwork.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/disconetwork-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/disconetwork-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/disconetwork-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/disconetwork-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/disconetwork-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/disconetwork-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/disconetwork-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/disconetwork-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/disconetwork-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/disconetwork-packages.yml
- group: design
  title: ''
  type: Components
  url: components/disconetwork-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/disconetwork-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/disconetwork-tool-crosswalk.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/disconetwork-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://disconetwork.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://disconetwork.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://disconetwork.com/press
created: '2026-07-17'
description: 'Disco (disconetwork.com, Disco Technology Inc.) is a commerce media network focused on the post-purchase moment. It helps ecommerce brands and platforms monetize order-confirmation, order-tracking, checkout, email and app surfaces by placing relevant partner offers in front of shoppers, and gives advertisers a performance channel to reach buyers at the point of purchase. Its product suite spans DiscoOffers (publisher monetization), DiscoBeat (a headless, white-labeled commerce media API for SaaS platforms), DiscoMix (non-endemic demand for retail media networks) and OffersAI (the ranking and personalization engine). Disco publishes a real developer surface: a partner-integration OpenAPI at docs.disconetwork.com, two versions of a Reporting API with downloadable OpenAPI 3.0.3 specs and Postman collections, a documented DiscoBeat Channel API, a JavaScript Web SDK, and an llms.txt. Backed by Felicis.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/disconetwork.png
layout: provider
modified: '2026-08-12'
name: Disconetwork
nav: Providers
network: true
overview: 'Disconetwork publishes 3 APIs on the [APIs.io](https://apis.io/) network: Discobeat API, Events API, and Recommendations API. Tagged areas include Company, Commerce Media, Retail Media, Post-Purchase, and Advertising.


  The Disconetwork catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Disconetwork''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, changelog, authentication, and 27 more developer resources.'
plans:
- name: Disconetwork Plans Pricing
  plan_count: 0
  slug: disconetwork-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Disconetwork Rate Limits
  slug: disconetwork-rate-limits
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 62.2
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/disconetwork/refs/heads/main/screenshots/disconetwork-2026-07-25T212103.png
security:
- kind: authentication
  name: Disconetwork Authentication
  slug: disconetwork-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Disconetwork Domain Security
  slug: disconetwork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: disconetwork
tags:
- Company
- Commerce Media
- Retail Media
- Post-Purchase
- Advertising
- E-Commerce
- AdTech
- Marketing
- Analytics
- Reporting
website: https://disconetwork.com
---
