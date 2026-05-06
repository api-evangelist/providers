---
aid: spx
name: SPX Graphics
description: SPX Graphics is an open-source, browser-based graphics control system for live video productions and live streams. It provides a REST API for external control of graphics templates, rundowns, and playback via integrations with CasparCG, OBS, vMix, and similar broadcast software. SPX enables operators to trigger, control, and update live graphics overlays programmatically or via UI.
image: https://spxgraphics.com/wp-content/uploads/2021/05/spx-logo.png
url: https://spxgraphics.com
created: '2026-05-02'
modified: '2026-05-02'
apis:
  - name: SPX Graphics Control API
    description: The SPX Graphics Control REST API provides external control over the SPX-GC graphics control system. It allows applications and devices such as Stream Deck to trigger graphics playback, control rundowns, manage templates, and interact with SPX extensions. The API runs locally on port 5656 and supports optional API key authentication.
    image: https://spxgraphics.com/wp-content/uploads/2021/05/spx-logo.png
    humanUrl: https://spxgc.tawk.help/article/help-api
    baseUrl: http://localhost:5656
    tags:
      - Graphics
      - Live Production
      - Broadcast
      - REST API
    properties:
      - type: Documentation
        url: https://spxgc.tawk.help/article/help-api
      - type: GitHub
        url: https://github.com/TuomoKu/SPX-GC
      - type: OpenAPI
        url: openapi/spx-graphics-control-api-openapi.yml
      - type: GettingStarted
        url: https://spxgc.tawk.help/article/help-intro
      - type: ChangeLog
        url: https://github.com/TuomoKu/SPX-GC/blob/master/RELEASE_NOTES.md
      - type: JSONSchema
        url: json-schema/spx-rundown-item-schema.json
      - type: JSONStructure
        url: json-structure/spx-rundown-item-structure.json
      - type: JSONLD
        url: json-ld/spx-context.jsonld
      - type: SpectralRules
        url: rules/spx-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/live-graphics-production.yaml
      - type: Vocabulary
        url: vocabulary/spx-vocabulary.yml
    contact:
      - type: GitHub
        url: https://github.com/TuomoKu/SPX-GC
common:
  - type: Website
    url: https://spxgraphics.com
  - type: GitHub
    url: https://github.com/TuomoKu/SPX-GC
  - type: Documentation
    url: https://spxgc.tawk.help/
  - type: KnowledgeBase
    url: https://spxgc.tawk.help/
maintainers:
  - name: Tuomo Kulomaa
    url: https://github.com/TuomoKu
tags:
  - Broadcast
  - Graphics
  - Live Production
  - Media
  - Streaming
  - Video Production
---
