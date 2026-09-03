---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-03'
api_count: 7
apis:
- description: 'Place title and escrow orders programmatically (into Qualia Core or to third-party systems) and track their status through the closing lifecycle. Modeled from Qualia''s public description of push/pull '
  name: Qualia Title Orders API
  slug: qualia-title-orders-api
- description: Send and receive closing documents attached to an order - upload, retrieve, and share files across the parties on a file. Modeled from Qualia's stated document exchange capability; concrete operations
  name: Qualia Documents API
  slug: qualia-title-documents-api
- description: Send and receive messages tied to an order or transaction, powering client communication and status notifications alongside Qualia Connect. Modeled from Qualia's public messaging capability. endpoints
  name: Qualia Messages API
  slug: qualia-title-messages-api
- description: Pull contact and party data for the files on an account - the people and organizations attached to a closing - to sync with CRM systems and build custom notifications. Modeled from Qualia's stated con
  name: Qualia Contacts and Parties API
  slug: qualia-title-contacts-api
- description: Pull accounting and escrow data across files for custom reporting and executive-level performance dashboards, and to connect Qualia to accounting platforms (e.g. NetSuite) and BI tools. Modeled from Q
  name: Qualia Accounting and Escrow API
  slug: qualia-title-accounting-api
- description: Programmatic access to Qualia's national network of technology-enabled independent title agents and Marketplace vendors, letting businesses without internal title operations place and route orders dig
  name: Qualia Connect and Marketplace API
  slug: qualia-title-marketplace-api
- description: The Qualia API is a read-write GraphQL API over the Qualia title, escrow and closing platform. It lets partner organizations place title orders into Qualia Core or Connect (or route them to third-part
  name: Qualia API
  slug: qualia-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/qualia-title-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qualia-title-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qualia-title-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qualiasoftware
- group: company
  title: ''
  type: Website
  url: https://www.qualia.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.qualia.com/qualia-api/
- group: learn
  title: ''
  type: LearningResources
  url: https://learn.qualia.com/api-u
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qualia.com/api-terms/
- group: commercial
  title: ''
  type: Plans
  url: plans/qualia-title-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qualia-title-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.qualia.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qualialabs
created: '2026-07-04'
description: Qualia is a digital real estate closing platform for the title, escrow, and settlement industry, connecting title agents, lenders, real estate agents, and homebuyers on a single system for managing closings end to end. The Qualia API is an enterprise-grade, cloud-based GraphQL read-write API with a developer hub and sandbox. It lets real estate businesses and PropTech companies place and track title orders, send and receive messages and documents, and pull order, accounting, and contact data for custom reporting and to connect accounting, CRM, and BI systems. Access is partner-gated behind a secure authorization framework (capability gates, authorized organizations, HTTP authentication, and rate limiting); Qualia does not publish an open, unauthenticated developer portal, so the API areas below are modeled from Qualia's public product and press material rather than from a public GraphQL schema.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qualia-title.png
layout: provider
modified: '2026-07-25'
name: Qualia
nav: Providers
network: true
overview: 'Qualia publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Title Insurance, Escrow, Real-Estate, Closing, and Settlement.


  Qualia''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Qualia Title Plans Pricing
  plan_count: 1
  slug: qualia-title-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Qualia Title Rate Limits
  slug: qualia-title-rate-limits
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 40.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qualia-title/refs/heads/main/screenshots/qualia-title-2026-09-02T152559.png
security:
- kind: domain-security
  name: Qualia Title Domain Security
  slug: qualia-title-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qualia Title Vulnerability Disclosure
  slug: qualia-title-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Qualia Title Trust Center
  slug: qualia-title-trust-center
  summary_line: SOC 2, ISO 27001
slug: qualia-title
tags:
- Title Insurance
- Escrow
- Real-Estate
- Closing
- Settlement
- PropTech
- GraphQL
website: https://www.qualia.com
---
