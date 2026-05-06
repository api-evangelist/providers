---
aid: celigo
url: https://raw.githubusercontent.com/api-evangelist/celigo/refs/heads/main/apis.yml
name: Celigo
tags:
  - API Management
  - Automation
  - Data Integration
  - Integration
  - iPaaS
  - Workflow
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-16'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: Celigo is an intelligent automation platform (iPaaS) that enables organizations to integrate applications, automate business processes, and connect data across their technology stack with low-code tooling. Celigo offers a REST-based integrator.io Platform API, an API Management console, OAuth 2.0 and Bearer Token authentication, and more than one thousand pre-built connectors and integration applications.
apis:
  - aid: celigo:celigo-integrator-io-api
    name: Celigo integrator.io Platform API
    tags:
      - Integration
      - iPaaS
      - REST
      - Platform
    humanURL: https://docs.celigo.com/hc/en-us/categories/360001519091-Platform-API
    properties:
      - url: https://docs.celigo.com/hc/en-us/categories/360001519091-Platform-API
        type: Documentation
      - url: https://github.com/celigo/integrator-api-docs
        type: Reference
      - url: https://docs.celigo.com/hc/en-us/articles/360042281231-Getting-started-with-standard-REST-API
        type: GettingStarted
      - url: https://docs.celigo.com/hc/en-us/articles/360038520652-Set-up-a-connection-to-Celigo-integrator-io
        type: Connection
    description: The integrator.io Platform API is a RESTful JSON API secured by Bearer Tokens. It provides programmatic access to integrations, connections, flows, imports, exports, iClients, and other integrator.io resources, with rate limiting via a leaky bucket algorithm of 1000 tokens and a fill rate of 300 tokens per second.
  - aid: celigo:celigo-oauth-api
    name: Celigo OAuth Authentication
    tags:
      - Authentication
      - OAuth 2.0
      - OAuth 1.0
      - Security
    humanURL: https://docs.celigo.com/hc/en-us/articles/360039586072-Set-up-an-OAuth-2-0-HTTP-connection
    properties:
      - url: https://docs.celigo.com/hc/en-us/articles/360039586072-Set-up-an-OAuth-2-0-HTTP-connection
        type: Documentation
      - url: https://docs.celigo.com/hc/en-us/articles/10552671272219-Set-up-an-OAuth-1-0-HTTP-connection
        type: OAuth1
      - url: https://docs.celigo.com/hc/en-us/articles/11933835192859-Create-an-OAuth-2-0-iClient-resource
        type: iClient
    description: Celigo supports OAuth 2.0 and OAuth 1.0 authentication for HTTP connections, configured through iClient resources for reusable OAuth client credentials across integrations.
  - aid: celigo:celigo-api-management
    name: Celigo API Management
    tags:
      - API Gateway
      - API Management
      - Publishing
    humanURL: https://docs.celigo.com/hc/en-us/articles/21179125401755-The-API-Management-console-Features-and-concepts
    properties:
      - url: https://docs.celigo.com/hc/en-us/articles/21179125401755-The-API-Management-console-Features-and-concepts
        type: Documentation
      - url: https://www.celigo.com/platform/api-management/
        type: Overview
    description: Celigo API Management allows organizations to build, publish, and govern APIs on top of Celigo-managed integrations and third-party systems with a dedicated API Management console.
common:
  - type: Website
    url: https://celigo.com/
  - type: Portal
    url: https://docs.celigo.com/
  - type: Documentation
    url: https://docs.celigo.com/hc/en-us/categories/360001519091-Platform-API
  - type: Reference
    url: https://github.com/celigo/integrator-api-docs
  - type: GettingStarted
    url: https://docs.celigo.com/hc/en-us/articles/360042281231-Getting-started-with-standard-REST-API
  - type: Authentication
    url: https://docs.celigo.com/hc/en-us/articles/360039586072-Set-up-an-OAuth-2-0-HTTP-connection
  - type: Privacy Policy
    url: https://celigo.com/privacy-policy/
  - type: Terms of Service
    url: https://celigo.com/terms-of-service/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
