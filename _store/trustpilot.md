---
aid: trustpilot
url: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/apis.yml
apis:
- aid: trustpilot:trustpilot-business-api
  name: Trustpilot Business API
  tags:
  - Business Profiles
  - Consumer Reviews
  - Reviews
  - Trust
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.trustpilot.com/v1
  humanURL: https://developers.trustpilot.com/
  properties:
  - url: https://developers.trustpilot.com/
    type: Documentation
  - url: https://developers.trustpilot.com/authentication
    type: Authentication
  - url: https://developers.trustpilot.com/business-units-api
    type: Documentation
  - url: https://developers.trustpilot.com/reviews-api
    type: Documentation
  description: The Trustpilot Business API provides programmatic access to business profile data, reviews, and review management capabilities on the Trustpilot platform. Businesses can retrieve their profile information, access and respond to consumer reviews, manage review invitations, and retrieve aggregate review statistics and star ratings. The API supports OAuth 2.0 authentication and enables integration of Trustpilot review data into business dashboards, CRM systems, and customer experience workflows.
- aid: trustpilot:trustpilot-invitation-api
  name: Trustpilot Invitation API
  tags:
  - Consumer Reviews
  - Email
  - Invitations
  - Reviews
  - Trust
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.trustpilot.com/v1
  humanURL: https://developers.trustpilot.com/invitation-api
  properties:
  - url: https://developers.trustpilot.com/invitation-api
    type: Documentation
  - url: https://developers.trustpilot.com/authentication
    type: Authentication
  description: The Trustpilot Invitation API allows businesses to programmatically send review invitations to their customers via email or SMS after a transaction or service interaction. It supports creating and managing invitation templates, scheduling bulk invitation sends, and tracking invitation delivery and response rates. The API integrates with e-commerce platforms and order management systems to automate post-purchase review collection at scale.
- aid: trustpilot:trustpilot-consumer-api
  name: Trustpilot Consumer API
  tags:
  - Consumer Reviews
  - Reviews
  - Trust
  - Widgets
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.trustpilot.com/v1
  humanURL: https://developers.trustpilot.com/consumer-api
  properties:
  - url: https://developers.trustpilot.com/consumer-api
    type: Documentation
  - url: https://developers.trustpilot.com/authentication
    type: Authentication
  description: The Trustpilot Consumer API provides public read access to business profiles, reviews, categories, and star ratings published on Trustpilot. Developers can retrieve lists of reviews for a business unit, search for business profiles by name or domain, and fetch aggregate rating data including TrustScore and review counts.
name: Trustpilot
tags:
- Consumer Reviews
- Reviews
- Trust
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Trustpilot is a global consumer review platform that connects businesses with their customers to build trust through transparent, verified reviews. Founded in 2007, Trustpilot hosts hundreds of millions of reviews across millions of businesses worldwide. The platform offers business APIs that allow companies to collect, manage, and display reviews programmatically, integrate review data into their own systems, and automate invitation workflows to gather customer feedback at scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

