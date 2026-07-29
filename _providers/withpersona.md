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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Withpersona Agentic Access
  operation_count: 49
  slug: withpersona-agentic-access
  summary_line: 49 operations · 25 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Persistent end-user records across Inquiries.
  name: Persona Accounts API
  slug: withpersona-accounts-api
- description: Grouped Persona objects for manual review.
  name: Persona Cases API
  slug: withpersona-cases-api
- description: Device-intelligence records.
  name: Persona Devices API
  slug: withpersona-devices-api
- description: Files collected during verification.
  name: Persona Documents API
  slug: withpersona-documents-api
- description: Immutable record of everything that happens in an account.
  name: Persona Events API
  slug: withpersona-events-api
- description: Bulk-load data into Persona lists.
  name: Persona Importers API
  slug: withpersona-importers-api
- description: Instances of an individual verifying their identity against a template.
  name: Persona Inquiries API
  slug: withpersona-inquiries-api
- description: Individual sessions within an Inquiry.
  name: Persona Inquiry Sessions API
  slug: withpersona-inquiry-sessions-api
- description: Watchlist, adverse-media, PEP, and business lookups.
  name: Persona Reports API
  slug: withpersona-reports-api
- description: Risk-scored events for ongoing fraud monitoring.
  name: Persona Transactions API
  slug: withpersona-transactions-api
- description: Individual identity checks (government ID, selfie, database, document, phone, email).
  name: Persona Verifications API
  slug: withpersona-verifications-api
- description: Webhook subscriptions that deliver Persona events.
  name: Persona Webhooks API
  slug: withpersona-webhooks-api
- description: Automation runs triggered by verification results or events.
  name: Persona Workflows API
  slug: withpersona-workflows-api
artifact_total: 21
collections:
- collection_type: open
  name: Persona API
  slug: open-withpersona
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/withpersona-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/withpersona-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/withpersona-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/withpersona-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/persona-id
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/withpersona
- group: company
  title: ''
  type: Website
  url: https://withpersona.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withpersona.com
- group: commercial
  title: ''
  type: Plans
  url: plans/withpersona-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/withpersona-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/withpersona-finops.yml
created: '2026-07-01'
description: Persona (withpersona.com) is a configurable identity platform for KYC, KYB, AML, and fraud prevention. Its JSON:API-style REST API lets organizations run identity Inquiries, collect Verifications (government ID, selfie, database, document, phone, and email), pull watchlist and adverse-media Reports, manage review Cases, score Transactions, and orchestrate Workflows, all under api.withpersona.com/api/v1.
finops:
- name: Withpersona Finops
  service_category: Identity and Compliance
  slug: withpersona-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/withpersona.png
layout: provider
modified: '2026-07-01'
name: Persona
nav: Providers
network: true
overview: 'Persona publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Cases API, Devices API, and 10 more. Tagged areas include Identity, Identity Verification, KYC, KYB, and AML.


  Persona''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Withpersona Plans Pricing
  plan_count: 4
  slug: withpersona-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Withpersona Rate Limits
  slug: withpersona-rate-limits
score:
  band: thin
  composite: 37.1
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Withpersona Authentication
  slug: withpersona-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Withpersona Domain Security
  slug: withpersona-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Withpersona Vulnerability Disclosure
  slug: withpersona-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: withpersona
tags:
- Identity
- Identity Verification
- KYC
- KYB
- AML
- Fraud
- Compliance
website: https://withpersona.com
---
