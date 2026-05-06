---
aid: astrology-api
name: Astrology API
description: Astrology API (astrologyapi.com) is a powerful tool that provides developers with access to accurate and reliable astrological data. The API offers Indian (Vedic) astrology, Western astrology, horoscope predictions, tarot readings, and PDF report generation. It provides planetary positions, zodiac sign information, birth chart calculations, compatibility analysis, panchang data, moon phases, and daily/monthly horoscope predictions. The API is JSON-based with SDK support and Postman collections available for testing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Astrology
  - Horoscopes
  - Zodiac
  - Vedic Astrology
  - Western Astrology
url: https://raw.githubusercontent.com/api-evangelist/astrology-api/refs/heads/main/apis.yml
created: '2025-01-07'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: astrology-api:astrology-api
    name: Astrology API
    description: The Astrology API provides comprehensive astrological data including Indian (Vedic) astrology with panchang and dosha data, Western astrology with planetary transits and synastry, daily and monthly horoscope predictions, tarot readings, and PDF report generation in both Western and Indian formats.
    humanURL: https://astrologyapi.com/docs
    baseURL: https://json.astrologyapi.com/v1
    tags:
      - Astrology
      - Horoscopes
      - Vedic
      - Western
    properties:
      - type: Documentation
        url: https://astrologyapi.com/docs
      - type: GettingStarted
        url: https://astrologyapi.com/docs/quickstart
      - type: OpenAPI
        url: openapi/astrology-api-openapi.yml
common:
  - type: Portal
    url: https://astrologyapi.com/
    title: Astrology API Website
  - type: Documentation
    url: https://astrologyapi.com/docs
    title: Documentation
  - type: SignUp
    url: https://astrologyapi.com/signup
    title: Sign Up
  - type: Pricing
    url: https://astrologyapi.com/pricing
    title: Pricing
  - type: Features
    data:
      - name: Indian (Vedic) Astrology
        description: Vedic astrology data including birth chart basics, horoscope dosha analysis, yearly predictions (Varshaphal), daily nakshatra forecasts, and panchang (Hindu almanac) data.
      - name: Western Astrology
        description: Western astrology data including birth chart basics, numerology, synastry (relationship analysis), moon phases, planetary transits, and zodiac compatibility.
      - name: Horoscope Predictions
        description: Daily, weekly, and monthly horoscope predictions for all sun signs in both Western and Vedic astrology traditions.
      - name: Tarot API
        description: General tarot card readings and yes/no tarot predictions for integrating tarot functionality into applications.
      - name: PDF Report Generation
        description: Generate detailed PDF horoscope reports in five types covering both Western and Indian astrology formats for end-user delivery.
  - type: UseCases
    data:
      - name: Astrology App Development
        description: Developers build mobile and web astrology applications integrating daily horoscopes, birth charts, and compatibility analysis.
      - name: Horoscope Website Integration
        description: Content websites add personalized horoscope sections using the Astrology API's daily and monthly prediction endpoints.
      - name: Vedic Consultation Platforms
        description: Astrology consultation platforms use the Vedic API for birth chart calculations and panchang data to support professional astrologers.
  - type: Integrations
    data:
      - name: Postman Collection
        description: Official Postman collection available for testing Astrology API endpoints before integration.
      - name: SDK Downloads
        description: Language-specific SDK downloads available for easier integration with the Astrology API.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
