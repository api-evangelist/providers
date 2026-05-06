---
aid: tegna
name: TEGNA
description: TEGNA Inc. is an American broadcast, digital media, and marketing services company headquartered in Tysons, Virginia, operating as a subsidiary of Nexstar Media Group following FCC approval of the $6.2 billion acquisition in March 2026. TEGNA operates 64 full-power broadcast television stations across 51 U.S. markets, reaching approximately 39 percent of all television households. TEGNA offers digital marketing solutions including AudienceOne first-party data targeting, OTT/CTV advertising through its Premion platform, and the TEGNA Marketing Solutions full-service agency. The company provides advertising APIs and programmatic integrations for digital, broadcast, streaming, and connected TV advertising campaigns.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Broadcasting
  - Media
  - Television
  - Digital Advertising
  - OTT
  - CTV
  - Fortune 500
url: https://raw.githubusercontent.com/api-evangelist/tegna/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tegna:audience-one-api
    name: TEGNA AudienceOne API
    description: TEGNA AudienceOne is a first-party data targeting platform enabling advertisers to reach audiences across TEGNA's 64 local television brands in 51 markets using privacy-first targeting. The platform provides programmatic access to audience segments, campaign management, and performance analytics for digital, display, native, and pre-roll video advertising. Supports geofencing, retargeting, and precision targeting without third-party cookies.
    humanURL: https://www.tegna.com/advertise/solutions/digital/
    baseURL: https://api.tegna.com
    tags:
      - Advertising
      - Audience Targeting
      - Digital Media
      - First-Party Data
      - Programmatic
    properties:
      - type: Documentation
        url: https://www.tegna.com/advertise/solutions/digital/
      - type: OpenAPI
        url: openapi/tegna-audience-one-openapi.yml
      - type: JSONSchema
        url: json-schema/tegna-campaign-schema.json
  - aid: tegna:premion-api
    name: TEGNA Premion OTT Advertising API
    description: Premion is TEGNA's over-the-top (OTT) and connected TV (CTV) advertising platform, enabling advertisers to reach audiences across premium streaming services including Roku, Hulu, Amazon Fire TV, and other OTT platforms. The Premion API provides campaign creation, audience targeting, impression delivery, and performance reporting for streaming video advertising at local and national scale.
    humanURL: https://premion.com/
    baseURL: https://api.premion.com
    tags:
      - OTT Advertising
      - CTV
      - Connected TV
      - Streaming
      - Video Advertising
    properties:
      - type: Documentation
        url: https://premion.com/
      - type: OpenAPI
        url: openapi/tegna-premion-openapi.yml
common:
  - url: https://www.tegna.com
    name: TEGNA
    type: Website
    description: TEGNA corporate website (redirects to Nexstar).
  - url: https://www.nexstar.tv/
    name: Nexstar Media Group
    type: Website
    description: Parent company Nexstar Media Group website.
  - url: https://www.tegna.com/advertise/
    name: Advertise With TEGNA
    type: Advertising
    description: Advertising solutions overview for TEGNA.
  - url: https://www.tegna.com/advertise/solutions/digital/
    name: TEGNA Digital Advertising Solutions
    type: Documentation
    description: Digital advertising platform documentation for TEGNA AudienceOne.
  - url: https://www.tegna.com/advertise/solutions/broadcast/
    name: TEGNA Broadcast Advertising
    type: Documentation
    description: Broadcast TV advertising solutions from TEGNA.
  - url: https://www.tegna.com/advertise/solutions/streaming/
    name: TEGNA Streaming/OTT Advertising
    type: Documentation
    description: OTT and streaming advertising solutions from TEGNA.
  - url: https://premion.com/
    name: Premion OTT Advertising
    type: Website
    description: TEGNA's Premion OTT advertising platform.
  - url: https://www.linkedin.com/company/tegna
    name: TEGNA on LinkedIn
    type: LinkedIn
    description: TEGNA LinkedIn company page.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
