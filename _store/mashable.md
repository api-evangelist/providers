---
aid: mashable
name: Mashable
description: Mashable is a digital media and entertainment company covering tech, culture, and digital trends. Founded in 2005, Mashable has grown into a global, multi-platform media and entertainment company. Mashable does not publish a first-party REST API, but its headlines and articles are accessible via the third-party News API REST service.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - Articles
  - Digital Culture
  - Headlines
  - Media
  - News
  - Technology News
url: https://raw.githubusercontent.com/api-evangelist/mashable/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mashable:mashable-via-newsapi
    name: Mashable via News API
    description: Mashable content is accessible via the News API, a third-party REST API that provides live headlines, articles, images, and metadata from Mashable and over 150,000 other worldwide news sources. Developers can search Mashable content using the source identifier "mashable" to retrieve top headlines and historical articles published by Mashable. The API returns structured JSON responses including article title, description, URL, image URL, publication date, and author. An API key is required to authenticate requests.
    humanURL: https://newsapi.org/s/mashable-api
    baseURL: https://newsapi.org/v2
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Articles
      - Headlines
      - News
    properties:
      - type: Documentation
        url: https://newsapi.org/s/mashable-api
      - type: GettingStarted
        url: https://newsapi.org/docs/get-started
      - type: Endpoints
        url: https://newsapi.org/docs/endpoints/top-headlines
      - type: Endpoints
        url: https://newsapi.org/docs/endpoints/everything
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/mashable/refs/heads/main/openapi/mashable-openapi.yml
common:
  - url: https://mashable.com/
    name: Mashable Website
    type: Website
  - url: https://mashable.com/about
    name: About Mashable
    type: About
  - url: https://mashable.com/advertise
    name: Advertise with Mashable
    type: Advertising
  - url: https://mashable.com/newsletter
    name: Mashable Newsletter
    type: Newsletter
  - url: https://newsapi.org/s/mashable-api
    name: Mashable API via News API
    type: Documentation
  - url: http://feeds.mashable.com/mashable
    name: Mashable RSS Feed
    type: RSS
  - url: https://mashable.com/privacy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://mashable.com/terms
    name: Terms of Service
    type: TermsOfService
  - url: https://twitter.com/mashable
    name: Mashable on X (Twitter)
    type: X
  - url: https://www.facebook.com/mashable/
    name: Mashable on Facebook
    type: Facebook
  - url: https://www.instagram.com/mashable/
    name: Mashable on Instagram
    type: Instagram
  - url: https://www.youtube.com/user/mashable
    name: Mashable on YouTube
    type: YouTube
  - url: https://www.linkedin.com/company/mashable
    name: Mashable on LinkedIn
    type: LinkedIn
  - url: https://github.com/mashable
    name: Mashable on GitHub
    type: GitHub
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
