---
aid: google-optimize
name: Google Optimize
description: Google Optimize was a website optimization and A/B testing tool that helped businesses test variations of web pages and personalize experiences. Google Optimize and Optimize 360 were sunset on September 30, 2023. Google recommends migrating to Google Analytics 4 with built-in A/B testing or third-party tools.
type: Index
image: https://www.gstatic.com/images/branding/product/1x/optimize_48dp.png
url: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - A/B Testing
  - Analytics
  - Deprecated
  - Experimentation
  - Google
  - Optimization
  - Personalization
  - Sunset
apis:
  - aid: google-optimize:optimize-api
    name: Google Optimize API (Sunset)
    description: API for managing Google Optimize experiments, variants, and accessing optimization data. Sunset on September 30, 2023. Migrate to Google Analytics 4 experiments or third-party A/B testing tools.
    humanURL: https://support.google.com/optimize/answer/12979939
    baseURL: https://www.googleapis.com/optimize/v1
    tags:
      - A/B Testing
      - Deprecated
      - Experimentation
      - Sunset
    properties:
      - type: Documentation
        url: https://support.google.com/optimize/answer/12979939
common:
  - type: Documentation
    url: https://support.google.com/optimize/answer/12979939
    description: Google Optimize sunset announcement and migration guidance.
  - type: Blog
    url: https://blog.google/products/marketingplatform/analytics/
  - type: TermsOfService
    url: https://www.google.com/analytics/terms/us.html
  - type: PrivacyPolicy
    url: https://policies.google.com/privacy
  - type: Features
    data:
      - name: A/B Testing (Sunset)
        description: Test two or more variants of a web page to determine which performs better. Service sunset September 30, 2023.
      - name: Multivariate Testing (Sunset)
        description: Test combinations of multiple page elements simultaneously. Service sunset September 30, 2023.
      - name: Redirect Tests (Sunset)
        description: Test entirely different pages against each other. Service sunset September 30, 2023.
      - name: Personalization (Sunset)
        description: Deliver targeted experiences to specific audience segments. Service sunset September 30, 2023.
      - name: Google Analytics Integration (Sunset)
        description: Native integration with Google Analytics for experiment targeting and reporting. Service sunset September 30, 2023.
      - name: Visual Editor (Sunset)
        description: WYSIWYG editor for creating test variants without code changes. Service sunset September 30, 2023.
  - type: UseCases
    data:
      - name: Landing Page Optimization
        description: Test landing page variations to improve conversion rates. (Service sunset)
      - name: CTA Testing
        description: Test call-to-action button text, color, and placement. (Service sunset)
      - name: Content Personalization
        description: Show different content to different audience segments. (Service sunset)
      - name: Checkout Flow Optimization
        description: Test checkout process variations to reduce abandonment. (Service sunset)
  - type: Solutions
    data:
      - name: Google Optimize (Sunset)
        description: Free A/B testing tool sunset September 30, 2023. Migrate to GA4 experiments or third-party tools.
      - name: Google Optimize 360 (Sunset)
        description: Enterprise A/B testing tool sunset September 30, 2023. Part of Google Marketing Platform.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
