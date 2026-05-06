---
aid: nascar
name: NASCAR
description: NASCAR, the National Association for Stock Car Auto Racing, is a professional auto racing organization that sanctions and governs multiple racing series, including the popular NASCAR Cup Series. NASCAR exposes a feed API documented via Swagger that delivers race results, standings, schedules, driver and team information, and other motorsport data for partners, broadcasters, and fans.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/nascar/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Auto Racing
  - Sports
  - Stock Cars
  - Motorsports
  - Race Results
  - Schedules
apis:
  - aid: nascar:nascar
    name: NASCAR Feed API
    tags:
      - Auto Racing
      - Sports
      - Stock Cars
      - Motorsports
    humanURL: https://feed.nascar.com/swagger/ui/index
    properties:
      - url: https://feed.nascar.com/swagger/ui/index
        type: Documentation
      - url: https://feed.nascar.com/swagger/ui/index
        type: Reference
    description: The NASCAR Feed API provides access to race results, standings, schedules, driver and team information, lap-by-lap data, and other motorsport data across NASCAR's racing series. Documentation is published via Swagger UI.
common:
  - url: https://www.nascar.com/
    type: Website
  - url: https://feed.nascar.com/swagger/ui/index
    type: Documentation
  - url: https://www.nascar.com/terms-of-service/
    type: Terms of Service
  - url: https://www.nascar.com/privacy-policy/
    type: Privacy Policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
