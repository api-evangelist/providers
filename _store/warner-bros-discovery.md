---
aid: warner-bros-discovery
url: https://raw.githubusercontent.com/api-evangelist/warner-bros-discovery/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-03'
name: Warner Bros. Discovery
tags:
  - Entertainment
  - Media
  - Streaming
  - Content
  - Television
  - Film
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
description: Warner Bros. Discovery is a leading global media and entertainment company that creates and distributes the world's most differentiated and complete portfolio of branded content across television, film, and streaming. WBD operates the Max streaming platform, Warner Bros. film studio, HBO, CNN, Discovery, TNT, TBS, and many other brands. The company provides content partner APIs for media supply chain integration and maintains open source projects through its engineering teams.
apis:
  - aid: warner-bros-discovery:wbd-content-partner-api
    name: Warner Bros. Discovery Content Partner API
    tags:
      - Content Delivery
      - Media Supply Chain
      - Metadata
      - Media Ingest
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://partnerhub.warnermedia.com
    humanURL: https://partnerhub.warnermedia.com/specifications-and-guides
    properties:
      - url: https://partnerhub.warnermedia.com/specifications-and-guides
        type: Documentation
      - url: openapi/warner-bros-discovery-content-partner-openapi.yml
        type: OpenAPI
      - url: rules/warner-bros-discovery-rules.yml
        type: SpectralRules
      - url: capabilities/content-delivery.yaml
        type: NaftikoCapabilities
      - url: json-schema/warner-bros-discovery-content-schema.json
        type: JSONSchema
      - url: json-ld/warner-bros-discovery-context.jsonld
        type: JSONLDContext
      - url: vocabulary/warner-bros-discovery-vocabulary.yml
        type: Vocabulary
    description: The Warner Bros. Discovery Content Partner Hub provides technical specifications and APIs for content partners to deliver media assets to WBD's supply chain. Supports Automated Content Delivery (ACD) via Aspera P2P and MovieLabs Media Manifest Core (MMC) for technical and configuration metadata delivery.
common:
  - url: https://www.wbd.com/
    name: Warner Bros. Discovery
    type: Website
  - url: https://partnerhub.warnermedia.com/
    name: Content Partner Hub
    type: Portal
  - url: https://partnerhub.warnermedia.com/specifications-and-guides
    name: Technical Specifications and Guides
    type: Documentation
  - url: https://github.com/WarnerMedia
    name: WarnerMedia Open Source GitHub
    type: GitHubOrganization
  - url: https://github.com/warnerbros
    name: Warner Bros. GitHub Organization
    type: GitHubOrganization
  - url: https://www.max.com/
    name: Max Streaming Service
    type: Website
  - url: https://developer.wbd.com/
    name: Warner Bros. Discovery Developer Portal
    type: Portal
integrations:
  - AWS
  - Aspera (IBM)
  - Google Vertex AI
  - Mux
  - MovieLabs Digital Distribution Framework
  - BCP-47 Language Tags
solutions:
  - Content Delivery and Media Supply Chain
  - Streaming Platform (Max)
  - Content Metadata Management
  - Media Ingest and Distribution
openSource:
  - name: gimme-aws-creds
    description: Python CLI tool to obtain AWS credentials from Okta
    url: https://github.com/WarnerMedia/gimme-aws-creds
  - name: antiope-aws-module
    description: AWS inventory and security tooling
    url: https://github.com/WarnerMedia/antiope-aws-module
  - name: react-static
    description: Static site generator for React
    url: https://github.com/warnerbros/react-static
  - name: mux.js
    description: JavaScript library for video segment parsing
    url: https://github.com/warnerbros/mux.js
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
