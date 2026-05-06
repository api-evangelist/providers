---
aid: monday-com
name: Monday.com
description: An expressive API to interact with your workflows, automate processes, power integrations, and more!
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Work Management
  - CRM
  - Automation
  - GraphQL
created: '2025-02-17'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/monday-com/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: monday-com:monday-com
    name: Monday.com API
    description: An expressive GraphQL API to interact with monday.com workflows, boards, items, users, and updates - automate processes, power integrations, and more.
    humanURL: https://developer.monday.com/api-reference/
    baseURL: https://api.monday.com/v2
    tags:
      - Work Management
      - CRM
      - GraphQL
    properties:
      - type: Documentation
        url: https://developer.monday.com/api-reference/
      - type: Authentication
        url: https://developer.monday.com/api-reference/docs/authentication
      - type: API Playground
        url: https://monday.com/developers/v2/try-it-yourself
      - type: GraphQL
        url: https://raw.githubusercontent.com/api-evangelist/monday-com/refs/heads/main/graphql/monday-com-graphql.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Features
    data:
      - Free for up to 2 users with 3 boards
      - Basic at $9/seat/mo with unlimited items and viewers
      - Standard at $12/seat/mo with 250 automation/integration actions
      - Pro at $19/seat/mo with 25K automation/integration actions
      - Enterprise with 250K actions, multi-level permissions, AI bundle
      - GraphQL API at api.monday.com/v2
      - 'Complexity budget: 5M points/min per account'
      - Default 5K requests/day (raise via support)
      - 10 concurrent requests cap
      - Webhooks for board, item, column changes
      - OAuth 2.0 and API tokens
      - monday Apps Framework for marketplace apps
      - Files API with S3-backed uploads
      - Custom column types via Apps
      - monday Forms and monday WorkForms
      - monday CRM, Dev, Service product variants
    sources:
      - https://monday.com/pricing
    updated: '2026-05-04'
---
