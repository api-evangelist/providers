---
aid: realtor
url: https://raw.githubusercontent.com/api-evangelist/realtor/refs/heads/main/apis.yml
modified: '2026-04-28'
apis:
  - aid: realtor:connections-plus-api
    name: Realtor.com Connections Plus API
    tags:
      - Agents
      - Brokers
      - CRM
      - Leads
      - Real Estate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.realtor.com/marketing/connections/
    properties:
      - url: https://www.realtor.com/marketing/connections/
        type: Documentation
      - url: asyncapi/realtor-connections-plus-asyncapi.yml
        type: AsyncAPI
    description: The Realtor.com Connections Plus API provides a direct connection between the Realtor.com lead delivery system and supporting CRM platforms. It enables real estate agents, brokers, and offices to receive buyer and seller leads in real time via API rather than email. The API delivers richer lead data including listing URLs, geographic coordinates, dates, and MLS information that are not available through standard email delivery.
  - aid: realtor:lead-delivery-api
    name: Realtor.com Lead Delivery API
    tags:
      - CRM Integration
      - Delivery
      - Leads
      - Notifications
      - Real Estate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.realtor.com/marketing/connections/
    properties:
      - url: https://www.realtor.com/marketing/connections/
        type: Documentation
      - url: asyncapi/realtor-lead-delivery-asyncapi.yml
        type: AsyncAPI
    description: The Realtor.com Lead Delivery API is an end-to-end integration layer that delivers real estate leads directly from Realtor.com to third-party CRM systems. It provides faster and more secure lead delivery compared to traditional email-based methods, with consistent formatting and additional data fields.
  - aid: realtor:property-data-api
    name: Realtor.com Property Data API
    tags:
      - MLS
      - Property Data
      - Property Listings
      - Real Estate
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://realtor.p.rapidapi.com
    humanURL: https://rapidapi.com/apidojo/api/realty-in-us
    properties:
      - url: https://rapidapi.com/apidojo/api/realty-in-us
        type: Documentation
      - url: openapi/realtor-property-data-openapi.yml
        type: OpenAPI
    description: The Realtor.com Property Data API provides programmatic access to real estate listing data from Realtor.com, one of the largest property listing platforms in the United States. It offers endpoints for searching properties by location, price range, bedrooms, bathrooms, and other criteria, as well as retrieving detailed property information including listing status, photos, and neighborhood data.
common:
  - type: JSON-LD
    url: json-ld/realtor-context.jsonld
  - type: JSONSchema
    url: json-schema/realtor-lead-schema.json
  - type: JSONSchema
    url: json-schema/realtor-property-schema.json
description: Realtor.com is an online real estate marketplace operated by Move, Inc., providing home listings, neighborhood information, and tools for buyers, sellers, and renters.
---
