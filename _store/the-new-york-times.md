---
aid: the-new-york-times
url: >-
  https://raw.githubusercontent.com/api-search/news/main/_apis/new-york-times/apis.md
apis:
  - aid: the-new-york-times:archive-api
    name: Archive API
    tags:
      - Archive
      - Months
      - Years
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com
    humanURL: https://developer.nytimes.com/docs/archive-product/1/overview
    properties:
      - url: https://developer.nytimes.com/docs/archive-product/1/overview
        type: Documentation
      - url: properties/new-york-times-archive-openapi-original.yml
        type: OpenAPI
    description: >-
      The Archive API returns an array of NYT articles for a given month, going
      back to 1851. Its response fields are the same as the Article Search API. 
  - aid: the-new-york-times:article-search-api
    name: Article Search API
    tags:
      - Articles
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com
    humanURL: https://developer.nytimes.com/docs/articlesearch-product/1/overview
    properties:
      - url: https://developer.nytimes.com/docs/articlesearch-product/1/overview
        type: Documentation
      - url: properties/new-york-times-article-search-openapi-original.yml
        type: OpenAPI
    description: >-
      Use the Article Search API to look up articles by keyword. You can refine
      your search using filters and facets.
  - aid: the-new-york-times:books-api
    name: Books API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.nytimes.com/docs/books-product/1/overview
    properties:
      - url: https://developer.nytimes.com/docs/books-product/1/overview
        type: Documentation
      - url: properties/new-york-times-books-openapi-original.yml
        type: OpenAPI
    description: >-
      The Books API provides information about book reviews and The New York
      Times Best Sellers lists.
  - aid: the-new-york-times:most-popular
    name: Most Popular
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com
    humanURL: https://developer.nytimes.com/docs/most-popular-product/1/overview
    properties:
      - url: https://developer.nytimes.com/docs/most-popular-product/1/overview
        type: Documentation
      - url: properties/new-york-times-most-popular-openapi-original.yml
        type: OpenAPI
    description: >-
      Provides services for getting the most popular articles on NYTimes.com
      based on emails, shares, or views.
  - aid: the-new-york-times:movie-reviews-api
    name: Movie Reviews API
    tags:
      - Bio
      - Critics
      - Images
      - Movie
      - Names
      - Reviewers
      - Reviews
      - Search
      - Search
      - Types
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: >-
      https://api.apis.guru/v2/specs/nytimes.com/movie_reviews/2.0.0/openapi.yaml
    humanURL: https://developer.nytimes.com/docs/movie-reviews-api/1/overview
    properties:
      - url: https://example.com/documentation
        type: Documentation
      - url: properties/new-york-times-movie-review-openapi-original.yml
        type: OpenAPI
    description: >-
      As an alternative, use the Article Search API to get New York Times movie
      reviews using the following filter query.
  - aid: the-new-york-times:semantic-api
    name: Semantic API
    tags:
      - Concepts
      - Names
      - Search
      - Specific
      - Types
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.nytimes.com/docs/semantic-api-product/1/overview
    properties:
      - url: https://developer.nytimes.com/docs/semantic-api-product/1/overview
        type: Documentation
      - url: properties/new-york-times-semantic-openapi-original.yml
        type: OpenAPI
    description: >-
      The Semantic API complements the Articles API. With the Semantic API, you
      get access to the long list of people, places, organizations and other
      locations, entities and descriptors that make up the controlled vocabulary
      used as metadata by The New York Times.
  - aid: the-new-york-times:timestags-api
    name: TimesTags API
    tags:
      - Tags
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.nytimes.com/docs/timestags-product/1/overview
    properties:
      - url: https://developer.nytimes.com/docs/timestags-product/1/overview
        type: Documentation
      - url: properties/new-york-times-times-tags-openapi-original.yml
        type: OpenAPI
    description: >-
      With the TimesTags API, you can mine the riches of the New York Times tag
      set. The TimesTags service matches your query to the controlled
      vocabularies that fuel NYTimes.com metadata. 
  - aid: the-new-york-times:times-newswire-api
    name: Times Newswire API
    tags:
      - Content
      - Sections
      - Sources
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.nytimes.com/docs/timeswire-product/1/overview
    properties:
      - url: https://developer.nytimes.com/docs/timeswire-product/1/overview
        type: Documentation
      - url: properties/new-york-times-times-newswire-openapi-original.yml
        type: OpenAPI
    description: >-
      With the Times Newswire API, you can get links and metadata for Times'
      articles as soon as they are published on NYTimes.com. The Times Newswire
      API provides an up-to-the-minute stream of published articles. 
  - aid: the-new-york-times:top-stories
    name: Top Stories
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.nytimes.com/docs/top-stories-product/1/overview
    properties:
      - url: https://developer.nytimes.com/docs/top-stories-product/1/overview
        type: Documentation
      - url: properties/new-york-times-top-stories-openapi-original.ymll
        type: OpenAPI
    description: >-
      The Top Stories API returns an array of articles currently on the
      specified section (arts, business, ...).
name: The New York Times
tags:
  - News
  - Articles
  - Books
  - Movies
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://developer.nytimes.com/get-started
    type: Getting Started
  - url: https://developer.nytimes.com/accounts/create
    type: Signup
  - url: https://developer.nytimes.com/accounts/login
    type: Login
  - url: https://developer.nytimes.com/terms
    type: TermsOfService
created: '2023-10-06T00:00:00.000Z'
modified: '2024-12-21'
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
description: >-
  The official developer area for accessing The New York Times archive, article
  search, books, most popular, reviews, semantic, times tags, times wire, and
  top stories APis.
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---