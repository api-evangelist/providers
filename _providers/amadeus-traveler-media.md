---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amadeus Traveler Media Agentic Access
  operation_count: 6
  slug: amadeus-traveler-media-agentic-access
  summary_line: 6 operations
api_count: 5
apis:
- description: The category-rated-areas API from Amadeus Traveler Media — 1 operation(s) for category-rated-areas.
  name: Amadeus Traveler Media category-rated-areas API
  slug: amadeus-traveler-media-category-rated-areas-api
- description: Sentiments about Hotels.
  name: Amadeus Traveler Media Hotel Ratings API
  slug: amadeus-traveler-media-hotel-ratings-api
- description: The recommended-locations API from Amadeus Traveler Media — 1 operation(s) for recommended-locations.
  name: Amadeus Traveler Media recommended-locations API
  slug: amadeus-traveler-media-recommended-locations-api
- description: The Retrieve API from Amadeus Traveler Media — 1 operation(s) for retrieve.
  name: Amadeus Traveler Media Retrieve API
  slug: amadeus-traveler-media-retrieve-api
- description: The Search API from Amadeus Traveler Media — 2 operation(s) for search.
  name: Amadeus Traveler Media Search API
  slug: amadeus-traveler-media-search-api
artifact_total: 137
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amadeus-traveler-media-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amadeus-traveler-media-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amadeus-traveler-media-domain-security.yml
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
- group: company
  title: ''
  type: Blog
  url: https://amadeus.com/en/insights
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
  url: rules/amadeus-traveler-media-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amadeus-traveler-media-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amadeus-traveler-media-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amadeus-traveler-media-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amadeus-traveler-media-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amadeus-traveler-media-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amadeus-traveler-media-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amadeus-traveler-media-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amadeus-traveler-media-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amadeus-traveler-media-lifecycle.yml
created: '2024-01-01'
description: The Amadeus Traveler Media APIs provide access to travel-related media and destination content, including photos, ratings, and information for points of interest, hotels, and destinations worldwide. These APIs power travel apps, destination guides, and travel planning platforms with rich content for tourist attractions, hotel sentiment ratings, travel recommendations, and location scoring.
examples:
- key_count: 6
  name: Hotel Ratings Collection Links Example
  slug: hotel-ratings-collection-links-example
- key_count: 2
  name: Hotel Ratings Collection Meta Example
  slug: hotel-ratings-collection-meta-example
- key_count: 3
  name: Hotel Ratings Error Source Example
  slug: hotel-ratings-error-source-example
- key_count: 1
  name: Hotel Ratings Error400 Example
  slug: hotel-ratings-error400-example
- key_count: 1
  name: Hotel Ratings Error401 Example
  slug: hotel-ratings-error401-example
- key_count: 1
  name: Hotel Ratings Error500 Example
  slug: hotel-ratings-error500-example
- key_count: 6
  name: Hotel Ratings Hotel Sentiment Example
  slug: hotel-ratings-hotel-sentiment-example
- key_count: 0
  name: Hotel Ratings Score Example
  slug: hotel-ratings-score-example
- key_count: 5
  name: Hotel Ratings Warning Example
  slug: hotel-ratings-warning-example
- key_count: 0
  name: Hotel Ratings Warning Not Found Example
  slug: hotel-ratings-warning-not-found-example
- key_count: 0
  name: Location Score Category Rated Areas Example
  slug: location-score-category-rated-areas-example
- key_count: 5
  name: Location Score Errors Example
  slug: location-score-errors-example
- key_count: 2
  name: Location Score Meta Example
  slug: location-score-meta-example
- key_count: 1
  name: Location Score Response_Error Example
  slug: location-score-response_error-example
- key_count: 3
  name: Location Score Response_Location Score Example
  slug: location-score-response_location-score-example
- key_count: 4
  name: Location Score Warning Example
  slug: location-score-warning-example
- key_count: 2
  name: Points Of Interest Collection_ Meta Example
  slug: points-of-interest-collection_-meta-example
- key_count: 1
  name: Points Of Interest Error_400 Example
  slug: points-of-interest-error_400-example
- key_count: 1
  name: Points Of Interest Error_404 Example
  slug: points-of-interest-error_404-example
- key_count: 1
  name: Points Of Interest Error_500 Example
  slug: points-of-interest-error_500-example
- key_count: 2
  name: Points Of Interest Geo Code Example
  slug: points-of-interest-geo-code-example
- key_count: 5
  name: Points Of Interest Issue Example
  slug: points-of-interest-issue-example
- key_count: 2
  name: Points Of Interest Links Example
  slug: points-of-interest-links-example
- key_count: 9
  name: Points Of Interest Location Example
  slug: points-of-interest-location-example
- key_count: 5
  name: Travel Recommendations Errors Example
  slug: travel-recommendations-errors-example
- key_count: 2
  name: Travel Recommendations Meta Example
  slug: travel-recommendations-meta-example
- key_count: 0
  name: Travel Recommendations Recommended Location Example
  slug: travel-recommendations-recommended-location-example
- key_count: 1
  name: Travel Recommendations Response_Error Example
  slug: travel-recommendations-response_error-example
- key_count: 3
  name: Travel Recommendations Response_Recommended Location Example
  slug: travel-recommendations-response_recommended-location-example
- key_count: 4
  name: Travel Recommendations Warning Example
  slug: travel-recommendations-warning-example
features:
- description: Discover tourist attractions, restaurants, museums, and nightlife venues near any geographic location with ranking scores.
  name: Points of Interest Discovery
- description: Access sentiment-based hotel ratings derived from thousands of traveler reviews covering all key aspects of the hotel experience.
  name: Hotel Sentiment Ratings
- description: Get AI-powered destination recommendations tailored to a traveler's origin and travel history patterns.
  name: Personalized Travel Recommendations
- description: Score any neighborhood for specific traveler personas including Shoppers, Foodies, Nightlife Seekers, Sightseers, and Beach Lovers.
  name: Location Scoring by Persona
- description: Combine POI data, hotel ratings, and location scores to create comprehensive destination guides and travel media content.
  name: Rich Destination Content
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amadeus-traveler-media.png
integrations:
- description: Combine hotel ratings with hotel search results to display sentiment scores alongside pricing for better hotel selection.
  name: Amadeus Hotel Search
- description: Pair hotel ratings with property images and descriptions from the Hotel Content API for complete hotel profiles.
  name: Amadeus Hotel Content API
- description: Extend POI discovery with bookable tours and activities from the Amadeus Tours and Activities API.
  name: Amadeus Tours and Activities
- description: Use city search to identify destination cities before fetching POIs and travel recommendations for that location.
  name: Amadeus City Search
- description: Combine travel recommendations with flight inspiration search to suggest both destinations and available flights.
  name: Amadeus Flight Inspiration Search
json_schemas:
- name: CollectionLinks
  property_count: 6
  slug: hotel-ratings-collection-links
- name: CollectionMeta
  property_count: 2
  slug: hotel-ratings-collection-meta
- name: ErrorSource
  property_count: 3
  slug: hotel-ratings-error-source
- name: Error400
  property_count: 1
  slug: hotel-ratings-error400
- name: Error401
  property_count: 1
  slug: hotel-ratings-error401
- name: Error500
  property_count: 1
  slug: hotel-ratings-error500
- name: HotelSentiment
  property_count: 6
  slug: hotel-ratings-hotel-sentiment
- name: Score
  property_count: 0
  slug: hotel-ratings-score
- name: WarningNotFound
  property_count: 0
  slug: hotel-ratings-warning-not-found
- name: Warning
  property_count: 5
  slug: hotel-ratings-warning
- name: category-rated-areas
  property_count: 0
  slug: location-score-category-rated-areas
- name: errors
  property_count: 5
  slug: location-score-errors
- name: Meta
  property_count: 2
  slug: location-score-meta
- name: response_error
  property_count: 1
  slug: location-score-response_error
- name: response_locationScore
  property_count: 3
  slug: location-score-response_location-score
- name: Warning
  property_count: 4
  slug: location-score-warning
- name: Collection_Meta
  property_count: 2
  slug: points-of-interest-collection_-meta
- name: Error_400
  property_count: 1
  slug: points-of-interest-error_400
- name: Error_404
  property_count: 1
  slug: points-of-interest-error_404
- name: Error_500
  property_count: 1
  slug: points-of-interest-error_500
- name: GeoCode
  property_count: 2
  slug: points-of-interest-geo-code
- name: Issue
  property_count: 5
  slug: points-of-interest-issue
- name: Links
  property_count: 2
  slug: points-of-interest-links
- name: Location
  property_count: 9
  slug: points-of-interest-location
- name: Errors
  property_count: 5
  slug: travel-recommendations-errors
- name: Meta
  property_count: 2
  slug: travel-recommendations-meta
- name: RecommendedLocation
  property_count: 0
  slug: travel-recommendations-recommended-location
- name: response_error
  property_count: 1
  slug: travel-recommendations-response_error
- name: response_recommendedLocation
  property_count: 3
  slug: travel-recommendations-response_recommended-location
- name: Warning
  property_count: 4
  slug: travel-recommendations-warning
json_structures:
- name: Hotel Ratings Collection Links Structure
  property_count: 6
  slug: hotel-ratings-collection-links-structure
- name: Hotel Ratings Collection Meta Structure
  property_count: 2
  slug: hotel-ratings-collection-meta-structure
- name: Hotel Ratings Error Source Structure
  property_count: 3
  slug: hotel-ratings-error-source-structure
- name: Hotel Ratings Error400 Structure
  property_count: 1
  slug: hotel-ratings-error400-structure
- name: Hotel Ratings Error401 Structure
  property_count: 1
  slug: hotel-ratings-error401-structure
- name: Hotel Ratings Error500 Structure
  property_count: 1
  slug: hotel-ratings-error500-structure
- name: Hotel Ratings Hotel Sentiment Structure
  property_count: 6
  slug: hotel-ratings-hotel-sentiment-structure
- name: Hotel Ratings Score Structure
  property_count: 0
  slug: hotel-ratings-score-structure
- name: Hotel Ratings Warning Not Found Structure
  property_count: 0
  slug: hotel-ratings-warning-not-found-structure
- name: Hotel Ratings Warning Structure
  property_count: 5
  slug: hotel-ratings-warning-structure
- name: Location Score Category Rated Areas Structure
  property_count: 0
  slug: location-score-category-rated-areas-structure
- name: Location Score Errors Structure
  property_count: 5
  slug: location-score-errors-structure
- name: Location Score Meta Structure
  property_count: 2
  slug: location-score-meta-structure
- name: Location Score Response_Error Structure
  property_count: 1
  slug: location-score-response_error-structure
- name: Location Score Response_Location Score Structure
  property_count: 3
  slug: location-score-response_location-score-structure
- name: Location Score Warning Structure
  property_count: 4
  slug: location-score-warning-structure
- name: Points Of Interest Collection_ Meta Structure
  property_count: 2
  slug: points-of-interest-collection_-meta-structure
- name: Points Of Interest Error_400 Structure
  property_count: 1
  slug: points-of-interest-error_400-structure
- name: Points Of Interest Error_404 Structure
  property_count: 1
  slug: points-of-interest-error_404-structure
- name: Points Of Interest Error_500 Structure
  property_count: 1
  slug: points-of-interest-error_500-structure
- name: Points Of Interest Geo Code Structure
  property_count: 2
  slug: points-of-interest-geo-code-structure
- name: Points Of Interest Issue Structure
  property_count: 5
  slug: points-of-interest-issue-structure
- name: Points Of Interest Links Structure
  property_count: 2
  slug: points-of-interest-links-structure
- name: Points Of Interest Location Structure
  property_count: 9
  slug: points-of-interest-location-structure
- name: Travel Recommendations Errors Structure
  property_count: 5
  slug: travel-recommendations-errors-structure
- name: Travel Recommendations Meta Structure
  property_count: 2
  slug: travel-recommendations-meta-structure
- name: Travel Recommendations Recommended Location Structure
  property_count: 0
  slug: travel-recommendations-recommended-location-structure
- name: Travel Recommendations Response_Error Structure
  property_count: 1
  slug: travel-recommendations-response_error-structure
- name: Travel Recommendations Response_Recommended Location Structure
  property_count: 3
  slug: travel-recommendations-response_recommended-location-structure
- name: Travel Recommendations Warning Structure
  property_count: 4
  slug: travel-recommendations-warning-structure
jsonld:
- class_count: 2
  name: Amadeus Hotel Ratings Collection Context
  property_count: 8
  slug: amadeus-hotel-ratings-collection-context
- class_count: 1
  name: Amadeus Hotel Ratings Error Context
  property_count: 3
  slug: amadeus-hotel-ratings-error-context
- class_count: 1
  name: Amadeus Hotel Ratings Error400 Context
  property_count: 1
  slug: amadeus-hotel-ratings-error400-context
- class_count: 1
  name: Amadeus Hotel Ratings Error401 Context
  property_count: 1
  slug: amadeus-hotel-ratings-error401-context
- class_count: 1
  name: Amadeus Hotel Ratings Error500 Context
  property_count: 1
  slug: amadeus-hotel-ratings-error500-context
- class_count: 1
  name: Amadeus Hotel Ratings Hotel Context
  property_count: 6
  slug: amadeus-hotel-ratings-hotel-context
- class_count: 0
  name: Amadeus Hotel Ratings Score Context
  property_count: 0
  slug: amadeus-hotel-ratings-score-context
- class_count: 1
  name: Amadeus Hotel Ratings Warning Context
  property_count: 5
  slug: amadeus-hotel-ratings-warning-context
- class_count: 0
  name: Amadeus Location Score Category Context
  property_count: 0
  slug: amadeus-location-score-category-context
- class_count: 1
  name: Amadeus Location Score Errors Context
  property_count: 5
  slug: amadeus-location-score-errors-context
- class_count: 1
  name: Amadeus Location Score Meta Context
  property_count: 2
  slug: amadeus-location-score-meta-context
- class_count: 1
  name: Amadeus Location Score Response_Error Context
  property_count: 1
  slug: amadeus-location-score-response_error-context
- class_count: 1
  name: Amadeus Location Score Response_Location Context
  property_count: 3
  slug: amadeus-location-score-response_location-context
- class_count: 1
  name: Amadeus Location Score Warning Context
  property_count: 4
  slug: amadeus-location-score-warning-context
- class_count: 9
  name: Amadeus Points Of Interest Context
  property_count: 20
  slug: amadeus-points-of-interest-context
- class_count: 1
  name: Amadeus Travel Recommendations Errors Context
  property_count: 5
  slug: amadeus-travel-recommendations-errors-context
- class_count: 1
  name: Amadeus Travel Recommendations Meta Context
  property_count: 2
  slug: amadeus-travel-recommendations-meta-context
- class_count: 0
  name: Amadeus Travel Recommendations Recommended Context
  property_count: 0
  slug: amadeus-travel-recommendations-recommended-context
- class_count: 1
  name: Amadeus Travel Recommendations Response_Error Context
  property_count: 1
  slug: amadeus-travel-recommendations-response_error-context
- class_count: 1
  name: Amadeus Travel Recommendations Response_Recommended Context
  property_count: 3
  slug: amadeus-travel-recommendations-response_recommended-context
- class_count: 1
  name: Amadeus Travel Recommendations Warning Context
  property_count: 4
  slug: amadeus-travel-recommendations-warning-context
layout: provider
mcp_servers:
- description: ''
  name: amadeus-traveler-media-mcp.yml
  slug: amadeus-traveler-media-mcpyml
modified: '2026-06-20'
name: Amadeus Traveler Media
nav: Providers
network: true
overview: 'Amadeus Traveler Media publishes 5 APIs on the [APIs.io](https://apis.io/) network, including category-rated-areas API, Hotel Ratings API, recommended-locations API, and 2 more. Tagged areas include Content, Destination, Media, Photos, and Points of Interest.


  The Amadeus Traveler Media catalog on APIs.io includes 21 JSON-LD contexts and 2 Spectral governance rulesets.


  Amadeus Traveler Media''s developer surface includes developer portal, getting-started guide, authentication, signup flow, pricing, engineering blog, FAQ, and 22 more developer resources.'
random_paper: 3
rules:
- name: Amadeus Traveler Media API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amadeus-traveler-media-jsonschema-spectral-rules
- name: Amadeus Traveler Media API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 8
  slug: amadeus-traveler-media-spectral-rules
score:
  band: developing
  composite: 55.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 57.8
    developer_ergonomics: 54.3
    discoverability: 92.6
    governance: 80.2
    operational_transparency: 21.1
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/screenshots/amadeus-traveler-media-2026-07-25T195907.png
security:
- kind: domain-security
  name: Amadeus Traveler Media Domain Security
  slug: amadeus-traveler-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amadeus Traveler Media Vulnerability Disclosure
  slug: amadeus-traveler-media-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amadeus-traveler-media
tags:
- Content
- Destination
- Media
- Photos
- Points of Interest
- Tourism
- Travel
use_cases:
- description: Build destination guide features in travel apps showing attractions, restaurants, and nightlife with ratings and location context.
  name: Travel App Destination Guide
- description: Display sentiment-based ratings alongside hotel pricing to help travelers choose accommodation based on experience quality.
  name: Hotel Comparison Platform
- description: Power "where should I go next" features with personalized destination recommendations based on traveler history and preferences.
  name: Personalized Travel Inspiration
- description: Help travelers understand the character of hotels or Airbnb locations using location scores for shopping, dining, and nightlife.
  name: Neighborhood Explorer
- description: Enable AI travel assistants to recommend attractions, rate hotels, and suggest destinations based on traveler interests.
  name: AI Travel Concierge
website: https://developers.amadeus.com/
---
