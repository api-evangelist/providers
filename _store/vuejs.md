---
name: Vue.js
description: Vue.js is a progressive JavaScript framework for building user interfaces and single-page applications. Created by Evan You and maintained by an open-source community, Vue.js is designed to be incrementally adoptable and focuses on the view layer. It integrates with other libraries or existing projects and powers complex single-page applications when combined with modern tooling like Vue Router, Pinia state management, and Vite build tooling. Vue.js is one of the most popular frontend frameworks with over 4 million weekly npm downloads and a rich ecosystem of components and plugins.
image: https://vuejs.org/images/logo.png
tags:
  - Component-Based
  - Framework
  - Frontend
  - JavaScript
  - Open Source
  - UI
created: '2024-01-01'
modified: '2026-05-03'
url: https://vuejs.org
specificationVersion: '0.19'
apis:
  - name: Vue.js Core API
    description: Core Vue.js composition and options API for building reactive user interfaces. Provides reactivity primitives (ref, reactive, computed, watch), lifecycle hooks, component system, template directives, and application mounting. The primary API surface for Vue.js component development.
    image: https://vuejs.org/images/logo.png
    humanUrl: https://vuejs.org/api/
    baseUrl: https://cdn.jsdelivr.net/npm/vue@3
    tags:
      - Components
      - Composition API
      - Framework
      - JavaScript
      - Reactive
    properties:
      - type: Documentation
        url: https://vuejs.org/guide/introduction.html
      - type: API Documentation
        url: https://vuejs.org/api/
      - type: Tutorial
        url: https://vuejs.org/tutorial/
      - type: Examples
        url: https://vuejs.org/examples/
      - type: Style Guide
        url: https://vuejs.org/style-guide/
      - type: GitHub
        url: https://github.com/vuejs/core
      - type: CDN
        url: https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.js
      - type: NPM
        url: https://www.npmjs.com/package/vue
      - type: Migration Guide
        url: https://v3-migration.vuejs.org/
  - name: Vue Router
    description: Official client-side routing solution for Vue.js single-page applications. Vue Router provides declarative routing with nested routes, dynamic route matching, navigation guards, route lazy-loading, and programmatic navigation. Supports both HTML5 history mode and hash-based routing.
    humanUrl: https://router.vuejs.org/
    baseUrl: https://cdn.jsdelivr.net/npm/vue-router@4
    tags:
      - Navigation
      - Router
      - SPA
    properties:
      - type: Documentation
        url: https://router.vuejs.org/guide/
      - type: API Documentation
        url: https://router.vuejs.org/api/
      - type: GitHub
        url: https://github.com/vuejs/router
      - type: NPM
        url: https://www.npmjs.com/package/vue-router
  - name: Pinia
    description: The official state management library for Vue.js, designed for composability and TypeScript support. Pinia provides a simpler and more intuitive API than Vuex with stores defined using the Composition API pattern, full TypeScript inference, devtools support, and hot module replacement.
    humanUrl: https://pinia.vuejs.org/
    baseUrl: https://cdn.jsdelivr.net/npm/pinia@2
    tags:
      - Data
      - State Management
      - Store
    properties:
      - type: Documentation
        url: https://pinia.vuejs.org/introduction.html
      - type: API Documentation
        url: https://pinia.vuejs.org/api/
      - type: GitHub
        url: https://github.com/vuejs/pinia
      - type: NPM
        url: https://www.npmjs.com/package/pinia
  - name: Vite
    description: Next-generation frontend build tooling powering the Vue.js development experience. Vite provides near-instant server startup with native ES modules, hot module replacement (HMR), optimized production builds using Rollup, and first-class Vue.js support with the official @vitejs/plugin-vue plugin.
    humanUrl: https://vitejs.dev/
    baseUrl: https://vitejs.dev
    tags:
      - Build Tool
      - Bundler
      - Development
    properties:
      - type: Documentation
        url: https://vitejs.dev/guide/
      - type: Configuration
        url: https://vitejs.dev/config/
      - type: GitHub
        url: https://github.com/vitejs/vite
      - type: NPM
        url: https://www.npmjs.com/package/vite
  - name: VueUse
    description: Collection of essential Vue Composition Utilities for Vue.js, providing over 200 composable functions for common browser APIs, sensors, animations, state management helpers, and utility patterns. VueUse is tree-shakable and works with both Vue 2 and Vue 3.
    humanUrl: https://vueuse.org/
    baseUrl: https://cdn.jsdelivr.net/npm/@vueuse/core
    tags:
      - Composables
      - Utilities
      - Vue.js
    properties:
      - type: Documentation
        url: https://vueuse.org/guide/
      - type: API Documentation
        url: https://vueuse.org/functions.html
      - type: GitHub
        url: https://github.com/vueuse/vueuse
      - type: NPM
        url: https://www.npmjs.com/package/@vueuse/core
  - name: Nuxt.js
    description: The intuitive Vue framework for building full-stack web applications with Vue.js. Nuxt provides server-side rendering (SSR), static site generation (SSG), file-based routing, auto-imports, and a rich module ecosystem. Nuxt is the primary meta-framework for production Vue.js applications.
    humanUrl: https://nuxt.com/
    baseUrl: https://nuxt.com
    tags:
      - Framework
      - Full-Stack
      - SSR
      - Vue.js
    properties:
      - type: Documentation
        url: https://nuxt.com/docs/getting-started/introduction
      - type: API Documentation
        url: https://nuxt.com/docs/api/
      - type: GitHub
        url: https://github.com/nuxt/nuxt
      - type: NPM
        url: https://www.npmjs.com/package/nuxt
common:
  - type: Blog
    url: https://blog.vuejs.org/
  - type: ChangeLog
    url: https://github.com/vuejs/core/blob/main/CHANGELOG.md
  - type: Terms of Service
    url: https://vuejs.org/about/coc.html
  - type: Privacy Policy
    url: https://vuejs.org/about/privacy.html
  - type: Support
    url: https://vuejs.org/support/
  - type: Sponsors
    url: https://vuejs.org/sponsor/
  - type: GitHubOrg
    url: https://github.com/vuejs
  - type: NPM
    url: https://www.npmjs.com/package/vue
  - type: Community
    url: https://discord.com/invite/vue
  - type: Forum
    url: https://forum.vuejs.org/
  - type: Twitter
    url: https://twitter.com/vuejs
  - url: vocabulary/vuejs-vocabulary.yml
    type: Vocabulary
  - url: json-schema/vuejs-component-schema.json
    type: JSONSchema
  - url: json-ld/vuejs-context.jsonld
    type: JSONLDContext
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
