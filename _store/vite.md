---
aid: vite
name: Vite
description: Vite is a next-generation frontend build tool that dramatically improves the frontend development experience. It provides a lightning-fast dev server using native ES modules, an optimized production build via Rolldown/Rollup, a rich plugin API, and a fully-typed JavaScript API for programmatic usage.
type: Index
position: Consumer
access: 3rd-Party
image: https://vitejs.dev/logo.svg
tags:
  - Build Tools
  - Bundler
  - Development Server
  - ESM
  - Frontend
  - Hot Module Replacement
  - JavaScript
  - Plugin API
  - TypeScript
  - Vite
created: '2025-01-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/vite/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: vite:javascript-api
    name: Vite JavaScript API
    description: The Vite JavaScript API provides a fully-typed programmatic interface for embedding Vite into build toolchains, frameworks, and custom CLI tools. It covers creating a dev server, triggering production builds, running previews, resolving configuration, and transforming files.
    humanURL: https://vite.dev/guide/api-javascript
    tags:
      - Build
      - Dev Server
      - JavaScript
      - Plugin
      - Preview
      - TypeScript
      - Vite
    properties:
      - type: Documentation
        url: https://vite.dev/guide/api-javascript
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vite/refs/heads/main/openapi/vite-javascript-api-openapi.yml
  - aid: vite:plugin-api
    name: Vite Plugin API
    description: The Vite Plugin API extends Rolldown's plugin interface with additional Vite-specific hooks, giving plugin authors full control over the build pipeline, dev server configuration, HTML transformation, and hot module replacement.
    humanURL: https://vite.dev/guide/api-plugin
    tags:
      - Build
      - Hot Module Replacement
      - Plugin
      - Transform
      - Vite
    properties:
      - type: Documentation
        url: https://vite.dev/guide/api-plugin
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vite/refs/heads/main/openapi/vite-plugin-api-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - url: https://vitejs.dev
    type: Website
  - url: https://vite.dev/guide/
    type: Documentation
  - url: https://github.com/vitejs
    type: GitHub Organization
  - url: https://github.com/vitejs/vite
    type: GitHub Repository
  - url: https://twitter.com/vite_js
    type: Twitter
  - url: https://chat.vitejs.dev
    type: Discord
  - url: https://www.npmjs.com/package/vite
    type: npm Package
  - url: https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md
    type: Changelog
  - url: https://github.com/vitejs/vite/blob/main/LICENSE
    type: License
  - url: https://github.com/vitejs/awesome-vite
    type: Integrations
  - url: https://github.com/vitejs/vite-plugin-vue
    type: SDK
  - url: https://github.com/vitejs/vite-plugin-react
    type: SDK
---
