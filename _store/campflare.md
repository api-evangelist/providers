---
aid: campflare
name: Campflare
url: https://raw.githubusercontent.com/api-evangelist/campflare/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Campgrounds
  - Outdoor
  - Recreation
  - Availability
  - Alerts
  - Webhooks
  - Reservations
access: 3rd-Party
created: '2024-11-14'
modified: '2026-04-23'
position: Provider
specificationVersion: '0.19'
description: Campflare provides real-time campground availability data and cancellation alerts as a public API. The platform tracks campsites across every major public reservation system in North America and notifies users (via webhook) the moment a site matching their criteria becomes available. Campflare's data and services are open to the public programmatically — individuals and non-profits get free access to all APIs, while commercial use requires a paid license. Campflare also powers partner products such as Hipcamp Alerts. Current API access is invite-only; requests go to contact@campflare.com and are typically granted within 24–48 hours.
apis:
  - aid: campflare:campflare-availability-api
    name: Campflare Availability & Alerts API
    description: Real-time campground availability data at the campsite level across all public campgrounds Campflare tracks. Developers can query current and upcoming availability, inspect amenities (hookups, facilities, accessibility), read official agency alerts and notices, create availability alerts with custom date/campground/site criteria, and receive webhook callbacks the moment a matching site opens up. The API is free for individuals and non-profits; commercial use requires a paid license.
    humanURL: https://campflare.com/api
    tags:
      - Campgrounds
      - Availability
      - Alerts
      - Webhooks
      - Outdoor
    properties:
      - type: Documentation
        url: https://campflare.com/api
      - type: SignUp
        url: mailto:contact@campflare.com
      - type: Webhooks
        url: https://campflare.com/api
common:
  - type: Website
    url: https://campflare.com/
  - type: Documentation
    url: https://campflare.com/api
  - type: Updates
    url: https://campflare.com/updates
  - type: FAQ
    url: https://campflare.com/info
  - type: iOSApp
    url: https://apps.apple.com/us/app/campflare/id1670055811
  - type: Contact
    url: mailto:contact@campflare.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
