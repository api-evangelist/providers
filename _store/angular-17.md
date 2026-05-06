---
aid: angular-17
url: https://raw.githubusercontent.com/api-evangelist/angular-17/refs/heads/main/apis.yml
apis:
  - aid: angular-17:angular-core-api
    name: Angular 17 Core API
    tags:
      - Change Detection
      - Components
      - Decorators
      - Deferrable Views
      - Dependency Injection
      - Framework
      - Signals
      - Standalone Components
      - TypeScript
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://angular.dev/api/core
    humanURL: https://v17.angular.io/api/core
    properties:
      - url: https://v17.angular.io/api/core
        type: Documentation
      - url: https://github.com/angular/angular
        type: GitHub
    description: Core Angular 17 framework APIs featuring stable Signals for reactive state management, deferrable views (@defer blocks) for lazy loading template dependencies, new built-in control flow syntax (@if, @for, @switch), and improved server-side rendering. Released November 8, 2023.
  - aid: angular-17:angular-common-api
    name: Angular 17 Common API
    tags:
      - Directives
      - Pipes
      - Utilities
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://angular.dev/api/common
    humanURL: https://v17.angular.io/api/common
    properties:
      - url: https://v17.angular.io/api/common
        type: Documentation
    description: Common Angular 17 directives and pipes. Many NgIf/NgFor use cases are replaced by the new built-in control flow syntax in Angular 17.
  - aid: angular-17:angular-router-api
    name: Angular 17 Router API
    tags:
      - Guards
      - Navigation
      - Routing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://angular.dev/api/router
    humanURL: https://v17.angular.io/api/router
    properties:
      - url: https://v17.angular.io/api/router
        type: Documentation
    description: Angular 17 routing and navigation APIs with View Transitions API support for animated page transitions.
  - aid: angular-17:angular-forms-api
    name: Angular 17 Forms API
    tags:
      - Forms
      - Reactive Forms
      - Typed Forms
      - Validation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://angular.dev/api/forms
    humanURL: https://v17.angular.io/api/forms
    properties:
      - url: https://v17.angular.io/api/forms
        type: Documentation
    description: Angular 17 forms APIs with typed reactive forms and signal-based form integration improvements.
  - aid: angular-17:angular-http-client-api
    name: Angular 17 HTTP Client API
    tags:
      - HTTP
      - Interceptors
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://angular.dev/api/common/http
    humanURL: https://v17.angular.io/api/common/http
    properties:
      - url: https://v17.angular.io/api/common/http
        type: Documentation
    description: Angular 17 HTTP client with functional interceptors and improved SSR hydration support.
  - aid: angular-17:angular-platform-server-api
    name: Angular 17 Platform Server API
    tags:
      - Hydration
      - SSR
      - Server-Side Rendering
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://angular.dev/api/platform-server
    humanURL: https://v17.angular.io/api/platform-server
    properties:
      - url: https://v17.angular.io/api/platform-server
        type: Documentation
      - url: https://v17.angular.io/guide/ssr
        type: Guide
    description: Angular 17 server-side rendering APIs with significant SSR improvements including hydration, non-destructive hydration support, and new application builder with Vite and esbuild integration.
  - aid: angular-17:angular-cdk-api
    name: Angular 17 CDK API
    tags:
      - Accessibility
      - CDK
      - Components
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://material.angular.io/cdk
    humanURL: https://v17.material.angular.io/cdk/categories
    properties:
      - url: https://v17.material.angular.io/cdk/categories
        type: Documentation
      - url: https://github.com/angular/components
        type: GitHub
    description: Angular 17 Component Dev Kit providing behavior primitives for building custom accessible UI components.
name: Angular 17
tags:
  - Deferrable Views
  - Framework
  - Frontend
  - JavaScript
  - Open Source
  - Signals
  - Single Page Application
  - TypeScript
  - Web Development
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Open Source
common:
  - url: https://v17.angular.io/
    name: Angular 17 Documentation
    type: Documentation
  - url: https://github.com/angular/angular
    name: Angular GitHub Repository
    type: GitHub
  - url: https://github.com/angular/angular/releases/tag/17.0.0
    name: Angular 17 Release Notes
    type: Changelog
  - url: https://blog.angular.dev/introducing-angular-v17-4d7033312e4b
    name: Angular v17 Announcement Blog Post
    type: Blog
  - url: https://v17.angular.io/guide/defer
    name: Deferrable Views Guide
    type: Guide
  - url: https://v17.angular.io/guide/signals
    name: Signals Guide
    type: Guide
  - url: https://v17.angular.io/guide/control_flow
    name: Control Flow Guide
    type: Guide
  - url: https://www.npmjs.com/package/@angular/core
    name: Angular Core on npm
    type: PackageRegistry
  - url: https://github.com/angular/angular/blob/main/LICENSE
    name: MIT License
    type: License
  - url: https://github.com/angular/angular/blob/main/CONTRIBUTING.md
    name: Contributing Guide
    type: Contributing
  - url: https://stackoverflow.com/questions/tagged/angular
    name: Stack Overflow Angular Tag
    type: StackOverflow
  - url: https://discord.gg/angular
    name: Angular Discord
    type: Discord
  - url: https://twitter.com/angular
    name: Angular on Twitter
    type: X
created: '2023-11-08'
modified: '2026-04-19'
specificationVersion: '0.19'
description: Angular 17 is a major release of the Angular TypeScript framework, released November 8, 2023. Key features include stable Signals for reactive state management, deferrable views (@defer blocks) for lazy loading, new built-in control flow syntax (@if, @for, @switch) that is ~30% faster than NgIf/NgFor, improved server-side rendering with non-destructive hydration, View Transitions API support, and a new application builder powered by Vite and esbuild.
---
