---
aid: camtasia
name: Camtasia
url: https://raw.githubusercontent.com/api-evangelist/camtasia/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Screen Recording
  - Video Editing
  - Tutorial Creation
  - E-Learning
  - Screencast
  - oEmbed
  - SDK
access: 3rd-Party
created: '2024-01-15'
modified: '2026-04-23'
position: Provider
specificationVersion: '0.19'
description: Camtasia is a screen recording and video editing software by TechSmith that allows users to create professional videos, tutorials, and presentations with built-in editing tools, effects, and media assets. Camtasia itself does not publish a public REST API, but it integrates tightly with TechSmith Screencast for sharing, and TechSmith publishes a public Screencast oEmbed API plus the Camtasia Screen Recorder SDK for embedding recording capabilities into third-party applications.
apis:
  - aid: camtasia:screencast-oembed-api
    name: TechSmith Screencast oEmbed API
    description: Public oEmbed API for TechSmith Screencast (app.screencast.com), the cloud destination where Camtasia videos and images are shared. The oEmbed endpoint returns embed HTML, thumbnail, and metadata for a given Screencast content URL, letting content platforms and CMSes render Screencast shares inline the same way they render YouTube or Vimeo. Documentation is maintained in a public GitHub repository.
    humanURL: https://github.com/TechSmith/screencast-public-api-docs
    baseURL: https://app.screencast.com/services/oembed
    tags:
      - oEmbed
      - Screencast
      - Embedding
      - Video
    properties:
      - type: Documentation
        url: https://github.com/TechSmith/screencast-public-api-docs/blob/main/sections/oembed.md
      - type: Repository
        url: https://github.com/TechSmith/screencast-public-api-docs
      - type: JSON-LD
        url: json-ld/camtasia-context.jsonld
  - aid: camtasia:camtasia-screen-recorder-sdk
    name: Camtasia Screen Recorder SDK
    description: A developer toolkit from TechSmith that lets developers embed reliable high-quality screen, webcam, and audio recording into their own applications. The SDK exposes APIs to configure, start, stop, and automate recording workflows, and to capture cursor and system audio alongside the screen.
    humanURL: https://www.techsmith.com/camtasia.html
    tags:
      - SDK
      - Screen Recording
      - Embedded
    properties:
      - type: ProductPage
        url: https://www.techsmith.com/camtasia.html
common:
  - type: Website
    url: https://www.techsmith.com/camtasia.html
  - type: Screencast
    url: https://www.techsmith.com/screencast/
  - type: GettingStarted
    url: https://www.techsmith.com/learn/camtasia/
  - type: Blog
    url: https://www.techsmith.com/blog/category/camtasia/
  - type: Support
    url: https://support.techsmith.com
  - type: PublicAPIRepository
    url: https://github.com/TechSmith/screencast-public-api-docs
  - type: TermsOfService
    url: https://www.techsmith.com/terms.html
  - type: PrivacyPolicy
    url: https://www.techsmith.com/privacy.html
  - type: JSON-LD
    url: json-ld/camtasia-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
