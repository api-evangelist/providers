---
aid: seatgeek
url: https://raw.githubusercontent.com/api-evangelist/seatgeek/refs/heads/main/apis.yml
apis:
  - aid: seatgeek:seatgeek-platform-api
    name: SeatGeek Platform API
    tags:
      - Events
      - Tickets
      - Performers
      - Venues
      - Live Events
    humanURL: https://seatgeek.com/build
    baseURL: https://api.seatgeek.com/2
    properties:
      - url: openapi/seatgeek-platform-openapi.yml
        type: OpenAPI
      - url: https://seatgeek.github.io/
        type: Documentation
      - url: https://seatgeek.com/build
        type: Portal
    description: The SeatGeek Platform API provides access to SeatGeek's comprehensive dataset of live events in the United States and Canada. The API enables developers to search events, performers, and venues, retrieve seat maps, get event recommendations, and deep-link users directly to the SeatGeek ticketing purchase flow. It supports JSON, JSONP, and XML response formats, with pagination, geolocation filtering, and price-range filtering across all event types including sports, concerts, and theater.
name: SeatGeek
tags:
  - Events
  - Tickets
  - Live Events
  - Concerts
  - Sports
  - Venues
  - Ticketing
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-02'
modified: '2026-05-02'
position: Consuming
description: SeatGeek is a live event ticketing and discovery platform that aggregates ticket inventory from multiple sources and provides a transparent, data-driven ticket buying experience. The SeatGeek Platform API gives developers access to a canonical dataset of live events including concerts, sports, and theater performances, along with performer and venue information, seating maps, ticket pricing, and personalized event recommendations. The API uses HTTP Basic Auth or query parameter authentication with a client ID and supports RESTful access to events, performers, venues, and taxonomies.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Website
    url: https://seatgeek.com
    type: Website
  - name: Developer Portal
    url: https://seatgeek.com/build
    type: Portal
  - name: API Documentation
    url: https://seatgeek.github.io/
    type: Documentation
  - name: GitHub Organization
    url: https://github.com/seatgeek
    type: GitHubOrganization
  - name: iOS SDK
    url: https://github.com/seatgeek/SGAPI
    type: SDK
  - name: API Support
    url: https://github.com/seatgeek/api-support
    type: Support
  - name: API Terms
    url: https://seatgeek.com/api-terms
    type: TermsOfService
  - url: json-schema/seatgeek-event-schema.json
    type: JSONSchema
  - url: json-structure/seatgeek-event-structure.json
    type: JSONStructure
  - url: json-ld/seatgeek-context.jsonld
    type: JSONLDContext
  - url: examples/seatgeek-list-events-example.json
    type: Example
  - url: rules/seatgeek-rules.yml
    type: SpectralRuleset
  - url: capabilities/event-discovery.yaml
    type: NaftikoCapability
  - url: vocabulary/seatgeek-vocabulary.yml
    type: Vocabulary
---
