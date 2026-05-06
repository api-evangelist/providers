---
aid: vitepress
name: VitePress
description: VitePress is a Vite and Vue powered static site generator widely used for developer documentation. It converts Markdown content into fast, beautiful documentation sites with support for Vue components embedded directly in Markdown pages. VitePress ships a polished default theme with built-in dark mode, mobile-responsive layout, full-text local search, Algolia DocSearch integration, internationalization, and automatic sitemap generation. VitePress is the official documentation framework used by Vue, Vite, Rollup, Pinia, and many CNCF and open source projects.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Documentation
  - Markdown
  - Open Source
  - Static Site Generator
  - Vite
  - Vue
url: https://raw.githubusercontent.com/api-evangelist/vitepress/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vitepress:runtime-api
    name: VitePress Runtime API
    description: The VitePress Runtime API provides Vue composition functions and helper utilities for use in custom themes, Vue components, and Markdown pages. Key composables include useData() for accessing site and page metadata, useRoute() for current route information, useRouter() for programmatic navigation, and withBase() for base URL resolution. Components include Content for rendering compiled Markdown and ClientOnly for browser-only rendering.
    humanURL: https://vitepress.dev/reference/runtime-api
    baseURL: https://vitepress.dev
    tags:
      - API
      - Composables
      - Documentation
      - JavaScript
      - Runtime
      - Vue
    properties:
      - type: Documentation
        url: https://vitepress.dev/reference/runtime-api
      - type: Reference
        url: https://vitepress.dev/reference/site-config
  - aid: vitepress:site-config
    name: VitePress Site Configuration
    description: The VitePress site configuration system exported from .vitepress/config.[js|ts]. Defines all settings controlling site metadata, routing, theming, Markdown processing, Vite and Vue integration, and build hooks. Includes the default theme configuration for navigation, sidebar, search, social links, and internationalization.
    humanURL: https://vitepress.dev/reference/site-config
    baseURL: https://vitepress.dev
    tags:
      - Configuration
      - Documentation
      - Static Site
      - Theming
    properties:
      - type: Documentation
        url: https://vitepress.dev/reference/site-config
      - type: Reference
        url: https://vitepress.dev/reference/default-theme-config
common:
  - type: Website
    url: https://vitepress.dev
  - type: Documentation
    url: https://vitepress.dev/guide/getting-started
  - type: GitHub
    url: https://github.com/vuejs/vitepress
  - type: JSONSchema
    url: json-schema/vitepress-config-schema.json
  - type: JSONSchema
    url: json-schema/vitepress-frontmatter-schema.json
  - type: JSONLD
    url: json-ld/vitepress-context.jsonld
  - type: JSONStructure
    url: json-structure/vitepress-config-structure.json
  - type: Vocabulary
    url: vocabulary/vitepress-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
