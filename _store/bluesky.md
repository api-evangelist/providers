---
aid: bluesky
url: https://raw.githubusercontent.com/api-search/bluesky/refs/heads/main/apis.yml
apis:
  - aid: bluesky:bluesky-api
    name: Bluesky API
    tags:
      - Social Networks
    humanURL: https://docs.bsky.app/
    properties:
      - url: https://docs.bsky.app/
        type: Documentation
      - url: openapi/bluesky-openapi.yml
        type: OpenAPI
      - url: https://www.postman.com/api-evangelist/bluesky/collection/ubo2xuv/bluesky-api
        type: PostmanCollection
      - url: https://docs.bsky.app/docs/api/at-protocol-xrpc-api
        type: APIReference
      - url: https://docs.bsky.app/docs/category/http-reference
        type: HTTPReference
      - url: https://docs.bsky.app/docs/advanced-guides/api-directory
        type: APIDirectory
      - url: https://docs.bsky.app/docs/advanced-guides/oauth-client
        type: Authentication
      - url: https://docs.bsky.app/docs/advanced-guides/rate-limits
        type: RateLimits
      - url: https://docs.bsky.app/docs/advanced-guides/firehose
        type: Firehose
      - url: https://docs.bsky.app/docs/advanced-guides/moderation
        type: Moderation
      - url: https://docs.bsky.app/docs/advanced-guides/resolving-identities
        type: Identity
      - data:
          numberOfAPITags: 1
          numberOfAPIGetMethods: 93
          numberOfAPIOperations: 168
          numberOfAPIParameters: 2
          numberOfAPIProperties: 4
          numberOfAPIPutMethods: 0
          numberOfAPIPostMethods: 75
          numberOfAPIPatchMethods: 0
          numberOfAPIDeleteMethods: 0
          numberOfAPIOptionMethods: 0
        type: Summary
    description: The Bluesky API allows you to work programmatically with actors, feeds, graph, conversations, and other resources available for the the Bluesky app and social network.
  - aid: bluesky:bluesky-jetstream
    name: Bluesky Jetstream
    tags:
      - Events
      - Social Networks
      - Streaming
    humanURL: https://docs.bsky.app/blog/jetstream
    properties:
      - url: https://docs.bsky.app/blog/jetstream
        type: Documentation
      - url: https://github.com/bluesky-social/jetstream
        type: GitHubRepository
    description: Jetstream is a simplified JSON event stream for the AT Protocol that converts CBOR-encoded MST blocks from the firehose into JSON objects over WebSocket connections, making it easier to consume real-time Bluesky network events for building feed generators, bots, and search engines.
name: Bluesky
tags:
  - At-Protocol
  - Decentralized
  - Federated
  - Open-Source
  - Social Networks
  - Social-Media
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://docs.bsky.app/docs/starter-templates/bots
    name: Bots | Bluesky
    type: Bots
  - url: https://docs.bsky.app/docs/category/support
    name: Support | Bluesky
    type: Support
  - url: https://docs.bsky.app/blog
    name: Blog | Bluesky
    type: Blog
  - url: https://docs.bsky.app/docs/get-started
    name: Get Started | Bluesky
    type: GettingStarted
  - url: https://docs.bsky.app/docs/category/starter-templates
    name: Starter Templates | Bluesky
    type: Templates
  - url: https://docs.bsky.app/docs/category/tutorials
    name: Tutorials | Bluesky
    type: Tutorials
  - url: https://docs.bsky.app/docs/support/mailing-list
    name: Developer Mailing List | Bluesky
    type: Newsletter
  - url: https://www.postman.com/api-evangelist/bluesky/overview
    name: Postman Workspace
    type: PostmanWorkspace
    description: This is the dedicated workspace for the Bluesky API, storing collections and automations that can be used.
  - url: https://docs.bsky.app/docs/support/developer-guidelines
    name: Developer Guidelines | Bluesky
    type: Guidelines
  - url: https://docs.bsky.app/docs/starter-templates/custom-feeds
    name: Custom Feeds | Bluesky
    type: CustomFeeds
  - url: https://docs.bsky.app/docs/advanced-guides/atproto
    name: AT Protocol Guide | Bluesky
    type: Protocol
  - url: https://docs.bsky.app/docs/category/advanced-guides
    name: Advanced Guides | Bluesky
    type: AdvancedGuides
  - url: https://bsky.social/about/support/tos
    name: Terms of Service | Bluesky
    type: TermsOfService
  - url: https://bsky.social/about/support/privacy-policy
    name: Privacy Policy | Bluesky
    type: PrivacyPolicy
  - url: https://bsky.social/about/support/community-guidelines
    name: Community Guidelines | Bluesky
    type: CommunityGuidelines
  - url: https://atproto.com/sdks
    name: AT Protocol SDKs
    type: SDKs
  - url: https://atproto.com/guides/overview
    name: AT Protocol Overview
    type: ProtocolOverview
  - url: https://atproto.com/
    name: AT Protocol Specifications
    type: Specifications
  - url: https://github.com/bluesky-social
    name: Bluesky GitHub Organization
    type: GitHub Org
  - url: https://github.com/bluesky-social/atproto
    name: AT Protocol Reference Implementation
    type: GitHubRepository
  - url: https://github.com/bluesky-social/feed-generator
    name: Feed Generator Starter Kit
    type: GitHubRepository
  - url: https://github.com/bluesky-social/ozone
    name: Ozone Moderation Tool
    type: GitHubRepository
  - url: https://github.com/bluesky-social/atproto/discussions
    name: GitHub Discussions | AT Protocol
    type: Forum
  - data:
      numberOfAPITags: 2
      numberOfAPIPaths: 168
      numberOfAPISchema: null
      numberOfAPIGetMethods: 93
      numberOfAPIParameters: 2
      numberOfAPIProperties: 4
      numberOfAPIPutMethods: 0
      numberOfAPIPostMethods: 75
      numberOfAPIPatchMethods: 0
      numberOfAPIDeleteMethods: 0
      numberOfAPIOptionMethods: 0
    type: Summary
created: '2024-11-16'
modified: '2026-04-21'
position: Consumer
description: API for the Bluesky decentralized social network built on the AT Protocol.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: Bluesky Social PBC
    email: support@bsky.app
    url: https://bsky.social
specificationVersion: '0.19'
---
