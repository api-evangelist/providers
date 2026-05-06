---
name: Ant Media
description: Ant Media Server is a scalable, open-source media server for ultra-low latency live streaming and WebRTC-based video applications. It supports WebRTC, RTMP, RTSP, SRT, HLS, and CMAF protocols, enabling developers to build real-time video applications with sub-second latency. Available in Community (open-source) and Enterprise editions with adaptive bitrate streaming, cloud auto-scaling, video recording, and REST API management.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/ant-media/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-19'
specificationVersion: '0.16'
tags:
  - Broadcasting
  - Live Streaming
  - Media
  - Streaming
  - Video
  - WebRTC
apis:
  - name: Ant Media Server REST API
    description: The Ant Media Server REST API provides programmatic access to all streaming server management functions including stream management, broadcast configuration, recording control, token authentication, cluster management, and server settings. Supports RTMP ingest, WebRTC publish/play, HLS delivery, and adaptive bitrate configuration.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://antmedia.io/rest/
    baseURL: https://your-ant-media-server:5080/WebRTCAppEE/rest/v2/
    tags:
      - Broadcasting
      - HLS
      - Live Streaming
      - Media Server
      - RTMP
      - Streaming
      - Video
      - WebRTC
    properties:
      - type: Documentation
        url: https://antmedia.io/rest/
      - type: GettingStarted
        url: https://antmedia.io/docs/guides/getting-started/quick-start/
      - type: Authentication
        url: https://antmedia.io/docs/guides/developer-sdk-and-api/rest-api-guide/
      - type: GitHubRepository
        url: https://github.com/ant-media/Ant-Media-Server
      - type: SDK
        url: https://antmedia.io/docs/guides/developer-sdk-and-api/sdk-integration/
        title: JavaScript SDK
      - type: SDK
        url: https://antmedia.io/docs/guides/developer-sdk-and-api/sdk-integration/
        title: Android SDK
      - type: SDK
        url: https://antmedia.io/docs/guides/developer-sdk-and-api/sdk-integration/
        title: iOS SDK
    contact:
      - FN: Ant Media Support
        url: https://antmedia.io/contact/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://antmedia.io
  - type: Documentation
    url: https://antmedia.io/docs/
  - type: GettingStarted
    url: https://antmedia.io/docs/guides/getting-started/quick-start/
  - type: Pricing
    url: https://antmedia.io/pricing/
  - type: Blog
    url: https://antmedia.io/blog/
  - type: GitHubOrganization
    url: https://github.com/ant-media
  - type: GitHubRepository
    url: https://github.com/ant-media/Ant-Media-Server
  - type: Support
    url: https://antmedia.io/support/
  - type: TermsOfService
    url: https://antmedia.io/terms/
  - type: PrivacyPolicy
    url: https://antmedia.io/privacy-policy/
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ant-media/refs/heads/main/json-schema/ant-media-broadcast-schema.json
    title: Broadcast Schema
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ant-media/refs/heads/main/vocabulary/ant-media-vocabulary.yaml
  - type: Features
    data:
      - name: Ultra-Low Latency WebRTC Streaming
        description: Achieve sub-500ms latency with WebRTC-based publish and play, enabling real-time interactive video applications like auctions, gaming, and telehealth.
      - name: Multi-Protocol Support
        description: Ingest and deliver streams via RTMP, RTSP, SRT, WebRTC, HLS, CMAF, and LL-HLS, supporting a wide range of encoders and players.
      - name: Adaptive Bitrate Streaming
        description: Automatically transcode streams to multiple bitrate/resolution ladders and deliver the optimal quality based on viewer bandwidth.
      - name: Video Recording and VoD
        description: Record live streams to MP4 or HLS on local disk or cloud storage, creating video-on-demand assets from live broadcasts automatically.
      - name: Cluster and Auto-Scaling
        description: Deploy Ant Media Server in horizontal cluster mode with auto-scaling on AWS, Azure, GCP, and Alibaba Cloud for high-concurrency events.
      - name: REST API Management
        description: Full programmatic control of streams, broadcasts, conferences, and server settings via a comprehensive REST API.
  - type: UseCases
    data:
      - name: Telehealth and Remote Consultations
        description: Enable HIPAA-compliant real-time video consultations between patients and healthcare providers with sub-second latency.
      - name: Live E-Commerce and Auctions
        description: Power interactive live shopping experiences and real-time bidding platforms with low-latency video and chat.
      - name: E-Learning and Virtual Classrooms
        description: Deliver interactive live lectures, webinars, and virtual classrooms with two-way video and screen sharing.
      - name: Gaming and Esports Broadcasting
        description: Broadcast gaming sessions and esports events with RTMP ingest from OBS and HLS/WebRTC delivery to viewers at scale.
      - name: Video Surveillance
        description: Ingest RTSP streams from IP cameras and provide browser-based WebRTC viewing with recording and motion detection.
  - type: Integrations
    data:
      - name: OBS Studio
        description: Ingest live streams from OBS Studio via RTMP for broadcast to WebRTC, HLS, or RTSP viewers through Ant Media Server.
      - name: AWS / Azure / GCP
        description: Deploy Ant Media Server clusters with auto-scaling on major cloud platforms using marketplace images and SDK integrations.
      - name: Zoom
        description: Integrate Zoom meetings and webinars with Ant Media Server for re-broadcasting to larger streaming audiences.
---
