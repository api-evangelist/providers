---
aid: dolby
name: Dolby
description: Dolby Laboratories is a leading technology company specializing in audio and video. The Dolby developer platform (dolby.io / Dolby OptiView) provides APIs and SDKs for media processing, real-time streaming, video playback, and ad delivery. Dolby is responsible for technologies including Dolby Atmos, Dolby Vision, and Dolby Digital.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Audio
  - Video
  - Streaming
  - Media
  - Real-Time
url: https://raw.githubusercontent.com/api-evangelist/dolby/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
access: 3rd-Party
position: Consumer
apis:
  - aid: dolby:optiview-player
    name: Dolby OptiView Player
    description: Deploy cutting-edge video playback experiences across web, mobile, and connected devices using the OptiView Player SDK and APIs.
    humanURL: https://optiview.dolby.com/docs/player/
    tags:
      - Video
      - Player
      - SDK
    properties:
      - type: Documentation
        url: https://optiview.dolby.com/docs/player/
  - aid: dolby:optiview-live
    name: Dolby OptiView Live
    description: Live streaming solution providing consistent playback across audience sizes, with low-latency ingest and global delivery.
    humanURL: https://optiview.dolby.com/docs/live/
    tags:
      - Streaming
      - Live
      - Video
    properties:
      - type: Documentation
        url: https://optiview.dolby.com/docs/live/
  - aid: dolby:real-time-millicast
    name: Dolby Real-time Streaming (Millicast)
    description: Sub-second, interactive-latency streaming powered by the Millicast platform for two-way audio and video at scale.
    humanURL: https://optiview.dolby.com/docs/real-time/
    tags:
      - Real-Time
      - WebRTC
      - Streaming
    properties:
      - type: Documentation
        url: https://optiview.dolby.com/docs/real-time/
      - type: Legacy Docs
        url: https://docs.millicast.com
  - aid: dolby:optiview-ads
    name: Dolby OptiView Ads
    description: Ad delivery platform for high-quality video advertising experiences across streaming environments.
    humanURL: https://optiview.dolby.com/docs/ads/
    tags:
      - Advertising
      - Video
    properties:
      - type: Documentation
        url: https://optiview.dolby.com/docs/ads/
  - aid: dolby:optiview-ad-engine
    name: Dolby OptiView Ad Engine
    description: Serverless conformance service that transforms ads to match content specifications for seamless playback.
    humanURL: https://optiview.dolby.com/docs/ad-engine/
    tags:
      - Advertising
      - Transformation
    properties:
      - type: Documentation
        url: https://optiview.dolby.com/docs/ad-engine/
common:
  - type: Website
    url: https://dolby.io
  - type: Documentation
    url: https://optiview.dolby.com/docs/
  - type: Company
    url: https://www.dolby.com
  - type: Developer
    url: https://dolby.io/developers/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
