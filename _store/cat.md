---
aid: cat
url: https://raw.githubusercontent.com/api-evangelist/cat/refs/heads/main/apis.yml
name: CAT
tags:
  - Construction
  - Engines
  - Equipment
  - Heavy Equipment
  - Locomotives
  - Manufacturing
  - Mining
  - Telematics
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-07'
modified: '2026-04-23'
position: Consumer
description: 'CAT is the brand name and ticker symbol for Caterpillar Inc. (NYSE: CAT), the world''s leading manufacturer of construction and mining equipment, off-highway diesel and natural gas engines, industrial gas turbines, and diesel-electric locomotives. Cat Digital publishes a public API catalog at digital.cat.com that exposes fleet, asset, telematics, and fuel data APIs built on the Cat Connect and VisionLink platforms.'
apis:
  - aid: cat:cat-digital-marketplace-api
    name: CAT Digital Marketplace API
    tags:
      - Assets
      - Construction
      - Heavy Equipment
      - Telematics
      - VisionLink
    humanURL: https://digital.cat.com/api-catalog-overview
    properties:
      - url: https://digital.cat.com/api-catalog-overview
        type: Documentation
      - url: openapi/cat-openapi.yml
        type: OpenAPI
      - url: https://digital.cat.com/
        type: Portal
      - url: https://digital.cat.com/release-notes-manager
        type: ChangeLog
    description: Explore the Cat Digital API catalog, subscribe to APIs, and execute calls against the Cat Digital products. Coverage includes fleet and asset management, telematics (VisionLink), fuel and utilization data, hours/odometer events, and geofencing.
common:
  - type: Portal
    url: https://digital.cat.com/
  - type: Website
    url: https://www.cat.com/
  - type: Login
    url: https://digital.cat.com/
  - type: Applications
    url: https://digital.cat.com/applications
  - type: FAQ
    url: https://digital.cat.com/knowledge-hub/faq
  - type: News
    url: https://digital.cat.com/news-announcements-list
  - type: ChangeLog
    url: https://digital.cat.com/release-notes-manager
  - type: TermsOfService
    url: https://digital.cat.com/legal
  - type: PrivacyPolicy
    url: https://digital.cat.com/privacy
  - type: InvestorRelations
    url: https://www.caterpillar.com/en/investors.html
  - type: PressReleases
    url: https://www.caterpillar.com/en/news.html
  - type: Careers
    url: https://www.caterpillar.com/en/careers.html
  - name: Features
    type: Features
    data:
      - name: Fleet Management
      - name: Asset Telematics
      - name: VisionLink
      - name: Cat Connect
      - name: Fuel Data
      - name: Utilization
      - name: Hours and Odometer
      - name: Location and Geofencing
      - name: Equipment Health
      - name: Service and Maintenance
      - name: Parts Catalog
      - name: Dealer Integrations
  - name: UseCases
    type: UseCases
    data:
      - name: Construction Site Fleet Tracking
      - name: Mining Fleet Optimization
      - name: Fuel Consumption Analytics
      - name: Predictive Maintenance
      - name: Dealer Parts Ordering
      - name: Telematics Integration
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
