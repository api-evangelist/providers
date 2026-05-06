---
aid: autoura
name: Autoura
description: Autoura is a digital experience platform for real-world tourism and travel experiences. They develop software and APIs that enable travel companies, destination management organizations, and developers to access and integrate tourism content including destination information, tour itineraries, cuisine guides, activities, and interactive local experience recommendations.
tags:
  - Tourism
  - Tours
  - Travel
  - Destinations
  - Experiences
  - Digital Tourism
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/autoura/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: autoura:autoura-api
    name: Autoura Experience API
    description: The Autoura Experience API provides access to tourism content including cuisine guides, destination information, tour itineraries, local activities, and points of interest. Developers can integrate Autoura content into travel applications, tourism websites, and experience booking platforms to provide personalized local recommendations.
    humanURL: https://www.autoura.com/docs/api/cuisines
    tags:
      - Tourism
      - Tours
      - Travel
      - Destinations
      - Activities
      - Cuisine
    properties:
      - type: Documentation
        url: https://www.autoura.com/docs/api/cuisines
      - type: Website
        url: https://www.autoura.com
common:
  - type: Website
    url: https://www.autoura.com
  - type: Documentation
    url: https://www.autoura.com/docs/api/cuisines
  - type: Features
    data:
      - name: Destination Content API
        description: Access rich destination content including local attractions, points of interest, neighborhood guides, and cultural highlights for tourism applications and travel content platforms.
      - name: Cuisine and Food Guide API
        description: Comprehensive cuisine data including local dishes, restaurant types, food tours, and gastronomic experience recommendations for culinary tourism applications.
      - name: Tour Itineraries
        description: Pre-built tour itineraries and self-guided tour content for destinations, enabling travel apps to offer structured sightseeing experiences.
      - name: Activity Recommendations
        description: Activity and experience data for destinations including outdoor activities, cultural experiences, adventure tourism, and seasonal events.
      - name: Personalized Recommendations
        description: Context-aware recommendation engine for suggesting local experiences based on traveler preferences, location, and time of visit.
  - type: UseCases
    data:
      - name: Travel App Integration
        description: Integrate Autoura destination content into travel booking apps and tourism portals to enhance destination discovery and trip planning.
      - name: Destination Marketing
        description: Destination management organizations embed Autoura experience content into tourism websites to promote local attractions and activities.
      - name: Culinary Tourism
        description: Food and travel platforms use the Cuisine API to build gastronomic guides and food tour features for culinary travelers.
      - name: Digital Tour Guide Apps
        description: Build digital tour guide applications with self-guided audio tours, interactive maps, and Autoura destination content.
  - type: Integrations
    data:
      - name: Booking Platforms
        description: Integration with travel booking platforms to surface Autoura activity and experience content alongside accommodation and transport bookings.
      - name: Mapping Services
        description: Combine Autoura POI and destination content with Google Maps, Mapbox, or Apple Maps for location-aware tourism applications.
      - name: CMS Platforms
        description: Embed Autoura destination content into CMS-based tourism websites using API integrations for dynamic content delivery.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
