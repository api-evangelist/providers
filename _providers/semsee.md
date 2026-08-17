---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_access: false
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
  score: 19.4
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: 'Partner-gated Upload/Download integration that pushes ACORD-based application and submission data from an agency management system (AMS) into the Semsee platform for multi-carrier quoting. No public, '
  name: Semsee Submissions API
  slug: semsee-submissions-api
- description: Partner-gated download of multi-carrier quote results back into an AMS or commercial rater so agents can compare and bind without re-keying. No public endpoint, schema, or base URL is published; acces
  name: Semsee Quotes API
  slug: semsee-quotes-api
- description: Carrier and MGA connectivity through which Semsee routes submissions to 50+ markets via carrier API and RPA integrations, including class-code and market-appetite matching. This is internal platform c
  name: Semsee Carriers API
  slug: semsee-carriers-api
- description: No public webhook or event-notification surface is documented by Semsee. This entry is a placeholder reflecting that event-driven callbacks, if they exist, are part of a private partner integration an
  name: Semsee Webhooks API
  slug: semsee-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Semsee API
  slug: open-semsee
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/semsee-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/semsee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semsee-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/semsee
- group: company
  title: ''
  type: Website
  url: https://www.semsee.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.semsee.com
- group: commercial
  title: ''
  type: Plans
  url: plans/semsee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/semsee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/semsee-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://semsee.com/blog/rss.xml
created: '2026-06-25'
description: Semsee is a digital small-commercial insurance quoting platform built on the SEMCI (Single Entry, Multiple Company Interface) principle, connecting independent agents to 50+ carriers and MGAs across multiple lines of business via API and RPA integrations. The platform handles submissions, multi-carrier quoting, proposals, and binding. Semsee exposes a partner Upload/Download (AMS) integration capability and SSO rather than a public, self-serve developer API. Semsee was acquired by iBynd in March 2026.
finops:
- name: Semsee Finops
  service_category: Insurance Technology
  slug: semsee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semsee.png
layout: provider
modified: '2026-06-25'
name: Semsee
nav: Providers
network: true
overview: 'Semsee publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Submissions API, Quotes API, Carriers API, and 1 more. Tagged areas include Insurance, Insurtech, Commercial Insurance, Quoting, and Submissions.


  Semsee''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Semsee Plans Pricing
  plan_count: 3
  slug: semsee-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 1
  name: Semsee Rate Limits
  slug: semsee-rate-limits
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 28.4
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Semsee Domain Security
  slug: semsee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Semsee Vulnerability Disclosure
  slug: semsee-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Semsee Trust Center
  slug: semsee-trust-center
  summary_line: SOC 2, GDPR
slug: semsee
tags:
- Insurance
- Insurtech
- Commercial Insurance
- Quoting
- Submissions
website: https://www.semsee.com
---
