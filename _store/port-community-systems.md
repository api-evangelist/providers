---
aid: port-community-systems
name: Port Community Systems
description: Port Community Systems (PCS) are neutral and open electronic platforms enabling intelligent and secure exchange of information between public and private stakeholders to optimise, manage, and automate efficient port and logistics processes through a single submission of data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Maritime
  - Port
  - Logistics
  - Customs
  - Cargo
  - Shipping
url: https://raw.githubusercontent.com/api-evangelist/port-community-systems/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: port-community-systems:portbase
    name: Portbase Port Community System API
    description: Portbase is the Dutch Port Community System providing APIs for customs declarations, cargo manifests, vessel call notifications, berth planning, and port logistics coordination at the Port of Rotterdam and Amsterdam, connecting shipping lines, freight forwarders, customs authorities, and terminal operators.
    humanURL: https://www.portbase.com/en/
    tags:
      - Maritime
      - Port
      - Customs
      - Cargo
      - Netherlands
    properties:
      - type: Documentation
        url: https://www.portbase.com/en/
      - type: OpenAPI
        url: openapi/portbase-port-community-openapi.yml
      - type: AsyncAPI
        url: asyncapi/portbase-vessel-events-asyncapi.yml
      - type: JSONSchema
        url: json-schema/portbase-vessel-call-schema.json
      - type: JSONLDContext
        url: json-ld/portbase-context.jsonld
  - aid: port-community-systems:ipcsa
    name: IPCSA Port Community Systems API
    description: The International Port Community Systems Association (IPCSA) represents Port Community System operators and Maritime Single Window operators worldwide. Member PCS platforms provide APIs for customs declarations, cargo manifests, vessel call data, and port logistics coordination using REST and EDIFACT protocols.
    humanURL: https://www.ipcsa.international/
    tags:
      - Maritime
      - Port
      - Customs
      - Cargo
      - International
    properties:
      - type: Documentation
        url: https://www.ipcsa.international/
common:
  - type: Website
    url: https://www.ipcsa.international/
  - type: Portal
    url: https://www.ipcsa.international/
  - type: Documentation
    url: https://www.ipcsa.international/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
