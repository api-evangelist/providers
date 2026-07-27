---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 64.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amadeus Media Agentic Access
  operation_count: 5
  slug: amadeus-media-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: Operations for retrieving detailed hotel property content.
  name: Amadeus Media Hotel Content API
  slug: amadeus-media-hotel-content-api
- description: Operations for retrieving hotel media assets including images and videos.
  name: Amadeus Media Hotel Media API
  slug: amadeus-media-hotel-media-api
- description: The Hotels API from Amadeus Media — 3 operation(s) for hotels.
  name: Amadeus Media Hotels API
  slug: amadeus-media-hotels-api
artifact_total: 75
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amadeus-media-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amadeus-media-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amadeus-media-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amadeus-media-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.amadeus.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262
- group: start
  title: ''
  type: SignUp
  url: https://developers.amadeus.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.amadeus.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://developers.amadeus.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/faq/
- group: operate
  title: ''
  type: Support
  url: https://developers.amadeus.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.amadeus.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.amadeus.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amadeus4dev
- group: build
  title: Python SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-python
- group: build
  title: Node.js SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-node
- group: build
  title: Java SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-java
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.amadeus.com/status
- group: design
  title: ''
  type: SpectralRules
  url: rules/amadeus-media-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amadeus-media-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amadeus-media-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amadeus-media-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amadeus-media-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amadeus-media-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amadeus-media-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amadeus-media-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amadeus-media-lifecycle.yml
created: '2024-01-01'
description: Amadeus Media provides APIs and data services for accessing travel-related media content, including hotel images, property descriptions, multimedia assets, and rich content for hospitality and travel applications. Amadeus partners with trusted content providers such as Leonardo to deliver high-quality hotel media through enterprise-grade APIs used by online travel agencies, metasearch platforms, and hospitality technology providers.
examples:
- key_count: 2
  name: Hotel Content Geo Code Example
  slug: hotel-content-geo-code-example
- key_count: 5
  name: Hotel Content Hotel Address Example
  slug: hotel-content-hotel-address-example
- key_count: 5
  name: Hotel Content Hotel Basic Info Example
  slug: hotel-content-hotel-basic-info-example
- key_count: 4
  name: Hotel Content Hotel Contact Example
  slug: hotel-content-hotel-contact-example
- key_count: 11
  name: Hotel Content Hotel Content Example
  slug: hotel-content-hotel-content-example
- key_count: 2
  name: Hotel Content Hotel Content Response Example
  slug: hotel-content-hotel-content-response-example
- key_count: 2
  name: Hotel Content Hotel Description Example
  slug: hotel-content-hotel-description-example
- key_count: 2
  name: Hotel Content Hotel Media Data Example
  slug: hotel-content-hotel-media-data-example
- key_count: 9
  name: Hotel Content Hotel Media Item Example
  slug: hotel-content-hotel-media-item-example
- key_count: 2
  name: Hotel Content Hotel Media Response Example
  slug: hotel-content-hotel-media-response-example
- key_count: 3
  name: Hotel Content Media Asset Example
  slug: hotel-content-media-asset-example
- key_count: 1
  name: Hotel List Error_400 Example
  slug: hotel-list-error_400-example
- key_count: 1
  name: Hotel List Error_404 Example
  slug: hotel-list-error_404-example
- key_count: 1
  name: Hotel List Error_500 Example
  slug: hotel-list-error_500-example
- key_count: 0
  name: Hotel List Hotel Example
  slug: hotel-list-hotel-example
- key_count: 2
  name: Hotel List Hotel Search Response Example
  slug: hotel-list-hotel-search-response-example
features:
- description: Access high-quality images and multimedia assets for hotel properties through the Enterprise Hotel Content API and trusted content partners like Leonardo.
  name: Hotel Property Images
- description: Retrieve detailed hotel descriptions, amenity lists, facility information, and property attributes for comprehensive hotel profiles.
  name: Rich Property Descriptions
- description: Access geographic coordinates, addresses, and time zones for over 770,000 hotels in the Amadeus global inventory.
  name: Geolocation Data
- description: Enterprise API tier provides access to detailed hotel content including media that is not available in self-service APIs due to licensing constraints.
  name: Enterprise Content Access
- description: Hotel content and descriptions available in multiple languages to support international travel applications and global markets.
  name: Multi-Language Support
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amadeus-media.png
integrations:
- description: Amadeus recommends Leonardo as the trusted data provider for hotel images and property media, offering a comprehensive library of hotel photography.
  name: Leonardo (Hotel Images)
- description: Developers can supplement Amadeus hotel data with Google Places API to retrieve hotel images and business information for properties in the Amadeus inventory.
  name: Google Places API
- description: Combine with Amadeus Hotel Search to display media alongside hotel offers and pricing for a complete shopping experience.
  name: Amadeus Hotel Search API
- description: Integrate hotel content with the booking flow to present property images and descriptions before and during the reservation process.
  name: Amadeus Hotel Booking API
- description: Pair hotel media with sentiment-based ratings to create compelling hotel profile pages that combine visual content with review insights.
  name: Amadeus Hotel Ratings API
json_schemas:
- name: GeoCode
  property_count: 2
  slug: hotel-content-geo-code
- name: HotelAddress
  property_count: 5
  slug: hotel-content-hotel-address
- name: HotelBasicInfo
  property_count: 5
  slug: hotel-content-hotel-basic-info
- name: HotelContact
  property_count: 4
  slug: hotel-content-hotel-contact
- name: HotelContentResponse
  property_count: 2
  slug: hotel-content-hotel-content-response
- name: HotelContent
  property_count: 11
  slug: hotel-content-hotel-content
- name: HotelDescription
  property_count: 2
  slug: hotel-content-hotel-description
- name: HotelMediaData
  property_count: 2
  slug: hotel-content-hotel-media-data
- name: HotelMediaItem
  property_count: 9
  slug: hotel-content-hotel-media-item
- name: HotelMediaResponse
  property_count: 2
  slug: hotel-content-hotel-media-response
- name: MediaAsset
  property_count: 3
  slug: hotel-content-media-asset
- name: Error_400
  property_count: 1
  slug: hotel-list-error_400
- name: Error_404
  property_count: 1
  slug: hotel-list-error_404
- name: Error_500
  property_count: 1
  slug: hotel-list-error_500
- name: Hotel
  property_count: 0
  slug: hotel-list-hotel
- name: HotelSearchResponse
  property_count: 2
  slug: hotel-list-hotel-search-response
json_structures:
- name: Hotel Content Geo Code Structure
  property_count: 2
  slug: hotel-content-geo-code-structure
- name: Hotel Content Hotel Address Structure
  property_count: 5
  slug: hotel-content-hotel-address-structure
- name: Hotel Content Hotel Basic Info Structure
  property_count: 5
  slug: hotel-content-hotel-basic-info-structure
- name: Hotel Content Hotel Contact Structure
  property_count: 4
  slug: hotel-content-hotel-contact-structure
- name: Hotel Content Hotel Content Response Structure
  property_count: 2
  slug: hotel-content-hotel-content-response-structure
- name: Hotel Content Hotel Content Structure
  property_count: 11
  slug: hotel-content-hotel-content-structure
- name: Hotel Content Hotel Description Structure
  property_count: 2
  slug: hotel-content-hotel-description-structure
- name: Hotel Content Hotel Media Data Structure
  property_count: 2
  slug: hotel-content-hotel-media-data-structure
- name: Hotel Content Hotel Media Item Structure
  property_count: 9
  slug: hotel-content-hotel-media-item-structure
- name: Hotel Content Hotel Media Response Structure
  property_count: 2
  slug: hotel-content-hotel-media-response-structure
- name: Hotel Content Media Asset Structure
  property_count: 3
  slug: hotel-content-media-asset-structure
- name: Hotel List Error_400 Structure
  property_count: 1
  slug: hotel-list-error_400-structure
- name: Hotel List Error_404 Structure
  property_count: 1
  slug: hotel-list-error_404-structure
- name: Hotel List Error_500 Structure
  property_count: 1
  slug: hotel-list-error_500-structure
- name: Hotel List Hotel Search Response Structure
  property_count: 2
  slug: hotel-list-hotel-search-response-structure
- name: Hotel List Hotel Structure
  property_count: 0
  slug: hotel-list-hotel-structure
jsonld:
- class_count: 13
  name: Amadeus Hotel Content Context
  property_count: 37
  slug: amadeus-hotel-content-context
- class_count: 4
  name: Amadeus Hotel List Context
  property_count: 12
  slug: amadeus-hotel-list-context
layout: provider
mcp_servers:
- description: ''
  name: amadeus-media-mcp.yml
  slug: amadeus-media-mcpyml
modified: '2026-06-20'
name: Amadeus Media
nav: Providers
network: true
overview: 'Amadeus Media publishes 3 APIs on the [APIs.io](https://apis.io/) network: Hotel Content API, Hotel Media API, and Hotels API. Tagged areas include Content, Hotels, Images, Media, and Travel.


  The Amadeus Media catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amadeus Media''s developer surface includes authentication, developer portal, getting-started guide, signup flow, pricing, engineering blog, FAQ, and 21 more developer resources.'
random_paper: 1
rules:
- name: Amadeus Media API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amadeus-media-jsonschema-spectral-rules
- name: Amadeus Media API Rules
  rule_count: 38
  severity_counts:
    error: 17
    hint: 0
    info: 6
    warn: 15
  slug: amadeus-media-spectral-rules
score:
  band: strong
  composite: 64.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 78.8
    developer_ergonomics: 60.9
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 64.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amadeus-media/refs/heads/main/screenshots/amadeus-media-2026-07-25T195903.png
security:
- kind: authentication
  name: Amadeus Media Authentication
  slug: amadeus-media-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amadeus Media Domain Security
  slug: amadeus-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amadeus Media Vulnerability Disclosure
  slug: amadeus-media-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amadeus-media
tags:
- Content
- Hotels
- Images
- Media
- Travel
use_cases:
- description: Power hotel search pages with rich property photos, descriptions, and amenity information sourced directly from Amadeus content services.
  name: Online Travel Agency Hotel Listings
- description: Integrate Amadeus hotel content into metasearch engines to display property images and descriptions alongside rate comparisons.
  name: Metasearch Platform Integration
- description: Enhance hotel booking flows with compelling property imagery and detailed descriptions to improve conversion rates.
  name: Hotel Booking Engine Content
- description: Display hotel photos and media in mobile travel apps to give users visual context when browsing and booking accommodation.
  name: Travel App Media Display
- description: Provide hotel content and imagery in corporate travel management systems to help business travelers make informed accommodation decisions.
  name: Corporate Travel Platform
website: https://developers.amadeus.com/
---
