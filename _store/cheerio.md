---
aid: cheerio
name: Cheerio
x-type: opensource
description: Cheerio is a fast, flexible, and elegant Node.js library for parsing and manipulating HTML and XML using a jQuery-compatible API. It is widely used for server-side web scraping, HTML transformation, data extraction, and static site generation. Cheerio is MIT licensed and distributed as the cheerio npm package, maintained under the cheeriojs GitHub organization.
type: Index
position: Producer
access: Open Source
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/cheerio/refs/heads/main/apis.yml
tags:
  - Data Extraction
  - DOM
  - HTML
  - HTML Parsing
  - jQuery
  - MIT License
  - Node.js
  - npm
  - Open Source
  - Parser
  - Scraping
  - Server-side
  - Web Scraping
  - XML
created: '2026-03-29'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: cheerio:cheerio
    name: Cheerio
    description: Cheerio implements a subset of core jQuery designed for the server. It parses markup into a traversable, manipulable DOM-like data structure and exposes a familiar jQuery-style API for selecting elements, traversing the tree, modifying attributes, extracting text, and rendering HTML. It is commonly used in scraping pipelines, build tools, static site generators, and tests that need to operate over HTML content without launching a browser.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cheerio.js.org/
    tags:
      - Data Extraction
      - HTML Parsing
      - jQuery
      - Node.js
      - Scraping
    properties:
      - type: Documentation
        url: https://cheerio.js.org/docs/intro
      - type: GettingStarted
        url: https://cheerio.js.org/docs/intro
      - type: APIReference
        url: https://cheerio.js.org/docs/api
      - type: Blog
        url: https://cheerio.js.org/blog
      - type: GitHubRepository
        url: https://github.com/cheeriojs/cheerio
      - type: NPMPackage
        url: https://www.npmjs.com/package/cheerio
      - type: License
        url: https://github.com/cheeriojs/cheerio/blob/main/LICENSE
      - type: ContributionGuide
        url: https://github.com/cheeriojs/cheerio/blob/main/CONTRIBUTING.md
      - type: Issues
        url: https://github.com/cheeriojs/cheerio/issues
      - type: Releases
        url: https://github.com/cheeriojs/cheerio/releases
common:
  - type: Website
    url: https://cheerio.js.org/
  - type: Documentation
    url: https://cheerio.js.org/docs/intro
  - type: APIReference
    url: https://cheerio.js.org/docs/api
  - type: GitHubOrganization
    url: https://github.com/cheeriojs
  - type: GitHubRepository
    url: https://github.com/cheeriojs/cheerio
  - type: NPMPackage
    url: https://www.npmjs.com/package/cheerio
  - type: License
    name: MIT
    url: https://github.com/cheeriojs/cheerio/blob/main/LICENSE
  - type: Issues
    url: https://github.com/cheeriojs/cheerio/issues
  - type: JSONLD
    url: json-ld/cheerio-context.jsonld
  - name: Features
    type: Features
    data:
      - name: jQuery-Compatible API
      - name: Server-Side HTML Parsing
      - name: XML Parsing
      - name: DOM Traversal
      - name: DOM Manipulation
      - name: CSS Selector Engine
      - name: parse5 Integration
      - name: htmlparser2 Integration
      - name: Streaming Parser
      - name: TypeScript Types
      - name: Browser-Compatible Builds
  - name: UseCases
    type: UseCases
    data:
      - name: Web Scraping
      - name: Server-Side HTML Manipulation
      - name: Static Site Generation
      - name: Data Extraction Pipelines
      - name: HTML Email Templating
      - name: SEO Auditing Tools
      - name: Content Migration
      - name: Test HTML Assertions
      - name: RSS and Atom Feed Generation
      - name: HTML Sanitization Tooling
  - name: Tools
    type: Tools
    data:
      - name: cheerio
      - name: parse5
      - name: htmlparser2
      - name: domhandler
      - name: domutils
      - name: css-select
  - name: Integrations
    type: Integrations
    data:
      - name: Node.js
      - name: npm
      - name: TypeScript
      - name: Bun
      - name: Deno
      - name: Puppeteer
      - name: Playwright
      - name: Axios
      - name: node-fetch
      - name: Got
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
