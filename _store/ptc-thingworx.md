---
aid: ptc-thingworx
url: https://raw.githubusercontent.com/api-evangelist/ptc-thingworx/refs/heads/main/apis.yml
apis:
  - aid: ptc-thingworx:thingworx-rest-api
    name: PTC ThingWorx REST API
    tags:
      - Digital Twin
      - IoT
      - Manufacturing
      - REST
    image: https://raw.githubusercontent.com/api-evangelist/ptc-thingworx/refs/heads/main/image.png
    humanURL: https://docs.ptc.com/r/en-US/ThingWorx-Help/ThingWorx/Help/Composer/Security/ApplicationKeys/ApplicationKeys
    baseURL: https://api.thingworx.example.com/Thingworx
    properties:
      - url: https://docs.ptc.com/
        type: Documentation
      - url: https://docs.ptc.com/
        type: Reference
      - url: openapi/ptc-thingworx-rest-openapi.yml
        type: OpenAPI
    description: PTC ThingWorx REST API provides programmatic access to the ThingWorx IoT platform including thing management, property read/write, service execution, event subscription, and mashup data APIs using Application Key or OAuth authentication.
  - aid: ptc-thingworx:thingworx-websocket-api
    name: PTC ThingWorx WebSocket/AlwaysOn API
    tags:
      - IoT
      - Manufacturing
      - Real-Time
      - WebSocket
    image: https://raw.githubusercontent.com/api-evangelist/ptc-thingworx/refs/heads/main/image.png
    humanURL: https://docs.ptc.com/
    baseURL: https://api.thingworx.example.com
    properties:
      - url: https://docs.ptc.com/
        type: Documentation
      - url: asyncapi/ptc-thingworx-websocket-asyncapi.yml
        type: AsyncAPI
    description: PTC ThingWorx AlwaysOn WebSocket API enables persistent bidirectional connections for industrial edge devices and remote assets, supporting real-time telemetry streaming, command and control, and device lifecycle management.
  - aid: ptc-thingworx:windchill-rest-api
    name: PTC Windchill REST API
    tags:
      - CAD
      - Manufacturing
      - PDM
      - PLM
      - REST
    image: https://raw.githubusercontent.com/api-evangelist/ptc-thingworx/refs/heads/main/image.png
    humanURL: https://docs.ptc.com/
    baseURL: https://api.windchill.example.com
    properties:
      - url: https://docs.ptc.com/
        type: Documentation
    description: PTC Windchill REST API provides product lifecycle management and PDM access for CAD data management, bill of materials, change management, workflow automation, and product lifecycle workflows in manufacturing environments.
common:
  - url: https://docs.ptc.com/
    type: Portal
  - url: https://docs.ptc.com/
    type: Documentation
  - url: https://www.ptc.com/en/technologies/iiot/thingworx-platform
    type: Website
  - url: https://www.ptc.com/en/privacy-policy
    type: PrivacyPolicy
  - url: https://github.com/ptc-iot-sharing
    type: GitHubOrganization
  - url: openapi/ptc-thingworx-rest-openapi.yml
    type: OpenAPI
  - url: asyncapi/ptc-thingworx-websocket-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/ptc-thingworx-thing-schema.json
    type: JSONSchema
  - url: json-ld/ptc-thingworx-context.jsonld
    type: JSONLDContext
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-04-28'
description: PTC ThingWorx is an industrial Internet of Things platform that enables companies to rapidly develop and deploy smart, connected solutions for industrial environments.
---
