---
aid: slack
url: >-
  https://raw.githubusercontent.com/api-search/messaging/main/_apis/slack/apis.md
apis:
  - aid: slack:slack-web-api
    name: Slack Web API
    tags: []
    contact:
      - FN: Support
        url: https://api.slack.com/support
    overlays:
      - url: >-
          overlays/https://raw.githubusercontent.com/slackapi/slack-api-specs/master/web-api/slack_web_openapi_v2.json-openapi-search.yml
        type: APIs.io Search
    description: >-
      The Slack Web API is an interface for querying information from and
      enacting change in a Slack workspace. Use it for individual queries, or as
      part of a more complex tapestry of platform features in a Slack app.
name: Slack
tags:
  - Messaging
  - Chat
  - Bots
  - Productivity
type: Contract
access: 3rd-Party
created: 2024/04/14
modified: '2024-12-16'
position: Consuming
description: >-
  Slack is a cloud-based freemium cross-platform instant messaging service
  created by Slack Technologies and currently owned by Salesforce. While
  initially developed for professional and organizational communications, it has
  also been adopted as a community platform.
maintainers:
  - FN: API Evangelist
    url: https://apievangelisgt.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---