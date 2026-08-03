---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The real, documented programmatic surface. VidCruiter provisions each institution a unique web-services API endpoint (obtained from a VidCruiter account representative) used for bidirectional integrat
  name: VidCruiter Partner Integration API
  slug: vidcruiter-partner-integration-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vidcruiter-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vidcruiter
- group: company
  title: ''
  type: Website
  url: https://vidcruiter.com
- group: docs
  title: ''
  type: Documentation
  url: https://vidcruiter.com/integrations/
- group: commercial
  title: ''
  type: Plans
  url: plans/vidcruiter-plans-pricing.yml
created: '2026-07-10'
description: 'VidCruiter is a Moncton, Canada based recruitment technology company that provides a modular hiring platform - pre-recorded and live video interviewing, automated interview scheduling, skills and pre-employment testing, automated reference checking, audio interviews, and video proctoring. VidCruiter does not publish a public, self-service developer API. Its programmatic surface is a partner and enterprise integration capability: pre-built connectors to major ATS/HCM, background-check, calendar, job-board, SSO, and video-conferencing providers, plus a bidirectional web-services integration in which an institution''s unique, account-provisioned API endpoint is exchanged with a system of record (for example Slate) to push application records into VidCruiter and pull completed interview results back out. API access is gated behind a VidCruiter account representative; there is no public API reference, OpenAPI document, base URL, or self-serve key issuance.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vidcruiter.png
layout: provider
modified: '2026-07-25'
name: VidCruiter
nav: Providers
network: true
overview: 'VidCruiter publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Recruitment, Video Interviewing, Hiring, HR Tech, and Applicant Tracking.


  VidCruiter''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Vidcruiter Plans Pricing
  plan_count: 1
  slug: vidcruiter-plans-pricing
random_paper: 44
score:
  band: minimal
  composite: 11.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Vidcruiter Domain Security
  slug: vidcruiter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vidcruiter
tags:
- Recruitment
- Video Interviewing
- Hiring
- HR Tech
- Applicant Tracking
- ATS Integration
- Candidate Screening
- Reference Checking
website: https://vidcruiter.com
---
