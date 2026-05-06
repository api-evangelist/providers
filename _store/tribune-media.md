---
aid: tribune-media
name: Tribune Media
description: Tribune Media was a diversified media and entertainment company with broadcasting, digital, and content businesses. Through Tribune Media Services (TMS), it provided comprehensive entertainment data APIs including TV programming, movie showtimes, celebrity information, and sports data. Tribune Media was acquired by Nexstar Media Group in 2019. The TMS OnConnect APIs are now operated by Gracenote (a Nielsen company), providing metadata for TV shows, movies, celebrities, and televised sports to consumer electronics manufacturers, cable operators, entertainment platforms, and application developers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Media
  - Entertainment
  - Broadcasting
  - Television
  - Movies
  - Sports
  - Celebrity
url: https://raw.githubusercontent.com/api-evangelist/tribune-media/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tribune-media:tms-onconnect
    name: TMS OnConnect API
    description: The Tribune Media Services (TMS) OnConnect API provides comprehensive entertainment metadata for TV programming, movies, celebrities, and sports. It delivers electronic programming guide (EPG) data, movie showtimes, celebrity information, and televised sports schedules. Originally developed by Tribune Media Services, the API is now operated by Gracenote (a Nielsen company) and powers content discovery for consumer electronics manufacturers, cable operators, and entertainment platforms.
    humanURL: https://developer.tmsapi.com/
    tags:
      - Entertainment
      - Television
      - Movies
      - Sports
      - Celebrity
      - Programming Guide
      - Metadata
    properties:
      - type: Documentation
        url: https://developer.tmsapi.com/docs
      - type: GettingStarted
        url: https://developer.tmsapi.com/Getting_Started
      - type: TermsOfService
        url: https://developer.tmsapi.com/page/API_Terms_of_Use
      - type: FAQ
        url: https://developer.tmsapi.com/page/Frequently_Asked_Questions
      - type: OpenAPI
        url: openapi/tms-onconnect-openapi.yml
features:
  - TV lineup and electronic programming guide (EPG) data
  - Movie showtimes and theatre location lookups
  - Celebrity details and appearance schedules
  - Sports event schedules and team information
  - Series, episode, and program metadata
  - Program images via Media Cloud CDN
  - International lineup support
  - Online video and social data endpoints
useCases:
  - Electronic programming guide (EPG) integration for smart TVs and set-top boxes
  - Movie discovery and showtime lookup applications
  - Sports schedule and broadcast tracking
  - Celebrity appearance and talk show scheduling
  - Content recommendation engines using entertainment metadata
  - Mobile apps integrating TV schedule and movie showtimes
integrations:
  - Gracenote (Nielsen) - current operator of TMS data services
  - Digitalsmiths Seamless Discovery platform - original API infrastructure
  - Placecast MatchAPI - movie showtimes integration
  - Mashery - API key management and developer portal
solutions:
  - Consumer electronics manufacturers requiring EPG data
  - Cable and satellite operators needing programming metadata
  - Entertainment platform providers building content discovery
  - Application developers integrating TV and movie information
common:
  - type: Website
    url: https://www.tribunemedia.com/
  - type: DeveloperPortal
    url: https://developer.tmsapi.com/
  - type: Documentation
    url: https://developer.tmsapi.com/docs
  - type: GettingStarted
    url: https://developer.tmsapi.com/Getting_Started
  - type: TermsOfService
    url: https://developer.tmsapi.com/page/API_Terms_of_Use
  - type: SignUp
    url: https://developer.tmsapi.com/member/register
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
