---
aid: fabric-origin
name: Fabric Origin
description: Fabric Origin (formerly IVA) is the entertainment data platform powering content discovery experiences for movies, television, games, and trailers. Fabric Origin offers comprehensive entertainment data solutions including metadata, images, trailers, TV listings, and celebrity information through a family of REST APIs. With 30 percent more coverage than other providers and tailored products for every stage of the release cycle, Fabric Origin is an affordable, scalable solution trusted by startups and Fortune 50 companies alike.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
position: Consumer
access: 3rd-Party
tags:
  - Entertainment
  - Movies
  - Television
  - Games
  - Trailers
  - Metadata
apis:
  - aid: fabric-origin:entertainment-api
    name: Fabric Origin Entertainment API
    description: The Entertainment API ingests and serves metadata for movies, television shows, and games, including identifiers used to retrieve associated videos and images from sibling APIs. Responses are available in JSON, XML, CSV, and HTML formats via Accept headers or the format query parameter.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://knowledgebase.fabricdata.com/origin/apis-all/
    baseURL: https://ee.iva-api.com/api/
    tags:
      - Entertainment
      - Metadata
      - Movies
      - Television
      - Games
    properties:
      - type: Documentation
        url: https://knowledgebase.fabricdata.com/origin/apis-all/
      - type: Knowledge Base
        url: https://knowledgebase.fabricdata.com/origin
  - aid: fabric-origin:celebrity-api
    name: Fabric Origin Celebrity API
    description: The Celebrity API serves metadata about celebrities, including actors, directors, and other entertainment industry figures, with cross references to titles served by the Entertainment API.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://knowledgebase.fabricdata.com/origin/apis-all/
    baseURL: https://ee.iva-api.com/api/
    tags:
      - Celebrities
      - People
      - Metadata
    properties:
      - type: Documentation
        url: https://knowledgebase.fabricdata.com/origin/apis-all/
  - aid: fabric-origin:video-api
    name: Fabric Origin Video API
    description: The Video API generates playable links for trailers and other video assets using video identifiers returned from the Entertainment API, allowing customers to embed Fabric Origin video content into their content discovery experiences.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://knowledgebase.fabricdata.com/origin/apis-all/
    baseURL: https://ee.iva-api.com/api/
    tags:
      - Video
      - Trailers
      - Streaming
    properties:
      - type: Documentation
        url: https://knowledgebase.fabricdata.com/origin/apis-all/
  - aid: fabric-origin:image-api
    name: Fabric Origin Image API
    description: The Image API provides access to images hosted on Fabric Origin's servers, including posters, stills, and promotional artwork referenced from the Entertainment and Celebrity APIs. Customers are encouraged to host and serve images from their own infrastructure for production use.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://knowledgebase.fabricdata.com/origin/apis-all/
    baseURL: https://ee.iva-api.com/api/
    tags:
      - Images
      - Posters
      - Artwork
    properties:
      - type: Documentation
        url: https://knowledgebase.fabricdata.com/origin/apis-all/
  - aid: fabric-origin:common-data-api
    name: Fabric Origin Common Data API
    description: The Common Data API exposes reference data used across the Fabric Origin product family, including country codes, image type lookups, and video type lookups required when working with the Entertainment, Celebrity, Video, and Image APIs.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://knowledgebase.fabricdata.com/origin/apis-all/
    baseURL: https://ee.iva-api.com/api/
    tags:
      - Reference Data
      - Lookups
    properties:
      - type: Documentation
        url: https://knowledgebase.fabricdata.com/origin/apis-all/
common:
  - type: Website
    url: https://www.fabricdata.com/
  - type: Knowledge Base
    url: https://knowledgebase.fabricdata.com/origin
  - type: Solutions
    url: https://knowledgebase.fabricdata.com/origin/solutions
  - type: Developer Portal
    url: https://developer.origin.fabricdata.com/portal/login
  - type: Documentation
    url: https://knowledgebase.fabricdata.com/origin/apis-all/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
