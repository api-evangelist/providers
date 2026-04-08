---
aid: google-pagespeed
url: https://raw.githubusercontent.com/api-evangelist/google-pagespeed/refs/heads/main/apis.yml
apis:
- name: PageSpeed Insights API
  description: The PageSpeed Insights API analyzes the content of a web page and generates suggestions to make it faster. It runs Lighthouse audits on the given URL and returns performance scores, Core Web Vitals metrics (Largest Contentful Paint, First Input Delay, Cumulative Layout Shift), field data from the Chrome User Experience Report, and detailed lab data with optimization opportunities and diagnostics.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://developers.google.com/speed/docs/insights/v5/get-started
  baseURL: https://www.googleapis.com/pagespeedonline/v5
  tags:
  - Audits
  - Core Web Vitals
  - Lighthouse
  - Performance
  properties:
  - type: Documentation
    url: https://developers.google.com/speed/docs/insights/v5/reference
  - type: OpenAPI
    url: openapi/pagespeed-insights-openapi.yml
  - type: Authentication
    url: https://developers.google.com/speed/docs/insights/v5/get-started#APIKey
  - type: Getting Started
    url: https://developers.google.com/speed/docs/insights/v5/get-started
  - type: JSONSchema
    url: json-schema/google-pagespeed-result-schema.json
name: Google PageSpeed
tags:
- Core Web Vitals
- Google
- Lighthouse
- Page Speed
- SEO
- Web Performance
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google PageSpeed Insights provides APIs for analyzing the performance of web pages on both mobile and desktop devices, returning performance scores, Core Web Vitals metrics, and actionable optimization recommendations powered by Lighthouse.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

