---
aid: common-sense-media
url: https://raw.githubusercontent.com/api-evangelist/common-sense-media/refs/heads/main/apis.yml
name: Common Sense Media
tags:
  - Apps
  - Books
  - Media
  - Movies
  - Non-Profit
  - Podcasts
  - Ratings
  - Reviews
  - Television
  - Video Games
  - YouTube
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2025-03-01'
modified: '2026-04-26'
position: Consumer
description: Common Sense Media is a nonprofit organization providing independent, age-rated reviews and ratings of movies, TV shows, books, video games, apps, podcasts, websites, and YouTube channels. The Common Sense Media Reviews API (v3) exposes this catalog via a partner-keyed REST surface hosted at api.commonsense.org/api/v3, with the partnership granted through Common Sense's Business Partner Program. The API is used by parenting apps, smart-TV guides, education platforms, and family- discovery products to surface age-appropriate guidance and the Common Sense Selection award.
apis:
  - aid: common-sense-media:common-sense-media-reviews-api
    name: Common Sense Media Reviews API
    tags:
      - Apps
      - Books
      - Media
      - Movies
      - Ratings
      - Reviews
      - Television
      - Video Games
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.commonsense.org/api/v3
    humanURL: https://www.commonsensemedia.org/developers
    properties:
      - url: https://www.commonsensemedia.org/developers/api-overview
        type: Documentation
      - url: https://www.commonsensemedia.org/developers/api/v3
        type: APIv3Overview
      - url: https://api.commonsense.org/docs/v3/
        type: SwaggerUI
      - url: https://www.commonsensemedia.org/developers/api/implementation
        type: ImplementationGuide
      - url: openapi/common-sense-media-reviews-api-openapi.yml
        type: OpenAPI
    description: JSON REST API exposing Common Sense Media's reviews and ratings catalog. Each review includes recommended age, age-rating group (littleKids/kids/tweens/teens), star rating, content grid (educational, message, role-model, diversity, violence, sex, language, consumerism, drugs), parents-need-to-know guidance, talking points, and product metadata. Clients filter by media type, age range, star range, character strengths, topics, genres, and the Common Sense Selection award. Authentication uses a partner-issued x-api-key header. The API is GET-only, HTTPS-only, rate-limited to 100 unique requests per minute, and content is refreshed at most hourly.
    x-features:
      - x-api-key header authentication
      - GET-only, HTTPS-only access
      - Filter by mediaType (app, book, game, movie, podcast, tv, website, youtube)
      - Age-range and star-range deepObject filters
      - Filter by character strengths, topics, genres
      - Common Sense Selection award filter (csmAward=true)
      - Vocabulary lookup endpoint for filterable fields
      - English and Spanish (en, es) language responses
      - Rate limited to 100 unique requests per minute
    x-use-cases:
      - Embedding age-rated reviews in parenting and family apps
      - Powering smart-TV guides with content advisories
      - Driving content discovery in education platforms
      - Surfacing Common Sense Selection award lists
      - Filtering streaming or library catalogs by recommended age
common:
  - type: Website
    url: https://www.commonsensemedia.org/
  - type: DeveloperCenter
    url: https://www.commonsensemedia.org/developers
  - type: APIOverview
    url: https://www.commonsensemedia.org/developers/api-overview
  - type: APIv3
    url: https://www.commonsensemedia.org/developers/api/v3
  - type: SwaggerUI
    url: https://api.commonsense.org/docs/v3/
  - type: ImplementationGuide
    url: https://www.commonsensemedia.org/developers/api/implementation
  - type: PartnerProgramContact
    url: https://commonsense.my.site.com/membersupport/s/contactsupport
  - type: PrivacyPolicy
    url: https://www.commonsensemedia.org/privacy-policy
  - url: json-ld/common-sense-media-context.jsonld
    type: JSON-LD
  - url: json-schema/common-sense-media-review-schema.json
    type: JSONSchema
  - url: rules/common-sense-media-rules.yml
    type: Spectral
  - url: capabilities/common-sense-media-reviews-capabilities.yml
    type: NaftikoCapabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
