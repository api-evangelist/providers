---
aid: google-search-console
url: https://raw.githubusercontent.com/api-evangelist/google-search-console/refs/heads/main/apis.yml
apis:
- name: Google Search Console API
  description: Provides access to Search Console data including search analytics, sitemaps, URL inspection, and index coverage reports.
  image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
  humanURL: https://developers.google.com/webmaster-tools
  baseURL: https://searchconsole.googleapis.com
  tags:
  - Indexing
  - Search Analytics
  - SEO
  - Sitemaps
  properties:
  - type: Documentation
    url: https://developers.google.com/webmaster-tools/v1/api_reference_index
  - type: OpenAPI
    url: openapi/google-search-console-api-openapi.yml
  - type: Discovery
    url: https://searchconsole.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://developers.google.com/webmaster-tools/v1/how-tos/authorizing
  - type: Getting Started
    url: https://developers.google.com/webmaster-tools/v1/quickstart
  - type: API Console
    url: https://console.cloud.google.com/apis/library/searchconsole.googleapis.com
  - type: Pricing
    url: https://developers.google.com/webmaster-tools/v1/limits
  - type: Terms of Service
    url: https://developers.google.com/terms
  - type: Code Examples
    url: https://developers.google.com/webmaster-tools/v1/samples
  - type: Change Log
    url: https://developers.google.com/webmaster-tools/v1/release-notes
  - type: Support
    url: https://support.google.com/webmasters/
  - type: Overview
    url: https://developers.google.com/webmaster-tools/about
  - type: Prerequisites
    url: https://developers.google.com/webmaster-tools/v1/prereqs
  - type: Python Quickstart
    url: https://developers.google.com/webmaster-tools/v1/quickstart/quickstart-python
  - type: Client Libraries
    url: https://developers.google.com/webmaster-tools/v1/libraries
  - type: Search Analytics Guide
    url: https://developers.google.com/webmaster-tools/v1/how-tos/search_analytics
  - type: Search Analytics Query
    url: https://developers.google.com/webmaster-tools/v1/searchanalytics/query
  - type: Sitemaps Reference
    url: https://developers.google.com/webmaster-tools/v1/sitemaps
  - type: Sitemaps Get
    url: https://developers.google.com/webmaster-tools/v1/sitemaps/get
  - type: Sitemaps Submit
    url: https://developers.google.com/webmaster-tools/v1/sitemaps/submit
  - type: Sites Get
    url: https://developers.google.com/webmaster-tools/v1/sites/get
  - type: URL Inspection
    url: https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect
  - type: URL Inspection Result
    url: https://developers.google.com/webmaster-tools/v1/urlInspection.index/UrlInspectionResult
- name: Google Search Console URL Testing Tools API
  description: Provides tools for running validation tests against single URLs, including mobile-friendly testing and rich results validation for structured data.
  image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
  humanURL: https://developers.google.com/webmaster-tools/search-console-api
  baseURL: https://searchconsole.googleapis.com
  tags:
  - Mobile Friendly
  - Rich Results
  - Structured Data
  - Testing
  - Validation
  properties:
  - type: Documentation
    url: https://developers.google.com/webmaster-tools/search-console-api/v1/
  - type: About
    url: https://developers.google.com/webmaster-tools/search-console-api/about
  - type: Rich Results Test
    url: https://search.google.com/test/rich-results
- name: Google Indexing API
  description: The Indexing API allows any site owner to directly notify Google when pages are added or removed, enabling faster crawling and indexing of content such as job postings and livestream videos.
  image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
  humanURL: https://developers.google.com/search/apis/indexing-api/v3/quickstart
  baseURL: https://indexing.googleapis.com
  tags:
  - Crawling
  - Indexing
  - SEO
  - URL Submission
  properties:
  - type: Documentation
    url: https://developers.google.com/search/apis/indexing-api/v3/reference/indexing/rest
  - type: Getting Started
    url: https://developers.google.com/search/apis/indexing-api/v3/quickstart
  - type: How-To Guide
    url: https://developers.google.com/search/apis/indexing-api/v3/using-api
  - type: Prerequisites
    url: https://developers.google.com/search/apis/indexing-api/v3/prereqs
  - type: Quota and Pricing
    url: https://developers.google.com/search/apis/indexing-api/v3/quota-pricing
  - type: Client Libraries
    url: https://developers.google.com/search/apis/indexing-api/v3/libraries
  - type: RPC Reference
    url: https://developers.google.com/search/apis/indexing-api/v3/reference/indexing/rpc
  - type: Publish Method
    url: https://developers.google.com/search/apis/indexing-api/v3/reference/indexing/rest/v3/urlNotifications/publish
name: Google Search Console
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
type: Contract
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google Search Console API provides programmatic access to Search Console data, allowing you to monitor and maintain your site's presence in Google Search results.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

