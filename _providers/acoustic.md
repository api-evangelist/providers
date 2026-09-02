---
access_model:
  confidence: medium
  label: Public docs, gated onboarding
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://developer.goacoustic.com
  - https://www.acoustic.com/pricing
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 166
  human_in_the_loop: 2
  name: Acoustic Agentic Access
  operation_count: 365
  slug: acoustic-agentic-access
  summary_line: 365 operations · 166 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: REST API for the Acoustic Campaign (formerly Silverpop Engage) marketing automation platform, covering contact databases, relational tables, programs, contact sources, channels (push, SMS, in-app, ric
  name: Acoustic Campaign REST API
  slug: acoustic-campaign-rest-api
- description: The long-lived XML-over-HTTP API for Acoustic Campaign, inherited from Silverpop Engage. A single POST endpoint per regional pod accepts XML request documents for contact list management, recipient ma
  name: Acoustic Campaign XML API
  slug: acoustic-campaign-xml-api
- description: The GraphQL API for Acoustic Connect — the platform's contact, consent, audience, reference-set, product-catalog, product-performance and signal surface. A single POST endpoint at the region host root
  name: Acoustic Connect API
  slug: acoustic-connect-api
- description: Real-time personalization library and APIs for delivering optimized, tailored content to each visitor based on behavior and contextual data, with product catalog, recommendations, zones, geolocation a
  name: Acoustic Personalization
  slug: acoustic-personalization
- description: The Administering user profiles API from Acoustic — 3 operation(s) for administering user profiles.
  name: Acoustic Administering user profiles API
  slug: acoustic-administering-user-profiles-api
- description: '## General Use the Content Asset service Rest APIs to work with assets. Assets are file types that are uploaded or created such as an image file, video file, or text that are used in content items. Yo'
  name: Acoustic Authoring assets API
  slug: acoustic-authoring-assets-api
- description: Use the Acoustic Content category authoring data service Rest APIs to work with category and taxonomy items.
  name: Acoustic Authoring categories API
  slug: acoustic-authoring-categories-api
- description: Use the Content Authoring Changes Rest APIs to apply changes, including bulk actions, to multiple types of Content items.
  name: Acoustic Authoring changes API
  slug: acoustic-authoring-changes-api
- description: Use the Content Authoring comment APIs to work with comments. Comments are a simple way to associate a message to an item in Content. Comments are associated with a single item and user (creatorId). A
  name: Acoustic Authoring comments API
  slug: acoustic-authoring-comments-api
- description: '## General Use the Content content authoring data service Rest APIs to work with content documents. Content includes items that you compose in your content hub and upload from outside your content sub'
  name: Acoustic Authoring content API
  slug: acoustic-authoring-content-api
- description: 'The Authoring context search is a discretional middleware service that is positioned before the Search service. Use the Authoring context search Rest APIs to retrieve user targeted content items. You '
  name: Acoustic Authoring context search API
  slug: acoustic-authoring-context-search-api
- description: Use the Acoustic Content authoring image profile service Rest APIs to work with image profiles. You can create, retrieve, and update image profiles in a database.
  name: Acoustic Authoring image profiles API
  slug: acoustic-authoring-image-profiles-api
- description: Provides generic copying and importing functionality
  name: Acoustic Authoring Import API
  slug: acoustic-authoring-import-api
- description: Use the Content content authoring layout service Rest APIs to work with layouts and layout mappings. Layouts define the template for the type documents. They define the markup and how to add content p
  name: Acoustic Authoring layouts API
  slug: acoustic-authoring-layouts-api
- description: Use the Content library Rest APIs to work with libraries. Libraries currently support having content and asset items added to them.
  name: Acoustic Authoring library API
  slug: acoustic-authoring-library-api
- description: 'The Content Authoring reference API is used to retrieve information about references between items in the system. The type of relationships that are tracked depends on the type of item. Typically, if '
  name: Acoustic Authoring reference API
  slug: acoustic-authoring-reference-api
- description: Use the Content renditions data service Rest APIs to work with image renditions. A 'rendition' of an image defines how you can customize a source image such as the width and height to be shown for a p
  name: Acoustic Authoring renditions API
  slug: acoustic-authoring-renditions-api
- description: 'Use the Content resources data service Rest APIs to work with resources. Resources are binary files that are stored in the CMS and used in content or site design. Resources that are not referenced by '
  name: Acoustic Authoring resources API
  slug: acoustic-authoring-resources-api
- description: Use the Content Review Rest APIs to review assets and content. Use reviews to receive feedback from other members of your team. You can start, update, and complete the reviews that are set up. You can
  name: Acoustic Authoring review API
  slug: acoustic-authoring-review-api
- description: '## General Use the Content authoring search service REST API to access assets, categories, content, content types, image profiles, and taxonomies by searching the content hub. You need prior authentic'
  name: Acoustic Authoring search API
  slug: acoustic-authoring-search-api
- description: Use the Content authoring sites service Rest APIs to work with sites. Sites are comprised of a site metadata and a hierarchy of pages. You can retrieve or update site metadata and create, read, update
  name: Acoustic Authoring sites API
  slug: acoustic-authoring-sites-api
- description: Use the Acoustic Content authoring type service Rest APIs to work with content type documents. Content types define a set of related elements that are used to create content. You can create, retrieve,
  name: Acoustic Authoring types API
  slug: acoustic-authoring-types-api
- description: Use the Content version Rest APIs to work with authoring items that have versions. Versioned documents currently includes assets and content items within Content. The version APIs allow you to retriev
  name: Acoustic Authoring version API
  slug: acoustic-authoring-version-api
- description: Use the Content delivery content service REST API to retrieve published content items. You can use the /delivery/v1/content routes to access content items as an unauthenticated user or the /mydelivery
  name: Acoustic Delivery content API
  slug: acoustic-delivery-content-api
- description: The Delivery context search is a discretional middleware service that is positioned before the Search service. Use the Delivery context search Rest APIs to retrieve user targeted content items. You ca
  name: Acoustic Delivery context search API
  slug: acoustic-delivery-context-search-api
- description: The Content Delivery rendering REST API provides information to render content and pages in client-side applications. **Client-side programming support** If you want to create a client-side applicatio
  name: Acoustic Delivery render API
  slug: acoustic-delivery-render-api
- description: The Delivery Resource Service (DRS) provides access to the published resources in Akamai. The recommended URL for addressing published resources is the Akamai URL which is a static file access. For mo
  name: Acoustic Delivery resources API
  slug: acoustic-delivery-resources-api
- description: 'Use the Watson Content Hub delivery search REST API to search for published assets, content items, categories and pages. You can use the /delivery/v1/search route to perform anonymous searches or the '
  name: Acoustic Delivery search API
  slug: acoustic-delivery-search-api
- description: Use the Content delivery sites service Rest APIs to retrieve published site artefacts.
  name: Acoustic Delivery sites API
  slug: acoustic-delivery-sites-api
- description: Login service offers endpoint to login into Acoustic Content.
  name: Acoustic Login service API
  slug: acoustic-login-service-api
- description: Use the Content Publishing APIs to update the default site revision, which is a snapshot of your published site at a specific time. current-job instance is used to track the state of the job. A site r
  name: Acoustic Publishing API
  slug: acoustic-publishing-api
- description: The Tenant Registry API from Acoustic — 1 operation(s) for tenant registry.
  name: Acoustic Tenant Registry API
  slug: acoustic-tenant-registry-api
- description: 'Use the Content webhook service Rest APIs to work with webhook profiles. You can create, retrieve and update webhook profiles in a database. ### Webhook Timeouts and Retry policy Webhooks will automat'
  name: Acoustic Webhook profiles API
  slug: acoustic-webhook-profiles-api
artifact_total: 53
asyncapis:
- description: ''
  name: Acoustic Webhooks
  slug: acoustic-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-channels-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-contactsources-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-databases-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-events-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-eventtypes-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-gdpr_jobs-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-messages-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-orgs-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-programs-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-relationaltables-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-rest-swagger-index
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-webtracking-swagger
- collection_type: open
  name: Acoustic Content API
  slug: open-acoustic-content-openapi-original
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/acoustic-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acoustic-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/acoustic-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.acoustic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.goacoustic.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.goacoustic.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.goacoustic.com/acoustic-content/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.goacoustic.com/acoustic-content/reference/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.acoustic.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.acoustic.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acoustic.com/pricing
- group: start
  title: ''
  type: Login
  url: https://login.goacoustic.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acoustic.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acoustic.com/privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acoustic-content-samples
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/1643559/2sBXqQEHNz
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goacoustic.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/acoustic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.acoustic.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acoustic-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/acoustic-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acoustic-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acoustic-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acoustic-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/acoustic-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/acoustic-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/acoustic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/acoustic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/acoustic-cli.yml
- group: design
  title: ''
  type: Components
  url: components/acoustic-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acoustic-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acoustic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acoustic-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acoustic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acoustic-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acoustic-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/acoustic-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/acoustic-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/acoustic-content-overlay.yaml
created: '2026-07-17'
description: 'Acoustic is a real-time behavioral marketing platform for B2C companies, delivering omnichannel customer engagement across email, SMS, WhatsApp, mobile push and web. Its developer portal at developer.goacoustic.com publishes an RFC 9727 api-catalog advertising six API products: Acoustic Connect (a GraphQL API for contacts, consent, audiences, product catalog and signals), Acoustic Campaign (a long-lived REST + XML API estate inherited from Silverpop, with a live Swagger service description per regional pod), Acoustic Content (a headless CMS / digital asset management REST API covering authoring, delivery, rendering, publishing and webhooks), Acoustic Personalization (a client-side library for real-time content and product recommendations), Acoustic Experience Analytics (Tealeaf) and Acoustic Exchange. Formerly IBM Watson Marketing, Acoustic was carved out as an independent martech company and is a portfolio company of Sapphire Ventures.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acoustic.png
layout: provider
modified: '2026-08-13'
name: Acoustic
nav: Providers
network: true
overview: 'Acoustic publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Campaign REST API, Campaign XML API, Administering user profiles API, and 28 more. Tagged areas include Company, MarTech, Marketing, Marketing Automation, and Customer Engagement.


  The Acoustic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Acoustic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 33 more developer resources.'
plans:
- name: Acoustic Plans Pricing
  plan_count: 3
  slug: acoustic-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Acoustic Rate Limits
  slug: acoustic-rate-limits
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 26
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.2
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 54.2
    developer_ergonomics: 78.0
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 65.8
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acoustic/refs/heads/main/screenshots/acoustic-2026-07-25T181511.png
security:
- kind: authentication
  name: Acoustic Authentication
  slug: acoustic-authentication
  summary_line: http/apiKey/oauth2 · 7 schemes
- kind: domain-security
  name: Acoustic Domain Security
  slug: acoustic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Acoustic Trust Center
  slug: acoustic-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: acoustic
tags:
- Company
- MarTech
- Marketing
- Marketing Automation
- Customer Engagement
- Content Management
- Personalization
- Email
- SMS
- Push Notifications
- Headless CMS
- Digital Asset Management
- Customer Data
- GraphQL
- Consent Management
website: https://www.acoustic.com
---
