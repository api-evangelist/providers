---
aid: carmax
url: https://raw.githubusercontent.com/api-evangelist/carmax/refs/heads/main/apis.yml
name: CarMax
description: 'CarMax (NYSE: KMX) is the largest retailer of used cars in the United States, operating an omnichannel business that spans brick-and-mortar stores, carmax.com online purchasing, home delivery, financing, appraisals, and trade-ins. CarMax does not publish a public developer portal, but its engineering organization operates an extensive internal API program built around distinct API roles (Data Access Layer, Business Logic Layer, Server-Driven UI, Backend for Frontend). Public-facing APIs documented by the CarMax Engineering Blog include a Store Locations API and a Vehicle Inventory API, and CarMax has publicly discussed a Server-Driven UI API that controls vehicle search filters across web and mobile. Partner and syndication integrations are handled case by case rather than through a self-service portal.'
type: Index
x-type: company
position: Consumer
access: Partner
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Auto Financing
  - Auto Retail
  - Appraisals
  - Automotive
  - Omnichannel
  - Retail
  - Server-Driven UI
  - Used Cars
  - Vehicle Inventory
  - VIN Lookup
created: '2026-03-21'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: carmax:store-locations-api
    name: CarMax Store Locations API
    description: The CarMax Store Locations API, discussed publicly on the CarMax Engineering Blog, exposes details about all CarMax store locations including addresses, hours, services offered, and geographic metadata. It is consumed primarily by carmax.com, the CarMax mobile app, and CarMax's digital marketing and SEO systems. The API is not offered as a self-service product to third parties.
    humanURL: https://www.carmax.com/stores
    tags:
      - Auto Retail
      - Store Locator
    properties:
      - url: https://www.carmax.com/stores
        type: Documentation
      - url: https://medium.com/carmax-engineering-blog
        type: Engineering Blog
    x-features:
      - Address, hours, and services per store
      - Geographic metadata for mapping
      - Used as a source of truth across CarMax channels
    x-use-cases:
      - Store locator on carmax.com and mobile
      - SEO and local-landing-page generation
      - Internal operations dashboards
  - aid: carmax:vehicle-inventory-api
    name: CarMax Vehicle Inventory API
    description: The CarMax Vehicle Inventory API exposes details about all used vehicles currently in CarMax's nationwide inventory, including year/make/model, trim, mileage, price, exterior and interior attributes, photos, and stock number. The API powers carmax.com's search experience and the Vehicle Detail Page. It is consumed internally and surfaced to customers through CarMax's own products rather than opened as a public partner feed.
    humanURL: https://www.carmax.com/cars
    tags:
      - Auto Retail
      - Automotive
      - Used Cars
      - Vehicle Inventory
    properties:
      - url: https://www.carmax.com/cars
        type: Documentation
      - url: https://medium.com/carmax-engineering-blog/api-roles-aec7999c095c
        type: Engineering Blog
    x-features:
      - Nationwide used-vehicle inventory
      - Year/make/model/trim, mileage, price, stock number
      - Exterior, interior, and photo metadata
      - Powers carmax.com search and VDP
    x-use-cases:
      - Online vehicle search and listing pages
      - Home delivery and store-transfer eligibility
      - Price and market analytics
      - Third-party automotive marketplaces (via syndication agreements)
  - aid: carmax:vehicle-search-sdui-api
    name: CarMax Vehicle Search Server-Driven UI API
    description: The CarMax Vehicle Search Server-Driven UI API controls the search filters and list layouts presented across carmax.com and CarMax's mobile apps. It was rewritten approximately three years prior to March 2026 and is an example of a Server-Driven UI pattern where the back end determines which filters and controls render on the client. It is an internal API, not published for external developers.
    humanURL: https://www.carmax.com/cars
    tags:
      - Auto Retail
      - Omnichannel
      - Server-Driven UI
    properties:
      - url: https://medium.com/carmax-engineering-blog/api-roles-aec7999c095c
        type: Engineering Blog
    x-features:
      - Server-Driven UI filter and layout payloads
      - Consistent web and mobile experience
      - Back-end controlled A/B testing and rollout
    x-use-cases:
      - Unified search UX across channels
      - Rapid filter experimentation
      - Per-market and per-user personalization
common:
  - type: Website
    url: https://www.carmax.com/
  - type: Stores
    url: https://www.carmax.com/stores
  - type: Cars
    url: https://www.carmax.com/cars
  - type: Finance
    url: https://www.carmax.com/finance
  - type: Sell Your Car
    url: https://www.carmax.com/sell-my-car
  - type: Engineering Blog
    url: https://medium.com/carmax-engineering-blog
  - type: Careers
    url: https://jobs.carmax.com/
  - type: Investor Relations
    url: https://investors.carmax.com/
  - type: Contact
    url: https://www.carmax.com/customer-service
  - type: Terms of Service
    url: https://www.carmax.com/terms
  - type: Privacy Policy
    url: https://www.carmax.com/privacy
  - type: LinkedIn
    url: https://www.linkedin.com/company/carmax
  - type: X
    url: https://x.com/CarMax
  - type: Facebook
    url: https://www.facebook.com/CarMax
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
