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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
asyncapis:
- description: Generated AsyncAPI view of GovDash's documented outbound webhook events for Opportunity lifecycle changes. Event names, delivery mechanism (Svix), and signature verification are taken verbatim from ht
  name: GovDash Webhooks
  slug: govdash-webhooks-asyncapi
- description: ''
  name: Govdash Webhooks
  slug: govdash-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://govdash.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.govdash.com/docs
- group: operate
  title: ''
  type: Support
  url: https://support.govdash.com
- group: company
  title: ''
  type: Blog
  url: https://www.govdash.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.govdash.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.govdash.com/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://dashboard.govdash.us/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.govdash.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.govdash.com/pages/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.govdash.com/vulnerability-report
- group: auth
  title: ''
  type: Compliance
  url: https://www.govdash.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/govdash-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/govdash-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/govdash-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/govdash-webhooks-asyncapi.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/govdash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/govdash-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/govdash-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govdash-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/govdash-lifecycle.yml
created: '2026-07-17'
description: GovDash is an end-to-end AI platform for government contracting (GovCon), helping companies discover, capture, price, propose, and manage federal, state, local, and education contracts. Its product suite spans Discover (automated bid matching from SAM.gov, GSA eBuy, GovWin, PIEE, and SLED portals), Capture (a GovCon CRM and pipeline), Pricer, Proposal (compliant proposal generation), and Contract lifecycle management, unified by Dash, an AI agent that synthesizes data and executes workflows. GovDash is FedRAMP Ready / Moderate-equivalent, NIST SP 800-53 and DFARS 252.204-7012 aligned for CUI, and integrates with Salesforce, SharePoint, Okta/Google SSO, Slack, and Microsoft Office. It exposes outbound webhooks (Svix) for opportunity lifecycle events. Founded 2021 (YC W22); raised a $30M Series B in January 2026.
image: https://www.govdash.com/opengraph-image?f0fc2d766b3d3aad
layout: provider
modified: '2026-07-19'
name: Govdash
nav: Providers
network: true
overview: 'Govdash is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government Contracting, GovCon, Artificial Intelligence, and Proposal Management.


  The Govdash catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Govdash''s developer surface includes documentation, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 41.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govdash/refs/heads/main/screenshots/govdash-2026-07-25T220126.png
security:
- kind: domain-security
  name: Govdash Domain Security
  slug: govdash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Govdash Vulnerability Disclosure
  slug: govdash-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Govdash Trust Center
  slug: govdash-trust-center
  summary_line: FedRAMP Moderate Equivalency, FedRAMP Ready (fedramp.gov Marketplace), NIST SP 800-53 (Moderate baseline aligned), DFARS 252.204-7012, CMMC (referenced)
slug: govdash
tags:
- Company
- Government Contracting
- GovCon
- Artificial Intelligence
- Proposal Management
- Capture Management
- Public Sector
- Enterprise
website: https://govdash.com
---
