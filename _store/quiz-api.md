---
aid: quiz-api
name: QuizAPI
description: QuizAPI provides programmatic access to thousands of quiz questions across topics such as programming, science, mathematics, and general knowledge. Developers can use the API to power trivia apps, online assessments, learning platforms, and embedded quizzes on their own websites. Questions can be filtered by category, difficulty, and tags, and quizzes can be created and managed through a JSON REST API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Quizzes
  - Trivia
  - Education
  - Assessment
  - Content
created: '2025-02-12'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/quiz-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: quiz-api:quiz-api
    name: QuizAPI
    description: The QuizAPI REST API exposes endpoints for browsing categories and metadata, searching and creating quizzes, retrieving quiz details, listing questions, and batch-importing questions into a quiz. Authentication is performed with a Bearer API key issued from quizapi.io. Responses are JSON with a consistent `data` and `meta` envelope and support standard pagination.
    humanURL: https://quizapi.io/
    baseURL: https://quizapi.io
    tags:
      - Quizzes
      - Trivia
      - Education
    properties:
      - type: Documentation
        url: https://quizapi.io/docs
      - type: OpenAPI
        url: https://quizapi.io/api/v1/openapi.json
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/quiz-api/refs/heads/main/openapi/quiz-api-openapi.json
      - type: SignUp
        url: https://quizapi.io/signup
      - type: Authentication
        url: https://quizapi.io/docs/authentication
      - type: RateLimits
        url: https://quizapi.io/docs/rate-limits
      - type: Webhooks
        url: https://quizapi.io/docs/webhooks
      - type: SDKs
        url: https://quizapi.io/docs/sdks
common:
  - type: Website
    url: https://quizapi.io/
  - type: Documentation
    url: https://quizapi.io/docs
  - type: SignUp
    url: https://quizapi.io/signup
  - type: Support
    url: https://github.com/QuizAPI/support/issues
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
