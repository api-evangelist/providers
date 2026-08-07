---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Meet Agentic Access
  operation_count: 11
  slug: google-meet-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 3
apis:
- description: The conferenceRecords API from Google Meet — 7 operation(s) for conferencerecords.
  name: Google Meet conferenceRecords API
  slug: google-meet-conferencerecords-api
- description: The Google Meet API API from Google Meet — 2 operation(s) for google meet api.
  name: Google Meet Google Meet API API
  slug: google-meet-google-meet-api-api
- description: The Spaces API from Google Meet — 1 operation(s) for spaces.
  name: Google Meet Spaces API
  slug: google-meet-spaces-api
artifact_total: 14
collections:
- collection_type: open
  name: Google Meet API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-meet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-meet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-meet-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/meet/api/guides/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/meet/pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/feeds/posts/default/-/Google%20Meet
created: '2026-03-13'
description: The Google Meet API provides programmatic access to Google Meet video conferencing functionality. It enables applications to create and manage meeting spaces, retrieve conference records including participant details, access recordings and transcripts, and end active conferences. The API supports building integrations that automate meeting workflows and extract meeting data.
finops:
- name: Google Meet Finops
  service_category: API
  slug: google-meet-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Google Meet API, derived from the [Google Meet REST API v2](https://developers.google.com/meet/api/reference/rest/v2).
  name: Google Meet GraphQL Schema
  slug: google-meet-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-meet.png
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 6
  slug: json-ld
layout: provider
modified: '2026-05-19'
name: Google Meet
nav: Providers
network: true
overview: 'Google Meet publishes 3 APIs on the [APIs.io](https://apis.io/) network: conferenceRecords API, Google Meet API API, and Spaces API. Tagged areas include Google, Google Workspace, Meetings, Recordings, and Transcripts.


  The Google Meet catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Meet''s developer surface includes getting-started guide, pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Google Meet Plans Pricing
  plan_count: 3
  slug: google-meet-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Google Meet Rate Limits
  slug: google-meet-rate-limits
rules:
- name: Google Meet API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-meet-jsonschema-spectral-rules
- name: Google Meet API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 5
  slug: google-meet-spectral-rules
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.6
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-meet/refs/heads/main/screenshots/google-meet-2026-06-20T182215.png
security:
- kind: domain-security
  name: Google Meet Domain Security
  slug: google-meet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Meet Vulnerability Disclosure
  slug: google-meet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-meet
tags:
- Google
- Google Workspace
- Meetings
- Recordings
- Transcripts
- Video Conferencing
---
