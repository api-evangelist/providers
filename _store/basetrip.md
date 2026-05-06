---
aid: basetrip
url: https://raw.githubusercontent.com/api-evangelist/basetrip/refs/heads/main/apis.yml
name: Basetrip
description: Basetrip is a travel intelligence platform providing APIs for country and city data, travel phrases, safety ratings, visa requirements, cost of living estimates, and health advisories. Designed to help travel apps, booking platforms, and trip planning tools differentiate their products and improve traveler experiences. The Basetrip API v3 uses API key authentication and returns JSON.
tags:
  - Cities
  - Countries
  - Health
  - Safety
  - Travel
  - Visa
type: Contract
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-11-13'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: basetrip:basetrip-api
    name: Basetrip API
    tags:
      - Cities
      - Countries
      - Health
      - Phrases
      - Safety
      - Travel
      - Visa
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.thebasetrip.com/v3
    humanURL: https://www.thebasetrip.com/en/documentation/v3
    properties:
      - url: https://www.thebasetrip.com/en/documentation/v3
        type: Documentation
      - url: openapi/basetrip-api-openapi.yml
        type: OpenAPI
    description: The Basetrip API provides travel intelligence data including country details, city lists, travel phrases, safety ratings, visa requirements, cost estimates, and health advisories. Uses API key authentication via X-API-Key header.
common:
  - type: Website
    url: https://www.thebasetrip.com/
    name: Basetrip
  - type: Documentation
    url: https://www.thebasetrip.com/en/documentation/v3
    name: Basetrip API Documentation
  - type: SignUp
    url: https://www.thebasetrip.com/en/sign_up
    name: Sign Up
  - type: Pricing
    url: https://www.thebasetrip.com/en/pricing
    name: Pricing
  - type: SpectralRules
    url: rules/basetrip-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/basetrip-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/travel-intelligence.yaml
  - type: JSON-LD
    url: json-ld/basetrip-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Country Data
        description: Country names, slugs, alpha-2 codes, capital, currency, languages, population, and timezone.
      - name: City Data
        description: City names, slugs, geographic coordinates, and timezone information per country.
      - name: Travel Phrases
        description: Language phrases for travel in English, French, German, Italian, and Spanish.
      - name: Safety Ratings
        description: Country safety ratings and travel advisory levels from 1 (normal) to 4 (do not travel).
      - name: Cost Estimates
        description: Daily budget estimates for budget, mid-range, and luxury traveler tiers.
      - name: Visa Requirements
        description: Visa requirement lookup by passport country and destination country.
      - name: Health Advisories
        description: Vaccination requirements, health risks, drinking water safety, and medical facility ratings.
  - name: Use Cases
    type: UseCases
    data:
      - name: Travel App Integration
        description: Embed country and city intelligence directly into travel booking apps.
      - name: Trip Planning Tools
        description: Provide travelers with safety, cost, and visa information before booking.
      - name: Destination Guides
        description: Power destination content with live data on safety, costs, and health.
      - name: Travel Risk Assessment
        description: Assess travel risk using safety ratings and health advisories for corporate travel.
      - name: Language Assistance
        description: Surface travel phrases in destination language for traveler communication tools.
  - name: Integrations
    type: Integrations
    data:
      - name: Booking.com
      - name: Airbnb
      - name: TripAdvisor
      - name: Skyscanner
      - name: Expedia
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
