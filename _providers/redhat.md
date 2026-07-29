---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'REST API surface for the Red Hat Hybrid Cloud Console at console.redhat.com providing access to inventory, insights, patch, vulnerability, notifications, RBAC, sources, and other cloud services. Uses '
  name: Red Hat Hybrid Cloud Console API
  slug: hybrid-cloud-console
- description: REST API for managing Red Hat subscriptions, allocations, manifests, and usage reporting via Subscription Services in the Hybrid Cloud Console. Uses OAuth 2.0 / OIDC-compatible service account tokens.
  name: Red Hat Subscription Management API
  slug: subscription-management
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/redhat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redhat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redhat.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redhat.com
- group: docs
  title: ''
  type: API Documentation
  url: https://console.redhat.com/docs/api
- group: start
  title: ''
  type: Customer Portal
  url: https://access.redhat.com
- group: start
  title: ''
  type: Hybrid Cloud Console
  url: https://console.redhat.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redhat.com/en/store
- group: start
  title: ''
  type: Signup
  url: https://www.redhat.com/wapps/ugc/register.html
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RedHatOfficial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/red-hat
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/blog/rss.xml
created: '2026-05-11'
description: Red Hat is an IBM subsidiary providing enterprise open source software including Red Hat Enterprise Linux, OpenShift, and Ansible Automation Platform, with cloud services managed through the Red Hat Hybrid Cloud Console. The Hybrid Cloud Console exposes REST APIs for subscription management, system inventory, vulnerability and patch management, notifications, RBAC, and other cloud services across hybrid environments. APIs use token-based authentication via service accounts (OAuth 2.0 / OIDC) following Red Hat's transition away from basic authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redhat.png
layout: provider
modified: '2026-05-11'
name: Red Hat
nav: Providers
network: true
overview: 'Red Hat publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Red Hat, Hybrid Cloud, Subscription Management, Enterprise Linux, and OpenShift.


  Red Hat''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 14.0
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redhat/refs/heads/main/screenshots/redhat-2026-06-20T192726.png
security:
- kind: domain-security
  name: Redhat Domain Security
  slug: redhat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Redhat Vulnerability Disclosure
  slug: redhat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: redhat
tags:
- Red Hat
- Hybrid Cloud
- Subscription Management
- Enterprise Linux
- OpenShift
- Cloud Services
- IBM
website: https://www.redhat.com
---
