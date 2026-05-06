---
aid: huginn
name: Huginn
description: Huginn is an open-source system for building agents that perform automated tasks online. Self-hosted agents can monitor the web, send and receive events, and trigger workflows. Each Huginn instance exposes a JSON-based HTTP interface (the Web Requests API) that lets external systems trigger scenarios and post events into the platform.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agents
  - Automation
  - Open Source
  - Self-Hosted
  - Workflow Automation
url: https://raw.githubusercontent.com/api-evangelist/huginn/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: huginn:huginn-platform
    name: Huginn Platform
    description: The Huginn platform is a self-hosted Ruby on Rails application that orchestrates agents, scenarios, and events. Operators install and run their own instance and configure agents to consume and produce events across the web.
    humanURL: https://github.com/huginn/huginn
    tags:
      - Agents
      - Self-Hosted
      - Workflow Automation
    properties:
      - type: Documentation
        url: https://github.com/huginn/huginn/wiki
      - type: GitHub Repository
        url: https://github.com/huginn/huginn
      - type: Installation Guide
        url: https://github.com/huginn/huginn/blob/master/doc/manual/installation.md
      - type: Docker
        url: https://hub.docker.com/r/huginn/huginn
  - aid: huginn:huginn-web-requests-api
    name: Huginn Web Requests API
    description: Each Huginn instance exposes a Web Requests endpoint that lets external systems POST or GET events into a configured Webhook Agent. The endpoint lives at /users/{user_id}/web_requests/{agent_id}/{secret} on the operator's installed instance and is the primary inbound integration surface for Huginn.
    humanURL: https://github.com/huginn/huginn/wiki
    tags:
      - Agents
      - Webhooks
    properties:
      - type: Documentation
        url: https://github.com/huginn/huginn/wiki
      - type: Webhook Agent
        url: https://github.com/huginn/huginn/blob/master/app/models/agents/webhook_agent.rb
common:
  - type: Website
    url: https://github.com/huginn/huginn
  - type: Documentation
    url: https://github.com/huginn/huginn/wiki
  - type: GitHub Repository
    url: https://github.com/huginn/huginn
  - type: License
    url: https://github.com/huginn/huginn/blob/master/LICENSE
  - type: Issues
    url: https://github.com/huginn/huginn/issues
  - type: Rules
    url: https://raw.githubusercontent.com/api-evangelist/huginn/refs/heads/main/huginn-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
