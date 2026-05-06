---
aid: roku
url: https://github.com/api-evangelist/roku
name: Roku
type: Index
image: https://image.roku.com/ImageServer/global/favicons/favicon-32x32.png
tags:
  - Streaming
  - Television
  - Media
  - Entertainment
  - Connected TV
  - Consumer Electronics
description: Roku is the leading TV streaming platform in the U.S., Canada, and Mexico, offering a comprehensive operating system that powers smart TVs, streaming players, and audio devices. Roku provides a robust developer program for building channel apps, monetizing through Roku Pay, integrating analytics, and controlling devices via the External Control Protocol. The platform supports both BrightScript and SceneGraph frameworks for app development, and the Nabu Cloud developer cloud for managing remote test devices and channel builds.
created: '2026-05-04'
modified: '2026-05-05'
specificationVersion: '0.19'
apis:
  - aid: roku:brightscript
    name: Roku BrightScript SDK
    humanURL: https://developer.roku.com/docs/references/brightscript/component-reference.md
    description: BrightScript is Roku's scripting language used to build apps for the Roku platform. The SDK provides a comprehensive component library with over 100 built-in objects covering UI, networking, media playback, and device interaction. BrightScript is a programming language and on-device runtime, not a network API.
    tags:
      - SDK
      - BrightScript
      - Channel Development
    properties:
      - type: Documentation
        url: https://developer.roku.com/docs/references/brightscript/component-reference.md
      - type: APIReference
        url: https://developer.roku.com/docs/references/brightscript/component-reference.md
  - aid: roku:scenegraph
    name: Roku SceneGraph
    humanURL: https://developer.roku.com/docs/developer-program/core-concepts/scenegraph-overview.md
    description: SceneGraph is Roku's XML-based declarative UI framework for building rich, performant channel applications. It provides node components, animations, and a scene-based architecture. SceneGraph is an on-device UI framework, not a network API.
    tags:
      - UI Framework
      - SceneGraph
      - Channel Development
    properties:
      - type: Documentation
        url: https://developer.roku.com/docs/developer-program/core-concepts/scenegraph-overview.md
      - type: APIReference
        url: https://developer.roku.com/docs/references/scenegraph/component-reference.md
  - aid: roku:external-control-protocol
    name: Roku External Control Protocol (ECP)
    humanURL: https://developer.roku.com/docs/developer-program/dev-tools/external-control-api.md
    description: The External Control Protocol (ECP) is an HTTP-based API exposed on port 8060 of every Roku device on the local network. It enables third-party applications, mobile remote-control apps, automated test systems, and home-automation hubs to discover devices via SSDP, inject simulated remote-control key presses, launch installed apps with deep-link parameters, query device state, and retrieve developer-mode diagnostics.
    tags:
      - REST
      - HTTP
      - Device Control
      - LAN
    properties:
      - type: Documentation
        url: https://developer.roku.com/docs/developer-program/dev-tools/external-control-api.md
      - type: APIReference
        url: https://developer.roku.com/docs/developer-program/dev-tools/external-control-api.md
      - type: OpenAPI
        url: openapi/roku-external-control-protocol.yaml
      - type: JSONSchema
        url: json-schema/external-control-protocol-active-app-schema.json
        title: Active App Schema
      - type: JSONSchema
        url: json-schema/external-control-protocol-app-list-schema.json
        title: App List Schema
      - type: JSONSchema
        url: json-schema/external-control-protocol-app-schema.json
        title: App Schema
      - type: JSONSchema
        url: json-schema/external-control-protocol-device-info-schema.json
        title: Device Info Schema
      - type: JSONSchema
        url: json-schema/external-control-protocol-media-player-schema.json
        title: Media Player Schema
      - type: JSONStructure
        url: json-structure/external-control-protocol-device-info-structure.json
        title: Device Info Structure
      - type: JSONStructure
        url: json-structure/external-control-protocol-app-structure.json
        title: App Structure
      - type: JSONStructure
        url: json-structure/external-control-protocol-app-list-structure.json
        title: App List Structure
      - type: JSONStructure
        url: json-structure/external-control-protocol-active-app-structure.json
        title: Active App Structure
      - type: JSONStructure
        url: json-structure/external-control-protocol-media-player-structure.json
        title: Media Player Structure
      - type: JSON-LD
        url: json-ld/roku-external-control-protocol-context.jsonld
      - type: Example
        url: examples/external-control-protocol-query-device-info-example.json
        title: Query Device Info Example
      - type: Example
        url: examples/external-control-protocol-query-apps-example.json
        title: Query Apps Example
      - type: Example
        url: examples/external-control-protocol-launch-app-example.json
        title: Launch App Example
  - aid: roku:pay
    name: Roku Pay Web Services
    humanURL: https://developer.roku.com/docs/developer-program/roku-pay/overview.md
    description: Roku Pay Web Services provide server-to-server APIs for billing, subscription management, transaction validation, and entitlement checks for monetized Roku channels. Channels query these endpoints from their authentication backends to verify entitlements, issue refunds, adjust billing cycles, and grant service credits.
    tags:
      - Billing
      - Payments
      - Subscriptions
      - Monetization
    properties:
      - type: Documentation
        url: https://developer.roku.com/docs/developer-program/roku-pay/overview.md
      - type: APIReference
        url: https://developer.roku.com/dev/docs/roku-web-service
      - type: OpenAPI
        url: openapi/roku-pay-web-services.yaml
      - type: JSONSchema
        url: json-schema/pay-web-services-transaction-validation-schema.json
        title: Transaction Validation Schema
      - type: JSONSchema
        url: json-schema/pay-web-services-refund-validation-schema.json
        title: Refund Validation Schema
      - type: JSONSchema
        url: json-schema/pay-web-services-cancel-subscription-request-schema.json
        title: Cancel Subscription Request Schema
      - type: JSONSchema
        url: json-schema/pay-web-services-refund-subscription-request-schema.json
        title: Refund Subscription Request Schema
      - type: JSONSchema
        url: json-schema/pay-web-services-update-bill-cycle-request-schema.json
        title: Update Bill Cycle Request Schema
      - type: JSONSchema
        url: json-schema/pay-web-services-issue-credit-request-schema.json
        title: Issue Credit Request Schema
      - type: JSONSchema
        url: json-schema/pay-web-services-subscription-result-schema.json
        title: Subscription Result Schema
      - type: JSONStructure
        url: json-structure/pay-web-services-transaction-validation-structure.json
        title: Transaction Validation Structure
      - type: JSONStructure
        url: json-structure/pay-web-services-refund-validation-structure.json
        title: Refund Validation Structure
      - type: JSONStructure
        url: json-structure/pay-web-services-subscription-result-structure.json
        title: Subscription Result Structure
      - type: JSON-LD
        url: json-ld/roku-pay-web-services-context.jsonld
      - type: Example
        url: examples/pay-web-services-validate-transaction-example.json
        title: Validate Transaction Example
      - type: Example
        url: examples/pay-web-services-cancel-subscription-example.json
        title: Cancel Subscription Example
  - aid: roku:nabu-cloud
    name: Roku Nabu Cloud
    humanURL: https://github.com/rokudev/dev-doc/tree/v2.0/reference/nabu_cloud
    description: Nabu Cloud is Roku's developer cloud platform for managing remote test devices, snapshots, builds, projects, organisations, groups, and personal access tokens. It provides REST APIs (and an AsyncAPI streaming endpoint) for orchestrating remote Roku test devices and CI/CD workflows. The OpenAPI specification is published in the Roku dev-doc repository.
    tags:
      - REST
      - Developer Cloud
      - Test Devices
      - CI CD
    properties:
      - type: Documentation
        url: https://github.com/rokudev/dev-doc/tree/v2.0/reference/nabu_cloud
      - type: OpenAPI
        url: openapi/roku-nabu-cloud.yaml
      - type: JSON-LD
        url: json-ld/roku-nabu-cloud-context.jsonld
      - type: Example
        url: examples/nabu-cloud-list-devices-example.json
        title: List Devices Example
      - type: Example
        url: examples/nabu-cloud-create-device-example.json
        title: Create Device Example
  - aid: roku:search-feed
    name: Roku Search Feed
    humanURL: https://github.com/rokudev/search-feed-json
    description: Roku Search Feed is a JSON feed format that publishers ingest to expose their catalog to Roku Search. The feed provides movies, series, episodes, short-form videos, TV specials, and live feeds with localized titles, descriptions, ratings, content links, and external IDs.
    tags:
      - Feed
      - Search
      - Content Catalog
    properties:
      - type: Documentation
        url: https://github.com/rokudev/search-feed-json
      - type: JSONSchema
        url: json-schema/search-feed-schema.json
        title: Search Feed Schema
      - type: JSON-LD
        url: json-ld/roku-search-feed-context.jsonld
      - type: Example
        url: examples/roku-search-feed-simple-example.json
        title: Simple Search Feed Example
      - type: Example
        url: examples/roku-search-feed-advanced-example.json
        title: Advanced Search Feed Example
  - aid: roku:direct-publisher-feed
    name: Roku Direct Publisher Feed
    humanURL: https://github.com/rokudev/feed-specifications
    description: Roku Direct Publisher (RDP) feed is a JSON feed specification that allows non-technical publishers to populate channels by hosting a structured catalog of short-form videos, movies, series, episodes, and live feeds. Roku ingests the feed on a schedule and renders the channel UI automatically.
    tags:
      - Feed
      - Direct Publisher
      - Content Catalog
    properties:
      - type: Documentation
        url: https://github.com/rokudev/feed-specifications/blob/master/direct-publisher-feed-specification.md
      - type: APIReference
        url: https://github.com/rokudev/feed-specifications
      - type: Example
        url: examples/roku-direct-publisher-feed-example.json
        title: Direct Publisher Feed Example
  - aid: roku:analytics
    name: Roku Analytics
    humanURL: https://developer.roku.com/docs/developer-program/marketing/roku-analytics.md
    description: Roku Analytics provides performance reporting, audience metrics, and engagement data for Roku channel publishers. Reports are accessed through the Roku Developer Dashboard rather than a public REST API.
    tags:
      - Analytics
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.roku.com/docs/developer-program/marketing/roku-analytics.md
  - aid: roku:authentication
    name: Roku Authentication Framework
    humanURL: https://developer.roku.com/docs/developer-program/authentication/authentication-overview.md
    description: APIs and patterns for implementing user sign-in and authentication within Roku channels, including device-linking ("on-device authentication") and OAuth-style flows. The framework is implemented in BrightScript on the device; the publisher's authentication backend is custom-built.
    tags:
      - Authentication
      - OAuth
    properties:
      - type: Documentation
        url: https://developer.roku.com/docs/developer-program/authentication/authentication-overview.md
      - type: CodeExamples
        url: https://github.com/rokudev/on-device-authentication
        title: On-Device Authentication Sample
common:
  - type: Website
    url: https://www.roku.com
  - type: DeveloperPortal
    url: https://developer.roku.com
  - type: Documentation
    url: https://developer.roku.com/docs
  - type: GettingStarted
    url: https://developer.roku.com/en-gb/docs/get-started/getting-started.md
  - type: Courses
    url: https://developer.roku.com/en-gb/videos/courses
  - type: SDK
    url: https://developer.roku.com/en-gb/docs/developer-program/dev-tools/dev-tools-overview.md
  - type: Support
    url: https://developer.roku.com/en-gb/support
  - type: Blog
    url: https://blog.roku.com
  - type: GitHubOrganization
    url: https://github.com/rokudev
  - type: GitHubRepository
    url: https://github.com/rokudev/dev-doc
    title: Roku Developer Documentation
  - type: GitHubRepository
    url: https://github.com/rokudev/samples
    title: Roku Channel Samples
  - type: GitHubRepository
    url: https://github.com/rokudev/roku-deploy
    title: roku-deploy npm Package
  - type: GitHubRepository
    url: https://github.com/rokudev/roku-debug
    title: BrightScript Debug Protocol Wrapper
  - type: GitHubRepository
    url: https://github.com/rokudev/vscode-brightscript-language
    title: VSCode BrightScript Extension
  - type: Tools
    url: https://github.com/rokudev/vscode-brightscript-language
    title: BrightScript VSCode Extension
  - type: Tools
    url: https://github.com/rokudev/roku-deploy
    title: roku-deploy CLI (npm)
  - type: Tools
    url: https://github.com/rokudev/automated-channel-testing
    title: Roku Automated Channel Testing (Selenium WebDriver)
  - type: Tools
    url: https://github.com/rokudev/unit-testing-framework
    title: Roku Unit Testing Framework
  - type: Tools
    url: https://github.com/rokudev/remote-debugger
    title: Python BrightScript Remote Debugger
  - type: CodeExamples
    url: https://github.com/rokudev/samples
    title: Roku Sample Channels
  - type: CodeExamples
    url: https://github.com/rokudev/hello-world
    title: Hello World Channel
  - type: CodeExamples
    url: https://github.com/rokudev/scenegraph-master-sample
    title: SceneGraph Master Sample
  - type: CodeExamples
    url: https://github.com/rokudev/hero-grid-channel
    title: Hero Grid Channel Sample
  - type: CodeExamples
    url: https://github.com/rokudev/standard-dialog-framework
    title: Standard Dialog Framework Sample
  - type: SpectralRules
    url: rules/roku-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/channel-operations.yaml
    title: Roku Channel Operations Workflow
  - type: NaftikoCapability
    url: capabilities/shared/external-control-protocol.yaml
    title: ECP Shared Capability
  - type: NaftikoCapability
    url: capabilities/shared/pay-web-services.yaml
    title: Roku Pay Shared Capability
  - type: NaftikoCapability
    url: capabilities/shared/nabu-cloud.yaml
    title: Nabu Cloud Shared Capability
  - type: Vocabulary
    url: vocabulary/roku-vocabulary.yaml
  - type: TermsOfService
    url: https://developer.roku.com/en-gb/docs/developer-program/agreements/registered-developer-agreement.md
  - type: PrivacyPolicy
    url: https://docs.roku.com/published/userprivacypolicy/en/us
  - data:
      - name: Channel Development
        description: BrightScript and SceneGraph frameworks for building Roku TV streaming channel applications.
      - name: Device Control
        description: Local-network HTTP API (ECP) for discovery, key injection, app launching, and diagnostics.
      - name: Roku Pay
        description: Server-to-server billing APIs for transaction validation, refunds, and subscription management.
      - name: Direct Publisher
        description: JSON feed ingestion path for non-technical publishers to populate Roku channels.
      - name: Search Feed
        description: Catalog feed ingestion that surfaces publisher content in Roku Search.
      - name: Nabu Cloud
        description: Roku's developer cloud for managing remote test devices, snapshots, and builds.
      - name: Channel Store Monetization
        description: Transactional and subscription monetization through ChannelStore and roChannelStore components.
      - name: Advertising Framework
        description: Roku Advertising Framework (RAF) for monetizing video content with ads.
    type: Features
  - data:
      - name: Streaming Channel Development
        description: Build full-screen TV streaming channels with BrightScript/SceneGraph and ship to the Roku Channel Store.
      - name: Subscription Video On Demand
        description: Monetize video content with recurring subscriptions managed by Roku Pay.
      - name: Transactional Video On Demand
        description: Monetize individual movie/episode purchases via the Channel Store and Roku Pay.
      - name: Free Ad-Supported Streaming TV
        description: Free streaming with the Roku Advertising Framework.
      - name: TV Remote and Home Automation
        description: Build mobile or hub-based remote-control apps that drive Roku devices via ECP.
      - name: Automated Channel Testing
        description: Run channel certification tests on remote Roku test devices in Nabu Cloud.
    type: UseCases
  - data:
      - name: Visual Studio Code
        description: BrightScript language extension for VSCode with debugging and side-loading.
      - name: Selenium WebDriver
        description: WebDriver-based automated channel testing.
      - name: npm
        description: roku-deploy and roku-debug published as npm packages.
      - name: Sublime Text
        description: BrightScript syntax-highlighting package.
      - name: GitHub
        description: Source-of-truth for Roku-published samples, tooling, and the dev-doc OpenAPI spec.
    type: Integrations
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
---
