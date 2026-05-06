---
aid: southwest-airlines
name: Southwest Airlines
description: Southwest Airlines is one of the world's most profitable airlines and the largest domestic air carrier in the United States by number of passengers. The company provides scheduled air transportation in the United States and near-international markets, known for its low fares, no baggage fees policy, and customer service. Southwest Airlines is a Fortune 500 company headquartered in Dallas, Texas.
url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Fortune 500
  - Airlines
  - Aviation
  - Travel
apis:
  - aid: southwest-airlines:southwest-flight-api
    name: Southwest Airlines Flight API
    description: The Southwest Airlines internal flight booking API powers the southwest.com website for searching and booking flights. It provides flight availability, pricing, schedules, and air booking shopping capabilities. Third-party flight data aggregators also provide API access to Southwest flight schedules and status information.
    humanURL: https://www.southwest.com/
    baseURL: https://www.southwest.com/api
    tags:
      - Airlines
      - Flight Booking
      - Flight Search
      - Travel
    properties:
      - type: Website
        url: https://www.southwest.com/
      - type: Documentation
        url: https://www.southwest.com/
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/json-schema/southwest-airlines-flight-schema.json
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/json-schema/southwest-airlines-reservation-schema.json
  - aid: southwest-airlines:southwest-rapid-rewards-api
    name: Southwest Airlines Rapid Rewards API
    description: The Rapid Rewards loyalty program API enables management of points balances, redemption, and tier status for Southwest Airlines frequent fliers.
    humanURL: https://www.southwest.com/rapid-rewards/
    tags:
      - Loyalty
      - Rewards
      - Airlines
    properties:
      - type: Website
        url: https://www.southwest.com/rapid-rewards/
  - aid: southwest-airlines:southwest-inflight-api
    name: Southwest Airlines In-Flight Network API
    description: The Southwest Airlines in-flight network provides a JSON API available at getconnected.southwestwifi.com/current.json while onboard the aircraft. It delivers real-time flight information including speed, altitude, position, weather, and flight status to connected passengers.
    humanURL: https://getconnected.southwestwifi.com/
    baseURL: https://getconnected.southwestwifi.com
    tags:
      - In-Flight
      - Airlines
      - Flight Status
      - Real-Time
    properties:
      - type: Documentation
        url: https://apievangelist.com/2016/10/06/your-southwest-airlines-flight-has-an-api/
common:
  - type: Website
    url: https://www.southwest.com
  - type: Investor Relations
    url: https://ir.southwest.com/
  - type: GitHub Organization
    url: https://github.com/SouthwestAir
  - type: LinkedIn
    url: https://www.linkedin.com/company/southwest-airlines
  - type: X
    url: https://twitter.com/SouthwestAir
  - type: Open Source
    url: https://github.com/SouthwestAir/.github
  - type: JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/json-ld/southwest-airlines-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/vocabulary/southwest-airlines-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
