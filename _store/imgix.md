---
aid: imgix
name: Imgix
description: imgix is a real-time image processing and CDN service that helps developers optimize images, improve page speed, and build responsive designs. The imgix Rendering API provides powerful image transformation and optimization capabilities directly through URL parameters.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CDN
  - Image Optimization
  - Image Processing
  - Media
created: '2024-11-13'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-search/imgix/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: imgix:imgix-rendering-api
    name: Imgix Rendering API
    description: The imgix Rendering API can optimize your images, improve your page speed, and make it easy to create responsive designs. Images are processed and delivered in real-time via URL parameters.
    humanURL: https://docs.imgix.com/en-US/apis/rendering/overview
    tags:
      - CDN
      - Image Optimization
      - Image Processing
    properties:
      - type: Documentation
        url: https://docs.imgix.com/en-US/apis/rendering/overview
      - type: Getting Started
        url: https://docs.imgix.com/
common:
  - type: Website
    url: https://imgix.com/
  - type: Documentation
    url: https://docs.imgix.com/
  - type: Support
    url: https://support.imgix.com/
  - type: Features
    data:
      - 'Starter $25/mo: 100 credits, 50 GB storage, 100 GB bandwidth'
      - 'Basic $75/mo: 375 credits, 187.5 GB storage, 375 GB bandwidth'
      - 'Midrange $150/mo: 830 credits'
      - 'Growth $300/mo: 1,875 credits'
      - 'Growth Plus $500/mo: 3,570 credits'
      - 'Enterprise: custom credits and workflows'
      - Per-extra-credit declines from $0.25 (Starter) to $0.12 (Growth Plus)
      - On-the-fly URL-based image transformations
      - 100+ transformation parameters
      - 'Render API: unmetered requests (counted in credits)'
      - 'Management API: 100 req/sec/source'
      - Master image counts toward storage
      - Webhooks for source/asset events
      - Auto-format (WebP/AVIF), auto-quality, auto-compress
      - Video processing (separate Video product)
      - Asset Manager DAM and Asset Cleanup
    sources:
      - https://imgix.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
