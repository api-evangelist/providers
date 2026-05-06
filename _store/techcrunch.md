---
aid: techcrunch
name: TechCrunch
description: TechCrunch (https://techcrunch.com/) is a leading technology media property dedicated to covering startups, venture capital, and innovation. Founded in 2005 and acquired by AOL in 2010 and later by Yahoo, TechCrunch delivers breaking news, in-depth analysis, and original reporting on the technology industry, emerging companies, funding rounds, and the people shaping the future of tech. The publication hosts flagship events including TechCrunch Disrupt and the Startup Battlefield competition. TechCrunch runs on WordPress and exposes the standard WordPress REST API for programmatic content access.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Media
  - News
  - Startups
  - Technology News
  - Venture Capital
url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: techcrunch:wordpress-rest-api
    name: TechCrunch WordPress REST API
    description: TechCrunch is built on WordPress and exposes the standard WordPress REST API, providing JSON endpoints for accessing posts, pages, categories, tags, authors, media, comments, and search. The API is available at the /wp-json/wp/v2/ base path and supports filtering, pagination, searching, and sorting across all TechCrunch content. TechCrunch uses a headless WordPress architecture with a React frontend, making the REST API the primary data layer for content delivery. No authentication is required for read operations.
    humanURL: https://developer.wordpress.org/rest-api/
    baseURL: https://techcrunch.com/wp-json/wp/v2
    tags:
      - Content
      - JSON
      - Media
      - REST
      - WordPress
    properties:
      - type: Documentation
        url: https://developer.wordpress.org/rest-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/openapi/techcrunch-wordpress-rest-api-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/json-schema/techcrunch-post-schema.json
      - type: NaftikoPCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/capabilities/content-discovery.yaml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/rules/techcrunch-wordpress-rules.yml
  - aid: techcrunch:rss-feed
    name: TechCrunch RSS Feed
    description: TechCrunch provides RSS feeds covering its full range of technology news, startup coverage, and venture capital reporting. The main feed delivers all published articles, and category-specific feeds are available for topics including startups, venture capital, artificial intelligence, security, apps, gadgets, and more. These standard RSS/Atom feeds allow readers and developers to consume TechCrunch content programmatically using any standard feed reader or parsing library.
    humanURL: https://techcrunch.com/feed/
    baseURL: https://techcrunch.com
    tags:
      - Feed
      - News
      - RSS
      - Syndication
    properties:
      - type: Documentation
        url: https://techcrunch.com/feed/
      - type: RSSFeed
        url: https://techcrunch.com/feed/
common:
  - url: https://techcrunch.com/
    name: TechCrunch
    type: Website
  - url: https://techcrunch.com/about-techcrunch/
    name: About TechCrunch
    type: About
  - url: https://techcrunch.com/newsletters/
    name: TechCrunch Newsletters
    type: Newsletter
  - url: https://techcrunch.com/feed/
    name: TechCrunch RSS Feed
    type: RSSFeeds
  - url: https://techcrunch.com/advertise/
    name: Advertise with TechCrunch
    type: Advertising
  - url: https://techcrunch.com/contact-us/
    name: Contact TechCrunch
    type: Contact
  - url: https://techcrunch.com/terms-of-service/
    name: Terms of Service
    type: TermsOfService
  - url: https://techcrunch.com/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://x.com/TechCrunch
    name: TechCrunch on X
    type: X
  - url: https://www.linkedin.com/company/techcrunch/
    name: TechCrunch on LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/techcrunch/
    name: TechCrunch on Facebook
    type: Facebook
  - url: https://www.instagram.com/techcrunch/
    name: TechCrunch on Instagram
    type: Instagram
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/vocabulary/techcrunch-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/json-ld/techcrunch-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
