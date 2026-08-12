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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Dub Agentic Access
  operation_count: 54
  slug: dub-agentic-access
  summary_line: 54 operations · 35 acting
api_count: 18
apis:
- description: Retrieve analytics and event data for links and workspaces including click counts, conversion events (leads and sales), geographic breakdowns, device information, and referrer tracking.
  name: Dub Analytics API
  slug: analytics
- description: Create and manage affiliate partners, partner groups, and partner tags. Supports payout management and advanced reward structures including geo-specific, product-specific, and performance-based reward
  name: Dub Partners API
  slug: partners
- description: List and manage custom domains associated with a Dub workspace, including SSL certificate provisioning and free .link domain support.
  name: Dub Domains API
  slug: domains
- description: The Analytics API from Dub — 1 operation(s) for analytics.
  name: Dub Analytics API
  slug: dub-analytics-api
- description: The Bounties API from Dub — 3 operation(s) for bounties.
  name: Dub Bounties API
  slug: dub-bounties-api
- description: The Commissions API from Dub — 3 operation(s) for commissions.
  name: Dub Commissions API
  slug: dub-commissions-api
- description: The Customers API from Dub — 2 operation(s) for customers.
  name: Dub Customers API
  slug: dub-customers-api
- description: The Domains API from Dub — 4 operation(s) for domains.
  name: Dub Domains API
  slug: dub-domains-api
- description: The Embed Tokens API from Dub — 1 operation(s) for embed tokens.
  name: Dub Embed Tokens API
  slug: dub-embed-tokens-api
- description: The Events API from Dub — 1 operation(s) for events.
  name: Dub Events API
  slug: dub-events-api
- description: The Folders API from Dub — 2 operation(s) for folders.
  name: Dub Folders API
  slug: dub-folders-api
- description: The Links API from Dub — 6 operation(s) for links.
  name: Dub Links API
  slug: dub-links-api
- description: The Partner Applications API from Dub — 3 operation(s) for partner applications.
  name: Dub Partner Applications API
  slug: dub-partner-applications-api
- description: The Partners API from Dub — 6 operation(s) for partners.
  name: Dub Partners API
  slug: dub-partners-api
- description: The Payouts API from Dub — 1 operation(s) for payouts.
  name: Dub Payouts API
  slug: dub-payouts-api
- description: The QR Codes API from Dub — 1 operation(s) for qr codes.
  name: Dub QR Codes API
  slug: dub-qr-codes-api
- description: The Tags API from Dub — 2 operation(s) for tags.
  name: Dub Tags API
  slug: dub-tags-api
- description: The Track API from Dub — 3 operation(s) for track.
  name: Dub Track API
  slug: dub-track-api
artifact_total: 52
collections:
- collection_type: postman
  name: Dub Analytics API
  slug: postman-dub-analytics-api
- collection_type: postman
  name: Dub Analytics Bounties API
  slug: postman-dub-bounties-api
- collection_type: postman
  name: Dub Analytics Commissions API
  slug: postman-dub-commissions-api
- collection_type: postman
  name: Dub Analytics Customers API
  slug: postman-dub-customers-api
- collection_type: postman
  name: Dub Analytics Domains API
  slug: postman-dub-domains-api
- collection_type: postman
  name: Dub Analytics Embed Tokens API
  slug: postman-dub-embed-tokens-api
- collection_type: postman
  name: Dub Analytics Events API
  slug: postman-dub-events-api
- collection_type: postman
  name: Dub Analytics Folders API
  slug: postman-dub-folders-api
- collection_type: postman
  name: Dub Analytics Links API
  slug: postman-dub-links-api
- collection_type: postman
  name: Dub Analytics Partner Applications API
  slug: postman-dub-partner-applications-api
- collection_type: postman
  name: Dub Analytics Partners API
  slug: postman-dub-partners-api
- collection_type: postman
  name: Dub Analytics Payouts API
  slug: postman-dub-payouts-api
- collection_type: postman
  name: Dub Analytics QR Codes API
  slug: postman-dub-qr-codes-api
- collection_type: postman
  name: Dub Analytics Tags API
  slug: postman-dub-tags-api
- collection_type: postman
  name: Dub Analytics Track API
  slug: postman-dub-track-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dub/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dub-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dub-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dub-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://dub.co
- group: docs
  title: ''
  type: Documentation
  url: https://dub.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dub.co/docs/api-reference/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dubinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dubinc
- group: other
  title: ''
  type: X
  url: https://x.com/dubdotco
- group: company
  title: ''
  type: Blog
  url: https://dub.co/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://dub.co/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://dub.co/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dub.co
- group: build
  title: ''
  type: SDKTypeScript
  url: https://github.com/dubinc/dub-ts
- group: build
  title: ''
  type: SDKPython
  url: https://github.com/dubinc/dub-python
- group: build
  title: ''
  type: SDKGo
  url: https://github.com/dubinc/dub-go
- group: build
  title: ''
  type: SDKRuby
  url: https://github.com/dubinc/dub-ruby
- group: build
  title: ''
  type: SDKPHP
  url: https://github.com/dubinc/dub-php
- group: commercial
  title: ''
  type: Plans
  url: plans/dub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dub-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dub-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/dub-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/dub-folder-schema.json
created: '2026-06-12'
description: Dub is an open-source link attribution platform for creating short links, QR codes, and managing affiliate programs. It provides a REST API that allows developers to programmatically create and manage links, track conversion events (clicks, leads, and sales), retrieve analytics, and manage workspaces and custom domains. Dub powers over 100 million clicks and 2 million links monthly for marketing teams at companies like Vercel, Perplexity, Twilio, and Framer. The platform offers native SDKs in TypeScript, Python, Go, Ruby, and PHP, along with mobile SDKs for iOS and React Native.
examples:
- key_count: 4
  name: Dub Analytics Response Example
  slug: dub-analytics-response-example
- key_count: 16
  name: Dub Create Link Example
  slug: dub-create-link-example
- key_count: 41
  name: Dub Link Response Example
  slug: dub-link-response-example
- key_count: 7
  name: Dub Track Sale Example
  slug: dub-track-sale-example
finops:
- name: Dub Finops
  service_category: SaaS / Link Management
  slug: dub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dub.png
json_schemas:
- name: AnalyticsCount
  property_count: 4
  slug: dub-analyticscount
- name: AnalyticsTimeseries
  property_count: 5
  slug: dub-analyticstimeseries
- name: DomainSchema
  property_count: 14
  slug: dub-domain
- name: FolderSchema
  property_count: 7
  slug: dub-folder
- name: Link
  property_count: 51
  slug: dub-link
jsonld:
- class_count: 45
  name: Dub Context
  property_count: 23
  slug: dub-context
layout: provider
modified: '2026-06-12'
name: Dub
nav: Providers
network: true
overview: 'Dub publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Bounties API, Commissions API, and 12 more. Tagged areas include Link Management, URL Shortener, Analytics, Conversion Tracking, and Affiliate Programs.


  The Dub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dub''s developer surface includes authentication, documentation, API reference, engineering blog, changelog, pricing, and 21 more developer resources.'
plans:
- name: Dub Plans Pricing
  plan_count: 5
  slug: dub-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 8
  name: Dub Rate Limits
  slug: dub-rate-limits
rules:
- name: Dub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dub-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.1
  delta: -0.8
  facets:
    commercial_clarity: 57.9
    contract_quality: 77.8
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 62.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dub/refs/heads/main/screenshots/dub-2026-06-20T180305.png
security:
- kind: authentication
  name: Dub Authentication
  slug: dub-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dub Domain Security
  slug: dub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dub Vulnerability Disclosure
  slug: dub-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dub Trust Center
  slug: dub-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: dub
tags:
- Link Management
- URL Shortener
- Analytics
- Conversion Tracking
- Affiliate Programs
- Open Source
website: https://dub.co
---
