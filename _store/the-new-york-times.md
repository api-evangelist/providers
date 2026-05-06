---
aid: the-new-york-times
url: https://raw.githubusercontent.com/api-evangelist/the-new-york-times/refs/heads/main/apis.yml
name: The New York Times
description: The New York Times is one of the world's most respected news organizations, providing comprehensive journalism across politics, culture, business, science, health, and the arts since 1851. The NYT Developer Network exposes a suite of RESTful APIs enabling developers to search and access NYT articles, best-seller book lists, movie reviews, semantic metadata, top stories, and popular content. All APIs require an API key obtained from the NYT Developer Portal.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - Articles
  - Books
  - Movies
  - News
  - Media
  - Publishing
  - Journalism
created: '2023-10-06T00:00:00.000Z'
modified: '2026-05-03'
position: Consuming
specificationVersion: '0.19'
apis:
  - aid: the-new-york-times:archive-api
    name: The New York Times Archive API
    description: The Archive API returns an array of NYT articles for a given month, going back to 1851. Its response fields are the same as the Article Search API. Use it to build your own local database of NYT article metadata.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/archive/v1
    humanURL: https://developer.nytimes.com/docs/archive-product/1/overview
    tags:
      - Archive
      - Articles
      - Months
      - Years
      - History
    properties:
      - url: https://developer.nytimes.com/docs/archive-product/1/overview
        type: Documentation
      - url: openapi/new-york-times-archive-openapi-original.yml
        type: OpenAPI
  - aid: the-new-york-times:article-search-api
    name: The New York Times Article Search API
    description: Use the Article Search API to look up articles by keyword. You can refine your search using filters and facets. The API searches NYT articles from September 18, 1851 to today, retrieving headlines, abstracts, lead paragraphs, links to associated multimedia and other article metadata.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/search/v2
    humanURL: https://developer.nytimes.com/docs/articlesearch-product/1/overview
    tags:
      - Articles
      - Search
      - Keywords
      - Facets
    properties:
      - url: https://developer.nytimes.com/docs/articlesearch-product/1/overview
        type: Documentation
      - url: openapi/new-york-times-article-search-openapi-original.yml
        type: OpenAPI
  - aid: the-new-york-times:books-api
    name: The New York Times Books API
    description: The Books API provides information about book reviews and The New York Times Best Sellers lists. Access current and historical bestseller lists, book details, and NYT critic reviews.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/books/v3
    humanURL: https://developer.nytimes.com/docs/books-product/1/overview
    tags:
      - Books
      - Best Sellers
      - Reviews
      - Lists
    properties:
      - url: https://developer.nytimes.com/docs/books-product/1/overview
        type: Documentation
      - url: openapi/new-york-times-books-openapi-original.yml
        type: OpenAPI
  - aid: the-new-york-times:most-popular
    name: The New York Times Most Popular API
    description: The Most Popular API provides services for getting the most popular articles on NYTimes.com based on emails, shares, or views. Retrieve the most emailed, shared, and viewed articles by section and time period.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/mostpopular/v2
    humanURL: https://developer.nytimes.com/docs/most-popular-product/1/overview
    tags:
      - Articles
      - Popular
      - Social Sharing
      - Trending
    properties:
      - url: https://developer.nytimes.com/docs/most-popular-product/1/overview
        type: Documentation
      - url: openapi/new-york-times-most-popular-openapi-original.yml
        type: OpenAPI
  - aid: the-new-york-times:movie-reviews-api
    name: The New York Times Movie Reviews API
    description: Search for NYT movie reviews by keyword and get lists of NYT Critics' Picks. As an alternative, use the Article Search API with appropriate filter queries to access movie review content.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/movies/v2
    humanURL: https://developer.nytimes.com/docs/movie-reviews-api/1/overview
    tags:
      - Movies
      - Reviews
      - Critics
      - Film
    properties:
      - url: https://developer.nytimes.com/docs/movie-reviews-api/1/overview
        type: Documentation
      - url: openapi/new-york-times-movie-review-openapi-original.yml
        type: OpenAPI
  - aid: the-new-york-times:semantic-api
    name: The New York Times Semantic API
    description: The Semantic API complements the Articles API. With the Semantic API, you get access to the long list of people, places, organizations and other locations, entities and descriptors that make up the controlled vocabulary used as metadata by The New York Times.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/semantic/v2
    humanURL: https://developer.nytimes.com/docs/semantic-api-product/1/overview
    tags:
      - Concepts
      - Semantics
      - Metadata
      - Entities
      - People
      - Organizations
    properties:
      - url: https://developer.nytimes.com/docs/semantic-api-product/1/overview
        type: Documentation
      - url: openapi/new-york-times-semantic-openapi-original.yml
        type: OpenAPI
  - aid: the-new-york-times:timestags-api
    name: The New York Times TimesTags API
    description: With the TimesTags API, you can mine the riches of the New York Times tag set. The TimesTags service matches your query to the controlled vocabularies that fuel NYTimes.com metadata. Note this API is deprecated; equivalent functionality is available through the Semantic API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/suggest/v1
    humanURL: https://developer.nytimes.com/docs/timestags-product/1/overview
    tags:
      - Tags
      - Autocomplete
      - Metadata
      - Search
    properties:
      - url: https://developer.nytimes.com/docs/timestags-product/1/overview
        type: Documentation
      - url: openapi/new-york-times-times-tags-openapi-original.yml
        type: OpenAPI
  - aid: the-new-york-times:times-newswire-api
    name: The New York Times Times Newswire API
    description: With the Times Newswire API, you can get links and metadata for Times articles as soon as they are published on NYTimes.com. The Times Newswire API provides an up-to-the-minute stream of published articles by section and source.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/news/v3
    humanURL: https://developer.nytimes.com/docs/timeswire-product/1/overview
    tags:
      - News
      - Wire
      - Streaming
      - Articles
      - Sections
    properties:
      - url: https://developer.nytimes.com/docs/timeswire-product/1/overview
        type: Documentation
      - url: openapi/new-york-times-times-newswire-openapi-original.yml
        type: OpenAPI
  - aid: the-new-york-times:top-stories
    name: The New York Times Top Stories API
    description: The Top Stories API returns an array of articles currently on the specified section (arts, business, health, home, etc.) of NYTimes.com. Use the home section to get articles currently on the homepage.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nytimes.com/svc/topstories/v2
    humanURL: https://developer.nytimes.com/docs/top-stories-product/1/overview
    tags:
      - Articles
      - Top Stories
      - Sections
      - News
    properties:
      - url: https://developer.nytimes.com/docs/top-stories-product/1/overview
        type: Documentation
      - url: openapi/new-york-times-top-stories-openapi-original.yml
        type: OpenAPI
common:
  - url: https://developer.nytimes.com/
    type: Portal
  - url: https://developer.nytimes.com/get-started
    type: Getting Started
  - url: https://developer.nytimes.com/accounts/create
    type: Signup
  - url: https://developer.nytimes.com/accounts/login
    type: Login
  - url: https://developer.nytimes.com/terms
    type: TermsOfService
  - url: https://developer.nytimes.com/faq
    type: FAQ
  - url: https://github.com/nytimes
    type: GitHub
  - url: https://nytimes.com
    type: Website
  - url: https://github.com/nytimes/public_api_specs
    type: OpenAPI
  - url: https://github.com/nytimes/times_wire
    name: Times Wire Ruby Client
    type: SDK
  - url: https://github.com/nytimes/nytcampfin
    name: Campaign Finance Python Client
    type: SDK
  - url: rules/new-york-times-rules.yml
    type: SpectralRuleset
  - url: capabilities/article-research.yaml
    type: NaftikoCapability
  - url: capabilities/content-discovery.yaml
    type: NaftikoCapability
  - url: capabilities/metadata-enrichment.yaml
    type: NaftikoCapability
  - url: json-schema/new-york-times-article-schema.json
    type: JSONSchema
  - url: json-schema/new-york-times-book-schema.json
    type: JSONSchema
  - url: json-ld/the-new-york-times-context.jsonld
    type: JSONLDContext
  - url: vocabulary/the-new-york-times-vocabulary.yml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
