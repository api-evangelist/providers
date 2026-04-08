---
aid: ghost
url: https://raw.githubusercontent.com/api-evangelist/ghost/refs/heads/main/apis.yml
apis:
- aid: ghost:content-api
  name: Ghost Content API
  tags:
  - Authors
  - Content Management
  - Headless CMS
  - Pages
  - Posts
  - Publishing
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://ghost.org/docs/content-api/
  properties:
  - url: https://ghost.org/docs/content-api/
    type: Documentation
  - url: openapi/ghost-content-api-openapi.yml
    type: OpenAPI
  description: The Ghost Content API is a RESTful, read-only API that delivers published content from a Ghost site to any client. It provides access to posts, pages, tags, authors, tiers, and settings resources. Access is controlled via a Content API key, and all responses are returned in JSON format.
- aid: ghost:admin-api
  name: Ghost Admin API
  tags:
  - Administration
  - Content Management
  - Members
  - Newsletters
  - Offers
  - Publishing
  - Tiers
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://ghost.org/docs/admin-api/
  properties:
  - url: https://ghost.org/docs/admin-api/
    type: Documentation
  - url: openapi/ghost-admin-api-openapi.yml
    type: OpenAPI
  description: The Ghost Admin API provides full read and write access to all content and configuration within a Ghost publication. It enables developers to create, update, and delete posts, pages, tags, members, tiers, newsletters, and offers programmatically. Authentication is handled via JSON Web Tokens generated from an Admin API key, integration tokens, or staff access tokens.
- aid: ghost:webhooks
  name: Ghost Webhooks
  tags:
  - Automation
  - Events
  - Integrations
  - Notifications
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://ghost.org/docs/webhooks/
  properties:
  - url: https://ghost.org/docs/webhooks/
    type: Documentation
  - url: asyncapi/ghost-webhooks-asyncapi.yml
    type: AsyncAPI
  description: Ghost Webhooks allow developers to receive real-time HTTP notifications when specific events occur within a Ghost publication, such as publishing a new post, updating a page, or gaining a new member. Webhooks can be configured through the Ghost Admin interface under custom integrations or created programmatically via the Admin API.
- aid: ghost:content-api-javascript-client
  name: Ghost Content API JavaScript Client
  tags:
  - Client Library
  - Content Management
  - JavaScript
  - Node.js
  - SDK
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://ghost.org/docs/content-api/javascript/
  properties:
  - url: https://ghost.org/docs/content-api/javascript/
    type: Documentation
  description: The Ghost Content API JavaScript Client is an official promise-based JavaScript library published as @tryghost/content-api on npm. It abstracts the complexity of authenticating and interacting with the Ghost Content API, providing a clean interface for fetching posts, pages, tags, authors, and settings. The library works in both client-side and server-side JavaScript environments and supports the full NQL filtering syntax.
- aid: ghost:themes-api
  name: Ghost Themes API
  tags:
  - Customization
  - Frontend
  - Handlebars
  - Templates
  - Themes
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://ghost.org/docs/themes/
  properties:
  - url: https://ghost.org/docs/themes/
    type: Documentation
  description: The Ghost Themes API provides a Handlebars-based templating system for building custom front-end themes for Ghost publications. It includes a comprehensive set of helpers including data helpers for fetching content, functional helpers for logic and formatting, and utility helpers for common tasks. Themes have access to all Ghost content through template variables and the get helper, which queries the Content API internally.
name: Ghost
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Ghost is an open-source publishing platform designed for professional publishers, with native subscription, membership, and newsletter features for content creators.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

