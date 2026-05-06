---
aid: starwood-hotels-and-resorts
url: https://raw.githubusercontent.com/api-evangelist/starwood-hotels-and-resorts/refs/heads/main/apis.yml
modified: '2026-05-02'
name: Starwood Hotels and Resorts
description: Starwood Hotels & Resorts Worldwide was a global hotel and leisure company headquartered in Stamford, Connecticut. Prior to its acquisition by Marriott International in September 2016, Starwood operated and franchised hotels, resorts, and residences under iconic brands including Sheraton, Westin, W Hotels, St. Regis, Le Méridien, Four Points, Tribute Portfolio, Design Hotels, Element, and Aloft. The company also operated the Starwood Preferred Guest (SPG) loyalty program, which was later merged into Marriott Bonvoy. At the time of acquisition, Starwood managed over 1,300 properties in approximately 100 countries. Starwood exposed APIs for hotel search, property data, and loyalty program integration that were consumed by travel platforms and partners.
apis:
  - aid: starwood-hotels-and-resorts:hotel-search-api
    name: Hotel Search API
    description: The Starwood Hotel Search API allowed partners and developers to search Starwood's portfolio of hotels and resorts by location, dates, and availability. It supported querying by country, province, city, and date range, returning property details including name, address, category, best available rate, and SPG points redemption options. This API underpinned partner booking integrations, OTA connections, and travel management platform integrations.
    humanURL: https://www.starwoodhotels.com/
    baseURL: https://www.starwoodhotels.com/api
    tags:
      - Hotels
      - Travel
      - Hospitality
      - Search
      - Availability
    properties:
      - type: Documentation
        url: https://github.com/StayExpert/starwood
      - type: OpenAPI
        url: openapi/starwood-hotel-search-openapi.yml
  - aid: starwood-hotels-and-resorts:spg-loyalty-api
    name: SPG Loyalty API
    description: The Starwood Preferred Guest (SPG) Loyalty API provided programmatic access to the SPG loyalty program, enabling partners to query member point balances, redeem Starpoints, look up member status and tier information, and book award nights. The program offered Preferred, Gold, and Platinum status tiers with corresponding benefits. Following the Marriott acquisition, SPG was eventually merged into the Marriott Bonvoy loyalty program in 2019.
    humanURL: https://www.starwoodhotels.com/preferredguest/
    baseURL: https://www.starwoodhotels.com/api/spg
    tags:
      - Loyalty
      - Rewards
      - Hotels
      - Travel
      - Hospitality
    properties:
      - type: Documentation
        url: https://www.starwoodhotels.com/preferredguest/
  - aid: starwood-hotels-and-resorts:property-data-api
    name: Property Data API
    description: The Starwood Property Data API provided detailed information about individual hotel properties including room types, amenities, dining options, meeting and event spaces, photos, geo-coordinates, and contact information. Partners used this API to populate travel booking sites and corporate travel management systems with accurate Starwood property content.
    humanURL: https://www.starwoodhotels.com/
    baseURL: https://www.starwoodhotels.com/api/properties
    tags:
      - Hotels
      - Properties
      - Travel
      - Content
      - Hospitality
    properties:
      - type: Documentation
        url: https://www.starwoodhotels.com/
common:
  - type: Website
    url: https://www.starwoodhotels.com
  - type: Developer Portal
    url: https://github.com/StayExpert/starwood
  - type: LinkedIn
    url: https://www.linkedin.com/company/starwoodhotels
  - type: Facebook
    url: https://www.facebook.com/starwood
  - type: Blog
    url: https://www.starwoodhotels.com/corporate/
  - type: Acquisition
    url: https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-completes-acquisition-starwood-hotels
  - type: Terms of Service
    url: https://www.starwoodhotels.com/corporate/terms.html
  - type: Privacy Policy
    url: https://www.starwoodhotels.com/corporate/privacy.html
  - type: OpenAPI
    url: openapi/starwood-hotel-search-openapi.yml
  - type: JSONSchema
    url: json-schema/starwood-hotel-search-schema.json
  - type: JSONStructure
    url: json-structure/starwood-hotel-structure.json
  - type: JSONLD
    url: json-ld/starwood-hotels-and-resorts-context.jsonld
  - type: Vocabulary
    url: vocabulary/starwood-hotels-and-resorts-vocabulary.yml
  - type: SpectralRules
    url: rules/starwood-hotels-and-resorts-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/hotel-booking.yaml
---
