---
aid: railway
name: Railway
description: The Railway public API is built with GraphQL and is the same API that powers the Railway dashboard, providing automation for projects, services, deployments, environments, volumes, and CI/CD workflows on the Railway platform.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Platform as a Service
  - Deployments
  - GraphQL
  - Infrastructure
  - DevOps
created: '2025-02-06'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/railway/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: railway:public-api
    name: Railway Public GraphQL API
    description: The Railway public API is a GraphQL API that powers the Railway dashboard, enabling automation of projects, services, deployments, environments, variables, volumes, and team workflows.
    humanURL: https://docs.railway.com/reference/public-api
    baseURL: https://backboard.railway.com/graphql/v2
    tags:
      - GraphQL
      - Deployments
      - Projects
      - Services
    properties:
      - type: Documentation
        url: https://docs.railway.com/reference/public-api
      - type: GettingStarted
        url: https://docs.railway.com/guides/public-api
      - type: GraphQL
        url: https://backboard.railway.com/graphql/v2
      - type: Playground
        url: https://railway.com/graphiql
      - type: Postman
        url: https://raw.githubusercontent.com/api-evangelist/railway/refs/heads/main/
common:
  - type: Documentation
    url: https://docs.railway.com/
  - type: GettingStarted
    url: https://docs.railway.com/guides/public-api
  - type: SignUp
    url: https://railway.com/login
  - type: Pricing
    url: https://railway.com/pricing
  - type: TermsOfService
    url: https://railway.com/legal/terms
  - type: Authentication
    url: https://docs.railway.com/guides/public-api#authentication
  - type: Features
    data:
      - 'Free: $5 trial credits, then $1/mo, up to 1 vCPU / 0.5 GB'
      - 'Hobby: $5 min/mo + $5 credits, up to 48 vCPU / 48 GB'
      - 'Pro: $20 min/mo + $20 credits, up to 1,000 vCPU / 1 TB'
      - 'Enterprise: up to 2,400 vCPU / 2.4 TB, SSO/HIPAA'
      - 'Per-second billing: memory, CPU, volumes, egress'
      - GraphQL API at backboard.railway.com/graphql
      - 'API rate limit: 1,000 req/min/token'
      - 'Build concurrency: 1 Hobby, 5 Pro'
      - GitHub auto-deploy
      - Built-in databases (Postgres, MySQL, MongoDB, Redis, Vector)
      - Templates and stacks
      - Volumes for persistent storage
      - Multi-region deployment (Pro+)
      - Public + private networking
      - Webhooks + GraphQL subscriptions
      - OAuth 2.0 + project tokens
    sources:
      - https://railway.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
