---
aid: songstats
name: Songstats
description: Songstats provides music data analytics through its Enterprise API, enabling music industry professionals to access streaming statistics, audience data, chart positions, playlist placements, and catalog information for artists, tracks, record labels, and collaborators across all major streaming platforms including Spotify, Apple Music, Amazon Music, Deezer, TikTok, and more. Integrated with Radiostats for radio airplay data across 40,000+ stations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Music
  - Streaming
  - Artists
  - Tracks
  - Labels
url: https://raw.githubusercontent.com/api-evangelist/songstats/refs/heads/main/apis.yml
created: '2025-02-12'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: songstats:songstats-enterprise-api
    name: Songstats Enterprise API
    description: The Songstats Enterprise API (v1) provides music data analytics for artists, tracks, labels, and collaborators. Endpoints return JSON data including current stats, historic stats, audience details, catalog information, activities, top playlists, top tracks, and geographic location data across major streaming platforms. Authentication uses an API key in the request header. Includes Radiostats integration for radio airplay data.
    humanURL: https://docs.songstats.com/
    baseURL: https://api.songstats.com/enterprise/v1
    tags:
      - Analytics
      - Music
      - Streaming
      - Artists
      - Tracks
      - Labels
      - Collaborators
    properties:
      - type: Documentation
        url: https://docs.songstats.com/
      - type: Reference
        url: https://docs.songstats.com/docs/api/e80265bb8b01b-songstats-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/songstats/refs/heads/main/openapi/songstats-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/songstats/refs/heads/main/json-schema/songstats-artist-schema.json
    contact:
      - FN: Songstats API Support
        email: api@songstats.com
        url: https://songstats.com/for/developers
common:
  - type: Portal
    url: https://songstats.com/for/developers
  - type: Documentation
    url: https://docs.songstats.com/
  - type: Website
    url: https://songstats.com/
  - type: GitHub
    url: https://github.com/Songstats
  - type: Blog
    url: https://lab.songstats.com/
  - type: SignUp
    url: https://songstats.com/for/developers
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
