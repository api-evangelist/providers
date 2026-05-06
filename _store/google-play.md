---
name: Google Play Developer
description: The Google Play Developer API allows developers to perform publishing and app-management tasks for Android applications. It includes the Publishing API for uploading and distributing apps, and the Subscriptions and In-App Purchases API for managing in-app products, subscriptions, and purchase verification.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-play/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Android
  - Apps
  - Google Play
  - In-App Purchases
  - Mobile
  - Publishing
  - Subscriptions
apis:
  - name: Google Play Developer API
    description: The Google Play Android Developer API provides programmatic access to publishing and app-management tasks including uploading APKs, managing in-app products, handling subscriptions, and verifying purchases.
    humanURL: https://developers.google.com/android-publisher
    baseURL: https://androidpublisher.googleapis.com
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.yml
common:
  - type: GettingStarted
    url: https://developers.google.com/android-publisher/getting_started
  - type: Pricing
    url: https://play.google.com/console/about/pricing/
  - type: JSONLD
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
