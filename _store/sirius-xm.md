---
aid: sirius-xm
name: Sirius XM
description: Sirius XM Holdings is the leading audio entertainment company in North America, providing satellite radio, digital streaming, podcast, and advertising services through SiriusXM, Pandora, and AdsWizz brands. The Pandora Developer API enables partners to build personalized music and podcast streaming experiences using GraphQL. AdsWizz, a SiriusXM company, provides programmatic audio advertising APIs for ad insertion, targeting, and measurement across streaming and podcast platforms.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Audio
  - Streaming
  - Radio
  - Music
  - Podcast
  - Advertising
  - Entertainment
x-fortune: Fortune 500
created: '2025-01-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sirius-xm/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sirius-xm:pandora-api
    name: Pandora Developer API
    description: The Pandora Developer API provides GraphQL-based access to Pandora's music catalog of over 30 million tracks, stations, podcasts, and playlists. It supports personalized playback, search, user feedback (thumbs up/down), collection management, and listener profile data. Authentication uses OAuth2. The API is available through the Pandora Developer Center for approved partner applications.
    humanURL: https://developer.pandora.com/
    baseURL: https://www.pandora.com/api
    tags:
      - Music
      - Streaming
      - Podcast
      - GraphQL
    properties:
      - type: Documentation
        url: https://developer.pandora.com/docs/key-concepts/apis/
      - type: DeveloperPortal
        url: https://developer.pandora.com/
  - aid: sirius-xm:adswizz-domain-api
    name: AdsWizz Domain API
    description: The AdsWizz Domain API is a programmatic audio advertising platform API enabling dynamic ad insertion, campaign management, and audience targeting across streaming radio, podcasts, and digital audio content. AdsWizz is a SiriusXM company powering audio advertising technology including AudioID for listener identity and contextual targeting.
    humanURL: https://docs.adswizz.com/domain-api/v8/
    baseURL: https://api.adswizz.com
    tags:
      - Advertising
      - Audio Ads
      - Programmatic
      - Ad Insertion
    properties:
      - type: Documentation
        url: https://docs.adswizz.com/domain-api/v8/
  - aid: sirius-xm:adswizz-sdk
    name: AdsWizz SDK
    description: The AdsWizz SDK provides mobile and web integration for audio advertising, supporting VAST-compliant ad tech with companion banner support. Available for iOS (Swift), Android (Kotlin), and Web (JavaScript).
    humanURL: https://docs.sdk.adswizz.com/
    baseURL: https://api.sdk.adswizz.com
    tags:
      - SDK
      - Mobile
      - Audio Ads
      - VAST
    properties:
      - type: Documentation
        url: https://docs.sdk.adswizz.com/
common:
  - type: Website
    url: https://www.siriusxm.com/
  - type: Website
    url: https://www.siriusxmmedia.com/
  - type: DeveloperPortal
    url: https://developer.pandora.com/
  - type: Documentation
    url: https://developer.pandora.com/docs/
  - type: Blog
    url: https://www.siriusxm.com/blog/
  - type: GitHubOrg
    url: https://github.com/SiriusXM
  - type: AdvertisingPlatform
    url: https://www.siriusxmmedia.com/
  - type: AdsWizz
    url: https://www.adswizz.com/
  - type: AdsWizzDocs
    url: https://docs.adswizz.com/
  - type: TermsOfService
    url: https://www.siriusxm.com/terms
  - type: PrivacyPolicy
    url: https://www.siriusxm.com/privacy
  - type: InvestorRelations
    url: https://investor.siriusxm.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
