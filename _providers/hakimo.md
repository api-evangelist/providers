---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.hakimo.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.hakimo.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hakimo.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.hakimo.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hakimo-ai
- group: start
  title: ''
  type: Login
  url: https://portal.hakimo.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hakimo
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hakimo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hakimo-domain-security.yml
coverage:
  checked: '2026-08-22'
  detail: Hakimo's only API is the same-origin backend of its customer portal at https://portal.hakimo.ai/v2/orm/, which answers unauthenticated requests with HTTP 401 {"message":"Invalid token"} behind a dedicated Auth0 tenant — there is no developer portal, no API reference and no /pricing page anywhere on hakimo.ai, so the contract is reachable only by an existing tenant.
  evidence:
  - status: 401
    url: https://portal.hakimo.ai/v2/orm/user/profile
  - status: 522
    url: https://support.hakimo.ai/
  - status: 404
    url: https://www.hakimo.ai/.well-known/api-catalog
  - status: 404
    url: https://www.hakimo.ai/pricing
  reason: customer-only-docs
  state: gated
created: '2026-08-22'
description: 'Hakimo is a Menlo Park, California physical-security software company founded by Stanford AI researchers Sam Joseph and Sagar Honnungar. Its AI platform sits on top of a customer''s existing camera, NVR/VMS and access-control estate and turns it into an autonomous security operations capability: the AI Operator triages alarms and assigns a true-alarm probability, remote guarding and SOC-as-a-Service provide 24/7 monitored response, and forensic search, weapon detection, facial recognition, an insights dashboard and a mobile app round out the product line. Hakimo integrates with roughly forty third-party systems (Genetec, Milestone, Avigilon, LenelS2, Eagle Eye Networks, Axis, ServiceNow, Slack, Microsoft Teams, ONVIF devices) by consuming those vendors'' APIs. As of August 2026 Hakimo publishes no public developer program of its own: there is no developer portal, no API reference, no OpenAPI or other machine-readable contract, and no SDK. Its tenant application API is served
  same-origin from the customer portal and answers unauthenticated requests with HTTP 401.'
image: https://cdn.prod.website-files.com/622f8e0fdb05fd4848ac6e54/67e54813882a3277300d6605_Updated%20OG%20Image%20(1).jpg
layout: provider
modified: '2026-08-22'
name: Hakimo
nav: Providers
network: true
overview: 'Hakimo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Physical Security, Video Surveillance, Access Control, and Artificial Intelligence.


  Hakimo''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Hakimo Plans Pricing
  plan_count: 0
  slug: hakimo-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Hakimo Rate Limits
  slug: hakimo-rate-limits
score:
  band: minimal
  composite: 10.9
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Hakimo Authentication
  slug: hakimo-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hakimo Domain Security
  slug: hakimo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hakimo
tags:
- Company
- Physical Security
- Video Surveillance
- Access Control
- Artificial Intelligence
- Computer Vision
- Security Operations
- Remote Guarding
- Alarm Monitoring
- Facility Management
website: https://www.hakimo.ai/
---
