---
aid: the-racing-api
name: The Racing API
description: High performance API for horse racing statistical modelling, application development and web content. Complete coverage of UK, Irish and Hong Kong horse racing with real-time data updates every 3 minutes.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Horse Racing
  - Sports
  - Statistics
  - Betting
  - Analytics
created: '2025-02-06'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/the-racing-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: the-racing-api:the-racing-api
    name: The Racing API
    description: High performance API for horse racing statistical modelling, application development and web content. Complete coverage of UK, Irish and Hong Kong horse racing. Access racecards, results, horse form, jockey and trainer statistics, and real-time analysis endpoints with 58 endpoints across courses, racecards, results, horses, jockeys, trainers, owners, sires, dams, damsires, odds, and North America/Australia add-on coverage.
    humanURL: https://www.theracingapi.com/
    baseURL: https://api.theracingapi.com
    tags:
      - Horse Racing
      - Sports
      - Statistics
      - Racecards
      - Results
      - Analytics
    properties:
      - type: Documentation
        url: https://api.theracingapi.com/documentation
      - type: OpenAPI
        url: openapi/the-racing-api-openapi.yml
      - type: Website
        url: https://www.theracingapi.com/
      - type: Authentication
        url: https://www.theracingapi.com/dashboard
      - type: JSONSchema
        url: json-schema/the-racing-api-racecard-summary-schema.json
        title: Racecard Summary Schema
      - type: JSONStructure
        url: json-structure/the-racing-api-racecard-summary-structure.json
        title: Racecard Summary Structure
      - type: JSON-LD
        url: json-ld/the-racing-api-context.jsonld
        title: The Racing API JSON-LD Context
common:
  - type: Website
    url: https://www.theracingapi.com/
  - type: Documentation
    url: https://api.theracingapi.com/documentation
  - type: Sign Up
    url: https://www.theracingapi.com/register
  - type: Dashboard
    url: https://www.theracingapi.com/dashboard
  - type: SpectralRules
    url: rules/the-racing-api-spectral-rules.yml
    title: The Racing API Spectral Rules
  - type: Vocabulary
    url: vocabulary/the-racing-api-vocabulary.yml
    title: The Racing API Vocabulary
  - type: NaftikoCapability
    url: capabilities/horse-racing-analytics.yaml
    title: Horse Racing Analytics
  - type: RateLimits
    url: https://api.theracingapi.com/documentation
    data:
      - name: Default Rate Limit
        description: 5 requests per second default rate limit; varies by endpoint
      - name: Plan-Based Limits
        description: Free, Standard, and Pro plans with different endpoint access levels
  - type: Authentication
    url: https://api.theracingapi.com/documentation
    data:
      - name: HTTP Basic Auth
        description: Username and password via HTTP Basic Authentication from the dashboard
  - type: Features
    data:
      - 'The Racing API: free public API'
      - 'Tiered pricing for horse racing data: Free / $19/mo / $59/mo / Enterprise.'
      - 'Public URL: https://theracingapi.com/'
    sources:
      - https://theracingapi.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Application Development
        description: Build horse racing applications and websites with live data
      - name: Statistical Modelling
        description: Develop betting models using historical results and real-time analysis
      - name: AI Agent Integration
        description: Feed racing data into AI agents for predictions and insights
      - name: Research and Analytics
        description: Perform academic and professional research on horse racing performance
  - type: Integrations
    data:
      - name: Claude AI
        description: Integration via remote MCP server for AI-powered racing insights
      - name: ChatGPT
        description: Integration via remote MCP server
      - name: Gemini
        description: Integration via remote MCP server
      - name: Grok
        description: Integration via remote MCP server
  - type: TermsOfService
    url: https://www.theracingapi.com/
  - type: Pricing
    url: https://www.theracingapi.com/
    data:
      - name: Free Plan
        description: Basic access to course listings and free racecards
      - name: Standard Plan
        description: Access to search endpoints and class/distance analysis
      - name: Pro Plan
        description: Full access including historical results and advanced analytics
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
