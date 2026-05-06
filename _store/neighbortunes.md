---
aid: neighbortunes
name: Neighbortunes
description: Welcome to NEIGHBORTUNES! The officially unofficial home of all things Neighbor. This site is a work in progress but we hope you enjoy being able to look up setlists, songs, teases, venues, band stats, and much more!
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Music
  - Setlists
  - Fan Site
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/neighbortunes/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: neighbortunes:neighbortunes
    name: Neighbortunes
    description: The Neighbortunes REST API exposes setlists, shows, songs, venues, jamcharts, albums, metadata, links, uploads, and appearances. No authentication required.
    humanURL: https://www.neighbortunes.net/
    baseURL: https://neighbortunes.net/api/v2
    tags:
      - Music
      - Setlists
    properties:
      - type: Documentation
        url: https://www.neighbortunes.net/api/docs.php
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/neighbortunes/refs/heads/main/openapi/neighbortunes-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
