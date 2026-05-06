---
aid: associated-press
name: Associated Press
description: The Associated Press (AP) is an American not-for-profit news agency founded in 1846. The AP is the world's oldest and largest newsgathering organization, serving media companies worldwide with text, photos, video, audio, and interactive content. The AP provides developer APIs for accessing election data, news content, and media assets including the AP Elections API for real-time election results, the AP Content API for news and media asset access, and the AP Media API for digital asset management integration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Elections
  - Journalism
  - Media
  - News
  - Content
created: '2024-04-14'
modified: '2026-04-19'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/associated-press/refs/heads/main/apis.yml
apis:
  - aid: associated-press:ap-elections-api
    name: AP Elections API
    description: Integrate your election systems with AP Elections API. Your election results delivery application retrieves election race information from AP Elections API to power election websites, reporting systems, and news dashboards. Provides real-time election results, candidate data, and race call information for federal, state, and local elections.
    humanURL: https://developer.ap.org/ap-elections-api/
    baseURL: https://api.ap.org
    tags:
      - Elections
      - News
      - Results
    properties:
      - type: Documentation
        url: https://developer.ap.org/ap-elections-api/
      - type: GettingStarted
        url: https://developer.ap.org/ap-elections-api/
  - aid: associated-press:ap-media-api
    name: AP Media API
    description: The AP Media API provides access to AP's digital media assets including photos, videos, and graphics from AP's global newsgathering operations. Enables integration with digital asset management systems and content management platforms for news organizations.
    humanURL: https://developer.ap.org/
    baseURL: https://api.ap.org
    tags:
      - Media
      - Photos
      - Video
      - Content
    properties:
      - type: Documentation
        url: https://developer.ap.org/
      - type: OpenAPI
        url: openapi/associated-press-meda-openapi-original.yml
common:
  - type: Portal
    url: https://www.ap.org/
    title: Associated Press Website
  - type: Portal
    url: https://developer.ap.org/
    title: AP Developer Portal
  - type: Documentation
    url: https://developer.ap.org/
    title: Developer Documentation
  - type: Features
    data:
      - name: AP Elections API
        description: Real-time election results delivery for federal, state, and local elections with candidate data, race calls, and vote totals.
      - name: AP Content API
        description: Access to AP's global news content including text stories, photos, video, and graphics from AP correspondents worldwide.
      - name: AP Media API
        description: Digital asset management integration for AP's extensive photo and video library with metadata, rights, and distribution capabilities.
      - name: AP DataStream
        description: Streaming news content delivery for applications requiring real-time news updates and content ingestion.
  - type: UseCases
    data:
      - name: Election Coverage
        description: News organizations and election management companies use the AP Elections API to power live election result dashboards and reporting.
      - name: News Content Integration
        description: Media companies integrate AP content APIs to supplement their own coverage with AP newswire stories and multimedia content.
      - name: Photo and Video Licensing
        description: Publishers and digital media companies access AP's photo and video archive through the Media API for editorial and commercial use.
  - type: Integrations
    data:
      - name: Newsroom CMS Integrations
        description: AP content APIs integrate with major content management systems used by newspapers, broadcasters, and digital media publishers.
      - name: Election Management Systems
        description: Election technology vendors integrate AP Elections API for authoritative election result data in voting systems and election night reporting tools.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
