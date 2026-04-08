---
aid: fumadocs
url: https://raw.githubusercontent.com/api-evangelist/fumadocs/refs/heads/main/apis.yml
apis:
- aid: fumadocs:fumadocs
  name: Fumadocs
  tags:
  - Documentation
  - Framework
  - Next.js
  humanURL: https://fumadocs.dev
  properties:
  - url: https://fumadocs.dev/docs
    type: Documentation
  - url: https://github.com/fuma-nama/fumadocs
    type: GitHub
  description: Fumadocs is an open-source documentation framework built on Next.js and React for creating fast, modern developer documentation sites. It provides a full stack of composable packages including fumadocs-core for source loading, page tree generation, and search; fumadocs-ui for pre-built accessible React components, themes, and layouts; fumadocs-openapi for generating interactive API reference pages from OpenAPI specifications with a built-in playground; and a CLI for scaffolding new projects.
- aid: fumadocs:search-api
  name: Fumadocs Search API
  tags:
  - Documentation
  - Search
  humanURL: https://fumadocs.dev/docs/headless/search/orama
  properties:
  - url: https://fumadocs.dev/docs/headless/search/orama
    type: Documentation
  - url: openapi/fumadocs-search-openapi.yml
    type: OpenAPI
  - url: json-schema/fumadocs-search-result-schema.json
    type: JSONSchema
  description: The Fumadocs Search API is a server-side HTTP endpoint embedded in each Fumadocs documentation site that enables full-text search across all indexed documentation content. The endpoint (typically at /api/search) accepts a query string along with optional locale and tag filters, and returns a ranked list of matching pages, headings, and text segments with highlighted content and breadcrumb trails.
- aid: fumadocs:openapi-proxy-api
  name: Fumadocs OpenAPI Proxy API
  tags:
  - Documentation
  - OpenAPI
  - Proxy
  humanURL: https://fumadocs.dev/docs/ui/openapi
  properties:
  - url: https://fumadocs.dev/docs/ui/openapi
    type: Documentation
  - url: openapi/fumadocs-openapi-proxy-openapi.yml
    type: OpenAPI
  description: The Fumadocs OpenAPI Proxy API is a server-side HTTP proxy included in the fumadocs-openapi package that enables the interactive API playground to make authenticated requests to external API servers from the browser without CORS restrictions. Documentation sites mount the proxy at a route such as /api/proxy, where it accepts any HTTP method, extracts the target URL from the url query parameter, and transparently forwards the request to the upstream server.
name: Fumadocs
tags:
- Documentation
- Framework
- Next.js
- React
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Fumadocs is a modern documentation framework built on Next.js for building developer documentation sites. It provides a complete set of composable packages for content loading, navigation tree generation, full-text search, UI components, and interactive API reference generation from OpenAPI specifications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

