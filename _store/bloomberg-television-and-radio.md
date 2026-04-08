---
aid: bloomberg-television-and-radio
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-television-and-radio/refs/heads/main/apis.yml
apis:
- name: Bloomberg Live TV Stream API
  description: Access to Bloomberg Television's live streaming content and broadcast schedule, including regional channels for US, Europe, and Asia markets coverage.
  image: https://www.bloomberg.com/images/tv-logo.png
  baseURL: https://api.bloomberg.com/tv/v1
  humanURL: https://www.bloomberg.com/live
  tags:
  - Financial News
  - Live Streaming
  - Markets
  - Television
  - Video
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/api/docs/tv
  - type: OpenAPI
    url: openapi/bloomberg-television-and-radio-live-tv-stream-openapi.yml
  - type: Authentication
    url: https://www.bloomberg.com/api/auth
  - type: Rate Limits
    url: https://www.bloomberg.com/api/rate-limits
- name: Bloomberg Radio API
  description: Access to Bloomberg Radio's live audio streams and podcast content, including Bloomberg Surveillance, Bloomberg Daybreak, and other flagship radio programming.
  image: https://www.bloomberg.com/images/radio-logo.png
  baseURL: https://api.bloomberg.com/radio/v1
  humanURL: https://www.bloomberg.com/audio
  tags:
  - Audio
  - News
  - Podcasts
  - Radio
  - Streaming
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/api/docs/radio
  - type: OpenAPI
    url: openapi/bloomberg-television-and-radio-radio-openapi.yml
  - type: Authentication
    url: https://www.bloomberg.com/api/auth
- name: Bloomberg Program Schedule API
  description: Retrieve television and radio program schedules and show information across Bloomberg's live TV and radio channels.
  baseURL: https://api.bloomberg.com/schedule/v1
  humanURL: https://www.bloomberg.com/live/schedule/us
  tags:
  - Programming
  - Radio
  - Schedule
  - Shows
  - Television
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/api/docs/schedule
  - type: OpenAPI
    url: openapi/bloomberg-television-and-radio-program-schedule-openapi.yml
name: Bloomberg Television and Radio
tags:
- Business News
- Financial News
- Market Data
- Radio
- Streaming
- Television
type: Contract
image: https://www.bloomberg.com/images/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bloomberg Television and Radio provides live streaming financial news, market data, and business analysis through television broadcasts and radio programming worldwide. Bloomberg Media produces over 30 podcasts and offers 24/7 live TV and radio coverage across multiple regional channels.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

