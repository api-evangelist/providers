---
aid: ticketmaster
url: https://raw.githubusercontent.com/api-evangelist/ticketmaster/refs/heads/main/apis.yml
name: Ticketmaster
description: Ticketmaster is the world's largest live entertainment ticketing company, providing access to tickets for concerts, sports, theater, and other live events globally. Their developer platform offers APIs for event discovery, ticket commerce, venue data, and partner integrations, giving developers access to over 230,000 events across dozens of countries.
image: https://www.ticketmaster.com/favicon.ico
tags:
  - Commerce
  - Concerts
  - Entertainment
  - Events
  - Sports
  - Tickets
  - Venues
created: '2025-01-08'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: ticketmaster:ticketmaster-discovery-api
    name: Ticketmaster Discovery API
    description: The Ticketmaster Discovery API allows developers to search for events, attractions, venues, and classifications across the Ticketmaster platform. Provides access to over 230,000 events across the United States, Canada, Mexico, Australia, New Zealand, the UK, Ireland, and Europe. Content sources include Ticketmaster, Universe, FrontGate Tickets, and Ticketmaster Resale (TMR). Authentication is via API key in the query string or header.
    image: https://www.ticketmaster.com/favicon.ico
    humanURL: https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/
    baseURL: https://app.ticketmaster.com/discovery/v2
    tags:
      - Attractions
      - Classifications
      - Events
      - Search
      - Venues
    properties:
      - type: Documentation
        url: https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/
      - type: Portal
        url: https://developer.ticketmaster.com
      - type: OpenAPI
        url: openapi/ticketmaster-discovery-openapi.yml
  - aid: ticketmaster:ticketmaster-commerce-api
    name: Ticketmaster Commerce API
    description: The Ticketmaster Commerce API enables developers to build ticket purchasing flows, retrieve event inventory, check seat availability, and manage ticket orders. Provides access to price ranges, ticket limits, and purchase links.
    image: https://www.ticketmaster.com/favicon.ico
    humanURL: https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
    baseURL: https://app.ticketmaster.com/commerce/v2
    tags:
      - Commerce
      - Inventory
      - Orders
      - Tickets
    properties:
      - type: Documentation
        url: https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
      - type: OpenAPI
        url: openapi/ticketmaster-commerce-openapi.yml
  - aid: ticketmaster:ticketmaster-partner-api
    name: Ticketmaster Partner API
    description: The Ticketmaster Partner API is a restricted API for authorized distribution partners that enables reserving, purchasing, and retrieving ticket and event information programmatically. Authentication uses API key via query parameter or x-api-key header.
    image: https://www.ticketmaster.com/favicon.ico
    humanURL: https://developer.ticketmaster.com/products-and-docs/apis/partner/
    baseURL: https://app.ticketmaster.com/partners/v1
    tags:
      - Commerce
      - Partner
      - Reservations
      - Tickets
    properties:
      - type: Documentation
        url: https://developer.ticketmaster.com/products-and-docs/apis/partner/
      - type: FAQ
        url: https://developer.ticketmaster.com/support/partner-api-faq/
common:
  - type: Portal
    url: https://developer.ticketmaster.com
  - type: Documentation
    url: https://developer.ticketmaster.com/products-and-docs/
  - type: Getting Started
    url: https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
  - type: API Explorer
    url: https://developer.ticketmaster.com/api-explorer/v2/
  - type: Website
    url: https://www.ticketmaster.com
  - type: Blog
    url: https://developer.ticketmaster.com/blog/
  - type: Twitter
    url: https://twitter.com/ticketmaster
  - type: LinkedIn
    url: https://www.linkedin.com/company/ticketmaster
  - type: Terms of Service
    url: https://developer.ticketmaster.com/support/terms-of-use/
  - type: Privacy Policy
    url: https://www.ticketmaster.com/h/privacy.html
  - type: JSON-LD
    url: json-ld/ticketmaster-context.jsonld
  - type: JSONSchema
    url: json-schema/ticketmaster-event-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
