---
aid: product-hunt
name: Product Hunt
description: Product Hunt is a platform for discovering new tech products, connecting makers with early adopters and enthusiasts. Each day, Product Hunt surfaces the best new products in technology including apps, websites, hardware projects, and developer tools, allowing the community to vote, comment, and discuss. It is widely used by founders to launch products and by developers and tech enthusiasts to stay current with the latest innovations in the startup and tech product ecosystem.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Product Discovery
  - Startups
  - Tech Products
  - Maker Community
url: https://raw.githubusercontent.com/api-evangelist/product-hunt/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: product-hunt:product-hunt-api
    name: Product Hunt API
    description: The Product Hunt API provides programmatic access to Product Hunt's platform data via GraphQL. Developers can query and retrieve information about products, posts, topics, collections, users, votes, and comments. The API supports OAuth 2.0 authentication with three scopes (Public, Private, Write), client-only authentication for public data, and developer tokens for simple scripts. It allows applications to interact with the Product Hunt community, fetch daily product launches, explore trending tech products, and integrate Product Hunt data into third-party applications.
    humanURL: https://api.producthunt.com/v2/docs
    baseURL: https://api.producthunt.com/v2/api/graphql
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Product Discovery
      - Startups
      - Tech Products
    properties:
      - type: Documentation
        url: https://api.producthunt.com/v2/docs
      - type: APIReference
        url: https://api-v2-docs.producthunt.com
      - type: Authentication
        url: https://www.producthunt.com/v2/oauth/applications
      - type: GraphQLExplorer
        url: https://ph-graph-api-explorer.herokuapp.com/
      - type: GitHub
        url: https://github.com/producthunt/producthunt-api
      - type: RateLimits
        url: https://api.producthunt.com/v2/docs#section/Getting-Started/Rate-Limiting
      - type: Support
        url: mailto:hello@producthunt.com
commonProperties:
  - type: Website
    url: https://www.producthunt.com/
  - type: Documentation
    url: https://api.producthunt.com/v2/docs
  - type: SignUp
    url: https://www.producthunt.com/join
  - type: Login
    url: https://www.producthunt.com/login
  - type: Authentication
    url: https://www.producthunt.com/v2/oauth/applications
  - type: RateLimits
    url: https://api.producthunt.com/v2/docs#section/Getting-Started/Rate-Limiting
  - type: TermsOfService
    url: https://www.producthunt.com/terms-of-service
  - type: PrivacyPolicy
    url: https://www.producthunt.com/privacy
  - type: Forum
    url: https://www.producthunt.com/discussions
  - type: Blog
    url: https://blog.producthunt.com/
  - type: X
    url: https://x.com/producthunt
  - type: LinkedIn
    url: https://www.linkedin.com/company/producthunt
  - type: Facebook
    url: https://www.facebook.com/producthunt
  - type: GitHub
    url: https://github.com/producthunt
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
