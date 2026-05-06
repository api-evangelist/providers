---
aid: google-search-console
name: Google Search Console
description: The Google Search Console API provides programmatic access to Search Console data, allowing you to monitor and maintain your site's presence in Google Search results.
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
url: https://search.google.com/search-console/about
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
tags:
  - Analytics
  - Google
  - Search
  - SEO
  - Webmaster Tools
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
      - type: Documentation
        url: https://searchconsole.googleapis.com/$discovery/rest?version=v1
        title: Discovery Document
      - type: Authentication
        url: https://developers.google.com/webmaster-tools/v1/how-tos/authorizing
      - type: GettingStarted
        url: https://developers.google.com/webmaster-tools/v1/quickstart
      - type: Console
        url: https://console.cloud.google.com/apis/library/searchconsole.googleapis.com
      - type: Pricing
        url: https://developers.google.com/webmaster-tools/v1/limits
      - type: TermsOfService
        url: https://developers.google.com/terms
      - type: CodeExamples
        url: https://developers.google.com/webmaster-tools/v1/samples
      - type: ChangeLog
        url: https://developers.google.com/webmaster-tools/v1/release-notes
      - type: Support
        url: https://support.google.com/webmasters/
      - type: Documentation
        url: https://developers.google.com/webmaster-tools/about
        title: Overview
      - type: Documentation
        url: https://developers.google.com/webmaster-tools/v1/prereqs
        title: Prerequisites
      - type: Quickstart
        url: https://developers.google.com/webmaster-tools/v1/quickstart/quickstart-python
        title: Python Quickstart
      - type: SDK
        url: https://developers.google.com/webmaster-tools/v1/libraries
        title: Client Libraries
      - type: Documentation
        url: https://developers.google.com/webmaster-tools/v1/how-tos/search_analytics
        title: Search Analytics Guide
      - type: APIReference
        url: https://developers.google.com/webmaster-tools/v1/searchanalytics/query
        title: Search Analytics Query
      - type: APIReference
        url: https://developers.google.com/webmaster-tools/v1/sitemaps
        title: Sitemaps Reference
      - type: APIReference
        url: https://developers.google.com/webmaster-tools/v1/sitemaps/get
        title: Sitemaps Get
      - type: APIReference
        url: https://developers.google.com/webmaster-tools/v1/sitemaps/submit
        title: Sitemaps Submit
      - type: APIReference
        url: https://developers.google.com/webmaster-tools/v1/sites/get
        title: Sites Get
      - type: APIReference
        url: https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect
        title: URL Inspection
      - type: APIReference
        url: https://developers.google.com/webmaster-tools/v1/urlInspection.index/UrlInspectionResult
        title: URL Inspection Result
      - type: JSONSchema
        url: json-schema/google-search-console-query-schema.json
      - type: JSONLD
        url: json-ld/google-search-console-context.jsonld
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
      - type: Documentation
        url: https://developers.google.com/webmaster-tools/search-console-api/about
        title: About
      - type: Documentation
        url: https://search.google.com/test/rich-results
        title: Rich Results Test
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
      - type: GettingStarted
        url: https://developers.google.com/search/apis/indexing-api/v3/quickstart
      - type: Tutorials
        url: https://developers.google.com/search/apis/indexing-api/v3/using-api
        title: How-To Guide
      - type: Documentation
        url: https://developers.google.com/search/apis/indexing-api/v3/prereqs
        title: Prerequisites
      - type: Pricing
        url: https://developers.google.com/search/apis/indexing-api/v3/quota-pricing
        title: Quota and Pricing
      - type: SDK
        url: https://developers.google.com/search/apis/indexing-api/v3/libraries
        title: Client Libraries
      - type: APIReference
        url: https://developers.google.com/search/apis/indexing-api/v3/reference/indexing/rpc
        title: RPC Reference
      - type: APIReference
        url: https://developers.google.com/search/apis/indexing-api/v3/reference/indexing/rest/v3/urlNotifications/publish
        title: Publish Method
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: DeveloperPortal
    url: https://developers.google.com/
  - type: StatusPage
    url: https://status.cloud.google.com/
  - type: Blog
    url: https://developers.googleblog.com/
  - type: PrivacyPolicy
    url: https://policies.google.com/privacy
  - type: TermsOfService
    url: https://policies.google.com/terms
  - type: Authentication
    url: https://developers.google.com/identity/protocols/oauth2/scopes
    title: OAuth 2.0 Scopes
  - type: SDK
    url: https://developers.google.com/api-client-library
    title: API Client Libraries
  - type: Blog
    url: https://developers.google.com/search/updates
    title: Google Search Central Blog
  - type: Support
    url: https://support.google.com/webmasters/
    title: Search Console Help
  - type: Console
    url: https://console.cloud.google.com/
  - type: SpectralRules
    url: rules/google-search-console-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/search-console.yaml
    title: Search Console Shared Definition
  - type: NaftikoCapability
    url: capabilities/seo-management.yaml
    title: SEO Management Workflow
  - type: Features
    url: https://search.google.com/search-console/about
    data:
      - name: Search Analytics
        description: Analyze search traffic data including impressions, clicks, CTR, and average position by query, page, country, device, and date.
      - name: Sitemap Management
        description: Submit, monitor, and manage XML sitemaps and sitemap indexes to optimize crawling and indexing.
      - name: URL Inspection
        description: Inspect individual URLs for indexing status, crawl details, mobile usability, and rich results eligibility.
      - name: Index Coverage
        description: Monitor which pages are indexed, identify indexing errors, and track coverage status across your site.
      - name: Mobile Usability Testing
        description: Test pages for mobile-friendliness and identify mobile usability issues.
      - name: Rich Results Validation
        description: Validate structured data markup and check rich results eligibility for individual URLs.
      - name: Site Verification
        description: Manage site ownership verification and access permissions for Search Console properties.
  - type: UseCases
    url: https://developers.google.com/webmaster-tools
    data:
      - name: SEO Performance Monitoring
        description: Track organic search performance metrics to identify trends, measure optimization impact, and report on search visibility.
      - name: Technical SEO Auditing
        description: Identify and resolve indexing issues, crawl errors, and mobile usability problems affecting search performance.
      - name: Content Optimization
        description: Analyze which queries drive traffic to specific pages and optimize content to improve rankings and click-through rates.
      - name: Automated Sitemap Submission
        description: Programmatically submit sitemaps when content is published or updated to accelerate indexing.
      - name: Multi-Site Management
        description: Monitor and manage search performance across multiple websites from a single integration.
  - type: Integrations
    url: https://developers.google.com/webmaster-tools
    data:
      - name: Google Analytics
        description: Combine Search Console data with Google Analytics for comprehensive website performance analysis.
      - name: Google Ads
        description: Connect search performance data with advertising campaigns to optimize paid and organic strategy together.
      - name: Google Cloud
        description: Deploy Search Console API integrations on Google Cloud Platform infrastructure.
      - name: BigQuery
        description: Export Search Console data to BigQuery for advanced analytics and cross-platform reporting.
      - name: Data Studio / Looker
        description: Visualize Search Console metrics in dashboards for stakeholder reporting and trend analysis.
include: []
---
