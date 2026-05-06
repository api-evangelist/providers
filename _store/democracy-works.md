---
aid: democracy-works
name: Democracy Works
url: https://raw.githubusercontent.com/api-evangelist/democracy-works/refs/heads/main/apis.yml
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/democracy-works-elections-api-democracy-works-election-data.png
tags:
  - Civic Tech
  - Elections
  - Government
  - Nonprofit
  - Voter Information
  - Voting
created: '2024-03-30'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
description: Democracy Works is a nonprofit civic technology organization providing reliable voting guidance for federal, state, and local elections. Its Elections API powers voter-facing platforms, apps, reminders, and outreach campaigns with comprehensive election and election-authority data keyed to Open Civic Data IDs.
apis:
  - aid: democracy-works:elections-api
    name: Democracy Works Elections API
    description: The Democracy Works Elections API provides reliable voting guidance for all levels of elections, from federal to local. It exposes elections, election authorities, state-level guidance, and bulk export endpoints used to inspire civic participation.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://data.democracy.works/api-info
    baseURL: https://api.democracy.works/v2
    tags:
      - Authorities
      - Elections
      - Exports
      - Voter Information
    properties:
      - type: Documentation
        url: https://data.democracy.works/api-info
      - type: SignUp
        url: https://data.democracy.works/api-signup
      - type: OpenAPI
        url: openapi/openapi-spec.yml
      - type: Rules
        url: rules/democracy-works-elections-api-rules.yml
      - type: Capabilities
        url: capabilities/democracy-works-elections-api-capabilities.yml
      - type: JSONSchema
        url: json-schema/democracy-works-election-schema.json
      - type: JSONSchema
        url: json-schema/democracy-works-authority-schema.json
common:
  - type: Website
    url: https://www.democracy.works
  - type: Data Portal
    url: https://data.democracy.works
  - type: GitHub
    url: https://github.com/democracyworks
  - type: GoogleGroup
    url: https://groups.google.com/a/democracy.works/g/democracy-works-data
  - type: Support
    url: mailto:partnerships@democracy.works
  - type: JSON-LD
    url: json-ld/democracy-works-context.jsonld
  - type: Vocabulary
    url: vocabulary/democracy-works-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
