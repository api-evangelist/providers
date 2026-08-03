---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chameleon Agentic Access
  operation_count: 33
  slug: chameleon-agentic-access
  summary_line: 33 operations
api_count: 18
apis:
- description: Chameleon REST API for managing user profiles, companies, tours, microsurveys, embeddables, segments, themes, webhooks, and other Experiences.
  name: Chameleon REST API
  slug: chameleon-rest-api
- description: The Alert Groups API from Chameleon — 2 operation(s) for alert groups.
  name: Chameleon Alert Groups API
  slug: chameleon-alert-groups-api
- description: The Companies API from Chameleon — 2 operation(s) for companies.
  name: Chameleon Companies API
  slug: chameleon-companies-api
- description: The Deliveries API from Chameleon — 2 operation(s) for deliveries.
  name: Chameleon Deliveries API
  slug: chameleon-deliveries-api
- description: The Domains API from Chameleon — 2 operation(s) for domains.
  name: Chameleon Domains API
  slug: chameleon-domains-api
- description: The Imports API from Chameleon — 2 operation(s) for imports.
  name: Chameleon Imports API
  slug: chameleon-imports-api
- description: The Interactions API from Chameleon — 2 operation(s) for interactions.
  name: Chameleon Interactions API
  slug: chameleon-interactions-api
- description: The Launchers API from Chameleon — 2 operation(s) for launchers.
  name: Chameleon Launchers API
  slug: chameleon-launchers-api
- description: The Limit Groups API from Chameleon — 2 operation(s) for limit groups.
  name: Chameleon Limit Groups API
  slug: chameleon-limit-groups-api
- description: The Microsurveys API from Chameleon — 2 operation(s) for microsurveys.
  name: Chameleon Microsurveys API
  slug: chameleon-microsurveys-api
- description: The Profiles API from Chameleon — 2 operation(s) for profiles.
  name: Chameleon Profiles API
  slug: chameleon-profiles-api
- description: The Properties API from Chameleon — 2 operation(s) for properties.
  name: Chameleon Properties API
  slug: chameleon-properties-api
- description: The Responses API from Chameleon — 1 operation(s) for responses.
  name: Chameleon Responses API
  slug: chameleon-responses-api
- description: The Segments API from Chameleon — 2 operation(s) for segments.
  name: Chameleon Segments API
  slug: chameleon-segments-api
- description: The Tags API from Chameleon — 2 operation(s) for tags.
  name: Chameleon Tags API
  slug: chameleon-tags-api
- description: The Tooltips API from Chameleon — 2 operation(s) for tooltips.
  name: Chameleon Tooltips API
  slug: chameleon-tooltips-api
- description: The Tours API from Chameleon — 2 operation(s) for tours.
  name: Chameleon Tours API
  slug: chameleon-tours-api
- description: The Webhooks API from Chameleon — 2 operation(s) for webhooks.
  name: Chameleon Webhooks API
  slug: chameleon-webhooks-api
artifact_total: 26
collections:
- collection_type: open
  name: Chameleon REST API
  slug: open-chameleon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chameleon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chameleon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chameleon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chameleon-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chameleon-io
- group: company
  title: ''
  type: Website
  url: https://www.chameleon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.chameleon.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/chameleon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chameleon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chameleon-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.chameleon.io/llms.txt
created: '2026-05-08'
description: Chameleon delivers in-app product tours, microsurveys, tooltips, launchers, and product demos to drive activation and feedback.
finops:
- name: Chameleon Finops
  service_category: Product
  slug: chameleon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chameleon.png
layout: provider
modified: '2026-05-08'
name: Chameleon
nav: Providers
network: true
overview: 'Chameleon publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Alert Groups API, Companies API, Deliveries API, and 14 more. Tagged areas include Product, In-App Guidance, Onboarding, Surveys, and Analytics.


  Chameleon''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Chameleon Plans Pricing
  plan_count: 1
  slug: chameleon-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 1
  name: Chameleon Rate Limits
  slug: chameleon-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 57.4
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chameleon/refs/heads/main/screenshots/chameleon-2026-06-20T174207.png
security:
- kind: authentication
  name: Chameleon Authentication
  slug: chameleon-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chameleon Domain Security
  slug: chameleon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Chameleon Trust Center
  slug: chameleon-trust-center
  summary_line: SOC 2, GDPR
slug: chameleon
tags:
- Product
- In-App Guidance
- Onboarding
- Surveys
- Analytics
website: https://www.chameleon.io/
---
