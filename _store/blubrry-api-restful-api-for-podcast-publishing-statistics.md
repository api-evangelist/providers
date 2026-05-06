---
aid: blubrry-api-restful-api-for-podcast-publishing-statistics
name: Blubrry API
description: Blubrry is a podcast hosting and statistics platform providing a RESTful API for podcast publishing, media management, episode management, audience statistics, and podcast network functionality. The API uses OAuth 2.0 authentication and enables third-party applications to integrate with podcast hosting workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/blubrry-api-restful-api-for-podcast-publishing-statistics/refs/heads/main/apis.yml
created: '2025-05-02'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Podcasting
  - Audio
  - Media
  - Publishing
  - Statistics
apis:
  - aid: blubrry-api-restful-api-for-podcast-publishing-statistics:blubrry-podcast-media-hosting-api
    name: Blubrry Podcast Media Hosting API
    description: The Blubrry Podcast Media Hosting API enables uploading and managing podcast media files through third-party applications. Supports listing shows, retrieving unpublished media files, deleting media, and publishing podcast media for shows hosted on Blubrry.
    humanURL: https://blubrry.com/developer/api/
    tags:
      - Podcasting
      - Media
      - Hosting
      - Publishing
    properties:
      - type: Documentation
        url: https://blubrry.com/developer/api/
      - type: Authentication
        url: https://blubrry.com/developer/api/
  - aid: blubrry-api-restful-api-for-podcast-publishing-statistics:blubrry-episode-management-api
    name: Blubrry Episode Management API
    description: The Blubrry Episode Management API supports creating new podcast episodes (publish, schedule, or save as draft) and updating existing episode fields. Enables CMS and podcast production tools to manage episode metadata programmatically.
    humanURL: https://blubrry.com/developer/api/
    tags:
      - Podcasting
      - Episodes
      - Publishing
      - CMS
    properties:
      - type: Documentation
        url: https://blubrry.com/developer/api/
  - aid: blubrry-api-restful-api-for-podcast-publishing-statistics:blubrry-podcast-statistics-api
    name: Blubrry Podcast Statistics API
    description: The Blubrry Podcast Statistics API provides analytics for podcast episodes including download and play counts, overall show download summaries, monthly download breakdowns, and episode-level statistics for measuring podcast audience reach and growth.
    humanURL: https://blubrry.com/developer/api/
    tags:
      - Podcasting
      - Statistics
      - Analytics
      - Downloads
      - Audience
    properties:
      - type: Documentation
        url: https://blubrry.com/developer/api/
  - aid: blubrry-api-restful-api-for-podcast-publishing-statistics:blubrry-podcast-network-api
    name: Blubrry Podcast Network API
    description: The Blubrry Podcast Network API provides access to user subscriptions with show management, episode metadata storage including playback status and position, show navigation by category and search, and access to Blubrry's podcast directory.
    humanURL: https://blubrry.com/developer/api/
    tags:
      - Podcasting
      - Network
      - Subscriptions
      - Directory
    properties:
      - type: Documentation
        url: https://blubrry.com/developer/api/
common:
  - type: Website
    url: https://blubrry.com
  - type: Portal
    url: https://blubrry.com/developer/api/
  - type: Documentation
    url: https://blubrry.com/developer/api/
  - type: Authentication
    url: https://blubrry.com/developer/api/
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
