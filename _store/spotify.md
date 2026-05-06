---
aid: spotify
name: Spotify
description: Spotify is the world's leading music streaming platform with 600M+ users and 100M+ tracks. The Spotify Web API enables developers to discover music and podcasts, manage Spotify libraries, control audio playback, access audio analysis, and build personalized music experiences. Authentication uses OAuth 2.0 with scopes for user-authorized access. The API underwent significant changes in February 2026 with new generic library endpoints and streamlined playlist management.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Music
  - Audio
  - Streaming
  - Podcasts
  - Playlists
created: '2023-11-15'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/spotify/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: spotify:spotify-web-api
    name: Spotify Web API
    description: The Spotify Web API provides RESTful access to Spotify's music and podcast catalog, user library management, playback control, and personalization features. Developers can retrieve metadata for albums, artists, tracks, shows, and episodes; manage user playlists and saved libraries; control playback on connected devices; and access audio analysis and recommendations. OAuth 2.0 authentication supports Authorization Code Flow, PKCE, and Client Credentials flows.
    humanURL: https://developer.spotify.com/documentation/web-api
    baseURL: https://api.spotify.com/v1
    tags:
      - Albums
      - Artists
      - Tracks
      - Playlists
      - Player
      - Search
      - Podcasts
      - Library
      - Recommendations
      - Audio Analysis
    properties:
      - type: Documentation
        url: https://developer.spotify.com/documentation/web-api
      - type: OpenAPI
        url: openapi/spotify-openapi-original.yml
      - type: Getting Started
        url: https://developer.spotify.com/documentation/web-api/tutorials/getting-started
      - type: Authorization
        url: https://developer.spotify.com/documentation/web-api/concepts/authorization
      - type: Rate Limits
        url: https://developer.spotify.com/documentation/web-api/concepts/rate-limits
      - type: Scopes
        url: https://developer.spotify.com/documentation/web-api/concepts/scopes
      - type: JSONSchema
        url: json-schema/spotify-track-schema.json
      - type: JSONSchema
        url: json-schema/spotify-playlist-schema.json
      - type: JSONStructure
        url: json-structure/spotify-track-structure.json
      - type: JSONLD
        url: json-ld/spotify-context.jsonld
      - type: SpectralRules
        url: rules/spotify-rules.yml
      - type: Capabilities
        url: capabilities/music-discovery.yaml
      - type: Vocabulary
        url: vocabulary/spotify-vocabulary.yml
    features:
      - type: MusicCatalog
        description: Search and retrieve metadata for 100M+ tracks, albums, and artists
      - type: PlaybackControl
        description: Control Spotify playback on any connected device via API
      - type: LibraryManagement
        description: Save, remove, and manage user's music library with generic URI-based endpoints
      - type: PlaylistManagement
        description: Create, update, and manage playlists; add, reorder, and remove items
      - type: AudioAnalysis
        description: Access beat-by-beat audio analysis including tempo, key, and energy
      - type: Recommendations
        description: Generate personalized track recommendations based on seeds and audio features
      - type: Personalization
        description: Access user's top artists and tracks over multiple time ranges
      - type: PodcastsAudiobooks
        description: Stream and manage shows, episodes, and audiobooks
    useCases:
      - type: MusicDiscovery
        description: Build recommendation engines and music discovery experiences
      - type: PlaylistBuilding
        description: Create collaborative or AI-generated playlists
      - type: PartyMode
        description: Control music playback at events, restaurants, or shared spaces
      - type: MusicAnalytics
        description: Analyze listening patterns and audio characteristics
      - type: DeviceControl
        description: Remote control Spotify playback from companion apps
common:
  - url: https://developer.spotify.com/
    type: Developer
  - url: https://developer.spotify.com/documentation/web-api/tutorials/getting-started
    type: Getting Started
  - url: https://developer.spotify.com/documentation/web-api/concepts/authorization
    type: Authorization
  - url: https://developer.spotify.com/documentation/web-api/concepts/rate-limits
    type: Rate Limits
  - url: https://developer.spotify.com/documentation/web-api/concepts/scopes
    type: Scopes
  - url: https://developer.spotify.com/community
    type: Community
  - url: https://developer.spotify.com/documentation/embeds
    type: Embeds
  - url: https://developer.spotify.com/terms
    type: Terms of Service
  - url: https://accounts.spotify.com/en/login
    type: Login
  - url: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
    type: Forum
  - url: https://developer.spotify.com/documentation/web-api/references/changes/february-2026
    type: Changelog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
