---
aid: bloomberg-tv
name: Bloomberg TV
description: Bloomberg TV is a 24-hour global business and financial news television network delivering real-time market coverage, business news, executive interviews, and economic analysis. Bloomberg TV reaches a global audience through cable, satellite, digital streaming, and over-the-top (OTT) platforms. The network provides live market open and close coverage, special event programming, and on-demand content access.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-tv/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Bloomberg TV
  - Television
  - Financial News
  - Media
  - Streaming
  - Live Coverage
  - Bloomberg
apis:
  - aid: bloomberg-tv:bloomberg-tv-api
    name: Bloomberg TV Content API
    description: Access Bloomberg TV video content, live stream, and on-demand clips for licensed distribution. Provides access to market coverage segments, interviews, and editorial content for enterprise and media partner integration.
    humanURL: https://www.bloomberg.com/live/
    baseURL: https://api.bloomberg.com/tv
    tags:
      - TV Content
      - Live Stream
      - Video
      - On-Demand
      - Media Distribution
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/live/
  - aid: bloomberg-tv:bloomberg-tv-embed
    name: Bloomberg TV Embed API
    description: Embed Bloomberg TV live stream and video clips on licensed digital properties using Bloomberg's embed API. Supports customizable player integration for websites, apps, and digital publishing platforms.
    humanURL: https://www.bloomberg.com/live/
    baseURL: https://embed.bloomberg.com/tv
    tags:
      - Embed
      - Live Stream
      - Video Player
      - Web Integration
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/live/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://www.bloomberg.com/live/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: 24/7 Live Coverage
        description: Round-the-clock live financial news and market coverage.
      - name: Market Open and Close
        description: Special programming covering US and international market open and close events.
      - name: Executive Interviews
        description: In-depth interviews with C-suite executives, policymakers, and economists.
      - name: On-Demand Video
        description: Access Bloomberg TV segments and interviews on demand.
      - name: Multi-Region Coverage
        description: Bloomberg TV channels covering Asia, Europe, Middle East, and Americas.
      - name: Digital Streaming
        description: OTT and digital streaming via Bloomberg.com, app, and partner platforms.
  - type: UseCases
    data:
      - name: Trading Floor Displays
        description: Display Bloomberg TV live on trading floor screens for market monitoring.
      - name: Digital Publishing
        description: Embed Bloomberg TV content on licensed financial news websites.
      - name: Enterprise Deployment
        description: Deploy Bloomberg TV to corporate offices and financial institutions.
      - name: Research and Media Monitoring
        description: Monitor Bloomberg TV coverage for media analysis and research.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
