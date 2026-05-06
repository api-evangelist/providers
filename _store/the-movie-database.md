---
aid: the-movie-database
name: The Movie Database
description: Welcome to version 3 of The Movie Database (TMDB) API. This is where you will find the definitive list of currently available methods for our movie, tv, actor and image API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Entertainment
  - Movies
  - Television
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/the-movie-database/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: the-movie-database:the-movie-database
    name: The Movie Database API
    description: The Movie Database (TMDB) API v3 provides comprehensive access to movie, TV show, person, and image data. Discover movies and series by genre, rating, and release date. Search across all content types. Retrieve cast and crew credits, external IDs, keywords, reviews, recommendations, similar titles, trailers, and watch providers. Manage user accounts with ratings, watchlists, and favorites. Supports multiple languages and regions. 148 endpoints covering movies, TV series, seasons, episodes, people, collections, companies, networks, keywords, and more.
    humanURL: https://developer.themoviedb.org
    baseURL: https://api.themoviedb.org/3
    tags:
      - Entertainment
      - Movies
      - People
      - Television
      - Streaming
    properties:
      - type: Documentation
        url: https://developer.themoviedb.org/docs/getting-started
      - type: Reference
        url: https://developer.themoviedb.org/reference/getting-started
      - type: GettingStarted
        url: https://developer.themoviedb.org/docs/getting-started
      - type: Authentication
        url: https://developer.themoviedb.org/docs/authentication-application
      - type: OpenAPI
        url: https://developer.themoviedb.org/openapi/tmdb-api.json
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/the-movie-database/refs/heads/main/openapi/the-movie-database-openapi.json
    features:
      - Movie Search and Discovery
      - TV Series Search and Discovery
      - Person and Actor Profiles
      - Cast and Crew Credits
      - Movie and TV Recommendations
      - Similar Titles
      - Trending Content
      - Watch Providers by Region
      - User Ratings
      - Watchlists and Favorites
      - Image and Video Assets
      - Multi-Language Support
      - External ID Mapping (IMDb, TVDB, Wikidata)
      - Content Change Tracking
      - Genre and Keyword Filtering
    useCases:
      - Entertainment Recommendation Apps
      - Streaming Service Aggregators
      - Movie and TV Show Trackers
      - Media Library Management
      - Content Discovery Platforms
      - Review and Rating Apps
      - Watch Provider Comparison
    integrations:
      - url: https://developer.themoviedb.org/docs/wrappers-and-libraries
        name: Official Wrappers and Libraries
        type: SDK
common:
  - type: Website
    url: https://www.themoviedb.org/
  - type: Documentation
    url: https://developer.themoviedb.org/docs/getting-started
  - type: Sign Up
    url: https://www.themoviedb.org/signup
  - type: Login
    url: https://www.themoviedb.org/login
  - type: Support
    url: https://www.themoviedb.org/talk/category/5047951f760ee3318900009d
  - type: OpenAPI
    url: https://developer.themoviedb.org/openapi/tmdb-api.json
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/the-movie-database/refs/heads/main/openapi/the-movie-database-openapi.json
  - type: Pricing
    url: https://www.themoviedb.org/api-terms-of-use
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
