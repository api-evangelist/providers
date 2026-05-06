---
aid: axios
name: Axios
description: Axios is a promise-based HTTP client for the browser and Node.js with automatic JSON data transformation and request/response interceptors.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Clients
  - HTTP Client
  - JavaScript
  - Node.js
url: https://raw.githubusercontent.com/api-evangelist/axios/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: axios:axios
    name: Axios
    description: Axios is a promise-based HTTP client for the browser and Node.js with automatic JSON data transformation and request/response interceptors.
    humanURL: https://axios-http.com
    tags:
      - Clients
      - HTTP Client
      - JavaScript
      - Node.js
    properties:
      - type: Documentation
        url: https://axios-http.com/docs/intro
      - type: GettingStarted
        url: https://axios-http.com/docs/intro
common:
  - type: Website
    url: https://axios-http.com
  - type: Documentation
    url: https://axios-http.com/docs/intro
  - type: GitHubOrganization
    url: https://github.com/axios/axios
  - type: GitHubRepository
    url: https://github.com/axios/axios
  - type: SDK
    url: https://www.npmjs.com/package/axios
    title: npm Package
  - type: Features
    data:
      - name: Promise-Based
        description: Built on promises for clean async/await and .then() chaining patterns.
      - name: Browser and Node.js Support
        description: Works in both browser and Node.js environments with automatic XHR/http adapter selection.
      - name: Automatic JSON Transformation
        description: Automatically serializes JavaScript objects to JSON and parses JSON responses.
      - name: Request and Response Interceptors
        description: Add custom logic to requests and responses before they are handled.
      - name: Request Cancellation
        description: Cancel in-flight requests using AbortController or the CancelToken API.
      - name: XSRF Protection
        description: Built-in client-side XSRF protection support.
      - name: Timeout Support
        description: Configure request timeouts for automatic cancellation of long-running requests.
      - name: Progress Tracking
        description: Track upload and download progress with onUploadProgress and onDownloadProgress callbacks.
  - type: UseCases
    data:
      - name: REST API Consumption
        description: Consume RESTful APIs from frontend applications and Node.js servers.
      - name: File Uploads
        description: Upload files with progress tracking to backend services.
      - name: Authentication
        description: Add auth tokens and headers automatically via request interceptors.
      - name: Data Fetching
        description: Fetch data in React, Vue, Angular, and other JavaScript frameworks.
      - name: API Testing
        description: Test API integrations in Node.js scripts and test suites.
  - type: Integrations
    data:
      - name: React
        description: Commonly used for data fetching in React applications with hooks.
      - name: Vue.js
        description: Official recommendation for HTTP requests in Vue.js applications.
      - name: Node.js
        description: Used for server-side HTTP requests with the native http/https adapter.
      - name: TypeScript
        description: First-class TypeScript support with bundled type definitions.
      - name: Jest
        description: Easily mocked with jest.mock() for unit testing HTTP-dependent code.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
