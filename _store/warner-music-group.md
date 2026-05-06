---
aid: warner-music-group
url: https://raw.githubusercontent.com/api-evangelist/warner-music-group/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
name: Warner Music Group
tags:
  - Music
  - Entertainment
  - Streaming
  - Licensing
  - Publishing
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
description: Warner Music Group is one of the major record labels in the music industry, with recorded music and music publishing operations spanning a roster of artists, songwriters, and labels around the world. WMG includes Warner Records, Atlantic Records, Elektra Records, and Warner Chappell Music (one of the world's largest music publishing companies). WMG provides music licensing APIs and developer tools for integrating licensed music into applications.
apis:
  - aid: warner-music-group:wmg-licensing-api
    name: Warner Music Group Licensing API
    tags:
      - Music Licensing
      - Sync Licensing
      - Content Rights
      - Publishing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.wmg.com
    humanURL: https://www.wmgmusiclicensing.com/
    properties:
      - url: https://www.wmgmusiclicensing.com/
        type: Documentation
      - url: openapi/warner-music-group-licensing-openapi.yml
        type: OpenAPI
      - url: rules/warner-music-group-rules.yml
        type: SpectralRules
      - url: capabilities/music-licensing.yaml
        type: NaftikoCapabilities
      - url: json-schema/warner-music-group-license-schema.json
        type: JSONSchema
      - url: json-ld/warner-music-group-context.jsonld
        type: JSONLDContext
      - url: vocabulary/warner-music-group-vocabulary.yml
        type: Vocabulary
    description: The Warner Music Group Licensing API enables content creators and developers to request synchronization licenses, mechanical licenses, and other music rights for WMG's catalog of recordings and compositions. The API covers tracks from Warner Records, Atlantic Records, Elektra, and Warner Chappell Music publishing.
common:
  - url: https://www.wmg.com/
    name: Warner Music Group
    type: Website
  - url: https://www.wmgmusiclicensing.com/
    name: WMG Music Licensing Portal
    type: Portal
  - url: https://warnerchappell.com/
    name: Warner Chappell Music
    type: Website
  - url: https://warnerchappell.com/music-licensing
    name: Warner Chappell Music Licensing
    type: Documentation
  - url: https://www.warnerchappellpm.com/
    name: Warner Chappell Production Music
    type: Website
  - url: https://developer.wmg.com/
    name: WMG Developer Portal
    type: Portal
  - url: https://github.com/wmg
    name: WMG GitHub Organization
    type: GitHubOrganization
labels:
  - Warner Records
  - Atlantic Records
  - Elektra Records
  - Reprise Records
  - Parlophone
  - Sire Records
publishers:
  - Warner Chappell Music
  - Warner Chappell Production Music
features:
  - Sync Licensing (film, TV, advertising, gaming)
  - Mechanical Licensing
  - Digital Licensing (streaming, download)
  - Production Music Library
  - Artist and Release Catalog Search
  - License Status Tracking
useCases:
  - License music for film and television productions
  - Clear music rights for advertising and brand campaigns
  - Integrate licensed music into apps and digital products
  - Access production music for video content creation
  - Discover and license music from major artists
integrations:
  - Adaptr (music licensing SDK)
  - Feed Media Group
  - Spotify (content delivery)
  - Apple Music (content delivery)
  - YouTube Content ID
solutions:
  - Music Licensing
  - Sync Licensing
  - Music Publishing
  - Artist Management Data
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
