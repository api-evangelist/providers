---
aid: keystatic
name: Keystatic
description: Keystatic is an open source, Git-based content management system that stores content as Markdown, JSON, and YAML directly in a project's Git repository. The Keystatic Reader API is a Node.js library that lets applications read Keystatic content from any local directory or GitHub repository server-side, supporting frameworks like Next.js, Astro, Remix, and React Server Components.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CMS
  - Content Management
  - Git-based
  - Open Source
  - SDK
  - Static Site
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/keystatic/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: keystatic:reader-api
    name: Keystatic Reader API
    description: The Reader API is a server-side Node.js library exposing createReader and createGitHubReader functions that let applications read Keystatic content from a local directory or GitHub repository. The Reader API is a programmatic SDK; it is not exposed as a public HTTP REST API.
    humanURL: https://keystatic.com/docs/reader-api
    tags:
      - CMS
      - SDK
    properties:
      - type: Documentation
        url: https://keystatic.com/docs/reader-api
      - type: Website
        url: https://keystatic.com/
      - type: GitHub
        url: https://github.com/Thinkmill/keystatic
common:
  - type: Website
    url: https://keystatic.com/
  - type: Documentation
    url: https://keystatic.com/docs
  - type: GitHub
    url: https://github.com/Thinkmill/keystatic
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
