---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-08'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Cvent Registration Agentic Access
  operation_count: 20
  slug: cvent-registration-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 2
apis:
- description: The Cvent Registration REST API is the registration surface of the unified Cvent Platform REST API. It allows integrations to create and manage events, registration types, fees, sessions, contacts, at
  name: Cvent Registration REST API
  slug: rest-api
- description: Cvent Webhooks deliver real-time push notifications when registration, attendee, session, and meeting request events occur in Cvent. Webhook subscribers receive event payloads at a configured URL, ena
  name: Cvent Registration Webhooks
  slug: webhooks
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event registrations and attendees
  name: Cvent Registration Attendees API
  slug: cvent-registration-attendees-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Contact/address book
  name: Cvent Registration Contacts API
  slug: cvent-registration-contacts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event lifecycle and configuration
  name: Cvent Registration Events API
  slug: cvent-registration-events-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Exhibitor management
  name: Cvent Registration Exhibitors API
  slug: cvent-registration-exhibitors-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: OAuth 2.0 token issuance
  name: Cvent Registration OAuth API
  slug: cvent-registration-oauth-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Agenda sessions
  name: Cvent Registration Sessions API
  slug: cvent-registration-sessions-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Webhook subscriptions
  name: Cvent Registration Webhooks API
  slug: cvent-registration-webhooks-api
- description: The legacy Cvent SOAP API, still served and still publishing its WSDL at api.cvent.com/soap/V200611.ASMX?WSDL (HTTP 200, 330,911 bytes, targetNamespace http://api.cvent.com/2006-11). Cvent maintains a
  name: Cvent SOAP API (legacy V200611)
  slug: soap-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Account-level orders and transactions for event registration commerce. Added to the Cvent contract in the 2026-08-20 release. Read-only.
  name: Cvent Registration Orders and Transactions API
  slug: cvent-registration-orders-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Post-event and in-event surveys attached to the registration record.
  name: Cvent Registration Surveys API
  slug: cvent-registration-surveys-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Speaker records, speaker documents and speaker-to-session assignment.
  name: Cvent Registration Speakers API
  slug: cvent-registration-speakers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Table assignment, seating, badge print jobs and badge printer pools for on-site check-in.
  name: Cvent Registration Seating and Badging API
  slug: cvent-registration-seating-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Discount codes and their association to order items.
  name: Cvent Registration Discounts API
  slug: cvent-registration-discounts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Custom field definitions and answers on contacts, events and sessions.
  name: Cvent Registration Custom Fields API
  slug: cvent-registration-custom-fields-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Registration travel — air, ground and arrival/departure data attached to an attendee.
  name: Cvent Registration Event Travel API
  slug: cvent-registration-event-travel-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Attendee activities, attendee insights (engagement scores) and attendee messages.
  name: Cvent Registration Attendee Activities API
  slug: cvent-registration-attendee-activities-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: SCIM 2.0 user provisioning (RFC 7643 / RFC 7644) at /scim/v2 — Users, Groups, Schemas, ResourceTypes and ServiceProviderConfig, using the canonical urn:ietf:params:scim:schemas:core:2.0:User and enter
  name: Cvent Registration SCIM User Provisioning API
  slug: cvent-registration-scim-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Read the account's REST usage tier (Free / Standard / Premium) and current quota consumption before planning a batch.
  name: Cvent Registration Usage and Quota API
  slug: cvent-registration-usage-api
artifact_total: 39
asyncapis:
- description: ''
  name: Cvent Registration Webhooks
  slug: cvent-registration-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cvent Registration REST Attendees API
  slug: open-cvent-registration-attendees-api
- collection_type: open
  name: Cvent Registration REST Attendees Contacts API
  slug: open-cvent-registration-contacts-api
- collection_type: open
  name: Cvent Registration REST Attendees Events API
  slug: open-cvent-registration-events-api
- collection_type: open
  name: Cvent Registration REST Attendees Exhibitors API
  slug: open-cvent-registration-exhibitors-api
- collection_type: open
  name: Cvent Registration REST Attendees OAuth API
  slug: open-cvent-registration-oauth-api
- collection_type: open
  name: Cvent Registration REST Attendees Sessions API
  slug: open-cvent-registration-sessions-api
- collection_type: open
  name: Cvent Registration REST Attendees Webhooks API
  slug: open-cvent-registration-webhooks-api
- collection_type: open
  name: Cvent Registration REST API
  slug: open-cvent-registration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-registration-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cvent-registration-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvent-registration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvent-registration-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cvent-registration-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/en/event-management-software/online-registration-software
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/docs/rest-api/reference/reference
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cvent.com/docs/rest-api/explanation/concepts
- group: auth
  title: ''
  type: OAuthTokenEndpoint
  url: https://api-platform.cvent.com/ea/oauth2/token
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cvent.com/en/event-management-software/cvent-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/product-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cvent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvent/
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/en/blog/feed.xml
- group: other
  title: ''
  type: Overlay
  url: overlays/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cvent-registration-public-overlay.yaml
- group: other
  title: ''
  type: WSDL
  url: wsdl/cvent-registration-soap-v200611.wsdl
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cvent-registration-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/cvent-registration-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cvent-registration-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cvent-registration-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/cvent-registration-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cvent-registration-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cvent-registration-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cvent-registration-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cvent-registration-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cvent-registration-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/cvent-registration-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cvent-registration-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cvent-registration-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cvent-registration-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cvent-registration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cvent-registration-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cvent-registration-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cvent-registration-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cvent-registration-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cvent.com/docs/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://developers.cvent.com/applications
- group: start
  title: ''
  type: Login
  url: https://developers.cvent.com/login
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.cvent.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cvent/rest-sdks
created: '2024-01-15'
description: Cvent Registration is the event registration product within the Cvent Event Cloud, providing online registration websites, attendee data capture, payment processing, registration travel, group registration, custom field collection, and badge / on-site check-in workflows. Registration data is exposed programmatically through the unified Cvent Platform REST API at api-platform.cvent.com (OAuth 2.0 client credentials), with a dedicated Registration Guide on the Cvent developer portal. Real-time registration changes are also delivered through Cvent Webhooks. Earlier integrations relied on the legacy Cvent SOAP API.
finops:
- name: Cvent Registration Finops
  service_category: API
  slug: cvent-registration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-registration.png
layout: provider
modified: '2026-09-07'
name: Cvent Registration
nav: Providers
network: true
overview: 'Cvent Registration publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 14 more. Tagged areas include Attendee Management, Attendees, Conferences, Event Management, and Event.


  The Cvent Registration catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cvent Registration''s developer surface includes authentication, API reference, support, pricing, engineering blog, changelog, documentation, and 41 more developer resources.'
plans:
- name: Cvent Registration Plans Pricing
  plan_count: 5
  slug: cvent-registration-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Cvent Registration Rate Limits
  slug: cvent-registration-rate-limits
scopes:
- name: Cvent Registration Scopes
  scope_count: 238
  slug: cvent-registration-scopes
  summary_line: 238 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 79.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 71.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 79.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/screenshots/cvent-registration-2026-06-20T175407.png
security:
- kind: authentication
  name: Cvent Registration Authentication
  slug: cvent-registration-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Cvent Registration Domain Security
  slug: cvent-registration-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cvent Registration Vulnerability Disclosure
  slug: cvent-registration-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cvent Registration Trust Center
  slug: cvent-registration-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cvent-registration
tags:
- Attendee Management
- Attendees
- Conferences
- Event Management
- Event
- Authentication
- On-Site Check-In
- Payments
- Registration
- REST API
- SCIM
- SDKs
- SOAP
- Ticketing
- Webhook
website: https://www.cvent.com/en/event-management-software/online-registration-software
---
