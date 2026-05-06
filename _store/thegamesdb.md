---
aid: thegamesdb
name: TheGamesDB
description: An open, online database for video game fans providing game information, artwork, and metadata via API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Database
  - Gaming
  - Video Games
  - Metadata
  - Artwork
created: '2025-02-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/thegamesdb/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: thegamesdb:thegamesdb
    name: TheGamesDB API
    description: An open, online database for video game fans providing game information, artwork, and metadata via API. Search and retrieve game details, platform information, game artwork (boxart, screenshots, fanart), genres, developers, and publishers. Requires an API key.
    humanURL: https://api.thegamesdb.net/
    baseURL: https://api.thegamesdb.net
    tags:
      - Database
      - Gaming
      - Video Games
      - Metadata
      - Artwork
    properties:
      - type: Documentation
        url: https://api.thegamesdb.net/
      - type: OpenAPI
        url: openapi/thegamesdb-openapi.yml
      - type: Sign Up
        url: https://api.thegamesdb.net/key.php
      - type: JSONSchema
        url: json-schema/thegamesdb-game-schema.json
        title: Game Schema
      - type: JSONStructure
        url: json-structure/thegamesdb-game-structure.json
        title: Game Structure
      - type: JSON-LD
        url: json-ld/thegamesdb-context.jsonld
        title: TheGamesDB JSON-LD Context
common:
  - type: Website
    url: https://thegamesdb.net/
  - type: Documentation
    url: https://api.thegamesdb.net/
  - type: Sign Up
    url: https://api.thegamesdb.net/key.php
  - type: GitHub Organization
    url: https://github.com/TheGamesDB
  - type: SpectralRules
    url: rules/thegamesdb-spectral-rules.yml
    title: TheGamesDB Spectral Rules
  - type: Vocabulary
    url: vocabulary/thegamesdb-vocabulary.yml
    title: TheGamesDB Vocabulary
  - type: NaftikoCapability
    url: capabilities/video-game-discovery.yaml
    title: Video Game Discovery
  - type: RateLimits
    url: https://api.thegamesdb.net/key.php
    data:
      - name: Monthly Allowance
        description: 1000 queries per month (20 calls per query = 20,000 total calls)
  - type: Authentication
    url: https://api.thegamesdb.net/key.php
    data:
      - name: API Key Query Parameter
        description: API key passed as 'apikey' query parameter on all requests
  - type: Features
    data:
      - name: Game Search
        description: Search games by name with optional platform filtering
      - name: Game Details
        description: Retrieve complete game metadata by ID including overview, ratings, and system requirements
      - name: Platform Catalog
        description: Full catalog of all gaming platforms with hardware specifications and images
      - name: Game Artwork
        description: Boxart, screenshots, fanart, banners, and clearlogos for games and platforms
      - name: Game Updates
        description: Retrieve games updated since a given timestamp for database synchronization
      - name: Reference Data
        description: Complete lists of genres, developers, and publishers
      - name: Batch Requests
        description: Request multiple game or platform IDs in a single API call
  - type: UseCases
    data:
      - name: Gaming Applications
        description: Build game databases, libraries, and collection managers
      - name: Media Centers
        description: Power game scrapers for Emulation Station, Kodi, and similar media centers
      - name: Game Collections
        description: Manage personal or commercial video game collection databases
      - name: AI Game Assistant
        description: Power AI agents that answer questions about video games
  - type: Integrations
    data:
      - name: EmulationStation
        description: Popular retro gaming frontend using TheGamesDB for scraping
      - name: Skraper
        description: Game scraper tools using the API for artwork and metadata
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
