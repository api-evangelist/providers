---
access_model:
  confidence: high
  label: Partnership + certification required
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - authentication
  - https://developer.travelokapartnersnetwork.com/get-started
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: OpenTravel (OTA) 2017B XML connectivity API for channel managers, property-management systems and hotel technology partners. Traveloka hosts the ARI (availability, rates, inventory) and content push e
  name: Traveloka Connect - Connectivity API
  slug: traveloka-connect-connectivity-api
- description: The 1.1 Content - Hotel & Room API from Traveloka — 2 operation(s) for 1.1 content - hotel & room.
  name: Traveloka 1.1 Content - Hotel & Room API
  slug: traveloka-1-1-content-hotel-room-api
- description: The 2.1 Search - HotelList API from Traveloka — 1 operation(s) for 2.1 search - hotellist.
  name: Traveloka 2.1 Search - HotelList API
  slug: traveloka-2-1-search-hotellist-api
- description: The 2.2 Search - RoomList API from Traveloka — 1 operation(s) for 2.2 search - roomlist.
  name: Traveloka 2.2 Search - RoomList API
  slug: traveloka-2-2-search-roomlist-api
- description: The 2.3 Search - BulkRoomList API from Traveloka — 1 operation(s) for 2.3 search - bulkroomlist.
  name: Traveloka 2.3 Search - BulkRoomList API
  slug: traveloka-2-3-search-bulkroomlist-api
- description: The 3.1 Booking - Book API from Traveloka — 1 operation(s) for 3.1 booking - book.
  name: Traveloka 3.1 Booking - Book API
  slug: traveloka-3-1-booking-book-api
- description: The 3.2 Booking - IssueCheck API from Traveloka — 1 operation(s) for 3.2 booking - issuecheck.
  name: Traveloka 3.2 Booking - IssueCheck API
  slug: traveloka-3-2-booking-issuecheck-api
- description: The 3.3 Booking - Issue API from Traveloka — 1 operation(s) for 3.3 booking - issue.
  name: Traveloka 3.3 Booking - Issue API
  slug: traveloka-3-3-booking-issue-api
- description: The 3.4 Booking - BookingSummary API from Traveloka — 1 operation(s) for 3.4 booking - bookingsummary.
  name: Traveloka 3.4 Booking - BookingSummary API
  slug: traveloka-3-4-booking-bookingsummary-api
- description: The 3.5 Booking - Cancel API from Traveloka — 1 operation(s) for 3.5 booking - cancel.
  name: Traveloka 3.5 Booking - Cancel API
  slug: traveloka-3-5-booking-cancel-api
- description: The Authorization API from Traveloka — 1 operation(s) for authorization.
  name: Traveloka Authorization API
  slug: traveloka-authorization-api
- description: The Booking API from Traveloka — 4 operation(s) for booking.
  name: Traveloka Booking API
  slug: traveloka-booking-api
- description: The Content API from Traveloka — 2 operation(s) for content.
  name: Traveloka Content API
  slug: traveloka-content-api
- description: This API is optional and intended for partners who do not have their own master data.
  name: Traveloka Discovery (Optional) API
  slug: traveloka-discovery-optional-api
- description: The Rate API from Traveloka — 2 operation(s) for rate.
  name: Traveloka Rate API
  slug: traveloka-rate-api
artifact_total: 36
asyncapis:
- description: ''
  name: Traveloka Connect Webhooks
  slug: traveloka-connect-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Traveloka Atlas 1.1 Content - Hotel & Room API
  slug: open-traveloka-1-1-content-hotel-room-api
- collection_type: open
  name: Traveloka Atlas 2.1 Search - HotelList API
  slug: open-traveloka-2-1-search-hotellist-api
- collection_type: open
  name: Traveloka Atlas 2.2 Search - RoomList API
  slug: open-traveloka-2-2-search-roomlist-api
- collection_type: open
  name: Traveloka Atlas 2.3 Search - BulkRoomList API
  slug: open-traveloka-2-3-search-bulkroomlist-api
- collection_type: open
  name: Traveloka Atlas 3.1 Booking - Book API
  slug: open-traveloka-3-1-booking-book-api
- collection_type: open
  name: Traveloka Atlas 3.2 Booking - IssueCheck API
  slug: open-traveloka-3-2-booking-issuecheck-api
- collection_type: open
  name: Traveloka Atlas 3.3 Booking - Issue API
  slug: open-traveloka-3-3-booking-issue-api
- collection_type: open
  name: Traveloka Atlas 3.4 Booking - BookingSummary API
  slug: open-traveloka-3-4-booking-bookingsummary-api
- collection_type: open
  name: Traveloka Atlas 3.5 Booking - Cancel API
  slug: open-traveloka-3-5-booking-cancel-api
- collection_type: open
  name: LOKA Authorization API
  slug: open-traveloka-authorization-api
- collection_type: open
  name: LOKA Booking API
  slug: open-traveloka-booking-api
- collection_type: open
  name: LOKA Content API
  slug: open-traveloka-content-api
- collection_type: open
  name: LOKA Discovery (Optional) Discovery (Optional) API
  slug: open-traveloka-discovery-optional-api
- collection_type: open
  name: LOKA Rate API
  slug: open-traveloka-rate-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/traveloka-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/traveloka-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.traveloka.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.travelokapartnersnetwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.travelokapartnersnetwork.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.travelokapartnersnetwork.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.travelokapartnersnetwork.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.traveloka.com/en-id/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.traveloka.com/en-id/help
- group: company
  title: ''
  type: Blog
  url: https://www.traveloka.com/en-id/explore
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/traveloka
- group: start
  title: ''
  type: SignUp
  url: https://traveloka.sg.larksuite.com/share/base/form/shrlg7CyVohw5GHPRXwt8LdPCCW
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.traveloka.com/en-id/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.traveloka.com/en-id/privacy-notice
- group: auth
  title: ''
  type: Security
  url: security/traveloka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/traveloka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/traveloka-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/traveloka-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/traveloka-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/traveloka-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/traveloka-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/traveloka-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/traveloka-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/traveloka-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/traveloka-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/traveloka-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/traveloka-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/traveloka-connect-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/traveloka-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/traveloka-loka-partner-api-overlay.yaml
created: '2026-08-05'
description: 'Traveloka (Traveloka Services Pte. Ltd.) is a Southeast Asian multi-product online travel agency operating across Indonesia, Thailand, Vietnam, Malaysia, Singapore, the Philippines, Australia, Japan and South Korea, selling flights, hotels and alternative stays, activities (Xperience), trains, cruises, buses, car rental and airport transfers. Its API surface is entirely partner-facing and runs in three distinct programs: the Traveloka Partners Network (LOKA) v2 REST API for distribution partners reselling Traveloka accommodation inventory; Traveloka Connect, an OpenTravel (OTA) 2017B XML connectivity API for channel managers and property-management systems pushing availability, rates and content; and Traveloka Atlas, a published JSON specification that accommodation suppliers implement on their own hosts so Traveloka can search and book against them. All three are approval-gated behind a partnership agreement and certification; none offer self-serve signup.'
image: https://ik.imagekit.io/tvlk/image/imageResource/2024/08/09/1723192761223-35bd6fefad235fbb690b6d79b050343f.png?tr=q-75
layout: provider
mcp_servers:
- description: ''
  name: Traveloka MCP Server
  slug: traveloka-mcp-server
modified: '2026-08-05'
name: Traveloka
nav: Providers
network: true
overview: 'Traveloka publishes 14 APIs on the [APIs.io](https://apis.io/) network, including 1.1 Content - Hotel & Room API, 2.1 Search - HotelList API, 2.2 Search - RoomList API, and 11 more. Tagged areas include travel, online-travel-agency, accommodation, hotel-booking, and Flights.


  The Traveloka catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Traveloka''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 1
  name: Traveloka Rate Limits
  slug: traveloka-rate-limits
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 58.7
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 48.9
  provenance:
    conformance: derived
    contracts:
      callable: 35.7
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/traveloka/refs/heads/main/screenshots/traveloka-2026-08-17T125942.png
security:
- kind: authentication
  name: Traveloka Authentication
  slug: traveloka-authentication
  summary_line: oauth2/apiKey/http · 0 schemes
- kind: domain-security
  name: Traveloka Domain Security
  slug: traveloka-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Traveloka Vulnerability Disclosure
  slug: traveloka-vulnerability-disclosure
  summary_line: Bugcrowd
slug: traveloka
tags:
- travel
- online-travel-agency
- accommodation
- hotel-booking
- Flights
- Activities
- hospitality
- Distribution
- channel-manager
- opentravel
- southeast-asia
- indonesia
website: https://www.traveloka.com/
---
