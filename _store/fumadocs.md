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
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-18'
modified: '2026-04-28'
position: Consumer
segments:
  - Documentation
description: Fumadocs is a modern documentation framework built on Next.js for building developer documentation sites. It provides a complete set of composable packages for content loading, navigation tree generation, full-text search, UI components, and interactive API reference generation from OpenAPI specifications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://fumadocs.dev
    name: Fumadocs
    type: Website
    description: The official Fumadocs documentation site and homepage.
  - url: https://fumadocs.dev/docs
    name: Fumadocs Documentation
    type: Documentation
    description: Full documentation for all Fumadocs packages and APIs.
  - url: https://github.com/fuma-nama/fumadocs
    name: Fumadocs GitHub Repository
    type: GitHub
    description: Source code, issues, and contributions for the Fumadocs monorepo.
  - url: https://fumadocs.dev/docs/ui/components
    name: Fumadocs UI Components
    type: Documentation
    description: Reference for all Fumadocs UI React components.
  - url: https://fumadocs.dev/docs/headless/search/orama
    name: Fumadocs Search Documentation
    type: Documentation
    description: Guide for configuring full-text search with Orama, Algolia, and other backends.
  - url: https://fumadocs.dev/docs/ui/openapi
    name: Fumadocs OpenAPI Documentation
    type: Documentation
    description: Guide for generating interactive API reference pages from OpenAPI specs.
  - url: https://www.npmjs.com/package/fumadocs-core
    name: fumadocs-core on npm
    type: Distribution
    description: npm package for the core Fumadocs library.
  - url: https://www.npmjs.com/package/fumadocs-ui
    name: fumadocs-ui on npm
    type: Distribution
    description: npm package for Fumadocs UI components and themes.
  - url: https://www.npmjs.com/package/fumadocs-openapi
    name: fumadocs-openapi on npm
    type: Distribution
    description: npm package for Fumadocs OpenAPI reference generation.
  - url: https://github.com/fuma-nama/fumadocs/blob/main/LICENSE
    name: Fumadocs License (MIT)
    type: License
    description: MIT open-source license for the Fumadocs project.
  - url: json-schema/fumadocs-page-tree-schema.json
    name: Fumadocs Page Tree Schema
    type: JSONSchema
    description: JSON Schema for the hierarchical navigation page tree structure.
  - url: json-schema/fumadocs-page-schema.json
    name: Fumadocs Page Frontmatter Schema
    type: JSONSchema
    description: JSON Schema for MDX page frontmatter fields.
  - url: json-schema/fumadocs-meta-schema.json
    name: Fumadocs Meta Schema
    type: JSONSchema
    description: JSON Schema for meta.json folder configuration files.
  - url: json-ld/fumadocs-context.jsonld
    name: Fumadocs JSON-LD Context
    type: JSONLD
    description: JSON-LD context mapping Fumadocs entities to schema.org and standard vocabularies.
---
