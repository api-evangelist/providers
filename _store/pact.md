---
aid: pact
name: Pact
description: Pact is an open source contract testing framework that verifies API consumer-provider interactions with support for Ruby, Java, .NET, JavaScript, Go, and Python. Pact Broker provides a hypermedia-driven HAL API for storing, retrieving, and verifying contracts between services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Contract Testing
  - Open Source
  - Testing
url: https://raw.githubusercontent.com/api-evangelist/pact/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: pact:pact-broker
    name: Pact Broker API
    description: Pact Broker is a hypermedia HAL API for storing and retrieving consumer contracts created with the Pact contract testing framework. It enables teams to share, version, and verify pacts between consumers and providers.
    humanURL: https://docs.pact.io/pact_broker
    tags:
      - Contract Testing
      - Testing
    properties:
      - type: Documentation
        url: https://docs.pact.io/pact_broker
      - type: GitHub Repository
        url: https://github.com/pact-foundation/pact_broker
      - type: Hosted Service
        url: https://pactflow.io
common:
  - type: Website
    url: https://pact.io
  - type: Documentation
    url: https://docs.pact.io
  - type: GitHub Organization
    url: https://github.com/pact-foundation
  - type: Slack
    url: https://pact-foundation.slack.com
  - type: Blog
    url: https://docs.pact.io/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
