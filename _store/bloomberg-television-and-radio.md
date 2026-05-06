---
aid: bloomberg-television-and-radio
name: Bloomberg Television and Radio
description: Bloomberg Television is a 24-hour global business and financial news television network, while Bloomberg Radio provides all-news financial radio coverage. Bloomberg TV and Radio deliver breaking market news, interviews with business leaders, economic analysis, and market commentary. Content is distributed via cable, satellite, streaming, and digital platforms globally.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-television-and-radio/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Television
  - Radio
  - Financial News
  - Media
  - Streaming
  - Bloomberg TV
  - Bloomberg Radio
apis:
  - aid: bloomberg-television-and-radio:bloomberg-media-content-api
    name: Bloomberg Media Content API
    description: Access Bloomberg TV and Radio content including video clips, interview segments, market coverage segments, and audio content for licensed distribution to enterprise clients and media partners.
    humanURL: https://www.bloomberg.com/media-distribution/
    baseURL: https://api.bloomberg.com/media
    tags:
      - TV Content
      - Radio Content
      - Video
      - Audio
      - Media Licensing
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/media-distribution/
  - aid: bloomberg-television-and-radio:bloomberg-live-stream
    name: Bloomberg Live Streaming API
    description: Embed or access Bloomberg TV live stream for licensed digital distribution on websites, apps, and digital platforms. Includes live market coverage, news programming, and special event coverage.
    humanURL: https://www.bloomberg.com/live/
    baseURL: https://stream.bloomberg.com
    tags:
      - Live Stream
      - Video
      - Streaming
      - Digital Distribution
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/live/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://www.bloomberg.com/media-distribution/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: 24/7 Financial News
        description: Round-the-clock global financial and business news coverage.
      - name: Market Open and Close Coverage
        description: Live coverage of major market open and close events.
      - name: Executive Interviews
        description: In-depth interviews with business leaders, economists, and policymakers.
      - name: Bloomberg Radio
        description: All-news audio coverage for on-the-go financial news consumption.
      - name: On-Demand Content
        description: Access archived Bloomberg TV segments and interviews on demand.
      - name: International Coverage
        description: Regional Bloomberg TV channels covering Asia, Europe, and US markets.
  - type: UseCases
    data:
      - name: Market Monitoring
        description: Monitor financial markets and breaking news through live TV coverage.
      - name: Enterprise TV Integration
        description: Distribute Bloomberg TV to trading floors and enterprise environments.
      - name: Content Licensing
        description: License Bloomberg TV content for redistribution on third-party platforms.
      - name: Media Research
        description: Access Bloomberg TV content archives for media and financial research.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
