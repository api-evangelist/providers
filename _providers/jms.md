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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Jakarta Messaging (formerly Java Message Service) specification for enterprise messaging and asynchronous communication between distributed components. Defines point-to-point queues and publish/su
  name: Jakarta Messaging
  slug: jms
artifact_total: 5
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/jakartaee/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/jakartaee/messaging/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jakarta.ee/specifications/messaging/
- group: docs
  title: ''
  type: Documentation
  url: https://jakarta.ee/specifications/messaging/3.1/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jakartaee
- group: operate
  title: ''
  type: Issues
  url: https://github.com/jakartaee/messaging/issues
created: '2025-01-01'
description: Java Message Service (JMS), now known as Jakarta Messaging, is a Java API that allows applications to create, send, receive, and read messages. It defines a common enterprise messaging API for loosely coupled, reliable, and asynchronous communication between distributed application components. Current release is Jakarta Messaging 3.1 (Jakarta EE 10).
finops:
- name: Jms Finops
  service_category: API
  slug: jms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jms.png
layout: provider
modified: '2026-04-28'
name: JMS
nav: Providers
network: true
overview: 'JMS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise Integration, Jakarta EE, Java, JMS, and Messaging.


  JMS''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Jms Plans Pricing
  plan_count: 3
  slug: jms-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Jms Rate Limits
  slug: jms-rate-limits
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 40.0
  previous_composite: 12.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jms/refs/heads/main/screenshots/jms-2026-06-20T183740.png
security:
- kind: domain-security
  name: Jms Domain Security
  slug: jms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jms
tags:
- Enterprise Integration
- Jakarta EE
- Java
- JMS
- Messaging
- Standard
website: https://jakarta.ee/specifications/messaging/
---
