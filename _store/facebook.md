---
aid: facebook
url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/apis.yml
apis:
- aid: facebook:facebook-graph-api
  name: Facebook Graph API
  description: The primary way to read and write data to the Facebook social graph, providing access to user profiles, posts, pages, and social interactions.
  humanURL: https://developers.facebook.com/docs/graph-api
  baseURL: https://graph.facebook.com
  tags:
  - Graph
  - Posts
  - Social
  - Users
  properties:
  - type: Documentation
    url: https://developers.facebook.com/docs/graph-api/overview
  - type: Authentication
    url: https://developers.facebook.com/docs/facebook-login/access-tokens
- aid: facebook:facebook-marketing-api
  name: Facebook Marketing API
  description: Programmatically manage Facebook ad campaigns, Custom Audiences, and advertising reports.
  humanURL: https://developers.facebook.com/docs/marketing-apis
  baseURL: https://graph.facebook.com
  tags:
  - Advertising
  - Campaigns
  - Marketing
  properties:
  - type: Documentation
    url: https://developers.facebook.com/docs/marketing-api
name: Facebook
tags:
- Advertising
- Authentication
- Messaging
- Social Media
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Facebook is Meta's social networking platform providing APIs for developers to integrate with Facebook's ecosystem. The Facebook Graph API is the primary way to read and write data to the Facebook social graph, enabling access to posts, users, pages, and other social data.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

