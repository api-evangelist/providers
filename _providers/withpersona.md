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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Withpersona Agentic Access
  operation_count: 49
  slug: withpersona-agentic-access
  summary_line: 49 operations · 25 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Persistent end-user records across Inquiries.
  name: Persona Accounts API
  slug: withpersona-accounts-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Grouped Persona objects for manual review.
  name: Persona Cases API
  slug: withpersona-cases-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Device-intelligence records.
  name: Persona Devices API
  slug: withpersona-devices-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Files collected during verification.
  name: Persona Documents API
  slug: withpersona-documents-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Immutable record of everything that happens in an account.
  name: Persona Events API
  slug: withpersona-events-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Bulk-load data into Persona lists.
  name: Persona Importers API
  slug: withpersona-importers-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Instances of an individual verifying their identity against a template.
  name: Persona Inquiries API
  slug: withpersona-inquiries-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Individual sessions within an Inquiry.
  name: Persona Inquiry Sessions API
  slug: withpersona-inquiry-sessions-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Watchlist, adverse-media, PEP, and business lookups.
  name: Persona Reports API
  slug: withpersona-reports-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Risk-scored events for ongoing fraud monitoring.
  name: Persona Transactions API
  slug: withpersona-transactions-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Individual identity checks (government ID, selfie, database, document, phone, email).
  name: Persona Verifications API
  slug: withpersona-verifications-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Webhook subscriptions that deliver Persona events.
  name: Persona Webhooks API
  slug: withpersona-webhooks-api
- baseURL: https://api.withpersona.com/api/v1
  baseurl_source: declared
  description: Automation runs triggered by verification results or events.
  name: Persona Workflows API
  slug: withpersona-workflows-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Persona Accounts API
  slug: open-withpersona-accounts-api
- collection_type: open
  name: Persona Accounts Cases API
  slug: open-withpersona-cases-api
- collection_type: open
  name: Persona Accounts Devices API
  slug: open-withpersona-devices-api
- collection_type: open
  name: Persona Accounts Documents API
  slug: open-withpersona-documents-api
- collection_type: open
  name: Persona Accounts Events API
  slug: open-withpersona-events-api
- collection_type: open
  name: Persona Accounts Importers API
  slug: open-withpersona-importers-api
- collection_type: open
  name: Persona Accounts Inquiries API
  slug: open-withpersona-inquiries-api
- collection_type: open
  name: Persona Accounts Inquiry Sessions API
  slug: open-withpersona-inquiry-sessions-api
- collection_type: open
  name: Persona Accounts Reports API
  slug: open-withpersona-reports-api
- collection_type: open
  name: Persona Accounts Transactions API
  slug: open-withpersona-transactions-api
- collection_type: open
  name: Persona Accounts Verifications API
  slug: open-withpersona-verifications-api
- collection_type: open
  name: Persona Accounts Webhooks API
  slug: open-withpersona-webhooks-api
- collection_type: open
  name: Persona Accounts Workflows API
  slug: open-withpersona-workflows-api
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
random_paper: 7
rate_limits:
- limit_count: 3
  name: Withpersona Rate Limits
  slug: withpersona-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/withpersona/refs/heads/main/screenshots/withpersona-2026-09-02T170853.png
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
