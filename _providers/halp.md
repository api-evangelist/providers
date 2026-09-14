---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://halp.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.atlassian.com/software/jira/service-management/help-desk-software-small-business-software — a different registrable domain (halp.com -> atlassian.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halp-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/halp-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/halp-security.txt
- group: company
  title: ''
  type: Website
  url: https://halp.com/
created: '2026-07-17'
description: Halp was a conversational ticketing and help-desk tool that let teams turn Slack and Microsoft Teams messages into trackable tickets, founded in Boulder, Colorado and backed by Techstars. Atlassian acquired Halp in February 2020 and folded its capabilities into Jira Service Management; the standalone Halp product and its API were subsequently discontinued. The halp.com domain now resolves to Atlassian and is served from Atlassian's edge, so no independent Halp developer portal, API reference, SDKs, or MCP surface remains to enrich. This profile records the company's history and the (Atlassian-operated) security posture still observable on the halp.com domain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/halp.png
layout: provider
modified: '2026-07-19'
name: Halp
nav: Providers
network: true
overview: Halp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Help Desk, Ticketing, Customer-Support, and Slack.
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/halp/refs/heads/main/screenshots/halp-2026-07-25T220553.png
security:
- kind: domain-security
  name: Halp Domain Security
  slug: halp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: halp
tags:
- Company
- Help Desk
- Ticketing
- Customer-Support
- Slack
- Microsoft Teams
- Conversational
- Acquired
website: https://halp.com/
---
