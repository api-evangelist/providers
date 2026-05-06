---
aid: dropbox
url: https://raw.githubusercontent.com/api-evangelist/dropbox/refs/heads/main/apis.yml
apis:
  - aid: dropbox:dropbox-api
    name: Dropbox API
    tags:
      - Documents
      - Storage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.dropboxapi.com
    humanURL: https://www.dropbox.com/developers/documentation/http/overview
    properties:
      - url: https://www.dropbox.com/developers/documentation/http/overview
        type: Documentation
      - url: openapi/dropbox-openapi-original.yml
        type: OpenAPI
    description: Dropbox is a file hosting service operated by the American company Dropbox, Inc., headquartered in San Francisco, California, U.S. that offers cloud storage, file synchronization, personal cloud, and client software.
  - aid: dropbox:dropbox-sign-api
    name: Dropbox Sign API
    tags:
      - Signatures
      - Documents
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hellosign.com
    humanURL: https://developers.hellosign.com/
    properties:
      - url: https://developers.hellosign.com/
        type: Documentation
      - url: https://developers.hellosign.com/docs/sdks/overview/
        type: SDKs
      - url: https://developers.hellosign.com/api/quickstart/
        type: Quickstart
      - url: openapi/dropbox-sign-openapi-original.yml
        type: OpenAPI
    description: The Dropbox Sign API offers a reliable, flexible set of eSignature tools that can be used to power digital agreements and turn slow, outdated business processes into a competitive advantage. With a broad range of highly-configurable features, the Dropbox Sign API empowers you to build secure signing experiences and document workflows that delight your users.
name: Dropbox
tags:
  - Documents
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://www.dropbox.com/developers
    type: Portal
  - url: https://www.dropbox.com/developers/support
    type: Support
  - url: https://www.dropbox.com/plans
    type: Plans
  - url: https://www.dropbox.com/register
    type: Signup
  - url: https://www.dropbox.com/developers/reference
    type: Guides
  - url: https://github.com/dropbox/dropbox-api-spec/commits/main
    type: Change Log
  - url: https://github.com/dropbox
    type: GitHub Org
  - url: https://www.dropbox.com/developers/documentation/communitysdks
    type: Community SDKs
  - url: https://blog.dropbox.com/
    type: Blog
  - type: Features
    data:
      - Standard at $15/user/mo with 3 TB pooled storage
      - Advanced at $24/user/mo with 15 TB and end-to-end encryption
      - 180-day (Standard) or 1-year (Advanced) deleted-file recovery
      - 100 GB Transfer for large file delivery
      - Dropbox Sign integrated PDF signatures
      - REST API at api.dropboxapi.com/2/
      - Default 1,200 req/min per app rate limit
      - OAuth 2.0 with team and individual scopes
      - Webhooks for file change notifications
      - List folder with cursor-based pagination
      - Paper for collaborative documents
      - Capture for screen recording
      - Replay for video review
      - Tiered admin (Advanced)
      - SSO, SCIM provisioning (Advanced)
      - Compliance tracking and EKM (Advanced)
    sources:
      - https://www.dropbox.com/plans
    updated: '2026-05-04'
created: '2024-06-07T00:00:00.000Z'
modified: '2026-05-04'
description: Dropbox is a file hosting service operated by the American company Dropbox, Inc., headquartered in San Francisco, California, U.S. that offers cloud storage, file synchronization, personal cloud, and client software.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: kin@apievangelist.com
specificationVersion: '0.19'
type: Contract
position: Consuming
access: 3rd-Party
---
