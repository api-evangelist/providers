---
aid: microsoft-xbox
url: https://raw.githubusercontent.com/api-evangelist/microsoft-xbox/refs/heads/main/apis.yml
apis:
- aid: microsoft-xbox:xbox-live-api
  name: Xbox Live Services API
  tags:
  - Achievements
  - Gaming
  - Multiplayer
  - Xbox Live
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://xbl.io/api/v2/
  humanURL: https://learn.microsoft.com/en-us/gaming/gdk/_content/gc/live/get-started/live-getstarted-nav
  properties:
  - url: https://learn.microsoft.com/en-us/gaming/gdk/_content/gc/live/get-started/live-getstarted-nav
    type: Documentation
  description: Xbox Live Services provides APIs for achievements, leaderboards, multiplayer, matchmaking, social features, presence, and cloud saves. Game developers can integrate Xbox Live features for player identity, social gaming, and cross-platform play across Xbox, PC, and mobile.
- aid: microsoft-xbox:playfab-api
  name: Azure PlayFab API
  tags:
  - Backend
  - Gaming
  - LiveOps
  - PlayFab
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{titleId}.playfabapi.com/
  humanURL: https://learn.microsoft.com/en-us/gaming/playfab/
  properties:
  - url: https://learn.microsoft.com/en-us/gaming/playfab/
    type: Documentation
  - url: https://learn.microsoft.com/en-us/rest/api/playfab/
    type: API Reference
  description: Azure PlayFab provides a complete backend platform for games with APIs for player authentication, data management, economy and commerce, multiplayer servers, analytics, and LiveOps. It supports real-time game telemetry, A/B testing, player segmentation, and content updates without client patches.
name: Microsoft Xbox
tags:
- Gaming
- Microsoft
- PlayFab
- Xbox
- Xbox Live
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Xbox gaming platform including Xbox Live Services and Azure PlayFab backend for games.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

