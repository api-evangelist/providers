---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Storyblok Agentic Access
  operation_count: 38
  slug: storyblok-agentic-access
  summary_line: 38 operations · 14 acting
api_count: 3
apis:
- description: Storyblok emits webhook events when content actions occur in a space such as story publication, unpublication, deletion, asset upload, and pipeline stage transitions. AsyncAPI specification for webhoo
  name: Storyblok Webhooks
  slug: storyblok-webhooks
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: Assets are files stored in Storyblok's asset library, including images, documents, and other media. The Management API allows uploading, tagging, and organizing assets.
  name: Storyblok Assets API
  slug: storyblok-assets-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: Collaborators are users invited to a Storyblok space with specific roles and permissions. The Management API allows adding, updating, and removing collaborators.
  name: Storyblok Collaborators API
  slug: storyblok-collaborators-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: Components define the schema and field structure for story content. This includes managing component definitions, field types, and component groups.
  name: Storyblok Components API
  slug: storyblok-components-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: Datasources are reusable key-value collections used for options lists, translations, and configuration data within Storyblok spaces.
  name: Storyblok Datasources API
  slug: storyblok-datasources-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: URL-based image transformation operations applied by constructing a specific path structure following the base asset URL. All operations require the /m/ path segment prefix.
  name: Storyblok Image Transformation API
  slug: storyblok-image-transformation-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: The links endpoint returns a flat or tree-structured list of all story URLs in a space, suitable for navigation generation and sitemap building.
  name: Storyblok Links API
  slug: storyblok-links-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: Spaces are the top-level containers in Storyblok. Each space has its own content, components, assets, and settings. The spaces endpoint allows retrieval and management of space metadata and configurat
  name: Storyblok Spaces API
  slug: storyblok-spaces-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: Stories are the content entries in Storyblok. Each story is defined by a component schema and holds the content of a page, post, or any other structured content type.
  name: Storyblok Stories API
  slug: storyblok-stories-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: The Tags API from Storyblok — 1 operation(s) for tags.
  name: Storyblok Tags API
  slug: storyblok-tags-api
- baseURL: https://api.storyblok.com/v2/cdn
  baseurl_source: declared
  description: Webhooks allow external services to be notified when events occur in a Storyblok space, such as story publication or asset upload. The Management API provides full CRUD operations for webhook configur
  name: Storyblok Webhooks API
  slug: storyblok-webhooks-api
arazzos:
- description: Sign an asset upload, create a story that references the asset, then publish it.
  name: Storyblok Asset to Story
  slug: storyblok-asset-to-story-workflow
- description: Create a draft story, read it back, update its content, then publish it.
  name: Storyblok Author and Publish Story
  slug: storyblok-author-and-publish-story-workflow
- description: Pull the space link tree for a folder, then fetch the folder start page content for a navigation header.
  name: Storyblok Build Navigation
  slug: storyblok-build-navigation-workflow
- description: Read an existing component definition, recreate it under a new name, and confirm it via the component list.
  name: Storyblok Clone Component
  slug: storyblok-clone-component-workflow
- description: Define a component schema, create a story that uses it, then publish the story.
  name: Storyblok Component to Story
  slug: storyblok-component-to-story-workflow
- description: Validate the space, invite a collaborator with a role, then list collaborators to confirm the invitation.
  name: Storyblok Onboard Collaborator
  slug: storyblok-onboard-collaborator-workflow
- description: Validate the space, create a datasource, then read its entries back through the Content Delivery API.
  name: Storyblok Provision Datasource
  slug: storyblok-provision-datasource-workflow
- description: Publish a draft story via the Management API and verify it is live through the Content Delivery API.
  name: Storyblok Publish and Verify Delivery
  slug: storyblok-publish-and-verify-delivery-workflow
- description: Validate the space, register a webhook endpoint, then read it back to confirm it is active.
  name: Storyblok Register Webhook
  slug: storyblok-register-webhook-workflow
- description: Read a story, unpublish it to pull it from delivery, then optionally delete it from the space.
  name: Storyblok Retire Story
  slug: storyblok-retire-story-workflow
- description: Discover tags, list the stories carrying a chosen tag, then fetch the full content of the first match.
  name: Storyblok Tag-Driven Content Sync
  slug: storyblok-tag-driven-content-sync-workflow
artifact_total: 67
asyncapis:
- description: The Storyblok Webhook system delivers real-time event notifications to registered HTTP endpoints when content events occur in a Storyblok space. Events are triggered by actions such as story publicati
  name: Storyblok Webhooks
  slug: storyblok-webhooks-asyncapi
collections:
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets API
  slug: postman-storyblok-assets-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Collaborators API
  slug: postman-storyblok-collaborators-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Components API
  slug: postman-storyblok-components-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Datasources API
  slug: postman-storyblok-datasources-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Image Transformation API
  slug: postman-storyblok-image-transformation-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Links API
  slug: postman-storyblok-links-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Spaces API
  slug: postman-storyblok-spaces-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Stories API
  slug: postman-storyblok-stories-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Tags API
  slug: postman-storyblok-tags-api
- collection_type: postman
  name: Storyblok Content Delivery API v2 Assets Webhooks API
  slug: postman-storyblok-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets API
  slug: open-storyblok-assets-api
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Collaborators API
  slug: open-storyblok-collaborators-api
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Components API
  slug: open-storyblok-components-api
- collection_type: open
  name: Storyblok Content Delivery API v2
  slug: open-storyblok-content-delivery-api-v2
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Datasources API
  slug: open-storyblok-datasources-api
- collection_type: open
  name: Storyblok Image Service
  slug: open-storyblok-image-service
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Image Transformation API
  slug: open-storyblok-image-transformation-api
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Links API
  slug: open-storyblok-links-api
- collection_type: open
  name: Storyblok Management API
  slug: open-storyblok-management-api
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Spaces API
  slug: open-storyblok-spaces-api
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Stories API
  slug: open-storyblok-stories-api
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Tags API
  slug: open-storyblok-tags-api
- collection_type: open
  name: Storyblok Content Delivery API v2 Assets Webhooks API
  slug: open-storyblok-webhooks-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/storyblok-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/storyblok-content-delivery-api-v2-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/storyblok/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/storyblok-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/storyblok-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/storyblok-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storyblok-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/storyblok-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/storyblok-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/storyblok-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/storyblok-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/storyblok-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/storyblok-cli.yml
- group: design
  title: ''
  type: Components
  url: components/storyblok-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/storyblok-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/storyblok-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storyblok-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/storyblok-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-asset-to-story-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-author-and-publish-story-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-build-navigation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-clone-component-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-component-to-story-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-onboard-collaborator-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-provision-datasource-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-publish-and-verify-delivery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-register-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-retire-story-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/storyblok-tag-driven-content-sync-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/storyblok
- group: start
  title: ''
  type: Portal
  url: https://www.storyblok.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.storyblok.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.storyblok.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.storyblok.com/blog
- group: company
  title: ''
  type: About
  url: https://www.storyblok.com/about
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.storyblok.com/changelog
- group: other
  title: ''
  type: CaseStudies
  url: https://www.storyblok.com/customer-stories
- group: operate
  title: ''
  type: Contact
  url: https://www.storyblok.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.storyblok.com/
- group: operate
  title: ''
  type: Support
  url: https://www.storyblok.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storyblok.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storyblok.com/legal/terms-of-service
- group: start
  title: ''
  type: Signup
  url: https://app.storyblok.com/#!/signup
- group: start
  title: ''
  type: Login
  url: https://app.storyblok.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/storyblok
- group: build
  title: ''
  type: SDKs
  url: https://www.storyblok.com/technologies
created: '2026-05-02'
description: Storyblok is a headless content management system (CMS) with a visual editor that enables developers and content editors to collaboratively build and manage digital experiences. It provides APIs for content delivery, content management, image optimization, and webhook-based event notifications. Storyblok supports composable content through reusable components, multi-language content, and multi-site management with real-time collaboration features.
examples:
- key_count: 2
  name: Storyblok Create Story Example
  slug: storyblok-create-story-example
- key_count: 3
  name: Storyblok Get Image Transform Example
  slug: storyblok-get-image-transform-example
- key_count: 2
  name: Storyblok List Stories Example
  slug: storyblok-list-stories-example
finops:
- name: Storyblok Finops
  service_category: Headless CMS
  slug: storyblok-finops
graphqls:
- description: The Storyblok GraphQL API is a read-only content delivery endpoint that exposes published and draft content from a Storyblok space. It provides a strongly typed, automatically documented interface tha
  name: Storyblok GraphQL API
  slug: storyblok-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/storyblok.png
json_schemas:
- name: Storyblok Component
  property_count: 13
  slug: storyblok-component
- name: Storyblok Story
  property_count: 24
  slug: storyblok-story
- name: Storyblok Webhook Payload
  property_count: 7
  slug: storyblok-webhook-payload
json_structures:
- name: Storyblok Story Structure
  property_count: 0
  slug: storyblok-story-structure
jsonld:
- class_count: 0
  name: Storyblok Context
  property_count: 10
  slug: storyblok-context
layout: provider
mcp_servers:
- description: ''
  name: Storyblok
  slug: storyblok
modified: '2026-06-20'
name: Storyblok
nav: Providers
network: true
overview: 'Storyblok publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Assets API, Collaborators API, and 8 more. Tagged areas include CMS, Content Delivery, Content Management, Headless CMS, and Image Optimization.


  The Storyblok catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Storyblok''s developer surface includes changelog, CLI, authentication, developer portal, documentation, pricing, engineering blog, and 39 more developer resources.'
plans:
- name: Storyblok Plans Pricing
  plan_count: 5
  slug: storyblok-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 6
  name: Storyblok Rate Limits
  slug: storyblok-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Storyblok API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: storyblok-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Storyblok API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: storyblok-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Storyblok API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 6
  slug: storyblok-rules
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 33
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 69.1
    developer_ergonomics: 48.8
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/storyblok/refs/heads/main/screenshots/storyblok-2026-06-20T194608.png
security:
- kind: authentication
  name: Storyblok Authentication
  slug: storyblok-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Storyblok Domain Security
  slug: storyblok-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Storyblok Trust Center
  slug: storyblok-trust-center
  summary_line: ISO 27001, SOC 2 Type II, TISAX, GDPR, EU-U.S. Data Privacy Framework
slug: storyblok
tags:
- CMS
- Content Delivery
- Content Management
- Headless CMS
- Image Optimization
- REST API
- Visual Editor
- Webhook
website: https://www.storyblok.com/
---
