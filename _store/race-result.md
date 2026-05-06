---
aid: race-result
name: RACE RESULT
description: The RACE RESULT REST interface allows retrieval of data from systems uploading to RACE RESULT servers, including RACE RESULT decoders that upload via TCP and Track Boxes, and supports remote control commands sent to decoders. Communication with the REST API requires API keys for the Customer ID being accessed.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Race Timing
  - Decoder
  - Sports
  - Hardware
  - Race Results
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/race-result/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: race-result:race-result
    name: RACE RESULT
    description: REST API for retrieving uploaded timing data and sending remote control commands to RACE RESULT decoders and Track Boxes.
    humanURL: https://www.raceresult.com/en-us/support/kb?id=22003-REST-API-Interface
    tags:
      - Race Timing
      - Decoder
      - Race Results
    properties:
      - type: Documentation
        url: https://www.raceresult.com/en-us/support/kb?id=22003-REST-API-Interface
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
