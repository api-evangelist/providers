---
aid: hacker-news
name: Hacker News
description: Hacker News is Y Combinator's technology news aggregation and discussion platform. It exposes a public, read-only Firebase-backed API that gives developers real-time access to stories, comments, jobs, polls, and user profiles across the full HN dataset.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/hacker-news/refs/heads/main/apis.yml
access: 3rd-Party
tags:
  - Developer Community
  - Technology News
  - Y Combinator
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hacker-news:hacker-news-api
    name: Hacker News API
    description: The Hacker News API provides access to items (stories, comments, jobs, Ask HNs, polls), users, and live data via Firebase endpoints. It is a public, read-only REST API that exposes the full dataset of Hacker News content in near real-time. Developers can retrieve individual items by ID, look up user profiles, and subscribe to live feeds of new, top, best, ask, show, and job stories. The API requires no authentication and returns JSON data from Firebase's real-time database infrastructure.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/HackerNews/API
    baseURL: https://hacker-news.firebaseio.com
    tags:
      - Comments
      - News
      - Stories
    properties:
      - type: Documentation
        url: https://github.com/HackerNews/API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/hacker-news/refs/heads/main/openapi/hacker-news-openapi.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/hacker-news/refs/heads/main/hacker-news-rules.yml
common:
  - url: https://news.ycombinator.com/
    name: Hacker News Website
    type: Website
  - url: https://github.com/HackerNews/API
    name: API Documentation
    type: Documentation
  - url: https://news.ycombinator.com/newsguidelines.html
    name: Community Guidelines
    type: Guidelines
  - url: https://news.ycombinator.com/legal
    name: Legal
    type: TermsOfService
  - url: https://news.ycombinator.com/security.html
    name: Security Policy
    type: Security
  - url: https://news.ycombinator.com/lists
    name: Lists
    type: Portal
  - url: https://news.ycombinator.com/rss
    name: RSS Feed
    type: RSS
  - url: https://news.ycombinator.com/ask
    name: Ask HN
    type: Forum
  - url: https://news.ycombinator.com/show
    name: Show HN
    type: Showcase
  - url: https://www.ycombinator.com/
    name: Y Combinator
    type: About
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
