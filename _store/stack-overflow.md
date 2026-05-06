---
aid: stack-overflow
name: Stack Overflow
description: 'Stack Overflow is the world''s largest question-and-answer community for developers, with over 23 million questions on programming, software development, and technology topics. Stack Overflow offers two API products: the public Stack Exchange API v2.3 for read/write access to Stack Overflow questions, answers, comments, users, tags, and badges; and the Stack Overflow for Teams API v3, a private team knowledge-base API with endpoints for questions, answers, articles, user groups, and SME management.'
url: https://raw.githubusercontent.com/api-evangelist/stack-overflow/refs/heads/main/apis.yml
tags:
  - Answers
  - Code
  - Developer Community
  - Developer Tools
  - Knowledge Base
  - Programming
  - Q&A
  - Questions
  - Stack Overflow
created: '2026-05-02'
modified: '2026-05-02'
apis:
  - aid: stack-overflow:stack-overflow-api
    name: Stack Overflow API
    tags:
      - Answers
      - Badges
      - Comments
      - Developer Community
      - Q&A
      - Questions
      - Stack Overflow
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stackexchange.com/2.3
    humanURL: https://api.stackexchange.com/
    description: The Stack Overflow public API (v2.3) provides programmatic access to questions, answers, comments, users, tags, and badges on the Stack Overflow site. Developers can read and write content with OAuth 2.0 authentication. The API returns JSON responses with a standard wrapper envelope that includes pagination, quota, and backoff metadata. Register an application at StackApps to obtain OAuth credentials.
    properties:
      - url: https://api.stackexchange.com/docs
        type: Documentation
      - url: https://stackexchange.com/legal/api-terms-of-use
        type: Terms of Service
      - url: https://api.stackexchange.com/docs/throttle
        type: Rate Limits
      - url: http://stackapps.com/apps/oauth/register
        type: Sign Up
      - url: openapi/stack-overflow-openapi.yml
        type: OpenAPI
  - aid: stack-overflow:stack-overflow-for-teams-api
    name: Stack Overflow for Teams API v3
    tags:
      - Articles
      - Enterprise
      - Knowledge Management
      - Q&A
      - Stack Overflow
      - Teams
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stackoverflowteams.com/v3
    humanURL: https://api.stackoverflowteams.com/docs
    description: The Stack Overflow for Teams API v3 provides read and write access to private team knowledge bases. It supports managing questions, answers, articles, user groups, subject matter experts (SMEs), and tags within a Stack Overflow for Teams instance. The API uses Personal Access Token (PAT) authentication via the Authorization Bearer header. Business tier subscriptions have read/write access; Basic tier has read-only access.
    properties:
      - url: https://api.stackoverflowteams.com/docs
        type: Documentation
      - url: https://stackoverflow.blog/2023/05/17/stack-overflow-for-teams-api-v3/
        type: Blog
      - url: openapi/stack-overflow-for-teams-openapi.yml
        type: OpenAPI
common:
  - url: https://stackoverflow.com
    type: Website
  - url: https://stackoverflow.blog/
    type: Blog
  - url: https://api.stackexchange.com/docs/authentication
    type: Authentication
  - url: http://stackapps.com/apps/oauth/register
    type: Sign Up
  - url: https://stackexchange.com/legal/api-terms-of-use
    type: Terms of Service
  - url: json-ld/stack-overflow-context.jsonld
    type: JSON-LD
  - url: json-schema/stack-overflow-question-schema.json
    type: JSONSchema
  - url: vocabulary/stack-overflow-vocabulary.yml
    type: Vocabulary
  - url: rules/stack-overflow-rules.yml
    type: SpectralRules
---
