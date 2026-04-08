---
aid: tripadvisor
url: https://raw.githubusercontent.com/api-evangelist/tripadvisor/refs/heads/main/apis.yml
apis:
- aid: tripadvisor:content-api
  name: Tripadvisor Content API
  tags:
  - Attractions
  - Hotels
  - Locations
  - Restaurants
  - Reviews
  - Travel
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.content.tripadvisor.com
  humanURL: https://developer-tripadvisor.com/content-api/
  properties:
  - url: https://developer-tripadvisor.com/content-api/
    type: Documentation
  - url: openapi/tripadvisor-content-api-openapi.yml
    type: OpenAPI
  description: The Tripadvisor Content API provides developers with access to Tripadvisor's extensive dataset of more than 7.5 million locations, 1 billion reviews and opinions, and content in 29 languages. The API includes endpoints for location search, location details, location photos, and location reviews, enabling developers to integrate rich travel content into their websites and applications. The first 5,000 API calls per month are free, making it accessible for initial development and testing.
- aid: tripadvisor:hotel-availability-check-api
  name: Tripadvisor Hotel Availability Check API
  tags:
  - Availability
  - Booking
  - Hospitality
  - Hotels
  - Travel
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer-tripadvisor.com/connectivity-solutions/hotel-availability-check-api/
  properties:
  - url: https://developer-tripadvisor.com/connectivity-solutions/hotel-availability-check-api/
    type: Documentation
  - url: openapi/tripadvisor-hotel-availability-check-api-openapi.yml
    type: OpenAPI
  description: The Tripadvisor Hotel Availability Check (HAC) API allows hotel booking partners to display their availability and pricing on Tripadvisor. When a user views a hotel page, Tripadvisor sends HTTP POST requests to the partner's API to retrieve real-time price and availability data. The API supports batch requests for multiple hotels and requires responses within 5 seconds on average. The current version (v8) provides richer availability data to help partners increase conversions.
- aid: tripadvisor:hotel-inventory-api
  name: Tripadvisor Hotel Inventory API
  tags:
  - Connectivity
  - Hospitality
  - Hotels
  - Inventory
  - Travel
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer-tripadvisor.com/connectivity-solutions/hotel-availability-check-api/documentation/hotel_inventory/
  properties:
  - url: https://developer-tripadvisor.com/connectivity-solutions/hotel-availability-check-api/documentation/hotel_inventory/
    type: Documentation
  - url: openapi/tripadvisor-hotel-availability-check-api-openapi.yml
    type: OpenAPI
  description: The Tripadvisor Hotel Inventory API enables connectivity partners to manage their hotel inventory listings on the Tripadvisor platform. Partners use this API to register and update the hotels they can provide availability and pricing data for, ensuring that their connected properties are accurately represented. This API works in conjunction with the Hotel Availability Check API as part of Tripadvisor's connectivity solutions for the hospitality industry.
name: Tripadvisor
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Tripadvisor is the world's largest travel guidance platform, helping hundreds of millions of travelers each month find places to stay, things to do, and restaurants through reviews, photos, and tools.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

