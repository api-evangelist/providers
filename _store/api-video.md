---
aid: api-video
name: API.Video
description: api.video is a video infrastructure platform offering APIs for video on demand, live streaming, analytics, and AI-powered features including transcription and summarization. It provides lightning-fast encoding, 99.999% uptime, 140+ global points of presence, and SDKs in 20+ languages for integrating video into websites, apps, and software.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Analytics
  - CDN
  - Encoding
  - Live Streaming
  - Transcription
  - Video
  - Video on Demand
url: https://raw.githubusercontent.com/api-evangelist/api-video/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: api-video:video-on-demand
    name: api.video Video On Demand API
    description: The api.video Video On Demand API enables uploading, encoding, and streaming videos with automatic format conversion, thumbnail generation, and global CDN delivery. Supports resumable uploads and programmatic video management.
    humanURL: https://docs.api.video/reference
    tags:
      - Encoding
      - On Demand
      - Streaming
      - Video
    properties:
      - type: Documentation
        url: https://docs.api.video/reference
      - type: GettingStarted
        url: https://docs.api.video/get-started/start-building
  - aid: api-video:live-streaming
    name: api.video Live Streaming API
    description: The api.video Live Streaming API enables low-latency live video broadcasts with RTMP ingest, automatic recording, and global CDN delivery for audiences worldwide.
    humanURL: https://docs.api.video/reference
    tags:
      - Broadcasting
      - Live Streaming
      - RTMP
      - Video
    properties:
      - type: Documentation
        url: https://docs.api.video/reference
  - aid: api-video:analytics
    name: api.video Analytics API
    description: The api.video Analytics API provides viewer engagement metrics, playback statistics, and performance data for both video on demand and live streaming content.
    humanURL: https://docs.api.video/reference
    tags:
      - Analytics
      - Engagement
      - Metrics
      - Video
    properties:
      - type: Documentation
        url: https://docs.api.video/reference
common:
  - type: Website
    url: https://api.video/
  - type: Documentation
    url: https://docs.api.video/
  - type: GettingStarted
    url: https://docs.api.video/get-started/start-building
  - type: StatusPage
    url: https://status.api.video
  - type: GitHubOrganization
    url: https://github.com/ApiVideo
  - type: Pricing
    url: https://api.video/pricing
  - type: Features
    data:
      - name: Lightning-Fast Video Encoding
        description: Video encoding with 0.02s playback speed using global infrastructure.
      - name: 99.999% Uptime SLA
        description: Enterprise-grade reliability with 99.999% uptime guarantee backed by SLA.
      - name: 140+ Global Points of Presence
        description: Global CDN with 140+ PoPs and 1 Petabyte monthly traffic capacity for worldwide delivery.
      - name: AI Transcription
        description: Automatic video transcription powered by AI for searchable captions and accessibility.
      - name: AI Video Summarization
        description: AI-generated video summaries to help viewers navigate long-form content.
      - name: 20+ SDKs
        description: Official SDKs for iOS, Android, Flutter, Java, Python, Node.js, PHP, C#, React Native, and more.
      - name: Usage-Based Pricing
        description: Flexible usage-based pricing with volume discounts scaling with consumption.
      - name: Resumable Uploads
        description: Reliable large file uploads with resumable upload support for videos of any size.
  - type: UseCases
    data:
      - name: Online Learning and Corporate Training
        description: Host and deliver training videos with analytics to track learner engagement and completion.
      - name: Short-Form Video Platforms
        description: Build TikTok-style or short-form video applications with fast encoding and global delivery.
      - name: E-Commerce Video
        description: Add product videos and live shopping streams to e-commerce and marketplace applications.
      - name: Communication Tools
        description: Integrate video messaging and user-generated content into communication platforms.
      - name: Generative AI Video Hosting
        description: Host and stream AI-generated video content at scale with reliable infrastructure.
  - type: Integrations
    data:
      - name: WordPress
        description: WordPress plugin for embedding and managing api.video content in WordPress sites.
      - name: Contentful
        description: Integration with Contentful CMS for video asset management in headless content workflows.
      - name: Bubble
        description: No-code integration with Bubble for adding video capabilities to Bubble applications.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
