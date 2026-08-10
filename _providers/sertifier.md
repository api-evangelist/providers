---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 30
  human_in_the_loop: 1
  name: Sertifier Agentic Access
  operation_count: 37
  slug: sertifier-agentic-access
  summary_line: 37 operations · 30 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Reusable custom key/value fields merged into credentials.
  name: Sertifier Attributes API
  slug: sertifier-attributes-api
- description: Verify API key validity.
  name: Sertifier Authentication API
  slug: sertifier-authentication-api
- description: Containers that bind a Design, Detail, and Email Template and issue credentials.
  name: Sertifier Campaigns API
  slug: sertifier-campaigns-api
- description: Individual issued credentials - retrieve, update, publish, and generate PDF links.
  name: Sertifier Credentials API
  slug: sertifier-credentials-api
- description: Visual designs applied to certificates and badges.
  name: Sertifier Designs API
  slug: sertifier-designs-api
- description: Descriptive metadata (title, skills, criteria) printed on a credential.
  name: Sertifier Details API
  slug: sertifier-details-api
- description: Templates used to deliver finished credentials to recipients.
  name: Sertifier Email Templates API
  slug: sertifier-email-templates-api
- description: Learners who receive credentials.
  name: Sertifier Recipients API
  slug: sertifier-recipients-api
- description: MODELED - inbound/outbound event automation. Not confirmed in the public reference.
  name: Sertifier Webhooks API
  slug: sertifier-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: Sertifier Credential API
  slug: open-sertifier
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sertifier-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sertifier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sertifier-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sertifierco
- group: company
  title: ''
  type: Website
  url: https://sertifier.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sertifier.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/sertifier-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sertifier-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sertifier-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sertifier.com/blog/
created: '2026-07-05'
description: Sertifier is a digital credential and certificate/badge management platform that lets organizations design, issue, verify, and analyze verifiable digital credentials (Open Badge-style certificates and badges) at scale. Beyond the web application, Sertifier exposes a REST Credential API (base https://b2b.sertifier.com, authenticated with a private secretKey header and an api-version header) so backend systems and LMS/CRM integrations can programmatically manage designs, credential details, email templates, campaigns, recipients, custom attributes, and issue and publish credentials the instant a learner completes a course. Sertifier has issued more than 10 million credentials across 70+ countries.
finops:
- name: Sertifier Finops
  service_category: Digital Credentialing and Certificates
  slug: sertifier-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sertifier.png
layout: provider
modified: '2026-07-05'
name: Sertifier
nav: Providers
network: true
overview: 'Sertifier publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Authentication API, Campaigns API, and 6 more. Tagged areas include Digital Credentials, Certificates, Badges, Open Badges, and Verifiable Credentials.


  Sertifier''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Sertifier Plans Pricing
  plan_count: 4
  slug: sertifier-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 3
  name: Sertifier Rate Limits
  slug: sertifier-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Sertifier Authentication
  slug: sertifier-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sertifier Domain Security
  slug: sertifier-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sertifier
tags:
- Digital Credentials
- Certificates
- Badges
- Open Badges
- Verifiable Credentials
- Credentialing
- EdTech
website: https://sertifier.com
---
