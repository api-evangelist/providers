---
aid: booking-com
url: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/apis.yml
apis:
- aid: booking-com:demand-api
  name: Booking.com Demand API
  tags:
  - Accommodations
  - Affiliates
  - Booking
  - Hotels
  - Search
  - Travel
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://demandapi.booking.com
  humanURL: https://developers.booking.com/demand/docs/getting-started/overview
  properties:
  - url: https://developers.booking.com/demand/docs/getting-started/overview
    type: Documentation
  - url: openapi/booking-com-demand-api-openapi.yml
    type: OpenAPI
  description: The Booking.com Demand API is a RESTful API that enables Affiliate Partners to access Booking.com's extensive travel inventory. It provides endpoints for searching accommodations such as hotels and apartments, checking availability, retrieving reviews, and getting detailed property information. The API uses JSON responses and requires HTTPS POST requests with Affiliate ID and token authentication.
- aid: booking-com:car-rentals-api
  name: Booking.com Car Rentals API
  tags:
  - Car Rentals
  - Transportation
  - Travel
  - Vehicles
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://demandapi.booking.com
  humanURL: https://developers.booking.com/demand/docs/open-api/demand-api/cars
  properties:
  - url: https://developers.booking.com/demand/docs/open-api/demand-api/cars
    type: Documentation
  - url: openapi/booking-com-car-rentals-api-openapi.yml
    type: OpenAPI
  description: The Booking.com Car Rentals API is part of the Demand API and provides endpoints specific to the car rental segment of the connected trip experience. Developers can use it to search for available car rentals, retrieve car details, and look up depots and suppliers. The API enables affiliate partners to integrate Booking.com's car rental inventory into their own platforms, offering users the ability to find and book vehicles as part of their travel planning workflow.
- aid: booking-com:connectivity-content-api
  name: Booking.com Connectivity Content API
  tags:
  - Connectivity
  - Content Management
  - Hotels
  - Properties
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://supply-xml.booking.com
  humanURL: https://developers.booking.com/connectivity/docs/content
  properties:
  - url: https://developers.booking.com/connectivity/docs/content
    type: Documentation
  - url: openapi/booking-com-connectivity-content-api-openapi.yml
    type: OpenAPI
  description: The Booking.com Connectivity Content API enables Connectivity Partners to register properties and modify their content directly without using the Booking.com extranet. Partners can manage facilities, rates, rooms, photos, and other property details programmatically. This API is designed for property management systems, channel managers, and other connectivity solutions that need to create and maintain property listings on Booking.com at scale.
- aid: booking-com:connectivity-reservations-api
  name: Booking.com Connectivity Reservations API
  tags:
  - Booking
  - Connectivity
  - Hotels
  - Reservations
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://secure-supply-xml.booking.com
  humanURL: https://developers.booking.com/connectivity/docs
  properties:
  - url: https://connect.booking.com/user_guide/site/en-US/res/
    type: Documentation
  - url: openapi/booking-com-connectivity-reservations-api-openapi.yml
    type: OpenAPI
  description: The Booking.com Connectivity Reservations API allows Connectivity Partners to retrieve and update reservation information for properties listed on Booking.com. It operates over a PCI-compliant secure endpoint and supports reservation retrieval, confirmation, and modification. This API is essential for property management systems and channel managers that need to synchronize booking data between Booking.com and their own systems in real time.
- aid: booking-com:connectivity-rates-availability-api
  name: Booking.com Connectivity Rates and Availability API
  tags:
  - Availability
  - Connectivity
  - Inventory
  - Pricing
  - Rates
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://supply-xml.booking.com
  humanURL: https://developers.booking.com/connectivity/docs/ari
  properties:
  - url: https://developers.booking.com/connectivity/docs/ari
    type: Documentation
  - url: openapi/booking-com-connectivity-rates-availability-api-openapi.yml
    type: OpenAPI
  description: The Booking.com Connectivity Rates and Availability API allows Connectivity Partners to set room availability, pricing, and restrictions for properties on Booking.com. Partners can manage advance booking windows, length of stay requirements, and rate plans programmatically.
- aid: booking-com:connectivity-promotions-api
  name: Booking.com Connectivity Promotions API
  tags:
  - Connectivity
  - Deals
  - Discounts
  - Marketing
  - Promotions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://supply-xml.booking.com
  humanURL: https://developers.booking.com/connectivity/docs
  properties:
  - url: https://developers.booking.com/connectivity/docs
    type: Documentation
  - url: openapi/booking-com-connectivity-promotions-api-openapi.yml
    type: OpenAPI
  description: The Booking.com Connectivity Promotions API enables Connectivity Partners to create and manage promotional offers for properties listed on Booking.com. Partners can programmatically set up deals, discounts, and special rates to attract travelers and increase bookings.
name: Booking Com
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Seamlessly incorporate Booking.com inventory into your travel application.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

