---
aid: incident-io
name: Incident.io
description: incident.io is an incident management platform that helps teams declare, manage, and learn from incidents.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AIOps
  - Incident Management
url: https://raw.githubusercontent.com/api-evangelist/incident-io/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: incident-io:incident-io
    name: Incident.io
    description: incident.io is an incident management platform that helps teams declare, manage, and learn from incidents.
    humanURL: https://incident.io
    tags:
      - AIOps
    properties:
      - type: Documentation
        url: https://api-docs.incident.io
common:
  - type: Website
    url: https://incident.io
  - type: Documentation
    url: https://api-docs.incident.io
  - type: Features
    data:
      - 'Basic: free Slack/MS Teams native incident response'
      - 'Team: $15/user/mo annual + $10/user for on-call'
      - 'Pro: $25/user/mo + $20/user for on-call; AI Scribe, SSO/SAML'
      - 'Enterprise: custom; Slack Enterprise Grid, Sandbox, CSM'
      - 'On-Call only: $20/user/mo standalone alerting'
      - Slack-native and MS Teams-native flow
      - AI suggestions for incident triage
      - AI Scribe for post-mortem writing (Pro+)
      - Status pages (public + internal)
      - Workflows for automation
      - Heartbeats for synthetic monitoring
      - REST API at api.incident.io
      - Default 600 req/min/org
      - Webhook delivery + Catalog API
      - OAuth 2.0 + Bearer tokens
      - Live call routing for paged engineers
    sources:
      - https://incident.io/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
