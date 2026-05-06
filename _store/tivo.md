---
aid: tivo
name: Tivo
description: TiVo provides a universe of high-quality entertainment imagery and information through its metadata APIs. The company offers Video Metadata API and Music Metadata API delivering TV, movie, and music content data for streaming platforms, smart TVs, IPTV systems, and entertainment applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Entertainment
  - Metadata
  - Television
  - Movies
  - Music
  - Streaming
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tivo:tivo-video-metadata
    name: TiVo Video Metadata API
    description: The TiVo Video Metadata API v3 provides access to high-quality entertainment imagery and information for TV shows, movies, and episodes. Supports content search by metadata fields and precise ID-based lookup using Rovi 1.1, Rovi 2.0, TMDB, and EIDR identifiers. Returns JSON responses for reliable, scalable entertainment experiences.
    humanURL: https://business.tivo.com/products-solutions/metadata/tv-movie-metadata-api
    baseURL: https://data.tivo.com
    tags:
      - Entertainment
      - Metadata
      - Television
      - Movies
      - Streaming
    properties:
      - type: Documentation
        url: https://tivo.stoplight.io/docs/video-metadata-api-v3/ZG9jOjQ3NjAxNTk-introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/openapi/tivo-video-metadata-openapi.yml
      - type: Developer Portal
        url: https://developers.tivo.com/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/json-schema/tivo-content-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/json-structure/tivo-content-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/json-ld/tivo-context.jsonld
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/rules/tivo-rules.yml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/capabilities/entertainment-metadata.yaml
  - aid: tivo:tivo-music-metadata
    name: TiVo Music Metadata API
    description: The TiVo Music Metadata API provides access to high-quality music information including artist details, album data, track information, and music imagery. Uses the same HTTP-based query structure and JSON response format as the Video Metadata API v3.
    humanURL: https://tivo.stoplight.io/docs/music-metadata-api/ZG9jOjQ3NjAxNTk-introduction
    tags:
      - Music
      - Metadata
      - Entertainment
    properties:
      - type: Documentation
        url: https://tivo.stoplight.io/docs/music-metadata-api/ZG9jOjQ3NjAxNTk-introduction
      - type: Developer Portal
        url: https://developers.tivo.com/metadata/
features:
  - Content search by multiple metadata fields
  - ID-based lookup for precise content retrieval
  - Support for Rovi 1.1, Rovi 2.0, TMDB, and EIDR identifiers
  - High-quality entertainment imagery
  - TV series season and episode data
  - Cast and crew information
  - Movie and TV show metadata
  - Music artist, album, and track data
  - Multi-language metadata support
  - FTP delivery option for bulk data
useCases:
  - Smart TV content discovery
  - Streaming platform content enrichment
  - IPTV guide data
  - Entertainment recommendation engines
  - Content catalog management
  - EPG (Electronic Program Guide) population
  - Music service metadata enrichment
integrations:
  - Smart TV platforms
  - DTS AutoStage automotive platform
  - IPTV platforms
  - Streaming services
solutions:
  - Entertainment metadata platform
  - Content experience enrichment
  - Smart TV application development
  - Automotive in-car entertainment
common:
  - type: Website
    url: https://business.tivo.com/
  - type: Documentation
    url: https://business.tivo.com/products-solutions/metadata/tv-movie-metadata-api
  - type: Developer Portal
    url: https://developers.tivo.com/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/openapi/tivo-video-metadata-openapi.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/json-ld/tivo-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/vocabulary/tivo-vocabulary.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/rules/tivo-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/capabilities/entertainment-metadata.yaml
  - type: GitHub Organization
    url: https://github.com/tivo
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
