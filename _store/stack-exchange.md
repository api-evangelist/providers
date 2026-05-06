---
aid: stack-exchange
name: Stack Exchange
description: Stack Exchange is a network of question-and-answer websites on topics in diverse fields, each site covering a specific topic, where questions, answers, and users are subject to a reputation award process. The network includes over 170 communities including Stack Overflow (programming), Server Fault (system administration), Super User (computing), and many others. The Stack Exchange API v2.3 provides programmatic access to questions, answers, comments, users, tags, badges, and search across all sites in the network.
url: https://raw.githubusercontent.com/api-evangelist/stack-exchange/refs/heads/main/apis.yml
tags:
  - Answers
  - Code
  - Community
  - Developer Tools
  - Knowledge Base
  - Q&A
  - Questions
  - Stack Exchange
created: '2023-11-15'
modified: '2026-05-02'
apis:
  - aid: stack-exchange:stack-exchange-api
    name: Stack Exchange API
    tags:
      - Answers
      - Badges
      - Comments
      - Community
      - Q&A
      - Questions
      - Stack Exchange
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stackexchange.com/2.3
    contact:
      - FN: Stack Exchange
        url: http://stackapps.com/
        email: team+api@stackexchange.com
    humanURL: https://api.stackexchange.com/
    description: The Stack Exchange API v2.3 provides programmatic access to the Stack Exchange network of Q&A sites. It supports reading and writing questions, answers, comments, tags, users, and badges across all network sites including Stack Overflow. Authentication is via OAuth 2.0 with support for both read and write access. All responses are JSON-encoded and support GZIP compression and field-level filtering.
    properties:
      - url: https://api.stackexchange.com/docs
        type: Documentation
      - url: https://stackexchange.com/legal/api-terms-of-use
        type: Terms of Service
      - url: https://api.stackexchange.com/docs/throttle
        type: Rate Limits
      - url: http://stackapps.com/apps/oauth/register
        type: Sign Up
      - url: http://stackapps.com/apps/oauth
        type: Applications
      - url: openapi/stack-exchange-openapi.yml
        type: OpenAPI
common:
  - url: https://api.stackexchange.com/docs/authentication
    type: Authentication
  - url: https://stackoverflow.blog/
    type: Blog
  - url: https://stackexchange.com/legal/api-terms-of-use
    type: Terms of Service
  - url: https://api.stackexchange.com/docs/throttle
    type: Rate Limits
  - url: http://stackapps.com/apps/oauth/register
    type: Sign Up
  - url: http://stackapps.com/apps/oauth
    type: Applications
  - url: https://github.com/topics/stackexchange-api
    type: GitHub Topics
  - url: json-ld/stack-exchange-context.jsonld
    type: JSON-LD
  - url: json-schema/stack-exchange-question-schema.json
    type: JSONSchema
  - url: vocabulary/stack-exchange-vocabulary.yml
    type: Vocabulary
  - url: rules/stack-exchange-rules.yml
    type: SpectralRules
---
